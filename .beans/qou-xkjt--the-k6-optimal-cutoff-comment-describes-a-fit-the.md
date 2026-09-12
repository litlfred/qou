---
# qou-xkjt
title: The K=6 'OPTIMAL cutoff' comment describes a fit the code does NOT implement (live cap is 11)
status: completed
type: task
priority: normal
created_at: 2026-09-12T22:31:04Z
updated_at: 2026-09-12T22:59:21Z
---

## The escalation was half right, and the half that is wrong matters more

The LP-hunt agent (`qou-8urh`) flagged `hecke_core_legacy.py:397-400` as a live
anti-fit violation: it calls `K = 6` the *"OPTIMAL partition cutoff"* on the
strength of an *"Empirical sweep with q-heat resolvent damping"*, and AGENTS.md
§"NO FITTING" names *"Sweeping a discrete parameter for accuracy"* verbatim as
fitting.

**The text does describe a fit. The code does not implement it.** Measured on
`main`:

- `K_PARTITION_MAX = 11` (`:404`) is the live constant.
- Every production call site passes it: `:1694`, `:1720`, `:2584`, `:2758`,
  `:2806`, `:2947` all use `k_cap = K_PARTITION_MAX` / `k_max=K_PARTITION_MAX`.
- The docstring at `:1790` confirms the live default: *"defaults (k_exact =
  k_max = K_PARTITION_MAX = 11)"*.
- **No production caller truncates at 6.** The only two live `k_*=6` call sites
  are `probes/uic_per_block_log_valley_scan_probe.py:167-168`, which pass
  `k_max=6` and `k_max=11` side by side *precisely to compare them* (this
  session's class-D valley scan), and `_deprecated/heavy_atom_opts.py:280`.
- The accuracy figures the comment cites — *"40Ca: 0.001 at K=6 -> 0.012 at
  K=9"* — appear **nowhere else in the tree**: no witness, no producer, no
  audit. Comment-only.

So the sweep was run, it recommended 6, and **6 was not adopted**. That is the
opposite of the anti-fit failure mode: it is a record of a fitted
recommendation that the corpus rejected in favour of the full partition set.

## What IS defective: the comment names three values for one constant

Reading `:389-404` top to bottom a reader is told the cap is 6, then 8, then 11:

| line | says |
|---|---|
| `:390` | "**K = 6** covers H₂..H₆ (24 partitions in total: 2 + 3 + 5 + 7 + 11)" |
| `:396` | "`K_PARTITION_MAX` is capped at **8** because empirical sweeps show the" — sentence truncated mid-clause, no verb |
| `:398` | "**K = 6** is the OPTIMAL partition cutoff" |
| `:404` | `K_PARTITION_MAX = 11` |

And its arithmetic is wrong in its own terms: `2 + 3 + 5 + 7 + 11 = 28`, not the
24 it claims. (Those are `p(2..6)`; at the live cap the figure is
`sum p(2..11) = 193`.) Verified by direct computation, both sums.

## Why this is worth fixing rather than leaving

An agent running the anti-fit audit reads `:398`, finds the phrase AGENTS.md
names verbatim, and reports a live fit in the binding compute — which is what
just happened. The comment manufactures a false positive against the
framework's own most-guarded discipline, and it does so in the file that
carries `unified_iterative_correction`. A reader cannot tell from the comment
which of 6/8/11 governs; only the code says.

## Disposition

Fixing this is **exemption 2** of the ASK-OWNER gate (*"derived from the
corpus"*): the file's own live constant one line down decides the answer, and a
reviewer checks the fix by reading `:404` rather than by trusting my reasoning.
No number moves — the change is comment-only.

**Not doing it here.** It rides on the gate-drop PR, which edits this same file
(`:2183-2188`) and carries the same defect class: an owner-ruled correction that
landed at `:328-374` and never reached the reasoning it invalidates 1,800 lines
down (`:2079-2084`). One comment-hygiene pass over `hecke_core_legacy.py`, not
two.

**Still open** (not for me): whether the rejected sweep should be *recorded* as
a negative result — "K=6 was measured to be more accurate and was not adopted,
because accuracy is not the ranking criterion" is exactly the kind of honest
negative AGENTS.md calls the corpus's most reusable output, and it is currently
only half-written, in a comment that reads as an endorsement.

---

## DONE 2026-09-12 — PR #7253, riding the gate-drop tranche as planned

The comment at `hecke_core_legacy.py:389-404` is rewritten. It now:

- **states the live cap first** (`K_PARTITION_MAX = 11`, `Σ_{k=2}^{11} p(k) = 193`
  partitions) and names the six production call sites that pass it as their
  default, by line;
- **quotes the three superseded values verbatim** (`K = 6` at `:390`, "capped at
  8" at `:396` with the truncation marked, `= 11` at `:404`) so the reader can
  see what was wrong rather than only what is right;
- **corrects the arithmetic**: "24 partitions in total: 2 + 3 + 5 + 7 + 11" —
  that sum is **28** (and it is `p(2..6)`, not the live set). Both sums verified
  by direct computation, not asserted;
- **finishes the truncated sentence** by deleting it, since the clause it began
  ("capped at 8 because empirical sweeps show the") asserted a cap the code does
  not have;
- **records the sweep as the honest negative it is**: the sweep ran, recommended
  6, and **6 was rejected**. AGENTS.md names "sweeping a discrete parameter for
  accuracy" verbatim as fitting and says accuracy is not the ranking criterion,
  so the rejection is the discipline working. Written up as an endorsement, it
  manufactured a false anti-fit positive against the framework's own
  most-guarded rule — which is what happened, and is why this bean exists;
- **retains the channel inventory** (volume, surface, Coulomb, asymmetry,
  pairing, exchange, shell, hook, Wigner, form factor, pn correlation,
  `[3,2,1]`, `[4,1,1]+[3,1,1,1]`, `[4,2]+[2,2,1,1]`), scoped as a subset of what
  is enumerated at the live cap rather than as the whole of it.

Comment-only, no number moves. **Exemption 2** of the ASK-OWNER gate, as this
bean predicted: a reviewer checks by reading the constant at `:434` (it moved
from `:404` because the comment grew).

The "still open" item this bean left for someone else — whether the rejected
sweep should be *recorded* as a negative result — is **closed by the rewrite**:
it is recorded, in the comment, at the site where the misreading happened.

Re-verified while editing: no production caller truncates at 6; the only live
`k = 6` sites remain `probes/uic_per_block_log_valley_scan_probe.py:167-168`
(passing 6 and 11 side by side to compare them) and
`_deprecated/heavy_atom_opts.py:280` (a different parameter).
