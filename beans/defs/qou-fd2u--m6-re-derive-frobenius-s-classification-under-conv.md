---
# qou-fd2u
title: 'M6: re-derive frobenius-s classification under convention D'
status: in-progress
type: task
priority: normal
created_at: 2026-10-10T08:52:03Z
updated_at: 2026-10-10T18:34:17Z
parent: qou-d8c7
---

frobenius-s-classification-proof.md:16 and table2-data:9 rest on z being invariant under q->1/q, true only for z_C. z_D(1/q0)=0.4036 vs z_D(q0)=0.6127. Classification must be re-derived under D (owner pick 3a, 2026-10-10: bean, not a restatement). Open research.


2026-10-10: under D, S maps z_D to 1/(q(q^2+1)) = z - h (sympy-verified), i.e. S swaps the two loop values. So Phi_1 = sum log|z a_i + b_i| needs re-derivation (its partner is sum log|(z-h) a_i + b_i|). Scope notes added to the proof and table2 on PR #7562.

Lean: frobenius-s-classification.lean:48 assigns z : SEigenvalue := .even, which is the C reading.

2026-10-10 (branch claude/frobenius-s-d-2026-10-10, commits 7e4e549fd / 6f47e2159 / eacdb322a). RE-DERIVED, partially.
(1) Which S: Table 3 fixes ud=(1,-h/2) only if S is the KL bar involution (q->1/q AND sigma->sigma^-1, coefficients barred); the q-fixed map (c,d)->(c,d-ch) sends ud to (1,-3h/2). Proof .md now says so.
(2) z_D(1/q) = 1/(q(q^2+1)) = z_D - h: Lean sorry-free over a generic field (zD_inv, zD_inv_eq_sub). Meaning: the D Markov trace COMMUTES with S (markov_bar_equivariant_zD; converse bar_equivariant_forces: equivariance forces z(1/q)=z-h; z=q also satisfies it). C is the opposite: z_C S-fixed, trace NOT equivariant (zC_not_bar_equivariant).
(3) Consequence: S acts on Phi_1 as the evaluation flip, Phi_1(S beta; q0) = Phi_1(beta; 1/q0) (probe, 7 chains, <1e-40). Raw Phi_1 is NOT an S-eigenvector in either convention; Table 1's +1 is the averaged projection Phi_1^+ only, true by construction.
(4) Phi_2 even, Phi_3 odd: confirmed on chains of the three primitives (z-free; dPhi2 = 0, Phi3+Phi3(S) ~ 1e-52).
(5) The classification's headline does NOT survive for the raw formula: m(S beta)-m(beta) = -2 alpha (Phi_1^- + h^2 Phi_3). Proton uud at proton pin, mpmath dps50: Phi_1^- = 0.0525921336, h^2 Phi_3 = 0.0091206746, ratio 5.766. (Excised C gives Phi_1^- = 0.0408, so C never had it either.) Proof corollary corrected.
(6) Lean FrobeniusClassification.z is now Option SEigenvalue := none (no consumers).
STILL OPEN: the statement .md (frobenius-s-classification.md) still says 'exactly one term is S-anti-invariant' and that S-symmetric ansatze 'cannot capture chirality'; both hold only if Phi_1 means Phi_1^+. Whether the mass formula should use Phi_1^+ (a formula change) or the claim should be restated is an owner decision. Also the Phi_3 '(-1)^n chi swap' argument in the proof checks only (1,0); the conclusion holds on primitive chains via bar(ratio)=1/ratio, but the written argument was not repaired. Not closeable.

## 2026-10-10 — owner pick applied: keep raw Phi_1, restate the claim (branch claude/tmvac-fd2u-owner-picks-2026-10-10, 0f138506d)

Statement .md: Phi_1 has no S-eigenvalue (only Phi_1^+ is S-even); term 1 shown as Phi_1^+ + Phi_1^-; the S-odd part has two channels, m(S beta) - m(beta) = -2 alpha (Phi_1^- + h^2 Phi_3); chirality is the only S-odd channel iff alpha Phi_1^- = 0. Corollary weakened to what holds: an S-invariant ansatz has zero S-difference and reproduces the mass S-difference only where Phi_1^- + h^2 Phi_3 = 0 (misses both channels, not just chirality). aligned env moved into a fenced tex block with \[ \]. .ts gains a refined-framing authorNote with the proton figures (0.0526 / 0.00912, from the earlier probe; not re-run).

Lean: chirality_is_unique_S_odd removed (a duplicate of the Phi_1^+ tag rfl-classification under a name asserting uniqueness). Added, sorry-free over generic CommRing, all hypotheses used: mass_S_difference, chirality_sole_S_odd_channel_iff, s_invariant_ansatz_captures_S_odd_iff. #print axioms: propext, Classical.choice, Quot.sound. frobenius_s_classification docstring now says it is about Phi_1^+. isospin-mass-split-em-localisation.md row that cited chirality_is_unique_S_odd now cites mass_S_difference. scripts/prior-art-probe.py docstring still mentions the old name (historical list; its --selftest already fails 4/5 on origin/main, unrelated).

