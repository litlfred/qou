# T2-b (bean qou-5lbe) — the concrete rank 3→4 Wenzl ascent: investigation report

Date: 2026-07-19 · Branch context: `claude/vndn-execution-2026-07-19` (read-only task; no repo files touched)
Artifacts beside this report: `gram_h4.py` (the sympy derivation, fully self-checking),
`gram_h4.log` (run log, 140 s wall), `gram_h4_matrix.json` (the 24×24 Gram matrix, exact),
`gram_h4_det.json` (determinant, weights, identity checks).

Sources read and pinned:
`QOU/Machinery/MarkovTraceH4.lean` (Fin-24 NF module: `TRM`, `mulσ0/1/2`, `mulNF`, `trM`),
`QOU/Machinery/HeckeH4StabilizationRung.lean` (second H4 convention: `TRM4`, `mulσ₀/₁/₂`, `iota34`),
`QOU/Machinery/HeckeTowerBasicConstruction.lean` (`WenzlTowerStep` et al.),
`QOU/Machinery/HeckeH3GramNondegeneracy.lean`, `HeckeH3Wedderburn.lean`, `HeckeH3Semisimple.lean`,
`HeckeH3AlgebraInstance.lean`, `HeckeH4BlockRep.lean`, `HeckeBraidedCategoryScaffold.lean`,
`QOU/Shared/DetFin.lean`, `QOU/MathlibExt/MatrixSemisimple.lean`;
compute infra `computations/markov/hecke_regular_nf_table.py`, `gen_gram_closure.py`,
`computations/h4_wedderburn/hecke-h4-wedderburn-seminormal.data.json`.

---

## 1. Rank-4 Gram route — det G₄ **VERIFIED** (exact symbolic, not conjectured)

### Setup pinned from the Lean source

Basis and trace transcribed **from `MarkovTraceH4.lean` verbatim** (the file that carries
`mulNF`): the 24 GB-NF words read off the `mulNF` composites (innermost `mulσ` = leftmost
letter, `mulσk` being right multiplication by σ_k):

```
b0..b23 = [], [2], [1], [0], [12], [21], [20], [01], [10], [121], [012], [201], [120],
          [010], [210], [0121], [0120], [1201], [1210], [2010], [01201], [01210],
          [12010], [012010]
```

with `TRM` exactly as in the Lean (index 9 = `h·z²+z`, index 23 = `h³z³+h²z²+2hz³+z²`, …).
Cross-checks all passed (see `gram_h4.log`):

* `TRM` = `markov_trace(Hecke(4))` of the independent generator
  `computations/markov/hecke_regular_nf_table.py`, entry-by-entry;
* each `mulσk` = `Hecke(4).gen[k]` row-by-row;
* `mulNF(e_0, e_j) = e_j` for all 24 words (word table consistent).

`G₄[i][j] = tr_M(b_i·b_j) = trM (mulNF h (e i) (e j))` computed for all 576 pairs.

**Symmetry: G₄ = G₄ᵀ holds exactly (all 276 off-diagonal pairs), symbolically over ℤ[z,h].**
This is precisely the content of the open `gram_symm` sorry in `MarkovTraceH4.lean` —
now confirmed at the sympy level (the `gen_gram_closure.py` → `MarkovTraceH4Gram` route,
bean `qou-svnb`, will discharge it in Lean).

### The determinant (fraction-free over ℤ[z,h], `DomainMatrix`; 124 s; numeric spot-check passed)

**VERIFIED (exact symbolic factorization, not interpolated):**

    det G₄ = − F₁²³ · F₂¹⁰ · F₃

    F₁ = z² − hz − 1
    F₂ = (h²+4)z² − (h³+4h)z − 1
    F₃ = (h²+3)² z² − h(h²+3)² z − 1

Notably det G₄ ∈ ℤ[z,h] is *q-free* (like the H3 det), 1391 terms expanded, deg_z = 68,
deg_h = 58. `F₁, F₂` are **the same polynomials** as in the rank-3 determinant
`det G₃ = −F₁⁵·F₂` (`HeckeH3GramNondegeneracy.gramMatrix_det`); the new rank-4 factor is
`F₃`, with `h²+4 = [2]_q²` and `h²+3 = [3]_q` (balanced, at `h = q−q⁻¹`): the [n]-ladder
enters exactly one rung per rank.

