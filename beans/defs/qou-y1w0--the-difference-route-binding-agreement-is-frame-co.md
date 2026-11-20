---
# qou-y1w0
title: 'The difference-route binding agreement is frame-conditional: multibond B(2H) goes -6.3% to -75.2% under the canonical ordering, exactly the 3.785x factor'
status: todo
pr: 8197
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-09-14T08:02:15Z
updated_at: 2026-11-20T16:06:50Z
parent: qou-v2om
---

## Measured — `binding_multibond_wenzl`, deuteron, Wenzl bridge at 50 dps

    AME B(2H) = 2.224566 MeV        m_e * Vol(B_3) = 3.744460 MeV

    ordering    tr_vac     tr_bond    dtr        B (MeV)   err vs AME
    grouped     1.131717   0.575091   0.556626   2.0843    **-6.3 %**
    borromean   0.299015   0.151947   0.147068   0.5507    **-75.2 %**

`0.556626 / 0.147068 = 3.785` — **exactly** the 2H absolute-trace factor that
`pyhecke.atom.nucleon_word_letters` documents. So the mechanism is not in
dispute and was already written down: the difference route is proportional to
`tr_M(W_free)`, and that docstring says in as many words that
"`binding_canonical`'s difference route moves with them by exactly the same
factor".

**What was NOT written down is the consequence.** The probe's -6.3 % agreement
with AME — its entire result — holds only in the superseded ordering. Under the
ordering ruled canonical on 2026-09-05 it is -75.2 %.

## This is the second of two, and I have only examined two

Working the `qou-t29k` drain I looked at exactly two sites in enough depth to
know what they report, and **both** turned out to have frame-conditional
agreement with experiment:

| site | route | grouped | canonical |
|---|---|---|---|
| `b_pred_mirror_slope_closed_form` (`qou-u8ji`) | ratio `tau_p/tau_n` | plateau 1.4223 vs measured 1.372 | 2.6936, +96 % |
| `binding_multibond_wenzl` (here) | difference `tr_vac - tr_b` | B -6.3 % vs AME | -75.2 % |

Two for two is a pattern worth naming, but it is **not** a corpus-wide result
and I am not claiming one: fourteen unguarded sites remain unexamined, and the
two I picked were the two that looked most likely to be interesting. What it
does establish is that the `qou-t29k` drain cannot be run as code hygiene.

## Which quantities are actually invariant

`nucleon_word_letters` documents invariance for `tr_M(W_atom)/tr_M(W_free)` —
ONE nucleus over its OWN free word, where connected-sum multiplicativity makes
letter order inside a summand irrelevant. That covers `L` and the three bond
constants. It does **not** cover:

  * `tau_p / tau_n` — two DIFFERENT nucleons (`qou-u8ji`);
  * `tr_vac - tr_b` — a DIFFERENCE, which carries the absolute scale (here);
  * any absolute trace.

A site is safe to switch iff its reported quantity is in the first class. That
is the triage question for the remaining fourteen, and it is answerable by
reading each site rather than by re-running it.

## Also found at this site, not the subject of this bean

`_chain_word` says it "mirrors `atom_braid_word_3A`" and diverges three ways:
the grouped ordering; a colour-BLIND `-h/2` p-n crossing where the canonical
convention is `bring_color_weighted` (owner ruling 2026-08-15); and
`float(c), float(d)` casts inside a 50-dps computation. Only the first is
`qou-t29k`'s subject.

## Not switched

Same reasoning as `qou-u8ji`: choosing the ordering that reproduces AME would
be selection against the target, and the 2026-09-05 ruling was made on
structural grounds. Left as committed and excluded from the drain.

## Progress Update (PR #8197 — `status: in-progress`)

- [x] Formalized pure Lean 4 module(s) (`QOU/MassTheory/BorromeanShadowCycleMerge.lean`, `QOU/MassTheory/SecondOrderContentCancellation.lean`, `QOU/Hecke/DeltaLongEMinusOrderingSplit.lean`, `QOU/MassTheory/LoopValueNormaliserAndFrameDiff.lean`) with `0 sorry` and `0` findings across all 6 static vacuity audits.
- [x] Added 50-dps `mpmath` + exact rational probe `computations/probes/borromean_shadow_c2_deltal_loop_frame_probe.py` and 2-commit stamped witness `computations/probes/borromean-shadow-c2-deltal-loop-frame-probe.witness.json` (`allPassed: true`, `0` raw `float64`).
- [x] Opened and signed [PR #8197](https://github.com/litlfred/qou/pull/8197) (`ready: 4a2ed9a21b68b7d23b2e693b68f472d7dcf102a6`).

## 2026-11-20 — claim released (W4 batch-PR triage, owner instruction)

Status `in-progress` → `todo`. The claim came from batch PR(s) #8197, closed on the owner's instruction as vacuous or superseded (`docs/coordination/2026-11-20-batch-pr-triage.md`, PR #8531). `todo` is the status this bean had before that claim. Before the reset, nothing showed this bean completed: it is not completed or scrapped, no open PR outside those batches cites it, and no main commit since the claim names it with a closing word.
