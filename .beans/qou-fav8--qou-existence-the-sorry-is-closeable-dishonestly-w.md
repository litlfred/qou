---
# qou-fav8
title: 'QOU existence: the sorry is closeable DISHONESTLY, which is the real finding'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:56:32Z
updated_at: 2026-08-16T17:44:32Z
---

## The sorry

`content/quantum-observable-universe/quantum-observable-universes/quantum-observable-universe-exists.lean:34`

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
