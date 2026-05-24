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
| **D4** | **Higgs boson / Higgs field** | H boson = 1-component knot (radial mode) | Goldstone field = absorbed into W/Z longitudinal polarisation | ⏳ skeleton | [`categorical-higgs-mechanism.md`](../content/quantum-observable-universe/braids-and-knots/categorical-higgs-mechanism.md) — W± → T(2,4), Z → T(2,6), H singlet | flesh out the Goldstone-eating as knot-to-link transition formally |
| **D5** | **CPT composite** | bar-involution on orbit closure | parity-mirror + time-reverse + charge-conjugate composite | ✅ formalised | [`cpt-orbit-closure-density.md`](../content/quantum-observable-universe/particle-interactions/cpt-orbit-closure-density.md) | (closed) — but C, P, T **separately** are not (see D6-D8) |
| **D6** | **Charge conjugation (C)** alone | flavor swap u ↔ ū, d ↔ d̄ on color sheets; matter ↔ antimatter | charge sign reversal | ⏳ scaffold | [`conj:c-from-color-flavor-swap`](../content/quantum-observable-universe/braids-and-knots/c-from-color-flavor-swap.md) (this PR) — Z/2 flavor-conjugation involution on color sheets; conditional on [`conj:inter-nucleon-channel-color-tube`](../content/quantum-observable-universe/braids-and-knots/inter-nucleon-channel-color-tube.md) (PR [#1111](https://github.com/litlfred/qou/pull/1111)) | author Lean class `CFromColorFlavorSwap` instance; verify C action numerically; promote conjecture → proposition |
| **D7** | **Parity (P)** alone | mirror reflection of braid diagram | left/right chirality | ⏳ implicit | writhe `w(K)` is classified as bar-anti-symmetric in [`bar-involution.md`](../content/quantum-observable-universe/braids-and-knots/bar-involution.md#tbl:bar-involution-table3-data) Table 3; not isolated as P | author `prop:p-from-braid-mirror` block — disambiguates from bar-involution (which composes P with C) |
| **D8** | **Time-reversal (T)** alone | braid-word reversal; trace cyclicity | future/past asymmetry | ❌ not isolated | not in any block (only the composite CPT exists) | author block deriving T as Markov-trace cyclicity dual |
| **D9** | **Isospin SU(2)_I** | flavor swap `u ↔ d` between proton/neutron color-sheet flavor triples | nucleon doublet `(p, n)` | ⏳ scaffold | [`crystal-isospin-degeneracy.md`](../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md) (plain-generator restricted, q→0 only) + [`conj:isospin-from-canonical-bowtie`](../content/quantum-observable-universe/braids-and-knots/isospin-from-canonical-bowtie.md) (this PR) — regularised crystal functional for operator-valued `⋈_K` extension; bar-anti-symmetric residue matches substrate 305 ppm flavor split | author Lean class `IsospinFromCanonicalBowtie` instance + `verify_isospin_bar_anomaly.py` numerical witness at 1 ppb |
| **D10** | **Spin SU(2)_S** | SU(2) action on color-sheet rotation | spatial rotation group | ⏳ partial (S₃ subgroup only) | implicit in knot-operator catalogue; full SO(3) gap flagged in [`2026-05-24-h4-coefficient-source-trace-and-so3-gap.md`](audits/2026-05-24-h4-coefficient-source-trace-and-so3-gap.md) | extend S₃ → full SO(3); ℓ = 2, 3 spherical harmonics populate h⁴+ |
| **D11** | **Wigner SU(4) = SU(2)_S × SU(2)_I** | combined spin-isospin classical limit | nuclear-physics 4-fold supermultiplets | ⚪ not in framework | one mention in [`2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md`](audits/2026-05-24-single-knot-vs-multi-nucleon-reconciliation.md) §L3 | requires D9 and D10 closed first; this is the natural L3 (nuclear-shell binding) categorical source per the three-layer decomposition |
| **D12** | **Kashiwara crystal** `q → 0` | KLR canonical basis | combinatorial / decategorification | ⏳ driver in 13-menu | [`crystal-isospin-degeneracy.md`](../content/quantum-observable-universe/braids-and-knots/crystal-isospin-degeneracy.md), CLAUDE.md §7b | full Borromean crystal-graph derivation — no QOU block ties h⁴ to crystal structure |
| **D13** | **Reverse limit** `q → ∞` | symmetric to D12 via bar | combinatorial | ⚪ not in framework | none | extend D12 (and D1) — pair `q → 0` with `q → ∞` |
| **D14** | **Modular S-transform** | `q ↔ q̃ = exp(2πi/τ)` | small-q ↔ root-of-unity asymptotics | ⚪ driver (viii) only | mentioned in 13-driver menu; root-of-unity probes on main (PRs #1116-area, RT level scan) | author `prop:modular-s-q-q-tilde-duality` block; ties to Volume Conjecture |
| **D15** | **Pachner 2-3 ↔ Pentagon** | TV/RT state-sum invariance | hyperbolic triangulation moves | ⚪ literature-pointer only | hinted in [`2026-05-24-pentagon-identity-broad-context.md`](audits/2026-05-24-pentagon-identity-broad-context.md) §2.4 | author `prop:pachner-pentagon-borromean` block — Borromean 8 ideal octahedra → 16 ideal tetrahedra |
| **D16** | **K-theoretic (K₃ / Bloch)** | Bloch-group element of Borromean complement | algebraic K-theory regulator `r₂: K₃(ℂ) → ℝ` | ⚪ literature-pointer only | mentioned in Pentagon broad-context §2.2 | `prop:borromean-bloch-group-element` block — ties `h⁴ = −3/4` to K-theoretic structure |
| **D17** | **DIM master Pentagon** | Macdonald-Pentagon = q-dilog-Pentagon = group-like in Ding-Iohara-Miki | unified algebraic ancestor | ⚪ literature-pointer | Pentagon broad-context §2.7 | research-grade — unified ancestor for several existing claims |
| **D18** | **Mirror / 3d-3d correspondence** | partition functions on hyperbolic 3-manifolds | 3d N=2 gauge theories | ⚪ literature-pointer | Pentagon broad-context §2.8 | very long horizon |
| **D19** | **Langlands dual** | `Ĝ` ↔ `G` quantum group | `H_n(q)` ↔ `H_n(q⁻¹)` quantum-Langlands | ⚪ not in framework | none | folding picture relates SU/SO/Sp — could ground `2b/pyhecke` work |
| **D20** | **Pontryagin** | character ↔ measure on dual locally-compact abelian group | classical Fourier duality | ❌ not in framework | none | low priority — abelian; QOU is non-abelian |
| **D21** | **Poincaré-Lefschetz** | Borromean complement cohomology ↔ homology | manifold-with-boundary duality | ❌ not in framework | none | medium priority — Pachner / Bloch group naturally invoke it |
| **D22** | **Folding (Type B / Type C / Type D ← Type A)** | symmetric-crystal Type-B folding for chirality / CPT | non-simply-laced Cartan reduction | ⚪ literature-pointer (CLAUDE.md §7b authoring shortcut) | CLAUDE.md §7b mentions for matter-antimatter via Type-B folding | author `prop:type-b-folding-cpt` block |
| **D23** | **Hecke algebraic / cyclic Frobenius** | `tr_M` symmetric pairing on Hecke | Σ-symmetric inner product on Frobenius algebra | ✅ inside D3 | covered by `def:frobenius-hopf-substrate` | (closed) |
| **D24** | **Lusztig braid / canonical basis** | canonical basis crystal at `q = 1` | KL polynomials | ⚪ literature-pointer | CLAUDE.md §7b authoring shortcut for decategorifying to KL | medium priority — connects D9 (isospin), D10 (spin), D12 (crystal) |

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
- PR [#1127](https://github.com/litlfred/qou/pull/1127) — q_0 reality / Hermitian * (D2)
