# The ≥3-row sign crossing is A-DEPENDENT, ⁴He was never compute-limited, and the block overtake is now Lean-proved

**Date:** 2026-08-08 · **Branch:** `claude/deltalambda-signcross-followups-2026-08-08` · **PR #4832**
**Bean:** `qou-prjo` (stays **OPEN** — nothing here closes the magnitude)
**Predecessor:** #4829 / [`2026-08-08-deltalambda-threerow-sign-crossing-probe.md`](2026-08-08-deltalambda-threerow-sign-crossing-probe.md)

| unit | probe | witness |
|---|---|---|
| **2** | [`threerow_crossing_a_dependence_probe.py`](../../computations/deltalambda/threerow_crossing_a_dependence_probe.py) | `threerow-crossing-a-dependence.witness.json` |
| **1** | [`threerow_4he_completion_probe.py`](../../computations/deltalambda/threerow_4he_completion_probe.py) + kernel [`threerow_chi_sparse.py`](../../computations/deltalambda/threerow_chi_sparse.py) | `threerow-4he-completion.witness.json` |
| **3** | [`ThreeRowSignCrossing.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ThreeRowSignCrossing.lean) | — (`lean`-direct exit 0) |

`free_parameters = 0` throughout. Experimental **proton** anchor
(`q_parameter.Q ≈ 1.1099785827513808`, owner directive 2026-08-07); `y_λ` via the
LIVE closed form `schur_principal_mpmath.y_lambda_at_q0_mpmath`, never the
muon-serving `wedderburn_jones_markov.y_lambda_at` cache. Layer-pure: `y_λ(q)`
and `χ^λ(β;q)` are always evaluated at the **same** running `q`. AME is never
used — not as an input and not as a target.

---

## 0. Headline

The object is #4829's ≥3-row signed trace,

```
F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3}  y_λ(q) · χ^λ(β_K; q) · Δ_λ ,    Δ_λ = (−1)^{n(λ)}·dim V_λ
```

with `Δ_λ` the PROVED value-only weight
(`QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`).

**Two of #4829's conclusions were too weak, and both were correctable by
measurement rather than by argument.**

1. **The deuteron crossing is NOT special — it is A-dependent.** #4829 swept only
   `q ∈ (1, q₀]` and reported "no crossing" for T/³He. That was a correct
   scope-(a) statement about an *interval*, but it conflated two very different
   structural facts. On a beyond-substrate diagnostic ray the n=9 crossing **is
   there**, at `q ≈ 1.4617` (T) and `q ≈ 1.4285` (³He) — just *above* `q₀`.
2. **⁴He was never compute-limited.** #4829's §5 attributed the n=12 wall to a
   missing mpfr Rust kernel. The wall was a dense `np.eye` densifying an
   already-sparse CSR operator. Fixed, the full 70-partition ℓ≥3 character sum
   runs in **~32 s per grid point** in pure Python, and ⁴He **crosses on the
   physical interval**.

**The resulting crossing ladder is NOT monotone in A:**

| isotope | n = 3A | Z, N | F(q→1⁺) | F(q₀) | crossing q | relative to q₀ |
|---|---:|---|---:|---:|---:|---|
| **D** | 6 | 1,1 | +8.05·10⁻⁵ | −0.1950 | **1.05365** | **below** |
| **T** | 9 | 1,2 | −4.06·10⁻⁴ | −2.318 | 1.46170 | *above* (diagnostic) |
| **³He** | 9 | 2,1 | −4.06·10⁻⁴ | −2.806 | 1.42852 | *above* (diagnostic) |
| **⁴He** | 12 | 2,2 | +1.177·10⁻³ | −5.947 | **1.02092** | **below** |

`q₀ ≈ 1.10998` sits **inside** the light-nucleus crossing band, not on one side
of it.

---

## 1. UNIT 2 — the n=9 crossing exists; it is above q₀

### 1.1 Why the extra sweep was the right move

"No crossing on `(1, q₀]`" and "no crossing" are different claims, and only the
first was measured. The distinction matters structurally:

* crossing **absent** at n=9 ⇒ the deuteron flip is an n=6 accident;
* crossing **present above q₀** ⇒ the crossing location is a *function of A*, and
  the substrate modulus is positioned between the light-nucleus crossings.

So the probe sweeps a **diagnostic ray** `q ∈ (1, 4]`.

> ⚠ **BEYOND-SUBSTRATE DIAGNOSTIC — NOT A PHYSICAL CLAIM.** The substrate modulus
> is `q₀ ≈ 1.10998`. No value of `F_K` at `q > q₀` is a prediction of anything.
> The ray exists solely to determine whether the analytic function `F_K` has a
> zero above `q₀`, which is a statement about the *object*, not about physics.
> Every such field in the witness is prefixed `diagnostic_`.

### 1.2 Result

| isotope | crossings on `(1,q₀]` (physical) | crossings on `(q₀,4]` (diagnostic) |
|---|---|---|
| D (n=6) | **1.05365** | 3.41010 |
| T (n=9) | none | **1.46170** |
| ³He (n=9) | none | **1.42852**, 3.21633 |

**Verdict: A-DEPENDENT, not special.** The n=9 crossing is real and sits just
above the anchor.

Every isotope has further sign changes far out on the ray (D at 3.4101, ³He also
at 3.2163). Those are recorded for completeness and carry no reading whatsoever —
`F_K` grows super-exponentially out there. The load-bearing comparison is the
**first** crossing and which side of `q₀` it falls on.

### 1.3 The n=9 mechanism is *not* the clean n=6 two-block overtake

At n=6 the crossing is a two-block dominance exchange with a clean change of
dominant block: `(4,1,1)` (Δ = −10) → `(3,2,1)` (Δ = +16). At n=9 the dominant
block does **not** change across the crossing — for T it is `(5,2,1,1)` on both
sides, for ³He it is `(5,3,1)` on both sides — and the total is a near
cancellation among several large opposite-sign terms:

| isotope | q | total | leading term | leading/total |
|---|---:|---:|---:|---:|
| T | 1.4178 (below cross) | −1.52·10² | `(5,2,1,1)` +1.298·10³ | 8.5× |
| T | 1.5055 (above cross) | +8.00·10² | `(5,2,1,1)` +8.875·10³ | 11.1× |
| ³He | 1.3857 (below cross) | −2.37·10² | `(5,3,1)` −1.091·10³ | 4.6× |
| ³He | 1.4714 (above cross) | +1.33·10³ | `(5,3,1)` −5.342·10³ | 4.0× |

A 4–11× cancellation is still ~13 orders of magnitude above the f64 noise floor,
so the located crossings are not precision artifacts. But the *structural reading*
differs: the n=6 crossing is a two-block overtake, the n=9 crossing is a
multi-block cancellation. Only the former is what the Lean of UNIT 3 formalises.

### 1.3-bis Three distinct regimes — the deuteron mechanism is not *the* mechanism

Adding ⁴He (§2.4) completes the picture. Measuring the leading ℓ≥3 term against
the total at q₀:

| n | leading/total at q₀ | regime |
|---|---:|---|
| 6 | ~1.2× | **two-block overtake** — one block essentially sets the total |
| 9 | 4–11× | **multi-block cancellation** — the total is a small residue of large opposite-sign terms |
| 12 | **0.34×** | **broad constructive accumulation** — the total *exceeds* its largest term; many blocks add coherently |

These are qualitatively different, and it matters for how #4829 §2 should be read.
The `(4,1,1) → (3,2,1)` overtake is a **correct description of n = 6 and of n = 6
only**. It should not be carried over as the mechanism behind the ⁴He or n=9 sign,
and the Lean lemma of UNIT 3 — which models exactly that two-block exchange — is
correspondingly an n=6 statement. Any closure attempt that generalises the
deuteron block story to larger A is generalising the wrong object.

### 1.4 A structural difference visible in Δ_λ alone

The `|Δ_λ|`-ordering of the ℓ≥3 stratum differs qualitatively between n=6 and n=9:

| n | ℓ≥3 count | max\|Δ\| | top of the stratum |
|---|---:|---:|---|
| 6 | 7 | 16 | `(3,2,1)` Δ = **+16** — *unique*, positive |
| 9 | 25 | 216 | `(4,3,1,1)` Δ = **+216** and `(4,2,2,1)` Δ = **−216** — a **± cancelling pair** |

At n=6 a single partition carries the largest weight and can therefore win
outright; at n=9 the top magnitude is shared by an equal-and-opposite pair, which
is consistent with the observed cancellation-driven crossing. This is an
**observation about the Δ_λ combinatorics**, not a derivation of the crossing
location.

---

## 2. UNIT 1 — ⁴He: the compute limit was an implementation artifact

### 2.1 The misdiagnosis

#4829 §5 recorded:

> ⁴He (n=12) — documented SANDBOX COMPUTE LIMIT … irrep dims in the thousands,
> GB-scale matrices … exceeds >4 min/grid point with no mpfr kernel. Re-run with
> `QOU_INCLUDE_4HE=1` on a host with `pyhecke_native`.

`build_seminormal_matrices` **already** returns scipy CSR whenever `dim > 500` —
each Hoefsmit matrix is block-diagonal with 1×1 and 2×2 blocks, hence ≤ 2
nonzeros per row. The consumer then built each braid-word letter as

```python
M = float(c) * sig[g] + float(d) * np.eye(dim)      # ← dense identity
```

which (i) materialises a dense identity — 474 MB at `dim = 7700` — and
(ii) **densifies the sparse σ back to a full matrix**, so `prod = prod @ M` costs
`O(dim³)` per letter. Over the ℓ≥3 stratum of 12, `Σ dim³ = 2.1·10¹²` *per word
letter*, with word length `L = 47`. That is the "GB-scale / >4 min per point".

### 2.2 The fix — exact, not an approximation

[`threerow_chi_sparse.py`](../../computations/deltalambda/threerow_chi_sparse.py):

1. keep the identity sparse (`scipy.sparse.identity`), so each letter
   `M_j = c_j σ_{g_j} + d_j I` stays CSR with ≤ 2 nonzeros per row;
2. never form the dense product — accumulate `Tr(∏_j M_j)` column-batch-wise, by
   applying the word in reverse to batches of identity columns and reading the
   diagonal. `O(L · dim²)` time, `O(dim · B)` memory.

`Σ dim² = 4.8·10⁸`, so the whole n=12 character sum is ~10¹⁰ flops. **Largest
n=12 partition: 3.5 s. Full 70-partition sum: ~32 s per grid point.** No native
kernel; no truncation.

This is an exact reorganisation of the *same* f64 arithmetic, gated two ways:

* **kernel gate** — bit-level against #4829's dense `chi_atom` on 8 n=6/n=9
  partitions: **max rel diff 1.44·10⁻¹⁵** (f64 epsilon);
* **convention gate** — `χ^λ(β_4He;q₀)` vs the canonical
  `atom-chi-rust-4he.witness.json`: **max rel diff 3.2·10⁻⁶**, same order as
  #4829's 1.5·10⁻⁶ for D/T (residual f64 Hoefsmit-seminormal accumulation).

### 2.3 No truncation was taken

The brief permitted a dominant-`|Δ_λ|` truncation *only* with a rigorous bound on
the neglected remainder. No such bound is available — the n=9 decomposition above
shows the total can sit an order of magnitude below the leading term, so
discarding sub-leading blocks is exactly the regime where truncation is unsafe.
**All 70 ℓ≥3 partitions of 12 are summed.** The optimisation removed the need for
the trade entirely.

### 2.4 Result

⁴He is `+ → −` on the physical interval, like the deuteron, and its crossing sits
**below** `q₀`:

| q | F_4He(q) |
|---:|---:|
| 1.0001 | +1.1768·10⁻³ |
| 1.00082 | +9.2660·10⁻³ |
| 1.00332 | +3.2684·10⁻² |
| 1.00668 | +5.2799·10⁻² |
| 1.01346 | +5.5008·10⁻² |
| 1.02710 | −9.0561·10⁻² |
| 1.05460 | −1.0121 |
| **q₀ = 1.109979** | **−5.9469** |

**Crossing on `(1, q₀]`: q = 1.0209229** (bisected, f64 resolution) — the sign
change is bracketed between q = 1.01346 (F = +5.50·10⁻²) and q = 1.02710
(F = −9.06·10⁻²).

Per-λ decomposition at q₀ (top blocks of the 70-partition sum):

| λ | Δ_λ | term |
|---|---:|---:|
| (8,3,1) | −891 | −1.9983 |
| (7,3,2) | −1925 | −1.8918 |
| (6,3,3) | −1650 | −1.5110 |
| (6,4,1,1) | −3080 | −1.1892 |
| (6,3,2,1) | +5632 | +0.9827 |
| (7,3,1,1) | +2376 | +0.9802 |
| (8,2,2) | +616 | −0.7426 |
| (5,4,2,1) | −5775 | −0.5269 |
| **TOTAL** | | **−5.9469** |

Note the leading term (−1.998) is **smaller** than the total (−5.947): at n = 12
the sign is set by many blocks adding coherently, not by one dominant block. See
§1.3-bis.

On the diagnostic ray above q₀, F_4He changes sign four further times — brackets
`(1.1908, 1.2513)`, `(1.3311, 1.4361)`, `(1.9966, 2.3127)`, `(2.7291, 3.2776)` —
before running away as `−9.5·10²³` at q = 4. Those are beyond-substrate structure
and carry no physical reading; they are recorded only so the ray is described
honestly rather than truncated at the first zero.

**Ray crossings are reported as BRACKETS, not bisected values.** Their location is
not load-bearing — only which side of q₀ the *first* one falls on matters — and at
n = 12 each `F` evaluation costs ~32 s, so bisecting four of them at 30 iterations
consumed >60 min of a 96-min first run to produce ~10⁻¹¹ resolution that the f64
character path cannot support anyway. The probe now brackets them (see
`why_not_bisected` in the witness). Only the physical crossing is bisected, at 18
iterations (~5·10⁻⁸ on a 0.014-wide bracket).

---

## 3. The non-monotone ladder, and one pattern I am NOT claiming

Crossing q against A: **1.05365 (D) → 1.4285/1.4617 (³He, T) → 1.02092 (⁴He)**. Not
monotone. The n=9 pair is the outlier, and the two n=9 crossings are nearly
degenerate with each other while sitting far from both Z=N cases.

The obvious pattern to reach for is isospin: `Z = N` (D, ⁴He) crosses **below**
q₀; `Z ≠ N` (T, ³He) crosses **above**. **I am flagging this and explicitly not
claiming it.** It is four data points forming two pairs, with no derivation
behind it, and the corpus discipline on exactly this kind of small-sample
regularity is the reason to say so out loud rather than to write it into a
conclusion. Distinguishing "isospin symmetry controls the crossing side" from
"two coincidences" needs at least the odd-A/even-A continuation (⁶Li, ⁷Li) — which
the sparse kernel now makes affordable — and a structural reason, neither of which
exists yet.

One genuine and relevant observation: **the character is decisive, not decorative.**
The character-free companion `G(q) = Σ_{ℓ≥3} y_λ(q)·Δ_λ` crosses at 1.0244 (n=6),
2.1089 (n=9) and 1.5974 (n=12) — so for n=12 the character-free weighting puts the
crossing *above* q₀ while the full character object puts it *below*. `χ^λ(β_K;q)`
is what moves the ⁴He crossing across the anchor. Any route that models the ≥3-row
sign from the `y_λ` weighting alone will get n=12 wrong.

---

## 4. UNIT 3 — the block overtake, Lean-proved sorry-free

[`ThreeRowSignCrossing.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/ThreeRowSignCrossing.lean),
namespace `QOU.BraidsAndKnots`, base ring `ℝ` (genuinely archimedean per §7c —
both results use the order structure and the IVT).