### Hecke specialization `h = q − 1/q` (factored over ℚ(q))

    det G₄ = − (z−q)²³ (qz+1)²³ ((q²+1)z−q³)¹⁰ ((q³+q)z+1)¹⁰
               · ((q⁴+q²+1)z−q⁵) ((q⁵+q³+q)z+1) / q⁵⁸

### Degeneracy-locus reading — exactly the Ocneanu weight zeros

The five Ocneanu weights (solved from the 5-conjugacy-class character system, characters from
the `HeckeH4BlockRep` seminormal blocks / `h4_wedderburn` JSON; `Σ d_λ y_λ = 1` checked):

| λ | d_λ | y_λ (factored numerator) |
|---|---|---|
| (4) | 1 | `(qz+1)·((q³+q)z+1)·((q⁵+q³+q)z+1)` / u₄ |
| (3,1) | 3 | `−q·(z−q)·(qz+1)·((q³+q)z+1)` / u₃₁ |
| (2,2) | 2 | `−q³·(z−q)·(qz+1)` / u₂₂ |
| (2,1,1) | 3 | `q²·(z−q)·(qz+1)·((q²+1)z−q³)` / u₂₁₁ |
| (1⁴) | 1 | `−q³·(z−q)·((q²+1)z−q³)·((q⁴+q²+1)z−q⁵)` / u₁⁴ |

(units u_λ ∈ ℚ(q)ˣ built from (q²+1)², q⁴+1, q²±q+1 — full forms in `gram_h4_det.json`.)

**Verified structural identity** (the expected Wenzl/Wedderburn shape, checked exactly in sympy):

    det G₄ = − (det A₄)² · Π_{λ⊢4} y_λ^{d_λ²}

where `det A₄ = −(q²+1)²⁴(q⁴+1)¹⁰(q²−q+1)³(q²+q+1)³/q⁵⁰` is the 24×24 Wedderburn
coordinate-change determinant already pinned in
`computations/h4_wedderburn/hecke-h4-wedderburn-seminormal.data.json`. The computed unit ratio
is exactly −1. Exponent bookkeeping (each linear factor's exponent = Σ over the partitions whose
weight contains it of d_λ²):

| z-zero | kills weights | exponent |
|---|---|---|
| `z = q` | (3,1),(2,2),(2,1,1),(1⁴) | 9+4+9+1 = **23** |
| `z = −1/q` | (4),(3,1),(2,2),(2,1,1) | 1+9+4+9 = **23** |
| `z = q³/(q²+1)` | (2,1,1),(1⁴) | 9+1 = **10** |
| `z = −1/(q(q²+1))` | (4),(3,1) | 1+9 = **10** |
| `z = q⁵/(q⁴+q²+1)` | (1⁴) | **1** |
| `z = −1/(q(q⁴+q²+1))` | (4) | **1** |

This retro-explains the rank-3 exponents too (5 = 4+1 twice), and gives the general
conjecture-with-two-data-points `det G_n = ±(det A_n)²·Π y_λ^{d_λ²}` (n = 3 verified in the
existing Lean/sympy; n = 4 verified here).

**Nondegeneracy statement**: away from the **six** points above (generic q), the H4 Markov-trace
pairing is nondegenerate — the exact rank-4 realization of the `WenzlTowerStep.semisimple_ascend`
trace-nondegeneracy hypothesis.

## 2. Feasibility verdict for Lean

**A raw 24×24 determinant is NOT reachable.** `QOU/Shared/DetFin.lean` tops out at
`det_fin_six`, whose RHS is already the full 720-term Leibniz sum (machine-generated); a
`det_fin_24` would carry 24! ≈ 6.2·10²³ terms. Incremental expansion, LU, or Bareiss on
symbolic ℤ[z,h] entries are all far past any heartbeat budget; an explicit-inverse
verification (G·G⁻¹ = 1, 576 rational-function identities with denominator F₁F₂F₃) is
bounded but brutally heavy. **Do not attempt the H3 `gramMatrix_det` pattern at rank 4.**

The honest reachable statements, in recommended order:

