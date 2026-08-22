# Two axioms proving `False`, and the 73 content-block Lean files nothing compiles

**Date:** 2026-08-22
**Bean:** `qou-rhax` (high)
**Branch/PR:** `claude/q-ns-classical-gaps-9l9mj9` / #5467
**Scope:** `content/quantum-observable-universe/stochastic-mechanics/macroscopic-stability-equivalence.{lean,md,ts}`, plus a corpus-wide measurement of which content-block `.lean` siblings compile.

---

## 1. The defect

`macroscopic-stability-equivalence.lean` carried two axioms:

```lean
axiom macroscopic_iff_rh_axiom :
    ∀ (ψ : R_q → R_q) (ζ : ℂ → ℂ), MacroscopicStability ψ ↔ RiemannHypothesis ζ

axiom rh_iff_persistence_axiom :
    ∀ (ζ : ℂ → ℂ) (spectral_limit : ℕ → Fin 8 → R_q),
      RiemannHypothesis ζ ↔ SpectralPersistence spectral_limit
```

**Both prove `False`, and for one shared structural reason.** An
`∀ a b, P a ↔ Q b` quantifies its two sides **independently**, which forces
`P` to be constant in `a`: fix any `b` and the right-hand side stops varying,
so all values of `P a` agree with each other.

`RiemannHypothesis` is not constant in `ζ`:

- `RiemannHypothesis (fun _ => 1)` holds **vacuously** — the constant 1 is
  never zero, so the implication's hypothesis `ζ s = 0` is never met.
- `RiemannHypothesis (fun _ => 0)` **fails** — every point of the strip is a
  zero, so `s = 1/4` would have to satisfy `1/4 = 1/2`.

Feed both into either axiom with the other argument fixed, and `False`
follows in four lines.

**Machine-checked** (Lean v4.24.0, `lean`-direct against the restored
Mathlib oleans). A standalone file restating the second axiom derives
`False` from it, and `#print axioms` reports the derivation depends on
nothing but that axiom plus `propext`, `Classical.choice`, `Quot.sound` —
no `sorryAx`, no other input.

The argument uses only `RiemannHypothesis`. It needs neither
`SpectralPersistence`'s content nor `LaurentPolynomial`, so it survives any
repair to those.

### The independently-reported route

`agent:p01` found this on the stochastic-mechanics trap-drain by a different
argument: `SpectralPersistence f`, as written, was

```lean
(∀ (n : ℕ) (i : Fin 8), spectral_limit n i = 1/2) →
  ∀ (i : Fin 8), spectral_limit 0 i = 1/2
```

— *"if every level is ½ then level 0 is ½"*, which is instantiation and is
inhabited by `fun h i => h 0 i`. So the axiom equated `RiemannHypothesis ζ`
with a **tautology**, for every `ζ`. Either route suffices; the
quantifier-shape route is the more general statement, since it also condemns
the first axiom.

---

## 2. Three further defects in the same file

**It had never compiled.** `lean`-direct reports **22 errors**: the two
imports never provided `LaurentPolynomial`; two docstrings sat back to back
before `macroscopic_iff_rh_axiom` (`unexpected token '/--'`); and the
`noncomputable section` was never closed, so the final `end
QOU.AlgebraicSubstrate` failed against an unnamed scope.

This is the real reason the blast radius was contained. The bean recorded
that nothing imports the file — true, but the stronger fact is that **there
was nothing to import**: no declaration in it ever entered any environment.

**`1/2 : R_q` does not elaborate.** `R_q = LaurentPolynomial ℤ` has no `Div`
instance, so `HDiv ℕ ℕ R_q` fails to synthesize. Both `SpectralPersistence`
and `MacroscopicStability` were **ill-typed as written** — the critical-line
condition and the `X ^ (1/2 + ε)` error bound are archimedean statements that
cannot live over a Laurent-polynomial ring. Restated over `ℝ`/`ℂ`, which is
what §7c requires here: the ordering, `|·|` and `rpow` are genuinely
archimedean, so this belongs on the archimedean side of the wall.

**The Weil attribution was wrong.** The second axiom was headed *"External
axiom (Weil 1948 explicit formula): RH ↔ spectral persistence"*. Weil's
explicit formula is a duality between zeros and prime powers. No formulation
of it makes RH equivalent to a proposition in which `ζ` does not occur — and
the removed axiom's right-hand side does not mention `ζ` at all. **The
citation is what made an arbitrary axiom look load-bearing.** It is
withdrawn; the `weil1948` cite is dropped from the block manifest. The von
Koch attribution on the first axiom is accurate for the direction it names
and is retained in prose.

