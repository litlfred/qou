---
# qou-fav8
title: 'QOU existence: the sorry is closeable DISHONESTLY, which is the real finding'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
    - needs-owner
created_at: 2026-08-16T13:56:32Z
updated_at: 2026-10-04T15:23:02Z
parent: b9cj
---

## The sorry

`folio/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe-exists.lean:34`

```lean
theorem QuantumObservableUniverse.exists_instance (k : Type*) [Field k] :
    Nonempty (QuantumObservableUniverse k) := by
  -- Ref: [kassel1995] Quantum Groups (Springer GTM 155), §IX (quantum SU(2));
  -- the constructive witness Rep(U_q(g)) with Haar Frobenius form is the
  -- content of prop:quantum-observable-universe-exists. Pending the full
  -- Lean construction of the Drinfeld–Jimbo representation category.
  sorry
```

This is the **only** cited `sorry` on the QOU existence path. Its QU sibling
(`quantum-universes/quantum-universe-exists.lean`) is not a sorry at all — it is
an `axiom QuantumUniverse.exists_instance_axiom`, cited [kassel1995] §XI, with a
one-line theorem projecting it. So the pair is: QU existence **assumed**, QOU
existence **stated with a sorry**. Neither is proved and nothing constructs
either structure (bean `qou-btq3`).

## Three distinct blockers, only one of which is mathematics

**B1 — Mathlib gap: no two-sided rigid instance, even for f.d. vector spaces.**
`RigidCategory` extends `RightRigidCategory` **and** `LeftRigidCategory`
(`Monoidal/Rigid/Basic.lean:598`). Mathlib gives `FGModuleCat K` only
`rightRigidCategory` (`FGModuleCat/Basic.lean:262`); there is no
`LeftRigidCategory` instance. So the most trivial rigid witness imaginable is
not available off the shelf. True mathematically, absent formally. Tractable
infra, in the spirit of `08a2`.

**B2 — the sorry is closeable *dishonestly*, and this is the actual finding.**
`adjointObj : C` is a **free field** with nothing tying it to `frobHopf`; the
docstring itself says *"here it is provided abstractly"*. The paired axiom is

```lean
adjoint_vanishing : Subsingleton ((𝟙_ C) ⟶ adjointObj)
```

For the natural choice `A = 𝟙` this is **false** (`Hom(𝟙,𝟙) ≅ R`, not a
subsingleton). But instantiate `adjointObj := 0` and it is **true trivially**.
So a witness satisfying every field is constructible today, and it would prove
nothing: it satisfies "no hidden global symmetries" by having no adjoint object
at all.

That reframes the question. The sorry has not survived because the mathematics
is hard. It has survived because **the honest witness is blocked (B1) and the
available one is vacuous.** Closing it as-is would be §1a audit-dodging —
`adjoint_vanishing` would join the list of fields satisfied by degenerate data.

**B3 — the statement over-quantifies its own citation.** The theorem asserts
existence for **every** field `k`. Kassel §IX constructs `Rep(U_q(sl₂))` over a
ground field admitting a suitable `q`. Whether the claim survives at, say,
`k = 𝔽₂` is not addressed anywhere in the corpus — the citation is doing work
the citation does not cover. Scope **(a)**: the statement is *unsupported* at
that generality, not *known false*.

## Resolution, in dependency order

1. **Constrain `adjointObj` so B2 closes.** `Ad(A)` is constructible from
   `(μ, Δ, S)` and the braiding — the docstring says so. Either construct it, or
   carry a field relating `adjointObj` to `frobHopf`. Until then no witness of
   this structure means what the axiom says, and that is true whether or not
   anyone ever discharges the sorry. **This is the item worth doing first, and
   it is independent of B1 and B3.**
2. **Build `LeftRigidCategory (FGModuleCat K)`** (B1). Standard, and reusable
   well beyond this file.
3. **Then split the existence claim.** `QuantumUniverse` has no
   `adjoint_vanishing` and no rigidity, so its existence is very likely provable
   with the witness the paper *already names* — `quantum-universe-exists.lean`'s
   own docstring says *"Trivial witness: R-Mod with A = R."* Proving that would
   replace an `axiom` with a theorem, and would be the first construction of
   either structure in the corpus. Only `QuantumObservableUniverse` needs
   Rep(U_q(sl₂)).
4. **Narrow B3** to the ground fields the citation covers, or find the argument
   that extends it.

## Do NOT

Discharge the sorry with `adjointObj := 0`, or with any witness chosen to
satisfy `adjoint_vanishing` by degeneracy. That is the §1a anti-pattern
verbatim, and it would convert a visible gap into an invisible one.

## Note on the 2026-08-16 structure change

