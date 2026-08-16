---
# qou-fav8
title: 'QOU existence: the sorry is closeable DISHONESTLY, which is the real finding'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:56:32Z
updated_at: 2026-08-16T16:32:01Z
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
