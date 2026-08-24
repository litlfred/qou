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

### Verified against the real modules — `IwahoriHeckeAlgebra` admits σ ≡ 0

Strengthened 2026-08-23, after the first probe below was noted as one step
removed from its subject. The carriers here are **imported, not restated**, so
no transcription can flatter them
([`2026-08-23-free-prop-real-module-probe.lean`](2026-08-23-free-prop-real-module-probe.lean),
`lean` exit 0, 0 errors):

```lean
instance degenerate : QOU.Mathlib.HeckeAlgebra.IwahoriHeckeAlgebra ℤ 3 (1 : ℤ) where
  carrier := ℤ
  …
  sigma := fun _ => 0          -- every braid generator is 0
  hecke_relation := True ;  hecke_holds := trivial
  braid_relation := True ;  braid_holds := trivial
  far_commute   := True ;  far_commute_holds := trivial
```

**This type-checks.** A structure in which every braid generator is `0` is an
`IwahoriHeckeAlgebra` — the class does not encode the Hecke presentation, it
names three propositions and asserts them.

> **🛑 The `degenerate` instance above was UNNECESSARY, and saying "one could
> build one" understates the finding. The library already ships one, as a
> GLOBAL instance.** `HeckeAlgebra.lean` declares
>
> ```lean
> instance triv_hecke (R : Type u) [CommRing R] (n : ℕ) (q : R) :
>     IwahoriHeckeAlgebra R n q where
>   carrier := PUnit
>   …
>   hecke_relation := True ; braid_relation := True ; far_commute := True
> ```
>
> so **typeclass resolution discharges `[IwahoriHeckeAlgebra R n q]`
> automatically, for every `R`, `n`, `q`**. Verified by synthesis, not by
> reading ([`2026-08-23-trivial-global-instance-probe.lean`](2026-08-23-trivial-global-instance-probe.lean),
> exit 0): `#synth IwahoriHeckeAlgebra ℤ 3 1` answers `triv_hecke ℤ 3 1`, and
> `(inferInstance …).carrier = PUnit` closes by `rfl`.
>
> `WedderburnDecomposition` has the same shape — `#synth` answers
> `triv_wedderburn ℤ 3 1`. Those are **two steps of the canonical derivation
> chain** whose Lean hypotheses are inert.
>
> Its docstring is candid about why it exists — *"Discharges the §3b-cond
> hypothesis at the audit level; genuine instances at `R = ℚ(q)` arrive when
> Mathlib's Iwahori–Hecke library lands"* — which is precisely what §3b-tax
> forbids: *"an unproved primary is honestly represented by a content-bearing
> class with no instance; do not fabricate a trivial instance to 'close' it."*
> The harm is not the placeholder but its **globality**: being an `instance`
> rather than a `def`, it reaches every downstream `[IwahoriHeckeAlgebra …]`
> silently.
>
> **Screened, not verified:** 8 further all-trivial global instances match the
> same shape (`HasGeneratorAction_punit`, `weinbergAngleCanonical`,
> `CrystalGraphRealization.canonical`, `hasBlochGroup_real`, …). Only the two
> above were confirmed by synthesis; some of the rest are likely legitimate
> (e.g. a genuine `Prop` Boolean-algebra instance). A count is not a verdict.
>
> **FIXED 2026-08-23**: both demoted `instance` → `def`. `#synth
> IwahoriHeckeAlgebra ℤ 3 1` now reports *failed to synthesize*; the trivial
> model stays reachable by name (`triv_hecke ℤ 3 1`). See the correction on
> blast radius below.

### Inhabitation is what makes a free `Prop` field harmful — and it re-ranks the queue

Crossing the census against inhabitation changes which carriers matter:

| free-`Prop` carriers | count |
|---|---|
| **no inhabitant at all** | **89** |
| `def`-only inhabitant | 17 |
| **inhabited by a global `instance`** | **7** |

The 89 are the §3b-tax **honest open state** — nothing inhabits them, so a
downstream `[C] → P` can never be *applied*. Weak, but inert. The harm needs an
inhabitant, so the actionable set is the intersection: `IwahoriHeckeAlgebra`,
`CanonicalKnotIdSDP`, `HeckeAnyonicSubstrate` (×2 — two *different* classes
sharing the name, one parameterless in `IwahoriHecke/Tw.lean` and one
`(R) [CommRing R] (q)` in `BraidKnot/`, so also a name collision),
`BorromeanQuark` (whose `instance canonical` is declared **twice**, in a
chapter sibling and in the library — the shadow-pair shape again), plus
`WedderburnDecomposition`.

