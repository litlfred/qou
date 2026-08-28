---
# qou-0gqn
title: 'STALE: canonical-with-proper-tower.witness.json does not reproduce -- E_0 collapses 3.59e6x, taking every B_MeV with it'
status: todo
type: task
priority: normal
created_at: 2026-08-28T20:29:47Z
updated_at: 2026-08-28T20:30:41Z
---

MEASURED 2026-08-28 on branch `claude/witnessbuilder-provenance-migration-2026-08-28`.
Found incidentally: the file was swept into a migration commit by a sample re-run
and had to be reverted, which is how the delta surfaced.

## What was measured

`computations/canonical-with-proper-tower.witness.json` as committed (timestamp
`2026-06-14T01:35:07Z`) does not reproduce from today's tree. Committed vs a
fresh run on `main`+this branch, all 16 result rows:

    field                    committed        fresh          rel move
    m_atom_per_irrep_total   6.30 .. 30.75    3.56 .. 19.88  0.35 - 0.45
    m_free_per_irrep_total   8.40 .. 49.53    4.96 .. 33.13  0.33 - 0.43
    E_0_MeV_per_cat          243.5284428      6.788428e-05   1.00
    E_0_MeV_per_cat (mode2)  249.4029733      1.200143e-04   1.00
    B_MeV                    510 .. 6218      9.5e-5 .. 2.8e-3

## The B_MeV collapse is entirely E_0's

`B_MeV = (m_free - m_atom) * E_0` holds in both files:

    committed  (8.396533659 - 6.302378037) * 243.5284428 = 509.986   (matches)
    fresh      (4.964617151 - 3.561992542) * 6.788428e-05 = 9.5216e-5 (matches)

So there are two independent moves, not one:

  1. the per-irrep mass totals moved ~40 % -- consistent in sign and rough
     magnitude across every row;
  2. `E_0_MeV_per_cat`, a single scalar shared by all rows within a `pair_mode`,
     collapsed by **3.587e6** (243.5284428 -> 6.788428e-05) and by **2.078e6**
     in the other mode. A clean 6-order collapse of one shared scalar reads like
     a unit or normalisation change upstream, not accumulated drift.

The fresh run also serialises these as `_precision.fmt` STRINGS where the
committed file has float64 numbers, i.e. the NO-FLOAT64 discipline has since
reached this producer's cone. That is a separate, expected change and is not
the cause of either move.

## Scope -- what this does NOT establish

scope-(a). This says the committed artifact does not reproduce. It does **not**
say which set of numbers is right, and both look wrong on their face: a light
nucleus does not have a 4573 MeV binding energy (committed) and does not have a
9.5e-5 MeV one (fresh). This is an exploratory tower probe, not production
compute, so "neither is a physical binding energy" is not itself news -- the
finding is that the file's own numbers are no longer derivable from its own
producer.

I did NOT bisect the cause. `E_0` is the thing to chase first, because it is one
scalar and it carries the whole B_MeV story.

## Relation to qou-wlaf

Same class, different artifact. `qou-wlaf` is
`probes/gram-norm-binding-probe.witness.json` failing its own cross-check
assertion by seven orders. This is a second instance in the same population
(June-era binding witnesses that stopped reproducing), which is weak evidence
that the population is larger than the two known members -- but only weak: two
is two, and I have not swept for more.

## Next step

1. Locate what sets `E_0_MeV_per_cat` in the producer and diff that expression
   against its June version (`git log -p` on the producer since 2026-06-14).
2. Decide whether this probe is still wanted at all before regenerating it -- a
   regenerated exploratory witness that nothing consumes is churn, and the
   committed one at least records what was believed in June.