| theorem | content |
|---|---|
| `sign_crossing_of_block_dominance_exchange` | `F = T₁+T₂+R` continuous, `T₁` positive and dominating the rest at `a`, `T₂` negative and dominating the rest at `b` ⟹ `∃ c ∈ Ioo a b, F c = 0` |
| `crossing_unique_of_strictMonoOn_ratio` | with `T₁ > 0` and the overtake ratio `r = (−T₂)/T₁` strictly monotone, the zero of `T₁+T₂` is **unique** |
| `two_block_neg_iff_ratio_gt_one` | `T₁+T₂ < 0 ↔ r > 1`, i.e. "(3,2,1) has overtaken (4,1,1)" and "the total went negative" are the *same* statement |

The first is the shape of the measured deuteron data (`T₁` = the `(4,1,1)` term,
`T₂` = the `(3,2,1)` term, `R` = the remaining ≥3-row blocks) and is falsifiable:
drop either dominance hypothesis and the conclusion fails. The second is the
formal content of the word *overtake* — `T₂` grows **relative to** `T₁`,
monotonically, hence crosses it exactly once.

**Scope of applicability: n = 6.** By §1.3-bis the two-block dominance picture
holds at n = 6 and does **not** describe n = 9 (multi-block cancellation) or
n = 12 (broad constructive accumulation). The theorems are stated for a *generic*
`T₁, T₂, R` split, so they remain true statements regardless; but the *empirical
premise* that one block dominates the rest is only satisfied by the deuteron. Do
not read them as a general account of the ≥3-row sign.

