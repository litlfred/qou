---
# qou-z9fx
title: 'GAP: docstring-states-a-VALUE the body does not compute — the schurElement/hookDim class'
status: todo
type: task
priority: high
created_at: 2026-08-26T21:41:57Z
updated_at: 2026-08-26T21:42:37Z
---

Proposed on [#5857](https://github.com/litlfred/qou/pull/5857) by the sibling
draining `lean-borrowed-name-audit.py`, who declined to fold it into their
detector: *"parsing a claimed return value out of prose is a different and
noisier problem, and I think it deserves its own bean rather than a row on
mine."* Agreed — this is that bean.

## The class

A declaration whose **docstring states a specific value or formula** that its
**body does not compute**. Distinct from every detector currently shipped:

- `dsm1` / `proof-docstring-sorry-mismatch` — doc claims a result, body has a
  `sorry`. Here there is **no `sorry`**; the body computes, just not what the
  doc says.
- `zero-placeholder` (`lean-borrowed-name-audit.py`, shipped by #5856) — body
  is identically `0` or discards its argument. Catches `hookDim`; does **not**
  catch `schurElement`, whose body is a full, correct-shaped computation with
  one wrong exponent.
- The vacuity family — nothing is vacuous. `schurElement` typechecks, computes,
  and has consumers that build on it.

## Two worked examples, both real, both from this PR

1. **`WenzlSchurElement.schurElement`** — docstring said `Q^{n(λ)}`, code said
   `Q ^ contentSum lam`. Different quantities (`contentSum = n(λ′) − n(λ)`),
   agreeing only for a single row of length ≤ 1. **The docstring was right and
   the code was wrong**, and the error made the Macdonald hook telescope FALSE
   from n=2 upward. Fixed on #5857; `old_contentSum_prefactor_breaks_telescope`
   proves the old form is not equal to the target.
2. **`hookDim`** in `mass-theory/y-lambda-closed-form-wenzl-bridge.lean` —
   docstring states the hook-length formula, body discards its argument. This
   one IS caught by `zero-placeholder`, which is why it is the easy end of the
   class.

## Why it is worth a detector

The `schurElement` case sat in the corpus long enough to be built on, and
nothing mechanical could see it. It was found only because someone tried to
prove a downstream theorem and it did not hold. A detector that even *narrows*
the candidate set here is catching wrong numbers rather than wrong hygiene.

## Why it is hard, stated up front

Parsing a claimed value out of prose is noisy in both directions. Some honest
shapes to try before anything NLP-flavoured:

- **Docstring contains display math that names the declaration's own symbols.**
  `Q^{n(λ)}` mentions `n(λ)`; the body mentions `contentSum`. Both are
  declarations in scope, and they are different constants — a purely symbolic
  mismatch, no prose understanding needed.
- **Docstring formula is evaluable.** Where the doc's formula can be read as an
  expression over declarations already in the environment, elaborate it and
  compare on small inputs. `decide`-level evidence, not a proof — a candidate.
- **Deliberately narrow beats deliberately complete.** The `defeq_collapse`
  calibration from #5856 applies: fire only where the doc names a constant the
  body does not use, and accept the recall loss.

Coordinate with the sibling before building: `lean-borrowed-name-audit.py` on
`main` is the natural home if the check can be made narrow enough, and the
kernel pass (`scripts/lean/audit-driver.sh`, single-pass since #5856) already
resolves constants by declaration rather than by string, which is what
distinguishes the overloaded `hookDim` / `wenzlSchurElement` names.
