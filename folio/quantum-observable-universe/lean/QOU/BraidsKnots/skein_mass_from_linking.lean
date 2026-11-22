import Mathlib.Algebra.BigOperators.Group.Finset.Basic
import Mathlib.Data.Real.Basic

/-!
# QOU.BraidsKnots.skein_mass_from_linking

Canonical declaration for content block
[`lem:skein-mass-from-linking`](../../../mass-theory/skein-mass-from-linking.md):
*Mass functional on a Skein resolution: linking-energy plus constituent
volume*.  The `lean.ref` URI
`qou:QOU.BraidsKnots.skein_mass_from_linking` resolves here.

**Lemma statement** (from manuscript): evaluating the mass functional
$\mathfrak{m}$ on the terminal Skein resolution of a hadron $H$ gives

$$
  \mathfrak{m}(H)
  =
  Q(q) \cdot \mathfrak{m}(\mathcal{L}_{\mathrm{Hopf}})
  +
  \sum_{i=1}^{n}
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{2}},
$$

where the first term is the binding energy from linking and the second
is the constituent mass (zero for torus-knot constituents),
$Q(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial of the linking
configuration, and $\hbar_q = 1 - q^{-1}$.

## 2026-09-03 — the previous docstring described a repair that was never made

This module's header used to say:

> *"It does **not** carry the Skein mass identity as a projected field
> (the previous version carried `claim_skein_mass_from_linking` and a
> `def` handing it back — the self-assuming projection forbidden by
> AGENTS.md §3b-cond item 5)."*
>
> *"`skein_mass_from_linking` states the **real** manuscript identity as a
> theorem over the class's data fields; it is unproved (`sorry` +
> manuscript citation per AGENTS.md §1a disposition 2)."*

Neither sentence described the code beneath it.
`SkeinMassFromLinkingContext` **did** carry the identity, as a field
`mass_identity`, and `skein_mass_from_linking` ended not in `sorry` but in
`ctx.mass_identity` — the projection, under prose naming the rule it
violates.  Only the rename `claim_skein_mass_from_linking → mass_identity`
had happened; the *class* docstring recorded that honestly ("carried as an
upstream class field"), and the module docstring above it went on asserting
the opposite.  This is the second file in this drain with that exact shape
(cf. `QOU.Archimedean.knot_operator_selection`), and in both the prose was
the only place the repair existed.

## Why `sorry` (disposition 2) would not have been sound either

With `mass`, `Q`, `mass_Hopf`, `n` and `Vol_K` chosen by the instance, the
identity is **refutable** — `not_skeinMassDecomposition_of_free_data` below
takes `mass = 1` against `Q = mass_Hopf = 0`, `n = 0`, and gets `1 = 0`.  A
`sorry` there would read as "true, not yet proved" over a statement that is
false at freely-chosen data, which is worse than the projection it would
replace.

The lemma is about *the* mass functional evaluated on *the* terminal Skein
resolution of a hadron, not about arbitrary reals, and this development
constructs none of those objects.

## Disposition: name it, assert nothing (AGENTS.md §1a, disposition 3)

`skein_mass_from_linking` is now a **`Prop`-valued definition over
caller-supplied data**.  A caller who has an actual Skein resolution
supplies its data and takes this as an ordinary hypothesis, and it
constrains them because the data are theirs.

Two things make this a better fit for disposition 3 than
`QOU.BraidKnot.six_term_mass_formula_complete`, where naming the claim
recovered nothing:

* `hbar_q` is no longer free.  `hbarQ q = 1 - q⁻¹` is a definition here, so
  the manuscript's `ℏ_q = 1 − q⁻¹` is encoded **structurally** rather than
  carried as an assumption an instance could satisfy vacuously.
* The torus-knot specialisation is a genuine consequence and is **derived**
  from the named `Prop` as a hypothesis (`skein_mass_torus_constituents`),
  so the file contains a real implication rather than only a schema.

## What is still unencoded, stated rather than implied

The mass functional `𝔪`, the Skein resolution and its terminality, and
`Q` being the **Skein polynomial** of the linking configuration are not
constructed anywhere in this file — `Q` is a real number, not a Laurent
polynomial evaluated at `q`.  So the decomposition names which quantities
are added, not why they are the ones that appear.

Note also what the manuscript's own proof
([`skein-mass-from-linking-proof.md`](../../../mass-theory/skein-mass-from-linking-proof.md))
establishes: it restates the decomposition and then derives the torus-knot
case from it.  The decomposition itself is asserted there too, so the Lean
is faithful to the manuscript in leaving it unproved — the gap is the
manuscript's, not this file's.

Bean `qou-z9ws`.
-/

namespace QOU.BraidsKnots

/-- Substrate q-Planck constant `ℏ_q = 1 − q⁻¹`.

A definition rather than a data field with a `hbar_q_def` hypothesis: as a
field an instance chooses `hbar_q` and the constraint merely records the
choice, whereas here the manuscript's relation holds by construction. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
noncomputable def hbarQ (q : ℝ) : ℝ := 1 - q⁻¹

/-- **The claim of `lem:skein-mass-from-linking`**, as a proposition over
caller-supplied data:

`𝔪(H) = Q(q) · 𝔪(L_Hopf) + Σ_{i < n} Vol(Kᵢ) / ℏ_q²`

with `ℏ_q = hbarQ q`.  **Named, not asserted** — see the module docstring
for why neither a projection nor a `sorry` is the honest form here. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
def skein_mass_from_linking
    (q mass Q mass_Hopf : ℝ) (n : ℕ) (Vol_K : ℕ → ℝ) : Prop :=
  mass = Q * mass_Hopf +
    (Finset.range n).sum (fun i => Vol_K i / hbarQ q ^ 2)

/-- **Torus-knot specialisation** — *derived* from the decomposition rather
than projected.

When every constituent is a torus knot (`Vol(Kᵢ) = 0` for all `i`, the
hyperbolic volume of a torus knot vanishing), the constituent sum drops and
the hadron mass is pure linking energy, `𝔪(H) = Q(q) · 𝔪(L_Hopf)`.

This is the one step the manuscript's proof actually derives, and it is the
reason the decomposition is worth naming: it is a hypothesis something is
proved *from*. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/skein-mass-from-linking-proof.md
theorem skein_mass_torus_constituents
    {q mass Q mass_Hopf : ℝ} {n : ℕ} {Vol_K : ℕ → ℝ}
    (hmain : skein_mass_from_linking q mass Q mass_Hopf n Vol_K)
    (h : ∀ i, Vol_K i = 0) :
    mass = Q * mass_Hopf := by
  simpa [skein_mass_from_linking, h] using hmain

/-- **The decomposition is refutable at freely-chosen data**, which is why
it is named rather than carried as a `sorry`.

At `mass = 1` with `Q = mass_Hopf = 0` and no constituents, it reads
`1 = 0`.  Recorded as a theorem so the module docstring's argument is
checked rather than asserted, and so a later attempt to "finish" this file
by adding a `sorry` over free data fails against a standing
counterexample. -/
-- Ref: [leitner2026] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
theorem not_skeinMassDecomposition_of_free_data :
    ¬ skein_mass_from_linking 2 1 0 0 0 (fun _ => 0) := by
  simp [skein_mass_from_linking]

end QOU.BraidsKnots