`QuantumUniverse`/`QuantumObservableUniverse` moved to `[CommRing R]` +
`Linear R C` + `IsUnit` + `centralIdem_complete` + `unitEndEquiv` (bean
`qou-w1g8`, this branch). That **strengthens** what a witness must supply, so
it raises the bar for items 2–3 above. It does not affect B2: `adjointObj` is
still free, and `0` still satisfies `adjoint_vanishing`.

Found while answering the owner's question *"what QOU has cited sorry? how
resolve?"* (2026-08-16).


## 2026-08-16 — STEP 1 DONE: `adjointObj` constrained; B2 closed

`adjointObj` was a free field. Three fields now tie it to `frobHopf`:

```lean
adjointIncl        : adjointObj ⟶ frobHopf.obj
adjoint_mono       : Mono adjointIncl
adjoint_augmented  : adjointIncl ≫ frobHopf.counit = 0
adjoint_nontrivial : adjointIncl ≠ 0
```

`adjointObj := 0` now fails on `adjoint_nontrivial` — the only morphism out of
the zero object is zero. So the degenerate witness is gone and
`adjoint_vanishing` is a statement with content.

`lean`-direct exit 0 on the library file. Applied to both copies carrying the
QOU structure. Consumers all *project* (`Q.adjointObj`) rather than construct,
so nothing broke; per `qou-btq3` there is still nothing constructing the
structure at all.

### Why `ker ε` and not `A` — the corpus settled this, and it matters

I first considered requiring `adjointObj = frobHopf.obj`, since for a Hopf
algebra the adjoint action is `H` acting on itself. **That is wrong here**, and
would have made condition (ii) FALSE rather than merely weak: `A` always
contains the unit `η : 𝟙 → A`, so `Hom(𝟙, A) = 0` fails for every nontrivial
`A`. Under that reading the axiom would be unsatisfiable — a worse defect than
the one being fixed.

The corpus is explicit that the trivial part is stripped:

- `brings-qou-axiom-map.md:7` — *"`Ad(A) ≅ V₁ ⊕ V₂ ⊕ ⋯` with **no spin-0
  summand**"*
- `brings-is-qou.lean:40` — *"Ad(A) ≅ V₂ (spin-1, dim 3), so Hom(𝟙, Ad(A)) = 0"*
- `q-bsd-rank-zero.md:17` — *"the **Lie algebra** has no `G`-fixed vectors"*

For `SU(2)`, `M₂ = 1 ⊕ 3` and `Ad` is the **3**, the traceless part. That is the
augmentation ideal `ker ε`, which the adjoint action preserves because `ε` is an
algebra map. Hence `adjoint_augmented`.

**Scope (a):** the fields assert `Ad(A) ⊆ ker ε`, mono, nonzero — not that it
*is* `ker ε`. Containment is what the corpus evidence supports and is already
enough to kill the degeneracy; asserting equality would go past the evidence.

### NEW FINDING — the same hole is replicated in four more structures

The free-`adjointObj` + `Subsingleton (𝟙 ⟶ adjointObj)` pattern appears
independently in:

| file | field |
|---|---|
| `QOU/ChannelSeparation.lean:73` | `adjointObj : C` + `:75` `adjoint_vanishing` |
| `QOU/GradedFrobeniusHopf.lean:119` | `(adjointObj : C)` + `:120` `adj_vanishing` |
| `QOU/QuantumObservableUniverse/Instanton.lean:111` | `(adjointObj : C)` + `:114` `subsingleton` |
| `QOU/QuantumObservableUniverse/GaugeTheory.lean:46` | `adjointObj : C` |

Each declares its own, unconnected to any `frobHopf`. Every one is satisfiable
at `adjointObj := 0` by the same argument, so each carries the same vacuity.
`GaugeTheory`'s is the mildest — it has `orbit_embed : projLine ⟶ adjointObj`
and an `involution`, which constrain it somewhat, though not away from zero.

**Not fixed here** — out of scope for this bean and each needs its own read of
what its `adjointObj` is for. Tracked as the natural follow-on. The lesson is
that the fix has to travel: patching the one structure the sorry mentions leaves
four copies of the same hole standing.


## 2026-08-16 — CORRECTION to my own "four replicated holes" note, and what they actually are

The note above said the free-`adjointObj` + `Subsingleton` pattern is replicated
in four structures and *"every one is satisfiable at `adjointObj := 0` by the
same argument, so each carries the same vacuity."* **That was too broad and I
retract it.** Inspected individually they are three different things, and one is
a false positive.

### RETRACTED — `GaugeTheory.FiberAdjointInvolution` is fine