---

## 3. The fix

Both axioms removed. Replaced by a single content-bearing **primary
conjecture class** (§3b, §3b-tax) over **one datum**:

```lean
structure SubstrateSpectralDatum where
  zeta : ℂ → ℂ
  psi  : ℝ → ℝ
  rho  : ℕ → Fin 8 → ℂ

class MacroscopicStabilityEquivalence (D : SubstrateSpectralDatum) : Prop where
  stability_iff_rh     : MacroscopicStability D.psi ↔ RiemannHypothesis D.zeta
  rh_iff_critical_line : RiemannHypothesis D.zeta ↔ CriticalLineSpectrum D.rho
```

Binding `ζ`, `ψ` and `ρ` into one structure **is** the fix. Both fields
quantify over the same `D`, so neither forces either side to be constant in
its argument — which is what the informal statement always meant. This is
the §"Grep the claim SHAPE" item-3 distinction (shared type vs shared
instance) applied as a repair rather than as a review finding.

There is deliberately **no instance**. The honest state of "RH ↔ our
spectral condition" is *open*, not axiomatised (§"Axiomatization is NOT a
Proof"). `CriticalLineSpectrum ρ := ∀ n i, (ρ n i).re = 1/2` constrains the
whole family, so unlike its predecessor it has content.

The one theorem is conditional on the class and derives the equivalence the
class does **not** carry — `(1) ↔ (3)` — by `Iff.trans`. That is a derivation
from the hypotheses, not a projection of a field (§3b-cond item 5, the
failure mode the old `macroscopic_stability_equivalence` exhibited by
returning `⟨axiom₁, axiom₂⟩`).

Two small theorems are kept in the file so the inconsistency argument is
checkable *there* rather than only in commentary:
`riemannHypothesis_const_one` and `not_riemannHypothesis_const_zero`.

**The block is demoted `theorem` → `conjecture`** (`thm:` → `conj:`), with
the three live references retargeted. Both downstream consumers are
`remark`s, which may freely interpret a conjecture (§3a), so no propagation
violation arises.

### Verification

- `lean`-direct on the rewritten file: **exit 0, silent, 2.4 s** — the first
  time this file has ever compiled.
- `#print axioms` on all three declarations: `[propext, Classical.choice,
  Quot.sound]`. No `sorryAx`, no custom axiom.
- Note this file is **not** covered by `lean-content-siblings.yml` and has no
  build target (see §4), so this agent verification is the only gate.

---

## 4. Why it survived: 73 content-block Lean files nothing compiles

Content-block `.lean` siblings live at `content/<paper>/<chapter>/<block>.lean`
— **outside** `content/<paper>/lean/`, and therefore outside the `qou`
package's `globs = ["QOU", "QOU.+"]`. `lake build QOU` never touches them.

Measured with `lean`-direct across all **958** such files, at 6-way
parallelism:

| | count | share |
|---|---:|---:|
| exit 0 | **885** | 92.4 % |
| non-zero | **73** | 7.6 % |

**The first pass of this measurement said 297 (31 %), and that was wrong.**
`LEAN_PATH` held only `.lake/packages/*`, so every file importing `QOU.*`
failed on an unresolvable module. Adding the three paper build directories
moved 224 of the 297 to exit 0. Quoting 31 % would have overstated the
problem by a factor of four — the number is 7.6 %.

By chapter, the 73 concentrate in `mass-theory` (27) and `predicted-spectra`
(10); the rest are scattered ≤ 8 per chapter.

This is the population that lets a file with 22 errors and an inconsistent
axiom sit in the tree indefinitely. The lakefile already records an earlier
widening (bean `qou-rc7b`, `QOU.lean` root → `QOU`/`QOU.+` globs) that
recovered 785 unbuilt modules **inside** `lean/`; the 958 siblings are a
separate population that widening did not reach.

**Not fixed here.** Repairing 73 files, or bringing them under a build
target, is its own tranche and is not in scope for this branch — the
measurement is recorded so the next agent starts from a number rather than
from a guess. The `macroscopic-stability-equivalence.lean` fix removes one
of the 73.

---

## 5. The sibling that got this right

`ClassicalRiemannHypothesis.lean`, flagged clean in the same trap-drain
batch, is the model: a content-bearing class, **no instance**, and a removed
axiom recorded in its docstring. Two files, one chapter, opposite
dispositions — which is what an unbuilt population looks like from the
inside.
