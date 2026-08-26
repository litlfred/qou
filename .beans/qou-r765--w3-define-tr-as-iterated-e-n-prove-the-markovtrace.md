---
# qou-r765
title: 'W3: define tr as iterated E_n; prove the MarkovTrace fields (cyclic + Markov normalization) from the tower'
status: in-progress
type: task
priority: normal
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-08-26T13:48:21Z
parent: qou-utb3
---


## W1 re-scope note (2026-07-25, qou-xik5 audit)

Title correction: the class does NOT carry "Markov normalization" — (M3) is
documented-not-enforced (MarkovTraceOnHecke.lean:70-71) and `tr(1)=1` is not a
field. W3's actual target: prove the THREE class fields (`cyclic`, `map_add`,
`map_smul`) for `tr = tr_1 ∘ E_1 ∘ ⋯ ∘ E_{n-1}`. The tower/stabilization
property feeds the separate `MarkovStabilization` class
(`observationFrame_stabilizes` consumer) — may be delivered alongside, but the
`MarkovTrace` instance does not block on it. No positivity anywhere
(`docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`).


## W3 first half landed — PR #5827 (2026-08-26)

`QOU/Machinery/MarkovTowerBridge.lean`: **4 of cyclic_two_g's 7 hypotheses derived**
from the W2 interface (`HeckeTower.HeckeConditionalExpectation`), leaving `hIH`
(the induction hypothesis) and `hgwg` (the Markov reduction).

Instantiation: A := Hn1; memB x := exists y, x = i y; E := i . e; tr := trn . e;
memBlow := memB.

`hCE` is the one with content — the trace cannot distinguish `a*x` from `a*E x`
for `a` in the subalgebra. Both sides evaluate to `trn (y * e x)`: left by
`bimodule` at z=1, right by `map_mul` + `retract`. Derived ONLY because tr is
DEFINED as trn . e; for a trace not of that form it is a genuine assumption.

**The instance is load-bearing, and this is proved not asserted.**
`hCE_fails_without_conditional_expectation`: with Hn=Hn1=R=Q, i=id, e=scale-by-2
(linear but neither retraction nor bimodule map), hCE reads 2=4 at a=x=1. So the
identity is FALSE without the instance, not merely unproved.

Verification: lean-direct exit 0; #print axioms clean on all seven declarations
(memB_one needs only propext); guard rc=0 on 58 entries with all seven pinned;
guard --selftest PASS; lean_freshness --selftest PASS.

**NOT closed.** HeckeConditionalExpectation has no instance and this does not
build one. Conditional-proved is not premise-established — what changed is the
SIZE of the conditional. W3's remaining half is the MarkovTrace class fields
(cyclic + Markov normalisation) from the tower, which still needs `hgwg`; the
coset-sum bricks for it are in QOU/Machinery/MarkovCosetLift.lean (PR #5822).

**W2 note:** bean qou-2017 is marked completed with NO completion evidence in its
body. Verified against the corpus instead: HeckeTowerBasicConstruction.lean does
exist and does carry the three classes at :169/:187/:209. Deliverable is real.
