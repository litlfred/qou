# GAP-A-4 final retrospective — Path B per-atom λ(K) closure converges with #1871's step-9 binding on the τ-image Dirac/SW PDE

**Date:** 2026-06-05
**Audit type:** consolidating retrospective; durable record of the GAP-A-4 axis closure
**Status:** **GAP-A-4 axis closed across all probe layers.** The single productive remaining direction (τ-image Dirac/SW PDE identification) converges with the sibling axis [PR #1871's step-9 binding workplan](../coordination/2026-06-05-step9-binding-closure.md) §4.A L3 — reducing the framework's open derivation math to one categorical conjecture (`conj:s5-so3-fiber-action`).
**Owners:** the full T1+T2+T3 chain shipped today; see PR table below.

---

## §1. What this session set out to do

The 1ppQ roadmap's Path B formula `m(K) = m_e · Vol(K)/ℏ_q² · λ(K) + S(K)` was the framework's open per-atom mass-multiplier question. After 14 prior no-fit closures on the Δ_λ side closed the per-partition decomposition, the productive direction shifted to deriving `λ(K)` directly. GAP-A-4 took that question.

The [Δ_λ Phase-4 audit (2026-05-19)](./2026-05-19-delta-lambda-phase4-z4N-closure.md) had already substrate-derived the per-atom binding-energy amplitude `A(K)` to ≤ 2.5 %, so the question wasn't "can we derive *anything* per-atom?" but "can we derive `λ(K)` specifically — the *mass* multiplier, not the binding amplitude?"

## §2. The four structural transplant routes — all REFUTED

Four plausible routes for `λ(K)` were tested across the session. Each treated `λ(K)` as a *transplant* of a quantity living at a different layer of the framework. All four closed NEGATIVE:

| Route | Hypothesis | Verdict | PR |
|---|---|---|---|
| **R1** Phase-4 carrier transplant | `λ(K) = f(A_Phase-4(K))` for some rational form | L1a/b/c REFUTED across light series (worst-rel −56 % to +106 358 %) | [#1874](https://github.com/litlfred/qou/pull/1874) |
| **R2** Vol(K) convention choice | `λ_emp(K)` becomes near-constant under the "right" Vol(K) | T2 REFUTED for all 3 conventions (best swing +132 %) | [#1891](https://github.com/litlfred/qou/pull/1891) |
| **R3** Additive `S(K)` sub-leading under uniform-λ | `S(K)` factors cleanly while `λ = 2.53` is held fixed | T1 REFUTED (100× S/m_e swing) | [#1886](https://github.com/litlfred/qou/pull/1886) |
| **R4** Bar-symmetric q-Pochhammer combinations | `λ(K)` = mass-side q-difference solution at depth 3·A | T3 REFUTED (worst −98 % at P3 Markov-trace ratio) | [#1897](https://github.com/litlfred/qou/pull/1897) |

(R4 was a sharper variant of R1, restricted by the formalize-first invariants I1 bar-symmetry + I2 proton-anchor before the data probe ran.)

## §3. Why all four refute structurally — the shared diagnosis

Each route treats `λ(K)` as a transplant from a layer that *was never derived to be a per-atom mass multiplier*:

| Layer | What it derives | Why it fails as λ(K) |
|---|---|---|
| Phase-4 amplitude `A(K)` | per-atom **binding-energy** amplitude (≤ 2.5 %) | wrong observable — λ(K) is the mass multiplier, not B(K) amplitude |
| Per-knot `Vol_hyp(K)` | hyperbolic volume of the atomic-braid-closure JSJ piece | only one factor of the mass; doesn't carry the per-(Z, N) structure |
| Uniform `linking_weight ≈ 2.53` | H₄ Family-A categorical count, A-independent | doesn't vary with A; T1 showed S(K) must absorb the variation, but with 100× swing |
| Bar-symmetric q-Pochhammer at depth 3·A | factorial-growth combinatorial weights | grows explosively (10⁹× off at ⁴He); wrong scaling regime |

The framework's existing layers all derive *something* per-atom — but none of them derive a *mass multiplier* per-atom. **`λ(K)` requires a Path-B-native derivation that the existing layers cannot transplant in.**

## §4. The axis convergence — same productive direction on two sides

Independently of GAP-A-4, [PR #1871's step-9 binding closure workplan](../coordination/2026-06-05-step9-binding-closure.md) (the *additive many-body binding series*, sibling axis) reached the same productive direction from the opposite side of the Path B identity:

```
m(K)  =  m_e · Vol(K)/ℏ_q² · λ(K)   +   S(K)          ← Path B
         └────────────────────┘       └──┘
              GAP-A-4 axis           step-9 binding axis
            (mass multiplier)         (additive many-body)
```

Both axes converge on the **τ-image Dirac/SW PDE identification**:

- **GAP-A-4 / T3 §7** (the just-merged scope): *"if the I1+I2-restricted Pochhammer space is empty, conclusion is τ-image Dirac/SW PDE identification — same direction #1871's workplan §4.A L3 names as load-bearing"*. T3's probe confirmed the space is empty.
- **#1871's workplan §4.A P4 + L3**: *"the binding generating function `G(x;q) = Σ B_n x^n` satisfies a fibre-level q-difference equation; under τ at real q₀ it becomes the Dirac/SW PDE, fixing both the per-order terms and the scale rule ρ·A"*.

The mass-side and binding-side closure **converge on a single categorical conjecture**: that the q-difference structure of `R_mass(q, x)` and `R_bind(q, x)` is the **τ-image of a Dirac/SW PDE on the brane manifold**, identifiable via `conj:s5-so3-fiber-action` (the S₅ ↔ SO(3) fibre action; the q-deformation enters via the Hecke embedding S₅ ↪ H₅(q) per AGENTS.md §7a Hecke-Skein convention, so the canonical `Σ_λ y_λ χ^λ` Wedderburn data at q₀ is over H_n(q) blocks even though the underlying S₅ symmetry is what the conjecture name records). The conjecture identifier `conj:s5-so3-fiber-action` is the canonical label this PR cites; spelled `fiber` (US) in the corpus identifier and `fibre` (UK) in prose for consistency with the rest of the audit chain.

## §5. Net for the framework's open math after this session

**Before this session** (the prior 14 no-fit closures + Phase-4):
- Δ_λ per-partition decomposition: closed (14 ansätze refuted)
- per-atom binding amplitude `A(K)`: closed (Phase-4 substrate-derived ≤ 2.5 %)
- per-atom mass multiplier `λ(K)`: open
- additive many-body binding series: open
- per-knot `Vol(K)` convention: open
- τ-image Dirac/SW PDE: open / gated on `conj:s5-so3-fiber-action`

**After this session** (T1+T2+T3 + #1871's workplan):
- per-atom mass multiplier `λ(K)`: closed across all transplant routes ✅
- additive many-body binding series: framed via SW-residue + q-difference ✅ (#1871)
- per-knot `Vol(K)` convention: closed **NEGATIVELY** as a standalone fix ✅ (T2 — no convention resolves λ(K) alone, smallest residual swing was still +132 %)
- τ-image Dirac/SW PDE: **the single productive remaining direction**, with two axes both pointing at it

**The framework's open derivation math is now reduced to one categorical conjecture.** That's the cleanest possible localization the available probe layers can achieve.

## §6. Session PR chain (chronological)

| # | PR | Outcome | Layer |
|---|---|---|---|
| 1 | [#1816](https://github.com/litlfred/qou/pull/1816) | merged | Option A diagnostic |
| 2 | [#1841](https://github.com/litlfred/qou/pull/1841) | merged | Bratteli induction REFUTED |
| 3 | [#1850](https://github.com/litlfred/qou/pull/1850) | merged | Markov stabilization REFUTED |
| 4 | [#1853](https://github.com/litlfred/qou/pull/1853) | merged | H₃→H₄ axes-refuted consolidation |
| 5 | [#1860](https://github.com/litlfred/qou/pull/1860) | merged | Kashiwara Δ_λ REFUTED (5/5) |
| 6 | [#1822](https://github.com/litlfred/qou/pull/1822) | merged | qbeta rung-lifts (sibling axis) |
| 7 | [#1864](https://github.com/litlfred/qou/pull/1864) | merged | 3-paths-refuted roadmap |
| 8 | [#1868](https://github.com/litlfred/qou/pull/1868) | merged | GAP-A-3 scope |
| 9 | [#1870](https://github.com/litlfred/qou/pull/1870) | merged | GAP-A-3 deuteron P_λ REFUTED |
| 10 | [#1872](https://github.com/litlfred/qou/pull/1872) | merged | GAP-A-4 Path B scope |
| 11 | [#1874](https://github.com/litlfred/qou/pull/1874) | merged | L1 light-series REFUTED (R1) |
| 12 | [#1876](https://github.com/litlfred/qou/pull/1876) | merged | L1 retrospective (4 directions) |
| 13 | [#1881](https://github.com/litlfred/qou/pull/1881) | merged | typo fix |
| 14 | [#1882](https://github.com/litlfred/qou/pull/1882) | merged | ³He residual (NUMEROLOGY) |
| 15 | [#1883](https://github.com/litlfred/qou/pull/1883) | merged | cross-isotope (numerology confirmed) |
| 16 | [#1886](https://github.com/litlfred/qou/pull/1886) | merged | **T1 additive S(K) REFUTED (R3)** |
| 17 | [#1888](https://github.com/litlfred/qou/pull/1888) | merged | cross-axis ledger link to #1871 |
| 18 | [#1891](https://github.com/litlfred/qou/pull/1891) | merged | **T2 per-knot Vol(K) REFUTED (R2)** |
| 19 | [#1894](https://github.com/litlfred/qou/pull/1894) | merged | T3 scope |
| 20 | [#1897](https://github.com/litlfred/qou/pull/1897) | merged | **T3 q-Pochhammer REFUTED (R4)** |
| 21 | this PR | open | final retrospective |

**Total closures**: 18 no-fit ansätze + 4 GAP-A-4 transplant routes = 22 across this session arc. Per-atom mass multiplier `λ(K)` axis closed; sibling axis converges on the same categorical conjecture.

## §7. The recommended framing for downstream content

After this session, the recommended scholarly framing is:

> *"The per-atom mass multiplier `λ(K)` of Path B is not derivable from any layer that exists at or below the Habiro-Pochhammer / q-difference / Markov-trace strata. The mass-side and binding-side closure of Path B both reduce to a single categorical conjecture: the τ-image identification of the substrate's q-difference kernel with a Dirac/SW PDE on the brane manifold, gated on the `conj:s5-so3-fiber-action`."*

This is the language `linking_weight_family_a` and related production constants should be described with going forward (per the [#1864 §5 framing recommendation](./2026-06-04-three-paths-refuted-roadmap-update.md) extended with the new τ-image identification).

## §8. Cross-references

- [`gap-a-path-b-lambda.md`](../coordination/gap-a-path-b-lambda.md) — GAP-A coordination ledger (T1/T2/T3 marked closed)
- [`2026-06-05-step9-binding-closure.md`](../coordination/2026-06-05-step9-binding-closure.md) — #1871's sibling-axis ledger
- [`2026-06-05-delta-lambda-sw-residue-qdifference-attack.md`](../workplans/2026-06-05-delta-lambda-sw-residue-qdifference-attack.md) — #1871's full workplan (§4.A L3 = the convergent τ-image direction)
- [`2026-06-04-three-paths-refuted-roadmap-update.md`](./2026-06-04-three-paths-refuted-roadmap-update.md) — earlier 3-paths-refuted consolidation; this retrospective extends it with T1+T2+T3
- [`2026-06-04-gap-a4-L1-retrospective.md`](./2026-06-04-gap-a4-L1-retrospective.md) — earlier L1 retrospective; the four §4 directions it identified now all closed (T1, T2, T3 negative; the implicit direction toward #1871's binding workplan converges)
- [`2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md`](./2026-06-05-gap-a4-T3-path-b-lambda-formulation-scope.md) — T3 scope (§7 honest-outcome alternative IS the conclusion of this retrospective)
- [`2026-05-19-delta-lambda-phase4-z4N-closure.md`](./2026-05-19-delta-lambda-phase4-z4N-closure.md) — Phase-4 amplitude (the existing positive substrate-derivation result)
- [`2026-05-18-delta-lambda-gating-context.md`](./2026-05-18-delta-lambda-gating-context.md) — original Δ_λ gate doc (the framework's prior derivation-gap framing this session closes for the mass-multiplier side)