**So "drain the 77" was the wrong queue**; ~5–7 carriers are.

> A note against my own earlier result: inhabitation **failed** as a signal when
> I tried it as a *legitimacy classifier* on the projection ledger (§1 above).
> Here it is not classifying legitimacy — it is the **harm multiplier**.
> Different question, so this does not overturn that negative.

### Correction: the blast radius was 3 errors, not 1

I reported "demoting both produces **exactly one** error." That was wrong, and
the way it was wrong is worth recording: **Lean halts elaboration of a
declaration at its first error, so each fix exposes the next.** The single
error I measured was only the first of a chain:

1. `triv_wedderburn` lost the instance it was resolving — fixed by taking
   `[self : IwahoriHeckeAlgebra R n q]` as a hypothesis. (A `letI` in the
   *type* does **not** work: it binds for the ascription but not for the
   `where` fields, which elaborate against the class and need it again.)
2. Then `block_proj _ := PUnit.unit` stopped type-checking — it only ever
   worked because the global instance pinned the carrier to `PUnit`. Over an
   arbitrary model the projector must land in `self.carrier`, so it becomes
   `self.one`, which is the honest reading of "trivial projector".

Final state: `lean` exit 0, 0 errors, and nothing outside this file needed
changing — so the *scope* claim ("nothing else in the corpus depended on the
global resolution") held; only the effort estimate was wrong.

**Three of my measurements in this session were truncated-log artifacts** — a
`lean` run killed by a 2-minute command timeout leaves a log with zero errors
in it, which reads as success. Both the "1 error" figure and a later "the
demotion still resolves" non-result came from that. Every Lean check here now
writes a `COMPLETE` sentinel *after* the process exits, and is only read once
that sentinel is present.

The witness genuinely violates the intended relation, not merely an unstated
one: at `q = 1` over `ℤ`, `q − q⁻¹ = 0`, so `σᵢ² = (q − q⁻¹)σᵢ + 1` reads
`σᵢ² = 1`; with `σᵢ = 0` that is `0 = 1`. So this is not a vacuous
"nothing was stated so nothing is violated" — the intended axiom is false of
the inhabitant, and the class admits it anyway.

This is AGENTS.md §7a's central algebraic object: *"The Hecke algebra generator
is `σᵢ` … `(σᵢ − q)(σᵢ + q⁻¹) = 0`"*. **Scope, again**: that relation holds — the
manuscript states it and the compute engine uses it. What is measured here is
only that **this Lean class does not carry it**, so a downstream
`[IwahoriHeckeAlgebra …] → P` reads as conditional while being unconditional
(also compiled, in the same probe).

### Also verified: the reproduction probe

The original triviality claim is likewise compiled, not argued
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

Not drained here, and not claimed: whether each should be repaired, demoted, or
is a legitimate abstraction point is a per-carrier agent call. The census is the
queue, not the verdict — which is the same discipline result 1 arrived at from
the other direction.

**Mind the units when quoting this.** The bucket table counts **fields**; the
drain queue is **carriers**. The 109 `UNPINNED-EMPTY` *fields* sit in **77**
carriers, and the 39 `UNPINNED-FAKE-IF` fields in 32. Quoting 109 as a carrier
count overstates the queue by 40 %.

## Follow-up that needs a decision, not a chore

Wiring this as a criterion in
[`content/pipeline/lean-vacuity-axiom-audit.ts`](../../content/pipeline/lean-vacuity-axiom-audit.ts)
would close the blind spot — **zero** of these carriers currently appear in the
ledger under *any* criterion. It would also seed every one of them as
`needs-agent`, and `--check-ledger` exits 1 unless every non-exempt candidate
carries a fresh verdict. Measured against the live ledger:

| | ledger | gate |
|---|---|---|
| today | 124 | green |
| wire `UNPINNED-EMPTY` only | ~201 (+77) | **red until all 77 are read** |
| wire `EMPTY` + `FAKE-IF` | ~233 (+109) | **red until all 109 are read** |

That turns the gate red for **every branch**, not just the one that wires it —
so it is an owner call on sequencing, not something to land quietly. The
standalone script is the interim: it measures the class without gating anyone.
