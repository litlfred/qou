---
# qou-kt8o
title: The ck-dk registry JSON twin never absorbed the dc_3/dq 3.84e6 correction, and a green probe assertion still pins the stale 4.6e6
status: in-progress
type: bug
priority: normal
created_at: 2026-08-29T01:22:39Z
updated_at: 2026-08-29T03:02:08Z
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


---

## RESOLVED for the machine-readable + live-code + Lean sites (PR #5942)

**Landed:**

1. `docs/coordination/ck-dk-registry.json` — the c_3 rung note now reads
   `-2.375%` / `3.84e6` with the correction's provenance inline. Its `.md`
   twin had carried the fix since 2026-08-25; the JSON had not.
2. `qbeta_qbessel_crossanchor_smoothness_refutation.py` — the inverted
   AUTH/SCOPE labels swapped to `_LIVE`/`_SUPERSEDED`, the assertion re-pointed
   at the live pair and the registry's 3.84e6, and a **second** assertion added
   pinning what the superseded value produces, so the corpus's 4.6e6 stays
   *traceable to its cause* rather than merely wrong. Both pass; the verdict is
   untouched (the assertion the refutation rests on is `> 1e6`, indifferent to
   which c_3 is used — the point of stating it at 1e6).
3. `qbeta_habiro_residual_probe.py` — `2.98`/`4.6e6` -> `2.3748`/`3.84e6`.
   Neither constant enters arithmetic, so no computed number moved.
4. The **three Lean docstrings** (`SRigidityPrune`, `ImQAnchorCarrier`,
   `ThetaLipschitzObstruction`). Docstring-only; `check-sidecars.sh` clean.

**The nicest part: one of them had already caught this.**
`ThetaLipschitzObstruction.lean`'s honesty boundary read *"Recomputing dS/dq
from the tabulated anchor values gives 3.84e6; the registry quotes ~4.6e6 …
they do not agree exactly and no attempt is made here to reconcile them."*
Someone measured it, saw the registry disagree, flagged it instead of papering
over it, and left it open. **That file was right and the registry was stale.**
Question closed in place.

## Still open

* **Root cause, untouched:** `qbeta_eigenphase_taylor_in_u.py:91` carries
  `C3_EMP_MUON = mpf("-2.0097")`. Changing it MOVES NUMBERS, so it needs its
  own commit with the blast radius measured — not a currency fix.
* **~50 prose sites** remain, mostly dated audit docs that `qou-3nva`
  deliberately preserves as historical records. Not overriding that.
* **AGENTS.md's own site list is wrong** (*"five other sites … audit docs and
  `local/compute-author` §precedent-table"*) — measured 55 files: 7 .json,
  3 .lean, 29 .md, 16 .py. It names neither Lean nor `computations/`. Worth a
  one-line correction there.
* **Nothing validates `ck-dk-registry.json` against its `.md` twin.** That is
  why this drifted for four days after the .md was fixed, and it will drift
  again. `kernel_constraints_registry_validate.py` covers a different file.

## A second-order note

AGENTS.md's corrected `3.8375e6` (route 1, secant) is now itself ~0.7 % stale:
the muon anchor moved to CODATA 2022 in `fca08de7d`, so the live secant gives
**3.812e6**. Route 2 (`2.37/u³`) is unaffected at **3.832e6** and reproduces
AGENTS.md exactly. Nothing turns on it; recorded so the next person re-deriving
does not think they have found a third figure.


## 2026-08-29 — the last two .lean, and AGENTS.md's own count

FaddeevModularDouble.lean was the worst of the five .lean sites: it carried the
superseded muon c_3 = -2.0097 ITSELF, not just the derived slope, plus both of
that value's arithmetic consequences. The stale pair reproduces its 4.66e6 and
4.4e-7 to every digit shown (live: 3.83925e6 / 5.39e-7) — that reproduction is
what identifies a figure as the stale twin, and is the cheapest available test.
MeridianHolonomyAnchorCarrier.lean needed only the slope; its argument turns on
the ORDER O(10^6), which both values satisfy, so nothing downstream moved.

lean-direct exit 0 on both against the real import cone (LEAN_PATH over the 19
restored olean dirs). Note the trap: oleans live under .lake/build/lib/lean/,
not .lake/build/lib/ — pointing LEAN_PATH at the latter fails with 'unknown
module prefix Mathlib' AND STILL EXITS 0, so the exit code alone is not a check.

AGENTS.md's 'five other sites … audit docs and local/compute-author
§precedent-table' is wrong twice over. Measured on origin/main excluding
.beans/: 43 files / 71 lines with c_3 named on the same line, or 88 files
allowing adjacent-line context — 10-20x. And the characterisation misses both
groups that matter: the largest is computations/qbeta (20 files), live probes
and producers that RECOMPUTE the figure, and the 5 .lean go unmentioned.

Measurement caution for whoever re-runs this: my first pass said 132 files
because I included the '0.0596' spelling unguarded. 66 of 78 of those hits were
coincidental prefixes (0.05968895…, 0.05963573…) in unrelated witnesses. The
figure has three spellings — 4.6e6, 4.66e6, Delta c_3 = 0.0596 — and only the
first two are safely greppable on their own.

Corrected AGENTS.md accordingly, including an explicit 'do not sweep the
remainder blind': most survivors are dated audit docs (qou-3nva's standing
decision, not overridden) or witness description fields that cannot be fixed
without re-running their producer.

Also fixed the #5942 PR body, which still asserted the route-1 3.812e6 and the
'AGENTS.md is ~0.7% stale' claim I had already retracted in a comment. A
retracted claim left standing in a PR body is the same defect class this bean
exists to drain.
