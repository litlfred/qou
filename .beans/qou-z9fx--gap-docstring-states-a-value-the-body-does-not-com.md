---
# qou-z9fx
title: 'GAP: docstring-states-a-VALUE the body does not compute — the schurElement/hookDim class'
status: todo
type: task
priority: high
created_at: 2026-08-26T21:41:57Z
updated_at: 2026-09-12T07:59:24Z
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


## Measured 2026-09-04 — one real defect found; the DETECTOR is a negative

### The real defect, and it has a MECHANISM

`hookDim` in `mass-theory/y-lambda-closed-form-wenzl-bridge.lean:109` —
docstring said **"Concrete model: returns `1`"**, body is **`n.factorial`**.

The git history of that one line settles how:

    7e2abe75ce4  2026-05-09  def hookDim … : ℕ := 1              doc CORRECT
    62c6091353e  2026-05-09  def hookDim … : ℕ := 1  -- noqa: one_def
    a754f12ab36  2026-05-09  def hookDim … : ℕ := n.factorial    doc NOT updated

`a754f12ab36` is *"Genuine sharpening: 9 noqa-exempted placeholders →
content-bearing values via structural fields"*. **A pass whose purpose was to
satisfy the `one_def` vacuity detector invalidated the docstring's declared
placeholder value and left it standing for four months.** That is a
generalisable mechanism, not a one-off: sharpening a placeholder body to
silence a detector makes its "concrete model returns X" note false.

**Scope — no number moves, and saying otherwise would be wrong.** The sole
consumer `wenzlNormalization` is
`Σ_λ (hookDim λ) * wenzlSchurElement λ Q X`, and `wenzlSchurElement` is an
**honestly-declared** placeholder — doc and body both say
`0 * (Q + X + lam.parts.length)`. The product is `0` whatever `hookDim`
returns. This is a documentation defect in a file whose numeric output is
identically zero by declaration; it is NOT the `schurElement` class, which was
a wrong exponent inside a live computation.

Docstring corrected in place, naming the numerator, the discarded `_lam`, the
real implementation in `y-lambda-recipe-from-partition.lean`, and the
invalidating commit.

### The detector: 1 true positive in 8. Reported as a negative.

