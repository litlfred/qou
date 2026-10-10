---
# qou-cdx1
title: 'MILESTONE: excise convention C, adopt proton pin + colour weighting (owner ruling 2026-08-15)'
status: todo
type: epic
priority: high
created_at: 2026-08-15T00:00:00Z
updated_at: 2026-10-04T15:09:59Z
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