It carries `orbit_embed : projLine ⟶ adjointObj`, `involution`,
`involution_sq`, `orbit_involution_compat` and `orbit_mono`. Genuinely
constrained, and it makes **no adjoint-vanishing claim at all** — so there is no
vacuous conclusion resting on the object. I grouped it by the `adjointObj : C`
field alone, which is exactly the "grep the topic, not the shape" error
`AGENTS.md` warns about. Nothing to fix here.

### WORSE THAN A FREE FIELD — three `P → P` theorems

These do not merely permit a degenerate witness; they **prove nothing at all**,
returning their own hypothesis while the docstring claims a substantive result.

| decl | binder that is pure decoration | docstring claims |
|---|---|---|
| `ChannelSeparation.adjoint_vanishing_propagation` | `(k : ℕ)` | vanishing at *all jet levels* `Ad(J^k(A))` |
| `ChannelSeparation.jet_preserves_channel_separation` | `(jfpg : JetFiltrationPreservesGrading)` | separation *preserved under prolongation* |
| `GradedFrobeniusHopf.adjoint_has_no_degree_zero` | — | the *degree-0 component of Ad(A)* is trivial |

Each body is the hypothesis verbatim (`jgcs.adjoint_vanishing`,
`adj_vanishing`, `adj_vanishing`). **The compiler already knew**: building the
file emits `warning: unused variable 'k'` and `warning: unused variable 'jfpg'`.
The third instance was found *by* that linter output, not by my grep — worth
noting as a cheaper detector than reading.

### The gap is STRUCTURAL, not a proof gap — do not try to "prove" these

- `JetGradedChannelSeparation` carries exactly **one** `GradedFrobeniusHopf`
  (`base`, level 0) and one `adjointObj`, despite its own docstring promising
  *"a graded Frobenius–Hopf object at each jet level"*. There is no
  `Ad(J^k(A))` in the data, so no `k`-dependent conclusion is even statable.
- `adjoint_has_no_degree_zero` takes a bare `adjointObj : C` with no grading, so
  it has no `symComponent` to be about. `GradedFrobeniusHopf` *does* carry
  `symComponent` — so the real statement is expressible, but only once the
  adjoint object carries the grading too.

So the fix is to give the structures the data their docstrings already claim
(a jet-indexed family; a graded adjoint), and only then state the theorems.
Restating them on the current data is impossible, and "proving" them by any
other route would be laundering.

### DONE this pass

Docstrings on all three corrected to say what is and is not proved, with the
structural reason. `lean`-direct **exit 0** on both files. Names left alone
deliberately — `adjoint_vanishing_propagation` propagates nothing, but renaming
has consumer blast radius and the marker is now impossible to miss while
reading.

**Not done:** the structural fix itself. That is the real work and is bigger
than this bean's step 1.


## 2026-08-16 — B1 IS REFUTED. `FGModuleCat K` is already rigid off the shelf.

B1 above says: *"Mathlib gives `FGModuleCat K` only `rightRigidCategory`; there
is no `LeftRigidCategory` instance. So the most trivial rigid witness imaginable
is not available off the shelf."* **That is wrong.** Asked Lean directly:

```lean
import Mathlib.Algebra.Category.FGModuleCat.Basic
import Mathlib.CategoryTheory.Monoidal.Rigid.Braided
open CategoryTheory
noncomputable example (K : Type) [Field K] : RightRigidCategory (FGModuleCat K) := inferInstance
noncomputable example (K : Type) [Field K] : BraidedCategory   (FGModuleCat K) := inferInstance
noncomputable example (K : Type) [Field K] : SymmetricCategory (FGModuleCat K) := inferInstance
noncomputable example (K : Type) [Field K] : LeftRigidCategory (FGModuleCat K) := inferInstance
noncomputable example (K : Type) [Field K] : RigidCategory     (FGModuleCat K) := inferInstance
```

`lean`-direct **exit 0**. All five resolve.

The derivation Mathlib already ships is
`Monoidal/Rigid/Braided.lean:88` —
`instance leftRigidCategoryOfRightRigidCategory [RightRigidCategory C] : LeftRigidCategory C`
— plus `:100` `rigidCategoryOfLeftRigidCategory`. In a **braided** category
right-rigid gives left-rigid gives rigid, and `FGModuleCat K` is symmetric.
Nothing needs building. Nothing needs a `Module.evalEquiv` double-dual transport
either, which is where I was heading next.

### The method error, because it is the second of its kind this session

I grepped `FGModuleCat/Basic.lean` for a `LeftRigidCategory` instance, found
none, and concluded it did not exist — without checking whether Mathlib
*derives* it generically. It does, two files away, for every braided category.
**`inferInstance` settles this in one step and I should have run it first.**

