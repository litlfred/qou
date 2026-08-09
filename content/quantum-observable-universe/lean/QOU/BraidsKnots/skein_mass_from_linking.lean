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
$\mathcal{M}$ on the terminal Skein resolution of a hadron $H$ gives

$$
  \mathcal{M}(H)
  =
  Q(q) \cdot \mathcal{M}(\mathcal{L}_{\mathrm{Hopf}})
  +
  \sum_{i=1}^{n}
  \frac{\mathrm{Vol}(K_i)}{\hbar_q^{2}},
$$

where the first term is the binding energy from linking and the second
is the constituent mass (zero for torus-knot constituents),
$Q(q) \in \mathbb{Z}[q^{\pm 1}]$ is the Skein polynomial of the linking
configuration, and $\hbar_q = 1 - q^{-1}$.

## Disposition (integrity)

The class carries only **genuine data**: the substrate parameter `q`,
the evaluated Skein polynomial `Q`, the Hopf-link mass, the constituent
count and volumes, the q-Planck constant `ℏ_q` with its *definitional*
link `ℏ_q = 1 − q⁻¹`, and the hadron mass `𝓜(H)`.  It does **not**
carry the Skein mass identity as a projected field (the previous
version carried `claim_skein_mass_from_linking` and a `def` handing it
back — the self-assuming projection forbidden by AGENTS.md §3b-cond
item 5).

- `skein_mass_from_linking` states the **real** manuscript identity as
  a theorem over the class's data fields; it is unproved (`sorry` +
  manuscript citation per AGENTS.md §1a disposition 2 — stated, not
  yet proved).
- `skein_mass_torus_constituents` is **derived** from it: for
  torus-knot constituents (all `Vol(K_i) = 0`, hyperbolic volume of a
  torus knot vanishes) the constituent term drops and the mass is pure
  linking energy `𝓜(H) = Q(q)·𝓜(L_Hopf)`.  Genuine specialisation, not
  a projection.
-/

namespace QOU.BraidsKnots

/-- Data of the Skein-mass-from-linking claim.  All fields are *inputs*
    (the Skein-resolution data of the hadron); none is the conclusion.
    The only propositional field is the definitional link
    `ℏ_q = 1 − q⁻¹`. -/
class SkeinMassFromLinkingContext where
  /-- The substrate parameter `q`. -/
  q : ℝ
  /-- The Skein polynomial `Q(q)` of the linking configuration,
      evaluated at the substrate parameter. -/
  Q : ℝ
  /-- Mass of the Hopf link `𝓜(L_Hopf)`. -/
  mass_Hopf : ℝ
  /-- Number of constituents. -/
  n : ℕ
  /-- Hyperbolic volume of constituent knot `K_i` (zero for torus-knot
      constituents). -/
  Vol_K : ℕ → ℝ
  /-- Substrate q-Planck `ℏ_q`. -/
  hbar_q : ℝ
  /-- Definitional link: `ℏ_q = 1 − q⁻¹`. -/
  hbar_q_def : hbar_q = 1 - q⁻¹
  /-- Total hadron mass `𝓜(H)` (value of the mass functional on the
      terminal Skein resolution). -/
  mass : ℝ

/-- **Skein mass identity** ([`lem:skein-mass-from-linking`]) — the real
    manuscript claim, stated over the class's data fields:

      `𝓜(H) = Q(q) · 𝓜(L_Hopf) + Σ_{i<n} Vol(K_i) / ℏ_q²`.

    Unproved: the manuscript derivation evaluates the mass functional on
    the terminal Skein resolution (resolve all linking crossings via the
    Skein relation, collect the Hopf-link binding term with coefficient
    `Q(q)`, leave the constituent volume term).  Stated with `sorry` +
    citation per AGENTS.md §1a disposition 2 — no conclusion field on
    the class hands this back. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] :
    ctx.mass = ctx.Q * ctx.mass_Hopf +
      (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) := by
  -- Ref: [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
  sorry

/-- **Torus-knot specialisation** — derived from the Skein mass
    identity: when every constituent is a torus knot (`Vol(K_i) = 0`
    for all `i`, hyperbolic volume of a torus knot vanishes), the
    constituent sum drops and the hadron mass is pure linking energy,

      `𝓜(H) = Q(q) · 𝓜(L_Hopf)`.

    Genuine specialisation of `skein_mass_from_linking` (instantiate
    the volume hypothesis, collapse the zero sum), not a projected
    field. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
theorem skein_mass_torus_constituents [ctx : SkeinMassFromLinkingContext]
    (h : ∀ i, ctx.Vol_K i = 0) :
    ctx.mass = ctx.Q * ctx.mass_Hopf := by
  have hmain := skein_mass_from_linking (ctx := ctx)
  simpa [h] using hmain

/-- **The statement above is refutable as written** — the class never relates
    the fields its conclusion names, so `∀ instances` admits ones that simply
    disagree. Not an open gap: the `sorry` cannot be discharged. Fixing it
    means giving the class the hypotheses the derivation needs (bean qou-octr,
    criterion §10 `proof-unclosable-context-sorry`). This refutation is the
    evidence, not the fix. -/
theorem skein_mass_from_linking_unconstrained_false :
    ¬ ∀ ctx : SkeinMassFromLinkingContext,
        ctx.mass = ctx.Q * ctx.mass_Hopf +
          (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) := by
  intro h
  have := h { q := 1, Q := 0, mass_Hopf := 0, n := 0, Vol_K := fun _ => 0,
              hbar_q := 1 - (1 : ℝ)⁻¹, hbar_q_def := rfl, mass := 1 }
  norm_num at this

end QOU.BraidsKnots
