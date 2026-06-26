---
# 60iz
title: 'T3 [BLOCKED]: Jones polynomial / knot-invariant infra → jet_filtered_knot_factor value side'
status: in-progress
type: task
priority: normal
tags:
    - keystone-infra
    - tier3
created_at: 2026-06-25T17:06:54Z
updated_at: 2026-06-26T01:57:37Z
parent: 08a2
---

jonesQuotient abstract; no Mathlib knot-invariant / Kauffman-bracket infra. Could build on Markov trace (Braiding/HnMarkovTrace) long-term; scoped as research-grade.

COORDINATION (2026-06-25): Jones layer = H_n(q) Markov-trace→knot-invariant, complementary to #2743's k[S_n] (q=1) Wedderburn build (MaschkeSnSemisimple/WedderburnSn, sorry-free Σ𝔫ᵢ²=n!). Main KnotRegistry/photon-Hecke also assembling knot+Hecke blocks. Intent+boundary posted #2743 (issuecomment-4805045194); build held pending their scope answer. Verifiable deps: HnMarkovTrace+BraidLinkTypes cached; IwahoriHecke/MarkovTrace NOT cached. Ledger: docs/coordination/keystone-infra.md.

PARTIAL (2026-06-25): built JonesViaMarkovTrace.lean — jonesHopf (Jones value of Hopf link via Markov trace) + PROVED jonesHopf_invariant (stabilisation ⇒ link invariant) + PROVED jonesHopf_canonical closed form. Sorry-free, in-build (BraidKnot aggregator), lean-direct exit 0. First layer; full arbitrary-braid Jones still needs IwahoriHecke (uncached). Complementary to #2743 q=1 Wedderburn.



[2026-06-26] Hopf layer LANDED on main (#2815, SHA 247c2e87): JonesViaMarkovTrace.lean sorry-free in-build — jonesHopf + jonesHopf_invariant (stabilisation⇒link-invariant) + jonesHopf_canonical + jonesHopf_pos. REMAINING blocked: jet_filtered_knot_factor.jonesQuotient wire needs IwahoriHecke olean (uncached). Epic 08a2 Tier-3 at drainable boundary.
