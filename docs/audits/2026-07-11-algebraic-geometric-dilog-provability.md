# Can `conj:algebraic-geometric-dilog-equivalence` be proved? Honest assessment

**Date:** 2026-07-11 · **Branch:** `claude/faddeev-phi-b-construction-e26myp` ·
**Tier:** provability triage (scope-(a)). **Anti-laundering rule respected: a
class instance is NOT a proof.**

The c₃ bar-odd `S` derivation converged (this session, every route) on a single
open link: the map `q₀ → m` (substrate → figure-eight meridian holonomy) =
`conj:algebraic-geometric-dilog-equivalence`. This doc records what of that
conjecture is provable and what is not.

## Verdict: the full conjecture is NOT provable (and must not be laundered)

Per its own [`.md`](../../content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.md),
the conjecture is **downstream of `conj:kashaev-volume-conjecture`** (the
Kashaev–Murakami–Murakami **volume conjecture**) and
`conj:dilogarithm-archimedean-limit`. The volume conjecture is one of the
central **open** problems of quantum topology — proven only for specific knots,
open in general. By AGENTS.md §3b (conjectural propagation) and the
"Axiomatization is NOT a Proof" rule, this block **cannot** be promoted to a
theorem, and the existing conditional class
`AlgebraicGeometricEquivalence` (consuming `[ArchimedeanLimit]` +
`[Kashaev.VolumeConjecture]`) is the **honest** representation — a rigorous
*conditional*, not a proof.

## What IS a theorem (proved this session, sorry-free)

The conjecture's **§1 algebraic pole side** is unconditional. New file
[`QOU/QBeta/QPochhammerPoles.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QPochhammerPoles.lean)
proves, over a generic `[Field K]` (no `ℝ`, §7c):

- `qPochDenom_eq_zero_at_pole` — the partial denominator
  `(x;q)_n = ∏_{k<n}(1 − x qᵏ)` **vanishes exactly at each pole `x = q^{-j}`,
  `j < n`**;
- `qPochDenom_poles` — the explicit root function `k ↦ q^{-k}` together with the
  proof that each is a genuine root.

This **strengthens** the conjecture class, whose current `pole_cusp_bijection`
field asserts only `∃ z, z k = q^{-k}` — vacuously true (it names the candidates
but never asserts they are zeros). The vanishing is now a theorem; only the
**cusp correspondence** (that these poles match ideal-tetrahedron cusps) remains
geometric/conjectural.

## What stays conjectural (the volume conjecture)

- **§1 pole→cusp bijection** (geometric): that the algebraic poles correspond to
  the hyperbolic triangulation's cusps. Conjectural (`conj:shared-denominator-cusp-holonomy`).
- **§2 asymptotic Bloch–Wigner**: `τ_arch(Φ_n(x;q₀)) → D(z(x)) = Vol_hyp`. This
  **is** the volume conjecture. Open in general; **known for the figure-eight**
  (Andersen–Hansen 2006; Ohtsuki's asymptotic expansion), which is exactly the
  `S = Im 𝔙` case — so for 4₁ the asymptotic half is a *literature theorem*, and
  the QOU-native reduction to it (not a fresh proof of the volume conjecture) is
  the tractable remaining task.

## Does the conjecture *follow* from Kashaev? (corpus check — NO Lean implication)

Asked directly: is `conj:algebraic-geometric-dilog-equivalence` a conditional
theorem `[VolumeConjecture] [ArchimedeanLimit] ⟹ (conj)`, with a Lean proof?
**Corpus answer: no such implication is proved, and it is not straightforwardly
provable.** Findings:

- **The three classes are unwired.**
  [`AlgebraicGeometricEquivalence`](../../content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.lean)
  is a *standalone* class — it does **not** take `[VolumeConjecture]` or
  `[ArchimedeanLimit]` as instance hypotheses and derive its fields. The `.md`'s
  "downstream theorems verify modulo those two instances" is aspirational, not
  realized in Lean.
- **They target different limits.** `ArchimedeanLimit` asserts
  `(1−q)·log Φ_n → LiTwo (= Li₂)`; the alg-geom class asserts convergence to
  `BlochWignerD (= D = Vol_hyp)`. `D(z)=Im Li₂(z)+arg(1−z)log|z|` is a *different*
  real functional under a *different* (Faddeev, complex) rescaling — so the
  alg-geom asymptotic is **not** a direct corollary of `ArchimedeanLimit`.
- **The Kashaev conditional theorems are vacuous stubs.**
  [`figure_eight_volume_from_vc`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-conjecture.lean)
  and `borromean_volume_from_vc` conclude `: True := trivial` (and `pieceVolume`
  is `sorry`). So VC does not, in the current Lean, actually yield `Vol(4₁)`.
- **The bridge is itself conjectural.** Even morally, the reduction of the
  QOU partial-product form to Kashaev passes through
  `conj:shared-denominator-cusp-holonomy` (pole↔cusp), which is open.

So there is **no Lean proof of the implication**, and writing one would require
the conjectural bridge — i.e. it would launder an open conjecture. Honest status:
the conjecture is *morally* downstream of the volume conjecture but the Lean
wiring does not exist and cannot be manufactured without proving the bridge. What
*is* provable is the algebraic pole half (above) — which this session did.

## Consequence for c₃ bar-odd S

`S = Im 𝔙` (`conj:binding-qbeta-complex-volume`) is **one geometric conjecture
away** — and that conjecture is *settled for the figure-eight in the
literature*. So the honest status is: the c₃ bar-odd `S` is **conditionally
closed for 4₁** modulo matching the QOU partial-product `τ_arch` to the
Andersen–Hansen asymptotic — a formalization/reduction task, **not** a
proof of the open general volume conjecture, and **not** a numerical fit.

## Cross-references
- Conjecture: [`algebraic-geometric-dilog-equivalence.md`](../../content/quantum-observable-universe/mass-theory/algebraic-geometric-dilog-equivalence.md)
- Gluing Newton solve: [`qbeta_c3_barodd_gluing_newton_solve.py`](../../computations/qbeta/qbeta_c3_barodd_gluing_newton_solve.py)
- Session gap doc: [`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`](2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md)
- AGENTS.md §"Axiomatization is NOT a Proof"; §3b; §"Before declaring open".
