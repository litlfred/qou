---
# qou-mfas
title: 'Route 76 reaches 10_100 under modStd: correct the G6 ceiling to scope-(a)'
status: completed
type: task
priority: normal
created_at: 2026-08-25T16:25:43Z
updated_at: 2026-08-25T16:40:20Z
---

## LANDED — PR #5772 (2026-08-25)

modStd reaches 10_100 (14 tets): **32.5s class 0, 38.8s class 1**, dim 0,
15 eliminants each. Class-1 eliminant degrees {20, 26, 38} factor as
14+6, 14+12, 14+24 — companion varies, 14 in every one, so the geometric
component is selected intrinsically. All three degree-14 factors give
field disc **75015471937637449** = Route 75's shape field.

G6 re-scoped (b) -> (a) in place: numbers kept, superseded sentence
retained beside its correction, `beats_route_75_reach` left False with
two new keys naming its scope.

**Trap pinned:** Singular auto-enables `short` output when every ring
variable is one character, dropping `*` and `^` (`x^14` -> `x14`). Silent
class: `x14+x13` parses as a legal LINEAR polynomial in two variables.
Fixed with `short = 0` plus a consumer-side refusal on `\bx\d`.

**Corrections to my own prior reporting:** I had quoted 42.04s (matches
neither class); and 11a1 remains untested here, not rescued.
