---
# qou-e4ri
title: '§7c push: HeckeAlgebra/Torsion/AlgebraicSubstrate cluster (JonesMarkovWenzl, YekutieliTriple, quantum_dilogarithm, QVonMangoldtFunction, QChebyshevFunction, WedderburnBlockDecomposition) to generic R'
status: in-progress
type: task
priority: normal
tags:
    - reorg-2026-10-04
created_at: 2026-08-01T23:07:47Z
updated_at: 2026-11-17T07:06:58Z
parent: qou-rtxm
---

## Content-based triage (2026-08-15) — criteria for whoever picks this up

Ran the **canonical folio-assistant checkers** (`wall-side-correct`, `wall-base-ring-minimal`, `q-usage-positivity-implicit` + q-regime detection) over this cluster — the same content-based, chapter-INDEPENDENT trio `q-usage-audit`'s orphan pass uses. **No path heuristics** (§7c: never infer the regime from the lean-tree directory).

`codeℝ` counts ℝ in code with comments/docstrings stripped, so docstring prose is not miscounted as a type. It is a heuristic count: a CANDIDATE is a **lead, not a verdict** — each still needs per-file adjudication (is the statement algebraic yet typed over ℝ?) plus a compile via `scripts/lean-direct-cone.sh`. Do NOT mass-fix from this table.

| file | codeℝ | generic | banner | baseRing | verdict |
|---|---|---|---|---|---|
| `JonesMarkovWenzl` | 26 | n | n | warn | **CANDIDATE** — largest in cluster |
| `YekutieliTriple` | 11 | n | n | warn | **CANDIDATE** |
| `quantum_dilogarithm` | 10 | n | n | pass | **CANDIDATE** — dilog is classically archimedean; adjudicate carefully |
| `QVonMangoldtFunction` | 3 | n | Y | pass | ℝ-typed **with** §7c banner — adjudicate |
| `QChebyshevFunction` | 5 | n | n | pass | **CANDIDATE** |
| `WedderburnBlockDecomposition` | 0 | Y | Y | warn | **DONE** — `(R : Type*) [Field R]`; the ~15-extender restructure `z1lz` deferred has since landed |

1 of 6 already done. Note the dilog files were flagged in the 2026-06-25 audit as *legitimately* archimedean — do not assume CANDIDATE means bug.


### Adjudicated: `QChebyshevFunction` is NOT a violation — correcting my own CANDIDATE call

The triage table above lists `QChebyshevFunction` as **CANDIDATE** (codeℝ=5, banner=n). **That call is wrong and is retracted.** Adjudicating the content — as the table itself demands before acting — shows the ℝ is correct:

1. **The summands are legitimately ℝ.** `psi_def` sums `Lambda_q`, the weight from the sibling `QVonMangoldtFunction`, whose own §7c note records it as *"archimedean over ℝ, since the weight `N(𝔪)^{ℏ_q}` is a real power"* (`Real.rpow`; hence its `Analysis.SpecialFunctions.Pow.Real` import). A sum of legitimately-ℝ weights is legitimately ℝ.
2. **The cut-off is an ordering.** `ideals.filter (fun m => N m ≤ X)` — ordering is archimedean content, and it is the *definitional* content of a prime-counting partial sum, not incidental.

Corroboration: `q-geometric-langlands/explicit-formula.lean`'s own `QChebyshevFunction hbar_q hbar_pos ideals X` carries a **positivity hypothesis** `hbar_pos`.

Generalising to `{R : Type*} [CommRing R]` would be *unfaithful* — it would have to drop either the real power in the weights or the order relation in the cut-off.

**Action taken instead of a port:** added the missing §7c banner to the module docstring recording exactly this, so sweeps stop re-flagging it (it read as a bare ℝ-typed module in an `AlgebraicSubstrate` namespace with no stated reason — which is precisely why it scored CANDIDATE). Compile-verified after the edit: `lean-direct-cone → ok=1`.

**Method note for the remaining CANDIDATEs in this cluster:** `banner=n` measures *documentation*, not *correctness*. Check the **sibling/definition chain** before porting — a file can inherit legitimate ℝ from the module that defines its summands. `quantum_dilogarithm` is the next most likely instance of this same pattern (the 2026-06-25 audit already lists the dilog files as legitimately archimedean).


### Adjudicated: `JonesMarkovWenzl` is NOT a violation — second CANDIDATE refuted

The table lists `JonesMarkovWenzl` as the cluster's largest **CANDIDATE** (codeℝ=26). **Refuted.** Its ℝ is required, for a sharper reason than `QChebyshevFunction`'s:

**Every `q` in the module carries a half-integer exponent.** The q-integer is `[k]_q = (q^{k/2} − q^{−k/2}) / (q^{1/2} − q^{−1/2})` and the Markov parameter is `z = 1/(q^{1/2} + q^{−1/2})`. **A square root of `q` does not exist in a generic `CommRing`** — these are `Real.rpow` applications, hence the `Mathlib.Analysis.SpecialFunctions.Pow.Real` import.

**And the generic content is not missing — it already exists, and this module proves the bridge to it.** The base-ring-generic q-integer is `QOU.QInteger.qIntBal` (`QOU.MathlibExt.QIntegerCanonical`); this file proves

```lean
theorem qInteger_eq_canonical (q : ℝ) (hq : 0 ≤ q) (k : ℕ) :
    qInteger k q = QOU.QInteger.qIntBal (q ^ ((1 : ℝ) / 2)) k
```

