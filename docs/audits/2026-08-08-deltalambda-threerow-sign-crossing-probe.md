# Δ_λ many-body sign: sign(Σ_{ℓ≥3} y_λ(q)·χ^λ·Δ_λ) DOES cross zero on (1,q₀] for the deuteron (q≈1.054), NOT for T/³He

**Date:** 2026-08-08 · **Branch:** `claude/deltalambda-sign-crossing-2026-08-08` · **PR #4829**
**Bean:** `qou-prjo` · **Tier:** analysis / structural probe
**Probe:** [`computations/deltalambda/threerow_sign_crossing_probe.py`](../../computations/deltalambda/threerow_sign_crossing_probe.py)
**Decomp:** [`computations/deltalambda/threerow_sign_crossing_decomp.py`](../../computations/deltalambda/threerow_sign_crossing_decomp.py)
**Witness:** `threerow-sign-crossing.witness.json`

`free_parameters = 0`. Proton anchor (experimental q₀, owner directive 2026-08-07).
Layer-pure. AME never used. This is the convergence-test both #4817 (LEAD-1,
algebraic) and #4818 (LEAD-2, geometric) explicitly pointed at.

---

## 0. The question and the verdict

Both siblings converged: the q₀-FREE combinatorics only *bracket* the AME ratios
with the **wrong sign order**, so the many-body `(+,−)` sign must live in the
**q₀-dependent `y_λ(q)·χ^λ` trace weighting**. #4817 §5 named the exact next unit:

> is the sign of `Σ_{λ⊢k,ℓ≥3} y_λ(q)·χ^λ·Δ_λ` q-dependent, and does it cross zero
> between the combinatorial (q→1) limit and q₀?

**VERDICT (headline).** **YES for the deuteron.** The ≥3-row signed trace
`F_D(q) = Σ_{λ⊢6, ℓ(λ)≥3} y_λ(q)·χ^λ(β_D;q)·Δ_λ` is **positive** just above q=1
(`F_D(1.0001) = +8.05·10⁻⁵`) and **negative** at the substrate
(`F_D(q₀) = −0.1950`), **crossing zero at q ≈ 1.05365** — well inside `(1, q₀)`,
`q₀ ≈ 1.10998`. The sign of the ≥3-row trace is genuinely **q-dependent** and its
value at the substrate is **archimedean-selected**, exactly as #4817 §5 / #4818 §5
hypothesised.

| isotope | n=3A | F(q→1⁺) | F(q₀) | sign | crossing q |
|---|---|---|---|---|---|
| **D** | 6 | **+8.05·10⁻⁵** | **−0.1950** | **+ → −** | **≈ 1.05365** |
| T | 9 | −4.06·10⁻⁴ | −2.318 | − → − | none |
| ³He | 9 | −4.06·10⁻⁴ | −2.806 | − → − | none |
| ⁴He | 12 | — | — | — | **compute-limited** (§5) |

**Character-free companion** `G(q) = Σ_{λ⊢n, ℓ≥3} y_λ(q)·Δ_λ` (full mpmath, no
character): **n=6 also crosses** (at q ≈ 1.02445, sign − → +), n=9 and n=12 do
**not**. So the sign-indefiniteness in q is intrinsic to the ≥3-row `y_λ` weighting
at n=6, and the deuteron character `χ^λ(β_D;q)` re-signs the object but preserves a
(relocated) crossing.

---

## 1. The exact object (pinned from the two audits + the synthesis)

The canonical binding base of `deltalambda-extensivity-gap-synthesis`
(`B_base = m_e·|Σ_λ y_λ χ^λ sgn·dim|`) has summand `y_λ·χ^λ·(sgn·dim)`, and
`sgn_conjugate_parabolic(λ)·dim(λ) = (−1)^{n(λ)}·dim V_λ = Δ_λ` — the PROVED
value-only per-partition weight (`dtEuler_eq_deltaLambda_unconditional`). Restrict
the sum to the **≥3-row stratum** `ℓ(λ) ≥ 3` (#4664: the stratum measured to
*dominate* binding). Object:

```
F_K(q) = Σ_{λ ⊢ 3A, ℓ(λ) ≥ 3}  y_λ(q) · χ^λ(β_K; q) · Δ_λ
```

- **Δ_λ = (−1)^{n(λ)}·dim V_λ** — proved integer, value-only.
- **y_λ(q)** — Wenzl/Jones–Markov weight via the LIVE closed form
  `schur_principal_mpmath.y_lambda_at_q0_mpmath` (**proton anchor**; NOT the
  muon-serving `wedderburn_jones_markov.y_lambda_at` cache — the AGENTS.md
  straddle hazard).