**(i) `isSemisimpleRing_H4A` via `wedderburn₄` transfer — RECOMMENDED PRIMARY.**
Mirror `HeckeH3Semisimple`: once A2-s3 assembles
`wedderburn₄ : H4A K (q−q⁻¹) ≃ₐ[K] K × K × M₂(K) × M₃(K) × M₃(K)`,
semisimplicity transfers by `RingEquiv.isSemisimpleRing` with the matrix factors supplied by
the existing `QOU.MathlibExt.MatrixSemisimple`. No Gram matrix, no determinant. Genericity
hypotheses read off `det A₄`: `q ≠ 0`, `q²+1 ≠ 0`, `q⁴+1 ≠ 0`, `q⁴+q²+1 ≠ 0` — note the
**new** `[4]`-type condition `q⁴+1 ≠ 0` absent at rank 3.

**(ii) `exists_pairing_ne_zero₄` via blocks, NOT via det — RECOMMENDED SECONDARY.**
The rank-4 analog of `HeckeH3GramNondegeneracy.exists_pairing_ne_zero`, proved from
`wedderburn₄` + per-block trace weights instead of a 24×24 determinant:
1. a finite lemma `trM_eq_weighted_char : trM z h v = Σ_λ y_λ·χ_λ(image)` — concretely 24
   scalar identities `TRM k = Σ_λ y_λ·tr(ρ_λ(b_k))`, each `field_simp; ring`-grade with the
   explicit `HeckeH4BlockRep` matrices (machine-generatable; entirely feasible);
2. given `y ≠ 0`, its `wedderburn₄` image has a nonzero component in some block λ; choose
   `w` = the preimage of the dual elementary matrix in that block (the `A_inv` columns of the
   JSON); then `trM(y·w) = y_λ·(nonzero matrix-trace pairing)`, nonzero under `y_λ ≠ 0`.
   The six degeneracy hypotheses enter only as the six linear z-conditions of §1's table,
   stated factor-by-factor exactly as at rank 3.

What (ii) adds beyond (i): the *trace-nondegeneracy* half of the Wenzl hypothesis pair at the
3→4 rung, which (i) does not mention; it is also what a future genuine tower-step proof
consumes. Cost: (ii) needs everything (i) needs **plus** the trace-decomposition lemma and
preimage bookkeeping; estimate (i) ≈ the HeckeH3Wedderburn+Semisimple effort scaled ×4 in
table size (machine-generated), (ii) ≈ +30% on top.

