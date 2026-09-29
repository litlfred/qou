---
# qou-30vo
title: The import-cone staleness audit's 1473 is dominated by the witness-WRITING module
status: todo
type: task
priority: normal
created_at: 2026-08-23T23:34:15Z
updated_at: 2026-08-23T23:48:09Z
---

computations/witness_import_cone_staleness_audit.py is well-designed and targets a real class -- the third staleness direction, where a producer stays byte-identical (SELF green) while a module it imports moves. My peel finding today is a CONFIRMED instance of exactly that (qou-3zby): markov-peel-atomic-tr-m-muon, producer not self-stale, numbers move up to 2.9x on re-run.

But its headline count cannot be used as a work list.

MEASURED on origin/main 2026-08-23:
  witnesses scanned                3052
  SELF-stale (excluded)             626
  IMPORT-CONE STALE                1473

  tools/qou-substrate/python/qou_substrate/witness.py   last commit 2026-08-23 (today)
  producers importing WitnessBuilder / qou_substrate.witness   2077
  witnesses with computedAt BEFORE 2026-08-23                  1972

1972 >= 1473. So that ONE module -- the witness-WRITING infrastructure -- is
sufficient on its own to explain the entire flagged set. The reported count is
not distinguishable from 'was this witness computed before the last time
anyone touched WitnessBuilder'.

A change to witness.py CANNOT move a mathematical result; it serializes JSON.
The corpus already holds this exact judgement about the same module one field
over: AGENTS.md records that witness.py masks scriptCommitSha in
_EPHEMERAL_META_FIELDS, and that witness_dependency_drift.py keys
self-staleness on scriptHash alone, precisely because that field is provenance
rather than mathematics. The same reasoning applies to the module itself when
it appears in a cone.

THE RANKING IS WORSE THAN THE COUNT. The audit sorts by lag, and all four
visible entries in its 'Worst 25 by lag' name witness.py as the newest
dependency. So the presentation puts the false positives at the top and buries
confirmed cases like peel below them.

PROPOSED FIX, not implemented here: exclude witness-writing / provenance
modules from the cone (qou_substrate/witness.py, computations/witness_base.py,
and the _precision serialization surface), or class them separately and report
both numbers so nothing is hidden. The audit already computes a by-newest-module
breakdown, so the data to do this is present; it just is not applied to the
headline.

SCOPE -- this is an UPPER-BOUND argument, and I am not claiming all 1473 are
false. It shows the infra module is SUFFICIENT to explain the count, so the
count carries no information; it does not show every flagged witness is clean.
Some are genuinely stale for mathematical reasons -- peel is one, confirmed by
re-run rather than by the detector. Deciding which needs the same 're-run to
decide' discipline AGENTS.md already prescribes for witness_staleness_triage,
where 72 substantive producers actually re-run yielded only 28 moved fields
(39%). Do not treat a corrected count as a work order either.

## EXACT BREAKDOWN — the audit's own by-module table, and it is worse than my bound

The audit already prints this; the headline just does not use it.

     count  module (newest change in the cone)
      1444  tools/qou-substrate/python/qou_substrate/witness.py
        22  computations/substrate/q_parameter.py
         3  computations/_path_bridge.py
         2  computations/substrate/_precision.py
         1  computations/_habiro_coefficient_extract.py
         1  computations/q1_mass_gap_probe.py

1444 of 1473 = 98.0 percent name the witness-WRITING module. The residue is 29,
of which 22 are q_parameter (which CAN move a number -- it serves q0, so those
are real candidates), 5 are path/precision plumbing, and 2 are mathematical
modules. Signal is ~29 of 1473, i.e. 2.0 percent.

## THE SHARPER DEFECT: 'newest' MASKS THE REAL CAUSE

I framed this as an inflated count. The by-module table shows something worse.
The audit reports only the NEWEST cone dependency, so one recent infrastructure
commit does not merely ADD false positives -- it OVERWRITES the attribution on
every witness behind it.

markov-peel-atomic-tr-m-muon is the worked example. It is genuinely cone-stale
(confirmed by re-run: numbers move up to 2.9x, qou-3zby), and its real movers
are 666e8959b1 (ctype / averaged_weighted repair) plus four
canonical_braid_crossings commits. NONE of those appear anywhere in this
output. The witness is counted among the 1444 and attributed to witness.py,
because witness.py is newer. A reader working this table would re-run it,
see the numbers move, and credit a JSON serializer.

So the fix is not only 'exclude infra from the count'. It is: report the newest
NON-INFRASTRUCTURE mover, or the full set of movers, not the single newest
module. Otherwise the one field the table offers for diagnosis is the one most
likely to be wrong.

Corrected signal-to-noise for the record: my upper-bound argument said the infra
module was SUFFICIENT to explain the count. Measured, it explains 98.0 percent
of it directly.

## 🛑 RETRACTED — my '98% false positive / ~29 real' reading was WRONG

I implemented the exclusion I proposed above, and it refuted the premise.

Excluding the two provenance modules and re-running: **15** of the 1,473 are
provenance-ONLY. Not 1,444. The count is essentially real; what was wrong was
the ATTRIBUTION.

    of which PROVENANCE-ONLY :    15
    of which SUBSTANTIVE     : 1458

The by-module table, peeling one layer at a time:

    attributed to                     count
    qou_substrate/witness.py           1444   <- as reported before the fix
    substrate/witness_base.py          1116   <- revealed by excluding the above
    substrate/q_parameter.py           1171   <- revealed by excluding both
    mass_at_3A_proper.py                247
    _li_2_q_util.py                      36

The provenance modules were not standing in for nothing. They were standing in
FRONT of real movers. I read 'newest_dep = witness.py on 1,444 rows' as
'1,444 witnesses have no real mover', which does not follow from a field that
reports only the SINGLE newest module -- the very masking mechanism this bean
is about. I applied the mechanism to the peel witness and then failed to apply
it to the population.

WHAT SURVIVES: the masking defect is real and is worse than I described. It did
not merely misfile one witness; it misfiled essentially the whole class. The fix
is correct and lands: attribution now names the newest module that could
actually move a number.

WHAT DOES NOT SURVIVE: 'the count is not distinguishable from computed-before-
someone-touched-WitnessBuilder', and 'signal is ~29 of 1473, 2.0 percent'. Both
retracted. The count did not move at all -- 1,473 before and after -- which is
the correct behaviour for an attribution fix and is how it should have been
framed from the start.

STILL NOT A WORK ORDER. q_parameter is now the top attribution at 1,171 and is
imported nearly as universally as WitnessBuilder, so the same 'one recent commit
to a near-universal module' dynamic applies -- but to a module that genuinely
CAN change values, which is the difference. Whether those 1,171 actually moved
is a re-run question this detector does not settle; AGENTS.md's measured rate on
the sibling triage is 39 percent.

A SECOND ERROR, recorded because it failed silently: my first draft listed
'computations/witness_base.py'. The file is at
'computations/substrate/witness_base.py'. The wrong path matched nothing, so
attribution fell through to the next provenance module and the fix LOOKED like
it had worked -- the headline moved, the top entry changed, and only the module
name gave it away. A path-based exclusion list needs its entries verified to
exist; noted in the code.
