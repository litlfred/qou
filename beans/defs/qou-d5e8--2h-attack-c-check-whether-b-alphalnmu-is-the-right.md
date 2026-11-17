---
# qou-d5e8
title: '2H ATTACK C: check whether B = -alpha*ln(mu) is the right functional at all - qou-kj4v says the degeneracy argues no flavour-only mu can be'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-25T18:37:51Z
updated_at: 2026-11-17T07:44:10Z
parent: qou-10v9
---

## RESOLVED 2026-08-25 — converges on the braid word. See docs/audits/2026-08-25-deuteron-attack-c-convergence.md

Three independent lines (my Hecke-element negative, qou-kj4v's exact flavour-only
degeneracy, and the 2026-08-09 chain-walk audit's alpha-is-pinned-elsewhere argument)
all eliminate the interface scalar and alpha and land on the BRAID WORD.

Also found: B = -alpha*ln|tr_M| is POSITED. Five-path corpus-grep finds no derivation
and NOTHING in Lean; the only statement of it in content/ is a row in a NOTATION TABLE.
And the dashboard's cited definition, 'Defn: standard-part-functor.md', is DEAD - that
block defines the standard-part map and functor and contains no B_sym, no alpha and no
binding at all. Same defect class as prop:hecke-spectral-sequence.

Measured: the 2H word is 23 crossings over 6 strands, of which exactly ONE carries the
interface offset (index 2, d = -0.4997h). The other 22 cancel in the free/atom ratio.
The entire deuteron binding rides on a single sigma-type crossing.


## 2026-08-31 — the "posited" verdict is WRONG; the derivation is in docs/audits/

This bean records, from the 2026-08-25 five-path grep:

  "B = -alpha*ln|tr_M| is POSITED. Five-path corpus-grep finds no derivation and
   NOTHING in Lean; the only statement of it in content/ is a row in a NOTATION
   TABLE."

**The first clause is false.**
`docs/audits/2026-08-08-binding-functional-attack-vectors-and-li2q-guard.md`
carries a section headed, verbatim:

  ## 10a. The functional is DERIVED, not chosen -- and it is the log form

dated **17 days earlier**, sitting in `docs/audits/` -- the first path the grep
table lists, and the one it reports as "files that USE the form; none derives
it". Its argument: tr_M is multiplicative over independent subsystems
(tr_atom = tr_free * PROD mu_k, measured to 1.2e-31) and energy is extensive, so
the trace-to-energy map obeys Cauchy's f(xy) = f(x) + f(y) on (R_+, x) and the
log form is forced.

`ursell_alternation_sign_identity_probe.py` had ALREADY cited 10a as a derivation
("THE BOLTZMANN IDENTIFICATION IS DERIVED, NOT ASSUMED -- and by the corpus").
So the corpus disagreed with itself in three places.

**Still true, and unretracted:** the dead-citation finding (the dashboard cites
`standard-part-functor.md`, which defines the standard-part map and functor and
contains no binding form), and the **Lean: nothing** row -- which is now fixed.

## What 10a needed, and now has

**Lean** (sorry-free, lean-direct exit 0, no sorryAx):

  logForm_extensive               -a ln(xy) = -a ln x + -a ln y
  linearForm_extensivity_defect   a(1-xy) - [a(1-x)+a(1-y)] = -a(1-x)(1-y)
  linearForm_not_extensive        nonzero whenever x != 1 and y != 1
  linearForm_ceiling              a(t_free - t_atom) < a * t_free

The closed form is new -- 10a reports the defect only as a measured number -- and
being an identity it holds at every q with no anchor.

**10a's number is convention-C frame.** That audit predates the 2026-08-09
convention-D excision by one day. At the proton pin with mu_pp = z, mu_nn = z - h:

    convention C   defect = 1.487498   <- 10a's quoted 1.4875, to 1.6e-6
    convention D   defect = 0.966887

Conclusion unaffected in both; the figure needed the scope. Both audits are
annotated in place rather than left for a third reader to rediscover.

**Paper:** `prop:binding-functional-is-the-log` (nuclear-interactions, validate
exit 0). **Compute:** `binding_functional_extensivity_probe.py` (4/4).

**NOT closed by this.** The uniqueness step -- only continuous solutions of
Cauchy's equation are c*ln x -- is classical and is NOT formalised, so "forced"
still rests on it. And this bean's own redirect stands: the three lines still
converge on the BRAID WORD, which none of this touches.


## 2026-08-31, SAME DAY — I correct my own entry above

The entry immediately above says the 2026-08-25 audit's "posited" verdict "is
WRONG" and that "the corpus disagreed with itself in three places". **Both are
wrong, and the error is the one this corpus documents most often: I read the
section and not the document.**

That audit **retracts its own verdict**, later in the same file, under
"RETRACTION + the real gap -- B = -alpha*ln|tr_M| IS derived, conditionally".
It derives the form by a different route (Vol_alg := tr_M -> tau_arch =
ln|Vol_alg| -> vol_through_tau -> evaluate at q_0) and says explicitly *"My
'posited' verdict is withdrawn."* So the corpus does NOT disagree with itself,
and no third reader had to rediscover anything.

**What survives, and it inverts to something better.** 10a IS a second
derivation, and the audit's retraction never cites it (verified: the only 10a
mentions in that file are the ones I inserted). The two routes are not
equivalent in strength:

  Vol chain   conditional on the Kashaev volume conjecture (gap a), and
              regime-mismatched -- KVC needs N -> infinity and q a root of
              unity; the framework has a fixed finite braid and real q_0 > 1
              (gap b)
  10a         needs only multiplicativity + extensivity, both of which hold at
              fixed finite n and real q. No conjecture, no asymptotics.

So gap (a) as stated -- *"every binding number is therefore KVC-conditional"* --
is **too strong for the FORM**. What is KVC-conditional is the identification of
ln|tr_M| with a hyperbolic VOLUME. The log form itself has a KVC-free derivation.
Gaps (b) and (c) stand untouched.

That is a better finding than the one I claimed, and it is the one the Lean now
formalises: the KVC-free route, sorry-free.

Everything else in the entry above is unaffected -- the four Lean theorems, the
closed form -a(1-x)(1-y), the convention-C scoping of 10a's 1.4875, and the
paper/compute wiring.

## Implementation & Witness Progress (PR #8261)
- Branch: `qou-10v9-d5e8-lq6k-tqfm-ughq-vvv4` (`215564fea0bbd17193637e08e9f87df6e0ac73b7`), PR: `litlfred/qou#8261`
- Lean 4 module: `folio/quantum-observable-universe/lean/QOU/Eightfold/BoltzmannExtensivityMilnorAntisymmetryShiftInertnessWenzlMarkovLockAndHadronicMeltOrdering.lean` (0 sorry, 0 axioms, 0 vacuity findings)
- Probe & witness: `computations/probes/boltzmann_extensivity_milnor_antisymmetry_shift_inertness_wenzl_markov_lock_and_hadronic_melt_ordering_probe.py` -> `computations/probes/boltzmann-extensivity-milnor-antisymmetry-shift-inertness-wenzl-markov-lock-and-hadronic-melt-ordering.witness.json` (`allPassed: true`, `scriptHash: 6d6a6f5a2d13`, `scriptCommitSha: 83f7ff931c7cc699e6338421bf57c15a92f557d2`)
