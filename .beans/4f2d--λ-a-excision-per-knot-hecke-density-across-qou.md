---
# 4f2d
title: 'λ_A excision: per-knot Hecke density across QOU'
status: completed
type: milestone
priority: normal
created_at: 2026-06-24T01:21:09Z
updated_at: 2026-08-08T22:13:01Z
---


## 2026-08-08 — this milestone appears finished; every child is closed

Picked up as live work (owner: "ok to overlap"). It is not live, as far as the
record shows. **Every child bean is `completed`** — `0voz`, `3pe5`, `ki79`,
`stv9`, `x5az` — as is the session bean `zeu7`, which records the milestone
superseded by the 2026-06-24 owner ruling and closed in #3340. This bean itself
is `in-progress` **with an empty body**, so nothing here says otherwise.

Re-verified in the corpus rather than trusting the beans (PR #4822):

* `vol_density_borromean` and `mass_vol_density` both emit `DeprecationWarning`;
  `vol_density_borromean_spectral` calls the former, so it inherits it.
* `mass_vol_density()` still has **zero external callers**.
* `noncanonical_reentry_audit.py`: **0 re-entry violations / 2104 scripts**.
* Two functions compute the deprecated `Vol·ρ/ℏ_q²` shape unguarded —
  `vol_density_vd` (docstring: *"the purge target"*) and
  `vol_density_borromean_bring_color_weighted`. Neither is a live hole:
  `vol_density_vd` has **zero** callers, and the other's only caller is a probe,
  which guardrail §3 permits. Recorded as known-empty, not fixed — a warning
  there would fire only in legitimate exploratory use.

One real defect found and fixed in #4822: `mass_table_comprehensive.py`'s
docstrings still advertised the removed λ_A form as "the current production
infrastructure" while the code below used the `canonical_mass` facade. Compute
was correct; the prose was two years of drift. Guard extension + the `\bNOT\b`
regex bug that hid it are in the same PR; the untriaged remainder is `qou-efcv`.

**Status left `in-progress` deliberately — closing is the owner's call.** If the
axis is done, this is a candidate to close.

### For `qou-3wc5`

Fourth instance of the stale-summary pattern, and one the proposed `status:`
check would miss: this bean's own status is `in-progress`; it is the **parent**
that is stale relative to its children. Suggested extra rule — *a milestone with
no open children and no body is a candidate stale parent.*

## 2026-08-08 — closed by the owner

Owner authorised the close against the #4822 evidence above. Status
`in-progress` → `completed`. The axis is done: the compute carries the
2026-06-24 canonical-mass ruling, the last stale prose is fixed, and the
remaining untriaged guard hits are tracked separately as `qou-efcv`.
