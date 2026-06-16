# Duality tracker — coord doc

**Date:** 2026-05-24
**Goal:** single source of truth for **every duality the QOU framework uses or could use**, with explicit status (✅ formalised / ⏳ partial / ⚪ literature-only / ❌ not in framework), the load-bearing content block (if any), and the open closure path.

**Why this exists:** PR [#1111](https://github.com/litlfred/qou/pull/1111)'s gap analysis surfaced ≥ 13 distinct duality structures relevant to the framework, of which only the **bar involution** `q ↔ q⁻¹` is exhaustively classified ([`bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md) + tables 1-4). Several other dualities have existing content blocks but no central index; the rest are flagged in audits as candidate closure paths but not formalised. This tracker is the index.

**See also**:
- [`docs/canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) — the chain
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](audits/2026-05-23-lambda-scale-canonical-unification.md) §"13-driver menu" — the categorical-mechanism catalogue
- [`content/quantum-observable-universe/braids-and-knots/bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md) — the canonical bar-classifier

## §1. Duality classification table

Status legend:
- ✅ formalised in framework with `prop:` or `def:` block
- ⏳ partial — block exists but scope-restricted; canonical extension open
- ⚪ literature-pointer only — no QOU block
- ❌ not in framework, not yet flagged as gap

Symmetry kind:
- **Anti-involution** — `α² = id` reversing some product structure
- **Functor duality** — contravariant functor establishing an equivalence
- **Symmetry** — group action preserving structure
- **Limit duality** — same object viewed in two limits (`q → 0` ↔ `q → ∞`, etc.)
- **Combinatorial** — refinement / decategorification

| # | Duality | Quantum / categorical side | Classical / dual side | Status | Load-bearing block | Closure path |
|---|---------|---------------------------|----------------------|--------|--------------------|--------------|
| **D1** | **Bar involution** `q ↔ q⁻¹` | Hecke generator inversion `σᵢ ↔ σᵢ⁻¹`; mirror crossing | classical / "real" projection of Hecke algebra | ✅ formalised, exhaustive | [`bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md) + Tables 1-4 | (closed) |
| **D2** | **Hermitian \*** | over ℂ, conjugate `q` with Im(q) ≠ 0 | identical to D1 **only** when Im(q) = 0 | ⏳ probing | PR [#1127](https://github.com/litlfred/qou/pull/1127) `q-zero-reality-audit.md` + new content blocks `prop:q-zero-complex-extension` (Hecke quadratic / bar / Frobenius polymorphic over R = ℂ with `|q|>1`) + `prop:lusztig-vs-hermitian-bar` (the categorical home for Im(q_0) contribution) | merge PR #1127; verify Lusztig-bar = Hermitian-* coincide iff q ∈ ℝ; structurally admissible but not the dominant 2.89% gap mechanism |
| **D3** | **Categorical self-duality** (Frobenius) | `A ⤳ ω_A^•` rigid dualizing complex; `⟨a, b⟩_F = λ(μ(a⊗b))` | observer = observed (substrate self-paired) | ✅ formalised | [`substrate-self-duality.md`](../content/quantum-observable-universe/quantum-observable-universes/substrate-self-duality.md), [`categorical-self-duality.md`](../content/quantum-observable-universe/quantum-observable-universes/categorical-self-duality.md) | (closed) |
| **D4** | **Higgs boson / Higgs field** | H boson = 1-component knot (radial mode) | Goldstone field = absorbed into W/Z longitudinal polarisation | ⏳ scaffold | [`categorical-higgs-mechanism.md`](../content/quantum-observable-universe/braids-and-knots/categorical-higgs-mechanism.md) — W± → T(2,4), Z → T(2,6), H singlet. Lean scaffolds: [`CategoricalHiggsIdempotent`](../content/quantum-observable-universe/lean/QOU/QuantumObservableUniverses/CategoricalHiggsIdempotent.lean) (PR [#1137](https://github.com/litlfred/qou/pull/1137), `m_W/m_Z = cos θ_W` PROVED via `field_simp; ring`), [`SubstrateEWHypotheses.lean`](../content/quantum-observable-universe/lean/QOU/BraidKnot/SubstrateEWHypotheses.lean) (PR #1143, 3 hypothesis scaffolds: `g = π·h_0` +0.26%, `v_framework/v_SM = log 6` −0.50%, `171/143 = 6/5` +0.35%; cardinality anchors `\|S_3\| = 6` + `partitionsOfFour = 5` PROVED rfl) | flesh out the 3 hypothesis sorries (Yekutieli MI / CS partition function / block-counting); promote conditional W/Z = cos θ_W to unconditional via downstream block derivations |
| **D5** | **CPT composite** | bar-involution on orbit closure | parity-mirror + time-reverse + charge-conjugate composite | ✅ formalised | [`cpt-orbit-closure-density.md`](../content/quantum-observable-universe/particle-interactions/cpt-orbit-closure-density.md) | (closed) — but C, P, T **separately** are not (see D6-D8) |
| **D6** | **Charge conjugation (C)** alone | flavor swap u ↔ ū, d ↔ d̄ on color sheets; matter ↔ antimatter | charge sign reversal | ⏳ scaffold | [`conj:c-from-color-flavor-swap`](../content/quantum-observable-universe/braids-and-knots/c-from-color-flavor-swap.md) (PR #1162) — Z/2 flavor-conjugation involution on color sheets; conditional on [`conj:inter-nucleon-channel-color-tube`](../content/quantum-observable-universe/braids-and-knots/inter-nucleon-channel-color-tube.md) (PR [#1111](https://github.com/litlfred/qou/pull/1111)) | author Lean class `CFromColorFlavorSwap` instance; verify C action numerically; promote conjecture → proposition |
| **D7** | **Parity (P)** alone | mirror reflection of braid diagram | left/right chirality | ⏳ scaffold | writhe `w(K)` is classified as bar-anti-symmetric in [`bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md#tbl:bar-involution-table3-data) Table 3; new [`conj:p-from-braid-mirror`](../content/quantum-observable-universe/braids-and-knots/p-from-braid-mirror.md) (PR #1168) — P maps σᵢ ↔ σᵢ⁻¹ with q fixed; bar = P · C · T factorisation | inhabit Lean class `PFromBraidMirror`; prove bar-involution = P·C·T factorisation |
| **D8** | **Time-reversal (T)** alone | braid-word reversal; trace cyclicity | future/past asymmetry | ⏳ scaffold | [`conj:t-from-trace-cyclicity`](../content/quantum-observable-universe/braids-and-knots/t-from-trace-cyclicity.md) (PR #1168) — T = word reversal at Markov-trace level; T-invariance immediate from `thm:jones-markov-trace` cyclicity; bar = P · C · T composes | inhabit Lean class `TFromTraceCyclicity`; numerical witness verifying canonical atomic braids have identical `\|tr_M\|` under word reversal |
| **D9** | **Isospin SU(2)_I** | flavor swap `u ↔ d` between proton/neutron color-sheet flavor triples | nucleon doublet `(p, n)` | ⏳ scaffold + verification + audit-correction | [`crystal-isospin-degeneracy.md`](../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md) (plain-generator restricted, q→0 only) + [`conj:isospin-from-canonical-bowtie`](../content/quantum-observable-universe/braids-and-knots/isospin-from-canonical-bowtie.md) (PR #1162) + [`verify_isospin_bar_anomaly.py`](../computations/verify_isospin_bar_anomaly.py) (this PR — 305 ppm verified at 0.03%) + [`2026-05-24-d9-bar-parity-correction.md`](audits/2026-05-24-d9-bar-parity-correction.md) (this PR — corrects bar-parity attribution: isospin Z/2 ≠ bar involution) | inhabit Lean class `IsospinFromCanonicalBowtie` instance; update audit + conj block per the correction audit |
| **D10** | **Spin SU(2)_S** | SU(2) action on color-sheet rotation | spatial rotation group | ⏳ scaffold | implicit in knot-operator catalogue (S₃ subgroup); full SO(3) gap flagged in [`2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md); new [`conj:spin-from-so3-fiber`](../content/quantum-observable-universe/braids-and-knots/spin-from-so3-fiber.md) (PR #1168) — spin SU(2)_S via S₅ → A₅ ≅ I ⊂ SO(3); ℓ = 2 contributes h⁴ = −3/4 | inhabit Lean class via PR [#1081](https://github.com/litlfred/qou/pull/1081)'s `BringFiberAction`; cross-check ℓ = 2 yields h⁴ = −3/4 |
| **D11** | **Wigner SU(4) = SU(2)_S × SU(2)_I** | combined spin-isospin classical limit | nuclear-physics 4-fold supermultiplets | ⏳ scaffold | [`conj:wigner-su4-from-spin-isospin`](../content/quantum-observable-universe/braids-and-knots/wigner-su4-from-spin-isospin.md) (this PR) — A=4 totally-antisymmetric tensor = SU(4) singlet = magic A·8G closure; α-cluster recursion = product of SU(4)-singlet quadruplets | requires D9 + D10 both ✅ first; verify magic A·8G constant from SU(4)-singlet projection numerically |
| **D12** | **Kashiwara crystal** `q → 0` | KLR canonical basis | combinatorial / decategorification | ⏳ driver in 13-menu | [`crystal-isospin-degeneracy.md`](../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md), CLAUDE.md §7b | full Borromean crystal-graph derivation — no QOU block ties h⁴ to crystal structure |
| **D13** | **Reverse limit** `q → ∞` | symmetric to D12 via bar | combinatorial | ⏳ scaffold | [`conj:reverse-limit-q-to-infinity`](../content/quantum-observable-universe/braids-and-knots/reverse-limit-q-to-infinity.md) (this PR) — bar-image of Kashiwara crystal at q→0; pairs matter/antimatter via Kashiwara/reverse-crystal fixed points | author the explicit reverse-crystal construction in Lean; verify every Kashiwara result has a bar-paired reverse-crystal counterpart |
| **D14** | **Modular S-transform** | `q ↔ q̃ = exp(2πi/τ)` | small-q ↔ root-of-unity asymptotics | ⏳ scaffold | [`conj:modular-s-transform-q-q-tilde`](../content/quantum-observable-universe/braids-and-knots/modular-s-transform-q-q-tilde.md) (this PR) — explicit S-transform `τ ↦ −1/τ` on Hecke modular parameter; complements D1 bar + D2 Hermitian * | verify modular continuation of framework quantities; numerical witness on Volume Conjecture asymptotic |
| **D15** | **Pachner 2-3 ↔ Pentagon** | TV/RT state-sum invariance | hyperbolic triangulation moves | ⏳ scaffold | [`conj:pachner-pentagon-borromean`](../content/quantum-observable-universe/braids-and-knots/pachner-pentagon-borromean.md) (this PR) — 𝓑₃: 8 ideal octahedra ↔ 16 ideal tetrahedra under Pachner 2-3; Pachner-invariance = Pentagon identity of Φ_q; conjectured h⁴ = −3/4 derivable from 10-fold Pentagon-coherent state contributions | compute prototype: Pachner state-sum on 𝓑₃ at q₀; cross-check h⁴ via Lobachevsky 8G = Σ Λ(θᵢ) |
| **D16** | **K-theoretic (K₃ / Bloch)** | Bloch-group element of Borromean complement | algebraic K-theory regulator `r₂: K₃(ℂ) → ℝ` | ⏳ scaffold | [`conj:borromean-bloch-group-element`](../content/quantum-observable-universe/braids-and-knots/borromean-bloch-group-element.md) (this PR) — `[𝓑₃] = 8·[e^(iπ/3)] ∈ B(ℂ)`; regulator `r₂ = 8G`; conjectured `r₂⁽²⁾ = −6G` gives h⁴ = −3/4 K-theoretically | extend Bloch-Wigner regulator to order h²; cross-check r₂⁽²⁾[𝓑₃] = −6G against Markov-trace closed form |
| **D17** | **DIM master Pentagon** | Macdonald-Pentagon = q-dilog-Pentagon = group-like in Ding-Iohara-Miki | unified algebraic ancestor | ⏳ scaffold | [`conj:dim-master-pentagon`](../content/quantum-observable-universe/braids-and-knots/dim-master-pentagon.md) (this PR) — DIM `U_{q,t}` master Pentagon specialises to Faddeev / Rogers / Macdonald / Pachner (D15) / Bloch (D16) | research-grade; identify specialisation maps |
| **D18** | **Mirror / 3d-3d correspondence** | partition functions on hyperbolic 3-manifolds | 3d N=2 gauge theories | ⏳ scaffold | [`conj:mirror-3d-3d-correspondence`](../content/quantum-observable-universe/braids-and-knots/mirror-3d-3d-correspondence.md) (this PR) — 3d-3d maps 𝓑₃ to T[𝓑₃]; h⁴ coefficient = 4-loop contribution | very long horizon; requires QFT Lean infrastructure |
| **D19** | **Langlands dual** | `Ĝ` ↔ `G` quantum group | `H_n(q)` ↔ `H_n(q⁻¹)` quantum-Langlands | ⏳ scaffold | [`conj:quantum-langlands-dual`](../content/quantum-observable-universe/braids-and-knots/quantum-langlands-dual.md) (this PR) — distinct from bar at algebra level; coincides with D13 reverse-limit; couples with D22 | research-grade |
| **D20** | **Pontryagin** | character ↔ measure on dual locally-compact abelian group | classical Fourier duality | ⏳ scaffold (degenerate) | [`conj:pontryagin-dual-coxeter-character`](../content/quantum-observable-universe/braids-and-knots/pontryagin-dual-coxeter-character.md) (this PR) — Z/2 self-Pontryagin-dual after S_n abelianisation; subsumed by D1 bar | low priority; recorded for completeness |
| **D21** | **Poincaré-Lefschetz** | Borromean complement cohomology ↔ homology | manifold-with-boundary duality | ⏳ scaffold | [`conj:poincare-lefschetz-borromean`](../content/quantum-observable-universe/braids-and-knots/poincare-lefschetz-borromean.md) (this PR) — H²(∂𝓑₃) ≅ H_1 ≅ ℤ³; vol-form ↔ fund-class pairs to 8G (third route alongside D16) | partial Mathlib; pair with D16 |
| **D22** | **Folding (Type B / Type C / Type D ← Type A)** | symmetric-crystal Type-B folding for chirality / CPT | non-simply-laced Cartan reduction | ⏳ scaffold | [`conj:type-b-folding-cpt`](../content/quantum-observable-universe/braids-and-knots/type-b-folding-cpt.md) (this PR, CLAUDE.md §7b authoring shortcut) — Type-B fold of `sl_n` Cartan datum yields symmetric crystal; bar-invariance by construction; alternative CPT decomposition (D6 ⊗ D22 ⊗ D8) | verify Type-B folding produces bar-invariant GS-NF on canonical atomic-braid catalogue; identify ⁴He as folded-crystal singlet |
| **D23** | **Hecke algebraic / cyclic Frobenius** | `tr_M` symmetric pairing on Hecke | Σ-symmetric inner product on Frobenius algebra | ✅ inside D3 | covered by `def:frobenius-hopf-substrate` | (closed) |
| **D24** | **Lusztig braid / canonical basis** | canonical basis crystal at `q = 1` | KL polynomials | ⏳ scaffold | [`conj:lusztig-canonical-basis-q-eq-1`](../content/quantum-observable-universe/braids-and-knots/lusztig-canonical-basis-q-eq-1.md) (this PR) — Kashiwara crystal at q→0 decategorifies to Lusztig canonical basis at q=1 via KL; completes Cluster D | partial Mathlib KL |

## §2. Duality clusters

Several dualities cluster — closing one progresses others:

### Cluster A — discrete-symmetry decomposition of CPT (D5 ↔ D6, D7, D8)

Currently the framework has D5 (composite CPT) but lacks separate C, P, T. The natural home for **C** is the color-tube flavor swap (PR [#1111](https://github.com/litlfred/qou/pull/1111) merged); **P** is braid mirror reflection (overlaps writhe bar-anti-symmetry); **T** is Markov-trace reversal.

Closing D6 + D7 + D8 separately would let CPT be verified as a derived composite identity, not an axiom.

### Cluster B — nuclear physics (D9 ↔ D10 ↔ D11)

Isospin SU(2)_I (D9) + spin SU(2)_S (D10) → Wigner SU(4) (D11). The reconciliation audit identifies SU(4) as the natural L3 layer (nuclear-shell binding). **D9 is the bottleneck** — extending crystal-isospin-degeneracy from plain generators to operator-valued `⋈_K` interface unlocks the cluster. See [`docs/audits/2026-05-24-isospin-categorical-source.md`](audits/2026-05-24-isospin-categorical-source.md).

### Cluster C — Pentagon validation (D15 ↔ D16 ↔ D17 ↔ D18)

Four candidate routes for h⁴ = −3/4 cross-validation: Pachner (D15), Bloch-group (D16), DIM master (D17), mirror 3d-3d (D18). Only Habiro / direct Jones-polynomial closed form (already in [`borromean-markov-trace-closed-form.md`](../content/quantum-observable-universe/braids-and-knots/borromean-markov-trace-closed-form.md)) is computationally done.

### Cluster D — limit dualities (D12 ↔ D13 ↔ D24)

Kashiwara `q → 0` (D12), reverse `q → ∞` (D13), Lusztig `q = 1` decategorification (D24). Currently only `q → 0` is partially exploited (crystal-isospin-degeneracy). Pairing these would give the full classical-limit picture across all three limits.

## §3. What's MISSING that this tracker exposes

1. **C, P, T separately** — D6, D7, D8 are not isolated. The framework only has CPT composite. The color-tube structure (PR #1111 merged) provides the natural home for C.

2. **SU(4) Wigner is L3 (nuclear-shell binding)** — the magic A·8G shell rule at A=4 IS the first Wigner SU(4) supermultiplet. The framework already has shell-closure infrastructure ([`shell-closure-nf-term-count.md`](../content/quantum-observable-universe/molecular-construction/shell-closure-nf-term-count.md), [`shell-closure-normal-form.md`](../content/quantum-observable-universe/archimedean-universe/shell-closure-normal-form.md)) but it is **not wired into the mass formula** — that's the deeper L3 gap. See [`docs/audits/2026-05-24-magic-shell-gs-filtration-exploitation.md`](audits/2026-05-24-magic-shell-gs-filtration-exploitation.md).

3. **Isospin operator-valued extension** (D9 ⏳ → ✅) — `crystal-isospin-degeneracy` covers only plain generators; canonical `⋈_K` interface is open. This is the Phase 5q open finding from the cheat sheet.

4. **SU(2) → SO(3) spin closure** (D10 ⏳ → ✅) — pipeline uses only S₃ subgroup; full SO(3) (ℓ = 2, 3) opens h⁴ refinement.

5. **Pentagon cross-validation** (Cluster C) — 4 candidate routes flagged; only direct-Jones-polynomial done.

## §4. How to use this tracker (for siblings)

When opening a PR that touches duality structure:

1. **Identify which D-row** your work is on. Add a comment in your PR description: `Duality: D9 (isospin)` etc.
2. **Coordinate with siblings** by D-row. If two PRs are both working on D9, post intent on each via `/coordinate`.
3. **Update this tracker** when your PR lands a new duality block. Move the row from ⏳ → ✅ or ⚪ → ⏳.
4. **Cross-link** from your audit doc to `docs/duality-tracker.md` so siblings find your work.
5. **GB-filtration + jet-order discipline** — every probe claim must report (a) GB filtration level (length / jet grade), (b) jet order (which power of h or q-1), (c) bar-symmetry status of the claim. See updated skill [`.claude/skills/local/canonical-watcher.md`](../.claude/skills/local/canonical-watcher.md) §"Probe follow-up discipline".

## §5. Cross-references

- [`docs/canonical-derivation-cheat-sheet.md`](canonical-derivation-cheat-sheet.md) — the canonical chain
- [`docs/audits/2026-05-23-lambda-scale-canonical-unification.md`](audits/2026-05-23-lambda-scale-canonical-unification.md) §13-driver menu — categorical mechanisms
- [`content/quantum-observable-universe/braids-and-knots/bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md) — bar duality D1 (most exhaustively classified)
- [`docs/audits/2026-05-24-pentagon-identity-broad-context.md`](audits/2026-05-24-pentagon-identity-broad-context.md) — Pentagon literatures (D15-D18)
- [`docs/audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`](audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md) — three-layer L1/L2/L3 (D9-D11 cluster B)
- [`docs/audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) — SU(2) → SO(3) (D10)
- [`docs/audits/2026-05-24-ew-couplings-substrate-empirical-matches.md`](audits/2026-05-24-ew-couplings-substrate-empirical-matches.md) — D4 EW substrate hypothesis scaffolds
- PR [#1127](https://github.com/litlfred/qou/pull/1127) — q_0 reality / Hermitian * (D2)
- PR [#1137](https://github.com/litlfred/qou/pull/1137) — `CategoricalHiggsIdempotent` proved `m_W/m_Z = cos θ_W` (D4)
- PR [#1143](https://github.com/litlfred/qou/pull/1143) — EW-substrate empirical matches + 3-hypothesis Lean scaffold (D4)