**Verification.** `lean`-direct against the real Mathlib import cone (restored
oleans, `LEAN_PATH` set to the package build dirs): **exit 0**. `#print axioms` on
all three declarations: `[propext, Classical.choice, Quot.sound]` — **no
`sorryAx`**, no `native_decide`, no axiom or class standing in for a proof.

**What these theorems do NOT say.** They take the per-block dominance data as
*hypotheses*. The `y_λ` and `χ^λ` numbers live in the f64 probe, not in Lean, and
nothing here certifies them. Per AGENTS.md §"Conditional-proved ≠
premise-established", these may be cited as *"a dominance exchange forces a zero"*
and may **not** be cited as evidence that the deuteron numbers are what §1 of
#4829 reports. A fully-numeric Lean instance would need exact rational (or
interval-certified) `y_λ` and `χ^λ` at rational sample q; that is a real
possibility — both are algebraic in q, and Young's *seminormal* form has rational
entries where the symmetric form used by the current code introduces
`b = √(aa'+1)` — but it is not done here, and no scaffolding was landed in its
place.

---

## 5. Scope classification (AGENTS.md §before-declaring-refuted)

* **"The deuteron crossing is special to n=6" — REFUTED, scope-(a)→positive.**
  Not a refutation-by-absence: the n=9 crossings were *located* (bracketed sign
  change of a continuous function + bisection). This is a positive existence
  statement.
