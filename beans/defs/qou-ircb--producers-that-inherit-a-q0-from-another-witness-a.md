---
# qou-ircb
title: Producers that INHERIT a q0 from another witness are stamped from a manifest that cannot know it
status: todo
type: task
priority: normal
created_at: 2026-08-24T13:34:53Z
updated_at: 2026-08-24T14:28:34Z
---

## What it is

A producer reads a q0 out of another producer's `*.witness.json` and computes
with it. Its own witness is then stamped by `witness.py` from its stem in
`q0_anchor_manifest.json`. Those two facts are independent: the manifest says
what the producer is *supposed* to be pinned at, the upstream witness carries
whatever it *is* pinned at today. Re-pin the upstream and the producer silently
follows while its stamp does not move.

Worked instance, and the one this was found on:
`parabolic_cylinder_channel_mixing_probe` — listed `ideal_muon`, so stamped
`q0Anchor: "muon"`, while `constants.q_0` in its witness is the **proton** pin,
copied verbatim from `binding-bar-even-odd-probe.witness.json` which main
re-pinned. The value reaches the arithmetic (`gamma_q_gt1(x, q0)`, line 92,
read at line 67); there is no `add_parameter` in the file, so this is **not**
the stamp-only class the aK retraction (`83de3b847c`) covers.

## Five gates, none of which can see it — measured, not reasoned

| gate | its question | verdict |
|---|---|---|
| `q0_anchor_consistency_audit` | stamp vs itself | `Q0_OK` |
| `anchor_flip_straddle_audit` (BLOCKING, `fa2794159b`) | does output move under `QOU_Q0_ANCHOR`? a q read from a FILE does not | **clean** |
| `q0_producer_pin_classifier` | accessors / imports / muon artifacts / 50-digit literals | `('none', [])` |
| `tnjb_stale_stamp_migrate` | producers the classifier resolves *proton* | `none` ⇒ excluded |
| `q0_anchor_contradiction_triage` | witnesses declaring **proton** | declares muon ⇒ out of scope |

None is wrong about its own question. The gap is that **nothing compares the
stamp against the numbers in the same file.**

## The control that settles intent

`defect_weighted_zero_point_probe` and `zero_point_channel_energy_probe` read
the **same** upstream witness by the **same** expression and are listed
`physical_proton`. Three readers of one file, two proton and one muon, is one
row disagreeing with its own input — not a layer-policy choice.

## Fixed here, and the fix moved no number

Manifest → `physical_proton`, witness regenerated **in the same commit**
(AGENTS.md constraint 4: do not split the change). The regeneration moved
`q0Anchor`, `q0Value` and the environment record and **nothing else** — the
`qou-bdkx` (b) signature: payload right, declaration wrong.

## Detector

[`computations/audits/inherited_q0_pin_audit.py`](computations/audits/inherited_q0_pin_audit.py).
Full tree after the fix: **MISLABEL=0, agrees=3, undetermined=17**.

**Its own blind spot is how it was found.** A first pass keyed on *literal*
subscript keys and missed the very producer this bean is about, which spells
the key as a module constant (`Q0_KEY = "q_0"; src["constants"][Q0_KEY]`).
Module-level `str` constants are resolved now; a key built at runtime or
reached through a helper still escapes. `--selftest` therefore pins the
**key-resolution reach**, not the (now-fixed) MISLABEL verdict — a gate that
goes red when the bug it names is fixed is not a gate.

## What is left

17 `undetermined`. Two causes, and they need different work:

1. the upstream filename does not resolve statically (`upstream=?`) — the path
   is assembled rather than named;
2. the producer is **ABSENT** from the manifest, so there is no declared class
   to compare the inherited pin against.

(2) is the more interesting half: an absent producer inherits a pin with
*nothing at all* asserting what it should be.


---

## Correction (same session): 17 undetermined was a detector artifact, not a corpus fact

The tally above read `undetermined=17`. Live figure is **7**. The difference
was not corpus drift — it was my own upstream resolution, and three of its
answers were **wrong**, not merely missing:

| spelling | what it reported | truth |
|---|---|---|
| regex over raw source with `re.S` | ran past the assignment it matched onto the next witness name — usually a **print string** | `hoefsmit_stage_b` reads `free-neutron-decay` (189) and prints its own name (529) |
| last-write-wins handle dict | `with open(out, "w") as f` rebinds the same `f` as the read above ⇒ producer "reads its own witness" | `frakV_askey_wilson` reads the anchor-**defining** pin (118) ⇒ exempt |
| first-write-wins (the fix for that) | an **earlier** read's file ⇒ a second `MISLABEL` | `qbeta_decay_sdp_extended_ck`'s `qp` is the anchor-defining pin ⇒ exempt |

**I nearly wrote up a `SELF-INHERITED` class** — a producer bootstrapping its
pin from its own prior output, which would be strictly worse than the defect
this bean is about because re-running could never correct it. Two candidates,
both false, both my regex hitting an output path or a print. There is no
evidence for that class in this corpus. Checking the two before writing them up
is the only reason it is not in the record.

Resolution is now scope-aware: a `with` handle binds only to the `json.load`
**lexically inside its own block**, write modes are excluded, unresolved reports
`?`. Six rows that read the anchor-defining pin through
`with <path>.open() as fh` now **exempt correctly** instead of sitting in
`undetermined`.

## A third value, kept distinct on purpose

New verdict `neither-pin`. `free-neutron-decay.witness.json` carries
`q0 = 1.1099785955541805` — agrees with the muon pin to **11** digits, then
diverges. That is the third stored muon value the corpus already tracks
(`muon_pin_three_values_probe`, `muon-pin-stored-vs-live.witness.json`). A
looser prefix would call it `muon` and erase the exact discrepancy those audits
exist to hold, so it is reported as neither — not as "no q0 found", which means
the opposite thing to a reader.