- **χ^λ(β_K; q)** — Hecke character of the color-weighted nuclide braid
  `atom_braid_word_3A(Z,N,q=q)`. This is **q-dependent** (not a fixed classical
  S_n integer: e.g. `χ^{(6)}(β_D;q₀) = 1.5599…`), so the sweep runs **both** y_λ
  and χ^λ at the **same** q. Holding χ^λ at q₀ while running y_λ(q) would be the
  forbidden layer-straddle.

**q₀ pin recorded in the witness:** experimental / proton
(`q_parameter.Q ≈ 1.1099785827513808`), live closed-form y_λ.

**Convention gate.** `χ^λ(β_K;q₀)` reproduces the canonical
`atom-chi-rust-{d,t,3he}.witness.json` values to **max rel 1.5·10⁻⁶** (signs
exact; the residual is f64 Hoefsmit-seminormal accumulation, see §5).

---

## 2. Why the deuteron sign crosses — the structural cause (a 3-row block overtake)

Per-partition term `y_λ·χ^λ·Δ_λ` for the deuteron (ℓ≥3), at the two ends:

| λ | ℓ(λ) | Δ_λ | term(q→1⁺) | term(q₀) |
|---|---|---:|---:|---:|
| **(4,1,1)** | 3 | −10 | **+1.042·10⁻⁴** | +0.04761 |
| **(3,2,1)** | 3 | +16 | −1.60·10⁻⁷ | **−0.23094** |
| (2,2,2) | 3 | +5 | −2.60·10⁻⁶ | −0.01352 |
| (3,1,1,1) | 4 | +10 | −2.08·10⁻⁵ | +0.00336 |
| (2,2,1,1) | 4 | −9 | +3.37·10⁻⁹ | −0.00252 |
| others | | | ≪ | ≪ |
| **TOTAL** | | | **+8.05·10⁻⁵** | **−0.19497** |

The crossing is a clean **competition between the two leading 3-row blocks**:

- near q→1 the total is set by **(4,1,1)** (Δ=−10) with a **positive** term
  (+1.04·10⁻⁴) ⇒ `F_D > 0`;
- as q → q₀ the **(3,2,1)** block (Δ=+16, the largest |Δ_λ| in the ℓ≥3 stratum of
  6) grows ~10⁶× (−1.6·10⁻⁷ → −0.231) while (4,1,1) grows only ~450×, so (3,2,1)
  **overtakes** and drives the total **negative**.

So the archimedean sign at q₀ is `sgn(F_D(q₀)) = sgn(term_{(3,2,1)}) = sgn(+16·y_{(3,2,1)}·χ^{(3,2,1)}) < 0` — the negative comes from `y·χ < 0` on the
top-Δ 3-row block. The crossing is the point where its magnitude overtakes the
(4,1,1) block. This is a **q₀-USE** result (q₀ is an input), never a q₀-derivation
(FOREVER GATED) — legitimate.

---

## 3. Scope classification (honest, per AGENTS.md §before-declaring-refuted)

- **Sub-question "where does the deuteron ≥3-row sign live" — CLOSED (positive).**
  It lives in the **q₀-dependent (archimedean) trace weighting**: the object is
  sign-indefinite in q and the substrate value is selected by the zero-crossing at
  q ≈ 1.054. This confirms #4817 §5 and #4818 §5's localization and is derived, not
  fitted (`free_parameters = 0`).
- **T, ³He (n=9) — scope-(a) negative.** *This object, alone, does not supply a
  sign change on `(1,q₀]` for n=9* — the ≥3-row trace is negative throughout. NOT
  scope-(b): no invariant is proved to forbid a crossing; it simply does not occur
  on the swept interval.
- **NOT a magnitude closure.** `F_K` is **value-only** (Δ_λ carries no extensive
  magnitude; the super-pairwise term stays open — bean `qou-prjo`). This probe
  tests only the **SIGN** of the ≥3-row weighting, not the binding magnitude.

**What is explicitly NOT claimed.** The deuteron per-isotope q-crossing is **not**
the same object as #4817's cross-isotope `(μ₃,μ₄)=(+,−)` cumulant window (that is a
3-body-vs-4-body statement over A, not a per-isotope q-flip). This probe shows the
**per-isotope trace sign is archimedean**; whether the q₀-weighted trace values
reproduce the cross-isotope `(+,−)` cumulant order is a **separate** surviving unit
(§6).

---

## 4. Character-free decomposition (what the y_λ weighting alone does)

