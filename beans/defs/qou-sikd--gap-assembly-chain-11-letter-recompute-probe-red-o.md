---
# qou-sikd
title: 'GAP: assembly_chain_11_letter_recompute_probe red on main (3/7) — LIVE literals predate the beta_Bor nucleon-word fix'
status: in-progress
pr: 8226
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-12T20:23:33Z
updated_at: 2026-10-04T15:19:44Z
parent: qou-trd0
---

Found as a by-product of qou-ales step 10 (PR #7233), while cross-checking the single-nucleon H_3 Markov trace against the exact H_6 two-nucleon computation. NOT caused by that branch and NOT a machinery regression.

MEASURED on main (clean tree, this container, 2026-09-12):

    python3 -u computations/markov/assembly_chain_11_letter_recompute_probe.py
    -> 3/7 assertions passed

    quantity            probe recomputes        probe's hardcoded LIVE literal    gap
    tr_M,H3(p)          0.62932840220292191816  1.145759692457300869             45.07 %
    tr_M,H3(n)          0.47513351715568221251  0.987743688115809571             51.90 %

ROOT CAUSE, established rather than guessed. Commit 7db032fb48 ("fix(qou-hu1f): atom_braid_word_3A emits beta_Bor -- the intra word was not the object its own comment named") CHANGED THE ELEMENT: the canonical 11-letter nucleon word now opens with beta_Bor = (sigma_0 sigma_1^-1)^3. A different element has a different trace. The probe's LIVE dict and the committed witnesses it quotes predate that commit. Corroboration, from three independent directions: (i) the post-fix crossings printed by atom_braid_word_3A_to_crossings(1,0) are EXACTLY step 3's nucleon_block("p", h, 0); (ii) the H_6 two-nucleon trace factorises as tr_M(p)^2 with tr_M(p) = (q^4+1)P(q)/(4 q^9 (q^2+1)^2) = 0.629328402..., i.e. the symbolic n=6 path agrees with the symbolic n=3 path; (iii) step 3's INDEPENDENT mpmath seminormal path gives the same free trace 0.396054237819282657 = 0.629328402...^2. So 0.6293 is the trace of the live element and 1.1458 is the trace of the retired one.

RULED OUT: dressing. Appending 1..4 further sigma_0 letters gives 0.5379 / 0.7418 / 0.6930 / 0.8867 -- none of them 1.1458. And hecke_character_symbolic.atomic_braid_to_crossings(1,0) returns the same 11 letters, so the "two extra gluon crossings per nucleon" its docstring mentions are not the difference either.

BLAST RADIUS. `grep -rl "1.1457596924573008" computations/` finds at least 8 committed witnesses/derivations carrying the retired value, among them chain-binding-closed-form.witness.json, atomic-tr-m-helium4.witness.json, tr-m-jones-markov-cross-check.witness.json, nucleus-real-sdp-proton.witness.json, skein-proton-canonical.witness.json and deltalambda/ka-additive-cluster-derivation.witness.json. Those are producer outputs; correcting them is a producer re-run, not a literal edit.

NOT FIXED, deliberately. Two reasons. (1) It is a drain across producer witnesses and AGENTS.md "ASK THE OWNER BEFORE CHANGING THINGS" (2026-09-07) gates that -- neither exemption applies (it does not increase precision, and which of the two elements is canonical for each downstream consumer is not settled by any single corpus artifact). (2) The probe's own assertions are the cheap part; the expensive question is whether every downstream consumer of 1.1458 WANTED the pre-beta_Bor element, which has to be decided per consumer.

NEXT HONEST STEP, for whoever picks this up: decide (owner call) whether 7db032fb48's element is canonical for the whole tr_M(p) consumer set. If yes, re-run those producers and make the probe READ its expectations from the witnesses instead of hardcoding literals -- the hardcoding is what let a 45 % change sit unnoticed. If no, 7db032fb48 needs revisiting instead.

Cross-reference: docs/audits/2026-09-12-gamma-gamma-word-selection-step10.md section 7.


## Round 52 Progress
- [x] PR https://github.com/litlfred/qou/pull/8226 (`523155d5604cc384f307eb1cb22785f1fded85da`): updated `computations/markov/assembly_chain_11_letter_recompute_probe.py` to read `("p", "muon2022")`, `("n", "muon2022")`, and `PINS["muon2022"]` from `computations/atomic-tr-m-mpfr-50dps.witness.json` (7/7 assertions pass).
