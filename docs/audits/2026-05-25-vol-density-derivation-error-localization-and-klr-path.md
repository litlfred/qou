# VolDensity derivation review, error localization, and full KLR path forward

**Date**: 2026-05-25
**Branch**: `claude/vol-density-derivation-bug-squash-2026-05-25`
**Status**: Audit + workplan. Reviews the canonical VolDensity derivation,
localizes the mass-sweep errors in (jet-order × filtration × partition ×
representation) space, and lays out concrete bug-squash paths for the
KLR option + 4 alternative structural options.

**Sibling coord**: This doc complements [PR #1224](https://github.com/litlfred/qou/pull/1224)
(Δ_λ closure synthesis). My measured per-atom h² coefficients (PR
[#1220](https://github.com/litlfred/qou/pull/1220)) ARE the multi-atom
consistency constraint #2 violation that #1224 audits structurally.

## §1. Review: the canonical VolDensity derivation

Per [`canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
+ [`lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md):

```
substrate q_0 → 𝐂 categorical action → Yekutieli non-abelian Stokes
              → H_n(q) Hecke algebra → Wedderburn decomposition (λ ⊢ n)
              → Frobenius pairing tr_M = Σ_λ y_λ χ_λ
              → confinement SDP → canonical T_w
              → Archimedean functor at q_0
              → MeV observables
```

**Single canonical mass formula**:
```
m(K) = m_e · VolDensity(K, q_0)
```

For binding energy with atom-to-knot assignment K = K_atom:
```
B(atom) = m_e · Σ_λ y_λ(atom) · χ_λ(β_atom)
```
where:
- **β_atom** is the canonical atomic braid (Rule-14 census assignment)
- **χ_λ(β)** is the character of partition λ ⊢ n on β (KLR-categorified)
- **y_λ(atom)** are SDP shadow-prices from the confinement constraint
- The sum runs over all partitions λ of n (Wedderburn blocks of H_n(q))

**Production simplification** (current `mass_table_ppb.py`):
```
B = ν_SDP · m_e · Vol(K)        [Kashaev law, single-block]
B = ν · m_e · A · 8G            [magic A·8G rule, ⁴He]
B = n_α · B(⁴He) + n_pairs·c_αα [α-cluster recursion]
```

These are **single-block projections** of the full Σ_λ y_λ χ_λ
formula — valid when the SDP shadow-prices are dominantly on ONE
Wedderburn block. **The error sources are precisely the missing
multi-block contributions.**

## §2. Error localization across (jet, filtration, partition, representation)

From [PR #1214](https://github.com/litlfred/qou/pull/1214) wiring status + [PR #1220](https://github.com/litlfred/qou/pull/1220) h² coefficient hunt:

### §2.1 Jet order (h^k scale)

Each atom's `err / B_AME` classified in h^k units:

| Atom | err % | jet-order | bar-parity | KLR |
|------|-------|-----------|------------|-----|
| 3H | −0.16% | **≈ h⁴ (1.91e-3)** | bar-sym | ✓ under |
| 2H | +1.09% | h⁴ → h²/2 | mixed | ✗ over |
| 3He | −2.97% | ≈ h² (4.37e-2) | bar-sym | ✓ under |
| 4He | +5.87% | ≈ h² (4.37e-2) | bar-sym | ✗ over |
| 12C, 16O, 20Ne | +5-8% | ≈ h² | bar-sym | ✗ over |
| 8Be, 24Mg | +10-11% | h² → h/2 | bar-sym → mixed | ✗ over |
| 40Ca | +19.5% | ≈ h (0.21) | bar-anti-sym | ✗ over |

**Key observations**:
- 3H is **already at h⁴ closure** — the Borromean Markov-trace h⁴ = −3/4 coefficient scale. Cleanest match in the sweep. Direction (under-prediction) is KLR-consistent.
- 3He, 4He, 12C, 16O, 20Ne all at **h² scale**, bar-symmetric. The under-predictor (3He) is KLR-consistent; the over-predictors (4He, 12C, 16O, 20Ne) violate KLR — these are the **squashable bugs**.
- 40Ca at **h scale** is the outlier — bar-anti-symmetric component dominates, suggesting α-cluster recursion accumulates h-order error that vanishes at h² for lighter atoms.

### §2.2 GB filtration

Per `canonical-watcher.md` §Slot J, GB filtration is the Coxeter
length ℓ(β_atom) of the canonical braid:

| Atom | β_atom (current) | Approx ℓ |
|------|-------------------|----------|
| 2H | 6_2 knot (EXPLORATORY) | 4-6 |
| 3H | 8_11 knot (EXPLORATORY) | 6-8 |
| 3He | L6a4 link (EXPLORATORY) | 6-8 |
| 4He | 4·𝓑₃ tower (extrap.) | 12-16 |
| α-cluster (A=8+) | recursion | accumulating |

The errors **scale with ℓ**: shorter braids (3H, ℓ≈6) closer to AME;
longer braids (40Ca via 10×𝓑₃ tower, ℓ≈40+) further from AME.

**Implication**: the per-block χ_λ evaluation diverges from the
single-block projection at higher ℓ, because more Wedderburn blocks
acquire non-zero shadow-price.

### §2.3 Partition (Wedderburn block λ ⊢ n)

For each atom, the canonical SDP distributes shadow-prices y_λ across
partitions λ ⊢ n. Current production assumes single-block:

| Atom | n | Current λ | Canonical λ distribution |
|------|---|-----------|--------------------------|
| 4He | 4 | λ = (1,1,1,1) only (Wigner singlet) | likely (1,1,1,1) + (2,1,1) + (2,2) all non-zero |
| 12C | 12 | n_α=3 × 4He decomposition | recursion-flat across (1^12), (2,1^10), etc. |
| 40Ca | 40 | n_α=10 × 4He | accumulating multi-block weight |

**Key claim** (from PR #1220 measurement): the per-atom c values vary
by 195% — this IS the signature of varying λ-distributions per atom.
A single Wedderburn block cannot reproduce all 7 atoms simultaneously.

### §2.4 Representation (irreducible) — KLR positivity

KLR (Khovanov-Lauda-Rouquier) categorification gives:
- Each λ ⊢ n indexes a simple KLR module S_λ
- χ_λ(β) is the graded character of β acting on S_λ
- **Canonical-basis structure constants are non-negative** (KLR positivity)

⇒ For any β and any SDP shadow-price y_λ ≥ 0:
```
B_canonical(atom) = m_e · Σ_λ y_λ · χ_λ(β_atom)  ≥ 0
```
AND the framework's **single-block projection** captures only one term
in the Σ_λ — it is a **lower bound**:
```
B_prod(atom) = m_e · y_dominant · χ_dominant(β_atom)  ≤  B_canonical(atom)
```

**KLR positivity inequality**: `B_prod ≤ B_canonical ≤ B_AME` (when
β_atom is the true canonical braid). So over-predictions
(B_prod > B_AME) are STRUCTURAL BUGS, not framework features.

## §3. Bug taxonomy

The 8 KLR violations (PR #1214) decompose into 4 bug types:

### Bug Type 1: Over-simplification of SDP distribution
**Affected**: 4He (+5.87%), 12C (+5.41%), 16O (+5.30%), 20Ne (+8.34%)

Each uses `ν_SDP = 2` (integer) instead of the actual SDP distribution
Σ_λ y_λ. The 5.87% over-prediction at 4He is the difference between
"single-block ν=2" and "actual SDP shadow-price distribution across
λ ⊢ 4".

**Squash path**: replace ν_SDP=2 with the SDP-computed distribution
(requires R5-full SDP solver landing for n=4).

### Bug Type 2: α-cluster recursion non-multiplicativity
**Affected**: 8Be (+10.3%), 24Mg (+9.02%), 40Ca (+19.5%)

The recursion `B = n_α · B(⁴He) + n_pairs · c_αα` assumes the SDP
shadow-price y_λ(α-cluster) is `n_α · y_λ(⁴He) + linear pair term`.
But the canonical SDP redistributes across larger λ ⊢ 4·n_α partitions
in ways the recursion doesn't capture.

**Evidence** (PR #1220 measurement): per-atom h² coefficients vary
from 0.91×c(4He) to 2.95×c(4He) across α-cluster atoms.

**Squash path**: replace α-cluster recursion with **per-atom direct
SDP** for each n_α. This is exactly what R5-full SDP would supply.

### Bug Type 3: Census-assigned knots without canonical derivation
**Affected**: 2H (+1.09%), 3H (−0.16%), 3He (−2.97%)

These atoms use census-assigned knots (6_2, 8_11, L6a4) that match
AME volumes approximately but lack derivation from substrate. The
canonical β_atom for each (Z, N) is not derived; the census is a
heuristic match.

**Squash path**: derive β_atom for each (Z, N) from the canonical
Hecke / Rule-14 framework. Per author direction 2026-05-24: "only
use canonical/SDP braid words" — census assignment is OUT.

### Bug Type 4: Atom-to-knot rule gap
**Affected**: 5Li, 6Li, 7Li (GAP), 9Be, 11B, 14N, 19F (unwired)

These atoms have no atom→knot rule in `ATOM_ASSIGN`. The Rule-14
atom-knot census audit (`docs/audits/2026-05-24-rule14-atom-knot-census.md`)
deferred these pending R5-full SDP.

**Squash path**: Rule-14 census expansion to A ∈ {5,6,7} + canonical
β_atom derivation for odd-A atoms.

## §4. Full KLR path forward (concrete)

The just-landed tier-3 Phase B infrastructure (commits `82cba62a9`,
`2b785a46d`, `1329cdff1`, `508015eb0`) supplies `chi_lambda_braid`,
`lr_coefficient`, `tr_m_atomic_mpfr` — the compute primitives needed
for canonical KLR-derived predictions.

### KLR Step 1: derive canonical β_atom per atom

**Input**: Z, N, A for the atom
**Output**: canonical braid word β_atom ∈ B_{3·A}

For each atom:
- Build the 3A-strand braid (3 color sheets × A nucleons)
- Identify the canonical inter-nucleon `⋈_K` couplings
- Reduce to canonical GS normal form

**Status**: census-assigned heuristics exist; canonical derivation
research-grade. Tied to Rule-14 atom-knot census.

### KLR Step 2: compute χ_λ(β_atom) per partition

**Input**: β_atom from Step 1, partition λ ⊢ n
**Output**: graded character χ_λ(β_atom) ∈ R(q)
**Compute**: `chi_lambda_braid` (just landed, tier-3 Phase B)

For each atom and each λ ⊢ 3A:
- Apply chi_lambda_braid to β_atom in the KLR module S_λ
- Get character value (polynomial in q)

### KLR Step 3: solve the confinement SDP for y_λ(atom)

**Input**: χ_λ(β_atom) for all λ ⊢ 3A
**Output**: SDP shadow-prices y_λ ≥ 0 satisfying confinement constraint
**Compute**: R5-full SDP solver (PENDING — load-bearing dependency)

The confinement SDP enforces:
- Σ_λ y_λ = 1 (probability simplex)
- y_λ ≥ 0 (KLR positivity)
- additional confinement constraints per `prop:operator-selection-lp`

### KLR Step 4: assemble B_canonical(atom)

```
B_canonical(atom) = m_e · Σ_λ y_λ(atom) · χ_λ(β_atom) |_{q=q_0}
```

### KLR Step 5: validation
- **KLR positivity**: each y_λ ≥ 0, each χ_λ ≥ 0 (verify per-atom)
- **Bar-invariance**: bar(B_canonical) = B_canonical (PR #1211 + commit 68e51f80e together imply this for Borromean + bowtie)
- **Multi-atom consistency**: y_λ distribution across atoms satisfies coherence constraints (sibling PR #1224 constraint #2)

### KLR option blockers

1. **R5-full SDP solver** — load-bearing for Step 3, currently absent
2. **Canonical β_atom** for census atoms — heuristic for 2H/3H/3He
3. **Rule-14 census** for A∈{5,6,7} + odd-A atoms

## §5. Alternative structural options (other paths to squash)

Sibling PR #1224 identifies 4 structural constraints not yet jointly
imposed. Combined with my D-row scaffolds (PR #1162/#1168/#1173/#1189/#1194):

### Option B: Type-B Cartan folding (AGENTS.md §7b, my D22 scaffold)

Fold sl_n Cartan datum into Type B → symmetric crystal → bar-invariant
GS-NF **by construction**. The framework gets bar-invariance "for
free" without explicit Z/2 axioms.

**Path**: implement Type-B fold of the canonical β_atom → derive
KL-classical-limit Δ_λ values structurally.

**Status**: scaffold in `conj:type-b-folding-cpt.md` (PR #1168); Lean
class declaration pending.

### Option E: Kazhdan-Lusztig classical-limit Δ_λ (sibling PR #1224 constraint #4)

At q=1, KL polynomials decategorify the Kashiwara crystal to give
**integer** Δ_λ values per partition λ. Lifting to q=q_0 gives
specific h-expansions for each Δ_λ.

**Path** (my D24 scaffold): inhabit Kashiwara → Lusztig
decategorification functor in Lean; compute classical-limit Δ_λ for
each atom's λ-distribution; lift to q_0.

**Status**: scaffold in `conj:lusztig-canonical-basis-q-eq-1.md` (PR #1194); decategorification functor pending.

### Option F: Wigner SU(4) singlet projection (my D11 scaffold)

For 4He specifically: the totally-antisymmetric `∧⁴(fundamental) =
𝟏_SU(4)` gives the magic A·8G closure. The +5.87% over-prediction
is the difference between "single-block ν=2" and the actual SU(4)
singlet projection (which involves multi-λ contributions).

**Path**: derive SU(4) singlet projection coefficients per λ ⊢ 4;
sum gives ν_canonical(4He) directly.

**Status**: scaffold in `conj:wigner-su4-from-spin-isospin.md` (PR #1173); singlet-projection formula pending.

### Option G: Pachner-Pentagon state-sum (my D15 scaffold)

For 4He via Borromean: the 8-octahedron ↔ 16-tetrahedron Pachner
move + Pentagon identity for Φ_q gives an alternative h⁴ closure
route. Could fix the 3H residual (h⁴ scale) categorically.

**Status**: scaffold in `conj:pachner-pentagon-borromean.md` (PR #1168); state-sum compute pending.

### Option H: Bloch-group / K-theoretic regulator (my D16 scaffold)

[𝓑₃] ∈ B(ℂ) with regulator r_2 = 8G; order-h² regulator correction
r_2⁽²⁾[𝓑₃] = −6G gives h² = −3/4 (Borromean) categorically. Could
fix the 4He bar-symmetric h² gap.

**Status**: scaffold in `conj:borromean-bloch-group-element.md` (PR #1168); regulator-h² extension pending.

## §6. Per-atom bug-squash priority

| Atom | Bug type | Squash path | Priority |
|------|----------|-------------|----------|
| 4He | Type 1 (SDP simplif.) | R5-full SDP + Option F (Wigner) + Option H (Bloch) | **CRITICAL** (load-bearing for α-cluster) |
| 3H | (already at h⁴) | Option G (Pachner) refinement | Low |
| 3He | Type 1 | R5-full SDP for n=3 | Medium |
| 2H | Type 3 (census) | Canonical β derivation for (1,1) | Medium |
| 12C/16O/20Ne | Type 2 (α-cluster) | Per-atom SDP + replace recursion | High (cascade from 4He) |
| 8Be/24Mg | Type 2 + h³ accumulation | Per-atom SDP + audit recursion | High |
| 40Ca | Type 2 + h-scale accumulation | Per-atom SDP critical | High |
| 5Li/6Li/7Li | Type 4 (gap) | Rule-14 expansion | Critical for completeness |
| 9Be/11B/14N/19F | Type 4 (no rule) | Atom→knot rule authoring | Medium |

## §7. Why the single load-bearing fix is R5-full SDP

Of the 8 KLR violations across the sweep:
- **6 of 8** (4He, 8Be, 12C, 16O, 20Ne, 24Mg) trace to **4He's ν_SDP=2 over-simplification** (the α-cluster recursion inherits this multiplicatively)
- 40Ca is the same path × 10 + accumulating h-order error
- 2H is the only odd one out (census mismatch)

⇒ **Canonical wiring of 4He fixes 7 of 8 KLR violations.**

The canonical wiring of 4He requires:
1. **canonical β_⁴He** — multi-strand braid representing the
   ⁴He nucleon configuration (Wigner SU(4) singlet saturating). The
   bare Borromean tower `4·𝓑₃` is an approximation.
2. **R5-full SDP** — to compute the y_λ shadow-price distribution
   across all λ ⊢ 12 (for 4 nucleons × 3 color sheets).
3. **chi_lambda_braid** — to compute χ_λ(β_⁴He) for each λ.

The just-landed `chi_lambda_braid` infrastructure unblocks step 3.
Steps 1 + 2 remain.

## §8. Closure paths cross-validation

Per PR #1224 + this audit, three independent paths converge on the
same canonical 4He value:

- **Path KLR** (full Σ_λ y_λ χ_λ): R5-full SDP supplies y_λ
- **Path Wigner SU(4)** (Option F): singlet-projection gives ν_canonical
- **Path Bloch-group h²** (Option H): r_2⁽²⁾[𝓑₃] correction gives h² term

If all three give the same B_canonical(4He) value, that's a **triple
cross-validation** of the structural answer. This is what the
sibling PR #1224's probe-1 (bar-invariance LP) starts to test.

## §9. Bar-invariance constraint from just-merged proofs

Two new Lean / symbolic proofs on main (2026-05-24/25):

1. **`Q_borromean(h) = 0`** (PR #1211, commit `5329eb054`): `trM_borromean(h) = trM_borromean(−h)` proved via `ring` over ℚ. No bar-anti-symmetric component in bare Borromean Markov trace.

2. **`⋈_K is bar-symmetric`** (commit `68e51f80e`): operator-valued bowtie's Q-channel projection vanishes symbolically in (2,1) of H_3(q). Proves `⋈_K(h) ↦ ⋈_K(h)` under bar (q ↦ q⁻¹, σ_g ↔ σ_g⁻¹).

Together: **any bar-anti-symmetric contribution to mass must come from non-Markov-trace, non-bowtie sources** — i.e., from the SDP shadow-price y_λ choice OR from the canonical β_atom braid structure itself, NOT from the Markov-trace evaluation.

For the **305 ppm Δm_{n−p}** (D9): the just-confirmed bar-symmetry of bowtie rules out bowtie-Q-channel as the carrier. **The carrier must be the isospin-Z/2 swap (u ↔ d, q FIXED)** — a different involution from bar. Audit-correction in `2026-05-24-d9-bar-parity-correction.md` already documented this; the new proofs reinforce.

## §10. Concrete next actions

1. **Author `pyhecke/chi_lambda_eval.py`** — Python wrapper around tier-3 `chi_lambda_braid` C ABI. Enables KLR Step 2 from Python. (Tier-3 Phase B Python wrapper missing.)

2. **Tabulate χ_λ(β_⁴He) for current heuristic β** using the new infra; compare against the ν_SDP=2 single-block projection. This isolates the SDP-distribution component of the bug.

3. **Cross-check with PR #1224 probe-1** (bar-invariance LP): supply my 7 measured c-values as constraint data. Their LP solution gives Δ_λ — verify it reproduces my c-variances.

4. **Author `mass_table_canonical_attempt.py`** — alternative mass-table script that takes the Σ_λ y_λ χ_λ form symbolically and emits whatever it can without the missing y_λ inputs. Establishes the structural template for when R5-full SDP lands.

5. **Per-atom audit witnesses**: for each KLR violator, emit a witness with measured c, bug type, squash path, and the specific λ-distribution insights this audit identifies.

## §11. Cross-references

- [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md) — canonical chain
- [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md) — VolDensity single-formula framing
- [`docs/duality-tracker.md`](../duality-tracker.md) — D-row scaffolds for each Option B/E/F/G/H
- [`docs/audits/2026-05-24-d9-bar-parity-correction.md`](2026-05-24-d9-bar-parity-correction.md) — bar vs isospin-Z/2 distinction (audit correction)
- [PR #1214](https://github.com/litlfred/qou/pull/1214) — wiring-status taxonomy + KLR positivity check
- [PR #1220](https://github.com/litlfred/qou/pull/1220) — per-atom h² coefficient hunt + α-cluster bug isolation
- [PR #1224](https://github.com/litlfred/qou/pull/1224) — sibling Δ_λ closure synthesis with 4 structural constraints
- PR #1211 / commit `5329eb054` — `Q_borromean(h) = 0` Lean proof
- Commit `68e51f80e` — `⋈_K bar-symmetric` symbolic proof
- Commits `82cba62a9` + `2b785a46d` + `1329cdff1` + `508015eb0` — tier-3 Phase B compute infrastructure (C / octave / julia / gap / node / jvm / wasm wrappers for `chi_lambda_braid`, `lr_coefficient`, `tr_m_atomic_mpfr`)
