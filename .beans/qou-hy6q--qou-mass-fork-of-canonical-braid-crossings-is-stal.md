---
# qou-hy6q
title: qou-mass fork of canonical_braid_crossings is stale — no averaged_weighted
status: todo
type: task
priority: normal
created_at: 2026-08-14T19:41:56Z
updated_at: 2026-08-14T20:07:07Z
parent: qou-1295
---

Confirmed against current main: qou-mass/src/qou_mass/_internal/canonical_braid_crossings.py is ~95 lines behind computations/ -- no _avg_color_delta, no averaged_weighted, no CTYPES, no d_for_ctype delta= kwarg. Its siblings hoefsmit_symbolic / markov_weights_symbolic / isotope_record_schema carry the same stale {sigma, sigma_inv, averaged} vocabulary. Not touched in PR #5029: qou-mass is a published PyPI facade and a version bump is a release decision, not a sweep. Scope when picked up: decide fork-vs-vendor first.
