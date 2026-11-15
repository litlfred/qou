---
# qou-vgat
title: 'The vacuity audit could not see the carriers most likely to be defective — gate + 3 compounding defects'
status: completed
type: task
priority: high
created_at: 2026-08-29T18:40:00Z
updated_at: 2026-08-29T18:40:00Z
---

Found triaging `qou-hprp` (the 23 `holds : Prop` carriers). The question was why
none of them appears in `docs/audits/lean-vacuity-review-ledger.json`. The answer
is that **the audit cannot see them.**

## The gate

`content/pipeline/lean-vacuity-axiom-audit.ts::isConjectureCarrier` admitted a
declaration only if its docstring contained a `conj:` reference or the word
"axiomatis". A carrier whose docstring is a bare

```lean
/-- **CONJECTURE.** Quantum Langlands duality — $H_n(q)$ ↔ $H_n(q^{-1})$ … -/
class QuantumLanglandsDual where
  holds : Prop
```

fails both tests. The gate runs **before every criterion in the family**, so
those carriers were invisible to `proof-claims-unencoded`,
`proof-no-empty-prop-carrier` and `proof-dependent-conjecture-not-conditional`
alike. Verified on five: `QuantumLanglandsDual`, `Mirror3d3dCorrespondence`,
`LusztigCanonicalBasisQEq1`, `SpinFromSo3Fiber`, `PoincareLefschetzBorromean` —
every one absent from the conjecture graph, every one `ledger:0`.

Widening the gate to accept a docstring that *announces* itself a conjecture:
**carriers 243 → 309.** Sixty-five carriers had never been examined.

## `proof-dependent-conjecture-not-conditional` was structurally dead

Severity **critical**, and it returned **0 hits across 244 carriers and 3264
files**. Three compounding defects, each of which alone was sufficient:

1. **Wrong source.** It scanned `c.doc`, the Lean docstring. A content block
   declares conditionality in its **`.md` sibling** — e.g.
   `lusztig-canonical-basis-q-eq-1.md` says *"conditional on
   [`conj:kazhdan-lusztig-classical-limit`]"* while the Lean docstring says
   nothing of the kind.
2. **Unpopulated label map.** `labelToName` was built from `ownConjLabels`,
   which keys on `\label{conj:…}` — present in **15** `.lean` files against
   **113** using the markdown-link form. So even a matched claim usually
   resolved to nothing and was dropped silently.
3. **The regex could not match the corpus's own spelling.** `[[`]?` allows
   *one* bracket-or-backtick; the canonical cross-reference is ``[`conj:X`]``
   — bracket **and** backtick. One `?` too few.

Fixed all three (`.md` sibling scanned; own label also read from the
authoritative `.ts` `label:` field; character class widened). **0 → 3 hits** (see the correction below —
my first pass said 5 and three of those were an artifact of my own change), and
the full-audit delta is exactly those 3 (134 → 137 defects), with no other
category moving — the fix is surgical, not a flood.

## CORRECTION — my first pass reported 5, and 3 were my own bug

I first reported five hits and wrote that *"three are conditional on
`QuantumLanglandsDual` — the carrier whose only field is `holds : Prop` — so they
declare themselves conditional on a conjecture that asserts nothing."*

**Retracted. That was an artifact of the fix, not a finding.**

A Lean docstring belongs to one declaration; a `.md` is the narrative of the
whole **content block**, and a block may define several carriers.
`phi-q-aj-machinery-identification.lean` defines **three** classes sharing one
`.md`, whose line 1 says *"conditional on [`conj:quantum-langlands-dual`]"*. By
charging the file-level narrative to every carrier in the file, I turned one
sentence into three hits.

Worse, the three classes I called out are **good** carriers, not defective ones.
`QuantumAPolynomial` carries `ahat`, `homogeneous`, `jones`, `annihilates`,
`nontrivial`; `PhiQRegulator` and `Li2QRegulator` each carry a real
`saddle_annihilated` field and bind `[QuantumAPolynomial …]` — and the file's own
section heading reads *"Conditional theorems (derived, not projected)"* with an
explicit §3b-cond item-5 note. I cited three well-formed carriers as evidence of
rot because my detector counted one prose line three times.

Fixed: `.md`-sourced claims are now scoped **once per file** and marked
`prose-conditional-block-level`, distinct from the per-declaration
`prose-conditional-not-in-type`.

## The three, and what they are NOT

```
RootOfUnityTruncationContext  block .md: conditional on QAubinLions          — no binder
MagicABindingFormula          block .md: conditional on MagicNumbersBring    — no binder
QuantumAPolynomial            block .md: conditional on QuantumLanglandsDual — no binder
```

All three are `prose-conditional-block-level`; **zero** are doc-sourced, i.e. no
Lean docstring in the corpus makes an unmet conditionality claim. These are
**candidates for adjudication, not established defects** — a block whose
narrative motivates itself by reference to a conjecture its theorems do not
depend on may be perfectly honest framing. The criterion's job is to surface the
mismatch; an agent decides. That is the design, and after the correction above it
is worth restating rather than assuming.

## STILL OPEN — `field : Prop` has no criterion at all

The gate was one blind spot; the missing criterion is another, and it is **not
fixed here**. Read the two existing shapes:

- `proof-no-empty-prop-carrier` fires on a carrier with **zero** fields.
- `proof-claims-unencoded` / `true-class-field` fires on a field typed
  **literally `: True`**.

`holds : Prop` is neither. It is a field whose *type* is `Prop` — a proposition
carried as **data**, so `⟨True⟩` inhabits the class exactly as it would an empty
one. My standalone
[`scripts/lean-overclaim-audit.py`](../scripts/lean-overclaim-audit.py) reports
**39** such declarations under `contentless-carrier`; the official audit reports
them under **no category**, which is why `proof-claims-unencoded` did not move
when the gate widened.

Adding that category is a bigger change than the two made here — a new severity
row, a CI-gate decision, and 39 candidates entering the agent-inspection ledger
at once. It is an owner call, not a repair. Tracked with `qou-hprp`, which
carries the reason the 39 must not be swept mechanically.
