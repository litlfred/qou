# α_EM bean B5 — the assembly: the conditional per-loop theorem (2026-07-18)

**Bean:** `qou-61lh` (B5) of the τ-correspondence proof plan (milestone
`qou-b5qg`) — the final brick. Upstream, all merged: B1
([#3955](https://github.com/litlfred/qou/pull/3955)), B2 shadow
([#3960](https://github.com/litlfred/qou/pull/3960)), B3
([#3969](https://github.com/litlfred/qou/pull/3969)), B4a
([#3973](https://github.com/litlfred/qou/pull/3973)), B4b
([#3977](https://github.com/litlfred/qou/pull/3977)).

**Probe:** [`computations/alpha_em/alpha_em_b5_assembly_probe.py`](../../computations/alpha_em/alpha_em_b5_assembly_probe.py)
→ [`alpha-em-b5-assembly.witness.json`](../../computations/alpha_em/alpha-em-b5-assembly.witness.json)
— 4/4 assertions PASS.

**Lean (this PR):** [`QOU/Archimedean/PerLoopMeasureShadowAssembly.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PerLoopMeasureShadowAssembly.lean)
— sorry-free, `lean`-direct exit 0 (core-only; imports the merged
`SigmaJGeometricCarrier` + `TauRhoHodgeShadow`).

**Scope guard (STRICT):** the theorem is **conditional**; nothing derived
unconditionally; no fit; nothing wired; `1/(8π)` stays phase-4 (owner ruling
`dd55a5748`).

## The conditional theorem

> **Theorem (conditional on the B2 functorial lift).** If the categorical
> τ-functor carries the fibre reality structure `ρ: q ↦ q̄` to the Hodge
> conjugation of `H¹(Bring)`, with one loop's mode space landing on the
> conjugate pair `H^{1,0} ⊕ H^{0,1}`, then the per-loop measure of the
> α_EM tower is
>
> $$\text{measure} \;=\; \tfrac{1}{2}\,a_0 \;=\; \tfrac{1}{2}\cdot\tfrac{1}{4\pi} \;=\; \tfrac{1}{8\pi} \;=\; \tfrac{|\chi|}{4\cdot\mathrm{Area}},$$
>
> with every factor derived **under the hypothesis**.

Factor provenance:

| Factor | Derivation route | Brick |
|---|---|---|
| channel count 2 | Hecke relation is quadratic — two idempotent channels `e₊/e₋` | clauseB F1, #3921 |
| `a₀ = 1/(4π)` | J ⟹ conformal class ⟹ Laplacian ⟹ universal heat unit (universality machine-verified) | B3, #3969 |
| `½` | forced by reality: antilinear intertwiner + real spectrum split every spectral trace equally across the conjugate pair; the FORCED shadow assignment `q=i↦H^{1,0}` picks the channel | B4b #3977 + B2s #3960 |
| `[2]_q` restoration | the tower's one-loop coefficient is −[2]_q·x exactly, with `[2]_q` = the KL eigenvalue of `b_s` on `e₊`; `[2]_1 = 2` = the pair count, so the q→1 one-loop total is `a₀·α` — B4's target | B4a, #3973 |
| geometrized form | `|χ|/(4·Area) = 1/(8π)` genus-independent (Lean, main) | GB identity |

## The Lean shadow assembly

`PerLoopMeasureShadowAssembly.lean` proves the shadow level sorry-free in
Lean core:

- `rho_forced_equal_split` / `channel_share_is_half` — any ρ-symmetric weight
  splits equally over the degenerate pair; the selected channel carries
  exactly half the doubled total.
- `kl_eigenvalue_at_one_eq_pairCount` — `[2]_1 = 2` = the conjugate-pair
  count.
- `pairCount_ne_bettiOneBring` — 2 ≠ b₁ = 8: the `1/(π·b₁) = 1/(8π)`
  coincidence stays a *different* decomposition (the "three readings of the
  2" disambiguation, machine-locked).
- `shadow_assembly` — the composed theorem: any assignment satisfying the B1
  dictionary agrees with the FORCED `hodgeShadow` (#3960 `shadow_unique`),
  and `klEigenvalueAtOne · w(i) = w(i) + w(−i)` for any ρ-symmetric weight.

**Honesty invariant (machine-checked by the probe):** the B2 lift enters the
Lean *only* as explicit hypotheses — no `axiom`, no `sorry`, no fabricated
class instance. Per AGENTS.md §"Axiomatization is NOT a Proof", the
conditional theorem does not close the conjecture.

## Where the program now stands

```
τ-correspondence proof plan qou-b5qg — COMPLETE AT SHADOW LEVEL
  B1  ρ reality structure          MERGED #3955
  B2  shadow FORCED                MERGED #3960   |  LIFT OPEN (qou-tq20, Mathlib-gated)
  B3  conformal inheritance        MERGED #3969
  B4a classical ½ origin (KL)      MERGED #3973
  B4b ρ-forced split (junction)    MERGED #3977
  B5  assembly                     THIS PR
```

**The α_EM per-loop wall is now exactly one open statement:** the B2
functorial lift. Its shadow is proved forced and obstruction-free
(`shadow_unique`, the #3942 geometric carrier, the type-consistent B1
dictionary); what remains is the categorical statement that τ itself
implements the dictionary — requiring category-theoretic apparatus
(Mathlib-gated in sandboxes; see `lean-environment-setup`).

Closing the lift would promote the conditional theorem to a derivation of
the per-loop measure `1/(8π)` and lift the phase-4 identification — subject
to owner review; nothing in this plan wires it.