Built to the bean's own prescription — fire only on an UNCONDITIONAL literal
value claim the body does not compute; no prose understanding. First pass: 124
candidates. Four gates (exclude vendored `.lake/packages`; stop body extraction
at the next docstring; reject conditional claims carrying "if/when/unless/
otherwise"; normalise `·`→`*`) cut it to **8**. All eight read:

  * **1 TRUE** — `hookDim`, above.
  * **7 FALSE**, in three classes:
    - **doc states the formula, body implements it** — `writhe`
      (`ε_1 + ⋯ + ε_k` vs a `foldl` over signs), `Hn`
      (`Σ_i x i * z^{ℓ(i)}` vs `∑ i, x i * z ^ lengthFn i`),
      `massSqQuadrupled` (`4 m²` vs `4*a + 4*b*Y + c*(…)`, which IS 4m²
      expanded). The bean names this as the hard case; it is.
    - **doc states an INTERMEDIATE value, not the return** — NEW, not
      anticipated here. `borromeanColorSum_trivTrace` reads *"Each
      half-Borromean evaluates to `1` … so the sum is `3`"* with body `3`.
      The docstring is **entirely correct** and even shows the arithmetic;
      the matcher grabbed `1` and compared it to the return.
    - **parser leakage** — `QChar` matched a type signature, not a body;
      `proton_topological` / `neutron_topological` leaked into the next
      declaration.

**Recommendation: do not ship this detector.** At 1-in-8 it would be quoted,
and its false positives are *correct documentation* — flagging `writhe` and
`borromeanColorSum_trivTrace` trains a reader to distrust docstrings that are
right. The bean's caution ("noisy in both directions") is now measured rather
than predicted.

### The honest form, for reference

Two declarations in the same file show what a correct placeholder note looks
like, and neither trips any detector because there is nothing to trip:
`wenzlSchurElement` (*"Content-bearing placeholder `0 · (…)`: … evaluating to 0
by `zero_mul`"*, body exactly that) and `nLambda` (*"Content-bearing via `n`
(the partition's size)"*, body `:= n`). The convention works when it is
maintained; `hookDim` is what happens when a later pass edits the body without
it.


---

## 2026-09-12 — a SECOND detector tried and also a NEGATIVE; and the class is live, found by hand 5× today

### The sub-shape this bean did not name

All five instances I hit today are the same class — *docstring states something
the body does not carry* — but a different **cause** from `schurElement` and
`hookDim`. Those were authored wrong, or sharpened out from under their prose.
These were **invalidated by a later fix to the thing they describe**, and the
fix's own commit never re-read the prose above it:

| file | claimed | reality |
|---|---|---|
| `Torsion/skein_generation.lean` | "no hadron restriction … `scratch_skein.lean` is closer" | the restriction is 140 lines **below**, added by the commit that deleted `scratch_skein.lean` |
| `Encounter/MostowRigidity.lean` | field "stores the 15-digit truncation … via `:leanval`" | 12 lines above a field whose own comment says the sync "is gone" |
| `MathlibExt/ManifoldVolumeBridge.lean` | "`= 2.0298…` holds by `rfl`" | **the `rfl` does not hold** — it is a Clausen value |
| `Encounter/FigureEightVolumeBridge.lean` | present tense: "Those differ at the 16th digit" | they no longer differ |
| `Archimedean/HyperbolicVolumeTranscendence.lean` | value "cross-checked against `MostowRigidity` which uses the identical value" | the cross-check that was this literal's **warrant** evaporated |

The mechanism generalises this bean's own: it recorded that *sharpening a body
to silence a detector* staled its docstring. The wider rule is that **any fix to
a body invalidates prose about that body, and nothing re-reads it** — and the
prose is what a reader meets first.

### Detector attempt 2, and it fails for YOUR measured reason

I tried the mechanical signature: *a decimal literal appearing in a file's
COMMENTS but in none of its CODE lines* (≥8 significant digits, skipping lines
that self-mark as struck/superseded).

    files scanned   2796
    candidates       400

**Do not build it.** It cannot separate prose about *this* declaration's value
from prose citing *another* constant for comparison — `FiveTwoOhtsukiBridge`
alone contributes ~16 legitimate intermediate values. That is exactly the wall
this bean already hit at 1-in-8, reached from a different direction. Two
independent attempts, same conclusion: **the general form of this detector does
not exist.**

### What IS high-precision — and it is a registry, not a parser

Grep for a **specifically retired literal**. `2.02988321281930` (the 15-digit
`Vol_4_1` truncation `qou-f8lit` retired) gives **9 sites in 5 files**, every one
adjudicable by eye in seconds: **7 correct records, 2 genuinely stale** (both
fixed today).

That is the shippable shape — not "parse a claimed value out of prose" but
"maintain a list of values the corpus has retired, and grep for them". It needs
no NLP, its precision is set by the curation of the list rather than by a
heuristic, and its false positives are a *readable* class (a quotation
explaining the retirement) rather than *correct documentation*, which is what
made attempt 1 and attempt 2 unshippable.

**The 9→2 is the finding, not the 9.** A docstring quoting a retired value to
explain why it was retired is indistinguishable under grep from one still
asserting it — the "quoted defect inside its own fix" trap this corpus has now
hit in `qou-ffwk`, in `qou-hok7`'s scare quotes, and here.

**Recommendation, marked as judgement:** close the "build a detector" question
NEGATIVE on the strength of two independent attempts, and open the retired-value
registry separately if anyone wants it. I have not built the registry — it is a
new tool, not a drain item, and under the ask-first override it is the owner's
call whether a sixth audit script earns its maintenance.
