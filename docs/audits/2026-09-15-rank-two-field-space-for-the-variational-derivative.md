# A rank-2 field space for the variational derivative

Bean `qou-h0ou`, downstream of `qou-ogj5` ("is the quantum-gravity claim GR or
analogue gravity"). Branch `claude/qg-rank-two-field-space-2026-09-15`.

**Scope.** This is a question about whether the categorical setting supports a
rank-2 variational calculus. It is not about gravity's numbers, and no
gravitational content is introduced anywhere in the work it records — no metric,
no curvature, no stress-energy, no Newton constant, no `8π`, no numerical
constant of any kind.

## 1. The diagnosis, verified

`QOU/MathlibExt/MonoidalCalcVar.lean:67`

```lean
class HasAction (R : Type*) (C : Type u) [Category.{v} C] [MonoidalCategory C]
    [Preadditive C] where
  action : ((𝟙_ C) ⟶ (𝟙_ C)) → R
```

The action's **domain is `End(𝟙_C)`, the scalars**. A variational derivative is
an object on the field space — the thing being varied — so there is no field
space here to vary, and nothing in the type mentions the objects being paired.

Downstream, both Einstein slots are scalars wearing a tensor's name:

| declaration | file:line | type |
|---|---|---|
| `ExternalCurrents.einsteinTensor` | `QOU/MathlibExt/MonoidalCalcVar.lean:89` | `(𝟙_ C) ⟶ (𝟙_ C)` |
| `CategoricalVariationalData.einsteinTensor` | `QOU/QuantumObservableUniverse/GaugeTheory.lean:127` | `(𝟙_ C) ⟶ (𝟙_ C)` |

`G_μν = 8π T_μν` is a rank-2 identity. A scalar cannot state it.

## 2. Blast radius — measured, and it is small

`grep -rn einsteinTensor` over the whole tree excluding `.beans/` and `.git/`:
**9 hits, 3 files, all `.lean`. Zero `.md`, zero `.ts`, zero witnesses.**

* `MonoidalCalcVar.lean` — 4 (`:89` declaration, `:115` class field, `:127`
  docstring, `:134` the instance).
* `GaugeTheory.lean` — 4 (`:127` declaration, `:159` class field, `:178`
  `Fact` binder, `:197` theorem statement). All four are self-references
  inside that one file.
* `Instanton.lean:239` — a **comment**.

Consumers of the `MonoidalCalcVar` declarations (`HasAction`,
`VariationalData`, `ExternalCurrents`, `HasMonoidalEOM`) outside that file:
**none**, except `QOU.lean:139` importing the module. So the scalar-typed
apparatus has no downstream mathematical dependant at all.

**No consumer treats it as rank-2.** Nothing in the corpus indexes it,
contracts it, or traces it.

### 2a. There is no constructed instance of the Einstein equation

* **`HasAction` has zero instances anywhere.** The class is declared and never
  inhabited, so no action functional exists in the corpus in the first place.
* `hasMonoidalEOM_of_def` (`MonoidalCalcVar.lean:130`) is the only
  `HasMonoidalEOM` instance. It discharges all three equations of motion with
  `rfl`, because the variational data is *defined* as
  `⟨ec.einsteinTensor + ec.stressTensor, ec.gaugeCurrent, 0⟩`. This is
  AGENTS.md §"Defined residual ≠ derived decomposition" in Lean form: writing
  `X := A + B` and then proving `X = A + B` is a definition, not a derivation.
* `hasCategoricalEOM_of_facts` (`GaugeTheory.lean:172`) is the only
  `HasCategoricalEOM` instance, and it takes the three identities as `Fact`
  hypotheses — it assumes them.

## 3. What was formalized

New library file, sorry-free:
`content/quantum-observable-universe/lean/QOU/FrobeniusHopfData/PairingVariationalDerivative.lean`,
namespace `QOU.Variational`.

The carrier the corpus already holds is
`QOU.FrobeniusHopfData.FrobeniusPairingData` (`FrobeniusPairingCategorical.lean:51`),
whose `eval : dual ⊗ obj ⟶ 𝟙_ C` is a pairing — the categorical shape of a
rank-2 object.

### §1 — the variational core, generic `{R} [CommRing R]`

| declaration | statement | why it is not a tautology |
|---|---|---|
| `QuadraticAction` | a symmetric `R`-bilinear `form : V →ₗ[R] V →ₗ[R] R` on a field space `V` | — |
| `value e` | `form e e` — a scalar, as an action should be | — |
| `variation` | `(2 : R) • form : V →ₗ[R] V →ₗ[R] R` | the derivative is **rank-2 because the field space is** |
| `value_add` | `value (e + δ) = value e + variation e δ + value δ` | the exact Taylor identity; false for any other coefficient in `variation`; its proof uses `form_symm` |
| `value_smul` | `value (r • e) = r ^ 2 * value e` | degree-2 homogeneity; false for any other exponent |
| `euler` | `variation e e = 2 * value e` | the contraction that recovers the scalar; the content is the coefficient |
| `polarization` | `variation e δ = value (e + δ) - value e - value δ` | the rank-2 object is recoverable from the action **as a function on the whole field space** |

**No limit is needed.** For a quadratic functional the Gateaux derivative is
algebraic, so it is definable over a bare commutative ring. `MonoidalCalcVar`
axiomatises the equations of motion on the ground that a categorical calculus of
variations "does not yet exist in Lean/Mathlib"; **for the quadratic case that
is not so**, and no axiom is required.

### §1a — the separating witness

`value_does_not_determine_variation` exhibits, over `ℤ`, two fields with the
**same action value** and **different derivatives**. This is the precise reason
one scalar cannot stand in for a rank-2 object: `polarization` recovers the
rank-2 object from the action as a *function*, never from its value at a point,
and `ExternalCurrents.einsteinTensor` is a value at a point.

### §2 — the categorical layer

`fieldSpace d := d.dual ⊗ d.obj ⟶ 𝟙_ C`. Under `[Preadditive C] [Linear R C]`
this is an `R`-module, so `QuadraticAction` applies to the pairings directly.
The two shapes side by side, from `#check`:

```
ScalarFieldAction  : … [Linear R C] → Type _                              -- no pairing argument at all
PairingFieldAction : … [Linear R C] → FrobeniusPairingData C → Type _     -- the field space is present
```

`contract d η : fieldSpace d →ₗ[R] (𝟙_ C ⟶ 𝟙_ C)` is `η ≫ ·`, the `R`-linear
trace of a rank-2 field against a co-pairing `η : 𝟙_ C ⟶ dual ⊗ obj`. **Its
codomain is exactly the corpus's `einsteinTensor` slot** — so the corpus keeps
the trace and discards the tensor. `map_add'` / `map_smul'` are the content:
they are what make it a trace rather than an arbitrary function.

### §2a — the structural result (scope (b), invariant cited)

`subsingleton_of_contract_reflects` —

> if equality of contractions implied equality of the rank-2 fields, uniformly
> in the co-pairing, then `Subsingleton (fieldSpace d)`: there would be at most
> **one** pairing.

The invariant is `zero_comp`: the degenerate co-pairing `η = 0` contracts every
rank-2 field to the same scalar, so it separates nothing. Hence in any
`Preadditive` monoidal category whose pairing space has two distinct elements, a
scalar-valued Einstein-shaped equation is **strictly weaker** than the rank-2
identity it is named after. `contract_eq_iff` states the exact residue: scalar
equality is rank-2 equality *modulo* `LinearMap.ker (contract d η)`.

### Verification

`lean -DautoImplicit=false -s 65536` → **exit 0**, no errors, no warnings
(`LEAN_PATH` against the main checkout's restored olean tree; `lake` never
invoked, so the restore is not evicted). The flags matter: a bare `lean` does
not read the lakefile, so `autoImplicit` defaults true.

`#print axioms` on all 12 declarations: `propext`, `Classical.choice`,
`Quot.sound` only — **no `sorryAx`**. Kernel-checked, not grep-checked.

`scripts/lean-self-assuming-audit.py` on the new file: **0 candidates**.

### What is NOT claimed

* No general Euler-Lagrange machinery. §1 covers **quadratic** actions; a
  higher-degree or non-polynomial action needs a genuine limit and is not
  addressed.
* `contract`'s co-pairing `η : 𝟙_ C ⟶ dual ⊗ obj` has the opposite handedness
  to the `coev : 𝟙_ C ⟶ obj ⊗ dual` in `FrobeniusPairingData.Nondegenerate`.
  In a braided or rigid setting the two transport into each other; **that
  transport is not asserted here**, and `η` is taken as a datum.
* Nothing is wired into `MonoidalCalcVar` or `GaugeTheory`. Both are
  **untouched**. Retyping `HasAction.action` to take a field space is a
  separate change and, per AGENTS.md §"ASK THE OWNER BEFORE CHANGING THINGS",
  needs owner sign-off — it is neither a precision fix nor corpus-derived. It
  would be cheap: `HasAction` has zero instances and zero consumers.

## 4. A detector blind spot found while running the required audit

**This is the NEXT cause in an arc the corpus already has a bean for, not a new
discovery.** Bean `qou-24m2` (2026-08-08, fixed 2026-08-22) records that
`scripts/lean-self-assuming-audit.py` could not see a class-field-is-conclusion
projection through an instance-implicit binder, named two causes, and a third
was found while fixing it. That fix works. The residual case is narrower: an
instance binder with **no name at all**.

**Measured, three probes, one variable changed at a time** — identical
mathematics, same class, same conclusion; only the binder spelling and the
projection differ:

| probe | binder | proof term | audit verdict |
|---|---|---|---|
| A | `(ctx : HasClaim X)` — round, named | `ctx.claim` | **1** class-field-is-conclusion |
| C | `[ctx : HasClaim X]` — instance-implicit, **named** | `ctx.claim` | **1** class-field-is-conclusion |
| B | `[HasClaim X]` — **anonymous** | `HasClaim.claim` | **0** candidates |

Probe C is exactly the case `qou-24m2` fixed, and it passes — so that bean's
`BINDER_INST` work is confirmed live, not superseded. Probe B is the gap: with
an anonymous binder there is **no name to enter the binder map**, so rule 2's
`binders.get(bname)` lookup is handed the class name, misses, and `continue`s.
The projection is spelled `ClassName.field` because that is the only way to
write it when the instance has no name.

`GaugeTheory.lean`'s entire equation-of-motion apparatus is spelled that way, so
the audit reports **0 candidates** on it:

* `variational_einstein := HasCategoricalEOM.einstein`
* `variational_yang_mills := HasCategoricalEOM.yang_mills`
* `variational_transport := HasCategoricalEOM.transport`

All three project a class field whose declared type is character-for-character
the theorem's conclusion — the shape AGENTS.md §3b-cond item 5 names as a
vacuous self-assuming projection. Verified by reading `:159` against `:197`, not
by the detector, which cannot see them.

**Scale, as a LOWER BOUND, not a census:** a narrow scan (class declared in the
same file, binder **anonymous**, proof term `ClassName.field`) finds **91 such
declarations across 2898 `.lean` files** in the QOU library. The scan is
calibrated against the three probes above: it flags B and correctly ignores A
and C, which the audit already sees.

🛑 **91 is a count of the SHAPE, not of defects.** Rule 2 additionally compares
the field's declared *type* against the conclusion, and a class carrying genuine
*hypotheses* that a theorem composes is legitimate — `q_bkm_criterion` is the
corpus's verified exemplar, and bean `qou-qf8t` measured and **refuted** the
tempting shortcut that counting distinct field projections discriminates the two.
The scan makes no type comparison. Read the 91 as *"candidates the audit cannot
even consider"*, not as 91 violations. The three `variational_*` above were
checked by hand and are genuine.

**No fix is proposed here, deliberately.** Row 43 of
[`2026-08-15-detector-blindness-taxonomy.md`](2026-08-15-detector-blindness-taxonomy.md)
records that fixing this same script's scan scope destroyed 106 of 329 committed
adjudications. Widening rule 2 would re-classify the whole
`lean-vacuity-review-ledger`, which is an owner call and not a side effect of a
branch sent to do something else. Tracked as its own bean, cross-referencing
`qou-24m2` / `qou-sa5c` / `qou-qf8t`.

## 5. Reproduce

```bash
# the new file, lean-direct against the main checkout's restored oleans
lean -DautoImplicit=false -s 65536 \
  content/quantum-observable-universe/lean/QOU/FrobeniusHopfData/PairingVariationalDerivative.lean

# the required audit on the new file
python3 scripts/lean-self-assuming-audit.py \
  content/quantum-observable-universe/lean/QOU/FrobeniusHopfData/PairingVariationalDerivative.lean

# the blind-spot probes are in §4 above; recreate them as two 10-line files
# differing only in `(ctx : C)` + `ctx.field` vs `[C]` + `C.field`.
```