`G(q) = Σ_{λ⊢n, ℓ≥3} y_λ(q)·Δ_λ` (drop χ^λ; full 50-dps mpmath):

| n | G(q→1⁺) | G(q₀) | crossing |
|---|---|---|---|
| 6 | −4.56·10⁻⁶ | +1.636·10⁻² | **q ≈ 1.02445** (− → +) |
| 9 | −3.07·10⁻⁵ | −2.291·10⁻² | none |
| 12 | +8.05·10⁻⁵ | +1.801·10⁻² | none |

The **y_λ weighting alone is already sign-indefinite in q at n=6** and crosses; the
deuteron character `χ^λ(β_D;q)` flips the overall sign (G: −→+ vs F_D: +→−) but the
crossing survives. For n=9 the weighting is monotone (consistent with T/³He no
crossing). For n=12 the character-free weighting does not cross — a (partial,
character-free) hint about ⁴He, whose full character object is compute-limited.

---

## 5. Verification status (honest)

- **Python probe:** run to completion; 3 assertions pass; witness emitted
  (`free_parameters=0`, AME unused).
- **Convention gate:** χ^λ(β_K;q₀) vs canonical `atom-chi-rust-*` witnesses,
  **max rel 1.5·10⁻⁶**, all signs exact.
- **Precision:** y_λ(q) is full 50-dps mpmath; χ^λ(β_K;q) is **f64** (pure-Python
  Hoefsmit seminormal `build_seminormal_matrices`; the mpfr Rust kernel
  `pyhecke_native` is unavailable in this sandbox — disk quota — documented, not a
  proof gap). The product is therefore f64-precision. This is **decisive for a SIGN
  question**: both deuteron crossings are bracketed by terms of magnitude
  O(10⁻²)–O(10⁻¹), enormous relative to f64 noise (~10⁻¹⁴). The located crossing q
  carries f64 resolution only (bisection to ~10⁻⁷).
- **⁴He (n=12) — documented SANDBOX COMPUTE LIMIT, not a proof gap.** The f64
  seminormal build for ~60 ℓ≥3 partitions of 12 (irrep dims in the thousands,
  GB-scale matrices) exceeds >4 min/grid point with no mpfr kernel. Re-run with
  `QOU_INCLUDE_4HE=1` on a host with `pyhecke_native`. Mirrors the LEAD-1 (#4817)
  disk-block precedent. n=6 (D) and n=9 (T,³He) fully answer the light-chain
  crossing question.
- **Lean:** none added. A sorry-free lemma would have to prove the two-point sign
  inequality `F_D(q_lo)>0 ∧ F_D(q₀)<0` (or the (3,2,1)-vs-(4,1,1) overtake), which
  requires the numerical character evaluation (f64 / disk-blocked here). Per the
  strict Lean discipline, **no sorry-laden scaffolding was written**; the
  structural cause (§2) is recorded as the honest exit and the formalization is
  left as §6.

---

## 6. Surviving sub-questions (sharp, honest)

1. **Cross-isotope cumulant order.** Does the q₀-weighted trace reproduce #4817's
   `(μ₃,μ₄)=(+,−)` cumulant window when the isotope `F_K(q₀)` values are
   Mayer-inverted over `C(A,k)`? (This probe establishes the per-isotope archimedean
   sign; the cumulant order is the distinct cross-A object.)
2. **⁴He full character object** — fill in the n=12 leg (`QOU_INCLUDE_4HE=1` +
   native kernel).
3. **Formalize the overtake** — a sorry-free Lean lemma that the (3,2,1) 3-row block
   term dominates and is negative at q₀ (needs an mpfr/interval character bound; not
   tractable in this sandbox).

None of these is the open magnitude; the deuteron/light-nucleus binding MAGNITUDE
stays open (bean `qou-prjo`).

## References
- Proved Δ_λ: `QOU.BraidsAndKnots.dtEuler_eq_deltaLambda_unconditional`,
  `computations/delta-lambda-witness.json` (value_only).
- Canonical base object: `deltalambda-extensivity-gap-synthesis.witness.json`.
- LEAD-1 (algebraic ≥3-row cumulant): #4817,
  `2026-08-08-threerow-extensive-cumulant-forward-qfree.md` §5 (the sub-question
  this probe answers).
- LEAD-2 (geometric NA-Stokes): #4818,
  `2026-08-08-nastokes-transverse-surface-curvature-geometric-route.md` §5.
- Scalar-trace null (why the sign is in the *weight* channel): #4619 `tr[A,B]=0`;
  #4818 `listPairing_trace_zero`.
- q₀ anchor convention (proton default): AGENTS.md §q₀ anchor (owner 2026-08-07).
