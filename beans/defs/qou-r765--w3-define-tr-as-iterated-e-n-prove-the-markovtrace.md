---
# qou-r765
title: 'W3: define tr as iterated E_n; prove the MarkovTrace fields (cyclic + Markov normalization) from the tower'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-11-16T21:54:00Z
parent: qou-rtxm
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


## W3 second half is BLOCKED, and on a specific missing brick (2026-08-26)

The remaining target is the `MarkovTrace` class field `cyclic : ∀ x y : H, tr (x*y) = tr (y*x)`
(`MarkovTraceOnHecke.lean:80`) — note it is **unconditional in x,y**.

`cyclic_two_g_of_tower` (PR #5827) gives cyclicity only for words already in the
shape `(u·g·v)·(p·g·r)` with u,v,p,r in H_n. Getting from there to arbitrary
x,y needs the **spanning decomposition H_{n+1} = H_n + H_n σ_n H_n**, to reduce a
general element to that shape. That decomposition **does not exist in the corpus**
(see the finding appended to qou-2017 — it was a named W2 deliverable, undelivered).

**Deriving `hgwg` does NOT unblock this.** `hgwg` would additionally need the
Markov property of the conditional expectation, `ε (b · σₙ · c) = z • (b·c)`, which
is NOT a field of `HeckeConditionalExpectation` (that class has exactly `retract`
and `bimodule`). Adding it as a new class field would RELOCATE the assumption into
a named carrier, not discharge it — worth doing for hygiene, but it is not progress
on the mathematics and should not be reported as such.

Also checked: `MarkovTraceCompatibility`, named in `MarkovTraceOnHecke.lean:16` as
"axiomatising the Markov properties", **does not exist** — stale docstring. And (M3),
the Markov reduction, is documented-not-enforced in the `MarkovTrace` class because
σₙ is absent from its signature.

**Real next brick:** the spanning decomposition, as a §3b class with a
content-bearing field, then W3's second half becomes reachable.


## CE + Markov fields DISCHARGED for H2 subset H3 (2026-08-26, PR #5827)

All three class fields proved concretely. epsLin is FORCED, not chosen — every
entry read off the coset table by imposing the Markov property:

  eps v = <v0 + z.v2 + z.v5 , v1 + z.v3 + z.v4 + z.h.v5>

  epsLin_retract   : eps (iota x) = x
  epsLin_bimodule  : eps (iota x * w * iota y) = x * eps w * y
  epsLin_markov    : eps (iota b * sigma1 * iota c) = z . (b*c)

**bimodule is the one that could have failed.** eps was written down from the
coset table; whether the resulting map is an (H2,H2)-bimodule map is a SEPARATE
question, settled by computation over all six coordinates with x, y, w symbolic.

**They are theorems, not instances, and the obstruction is NOT mathematical.**
HeckeConditionalExpectation and HeckeMarkovExpectation both bind the UNBOUNDED
HeckeBraidedPresentation, which has no contentful instance for a finite algebra
(constant_generator_presentation + far_commute_zero). Re-pointing them at
HeckeBraidedPresentationOfRank — as HeckeCosetSpanning already is — would make
both instances declarable and would then make cyclic_two_g_of_tower
UNCONDITIONALLY INSTANTIABLE at this rung.

Not done here: that is a signature change to classes predating this work, which
JonesBasicConstruction also binds. Left to the author.

Guard rc=0 on 77 entries (74 -> 77).


## W3 first half MERGED — PR #5827, 2026-08-26 (rebase, sha 09e2be2b50)

Landed: the bridge (4 of 7 hypotheses derived), spanning class + its H2-H3
instance, rank-bounded presentation + H2A/H3A instances, and all three CE/Markov
class FIELDS proved concretely.

**NOT completed.** cyclic_two_g_of_tower stays CONDITIONAL: HeckeConditionalExpectation
and HeckeMarkovExpectation have their fields proved but no instances, because both
still bind the UNBOUNDED HeckeBraidedPresentation. Re-pointing them at
HeckeBraidedPresentationOfRank is the two-line change that would make both
declarable and make cyclic_two_g_of_tower unconditionally instantiable at this rung.
Author's call — it is a signature change to classes predating this work that
JonesBasicConstruction also binds.

And this is ONE RUNG. Nothing here speaks to general n; WenzlTowerStep untouched.



## Claim reset 2026-10-04

Was in-progress with no bean update since 2026-08-26 and no main commit naming it since 2026-09-20 (owner decision 3). Re-claim with `bun run beans:claim` if you pick it up.

## 2026-11-16 — W3 Iterated Conditional Expectation Tower Trace (`QOU.Foundations.ConventionDKeystoneTraceTower`, PR #8214)
- Formalized `iteratedTowerTrace`, `iteratedTowerTrace_map_add`, `iteratedTowerTrace_map_smul`, and `iteratedTowerTrace_markov_step` in `folio/quantum-observable-universe/lean/QOU/Foundations/ConventionDKeystoneTraceTower.lean` (pure Lean 4 core, generic `CommRingOps R` per §7c, `0` `sorry`, `0` warnings, `0` vacuity audit hits; wired into `QOU.lean`).
- Commit: `7cc3c04b0719e92286ff6279855cbf3f0b9a7826` | PR: `https://github.com/litlfred/qou/pull/8214`
- Kept at `status: in-progress` per merge-manager protocol.
