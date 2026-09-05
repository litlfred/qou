---
# qou-gpb5
title: 'Implement the multi-level character ratio: quark and nuclear-jet levels are unbuilt'
status: todo
type: task
created_at: 2026-09-05T06:49:42Z
updated_at: 2026-09-05T06:49:42Z
---


Opened 2026-09-05. The **nucleon level is now implemented**
(`the_character_ratio_derivation_path_is_the_bond_model_probe`, 3/3); this bean
is the two levels that are not.

## What the specification says

`prf:confined-knot-binding`: "the character ratio measures the volume departure
from the free constituents. The total knot factor multiplies these strict,
empirically-independent character ratios **across all levels**." It names three:
**quark, nucleon, and nuclear jet**.

`hecke_core_legacy.knot_factor` concedes it does not run this: "the per-level
character ratio (nucleus/free-nucleon product) and confined-state accumulation
provide the categorical derivation path. **Currently using the product formula
for A<=4 and generic for A>=5.**"

## What implementing the nucleon level established

The character ratio `R = tr_M(nucleus)/tr_M(free constituents)` on the canonical
word, exact at 200 bits, **equals `exp(-L)` to the working floor**. So the
specified path and the bond model are the same object, and retiring the
knot-selection routes leaves no second unfitted channel in reserve.

| atom | R | B = -alpha log R | B_AME | error |
|---|---|---|---|---|
| 2H | 0.508229789377 | 2.8332 | 2.224566 | +27.36 % |
| 3H | 0.205135640449 | 6.6309 | 8.481796 | -21.82 % |
| 3He | 0.311386312073 | 4.8839 | 7.718041 | -36.72 % |
| 4He | 0.125684152895 | 8.6817 | 28.295662 | -69.32 % |

And the hardcoded factor is **not an approximation** to it: `1 - h^2 = 0.9563`
against a true ratio of `0.2051` / `0.3114`, and `(1-h^2)^2 = 0.9145` against
`0.1257` — off by 4.7x, 3.1x and 7.3x.

## Why the missing levels matter

Every character ratio is `< 1`, so multiplying in further levels drives `R`
**down** and `B = -alpha log R` **up**. The nucleon level alone leaves `4He` at
`-69 %`, i.e. short. So the missing levels move it in the right direction. That
is a direction and not a prediction, and nothing measured estimates their size —
this bean exists to find out, not to assume.

- [ ] Establish whether the quark level has a computable word at all. The
      substrate has quark-level structure (three strands per nucleon), so the
      "free constituents" at that level may be the three free quark strands and
      the "nucleus" the intra-nucleon word. If so it is the SAME engine with
      `include_inter=False` at one level down, and is cheap.
- [ ] Same question for the nuclear-jet level.
- [ ] If both are computable, multiply the three ratios and report. Do NOT tune
      anything: if the product overshoots or undershoots, that is the answer.
- [ ] If they are not computable, say so plainly and close. The specification
      would then name levels the framework cannot evaluate, which is itself the
      finding.

## Discipline

No fitting. This is the only unfitted binding route left after the 2026-09-05
ruling, and its value is precisely that it is unfitted — a number obtained by
computing beats a better number obtained by selecting. If the three-level
product misses, record the miss.