## Residue

7 `undetermined`, all `manifest=ABSENT`. That is the honest remainder and it is
the half worth working: an absent producer inherits a pin with **nothing**
asserting what it should be — a weaker guarantee than the mislabel that was
fixed here, not a stronger one.


---

## The oracle was wrong too: the MANIFEST is not the STAMP

Comparing an inherited pin against `q0_anchor_manifest.json` answers *"what was
this producer supposed to be pinned at"*. What misleads a reader is the other
question — *"what does its witness claim"*. Measured, they come apart three
ways:

- **ABSENT resolves to `proton` at runtime**, not to "unknown"
  (`witness.py:291`, *"matching the runtime default"*). The corpus already
  names the distinction: `q0_anchor_is_declared` exists because *"absence is
  the runtime default, not evidence"*.
- **...but only for producers that stamp at all.** `mu3_target_frame_robustness`
  is ABSENT *and* emits no `q0Anchor`, so the manifest default never applies.
  **Reading ABSENT as "declared proton" would have made it a MISLABEL — it is
  not one.** That was my next intended change; measuring it before writing it
  is the only reason it is not in the tree. Fourth near-miss of the same kind.
- **`independent` / `comparison`** are declared by the producer at `save()` and
  can never come from a manifest lookup.

Oracle is now the committed witness, indexed by its own `scriptFile` field —
exact, rather than guessing the filename from the stem (`strip_float64_padding`
emits `q0-value-drift-audit.witness.json`). A witness with no `scriptFile`
falls back to the stem convention, because `no-witness` is the wrong thing to
say about a producer whose witness is sitting right there.

## The residue, resolved into classes that need different work

| verdict | n | meaning |
|---|---|---|
| `unstamped` | 5 | inherit a pin **and** emit no anchor — invisible to every anchor audit |
| `undetermined` | 1 | upstream unresolved |
| `no-witness` | 1 | `_li_2_q_util`, a library module — correct |
| `agrees` | 3 | unchanged |
| `MISLABEL` | 0 | after the rebase onto main (+147) |

The `unstamped` five are **`qou-veu1`'s mechanism and this bean's,
intersecting** — measured on one population for the first time. One of them,
`mu3_target_frame_robustness`, inherits a **muon** pin: the layer-straddle
AGENTS.md documents at 11.54 ppb, reached here from a third angle.

## PR hygiene, and one coupling a reviewer should know

Rebased onto main: the PR showed **57 commits / 34 files / +3399** because
rebase-merge rewrote #5519's SHAs, so already-merged content read as new. Now
**4 commits / 4 files / +487** — the same content, actually reviewable.

Adding a witness-**reading** script moves `witness-provenance-audit`:
`prov_exempt_no_reader` 224 → 223, `prov_missing` 75 → 76. Real and
attributable to this bean. Not committed: the same gates run also moved
`q0-value-drift-audit` by a delta I could not attribute (+2 proton / −1
canonical, net +1 witness) and rewrote `pyhecke_native_build` to this
container's hash. Per AGENTS.md — check whether the movement is yours or
main's *before* claiming it — those three derived audits were reverted rather
than committed on a guess.


---

## 🛑 Correction to my own "what is left": the 5 unstamped are NOT a notable class

Last turn I called the five `unstamped` rows "the highest-value remainder,
precisely because no audit can currently reach them." **Measured, that does not
hold.** Two facts I should have checked before asserting it:

1. **Unstamped is the corpus NORM, not an anomaly.** The committed
   `q0-anchor-consistency-audit` reports `Q0_ANCHOR_MISSING = 1839` of **2589**
   audited witnesses — **71 %** — against `Q0_OK = 750` and `Q0_FLIP = 0`. And
   AGENTS.md states plainly that `Q0_ANCHOR_MISSING` "is not a failure."
   Five witnesses in the majority state is not a finding.

2. **The conjunction shows NO enrichment.** Of the 9 inheritors that have a
   witness, 5 are unstamped — **56 %**, against the 71 % baseline. Expected
   under independence: 6.4. **Enrichment factor 0.78×.** If anything they are
   marginally *less* likely to be unstamped, and at n=9 the honest reading is
   "indistinguishable from the base rate". The conjunction of inheritance and
   unstamped-ness is not evidence of a special class.

Scope, per the refuted/ruled-out discipline: this is **scope (a)** — *these
five, as a group, are not distinguishable from the corpus baseline*. It is
**not** the structural claim that an unstamped inherited pin can never matter.
No invariant forbids it; the population is simply too small and too ordinary to
carry the weight I put on it.

## What the regeneration test did establish

Re-running two of the five does **not** add a stamp (`stamp=None` after), so
they are structurally unstamped rather than stale — and the fresh witnesses
carry **no q0-classed value at all** (`body=[]`). So the inherited pin reaches
the arithmetic and is recorded **nowhere** in the artifact: not as a stamp, not
as a constant. That is a real property, and it is genuinely worse than a wrong
stamp — a wrong stamp is at least falsifiable. It is also, on the numbers
above, the ordinary condition of most of this corpus, so it is a **corpus-wide
observation, not a defect these five have.**

Sub-mechanisms differ, and only one is a bypass: `mu3_target_frame_robustness`
writes raw `json.dump` (never stamped); the other four **use `WitnessBuilder`
and are still unstamped**, which was the opposite of my hypothesis.

## Standing conclusion for this bean

The defensible result is the one already landed: **one live MISLABEL, found,
fixed, and its detector hardened through three wrong upstreams and one wrong
oracle.** The residue is ordinary. I am not building further on it.
