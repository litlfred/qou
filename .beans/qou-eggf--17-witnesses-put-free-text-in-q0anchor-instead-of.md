---
# qou-eggf
title: 17 witnesses put free text in q0Anchor instead of the token; the vocabulary cannot parse it
status: todo
type: task
priority: normal
created_at: 2026-09-03T04:57:50Z
updated_at: 2026-09-03T04:57:51Z
---

## The finding

`q0_anchor_consistency_audit.py` on `main` (`8ddfeaf1b7`) reports **18
`Q0_FLIP`s**. Only **one** is a genuine anchor-vs-value mismatch
(`hadron-knot-table.witness.json`, retired value A — that is `qou-tekx` stage 2).
The other **17** are a different defect entirely, and nothing tracked them.

They put **free text in `q0Anchor`**, where the taxonomy expects one of five
tokens. Three distinct strings:

| count | string found in `q0Anchor` | should be |
|---:|---|---|
| 15 | `'proton (experimental pin)'` | `proton` |
| 1 | `'muon (convention-free geometric pin) @ CODATA 2022'` | `muon` |
| 1 | `'both: proton q_at() + muon q_muon_at() @ CODATA 2022'` | `comparison` |

**The values are correct; only the label is malformed.** Verified on three of
them — each carries a real, right `q0Value`, and each has `q0AnchorReason`
**absent**. The producers packed the rationale into the token field instead of
using the field that exists for exactly that. This is the **inverse** of
`qou-mw1p` (completed), which established `q0AnchorReason` as the home for that
free text: mw1p fixed "token with no reason", this is "reason inside the token".

## Two of the three are mechanical; the third is not

- 15 + 1 → set `q0Anchor` to the bare token, move the gloss to
  `q0AnchorReason`.
- The `'both: …'` one is semantically a **comparison**, and the taxonomy is
  explicit that a comparison carries `q0Values` (a mapping, one entry per pin
  read) and **no bare `q0Value`**. It currently carries a bare `q0Value`
  (`1.10997859564273904668179512938`), which under the correct token is itself a
  `Q0_FLIP`. So fixing the label alone would move it from one flip class to
  another; its producer must emit `q0Values`.

## Scope and ownership

All 17 are `qbeta-*` witnesses from the `qou-cds1` / `qou-pdix` arc — the same
in-flight work that owns the 10 residual convention-C bindings in `qou-t9r1`.
**Fix at the producer, never by hand-editing a witness** (AGENTS.md). That means
touching 17 live producers belonging to another session, which is why this is a
bean and not a PR.

Witnesses (17):

```
qbeta-blind-sector-is-the-tl-kernel          qbeta-holonomy-spectrum-sign-obstruction
qbeta-bond-decay-rates-from-transfer-spectrum qbeta-imq-elliptic-generator-refutation
qbeta-bring-elliptic-generator                qbeta-level-k-binding-operator
qbeta-bring-tau0-and-jet-tower-closure        qbeta-level-k-operator-and-real-decays
qbeta-c3-muon-anchor-codata-edition-attribution  <- the 'both:' one
qbeta-cosine-parametrisation-justification    qbeta-nucleon-difference-ellipticity-structural
qbeta-d-frame-z-determinations-experimental-budget  <- the 'muon (...)' one
qbeta-decay-functional-unification-protium    qbeta-tanh-em-match-is-formal
qbeta-decay-operator-elliptic-spectrum
qbeta-discriminant-curve-in-q
qbeta-eigenphase-tower-and-fraction-readings
```

## Why it matters beyond tidiness

`Q0_FLIP` is the flip-flop detector. With 17 of its 18 hits being label-shape
noise from one producer family, the **one real flip is 6 % of the signal** — a
reader triaging the gate sees 18 reds and has to read every one to find the
single anchor-vs-value mismatch. Draining these makes the gate mean what its
name says.

## Measurement note

I first reported this as "16". It is **17** (15 + 1 + 1), against 18 total
flips. Re-count from the audit output rather than trusting either figure.
