---
# qou-xik5
title: 'W1: audit MarkovTrace class fields — is Wenzl positivity actually needed, or surplus like PSD in #4151? (re-scope the gap before building)'
status: completed
type: task
priority: normal
created_at: 2026-07-25T13:00:16Z
updated_at: 2026-07-25T13:37:18Z
parent: qou-utb3
---


## W1 findings (2026-07-25, branch claude/markovtrace-w1-audit-2026-07-25)

**VERDICT: Wenzl positivity is SURPLUS** (scope (a), the #4151 PSD pattern).
Full evidence: `docs/audits/2026-07-25-markovtrace-w1-class-fields-audit.md`.

- Class `QOU.Machinery.MarkovTrace` (MarkovTraceOnHecke.lean:62-71) has exactly
  3 fields: `cyclic` / `map_add` / `map_smul`. No positivity field, and none is
  statable over `[CommRing R]` (no order/star — §7c, ordering is post-wall).
- Only consumer file: `TauFunctorReduction.lean` — `cyclic` at :82, `map_add`
  at :92; `map_smul` had zero consumers (new `observationFrame_smul` lemma now
  consumes it — class is witnessed-minimal). No consumer touches positivity.
- Instances already exist at n=2 (`H2A`, HeckeH2AlgebraInstance.lean:131) and
  n=3 (`markovTrace_H3A`, HeckeH3AlgebraInstance.lean:120), both generic
  `[CommRing R]`, zero positivity.
- (M3)/normalization is NOT a class field; the tower consumer runs through the
  separate `MarkovStabilization` class (also positivity-free).
- Minimal construction: (b) close n=4 now (gen_gram_closure.py →
  `MarkovTraceH4Gram` discharges `gram_symm`; wrap `H4A` like `H3A`) + (a)
  Ocneanu E_n tower for generic n WITHOUT `WenzlTowerStep` in the hypothesis
  set.
