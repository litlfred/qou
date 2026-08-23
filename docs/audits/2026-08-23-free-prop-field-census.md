# Free `: Prop` fields — corpus census, and a failed triage

**Branch** `claude/bring-surface-categorical-trace-wtrwtb` · **PR** #5562 ·
beans `qou-lo1t` (vacuity drain), `qou-tsnp` (the census this widens).

Two results, one positive and one negative. The negative came first and is the
reason the positive exists.

---

## 1. Negative: the `genuine` vacuity queue cannot be triaged mechanically

Bean `qou-lo1t` batch 2 recorded a hypothesis worth testing: that a meaningful
fraction of the `proof-no-self-assuming-projection` queue is a false-positive
class — a **definition's field accessor** (`kernelIncl_exact := cj.exact`,
Mathlib's `mul_assoc := Group.mul_assoc` idiom) rather than a **claim carrier's
projection**. The two are *syntactically identical*; only the semantics differ.

Three candidate discriminators were implemented
([`scripts/vacuity-carrier-shape-triage.py`](../../scripts/vacuity-carrier-shape-triage.py))
and validated against the ledger's **8 hand-adjudicated `legit`** entries —
ground truth for the false-positive class — versus its 97 `genuine`:

| signal | legit (n=8) | genuine (n=97) | separates? |
|---|---|---|---|
| carrier holds data fields | 4 / 4 | 65 / 30 | **no** — legit splits evenly |
| carrier is inhabited | 3 (38 %) | 29 (30 %) | **no** |
| referenced in ≥ 3 other files | 3 (38 %) | 2 (2 %) | one-way only |

The first bucket reported **67 % DEFINES-OBJECT**, which looks like
confirmation. It is not: half the *known* legit entries land in the opposite
bucket, so the split has no adjudicative content. The cause is that
setup/parameter data (`Z : ℕ`, `q : ℝ` in a `…Context`) is indistinguishable
from definitional data (`jetObj`, `jetEval` in a `CategoricalJet`).

The third signal is real but cannot drain: 73 of 97 `genuine` **and** 3 of 8
`legit` sit at zero external sites.

**So the (a)/(b) call stays an agent judgement, and the `genuine` count is a
review queue rather than a defect count.** This is the third heuristic tried on
this queue — an earlier pass split it by binder style (instance-binder vs
explicit-arg), read all 30 of the smaller bucket, and found the same nothing.

---

## 2. Positive: the free-`Prop`-field class is ~9× the recorded census

Chasing the negative surfaced `HabiroFlowSolution`, whose three fields are
typed `: Prop` — free propositional **variables**, not claims.

**This defect is known.** Bean `qou-tsnp` is its corpus-wide census, at
**12** carriers; it was named for single instances earlier still, in
[`2026-06-07-klr-gs-order-formalization-plan.md`](2026-06-07-klr-gs-order-formalization-plan.md)
and [`2026-06-24-devils-advocate-wave10.md`](2026-06-24-devils-advocate-wave10.md).
What is new here is the **scope** and a re-runnable detector.

`qou-tsnp` scopes to *conjecture sibling carriers with a field literally named
`holds`*. Measured with
[`scripts/free-prop-field-audit.py`](../../scripts/free-prop-field-audit.py):

```
free `: Prop` fields: 166 in 113 carrier(s), 101 file(s)

  UNPINNED-EMPTY      109  (66%)
  UNPINNED-FAKE-IF     39  (23%)
  PINNED               18  (11%)
```

> **113 is not a fourth correction of `qou-tsnp`'s 12.** That bean's count went
> 18 → 16 → 12, each downward and each because the earlier figure was **wrong**,
> so a bigger number here reads like a fourth bad count. It is not: the two
> measure **different sets**. Of the 113, only **21** have a field named
> `holds`, and **11** are on that bean's list — the twelfth,
> `TFromTraceCyclicity`, has since been repaired and now carries a real
> quantified statement, so its live count is 11, not 12. The other **102**
> carriers are outside its scope by construction: **67 in library files**
> (`lean/QOU/**`), 30 chapter siblings, 5 glossary.

The library concentration is the part the narrower scope could not see. Three
examples, all in `lean/QOU/**` and none a conjecture stub:

| carrier | free fields | what the docstring says it encodes |
|---|---|---|
| `IwahoriHeckeAlgebra` | `hecke_relation`, `braid_relation`, `far_commute` | the Hecke presentation itself (§7a) |
| `MarkovTraceRecursion` | `markov_axiom_holds` | the Markov axiom |
| `ClassicalLimitFunctor` | `is_exact` | exactness — the docstring **admits** it: *"Stated abstractly as a Prop field; the full proof requires checking preservation of finite limits and colimits"* |

### The three buckets

A free `P : Prop` is **not** automatically a defect. It is harmless when another
field *pins* it (`regular_iff : regular ↔ 0 < x` — now `True` is refutable). It
is **not** pinned by a field that merely asserts it (`hP : P`) or uses it as an
antecedent (`impl : P → X`); both survive `P := True`. The antecedent case is
its own weaker defect — the *conditionality* is fake while the consequents may
still carry content — hence `UNPINNED-FAKE-IF` as a separate bucket.

### Verified, not asserted

The triviality claim is compiled, not argued
([`2026-08-23-free-prop-field-triviality-probe.lean`](2026-08-23-free-prop-field-triviality-probe.lean),
`lean` exit 0, 0 errors). Carriers reproduced verbatim from their sources:

```lean
instance : DimMasterPentagon := ⟨True⟩
instance : BringSurfaceSmoothness := ⟨True, True, True⟩
instance : HabiroFlowSolution := ⟨True, True, True, ⟨trivial, trivial, trivial⟩⟩

theorem conditional_on_habiro [HabiroFlowSolution] (P : Prop) (hP : P) : P := hP
example (P : Prop) (hP : P) : P := conditional_on_habiro P hP
```

`DimMasterPentagon`'s *entire* body is `holds : Prop`.

### Two bugs this script shipped with, both caught before the number was quoted

Recorded because each moved the answer, and both are now in `--self-test`:

1. **Fields whose type starts on the next line were dropped.** `impl_… :\n  P → X`
   matched no field regex, so the very field that makes `P` a *fake conditional*
   was invisible — inflating `UNPINNED-EMPTY`. Fixing it moved FAKE-IF 16 → 39.
2. **An `=` anywhere in a field's type was read as a pin.** In
   `impl : P → n_linking_ops = 2 ∧ …` the `=` belongs to the **consequent** and
   pins nothing; the pin test now requires the free field to be an *operand* of
   the `↔`/`=`. Fixing it moved PINNED 37 → 18.

Six `UNPINNED-EMPTY` carriers were then read by hand: **6/6 confirmed**.

## Scope

This is a claim about **Lean encodings**, not about the mathematics. That
`IwahoriHeckeAlgebra`'s Lean does not encode the Hecke relation says nothing
about whether the Hecke relation holds — §7a states it and the compute uses it.
The defect is that a downstream `[IwahoriHeckeAlgebra] → P` reads as conditional
while being unconditional.

Not drained here, and not claimed: whether each of the 109 should be repaired,
demoted, or is a legitimate abstraction point is a per-carrier agent call. The
census is the queue, not the verdict — which is the same discipline result 1
arrived at from the other direction.
