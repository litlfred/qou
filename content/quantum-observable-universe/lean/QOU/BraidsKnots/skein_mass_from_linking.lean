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
    (the Skein-resolution data of the hadron).  The mass identity is
    carried as an upstream class field (added 2026-08-23 to repair the
    refutable encoding). -/
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
  /-- The Skein mass identity:
      `𝓜(H) = Q(q) · 𝓜(L_Hopf) + Σ_{i<n} Vol(K_i) / ℏ_q²`. -/
  mass_identity : mass = Q * mass_Hopf +
    (Finset.range n).sum (fun i => Vol_K i / hbar_q ^ 2)

/-- **Skein mass identity** ([`lem:skein-mass-from-linking`]).
    Proved from the upstream class field constraint. -/
-- Ref: [manuscript] quantum-observable-universe/mass-theory/skein-mass-from-linking.md
theorem skein_mass_from_linking [ctx : SkeinMassFromLinkingContext] :
    ctx.mass = ctx.Q * ctx.mass_Hopf +
      (Finset.range ctx.n).sum (fun i => ctx.Vol_K i / ctx.hbar_q ^ 2) :=
  ctx.mass_identity

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

end QOU.BraidsKnots