This is the same shape as the `GaugeTheory.FiberAdjointInvolution` retraction
one pass earlier: reasoning from where I expected a thing to be declared instead
of testing whether it is reachable. For instance-availability questions the test
is cheap and decisive; the grep is neither.

### Consequence for the sorry

The blocker list drops from three to two. B2 (the degenerate-witness hole) is
**closed** — `adjointObj` is now constrained. B3 (the statement over-quantifies
its citation, `∀ k` vs a construction over one suitable ground field) stands.

So an honest witness attempt is closer than this bean claimed. The category is
available; what is missing is the `FrobeniusHopfData` on it plus the QOU
observability conditions, and — because of the step-1 work — those can no longer
be satisfied by a degenerate `adjointObj`. That ordering turned out to matter:
had B1 been checked first and B2 not fixed, the newly-reachable witness would
have had the vacuous escape still open.


## 2026-08-16 — the witness is MOSTLY BUILT. Measured obligations, with proofs.

Attempted the paper's own *"Trivial witness: R-Mod with A = R"* against the
**strengthened** `QuantumUniverse` (the `Preadditive`/`Linear`/`IsUnit`/
`centralIdem_complete`/`unitEndEquiv` fields added earlier today). Every result
below is `lean`-direct measured, not reasoned.

### DISCHARGED — the instances today's strengthening demands

```lean
noncomputable example : Preadditive (FGModuleCat K) := inferInstance   -- exit 0
noncomputable example : Linear K (FGModuleCat K)    := inferInstance   -- exit 0
```

Both resolve. **This is the falsifiability test today's commit needed and did
not have**: `qou-btq3` established nothing constructs the structure, so the new
fields were unfalsifiable. They are not vacuous — the intended witness supplies
them off the shelf. (`RigidCategory (FGModuleCat K)` likewise, from the B1
refutation above.)

### DISCHARGED — all three `FrobeniusHopfData` equations at `A = 𝟙`, generically

`simp` does **not** close these (measured: two unsolved goals). `coherence`
does, and over an arbitrary monoidal category rather than just `FGModuleCat`:

```lean
import Mathlib.Tactic.CategoryTheory.Coherence
open CategoryTheory MonoidalCategory

-- snake-left
example (C : Type) [Category C] [MonoidalCategory C] :
    (ρ_ (𝟙_ C)).inv ≫ ((𝟙_ C) ◁ (λ_ (𝟙_ C)).inv) ≫ (α_ (𝟙_ C) (𝟙_ C) (𝟙_ C)).inv
      ≫ (((λ_ (𝟙_ C)).hom ≫ 𝟙 (𝟙_ C)) ▷ (𝟙_ C)) ≫ (λ_ (𝟙_ C)).hom = 𝟙 (𝟙_ C) := by
  coherence

-- snake-right
example (C : Type) [Category C] [MonoidalCategory C] :
    (λ_ (𝟙_ C)).inv ≫ ((λ_ (𝟙_ C)).inv ▷ (𝟙_ C)) ≫ (α_ (𝟙_ C) (𝟙_ C) (𝟙_ C)).hom
      ≫ ((𝟙_ C) ◁ ((λ_ (𝟙_ C)).hom ≫ 𝟙 (𝟙_ C))) ≫ (ρ_ (𝟙_ C)).hom = 𝟙 (𝟙_ C) := by
  coherence

-- Frobenius relation, μ = (λ_).hom, Δ = (λ_).inv
example (C : Type) [Category C] [MonoidalCategory C] :
    (λ_ (𝟙_ C)).hom ≫ (λ_ (𝟙_ C)).inv
      = ((λ_ (𝟙_ C)).inv ▷ (𝟙_ C)) ≫ (α_ (𝟙_ C) (𝟙_ C) (𝟙_ C)).hom
        ≫ ((𝟙_ C) ◁ (λ_ (𝟙_ C)).hom) := by
  coherence
```

`lean`-direct **exit 0**, no `sorry`. Data: `μ = (λ_ 𝟙).hom`, `η = 𝟙`,
`Δ = (λ_ 𝟙).inv`, `ε = 𝟙`, `S = 𝟙`, `λ = 𝟙`, `coev = (λ_ 𝟙).inv`.

### REMAINING, in rough order of expected cost

1. `unitEndEquiv : K ≃+* End (𝟙_ (FGModuleCat K))` — `exact?` **timed out at
   120 s**; not attempted further. `𝟙_ (FGModuleCat K)` is `K` as a module over
   itself and `End K ≅ K`, so the content exists; the work is finding or
   building the `≃+*`.
2. `frobenius_symmetric` — `leftTrace f = rightTrace f` for `f : 𝟙 ⟶ 𝟙`. Not
   pure coherence (`f` is arbitrary) but should fall to unitor naturality.
