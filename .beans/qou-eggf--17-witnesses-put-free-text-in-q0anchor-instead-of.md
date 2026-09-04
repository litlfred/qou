---
# qou-eggf
title: 17 witnesses put free text in q0Anchor instead of the token; the vocabulary cannot parse it
status: in-progress
type: task
priority: normal
created_at: 2026-09-03T04:57:50Z
updated_at: 2026-09-04T12:47:20Z
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



---

## Worked 2026-09-04 (PR #6654) — and the bean's own 17 were already fixed

**The 17 named above are ALL clean on `main`**, every one carrying a bare token
(`proton` x15, `ambiguous` x1, `muon` x1). Checked individually, not sampled.

Note one deviation from this bean's own prescription: the `'both: ...'` witness
(`qbeta-c3-muon-anchor-codata-edition-attribution`) became **`ambiguous`**, not
the `comparison` + `q0Values` this bean recommended. Not adjudicated here;
recording it so the next reader does not assume the recommendation was followed.

## The live 13 are a DISJOINT set — this drained and refilled in one day

    Q0_FLIP                  1   (hadron-knot-table, retired value A, qou-tekx stage 2)
    Q0_ANCHOR_UNRECOGNISED  13

Not one of the 13 appears in the 17 above. **Every one was first committed
2026-09-01 to 2026-09-04** — during and after the drain.

**Because the producers were never touched.** 12 still carried
`q0_anchor="proton (experimental pin)"` at the stamp site, so each re-run
re-emitted it. This is `qou-q0rf`'s revolving-door thesis reproduced on a second
gate, with the mechanism visible rather than inferred: outputs were cleaned while
the source kept writing.

## Fixed at the producer (PR #6654)

* **12 uniform sites** -> token + `q0_anchor_reason`. Verified AT THE VALUE, not
  transcribed from the label (sibling commits `4f68183902`, `ec597e2e49`,
  `f4d031de71` all found labels disagreeing with their own numbers): all 12
  carry the canonical proton 50-digit `1.1099785827513808...`, 10 as a literal
  and 2 via `CONST.Q_50_DIGIT_STR`.
* **`qbeta_kd_monodromy_reading_closed`** wrote `'none (exact symbolic
  identities in q)'` -> **`independent`**, verified two ways (the anchor line is
  the only q0-ish token in the file; import cone is stdlib + sympy only). Its
  `q0_value="n/a"` is **dropped**, per the audit's own rule that a single value
  "asserts the one pin the label denies".
* **`markov_bond_rule_forces_pairwise`** passed `q0_anchor=True` -- **my own**,
  from this session's P30 port. A 4th defect class this bean's table does not
  have: only `False` is special-cased (`is False`), so `True` was stamped
  verbatim.
* **`aoperator_a5_crosscheck`** defaulted to the literal `"unrecognised"`, which
  is the audit's VERDICT NAME and not a token it accepts -- a latent 5th source
  that has never fired. Now `ambiguous` with a conditional reason.

## The arrival rate now has a check

`stamp_staleness_metadata` warns to stderr on an anchor outside the five tokens.
**Warn, not raise, deliberately**: stamping happens at the END of a producer and
several here run past 40 minutes, so raising would discard a whole compute to
correct a label -- and the repo settled this same question in this direction when
the owner declined a blocking `precommit-precision-warn.sh` on 2026-08-25. It
changes no value, so `test_only_False_suppresses_not_any_falsy_value` passes
unmodified. 34/34 tests green (run by direct import; pytest is not installed here
and PyPI read-timed out).

## Measurement note worth keeping

The "no number moved" check was WRONG on its first pass: 11 of 12 read MOVED,
and the sole difference in each was `gitCommit` -- a provenance field this family
writes under a name the mask did not have (`commitSha` was masked). Recording
WHICH field differed turned a false alarm into a one-line mask fix instead of a
second full sweep. With it masked: 12/12 byte-identical.

## Still open

* 2 producers exceed 240 s (`qbeta_derived_w_overdetermined_test`,
  `qbeta_interface_w_deciding_test`); re-running on a long budget.
* Whether the guard should BLOCK rather than warn is a real question and is
  deliberately not decided here.
* The 12 producers hardcode the proton 50-digit literal rather than calling
  `q_at()`, so they will not track a re-pin. Out of scope for this bean
  (`qou-0hnz` territory), recorded so it is not lost.
