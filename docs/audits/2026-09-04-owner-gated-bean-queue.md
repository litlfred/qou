# 51 in-progress beans are waiting on an owner decision — a queue nobody was counting

**Date:** 2026-09-04 · **Measured on:** `origin/main` · **Session:** clinical-derivation-attack-vectors

## What was measured, and what it replaced

This started as a **staleness sweep** — my own suggestion, made after finding two
consecutive beans (`08a2`, `2x2i`) whose described work had already landed. I
proposed that a sweep "would likely close several more."

**That hypothesis did not replicate, and this document exists partly to record
the negative.** A reproducible random sample of 20 of the 418 `in-progress`
beans (seed `20260904`) yielded:

- **4 of 20** carried any mechanically-decidable claim at all — so keyword
  detection covers roughly **20 %** of the population and cannot measure a
  staleness rate. Every keyword detector I built this session was too narrow;
  this one is no exception, and the 20 % is the honest ceiling on the method.
- Of those 4, **3 were owner-gated decisions and 0 were stale.**

The two stale beans that prompted the idea were found because the author pointed
me at them, not by sampling. **A rate estimated from author-selected examples is
not a rate**, and I should not have offered one.

## The signal that did show up

Sampling surfaced something else, and it is measurable corpus-wide rather than by
sample: **beans blocked on a decision only the owner can make.**

    in-progress beans                                        418
    waiting on an owner decision                              51   (12.2 %)

**This is a lower bound**, for the same reason the staleness number was
unobtainable: it is a keyword match over eight phrasings (`owner's go`,
`owner decision`, `owner sign-off`, `OWNER-GATED`, `pending owner`,
`awaiting owner`, `needs owner`, `blocked on owner`). A bean that describes an
owner decision in its own words is invisible to it. Re-run rather than quote:

```
python3 - <<'EOF'
import glob, re
inprog=[p for p in glob.glob('.beans/*.md')
        if re.search(r'^status:\s*in-progress', open(p,errors='ignore').read(600), re.M)]
pats=[r"owner(?:'s)? (?:go|decision|sign-?off|ruling needed|call)", r'awaiting owner',
      r'pending owner', r'owner-gated', r'needs? owner',
      r'decision for the (?:owner|author)', r'owner must', r'blocked on owner']
print(len(inprog), sum(any(re.search(p,open(f,errors='ignore').read(),re.I) for p in pats)
                       for f in inprog))
EOF
```

## Why it matters

Each of these is work that **cannot progress no matter how many agent-hours are
spent on it**. An agent picking one up burns a tranche and lands back at the same
question. Several are also *cheap* to answer — a one-word ruling unblocks a
migration — which is exactly the case where an uncounted queue is most wasteful.

They are not a backlog of undone work. They are a backlog of **unasked
questions**, and AGENTS.md §"NAMING A DECISION IS ASKING A QUESTION" is explicit
that a decision raised without its frame is a mention rather than a hand-off.
Fifty-one such mentions have accumulated.

## The inventory

