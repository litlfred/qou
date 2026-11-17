---
# qou-cdx1
title: 'MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)'
status: todo
type: epic
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-11-17T23:08:23Z
parent: qou-10v9
---

## The ruling

Owner, 2026-08-15, verbatim, two messages:

> "convention D is convention. excise convention C."

> "similarly, use proton pin and color wighting"

R1 convention **D** canonical, **C** excised. R2 **proton pin** canonical.
R3 **`bring_color_weighted`** canonical.

Full record, measured blast radius, and the tranche plan:
[`docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md`](../docs/audits/2026-08-15-owner-ruling-convention-d-proton-color.md).

## What is actually new here

**R1 is mostly a re-affirmation.** The 2026-08-09 owner ruling already excised C
and three of four registered channels are `status: agreed` on D. R1 closes the
**two surviving carve-outs**:

1. `channels.qbeta-decay`, registered `disputed` earlier today (PR #5111, bean
   `qou-b3nk`) — `definitional: null`, `production: C`. This ruling settles it.
2. `blocked_migrations[0]` — the registry's only `owner_decision_required: true`
   (`tools/pyhecke/gram.py::z` stays C because `G_INV` is singular under D).

R1 removes the *convention* question from (2). It does **not** remove the
singularity.

## Children

| bean | tranche | kind |
|---|---|---|
| `qou-cdh1` | H1 register the ruling | hygiene |
| `qou-cdh2` | H2 close the `pyhecke.gram.z` leak | hygiene (blocked on S2) |
| `qou-cdh3` | H3 regenerate the 14 C witnesses | hygiene (two gates) |
| `qou-cdh4` | H4 convention-label hygiene | hygiene |
| `qou-cds1` | S1 re-derive the Q_β `c_k` ladder under D | **SCIENCE** |
| `qou-cds2` | S2 `pyhecke.gram.z` + Gram singularity | **SCIENCE** |
| `qou-cds3` | S3 muon → proton witness migration | **SCIENCE** |
| `qou-cds4` | S4 p/n convention | **SCIENCE** |
| `qou-cds5` | S5 verify the `r*` D-frame band | **SCIENCE** |

## Sequencing constraint

**Producers read each other's witnesses** (`qou-eea0`'s hardest lesson: a stale
upstream witness propagates into a freshly-migrated downstream producer and the
output looks clean). H3 must not run before S1/S2 settle what the decay and Gram
layers compute.

## Do not re-derive (survives the ruling)

- KC21 parity is **proved** convention-immune, quantified over every reflective
  Markov parameter (`alphaPhase_im_odd_of_reflective_markov`, sorry-free).
- The REFUTED-as-real-q verdict — anchor swing ratio D/C = 1.0052.
- `c₂ = −1` Taylor-exactness (the proof; its object now carries its convention).
- The mass channel: `m_p`/`m_n` unchanged, production was already D.
- The `z_C` full-bar FAILURE (#5111) now reads as **evidence FOR** the ruling.



## Reorganisation 2026-10-04

Now the epic for P1.CONV under PROGRAM: L2 at 1 ppQ (mass and binding accuracy).


## RE-AUDIT 2026-10-10 — read `convention-d-migration-status.md` before any child of this milestone (bean `qou-am5t`)

This milestone has **57 children and every one is `todo`**. That is the signal
the owner reported as "a mess", and it is misleading in a specific way:
intersecting the concrete file paths each child names against today's live
convention-C sets puts **exactly one** of the 57 on a still-actionable file.

| bucket | n | meaning |
|---|---:|---|
| names a still-actionable file | **1** | `qou-pmkh` |
| names no path at all | 15 | claim-level; cannot be triaged mechanically, must be read |
| every named file is clean | 41 | **a reading queue, NOT a close list — see below** |

**The 41 are not closeable on this evidence and were not closed.** The
intersection answers *"do this bean's files still carry a convention-C
binding"*. Most of these beans are about something else, and those claims
survive a clean code surface entirely:

- published accuracy figures left behind by the excision — `qou-zzwm`
- witnesses — `qou-eea0` (titled "all 84"; measured today: **1**)
- detector blind spots — `qou-ng7j`, `qou-okkz`, `qou-4bq3`, `qou-5le1`
- q-integer naming, a different convention question — `qou-gl58`, `qou-qint`, `qou-b8vx`
- laundering / float64 — `qou-b7cf`, `qou-nmza`, `qou-eg4l`

Closing those because no `z_C` binding remains in the files they happen to cite
would be *"shrinking the number without changing the corpus"*, which the
registry's own `blocked_on_rederivation_note` names as the thing it exists to
prevent. Each needs its own verdict with its own evidence.

**Two of the 41 are worth naming because they are measurably satisfied**, and
both can be closed by someone willing to write the one-line evidence:

- **`qou-m7py`** — "Rust gram.rs `TR_M[5]=z^3` bug". **Fixed.**
  `tools/hecke-engine/src/gram.rs:138` records *"This entry was `z³` until
  2026-08-15"*, and `:137` gives the corrected `TR_M[5] = h·z² + z`.
- **`qou-wgta`** — the designated canonical ledger, titled "174 py + 61 lean";
  measured 0 / 0. Corrected on that bean in this pass.

**Milestone-level state**, from the registry: three of the four trace channels
are `agreed` with definitional **and** production convention D (`mass`,
`binding`, `borromean-binding-single-pipeline`). The fourth, `qbeta-decay`, is
definitional D / production **C** and is the whole of what is left — one
producer (`computations/qbeta/qbeta_ck_cache.py:140`) plus the `qou-cds1`
re-derivation, which is **not** blocked on the phase `qou-pdix` (the cosine cap
`1 − u² = 0.99992745` cannot reach `F_required = 1.759`).

So this milestone is **not** blocked on 57 pieces of work. It is blocked on one,
and the other 56 are bookkeeping of varying liveness.


### Correction, same hour — `qou-m7py` is NOT satisfied; retracting one of the two I named

The append above lists two of the 41 as *"measurably satisfied … worth naming"*.
**`qou-m7py` is not one of them and that line is retracted.** I called it on a
single grepped source line (`gram.rs:138`, *"This entry was `z³` until
2026-08-15"*) without reading the bean, and the bean's point is the opposite of
what that line suggests: it exists to say *"do not just fix the Rust bug"*,
because the fix makes the Gram singular and the consumers must move together.

Read properly: both divergences **were** resolved 2026-08-15 — one day after the
bean's last substantive update — and the predicted singularity was handled
(`gram_inverse` removed, `gram_quotient_inverse` added under a new name, 73.3 %
re-derivation measured in the module header). But its Remaining items 3 and 4
(rebuild `pyhecke_native` / drop the `_native_ok()` guard; regenerate the 53
certificates, `[OWNER]`) are **not** verified, and `pyhecke_native` is not
installed in this container so the C/D split it turns on is not observable here.
Full evidence on `qou-m7py`.

`qou-wgta` stands as named — its title is measurably 0/0 against "174 py + 61
lean", and that is a claim about counts I did measure.

This is the hazard the status doc's §6 item 3 warns about, demonstrated on
myself within the hour: the path intersection tests whether a bean's **files**
still carry a convention-C binding, not whether its **claim** is closed. Treat
all 41 as a reading queue.



## 2026-11-17 sibling sweep
Remaining convention-C surface is tracked by qou-egqr / qou-ng7j; sibling sessions on it archived with nothing extra left.
Recorded 2026-11-17 from the stale-sibling-session sweep (table: /mnt/project-files/qou-sibling-consolidation/table.md). Source session archived; work not lost.
