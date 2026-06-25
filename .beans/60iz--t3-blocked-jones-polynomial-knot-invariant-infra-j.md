---
# 60iz
title: 'T3 [BLOCKED]: Jones polynomial / knot-invariant infra → jet_filtered_knot_factor value side'
status: todo
type: task
priority: normal
tags:
    - keystone-infra
    - tier3
created_at: 2026-06-25T17:06:54Z
updated_at: 2026-06-25T23:31:57Z
parent: 08a2
---

jonesQuotient abstract; no Mathlib knot-invariant / Kauffman-bracket infra. Could build on Markov trace (Braiding/HnMarkovTrace) long-term; scoped as research-grade.

COORDINATION (2026-06-25): Jones layer = H_n(q) Markov-trace→knot-invariant, complementary to #2743's k[S_n] (q=1) Wedderburn build (MaschkeSnSemisimple/WedderburnSn, sorry-free Σ𝔫ᵢ²=n!). Main KnotRegistry/photon-Hecke also assembling knot+Hecke blocks. Intent+boundary posted #2743 (issuecomment-4805045194); build held pending their scope answer. Verifiable deps: HnMarkovTrace+BraidLinkTypes cached; IwahoriHecke/MarkovTrace NOT cached. Ledger: docs/coordination/keystone-infra.md.
