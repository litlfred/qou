---
# qou-jopk
title: 'ROUTE A: the 2=2+0 coproduct split - does bowtie_K ACT on the depth-2 volume stratum?'
status: todo
type: task
priority: normal
created_at: 2026-09-04T20:42:08Z
updated_at: 2026-09-04T20:43:04Z
---

ROUTE A of epic qou-2q85. THE CHEAPEST LIVE ROUTE, and the only one needing NO new object.

WHAT IT IS. def:hq-bi-filtration's coproduct law splits depth: Delta_q(H_q^(n,K)) subset of + over n1+n2=n of H_q^(n1,K1) tensor H_q^(n2,K2). At n=2 the splits are 2=1+1 and 2=2+0. The 1+1 component needs the depth-1 stratum nobody has built (that is ROUTE B). The 2+0 component pairs the EXISTING depth-2 volume stratum with the EXISTING depth-0 interface layer.

SO THE QUESTION IS A MODULE STRUCTURE, NOT A MAP: does bowtie_K ACT on H_q^(2,K)? Not 'does the convolution layer map into the volume layer' - it cannot, 0+0=0 - but 'does it act on it', which the coproduct's 2+0 term is exactly the shape of.

WHAT TO CHECK FIRST, cheaply: is the action compatible with the Markov trace? tr_M is depth-PRESERVING (H_q^(n,K) -> P_n/P_{n-1}) per the same table, so a bowtie_K action on H_q^(2,K) would have to commute with tr_M to be meaningful for volume. That commutation is a finite check on objects that already exist.

COST: no new content object; a compatibility statement plus its proof. RISK: the action may be trivial - the 2+0 term could be the unit action, in which case nothing is learned. That is worth knowing early and is itself cheap to test.

DEFAULT IF NOTHING DONE: nothing changes; the two layers stay disconnected.