**(iii) det G₄ stays a compute-layer fact.** Record the verified factorization as a witness
JSON + audit doc (this report's data files are the seed), cited from Lean docstrings the way
`hecke-h3-markov-gram.data.json` is — but labelled **sympy-verified, Lean-out-of-reach**; the
Lean-facing statement is (ii), which needs no det.

## 3. What a genuine `WenzlTowerStep` instance at (n=3 → n=4) would require

**Blocking discovery: the class is not instantiable at finite rank at all — the obstruction is
in its binders, not in missing Gram/Wedderburn work.** `WenzlTowerStep` binds
`[HeckeBraidedPresentation R q Hn σn] [HeckeBraidedPresentation R q Hn1 σn1]` with
`σ : ℕ → H` and laws **for all i ∈ ℕ** (`hecke_quadratic : ∀ i`, `braid_adjacent : ∀ i`).
A finite-rank algebra cannot supply the tail: the natural padding `σ_i := q•1` (i ≥ rank)
satisfies the quadratic (q is a root) but **fails the mixed braid relation** — for the last
real generator σ against the scalar tail t = q•1, `σ·t·σ = q•σ² = (q²−1)•σ + q•1` while
`t·σ·t = q²•σ`, equal only if σ is scalar. So no scalar/central tail works; the
`HeckeH3AlgebraLaws` docstring's "no finite-level instance possible" is confirmed with a proof
sketch. Any concrete (3→4) instance requires a **class refactor** first (generators indexed by
`Fin (n−1)`, or laws guarded by `i+1 < n`) — a design change, out of scope here.

Ingredient inventory for the concrete rung (independent of the binder problem):

| Ingredient | Status |
|---|---|
| `Hn = H3A K h` as `Ring`/`Algebra` | **EXISTS** (`HeckeH3AlgebraInstance` + `HeckeH3AlgebraLaws`) |
| `Hn1 = H4A` as `Ring`/`Algebra` on `Fin 24 → R` with `mulNF` | **MISSING — the single biggest gap.** No `H4A` wrapper exists anywhere (grep confirms). Needs the H4 analog of `HeckeH3AlgebraLaws` — above all `mulNF` associativity: 24³ = 13 824 basis triples. Machine-generatable by the `gen_gram_closure.py` sparse-basis-chain method, but the generated module will be very large. Alternative worth weighing: realize H4A as the subalgebra of `End` generated by the three right-action operators (Ring instance for free) and transport the NF basis — cheaper on proofs, costlier on API. |
| `ι : H3A →ₐ[R] H4A` | **PARTIAL + convention clash.** `iota34` + intertwining lemmas exist (`HeckeH4StabilizationRung`) but in the **other** 24-basis ordering (H3-prefix), while `mulNF` lives in the `MarkovTraceH4.lean` ordering (H3 parabolic at indices {0,2,3,7,8,13}). The two Fin-24 conventions coexist in the same namespace `QOU.Machinery.H4` (`mulσ₀` vs `mulσ0` differ only by subscript glyph) — unification (a permutation lemma, or porting `mulNF` to the prefix basis) is prerequisite hygiene before any AlgHom `ι`. |
| `trn1 = trM z h` | **EXISTS** (`MarkovTraceH4.trM`; cyclicity pending `gram_symm` closure, bean `qou-svnb`) |
| Trace nondegeneracy hypothesis | **NOW PINNED** by §1: nonzero away from six explicit z-points |
| Rank-3 semisimplicity (ascent input) | **EXISTS** (`isSemisimpleRing_H3A`) |
| The ascent field itself | Would be discharged **vacuously-forward**: at a concrete rank one proves the *consequent* (`IsSemisimpleRing H4A` via `wedderburn₄`), making `semisimple_ascend` trivially true — legitimate but it bypasses the tower content entirely. |

**Shortest honest path — recommendation: do NOT instantiate the class.** Prove the rank-4
conclusions directly — (i) `isSemisimpleRing_H4A` and (ii) `exists_pairing_ne_zero₄` — and add
a remark that at concrete ranks the tower step is bypassed by explicit Wedderburn, exactly as
the rank-3 rung already is; the genuine tower-step proof through the Jones basic construction
remains the general-n OPEN target, now with its two hypotheses *both* concretely realized at
the 3→4 rung ((i)+§1). If an instance is still wanted later, it needs the finite-rank class
refactor first.

## 4. Findings summary (one screen)

1. **det G₄ = −(z²−hz−1)²³·((h²+4)z²−(h³+4h)z−1)¹⁰·((h²+3)²z²−h(h²+3)²z−1) — VERIFIED**
   exact symbolic (fraction-free ℤ[z,h] det + factor + numeric spot-check), not conjectured.
   q-free like rank 3; first two factors are literally the rank-3 factors; the new factor
   carries `[3]_q = h²+3`.
2. **Wenzl/Wedderburn identity verified: det G₄ = −(det A₄)²·Π_λ y_λ^{d_λ²}** with the JSON's
   coordinate determinant and the five solved Ocneanu weights; every exponent
   (23/23/10/10/1/1) accounted for by the d_λ² of the weights vanishing there.
3. **G₄ symmetry holds symbolically** — independent confirmation of the `gram_symm` content.
4. **Lean verdict: Fin-24 det unreachable; go block-wise.** Recommend (i) `wedderburn₄` +
   `isSemisimpleRing_H4A` (mirror of rank 3; new genericity `q⁴+1 ≠ 0`), then (ii)
   `exists_pairing_ne_zero₄` via `trM = Σ y_λ χ_λ` (24 finite identities) + block preimages —
   no determinant anywhere.
5. **`WenzlTowerStep` cannot be instantiated at finite rank as stated** (∀-ℕ presentation
   binders; scalar-tail padding provably fails the mixed braid relation). Bypass, don't
   instantiate; note the bypass in prose.
6. **Missing-ingredient list**: H4A Ring/Algebra instance (assoc closure — big,
   machine-generatable), `wedderburn₄` assembly (A2-s3; JSON `A`/`A_inv` ready),
   trace-decomposition lemma, `ι` AlgHom + **dual Fin-24 basis-convention unification**
   (`MarkovTraceH4` vs `HeckeH4StabilizationRung`, same namespace, near-identical names —
   flagged as latent-confusion debt).
