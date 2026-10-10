---
# qou-rhax
title: 'An axiom in the Lean tree is inconsistent — rh_iff_persistence_axiom proves False'
status: completed
type: task
priority: high
created_at: 2026-08-22T05:45:00Z
updated_at: 2026-08-22T05:45:00Z
---

Found by `agent:p01` on the stochastic-mechanics trap-drain; **confirmed by
reading the source** in the coordinating session. This is the most severe
class of defect the corpus admits: an axiom from which `False` follows.

## The derivation, in four lines

`stochastic-mechanics/macroscopic-stability-equivalence.lean`:

```lean
def RiemannHypothesis (ζ : ℂ → ℂ) : Prop :=
  ∀ (s : ℂ), 0 < s.re → s.re < 1 → ζ s = 0 → s.re = 1/2          -- line 44

def SpectralPersistence (spectral_limit : ℕ → Fin 8 → R_q) : Prop :=
  (∀ (n : ℕ) (i : Fin 8), spectral_limit n i = 1/2) →
    ∀ (i : Fin 8), spectral_limit 0 i = 1/2                        -- line 52

axiom rh_iff_persistence_axiom :
  ∀ ζ spectral_limit, RiemannHypothesis ζ ↔ SpectralPersistence spectral_limit
```

1. **`SpectralPersistence f` is a tautology for every `f`** — inhabited by
   `fun h i => h 0 i`. It says "if every level is ½ then level 0 is ½",
   which is instantiation, not persistence.
2. The axiom is universally quantified over **both** arguments, so it gives
   `RiemannHypothesis ζ ↔ True` for **every** `ζ`, hence
   `RiemannHypothesis ζ` for every `ζ`.
3. Take `ζ := fun _ => 0` and `s := (1/4 : ℂ)`. Then `0 < 1/4`, `1/4 < 1`,
   and `ζ s = 0`, so the definition forces `1/4 = 1/2`.
4. `False`.

## Blast radius: contained, and that is the only good news

`grep -rln` over every `.lean` in the tree: **the file references its own
names and nothing else does.** Nothing downstream inherits the
inconsistency today. But an axiom that proves `False` makes every
`#print axioms` result in that file meaningless, and if anything ever
imports it the whole library becomes unsound.

## Two aggravating details

**The caption attributes it to a paper that does not say it.** The axiom is
headed *"**External axiom (Weil 1948 explicit formula):** RH ↔ spectral
persistence"*. Weil's explicit formula is a duality between zeros and prime
powers; it is not an equivalence between RH and the statement above, and no
formulation of it makes RH equivalent to a proposition with no free
occurrence of ζ. The citation is what makes the axiom look load-bearing
rather than arbitrary.

**The "theorem" built on it is two axiom projections.**
`macroscopic_stability_equivalence` (line 99) is
`⟨macroscopic_iff_rh_axiom ψ ζ, rh_iff_persistence_axiom ζ spectral_limit⟩`.
It asserts a conjunction of two axioms and proves nothing. Under Strict Lean
Discipline §7 — *"No axiom/class may substitute for a proof … Creating
`axiom myResult : P` and then consuming it downstream is NOT proving `P`"* —
that is the pattern by name.

## What would close this

The fix is **not** to weaken the axiom until it is consistent, and **not**
to delete `SpectralPersistence` and keep the equivalence. Either:

1. **State `SpectralPersistence` so that it has content** — the docstring
   describes a genuine limit statement ("given `q_n → 1`, if the Reeb
   eigenvalues at each `q_n` satisfy `Re(ρ_i) = ½`, then the limiting
   spectral data also satisfies it"), which is a claim about a limit the
   type never mentions. Formalise that, and the axiom stops being vacuous
   on the right-hand side; then re-examine whether the equivalence is
   defensible at all.
2. **Or demote the whole file to a conjecture carrier** — a content-bearing
   `class` with no instance, per §3b. The honest state of "RH ↔ our spectral
   condition" is *open*, not axiomatised.

Either way the Weil attribution must go or be replaced with something that
actually states the claim.

## Note on the sibling that got this right

`ClassicalRiemannHypothesis.lean`, flagged clean in the same batch, is the
model: a content-bearing class, **no instance**, and a removed axiom
recorded in its docstring. Two files in one chapter, opposite dispositions.

---

## RESOLVED 2026-08-22 — commit `ac452c37f`, PR #5467

Audit: [`docs/audits/2026-08-22-inconsistent-axioms-and-unbuilt-lean-siblings.md`](../docs/audits/2026-08-22-inconsistent-axioms-and-unbuilt-lean-siblings.md)

Fixed as option 2 (demote to a conjecture carrier). Three corrections and
one extension to this bean's analysis, all confirmed by reading and by
`lean`-direct:

**1. There are TWO inconsistent axioms, not one.** `macroscopic_iff_rh_axiom`
fails by the same route. The general defect is the quantifier shape:
`∀ a b, P a ↔ Q b` forces `P` constant in `a`, and `RiemannHypothesis` is
not constant in `ζ` (vacuous at `ζ ≡ 1`, false at `ζ ≡ 0`). This route needs
neither `SpectralPersistence`'s tautology nor `LaurentPolynomial`, so it is
the more general statement — and unlike the tautology route it also
condemns the first axiom. Machine-checked; `#print axioms` on the `False`
derivation reports only the axiom plus `propext`/`Classical.choice`/`Quot.sound`.

**2. The containment reason is stronger than "nothing imports it": the file
had never compiled.** `lean`-direct reports 22 errors — the imports never
provided `LaurentPolynomial`, two docstrings sat back to back before the
first axiom, and the `noncomputable section` was never closed. No
declaration in the file had ever entered any environment.

**3. `1/2 : R_q` does not elaborate.** `LaurentPolynomial ℤ` has no `Div`,
so `SpectralPersistence` and `MacroscopicStability` were **ill-typed**, not
merely vacuous. Option 1 of this bean ("state `SpectralPersistence` so that
it has content") could not have been done over `R_q` at all — the critical
line is archimedean and the replacement is stated over `ℝ`/`ℂ` per §7c.

**4. Why it survived — measured.** Content-block `.lean` siblings live
outside `content/<paper>/lean/` and so outside the package's
`["QOU","QOU.+"]` globs; nothing compiles them. `lean`-direct across all
**958**: **885 pass, 73 fail (7.6 %)**, concentrated in `mass-theory` (27)
and `predicted-spectra` (10). My first pass reported 297 / 31 % — wrong,
`LEAN_PATH` lacked the three paper build dirs, and adding them moved 224 to
exit 0. Repairing the 73 is a separate tranche and is **not** done here.

**The Weil attribution is withdrawn** and the `weil1948` cite dropped, per
this bean's closing requirement. The von Koch attribution is accurate for
the direction it names and stays in prose.

**Verification:** `lean`-direct exit 0, silent, 2.4 s — first successful
compile of this file. `#print axioms` clean on all three declarations
(`[propext, Classical.choice, Quot.sound]`). `run-validate` exit 0.
`qa-sweep` 0 failing criteria.
