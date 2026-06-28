# The ED / Hopf / gauge-SU(2) embedding: right door for the volume S³, wrong door for W_λ (Schur–Weyl dual)

**Date:** 2026-06-28
**Branch:** `claude/q-askey-scheme-gaps-wubsmv`
**Status:** Scope/assessment audit — affirms a correct geometric identification, re-confirms an existing (b) structural exclusion, and proposes a non-excluded redirect. No fit; no closure.
**Keystone bean:** `s5bb` (s5-so3); ledger [`docs/coordination/s5-so3-keystone.md`](../coordination/s5-so3-keystone.md).

## The question

Working intuition (owner, 2026-06-28): *where is the hyperbolic knot volume
actually computed? Bring's surface has the exceptional divisor (ED) where all
the action takes place, so the embedding into S³ runs through the ED — and if
the knot operators live in the gauge group, maybe there is an embedding there
that yields W_λ.*

The intuition has two separable parts. **Part (i)** — the ambient volume-S³ is
reached through the ED and is the gauge SU(2) — is **correct and useful**.
**Part (ii)** — that this embedding *yields* W_λ — is the **already-excluded
SU(2) sub-route**. Keeping them apart is the whole content of this note.

## Part (i) — correct: the ambient volume-S³ = Hopf-over-ED = gauge SU(2)

Where the hyperbolic volume lives. The framework's hyperbolic volume is
`Vol(S³ ∖ K)` of a knot complement, recovered from the **colored** Markov
trace / colored Jones via the Kashaev volume conjecture
([`mass-theory/kashaev-volume-density.md`](../../content/quantum-observable-universe/mass-theory/kashaev-volume-density.md)):
`Vol(K) = 2π·limₙ log|Jₙ(K; e^{2πi/N})|/N`. The colored Jones is built from the
**Rep(SU_q(2))** R-matrix — the `V_λ` (quantum-group / gauge) side.

Where the ambient S³ comes from. [`brings-surface/embeddability-closure.md`](../../content/quantum-observable-universe/brings-surface/embeddability-closure.md)
puts the link in *"the total space `S³ → 𝒮_c`"* with `𝒮_c ≅ S²` the exceptional
divisor (the base `ℙ(V) ≅ ℂP¹`). That fibration `S³ → S²` is the **Hopf
fibration**, which is exactly the coset projection
`SU(2) → SU(2)/U(1) = ℂP¹`. So the ambient three-sphere is presented as the
Hopf bundle of `SU(2)` over its flag variety `ℂP¹ = SU(2)/T` — i.e. **the
ambient volume-S³ is the gauge-group SU(2) itself, fibered over the ED.**

This vindicates Part (i): in QOU the "ambient S³" is *not* an arbitrary base
manifold whose coincidence `SU(2) ≅ S³` is irrelevant (the generic Chern–Simons
caveat). Here the ambient S³ is *built from* the gauge data — it is the Hopf
total space of `SU(2)` over the ED. The knots embed in the genus-4 Bring **fiber**
`Σ₄` (Seifert-genus filter `g ≤ 4`) and sit in this ambient `SU(2) = S³`. This
also sharpens the companion remark
[`rem:markov-trace-ambient-s3`](../../content/quantum-observable-universe/braids-and-knots/markov-trace-ambient-s3.md):
the Alexander–Markov ambient S³ is concretely the Hopf-over-ED gauge SU(2).

## Part (ii) — excluded: the gauge side does NOT yield W_λ

The hope "knot operators in the gauge group ⇒ an embedding yielding W_λ" is the
**SU(2) sub-route to W_λ**, and the keystone has run it and **structurally
excluded it** ((b), with a cited invariant — not a scope-limited negative):

- **#2717 (2026-06-24), Step-1 gate** ([`2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md`](2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md)):
  SU(2)/WRT(S³/2I) does **not** reproduce W_λ. Two grounds:
  - **Coverage.** All ≥3-row blocks — *including the electron `(3,1,1)`* — lie
    outside the GL₂ Schur–Weyl image, so they carry **no SU(2) weight at all**.
  - **Value.** `d_q(λ) = [2j+1]_q` only on the standard rep `(n−1,1)` (∀n).
- **Schur–Weyl capstone** ([`2026-06-22-keystone-schurweyl-dual-sides.md`](2026-06-22-keystone-schurweyl-dual-sides.md)):
  the exact two-sided table. `W_λ = d_q(λ)²/[n]_q!` is the **Hecke / S_n-side**
  hook-content; the WRT/gauge weight is the **SU(2) / V_λ-side** `[2j+1]_q`.
  They differ off the accidental `(4,1)`: the muon block `(3,2)` has Hecke
  `d_q = [5]_q ≈ 5.22` but SU(2) `[2]_q ≈ 2.01`.