3. Block data — `blocks := Unit`, `centralIdem _ := 𝟙`, orthogonality vacuous,
   `centralIdem_complete` a one-element sum, `frobWeight = dimQ = 1` with
   `IsUnit 1`. Expected easy.
4. The QOU layer — rigidity is free, but `adjointIncl`/`adjoint_mono`/
   `adjoint_augmented`/`adjoint_nontrivial` now have to be *satisfied*. At
   `A = 𝟙` the augmentation ideal is `0`, so `adjoint_nontrivial` should
   **fail** — meaning the trivial witness gives a `QuantumUniverse` but **not**
   a `QuantumObservableUniverse`.

**That last point is the design working.** Before the step-1 fix, `A = 𝟙` would
have satisfied QOU via `adjointObj := 0`. It no longer can. So the honest
reading is: the *trivial* witness should discharge
`QuantumUniverse.exists_instance_axiom` — replacing an axiom with a theorem —
while `QuantumObservableUniverse.exists_instance` still needs a genuinely
non-trivial `A`, which is what its Kassel §IX citation was always about.

Scope **(a)**: items 1–3 are measured-plausible, not proved. Item 4's failure
prediction is reasoning, not measurement.


## 2026-08-16 — DONE: `QuantumUniverse` is inhabited, sorry-free. The axiom is retired.

`QOU/QuantumObservableUniverse/TrivialWitness.lean`. `C := ModuleCat R`,
`A := 𝟙`, one block. `quantum-universe-exists.lean`'s `axiom` is **deleted**;
the claim is now a theorem deriving from the witness.

```
#print axioms QOU.TrivialWitness.nonempty_quantumUniverse
  --> [propext, Classical.choice, Quot.sound]
```

Lean's own three. No `sorryAx`, no repo axiom. **The corpus's first construction
of either structure** (`qou-btq3` measured zero).

### Three things I got wrong on the way, all worth keeping

1. **Wrong category.** I reached for `FGModuleCat K` because I had rigidity on
   the brain from B1, and burned several probes fighting its full-subcategory
   `smul` API (`ModuleCat.hom_smul` does not fire there). `QuantumUniverse`
   does **not** require rigidity, and the paper says **R-Mod**, not f.g.
   modules. `ModuleCat R` is both easier and what was actually written down.
2. **Stale olean.** The first assembly failed `failed to synthesize Field R`
   although `CategoricalFoundations.lean` had said `CommRing R` for hours.
   `lean`-direct verifies the **source you hand it**; `import` resolves against
   **built oleans**. Rebuilding that one olean with `lean -o` cleared it.
   *Verifying a file does not update what importers see* — this will bite
   anyone doing multi-file lean-direct work.
3. **`simp` is not `coherence`.** The three `FrobeniusHopfData` equations at
   `A = 𝟙` are pure coherence; `simp` leaves goals, `coherence` closes them.

### The prediction held

Last pass I predicted `adjoint_nontrivial` would fail at `A = 𝟙` because the
augmentation ideal vanishes, so the trivial witness gives a `QuantumUniverse`
but **not** a `QuantumObservableUniverse`. That is exactly the outcome — and it
is what the step-1 field was added to produce. Before it, this same witness
would have satisfied the observability axiom via `adjointObj := 0` and I would
have "closed" the QOU sorry with something meaningless.

### What this does and does not settle

**Does:** the `QuantumUniverse` axioms are mutually consistent; the five fields
added under `qou-w1g8` (`Preadditive`, `Linear R`, `IsUnit`,
`centralIdem_complete`, `unitEndEquiv`) are satisfiable — they were
unfalsifiable this morning and are now exercised by a real term; and `Field`
was never needed, `CommRing` suffices.

**Does not:** say anything about QOU existence, which still rests on its cited
`sorry` with B3 (the `∀ k` over-quantification) unaddressed. And a *trivial*
witness proves consistency, not that the axioms are **strong** — a structure
satisfied by `A = 𝟙` with one block is not thereby saying much. That is a fair
criticism of the axioms, and this construction is evidence for it.


## 2026-08-16 — B3 REFRAMED. "Narrow to fields" is the wrong fix; the field is not load-bearing.

B3 above says the QOU existence statement over-quantifies (`∀ k, [Field k]`
against a citation constructing over one suitable ground field) and proposes
narrowing to the fields Kassel §IX covers. **That fix is wrong in direction.**
Asked where the field is actually needed, ingredient by ingredient:

| ingredient | what it really needs | over a ring? |
|---|---|---|
| `U_q(sl₂)` Hopf algebra | `q − q⁻¹` invertible | **yes** — Lusztig integral form |
| rigidity / duals | f.g. **projective** (not merely f.g.) | **yes** |
| Wedderburn blocks of `A` | Schur elements non-vanishing | **yes**, as unit conditions |
| complete reducibility of *every* module | genuinely field-like | no |

