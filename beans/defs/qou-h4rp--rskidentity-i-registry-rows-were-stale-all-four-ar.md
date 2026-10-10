---
# qou-h4rp
title: 'RSK/Identity-I registry rows were stale: all four are sorry-free unconditionally'
status: completed
type: task
priority: normal
created_at: 2026-08-25T20:04:00Z
updated_at: 2026-08-25T20:04:41Z
---

## MEASURED 2026-08-25 — the four `sorryAx` rows were STALE; all are clean

Task was "verify the 5 remaining registry modules (70 builds); low value, four of
seven entries are `sorryAx` by design." **That prediction was mine and it was wrong.**
The build took 753 s (70/70 exit 0) and overturned the registry.

**All four supposedly-known-bad entries are sorry-free**, and so are their
UNCONDITIONAL forms:
- `OVTopAssembly.sum_numSYT_sq_eq_factorial`  (`Σ_λ #SYT(λ)² = n!`)
- `RSKBurnsideDischarge.rskBurnsideHolds`
- `PlancherelNormalisation.sum_sytDim_sq_eq_factorial`
- `PlancherelNormalisation.nuV_top_closed_form_unconditional`

Cause: the in-repo Robinson–Schensted development — **40 `QOU.Mathlib.Schensted*`
files, 5 sorry tokens between them**, landed via PR #5745 — plus the keystone
instance. Nobody noticed because the gate needed a 70-module build to run, so the
registry kept asserting a gap that had already closed.

## `clean` alone was NOT sufficient evidence, and I treated it as a red flag

All four carry `[SnIsotypicSpechtSplit ℚ]`, so each proves an IMPLICATION.
`#print axioms` cannot see an undischarged instance hypothesis — a declaration can
go `sorryAx` -> `clean` with ZERO new mathematics by moving the obligation into a
class binder (§3b-cond; "conditional-proved ≠ premise-established"). Checked three
ways before believing it:
1. the instance `instSnIsotypicSpechtSplit` is itself sorry-free — yes;
2. each theorem composed with the ambient instance is sorry-free — yes, all four;
3. the composition elaborated with **exit 0**. This one matters: a draft that failed
   to elaborate reported `sorryAx` from *error recovery*, which is not a finding and
   would have been misread as a defect.

## Hardening added

Pinned `instSnIsotypicSpechtSplit` in the registry. The four theorems being `clean`
is **not** self-sustaining: they are conditional, so they stay green even if the
instance is weakened or acquires a `sorry`. The instance is the only place such a
regression can be caught.

## Still open (unchanged)

RETRACTED — see the correction appended below. (Original text: "The Specht
core still carries ~500 sorry tokens across 36 modules"; the four
headline results simply do not route through them. Getting to zero repo-wide
remains the multi-session program in
`docs/scope/2026-06-24-identity-i-plancherel-snrep-infra-program.md`.

## Correction for that scope doc

It records the rep-theory route as blocked by "`RepresentationTheory` oleans absent
+ unfetchable". Those oleans are now present (30, incl. `Maschke`, `Character`,
`FDRep`). The route is **still** blocked, but for a deeper reason: Mathlib at this
toolchain has `FDRep.char_orthonormal` yet **no** `Irrep` type, no completeness, no
regular-rep decomposition — so `Σ dim² = |G|` is not available off the shelf.
Fetching oleans does not unblock it, and a future reader of that doc would think it
does.


## RETRACTION 2026-08-25 — the "~500 sorry tokens" figure was mine and was wrong

It counted the WORD `sorry` in comments and docstrings. Re-measured with a
comment-stripping parser, validated by a 7-case selftest (term-mode, tactic-mode,
line comment, block comment, docstring, `sorryAx` mention):

**The QOU Lean tree has ZERO `sorry` in code across all 2200 files.** Also zero
`sorryAx` and zero `: True :=`. `SpechtStandardBasisCore` supplied 101 of the
phantom hits and has none; its docstring says "its single honest straightening
stub" and I read past that too.

The real residual assumption surface is **24 `axiom` declarations in 15 files**
plus **1 `native_decide`** — the vector a sorry count cannot see. Clusters:
Hecke/Markov trace 7, SDP 5, Hoefsmit 3, central idempotents 3, analysis 4, misc 2.
