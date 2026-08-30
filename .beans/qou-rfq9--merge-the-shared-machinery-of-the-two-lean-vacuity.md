---
# qou-rfq9
title: Merge the shared machinery of the two Lean vacuity text-detectors
status: completed
type: task
priority: normal
created_at: 2026-08-27T11:56:04Z
updated_at: 2026-08-30T09:56:31Z
---

Measured 2026-08-27. Two text-level detectors now exist for the same defect
FAMILY, built ~3 weeks apart, and I did not find the first before writing the
second — a corpus-grep failure on my part (bean qou-0avp; the existing one is
bean qou-k9yt, still at `todo`).

    scripts/lean-definition-collapsed-audit.py   (2026-08-08, qou-k9yt)
    scripts/lean-borrowed-name-audit.py          (2026-08-26, qou-0avp)

## They are NOT duplicates — measured, and this is the useful part

    my 19 CRITICAL flagged by the existing tool at any tier :  0 of 19
    my 115 major flagged by the existing tool at any tier    : 21 of 115  (18%)
    its 1 CRITICAL flagged by mine at any tier               :  0 of 1

The discriminating signals are different and find near-disjoint populations:

- definition-collapsed keys on docstring-says-OPEN + proof-is-definitional.
  Its CRITICAL count is 1 because the corpus was drained of that shape in #4741.
- borrowed-name keys on a name invoking a MATHEMATICIAN + local-only defs +
  cheap proof, with OVERCLAIM (docstring OVER-claims) as the mirror signal.

## What IS duplicated, and should be shared

The generic machinery, written twice:
  - the COLLAPSED signal (rfl / trivial / short simp-unfold over a same-file def)
  - the binder-field exclusion (proof discharges via `C.field` / `h.foo` ⇒ a real
    conditional derivation, skip). Both implementations arrived at this
    independently and it is the same rule.
  - docstring extraction above a decl; comment blanking; local-def resolution.

Proposal: factor these into one module both import, keeping the two
discriminating signals as separate front-ends. Do NOT merge the front-ends —
their populations barely overlap, and collapsing them would bury one tier's
signal in the other's ~1880/~1030 advisory noise.

## The Lean-side sharpening qou-k9yt asked for now EXISTS

That bean's "Caveat / future work" says the advisory tier could only be sharpened
by "a Lean-side check (does the statement still hold with the defs made
opaque?)". scripts/lean/BorrowedNameKernel.lean does exactly that, via
`Meta.isDefEq` under `forallTelescopeReducing` — 42 modules / 615 theorems / 102
collapses so far (docs/audits/2026-08-26-kernel-defeq-sample.witness.json).

It INDEPENDENTLY reproduced that tool's single surviving CRITICAL,
`qInt_eq_canonical` — which on inspection is a false positive for both of us:
its docstring says "The two are definitionally the same object, so the
consolidation here is this equation — checked, not asserted", i.e. a
compatibility lemma that SHOULD be `rfl`. Good calibration: defeq_collapse is a
candidate, never a verdict.

Blocked on nothing. Whoever takes it should also decide whether qou-k9yt's
`--strict` CRITICAL gate belongs in the (currently dispatch-only) CI.


---

## 2026-08-27 — done, and the unification CORRECTED a published count

Branch `claude/lean-vacuity-detector-shared-machinery-2026-08-27`.
Shared module: `scripts/lib/lean_decl_scan.py`. Selftest:
`scripts/lib/test_lean_decl_scan.py` (12 regression cases, all from bugs
actually hit). Full measured delta: `scripts/lib/lean_decl_scan_delta.md`.

Both front-ends kept separate, as this bean proposed — only the substrate is
shared (comment blanking, decl spans, docstring lookup, binder extraction,
the binder-field exclusion).

**The headline is not the deduplication, it is what it exposed.**

    lean-definition-collapsed   1 CRITICAL / 2047 adv  ->  1 CRITICAL / 2100 adv
    lean-borrowed-name         19 CRITICAL /  115 maj  -> 25 CRITICAL /  145 maj

The borrowed-name figures 19/115, published in PR #5875 (merged), were
UNDER-COUNTS from a real bug: a declaration body ran to the next declaration
head, so `end Foo` and `omit [...] in` lines were read as part of the proof.
`:= by decide` became `by decide\n\nend Trefoil`, which fails every
"proof is short/trivial" test. 25/145 are the corrected numbers.

Every adjudication made under the old counts stays valid — each verdict is
about a named declaration and none changed. Only the denominator grew. Exactly
one verdict is orphaned (`euler_machinery_misses_dt_count`, `legit`); kept and
annotated rather than deleted.

Three further defects found by measuring, not by reading:

- `definition-collapsed` never blanked comments, so it scanned declarations
  QUOTED INSIDE DOCSTRINGS. `blochWignerD_real_pos` does not exist — it is
  quoted in a module docstring recording its own removal for being a banned
  tautology. The detector was flagging a theorem from its obituary.
- The same gap hid real proofs: `b3_nf_wedderburn_uniqueness` carries comments
  between its name and its statement, so its `:= rfl` was invisible. That one
  is already adjudicated `genuine` by the other detector — blanking recovers a
  known true positive this detector structurally could not see.
- The binder-field exclusion fired on ordinary dot-notation over a VALUE binder
  (`A.choose` where `A : ℕ`). `assumption_binders` now restricts it to
  instance brackets, Prop-ish types and the `h`-prefix convention; applying it
  to borrowed-name moved 8 items advisory -> major.

Deliberately NOT applied, and measured enough to be a real proposal: signal B
should read `--` comment blocks, not only `/--` docstrings.
`b3_nf_wedderburn_uniqueness`'s prose says "Full proof requires Wedderburn-Artin
over R_q" — a textbook OPEN-CLAIM — in `--` comments where signal B cannot see
it. That would move the `definition-collapsed` CRITICAL count, the one
published tier this change leaves untouched, so it deserves its own decision.

Still open from this bean: whether `--strict` belongs in CI. CI is
dispatch-only here, so it would not fire on push anyway.


## Follow-up 1 closed 2026-08-30 (PR #6168) — and its diagnosis was half wrong

The recorded follow-up said signal B should read `--` comment blocks, naming
`b3_nf_wedderburn_uniqueness` as the miss. Implemented and measured:

| change | CRITICAL | findings |
|---|---|---|
| baseline | 2 | 2255 |
| comment cone only | **2** | **2255** |
| cone + vocabulary | 3 | 2255 |

**The comment cone alone is a NO-OP.** Zero findings move, zero severities
flip, `cone_only` = 0. The second, unnamed defect is `DOC_OPEN`'s vocabulary:
the declaration says "Full proof **requires** Wedderburn-Artin" and "The formal
proof **needs:** Wedderburn", and the pattern had `needs the` / `unproved` and
nothing for `requires` (`needs the` does not match `needs:`). Jointly
necessary, individually insufficient.

Vocabulary stayed narrow on measurement: a bare `needs|requires` net matches 29
of the 2252 advisory cones and hand-adjudicating all 29 gives **0** proof-
absence admissions — all ordinary prose about hypotheses. 29 FP for 0 TP.

**The +1 is corroboration, not new coverage.** That declaration is already in
the review ledger under `proof-borrowed-name`, verdict `genuine`, `file_sha`
`2f1fc03ae00a` still current. Borrowed-name reads the NAME against the proof;
definition-collapsed reads the PROSE against the proof. Two independent signals,
one verdict, one ledger row.

Follow-up 2 (`--strict` in CI) remains moot while CI is `workflow_dispatch`-only.