**The invariant that forbids Part (ii):** Schur–Weyl duality
`(ℂ²)^{⊗n} = ⊕_{λ: ≤2 row} S^λ ⊗ V_λ`. The gauge/`V_λ` side (where the knot
operators and the volume live) is the **dual** of the Hecke/`S^λ` side (where
`W_λ` lives), and the duality is not an equality of weights. A gauge-group
embedding therefore delivers the `V_λ`-side modular data, never the `S^λ`-side
`W_λ` — and it cannot even *see* the ≥3-row blocks (electron included). This is
the same KL-positivity-flavoured lesson as the Δ_λ PROBE-4 prune: a structure on
the wrong side of a representation-theoretic duality supplies at most a
coincidental sub-family, never the whole target.

## Part (iii) — the non-excluded redirect: the ED motivates *why* S³/2I and (2,3,5)

The ED observation is not wasted; it lands on the **geometry/base**, which is
exactly where the keystone's open object lives — and on the `V_λ`/volume side,
consistent with (i).

The ED is `𝒮_c ≅ S² = ℂP¹ = SU(2)/T`. Bring's surface carries the icosahedral
symmetry (`Aut(Bring) = S₅ ⊃ A₅`; [`brings-surface/brings-curve.md`](../../content/quantum-observable-universe/brings-surface/brings-curve.md)),
and the icosahedral rotation group `A₅` acts on `ℂP¹` (the Riemann sphere) with
the classical orbits of stabiliser orders `{5, 3, 2}` (12 vertices, 20 faces,
30 edges) — i.e. the orbifold quotient is `S²(2,3,5)`. The keystone's Seifert
fibration is precisely `S³/2I → S²(2,3,5)` (Reeb = Seifert `S¹`), with `2I` the
binary cover of that same `A₅`.

**Proposed identification (a lead, not a closure):** the brings-surface ED —
"where all the action takes place" — *is* the `S²(2,3,5)` orbifold base of the
keystone's `S³/2I` Seifert fibration, with the icosahedral `A₅` action on
`ℂP¹ = ED` supplying the `(2,3,5)` cone structure. Under this reading:

- the ambient volume-S³ = Hopf-over-ED = gauge `SU(2)` (Part i);
- its `2I`-quotient is the Poincaré sphere `S³/2I`, whose RT/Verlinde **vacuum
  Plancherel** measure `d_q²/D²` is the keystone's `W_λ` candidate
  ([`2026-06-20-keystone-wlambda-beasley-witten-localization.md`](2026-06-20-keystone-wlambda-beasley-witten-localization.md));
- the `(2,3,5)` cone data is *forced* by Bring's icosahedral `A₅`, not chosen.

This **geometrically motivates the keystone arena** (why `S³/2I`, why `(2,3,5)`)
from the brings-surface ED, on the `V_λ`/volume side — and the bridge back to the
`S^λ`-side `W_λ` is the Schur–Weyl duality of Part (ii), *not* a direct gauge
embedding. What remains to confirm (the lead): that the QOU ED literally carries
the icosahedral `A₅` action with the `(2,3,5)` orbit structure (the math is
standard; the QOU wiring `ED ↔ S²(2,3,5)` is the open step). Per the keystone
discipline this is **not** a new fit and changes none of the falsifiable
content: the defect cubic `144·C(n) = −n(n−1)(2n−13)` (Lean-proved sorry-free)
and Identity I `M(n) = n(3n−1)/2` (proved `n ≤ 12`) remain the gates.

## Net

| Part | Claim | Verdict |
|---|---|---|
| (i) | ambient volume-S³ = Hopf-over-ED = gauge SU(2) | **correct** — the volume lives on the `V_λ`/colored-Jones side; sharpens `rem:markov-trace-ambient-s3` |
| (ii) | gauge-group embedding *yields* W_λ | **excluded** (b) — #2717 coverage+value; W_λ is Hecke/`S^λ`-side, dual to the gauge `V_λ` side; electron `(3,1,1)` carries no SU(2) weight |
| (iii) | ED = `S²(2,3,5)` Seifert base; motivates `S³/2I` arena from Bring's `A₅` | **lead** (not closure) — non-excluded, on the `V_λ`/geometry side; Schur–Weyl is the bridge to the `W_λ` Hecke side |

The gauge embedding is the right door for the **volume / ambient-S³** story and
for *motivating the keystone arena*, and the wrong door for **W_λ** itself. The
productive next step is the ED ↔ `S²(2,3,5)` identification (Part iii), not a
re-run of the pruned SU(2)-weight route (Part ii).