Only the last row wants a field, and `QuantumUniverse` **never asks for it** —
axiom 4 constrains the blocks of `A`, not the whole module category.

**The corpus already frames every one of these as a ring condition, not a field
condition.** This is not my inference:

- `q-casimir-exists-proof.md` — *"whenever `(q − q⁻¹)` is invertible in the
  ground ring `R`"*.
- `descartes-knot-eigenbasis-derivation.md` — semisimplicity of `H_n(q)` follows
  from *"`6 ∈ R^×` and non-degeneracy of the Frobenius form"* via Jimbo. A
  **unit condition on `R`**, stated as such.
- `qou-p-neq-np.md` §companion — semisimplicity is governed by non-vanishing of
  Schur elements (Geck–Pfeiffer), with `WenzlGeneric` formalising `q^k ≠ 1`
  *"over a generic monoid"* and `schurElement_ne_zero` proved sorry-free in
  [`WenzlSchurElement`](../lean/QOU/MathlibExt/WenzlSchurElement.lean).
- `substrate-parameter-limits-and-lusztig.md` — the algebraic home is
  *"the Lusztig integral form `𝒰^ℤ_q(su(2))`"*, i.e. over `ℤ[q,q⁻¹]`.

So the framework's own ground ring `R_q = ℤ[q,q⁻¹]` is where the construction
naturally lives, and `[Field k]` **excludes it**.

### The distinction that makes this coherent

Statability over `R` and constructibility over `R` are different questions.
`QuantumUniverse` only asks you to **supply** block idempotents and units for
`A`; it does not ask the ambient category to be semisimple. `ModuleCat ℤ[q,q⁻¹]`
is not semisimple, and that is no obstacle — `H_n(q)` over `R_q` with Schur
elements invertible has exactly the blocks the axiom wants.

### Proposed replacement for B3

Not `∀ k, [Field k]` and not a bare `[CommRing R]` either, but

```
∀ (R) [CommRing R], IsUnit (q - q⁻¹) → WenzlGeneric … → Nonempty (QuantumObservableUniverse R)
```