Still open, so keep open: the Phi_3 '(-1)^n chi swap' argument in the proof checks only (1,0) and was not repaired; .qa.json sidecars for frobenius-s-classification and its proof/table blocks are stale; the FrobeniusClassification tag structure remains hardcoded defaults (rfl classification), not derived.


2026-10-10 (session_01UboXkGB32JJhxiv7omapE4): Phi3 step generalised. Proof .md now derives S-oddness of Phi3 for every chain of bar-homogeneous factors (the three primitives and the unit are homogeneous; products stay homogeneous; S swaps chi_sym/chi_alt up to sign, so the ratio inverts). Lean, sorry-free over a generic field: chi_swap, barHom_hmul, barHom_chainProd, primitives_barHom, chiRatio_inverts in frobenius-s-classification.lean (axioms: propext, Classical.choice, Quot.sound only). Scope stated: NOT true on all of H_2 (sigma+1 gives ratio product -(q+1)^2/(q-1)^2). Probe |Phi3 + Phi3 o S| <= 1.4e-51 on all seven chains.
Still open: (a) the statement block itself (decision 3 restatement, two S-odd channels); (b) the in-tree .qa.json sidecars for -proof and the main block are stale. qa-sweep now writes test/attestations/block-qa/*.attestations.json instead and left 4 trap-* criteria needs-agent; not committed, since the old sidecars are what is stale.


CORRECTION 2026-10-10 (same session): item (a) above is wrong. The statement block already carries the decision-3 restatement on main (from #7626): two S-odd channels, Phi1^- and h_A^2 Phi3, at frobenius-s-classification.md lines 32-47. The only remaining open item is (b), the stale .qa.json sidecars. Same wrong claim also went into the #7641 PR body and the #7558 comment; both corrected.


## 2026-10-10: sidecar refresh NOT done, because the procedure no longer exists (no files changed)

**No sanctioned route refreshes the in-tree `<block>.qa.json` at platform pin `717aa19a`.** `cat-harness/content/pipeline/qa-paths.ts` (owner decision 2026-09-19) makes `test/results/block-qa/<mirror>.qa.json` the only WRITE target ("read both, prefer the new, write only the new"); the in-tree sibling is a read-fallback. Script verdicts go there and are gitignored (`qou.json` `qa` entry, owner ruling 2026-10-04 decision 11). Agent and human verdicts go to `test/attestations/block-qa/` on main (`cat-harness/schemas/qa-attestations.ts`, owner ruling D2(a) 2026-10-01). So AGENTS.md's remedy ("delete the stale `criteria.<crit>` entry and re-run qa-sweep") is obsolete, and hand-editing the in-tree file would fake currency (same call as `qou-99fk`). `scripts/check-sidecars.sh` does not measure staleness at all. It lists cached criteria from the in-tree file and always prints the qa-sweep line, so it cannot report these blocks "clean" whatever is done.

**Why the judgement half was not written either.** The platform design says to commit agent verdicts under `test/attestations/block-qa/`, and main has carried 9 such files since `896ded7a48` (today). But `qou-99fk` (todo, high) frames whether block-qa attestations belong in the tracked store as an owner call. `qou.json` describes `test/attestations/` as holding only the two bib ledgers. And no CLI records an agent verdict for a block-qa criterion: only qa-sweep and translation-block-qa call `writeCriteriaAttestations`, so the entry would have to be hand-written JSON. That is ambiguous, so nothing changed.

**Agent verdicts on the four `needs-agent` trap criteria**, from reading the .md and .ts at origin/main `ee2b758144`. They are recorded here, not in any store.

`prop:frobenius-s-classification`:
- thesis-restatement **pass**: the closing sentence states the S-symmetric-ansatz consequence, which is new content.
- performed-warmth **pass**.
- superlative **pass**: "the only S-odd channel exactly when …" is a precise iff.
- nonspeakable **pass**: the title "Frobenius S-eigenvalue classification of the 3-term mass formula" is a noun stack, which is acceptable for a title.

`prf:frobenius-s-classification`:
- thesis-restatement **FAIL (major)**. The final `**Witness**:` paragraph re-asserts that the derivation "verifies the eigenvalue assignments", which the proof has just established. It points to "the formal derivation" without a link, and it adds a claim the proof body never argues ("Φ₃ ≈ 0 for inter-nucleon-only chains in free A=1 nucleons"). The paragraph before it ("the S-odd part … has two sources … not one") also restates the corollary. Suggested fix: delete the Witness paragraph, or replace it with a link to the Lean file or probe.
- performed-warmth **pass**.
- superlative **pass, borderline**. "the structural carrier of the proton-neutron splitting" is a strong definite-article claim, but it is qualified by "at the Wedderburn formula level".
- nonspeakable **FAIL (minor)**. This sentence stalls when read aloud: "verifies the eigenvalue assignments canonical at $q_0$ and confirms that $\Phi_3 \approx 0$ for inter-nucleon-only chains in free $A=1$ nucleons".

Separately, the `.ts` title "Proof of frobenius s classification" is a lowercased slug. None of this was fixed, because content edits are out of scope for this refresh task.
