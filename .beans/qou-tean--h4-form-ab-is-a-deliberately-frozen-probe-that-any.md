---
# qou-tean
title: h4-form-AB is a deliberately frozen probe that any run silently overwrites
status: todo
type: bug
priority: normal
created_at: 2026-08-23T23:11:17Z
updated_at: 2026-08-24T12:45:00Z
---

## The question this started as, and why it dissolved

`h4-form-AB-cross-anchor-stability.witness.json` is one of the `qou-bdkx`
contradictions: it declares `q0Anchor: proton` while
`parameters.q_proton = 1.109978595557…` — the **muon** basin. I flagged it
repeatedly as needing an owner ruling on whether a proton-named field holding a
muon value was a naming defect.

**It is not a naming defect.** The producer reads `q_at(DPS)` at line 98 and
writes what that returns. Run today it writes the correct proton pin:

```
committed  parameters.q_proton = 1.1099785955573347198997632204832250266562…
FRESH      parameters.q_proton = 1.1099785827513808075916690956107688798744…
```

The committed witness is **stale**, predating the 2026-05-28 proton re-pin. No
ruling needed — and I withdraw the three requests for one.

## But do NOT regenerate it — the file says so

The header, dated 2026-06-22, ends: *"This probe is **preserved as-is by
design**."*

So the stale values are deliberate. Regenerating destroys a frozen result. I ran
it, saw what it produces, and **reverted** rather than commit.

## What regenerating would have destroyed

The probe's headline conclusion, not just its pin:

| | committed (frozen) | fresh |
|---|---|---|
| `Form_A_ppb_proton` | 4753.80226522 | **207.114326709** |
| `Form_B_ppb_proton` | 4753.80454962 | **207.116611119** |
| `Form_A_ppb_muon` | 4752.63138326 | 4992.62545608 |
| `data.q_muon` | 1.109978595554180575281594 | 1.109978595642739046681795 |

`evaluate_form` confirms `Form_A_ppb_proton` is exactly what the docstring
means — the ppb residual of Form A at `q_proton` — so this is like-for-like.

**Neither value matches the docstring's own claim** of *"Form A → 0.003 ppb at
q_proton; Form B → 0.0008 ppb"*: 4754 and 207 are both ~5 orders of magnitude
away. The residual also depends on `alpha_em`, `m_e`, `m_mu`, `m_p` from the
CODATA registry, which have moved too, so I am **not** claiming the docstring
was ever wrong — the likeliest reading is that 0.003 ppb was true at the inputs
of its day and every input has since drifted. What is certain is that **the
documented sub-ppb closure is not reproducible today**, and nothing in the file
says so.

## The actual defect: "preserved" is an intention, not a mechanism

Nothing enforces the freeze. Any agent running this producer — a sweep, an
audit, a `--candidates` pass — silently overwrites the preserved numbers, and
`git add -A` commits them. **I nearly did exactly that**, and in the same
session I did do it to a different witness (`qou-wee5` work, reverted in
`a93d01c250`).

A frozen artifact whose only protection is a sentence in a docstring will be
destroyed by the next tool that walks the tree.

## And the header is itself inverted

```
canonical proton q0 is q_at() ≈ 1.1099785955573347…
```

Measured today: `q_at()` = `1.10997858275138…`, `q_muon_at()` =
`1.10997859564274…`. The value the header attributes to the **proton** accessor
is the **frozen muon literal**. Same inversion class as `qou-q0inv`, in a
file-level comment rather than an audit.

## Next

1. **Give the freeze a mechanism.** Options: a `"preserved": true` /
   `"frozen_at"` field the regeneration harnesses honour; a `--force` guard in
   the producer; or move the frozen numbers into an audit doc and let the
   witness be live. Any of the three beats a docstring sentence.
2. **Fix the header's inversion** — one line, and it is actively misleading
   about which accessor returns what.
3. **Decide what `q0Anchor` should say** for a deliberately frozen witness.
   `proton` is currently false-in-fact; the honest options are re-stamping to
   what it actually holds, or an explicit `preserved` anchor value that the
   triage can skip. Until then it will keep appearing in the `qou-bdkx`
   contradiction list, which is where it correctly surfaced.


## RESOLVED — all three mechanisms landed (PR #5638, 2026-08-24)

Owner chose all three. They are not redundant; each survives a different failure.

1. **Audit doc** `docs/audits/2026-08-24-h4-form-ab-frozen-record.md` — numbers
   in prose, in a directory no harness writes to. Also records what nothing in
   the file said: the documented 0.003/0.0008 ppb closure is NOT reproducible
   (committed 4753.80, fresh 207.11).
2. **`"preserved": true` enforced in `WitnessBuilder.save()`** — at the single
   point every producer's output passes through, so it protects any witness that
   opts in. A blocked run RAISES. Escape: QOU_ALLOW_OVERWRITE_PRESERVED=1, and an
   overwrite must re-declare the freeze.
3. **`--force` on the producer** — the discoverable local half.

Verified: blocked run raises; --force overwrites AND re-declares; unrelated
producer unaffected (exit 0); witness diff is exactly ONE line.

**Left unfixed deliberately:** the header inversion (attributes the frozen MUON
literal to `q_at()`). Offered as a fourth item, not selected — recorded in the
audit doc rather than silently changed.