So `JonesMarkovWenzl` **is** `qIntBal` instantiated at the real square root of the substrate parameter. That is precisely the §7c-correct shape — generic core in one module, archimedean realisation in another — not a violation of it. Porting it to `{R : Type*} [CommRing R]` would be unfaithful: there is no `√q` to instantiate at, and restating it in a variable that *means* `q^{1/2}` is exactly what `qIntBal` already is.

**Action:** added the §7c banner recording this (docstring-only). Compile verification deferred to the running whole-corpus `lean-direct-cone --all` survey rather than run concurrently against the same olean files; a docstring-only edit cannot change elaboration, and the survey result will be appended to `qou-kljb`.

### Running pattern across this cluster — two for two

Both CANDIDATEs adjudicated so far were **legitimately archimedean with a missing banner**, not gratuitous ℝ:

| file | why ℝ is correct | defect |
|---|---|---|
| `QChebyshevFunction` | sums `Λ_q` (a `Real.rpow` weight); cut-off `N m ≤ X` is an ordering | no banner |
| `JonesMarkovWenzl` | half-integer powers `q^{k/2}` — no `√q` in a `CommRing`; generic form is `qIntBal` | no banner |

`quantum_dilogarithm` (codeℝ=10, no banner) is the next likely instance — the 2026-06-25 audit already lists the dilog files as legitimately archimedean. **Recommended for this cluster: assume banner-not-port until a definition-chain read says otherwise.** The remaining unadjudicated files are `YekutieliTriple` (11) and `QChebyshevFunction`'s neighbour `QVonMangoldtFunction` (3, already banner'd).


### PORTED: `QOU/Torsion/YekutieliTriple.lean` → `[GroupWithZero R]` (first genuine §7c fix in this cluster)

Unlike the three CANDIDATEs refuted above, this one was real. Content check: the module has **no archimedean construct at all** — the Čech deviation is `g_ij · g_jk · g_ik⁻¹`, the twisted-cocycle condition is a conjugation, and the only hypothesis used is `≠ 0`. Nothing adds, orders, or takes a limit. It was algebraic content sitting on `ℝ`.

**Base ring chosen: `[GroupWithZero R]`, not `[Field R]`** (owner steer). That is the *minimal* structure supporting what is actually used — multiplication, and inverses of non-zero elements, with no zero divisors. Addition and distributivity are never used, so `Field` would over-constrain the transition groupoid. `GroupWithZero` is already one of the generic-`R` markers §7c recognises.

**Verified by compile, at every level:**

| module | result |
|---|---|
| `QOU.Torsion.YekutieliTriple` (ported) | `ok=13, err=0` |
| `QOU.Torsion.YekutielijTriple` (compat aliases — adapted with no edit) | `ok=1` |
| `QOU.Archimedean.HyperbolicVolumeTranscendence` (consumer, 3 sites instantiated at `ℝ`) | **`ok=35, err=0`** |

Checker verdict flipped: `wall-side` **pass**, code-`ℝ` count **0**, regimes now `generic-R`.

The consumer instantiating at `ℝ` is the §7c-correct shape: the generic groupoid lives here, and the *archimedean* module picks `ℝ` at the point of use.

**Why not `R_q = ℤ[q,q⁻¹]`** (the sibling `QOU.LiftingDescent.CosimplicialCrossedGroupoid`'s ground ring): `R_q` is a `CommRing` whose non-monomial elements are not invertible, so `g_ik⁻¹` has no meaning there. `base-ring-minimal` still reports `warn` (5 `⁻¹` hits) for exactly this reason — that advisory is correct and is the open question, not a defect. Unifying the two modules would first require restating the deviation as a division-free multiplicative relation (the `R[h]` pattern) or moving to `R_qˣ`.

**Deferred, recorded:** the A/B duplication (`Torsion` vs `LiftingDescent` both declaring `YekutieliTriple`/`CosimplicialCrossedGroupoid`) is now *two generic modules over different rings* rather than generic-vs-ℝ. Merging them turns on the division question above — an owner call, not attempted here.

**Correction to my own earlier note:** I described `QOU/Torsion/YekutielijTriple.lean` as a likely stale typo file. It is not — it is a deliberate backward-compatibility re-export of the "Yekutielij" spelling, and its `abbrev`s absorbed the new parameter with no edit.


## Round 56 Progress (lane-e667)
- **PR:** https://github.com/litlfred/qou/pull/8241 (`f5d60a0cc755a36459696dc679eebd3728acc344`)
- **Module:** `QOU.Foundations.SymplecticAtomicityWenzlSemisimplicity` (`folio/quantum-observable-universe/lean/QOU/Foundations/SymplecticAtomicityWenzlSemisimplicity.lean`), wired into `QOU.lean`.
- **Theorems:** `tlSemisimple_nonvanishing_quantumDim`, `tlSemisimple_wenzl_denom_invertible`, `tlSemisimple_cell_gram_nondegenerate`, `tlSemisimple_iff_all_quantumDims_unit`, `tlFailureAtRootOfUnity_not_semisimple` — proving Wenzl's semisimplicity criterion for `TL_n(d)` iff `∏_{k=1}^n [k]_q ∈ Rˣ` (and non-semisimplicity at root of unity `[p]_q = 0`).
- **Status:** Kept at `in-progress` pending Merge Manager merge and full dependency verification.
