---
# qou-fav8
title: 'QOU existence: the sorry is closeable DISHONESTLY, which is the real finding'
status: todo
type: task
priority: normal
created_at: 2026-08-16T13:56:32Z
updated_at: 2026-08-16T13:57:27Z
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
