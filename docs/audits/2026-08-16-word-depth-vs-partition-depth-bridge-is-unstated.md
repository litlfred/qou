# The curvature-rank chain rests on a bridge that is stated nowhere

> **▶ SUPERSEDED IN PART (2026-08-26, bean `qou-wjbd`).** "Unstated" is now an
> understatement. Every candidate reading of `J^•` present in the corpus has
> been excluded, and the degree-`0` argument excludes the identification *as
> written* for any filtration whatsoever:
> [`2026-08-26-no-shift-rescues-the-word-partition-bridge.md`](2026-08-26-no-shift-rescues-the-word-partition-bridge.md).
> The scope-(a) framing below — "unstated, not false" — remains correct about
> the *identification in the abstract*, which is still not refuted: a filtration
> realising the `gbDepth` grading exists trivially. What is refuted is that any
> `J^•` the corpus names is one.



Raised as an open question in [#5183](https://github.com/litlfred/qou/pull/5183)
while fixing a mis-aimed citation: *"whether the word-depth ↔ partition-depth
identification is proved anywhere"* was flagged unestablished. It is not proved,
not conjectured, and **five sites assume it by citation** — four content blocks
and one production compute script.

## The two objects

| | indexed by | where it lives |
|---|---|---|
| **word / curvature-rank depth** | algebra elements `T_w` | `prop:curvature-rank-gb-stratification`: `J^r(q)/J^{r+1}(q) = {T_w : r(T_w) = r}` |
| **partition-cellular GB-depth** | Young diagrams `λ` | `gbDepth λ = max_□ h(□)`, a Lean `def` in `QOU/BraidKnot/TwoFiltrationBridge.lean` |

They are different indexings. Nothing in the corpus relates them.

## The claim being assumed

$$
Z^{(k)}(A) \;=\; \mathrm{span}\{\, e_\lambda \;:\; \mathrm{depth}_{\mathrm{GB}}(\lambda) = k \,\}
$$

— that the centre's grading by *partition* depth is what the *word* filtration
supplies. Every site below cites `prop:curvature-rank-gb-stratification` for it.

| site | what it says |
|---|---|
| [`prf:phi-q-categorical-truncation`](../../content/quantum-observable-universe/mass-theory/phi-q-categorical-truncation-proof.md) Step 3 | writes the `span{e_λ}` formula verbatim, "By curvature-rank stratification" |
| [`prf:quantum-dilogarithm-stratified`](../../content/quantum-observable-universe/mass-theory/quantum-dilogarithm-stratified-proof.md) Step 3(b) | "the GB-depth of λ is max hook", same citation *(corrected in #5183)* |
| [`prf:unified-curvature-rank-mass-formula`](../../content/quantum-observable-universe/mass-theory/unified-curvature-rank-mass-formula-proof.md) | "By curvature-rank stratification, `e_λ` has GB-depth `depth(λ)`, so the centre splits" |
| [`conj:two-filtration-bridge`](../../content/quantum-observable-universe/mass-theory/two-filtration-bridge.md) | takes the partition-cellular filtration as **given**, citing the same proposition |
| [`gb_depth_period_bring_fig8.py`](../../computations/gb_depth_period_bring_fig8.py) | *"the cellular GB-depth on Z(H_n(q)) (max-hook of partition, **per prop:curvature-rank-gb-stratification**)"* |

## What the cited proposition actually contains

Its `.md` is about words. So is its Lean. `curvature_rank_gb_stratification` is a
§3b-conditional `def` over `CurvatureRankGbStratificationContext`, whose fields
are

```lean
rank_T_w     : A → ℕ
quotient_set : ℕ → Set A
```

**No partition type appears anywhere in the class.** There is no `YoungDiagram`,
no `λ`, no hook. The declaration's own docstring says *"the substantive
mathematical content is carried by the context-class axioms, and a full
derivation from substrate primitives remains pending"* — so even the word-side
statement is conditional, honestly labelled.

## Why the existing conjecture does not cover it

`conj:two-filtration-bridge` relates **iterated-integral depth** `dII` to
**partition GB-depth** `gbDepth`. Its Lean class field is

```lean
(μ.transpose ≠ μ → ¬ isChiralPair μ → dII μ ≤ gbDepth μ)
```

That is `dII ↔ gbDepth`, not `word-rank ↔ gbDepth`. And the conjecture
*presupposes* the partition-cellular grading exists — it is listed as one of the
"two distinct filtrations" the bridge connects, cited to the same proposition.
So the conjecture consumes the missing step rather than supplying it.

The compute script says the same thing from the other side, and says it
correctly: the two depths are *"a SEPARATE filtration"* whose *"relationship is
open"*. It then attributes the partition one to the word proposition in the same
sentence.

## Search performed

Per the "before declaring open" checklist, all four paths:

1. **`docs/audits/`** — nothing establishing the bridge.
2. **`content/`** — 12 blocks name both `e_λ` and the word filtration; the four
   above are the ones asserting the identification, all by citation.
3. **`computations/`** — one script, same attribution, and it flags the
   relationship as open.
4. **`docs/coordination/`** — no ledger entry.

Plus an exhaustive Lean pass: **no declaration mentions both `gbDepth` (or any
partition-indexed depth) and a curvature-rank / `J^r` object.** The single
candidate file from a coarse grep (`UnstableAtom/decay_channel.lean`) contains
neither on inspection.

## Scope

**Scope-(a).** This says the bridge is *unstated*, not that it is false — the
identification may well be true and provable. Two independent reasons to expect
it is not trivial:

- The word filtration is by *rewrite depth to normal form*; the partition depth
  is a *hook statistic*. Nothing forces a max-hook to count `R_H`/`R_YB`
  rewrites.
- The compute script's own counterexample-shaped remark: the `(2,2)`
  self-conjugate cell of `H_4(q)` has max-hook **3**, and it is exactly where
  the two filtrations were observed to disagree in the neighbouring
  iterated-integral comparison.

**Not claimed:** that the downstream results are wrong. They are conditional on
a step nobody has stated. That is a different and weaker thing than false, and
the honest fix is to state the step — as a conjecture if it is open, as a
proposition if it can be proved — and let the four blocks cite *it*.

## The cheapest honest repair

Give the identification its own block. Everything downstream then cites a
statement that says what they use, and the `conjectural-propagation` audit can
see the dependency instead of it hiding inside a citation to a proposition about
a different object.

If it is conjectural, the three `prf:` blocks become downstream of a conjecture,
which §3b forces to be handled — either by the §3b-cond class route or by
demoting their parents. That consequence is exactly why the step should be
named rather than left implicit.