* **"⁴He is compute-limited" — REFUTED by construction.** Superseded by a working
  computation, not by an argument.
* **"No crossing on `(q₀, 4]`" statements** (e.g. D) are **scope-(a)**: about the
  swept ray only. No invariant is proved to forbid a zero anywhere, so no
  scope-(b) exclusion is claimed for any isotope.
* **The isospin pattern of §3 is NOT a claim** — recorded as an observation with
  its sample size stated.
* **NOTHING here closes the magnitude.** `F_K` is **value-only** (`Δ_λ` carries no
  extensive magnitude). The super-pairwise extensive term — the actual content of
  bean `qou-prjo` — is untouched, and the pairwise cap
  `QOU.MassTheory.exchangeDet_pow_two_le_four` still stands between this object
  and a binding energy. **Bean `qou-prjo` stays OPEN.**
* **Not the same object as #4817's cumulant window.** The per-isotope q-crossing
  is a statement about one nuclide as q varies; #4817's `(μ₃,μ₄) = (+,−)` window
  is a cross-isotope statement at fixed q. Related, not identical; §3's
  observation that the crossing side varies with A is the reason they should not
  be conflated.

## 6. Precision

`y_λ(q)` is full 50-dps mpmath. `χ^λ(β_K;q)` is f64 (pure-Python Hoefsmit
seminormal; no mpfr Rust kernel in this sandbox — the sparse reorganisation
changes the *cost*, not the precision class). Decisive for the sign questions
asked here: the largest cancellation observed is ~11× (T on the ray), leaving the
totals ~13 orders of magnitude above the f64 noise floor; at q₀ the ⁴He noise
floor is 4.4·10⁻¹⁶ against a total of 5.95. Located crossing q values carry f64
resolution only, which is why ray crossings are reported as brackets (§2.4).

