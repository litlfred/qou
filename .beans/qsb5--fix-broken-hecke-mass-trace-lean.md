---
# qsb5
title: Fix broken QOU/Braiding/hecke_mass_trace.lean (missing invR arg, pre-existing)
status: completed
type: task
priority: normal
tags:
    - qa-drain
    - lean
created_at: 2026-07-02T17:18:19Z
updated_at: 2026-07-04T22:56:57Z
---

Found during qsb2 stub-disposition work (2026-07-02): QOU/Braiding/hecke_mass_trace.lean does not compile — missing invR argument to HeckeAlgebra at line 52, cascading binder error. Also another §3b-cond projection carrier. Pre-existing on main, out of scope for PR #3222.
