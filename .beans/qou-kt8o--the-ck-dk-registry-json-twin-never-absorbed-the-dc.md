---
# qou-kt8o
title: The ck-dk registry JSON twin never absorbed the dc_3/dq 3.84e6 correction, and a green probe assertion still pins the stale 4.6e6
status: in-progress
type: bug
priority: normal
created_at: 2026-08-29T01:22:39Z
updated_at: 2026-08-29T01:23:27Z
---

Found working the `dc_3/dq ≈ 4.6×10⁶` staleness. **The interesting part is not
the prose — it is that a correction landed in the authoritative `.md` and its
machine-readable twin never absorbed it, because nothing compares them.**

## The settled value, re-derived rather than trusted

Three routes, computed here from the live pins:

    ROUTE 1  secant, live anchors      dc_3/dq = 3.812e6
    ROUTE 2  2.37/u³ at u = 0.00852    dc_3/dq = 3.832e6
    (AGENTS.md quotes 3.8375e6 by route 1 and 3.8320e6 by route 2)

Route 2 reproduces AGENTS.md exactly, and my `u = 0.0079595` needed to reach
4.7e6 matches theirs. Route 1 differs slightly (3.812e6 vs 3.8375e6) **because
the muon anchor moved to CODATA 2022** in `fca08de7d` since that figure was
written — so AGENTS.md's own corrected number is now itself ~0.7 % stale. No
conclusion turns on it.

**Where 4.6e6 comes from is now certain.** `qbeta_qbessel_crossanchor_smoothness_refutation`
computes BOTH and prints them side by side:

    [authoritative] c_3: -2.0693 -> -2.0097   dc_3/dq₀ = 4.6552e+6
    [scope_phi2   ] c_3: -2.0693 -> -2.0202   dc_3/dq₀ = 3.8351e+6

`-2.0097` is the **pre-#1422 superseded** muon c_3; `-2.0202` is live (registry
§3 records `−2.06934258 / −2.02020024`). So 4.6e6 is exactly the stale-c₃ twin
AGENTS.md says it is — confirmed by the corpus's own probe.

## Three live defects (not prose)

1. **`docs/coordination/ck-dk-registry.json`** still says `dc_3/dq ~ 4.6e6`.
   Its `.md` twin `ck-dk-canonical-registry.md` §3 **was corrected** on
   2026-08-25 (PR #5765), with the correction written out in full. The JSON is
   the machine-readable authoritative form and it now contradicts the document
   it twins. **Nothing catches this:** `kernel_constraints_registry_validate.py`
   validates `kernel-constraints-registry.json` (§9), a *different* file.
   `ck-dk-registry.json` has no validator at all.

2. **`qbeta_qbessel_crossanchor_smoothness_refutation.py`** labels the
   superseded value "authoritative" and the live one a "sensitivity check" —
   backwards — then hard-asserts

       "authoritative dc_3/dq₀ ≈ 4.6e6 ... within 10%"

   which **passes**, pinning the stale figure. Against the live c_3 the same
   assertion would read 3.835e6 vs 4.6e6 = 17 % and FAIL. A green assertion
   enforcing a superseded number is worse than a red one.

3. **`qbeta_habiro_residual_probe.py:85`** — `C3_DCDQ = mp.mpf("4.6e6")`,
   commented *"Registry-settled ... ck-dk-canonical-registry.md §3"*. §3 now
   says 3.84e6, so the comment's own citation refutes the value.

## Root cause, NOT fixed here

`qbeta_eigenphase_taylor_in_u.py:91` carries `C3_EMP_MUON = mpf("-2.0097")` —
the superseded constant every downstream 4.6e6 derives from. **Changing it moves
numbers**, so it is reported rather than edited: that is a value change and
needs its own deliberate commit with the blast radius measured.

## Scope

55 files carry the stale figure in prose (7 .json, 3 .lean, 29 .md, 16 .py) —
far more than AGENTS.md's "five other sites". Most are **dated audit docs**,
which `qou-3nva` explicitly decided to leave as historical records of the
analysis; that decision stands and I am not overriding it. This bean covers the
machine-readable and live-code sites only.