## 7. Compute cost (per the long-compute logging discipline)

| stage | cost |
|---|---|
| n=6, n=9 full sweep + ray + decomposition | ~2 min total |
| n=12 single `F` evaluation (70-partition ℓ≥3 sum) | **~32 s** |
| n=12 largest single partition `(5,3,2,1,1)`, dim 7700 | 3.5 s |
| ⁴He full probe (11 physical + 13 ray + 18 bisect + decomposition) | **~23 min** |

**Bottleneck and the mistake worth recording:** the first ⁴He run took **96 min**,
of which **>60 min** was bisecting four *diagnostic-ray* crossings at 30 iterations
each. That is ~10⁻¹¹ resolution on quantities that are not load-bearing and that
the f64 character path cannot support. The probe now brackets ray crossings and
bisects only the physical one (18 iterations), and memoizes `F`. Same numbers,
~4× less wall clock.

Second cost note: running the UNIT 2 and UNIT 1 probes concurrently on a 4-core
box caused severe BLAS oversubscription — a T (n=9) sweep that takes 15 s alone
took **985 s** under contention, and the UNIT 2 re-run was killed by its own
30-minute `timeout`. Run these serially.

## References

* Predecessor: #4829, [`2026-08-08-deltalambda-threerow-sign-crossing-probe.md`](2026-08-08-deltalambda-threerow-sign-crossing-probe.md)
* Proved `Δ_λ`: `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`, `computations/delta-lambda-witness.json` (value_only)
* LEAD-1 (algebraic ≥3-row cumulant): #4817, [`2026-08-08-threerow-extensive-cumulant-forward-qfree.md`](2026-08-08-threerow-extensive-cumulant-forward-qfree.md)
* LEAD-2 (geometric NA-Stokes): #4818, [`2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md`](2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md)
* Pairwise cap: `QOU.MassTheory.exchangeDet_pow_two_le_four`
* q₀ anchor convention (proton default): AGENTS.md §q₀ anchor (owner 2026-08-07)
