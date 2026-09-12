---
# qou-m8f3
title: 'Dominant-summand extensive test: Ursell-invert log|y_λ χ^λ(β_A)| of the trace''s dominant summand alone (qou-brng live remainder)'
status: in-progress
type: task
priority: normal
created_at: 2026-09-12T05:08:33Z
updated_at: 2026-09-12T05:23:52Z
---

Claimed 2026-09-12 by branch claude/dominant-summand-extensive-test-2026-09-12. Front: the live remainder named in qou-brng (2026-09-11, PR #7181 section) — the dominant summand's own log-weight L(A) = log|y_λ* χ^λ*(β_A)|, Ursell-inverted alone, on the live post-2026-09-05 alternating-core atom word (qou-hu1f), proton pin, convention D. Caches chi-<atom>-h<n>-at-q0-50dps (computedAt 2026-09-06) verified against a live recompute of the deuteron: max |cache − live| over χ and y_λ = 1.4e-49.


## RESULT 2026-09-12 — NEGATIVE at A ≤ 4, scope (b); the channel moves to A ≥ 6 / classes B, D

Producer `computations/brng_dominant_summand_ursell_probe.py` (14/14, 60 dps, proton pin, convention D); audit `docs/audits/2026-09-12-dominant-summand-extensive-test.md`; Lean `QOU/Mass/OneRowBlockLetterProduct.lean` (generic ring, NOT compiled here — disk).

**Claim.** For every typed cluster with A ≤ 4 (p, n, pp, pn, nn, ppp, ppn, pnn, nnn, ppnn) the trace's dominant summand `argmax|y_λ χ^λ|` on the live alternating-core word is the ONE-ROW block `[3A]` (runner-up ≤ 0.754 of it, ⁴He). Its character is `∏_letters (c q + d)` (ring hom, verified 1.2e-49), so the word-dependent part of `L(A) = log|y_λ* χ^λ*|` is EXACTLY chain-edge additive (residual 7.4e-51 in the atom's own block). The complete-graph Ursell cumulants are the chain's missing-edge accounting: `b₃(ppn) = b₃(pnn) = −b₂(pn)` (ratio −1.000 exactly; AME +0.81/+0.47). The rest of `ΔL = L_free − L_atom` is the free-side argmax switch — a function of the FREE word only — and it is 100.6 % of ⁴He's `E₀·ΔL = 3.93 MeV`. The word-free `log y_(3A)` has alternating cumulants (−0.795, +0.622, −0.516 log units ≈ −3.33, +2.60, −2.16 MeV) identical for ³H and ³He and for any word. Uniform-e₂ frame: e₂ = −0.023 MeV (deuteron anti-bound), b₃(³H) = +0.483, b₃(³He) = −0.391 MeV (mirror pair OPPOSITE signs; AME +1.808/+1.044). No connected many-body term with nuclear content. Invariant for (b): one-row dominance (measured) + letter-multiplicativity (exact).

**Where it stops.** At ⁶Li the dominant block is two-row `[15,3]`; E₀·ΔL(⁶Li) = 8.5 MeV vs AME 32.0 — one point, scope (a) for A ≥ 6.

**Secondary, reported NOT wired.** The BINDING-sum argmax `|yχΔ|` is `[5,1]/[6,3]/[6,3]/[9,3]` — exactly BindingConcentration.lean's list (its 'dominant partition' is this argmax, not the trace's; survived the word change). Two-row, not letter-multiplicative: uniform-e₂ b₃(³H) = +1.016, b₃(³He) = +0.747 MeV (0.56×/0.72× AME, right sign), but typed b₃(ppn) = −1.26 MeV, b₄(⁴He) = −4.27 vs +9.24 (wrong sign), and b₃ is monotone in N−Z (−4.92, −1.26, +2.34, +4.58 MeV for ppp, ppn, pnn, nnn). A charge-asymmetry artefact of the colour-weighted interface, not a connected binding term. Not selected, not wired.

**Controls.** Full-trace log(tr_f/tr_a) is chain-edge additive to 5.3e-50 on the LIVE word with b₂(pp) = ln(1/z_D) to 20 digits — first numerical confirmation of the qou-g8i1 bond rule post-ruling. Cache provenance: the four 2026-09-06 chi caches reproduce to 3.4e-49.

**Next (judgement).** Default: record and stop. Honest continuation of THIS channel: A ≥ 6 on the two-row dominant with the typed decomposition from the start (21 typed words, seconds each). Do not follow the secondary's b₃ > 0 — fit signature.

Bean stays OPEN pending merge of #7200; its subject (qou-brng's extensive term) is an open conjecture and qou-brng stays open regardless (rule 13a).