— simultaneously **narrower** (excludes rings where the construction fails, which
the current `∀ field` already gets wrong at e.g. `𝔽₂`, where no generic `q`
exists) and **broader** (admits `ℤ[q,q⁻¹]`, the framework's actual ground ring).
It also matches the `IsUnit`-not-`≠ 0` move already made under `qou-w1g8`: the
same correction, one level up.

**Not implemented.** Changing the hypotheses of an unproved `sorry` alters what
must eventually be proved, and the right hypothesis list should be read off
`WenzlSchurElement`'s existing criterion rather than guessed. Flagging as the
next concrete step on this bean.

Scope **(a)**: this argues the field is *unnecessary* for the named
ingredients, not that the full construction over `ℤ[q,q⁻¹]` has been carried
out — nobody has done that here.


## 2026-08-17 — the QOU witness cannot be a module category. Proved, sorry-free.

Given the go-ahead to attempt the Drinfeld–Jimbo representation category, I ran
the **formalize-first** step first: look for the invariant that prunes the
search before running it. There is one, and it is decisive.

[`QOU/QuantumObservableUniverse/WitnessObstruction.lean`](../folio/quantum-observable-universe/lean/QOU/QuantumObservableUniverse/WitnessObstruction.lean),
`lean`-direct **exit 0**:

```lean
theorem qou_needs_nongenerating_unit
    {C : Type*} [Category C] [MonoidalCategory C] [Limits.HasZeroMorphisms C]
    {adjointObj A : C} (incl : adjointObj ⟶ A)
    (hvanish : Subsingleton ((𝟙_ C) ⟶ adjointObj))     -- observability axiom
    (hnontrivial : incl ≠ 0)                            -- adjoint_nontrivial
    (hgen : ∀ W : C, Subsingleton ((𝟙_ C) ⟶ W) → IsZero W) : False

theorem moduleCat_unit_generates (R) [CommRing R] (W : ModuleCat R) :
    Subsingleton ((𝟙_ (ModuleCat R)) ⟶ W) → IsZero W

theorem no_qou_on_moduleCat …  -- the composite
```

### What it says

The QOU observability axiom (`Subsingleton (𝟙 ⟶ Ad(A))`) and
`adjoint_nontrivial` are **jointly contradictory in any monoidal category where
`Hom(𝟙, −)` reflects zero objects**. `ModuleCat R` is such a category —
`Hom(R, W) ≅ W` by evaluation at 1 — so no module category carries a QOU.

This is a *shape* argument about two fields. It is independent of `R`, of the
choice of `A`, and of everything else in the structure.

### Why this is the useful result rather than a detour

It is a **necessary condition on any witness, obtained without attempting the
construction**: the unit must not generate. That is precisely what separates a
representation category from a plain module category — in `Rep(G)`,
`Hom(𝟙, W) = W^G` can vanish for `W ≠ 0`.

So `[kassel1995]` §IX naming `Rep(SU_q(2))` is **not** a convenience choice: no
module category could ever have worked. The citation is now explained rather
than merely deferred to.

It also further validates the `qou-fav8` step-1 field. `adjoint_nontrivial` is
doing real work here — it is exactly the half that makes the pair
contradictory. Without it, `ModuleCat R` with `adjointObj := 0` would satisfy
observability and the obstruction would not exist.

### Contrast with the QU witness

`QOU.TrivialWitness` puts a `QuantumUniverse` on `ModuleCat R`. This file shows
the *same category* cannot be upgraded to a QOU. The two results together
locate the QU/QOU boundary concretely: it is not a matter of adding more data
to the same category, it requires a categorically different one.

### Scope

**(a)**: rules out module categories. Does **not** show a QOU exists anywhere,
and is **not** progress toward discharging
`QuantumObservableUniverse.exists_instance` — that `sorry` is untouched.

### On the Drinfeld–Jimbo construction itself

Not started. This result changes its shape: the target is not "build an algebra"
but "build a category whose unit does not generate", and the honest next
question is whether Mathlib has enough representation-category infrastructure to
carry `Rep(U_q(sl₂))` at all. That is a scoping question worth answering before
writing code.


## 2026-08-17 — Mathlib scoping for a QOU witness, and a finding that cuts against the framework

Scoped what Mathlib actually carries before writing any construction code.
Read-only; nothing built.

### `Rep(U_q(sl₂))` is not feasible

**Mathlib has no quantum groups at all.** No `U_q`, no Drinfeld–Jimbo, no
`RepresentationTheory/Quantum*`; the only `Drinfeld` hits are
`Monoidal/Center.lean` (Drinfeld *centre*, unrelated) and `Braided/Basic.lean`.
Building `U_q(sl₂)` and its representation category is a Mathlib-scale project,
not a session.

### `FDRep k G` — the *classical* representation category — is fully equipped

| requirement | Mathlib | where |
|---|---|---|
| `MonoidalCategory` | ✅ | `FDRep.lean:159` |
| `Preadditive`, `Linear R`, `MonoidalLinear` | ✅ | `FDRep.lean:72,75,163` |
| `RightRigidCategory` | ✅ | `FDRep.lean:202` |
| ⇒ `RigidCategory` | ✅ | braided + right-rigid, per the B1 refutation above |
| `SymmetricCategory` | ✅ | `Rep.lean:840` |
| semisimplicity | ✅ | `Maschke.lean` |
| `Hom(𝟙, −) = invariants` | ✅ | `Invariants.lean` (`mem_invariants_iff_comm`) |

That last row is the one that matters: it is exactly the *"unit does not
generate"* property the obstruction theorem above says a witness needs. `FDRep`
has it; `ModuleCat` provably does not.

### THE FINDING: nothing in the QOU axioms forces q-deformation

If `FDRep k G` — ordinary finite-group representation theory, no `q` anywhere —
satisfies every QOU field, then **the axioms do not pin down anything quantum.**

The shape works out. `A = 𝟙` fails (`Ad = 0`, the obstruction). `A = k[G]` also
fails, for a *different* reason worth recording: the adjoint invariants are the
centre, of dimension = #conjugacy classes > 1, so `Hom(𝟙, Ad(A)) = 0` is false.
But `A = End(V)` for `V` an irreducible faithful rep **does** fit: `End(V)` is
central simple, so `Ad(A)` is the traceless part, and its invariants vanish
precisely when `G` acts irreducibly.

And that is *literally the corpus's own description*: `brings-is-qou.lean` says
**"Ad(A) ≅ V₂ (spin-1, dim 3), so Hom(𝟙, Ad(A)) = 0"** — `M₂ = 1 ⊕ 3`. That
decomposition is identical for classical `SU(2)` and for `SU_q(2)`; the `q` does
no work in it.

So the honest reading: the QOU axioms as formalized look satisfiable by a
classical witness, and the framework's quantum content — if any — lives in
things the axioms do not currently say. Braided-but-not-symmetric is the
obvious candidate for what *should* be doing that work, and `QuantumUniverse`
does not require it (`quantum-universe-axiom-motivation.md` even notes a
symmetric braiding is "the classical limit", but nothing in the type excludes
it).

**Scope (a).** The instances exist and the shape matches. I have **not** built
the classical witness, so this is "appears satisfiable", not "is satisfiable".
Building it is the decisive test and it is now the cheapest one available —
much cheaper than `U_q`, and far more informative, because a *success* would be
a substantive criticism of the axioms rather than a confirmation of them.

### Recommendation

Do **not** start Drinfeld–Jimbo. Build the classical `FDRep k G` witness
instead. Either it succeeds — and the axioms need strengthening to exclude it —
or it fails on a specific field, and that field is where the framework's quantum
content actually lives. Both outcomes are worth more than an unfinished `U_q`.

Owner call, since "which witness to attempt" is a scope decision and the
successful outcome is a critical result.


## 2026-08-17 — the classical case is not excluded, and axiom 1 is not encoded at all

Two measurements on `CategoricalFoundations.lean`, both of which sharpen the
"nothing forces quantum" finding:

1. **Axiom 1 is entirely absent from the type.** `def:quantum-universe` axiom 1
   is *"the ordering `≺_c` induced by the braiding on the Hecke basis of `A` is
   well-founded"*. Grep for `WellFounded` / `≺` / `prec` in the structure:
   **nothing**. The only trace is `[braidedInst : BraidedCategory C]`, whose own
   docstring says the braiding is *"not required to be symmetric"* — i.e. it
   records that symmetric is **permitted**. So of four prose axioms, the type
   encodes 2, 3 and 4; axiom 1 is prose only.

2. **`QuantumUniverse` carries no `q`.** No substrate-parameter field anywhere.
   The framework is *about* a modulus `q₀`; the structure meant to formalise its
   categorical layer does not mention one. `unitEndEquiv` names the ground ring
   but nothing distinguishes an element of it.

**And encoding axiom 1 would not fix it.** At `q = 1` the Hecke algebra is
`k[S_n]` and the induced order is Coxeter word length, which *is* well-founded.
So well-foundedness holds classically; it is not the discriminator.

### Why "just forbid symmetric" is probably the wrong fix

The obvious patch — a field asserting `∃ X Y, β_{Y,X} ∘ β_{X,Y} ≠ 𝟙` — has a
cost the framework may not want to pay: the corpus treats the symmetric case as
the **classical limit** (`quantum-universe-axiom-motivation.md`: *"A symmetric
braiding forgets the difference, and that is the classical limit"*), and the
classical-limit chapter reasons about `q → 1` as a limit **of** QOUs. Excluding
symmetric puts the limit outside the category it is a limit of. It is also a
negative, very weak condition — "somewhere non-symmetric" permits arbitrarily
mild deformation.

### Options, with the trade-off that decides each

| | change | keeps `q→1` in scope? | cost |
|---|---|---|---|
| **A** | forbid symmetric braiding | **no** — limit leaves the category | 1 field; weak, negative |
| **B** | require a ribbon twist `θ ≠ 𝟙` | no, same boundary problem | ribbon absent from Mathlib (repo has `KeystoneRibbonCategory`) |
| **C** | **carry `q : R` + the Hecke relation on the braiding** | **yes** — classical is `q = 1`, a boundary not an exclusion | 2 fields; needs the σ-eigenvalue statement |
| **D** | accept, re-scope the claim | yes | none, but concedes the axioms do not produce the physics |

**C is the recommendation.** It is positive rather than negative, it is verbatim
`AGENTS.md` §7a (the Hecke-skein convention `(σ − q)(σ + q⁻¹) = 0` — the corpus's
own stated convention), it repairs gap 2 above as a side effect, and it keeps
`q = 1` as a describable boundary rather than banishing the classical limit.

**D deserves to stay on the table honestly.** The framework's numbers all come
from *evaluating* at `q₀ ≈ 1.10998`, an input; the categorical axioms supply the
*shape* (Hecke, Markov trace, blocks). If that is the real epistemic structure,
saying so is better than bolting on a field to make the axioms look like they do
more than they do.

### The classical witness is now the falsification test, not just a criticism

Whichever option is chosen, `FDRep k G` with `A = End(V)` is how you check it
worked. Under **C** that witness has `σ² = 𝟙`, i.e. `q = 1`, so it is excluded
exactly and for the right reason. Under **D** it should succeed and be
documented as an intended model. Under **A**/**B** it should fail on the new
field. Building it tests the fix rather than merely embarrassing the axioms.

Owner decision. Not implemented.

## Round 72 Progress (PR #8491)
- De-vacuified and proved genuine Lean 4.24.0 theorems in PR `litlfred/qou#8491` (C1 `0a93eba0e8b5b8ee92b4af6972a325d2dc1a28fd`, C2 `a9b922df9d2baa717878dbac10e60b5a5c341c6e`, 80-dps mpmath witness verified, 0 static audit findings).