| bean | title | gating phrase |
|---|---|---|
| `b9ms` | 9b binding side lean formalization campaign prove ev | owner-gated |
| `dgpc` | tier c family chains | owner decision |
| `prn1` | two bulk prunes removed 785 dependencies not redundancies | owner decision |
| `qou-0yqu` | gap prove the 5 saddle sum rule σ j re v j 3π2 | pending owner |
| `qou-1c4y` | migration move the 840 muon q0 computations witnes | owner call |
| `qou-1jw9` | gap thmwedderburn mass formula is not exact at n3 | owner decision |
| `qou-2tuv` | h 3 vs h 3a the proper sum is infeasible past a12 | owner's call |
| `qou-324i` | the independent q0 disposition tests override sens | owner call |
| `qou-47sx` | convention d atompy caller sweep measure the true | owner decision |
| `qou-48is` | gap the canonical cross species nucleon ordering p | owner sign-off |
| `qou-52i4` | seed lake cacheqou v4 24 0 orphan branch after ful | owner's call |
| `qou-7kq3` | raw float64 ratchet is red on main 4 new dirty wit | owner decision |
| `qou-8na1` | y 0 0 is forced by the trace form radical so the l | owner decision |
| `qou-9xla` | producer missing prfinterface knot markov zs 4 ato | needs owner |
| `qou-agvb` | witness provenance is spelled three ways scriptfil | owner's call |
| `qou-avtq` | milestone attack vector queue qbeta c3odd fmap | owner call |
| `qou-c8p8` | mathlib infra close class field debt | owner decision |
| `qou-cds1` | s1 science re derive the qbeta ck ladder under d n | owner's go |
| `qou-d7h1` | gap eightfold way flavor su3 from qou components d | owner decision |
| `qou-e9pp` | witness refresh advice is unsafe zero of 700 self | owner call |
| `qou-fngs` | vacuous instance canonical makes gbfiltrationcolla | owner call |
| `qou-goc9` | gap which nucleon nf is canonical for the q beta c | owner call |
| `qou-gw96` | delta element fork the bar involution separates th | owner call |
| `qou-hey2` | gap feynman eigenbasismd29 claims balanced homfly | owner decision |
| `qou-im4m` | nucleon crossing counts the corpus derives a 13 cr | owner call |
| `qou-imkb` | gap paper six term isotope sweeps model b leg name | owner's call |
| `qou-ishr` | qou masssrc ships 44937 raw float64 and is scanned | owner's go |
| `qou-j3m4` | 37 unknown field warnings triaged one chapter cont | owner call |
| `qou-k4f8` | dual certificate existence for the operator select | owner decision |
| `qou-kc21im` | gap is kc21 structural parity convention immune verified or asserted | awaiting owner |
| `qou-kfcl` | 38 defabbrev fqns are declared in two library modu | owner call |
| `qou-lt8x` | the convention d blast radius does not cover 31 of | owner decision |
| `qou-m7py` | d2 rust gramrs tr m5z3 bug is load bearing under c | owner decision |
| `qou-orph` | 761 of 1598 qou lean modules are never built by lake build | need owner |
| `qou-p77d` | gap 883 non integral float64 at assertionscomputed | owner decision |
| `qou-puwe` | defmass identity lean formalises multiplicative in | owner decision |
| `qou-pwut` | 287 root level ad hoc qa writers bypass qa agent e | decision for the author |
| `qou-qflp` | q0 flip 262 was one corrupted reference not a tranche | owner-gated |
| `qou-r4ya` | balanced d function theta limit close the fibre le | needs owner |
| `qou-rgiz` | arc alpha em per loop measure 18pi non abelian sto | owner-gated |
| `qou-sf1t` | qplancherel constructed partition function total m | owner-gated |
| `qou-t7mt` | deffrobenius hopf substrate presupposes a dual its | needs owner |
| `qou-u87j` | 43 content block lean siblings redefine a library | owner call |
| `qou-vr3q` | deep dive 1 g3 monodromystokes constant keystone d | owner call |
| `qou-w1g8` | qu axiom 4 lean field omits idempotent orthogonali | owner's call |
| `qou-zdz5` | drain vol4 1 lambda cl2 wrong forms 54 sites 35 fi | owner call |
| `qou-zrx2` | gap the signed trace difference has an hbar q0 cla | owner decision |
| `qou-zzwm` | the c d excision left published accuracy figures b | owner call |
| `t7qv` | mass binding gap review theta reeb | owner's call |
| `w5tg` | lever 2 edge setoccupancy beyond refuted static in | owner-gated |
| `z2bn` | lever 1 focus derivetest fibre q difference kernel | owner go |

## What this document does NOT claim

- It does **not** rank these by importance; the phrasing match says nothing about
  cost or blast radius.
- It does **not** assert each is genuinely blocked — some may have been resolved
  in conversation without the bean being updated. That is the very staleness this
  sweep failed to measure, and it applies here too.
- It is **not** a request to answer all 51. It is a count, so the queue can be
  triaged deliberately rather than rediscovered one bean at a time.

## Suggested next step (judgement, not a finding)

Triage the 51 into *cheap ruling* vs *needs real thought*, and put the cheap ones
to the author in one batch. I would not do that unprompted: batching questions is
itself a judgement about the author's attention, and the accessibility rules in
AGENTS.md make that the author's call, not mine.
