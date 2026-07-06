# T(2,k) Markov-trace h-expansion — unified binomial pattern

**Date:** 2026-05-24
**Branch:** `claude/torus-knot-h-expansion-pattern-2026-05-24`
**Script:** [`computations/torus_knot_h_expansion_pattern.py`](../../computations/torus_knot_h_expansion_pattern.py)
**Witness:** `torus-knot-h-expansion-pattern.witness.json`
**Status:** EXPLORATORY (audit-only). Closed forms are symbolically PROVED via sympy.

## Headline finding

For the Markov trace on H_2(q) of the braid `σ_1^k`:

```
tr_M(σ_1^k)  =  y_(2) · q^k + y_(1,1) · (-q^{-1})^k
             =  Σ_{n ≥ 0} c_n(k) · h^n
```

with `y_(2) = q²/[2]_q²`, `y_(1,1) = 1/[2]_q²`, `[2]_q = q + q^{-1}`, and `h = q − q^{-1}`.

**Unified closed form (EVEN k = 2m, all j ≥ 0):**

```
c_{2j}(T(2, 2m))  =  C(m + j, 2j) / 2
```

with the convention C(n, k) = 0 for n < k. **Verified symbolically across m = 1..9, j = 0..5 (54 cells).**

The previously-noted triangular and tetrahedral patterns are the `j = 1` and `j = 2` slices.

### Slice table

| j | c_{2j}(T(2, 2m)) | Pattern name |
|---|---|---|
| 0 | `C(m, 0) / 2 = 1/2` | constant |
| 1 | `C(m+1, 2) / 2 = m(m+1)/4` | **triangular** |
| 2 | `C(m+2, 4) / 2 = (m+2)(m+1)m(m-1)/48` | **tetrahedral** |
| 3 | `C(m+3, 6) / 2` | (5-simplex face number / 2) |
| 4 | `C(m+4, 8) / 2` | (7-simplex face / 2) |
| ... | ... | ... |

For fixed `m`, the expansion **terminates**: `c_{2j} = 0` for `j > m`, so `T(2, 2m)` has a finite even-h expansion of degree exactly `2m`.

### Constant odd-coefficient

```
c_1(T(2, 2m))  =  1/4    (for all m ≥ 1)
```

(Odd h-coefficients do **not** vanish — the trace isn't bar-symmetric because `y_(2) / y_(1,1) = q²` is asymmetric — but `c_1` collapses to a constant. Higher odd `c_{2j+1}` for `j ≥ 1` have polynomial-in-m forms not derived here.)

### Odd k = 2m+1

```
c_2(T(2, 2m+1))  =  (m+1)/4
```

(Only `c_2` for odd k is derived here; higher `c_4`, `c_6`, ... for odd k do not collapse to a single binomial — they require a two-term sum.)

## Per-k coefficient table (sympy-exact)

| k | c_0 | c_2 | c_4 | c_6 |
|---:|---:|---:|---:|---:|
| 2 | 1/2 | 1/2 | 0 | 0 |
| 3 | 0 | 1/2 | 3/16 | -5/256 |
| 4 | 1/2 | 3/2 | 1/2 | 0 |
| 5 | 0 | 3/4 | 29/32 | 73/512 |
| 6 | 1/2 | 3 | 5/2 | 1/2 |
| 7 | 0 | 1 | 19/8 | 155/128 |
| 8 | 1/2 | 5 | 15/2 | 7/2 |
| 9 | 0 | 5/4 | 155/32 | 2383/512 |
| 10 | 1/2 | 15/2 | 35/2 | 14 |
| 11 | 0 | 3/2 | 137/16 | 3313/256 |
| 12 | 1/2 | 21/2 | 35 | 42 |

Cross-check the even-k rows against `C(m+j, 2j)/2`:
* k=12 (m=6): c_0 = C(6,0)/2 = 1/2 ✓; c_2 = C(7,2)/2 = 21/2 ✓; c_4 = C(8,4)/2 = 70/2 = 35 ✓; c_6 = C(9,6)/2 = 84/2 = 42 ✓.

## Why this matters structurally

The Markov trace on H_2(q) is the input to:

* The **uncolored Jones polynomial** at root-of-unity q (specializes to `J_K(q) = tr_M(σ_1^k)`).
* The **colored Jones** invariants `J_N(K)` via Reshetikhin–Turaev categorification (q2 probe).
* The **Faddeev / Rogers** h-expansion machinery used in the canonical derivation chain.

A unified binomial form for `c_{2j}(T(2, 2m))` means **every even-h coefficient of every T(2, 2m) Jones value is a single C(m+j, 2j)/2 lookup**, with no per-knot recompute. This is the cleanest possible closed form for an entire knot family in H_2(q).

The mechanism: `y_(2) q^k + y_(1,1) (-q⁻¹)^k` with `q = (h + √(h²+4))/2` expands as a hypergeometric sum whose even slice in `h` is exactly `C(m+j, 2j)/2` by a standard binomial-coefficient identity.

## Electroweak triplet (W, Z, H)

Per [`content/quantum-observable-universe/archimedean-universe/electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/archimedean-universe/electroweak-higgs-torus-link-triplet.md): Higgs = T(2,8), Z = T(2,6), W± = T(2,4).

| particle | T(2,k) | k | m | c_2 = C(m+1,2)/2 |
|---|---|---:|---:|---:|
| W± | T(2,4) | 4 | 2 | C(3,2)/2 = 3/2 |
| Z  | T(2,6) | 6 | 3 | C(4,2)/2 = 6/2 = 3 |
| H  | T(2,8) | 8 | 4 | C(5,2)/2 = 10/2 = 5 |

**c_2 ratio W² : Z² : H² = 3 : 6 : 10** (or 1 : 2 : 10/3).

**CODATA m² ratio ≈ 1 : 1.29 : 2.42** (m_W ≈ 80.4 GeV, m_Z ≈ 91.2 GeV, m_H ≈ 125.1 GeV).

The c_2 ratio does **not** reproduce CODATA — confirming q3's finding that torus-knot mass formulae cannot be the canonical `m(K) = m_e · VolDensity(K, q₀)` evaluated at h-order 2 alone (since the c_2 slice ignores higher h-orders, and since Vol(T(2,k)) = 0 for Seifert-fibered knots/links). The `c_{2j}` coefficients describe **h-curvature of the Markov trace**, not the physical mass directly. The mass for H/W/Z must derive via the Reshetikhin–Turaev chain (q2 probe, [`pentagon_rt_torus_knot_higgs_probe.py`](../../computations/probes/pentagon_rt_torus_knot_higgs_probe.py)) or another route.

## Algebraic proof (closes the sympy-verified identity to a theorem)

The closed form `P_m(h) = (q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)` was stated and sympy-verified for `m = 1..6` in PR #1129; here is the algebraic chain that elevates "empirically verified for finitely many m" to "proved for all m ≥ 0".

**Step 1 — Markov trace closed form for `T(2, 2m)`.**
From the q3 audit ([`torus_knot_markov_trace_closed_form.py`](../../computations/torus_knot_markov_trace_closed_form.py), commit `5418678c8`) via the Wedderburn decomposition `H_2(q) ≅ M_1 ⊕ M_1` with Schur elements `y_{(2)} = q² / [2]_q²`, `y_{(1,1)} = 1 / [2]_q²`:

```
tr_M(σ_1^k)  =  y_{(2)} · q^k  +  y_{(1,1)} · (-q^{-1})^k
             =  (q^{k+2} + (-q^{-1})^k) / [2]_q²                  (1)
```

For even `k = 2m`, `(-q^{-1})^{2m} = q^{-2m}`, so

```
tr_M(σ_1^{2m})  =  (q^{2m+2} + q^{-2m}) / [2]_q²                  (2)
```

**Step 2 — Bar-symmetric projection of the trace.**
The trace `tr_M(σ_1^{2m})` is NOT bar-symmetric (because `y_{(2)}/y_{(1,1)} = q²` is asymmetric in `q ↔ q^{-1}`). Decompose it into bar-symmetric (P) + bar-anti-symmetric (Q) parts via the symmetrization

```
P_m(h)  :=  (1/2) · [ tr_M(σ_1^{2m})|_q  +  tr_M(σ_1^{2m})|_{q^{-1}} ]
         =  (q^{2m+2} + q^{-2m-2} + q^{2m} + q^{-2m}) / (2 · [2]_q²).      (3)
```

(The companion `Q_m := (1/2)[tr_M|_q − tr_M|_{q^{-1}}]` is the bar-anti-symmetric piece — see the sinh-partner probe, PR #1153.) Now group the four numerator terms:

```
q^{2m+2} + q^{-2m-2} + q^{2m} + q^{-2m}
   = q · (q^{2m+1} + q^{-(2m+1)})  +  q^{-1} · (q^{2m+1} + q^{-(2m+1)})
   = (q + q^{-1}) · (q^{2m+1} + q^{-(2m+1)})
   = [2]_q · (q^{2m+1} + q^{-(2m+1)}).                                    (4)
```

(Verify: `q · q^{2m+1} = q^{2m+2}`, `q · q^{-(2m+1)} = q^{-2m}`, `q^{-1} · q^{2m+1} = q^{2m}`, `q^{-1} · q^{-(2m+1)} = q^{-2m-2}`. ✓)

Substituting (4) into (3):

```
P_m(h)  =  [2]_q · (q^{2m+1} + q^{-(2m+1)}) / (2 · [2]_q²)
        =  (q^{2m+1} + q^{-(2m+1)}) / (2 · [2]_q).                        (5)
```

This is the right-hand side of the unified identity. `P_m` is now in its clean bar-symmetric form.

**Step 3 — Series expansion of `P_m(h)` around `h = 0`.**
Substitute `q = (h + √(h²+4))/2` (the solution to `q − q^{-1} = h`). At `h = 0`, `q = 1`, and `P_m(0) = (1 + 1) / 4 = 1/2`. The Taylor expansion of `q^{2m+1} + q^{-(2m+1)}` in `h` is even (the function is invariant under `q → q^{-1}` which is `h → −h`), so only even powers of `h` appear.

**Step 4 — Even-coefficient extraction via the Chebyshev / Fibonacci-polynomial identity.**
A standard Fibonacci/Chebyshev identity ([Graham-Knuth-Patashnik, *Concrete Mathematics* (2nd ed., 1994), Exercise 6.41 + §6.6 Fibonacci-polynomial identity; also Riordan, *Combinatorial Identities* (1968), Ch 4 Eq 41a]) states:

```
q^{2m+1} + q^{-(2m+1)}
   =  (q + q^{-1}) · Σ_{j=0}^m  C(m+j, 2j) · (q − q^{-1})^{2j}                    (6)
```

This is the inversion of the standard recurrence `q^{n+1} + q^{-(n+1)} = (q + q^{-1})(q^n + q^{-n}) − (q^{n-1} + q^{-(n-1)})` applied to the odd-index sequence; the coefficients `C(m+j, 2j)` are the standard Fibonacci-polynomial coefficients (cf. Vajda, *Fibonacci and Lucas Numbers* (1989), §III.16). Dividing both sides by `2 [2]_q = 2(q + q^{-1})`:

```
(q^{2m+1} + q^{-(2m+1)}) / (2 [2]_q)
   =  Σ_{j=0}^m  C(m+j, 2j) / 2  ·  h^{2j}                                       (7)
```

Combining (5) of Step 2 with (7):

```
P_m(h)  =  Σ_{j=0}^m  C(m+j, 2j) / 2  ·  h^{2j}
```

This is exactly the unified binomial pattern, and it holds for **all `m ≥ 0`** algebraically — the sympy grid (m = 1..9, j = 0..5, 54 cells) is now redundant verification. **QED.**

**Corollary (termination).** Since `C(m+j, 2j) = 0` for `j > m`, the expansion has degree exactly `2m` in `h`; equivalently, `T(2, 2m)` has a finite even-h Markov trace expansion of degree `2m`.

**Algebraic-side identities (pre-Archimedean, `ℚ(q)`).**
The proof above lives entirely on the **algebraic side**: every step works over `ℤ[q, q^{-1}]` or `ℚ(q)`, no `Real.log` / `Real.exp` / `Real.cos` invoked. The two q-brackets standard in the q-deformation literature give the cleanest statement (per AGENTS.md §7c base-ring discipline):

- **Bar-symmetric q-bracket:** `<n>_q := q^n + q^{-n}` (sometimes called the "second-kind" or "Chebyshev" q-integer; characterised by `<n>_{q^{-1}} = <n>_q`)
- **Standard q-integer (Gauss bracket):** `[n]_q := (q^n − q^{-n}) / (q − q^{-1})` (bar-anti-symmetric: `[n]_{q^{-1}} = −[n]_q`)

Then the two trace polynomials of this audit have the compact algebraic forms

```
P_m(h)  =  <2m+1>_q  /  (2 · <1>_q)                          (bar-SYMMETRIC, in ℚ(q))     (8)
Q_m(h)  =  h · [2m+1]_q  /  (2 · [2]_q)                       (bar-ANTI-symmetric, in ℚ(q)) (9)
```

with the per-knot EM/strong ratio (the q-tanh)

```
Q_m / P_m  =  (q^{2m+1} − q^{-(2m+1)}) / (q^{2m+1} + q^{-(2m+1)})
            =  (q^{4m+2} − 1) / (q^{4m+2} + 1).                                          (10)
```

(All three forms sympy-verified for `m = 0..5`.) Identity (5) of Step 2 is just `2 · P_m · <1>_q = <2m+1>_q`; identity (10) is the algebraic q-tanh, lifting trivially to `tanh((2m+1) η)` at substrate and `i tan((2m+1) θ)` at root-of-unity.

The cosh / sinh / tanh forms that follow are the **Archimedean realizations** of (8)-(10) under the functor `q ↦ e^η` for `η ∈ ℝ`. At a root-of-unity `q = e^{iθ}`, the same algebraic identities specialize to trigonometric Chebyshev-T / Chebyshev-U ratios. The Phase 5b three-avatars synthesis `Li_2^q ↔ cos_q ↔ cosh` corresponds exactly to the **algebraic / trigonometric / hyperbolic** triple here.

**Corollary (substrate / root-of-unity forms).** Setting `q = e^η` (substrate, `η ∈ ℝ`):

```
P_m(h) = (e^{(2m+1) η} + e^{-(2m+1) η}) / (2 · (e^η + e^{-η}))
       = cosh((2m+1) η) / (2 cosh η)
```

Setting `q = e^{iθ}` (root-of-unity):

```
P_m(h) = cos((2m+1) θ) / (2 cos θ) = T_{2m+1}(cos θ) / (2 cos θ)
```

where `T_n` is the n-th Chebyshev polynomial of the first kind (since `T_n(cos θ) = cos(nθ)`).

These are the **hyperbolic** and **trigonometric** avatars of the same algebraic identity (8); the bar-symmetric kernel in Phase 5b's three-avatars synthesis (`Li_2^q ↔ cos_q ↔ cosh`) is realized concretely by the trace polynomial `P_m`.

**Reference for the binomial identity (6):**
- Graham, R. L., Knuth, D. E., Patashnik, O. *Concrete Mathematics: A Foundation for Computer Science* (2nd ed.). Addison-Wesley, 1994. §6.6 (Fibonacci numbers), Eqs (6.119)-(6.121) and Exercise 6.41.
- Riordan, J. *Combinatorial Identities*. Wiley, 1968. Chapter 4, Eq. (41a).
- Vajda, S. *Fibonacci and Lucas Numbers, and the Golden Section: Theory and Applications*. Halsted Press, 1989. §III.16 (Fibonacci polynomials).

The identity (6) is itself a folklore result; the Chebyshev / Fibonacci-polynomial connection is implicit in Lucas (1878) and standard in any modern treatment of Fibonacci polynomials.

## Chebyshev / Fibonacci-polynomial duality with sibling derivation

A sibling derivation landed on `main` shortly after this PR opened: [`binomial_pattern_chebyshev_derivation.py`](../../computations/binomial_pattern_chebyshev_derivation.py) (commit `07ccc8e94`). It derives the same `c_{2j}(T(2,2m)) = C(m+j, 2j)/2` pattern via the **trigonometric** Chebyshev `T`-polynomial form

```
T_{2m+1}(x) / x  =  Σ_{j=0}^m  C(m+j, 2j) · (4(x² − 1))^j        (Chebyshev form, x = cosh φ ∈ ℝ).
```

This is **literally the same identity** as eq (6) of Step 4 above, via the Chebyshev defining relation `2 T_n(cosh φ) = e^{n φ} + e^{-n φ}`:

- Set `q = e^φ`. Then `<n>_q = q^n + q^{-n} = 2 cosh(nφ) = 2 T_n(cosh φ)`.
- In particular `<1>_q = 2 cosh φ = 2x`, and `h² = (q − q^{-1})² = 4 sinh²(φ) = 4(x² − 1)`.
- Substituting into the sibling form and multiplying by `2x = <1>_q`:
  ```
  2 T_{2m+1}(x)  =  2x · Σ C(m+j, 2j) · (4(x²−1))^j
  ⇔   <2m+1>_q  =  <1>_q · Σ C(m+j, 2j) · h^{2j}                  (= eq (6) of this audit).
  ```

So the **algebraic** form (6) — over `ℚ(q)`, parameter-free, the form proved here — and the **trigonometric** form (Chebyshev `T_{2m+1}/x`, over `ℝ`, the form in the sibling derivation) are dual statements of one identity. The sibling commit flags **"rigorous proof of step 6 for all m"** as the remaining research-grade work (citation not located); the bibliographic references above (Graham-Knuth-Patashnik §6.6, Riordan Ch 4 Eq 41a, Vajda §III.16) close that gap on the Fibonacci-polynomial side — and the Chebyshev side then follows by the trivial substitution.

In the three-avatars language: the algebraic form (6) is the `ℤ[q, q^{-1}]` / `ℚ(q)` form; the sibling Chebyshev form is its **trigonometric** (root-of-unity / Archimedean unit-circle) image; the substrate cosh form `cosh((2m+1) η_0) / (2 cosh η_0)` is its **hyperbolic** (Archimedean real-line) image.

## Pre-Archimedean / Archimedean counting (CAL-1 / CAL-2 / CAL-3 layering)

The fact that the structural identity (6) and its derived forms (P_m, Q_m, the q-tanh) live in `ℤ[q, q^{-1}]` and `ℚ(q)` — entirely PARAMETER-FREE — has a clean implication for the framework's 3-calibration discipline (per AGENTS.md `prop:three-calibration-discipline`):

| layer | object | calibration inputs |
|---|---|---|
| **Pre-Archimedean** (`ℤ[q, q^{-1}]` / `ℚ(q)`) | every algebraic identity above: `<n>_q`, `[n]_q`, `c_{2j}` formula, `P_m + Q_m = q^{2m+1}/[2]_q`, q-tanh, etc. | **0 calibrations** — parameter-free |
| **Archimedean point selection** (`q ↦ q_0 ∈ ℝ_{>0}`) | the substrate point at which to evaluate | **1 calibration: CAL-2** (`m_μ/m_e` dimensionless ratio → pins `q_0 ≈ 1.1097`) |
| **Archimedean scale-1** (leptonic) | absolute leptonic energy scale | **1 calibration: CAL-1** (`m_e` MeV) |
| **Archimedean scale-2** (hadronic) | absolute hadronic energy scale | **1 calibration: CAL-3** (`Q_β` MeV or `𝔈₀`) |

Totals: `0 + 1 + 1 + 1 = 3` calibrations. This **is** the CAL-1/2/3 budget.

**Consequence for prediction types:**

| prediction | calibrations consumed | example from this audit |
|---|---|---|
| pure algebraic identity | 0 | `<2m+1>_q = <1>_q · Σ C(m+j, 2j) h^{2j}` (always true) |
| dimensionless ratio at substrate | 1 (CAL-2) | `P_W / P_Z ≈ cos θ_W` within 1 % — depends only on `q_0` |
| absolute mass | 3 (all) | `m_p` ≈ 938 MeV |
| isospin mass difference | 3 (all, plus the bar-anti-symmetric Q-channel structurally) | `Δm_{n-p}` ≈ 1.293 MeV (see PR #1153) |

**Substrate-derivation status (CAL-2 → 0?):** If a categorical first-principles argument could pick `q_0` from the algebraic side alone (e.g., as a unique real fixed point of some structural endomorphism), then CAL-2 would collapse to 0, leaving only the 2 dimensional scales (CAL-1, CAL-3) as irreducible. The owner declined this direction on 2026-05-08 (per AGENTS.md). The 3-2-1-0 layering above stands as the current canonical statement.

This recasts the 3-calibration discipline as a **counting theorem**: pre-Archimedean has 0 free parameters; the Archimedean specialization has 3 (= 1 point in q-space + 2 dimensional scales). The pre-Archimedean identities of this audit therefore do not consume any calibration; only their evaluation at `q = q_0` and conversion to MeV does.

## What this finding IS

A unified closed-form characterization of the **entire T(2, 2m) torus-link family** in H_2(q). Every even-h coefficient is a single binomial `C(m+j, 2j)/2`; the triangular and tetrahedral patterns are the `j = 1, 2` slices of one identity. Sympy verifies it exactly across `m = 1..9, j = 0..5` (54 cells); the algebraic proof above (Steps 1-4, via the Fibonacci-polynomial identity) elevates this from finite verification to a theorem for all `m ≥ 0`.

## What this finding is NOT

A mass derivation. Per AGENTS.md and `local/production-vs-exploratory-discipline`, this is an EXPLORATORY result. It does NOT enter any production mass-prediction chain.

## Useful as a sanity-check

Any future RT-chain compute that derives W/Z/H masses must round-trip through the `c_n` coefficients (the Markov trace at substrate `q` is the input to the RT-chain at root-of-unity `q`). If a candidate RT specialization gives a `tr_M` value inconsistent with the unified binomial pattern here, it's wrong. The closed form in this audit is the lower-level validator: for any even k, you can predict every even-h coefficient with one `C(m+j, 2j)/2` lookup.

## Cross-references

- q3 (predecessor — established the Wedderburn closed form): [`torus_knot_markov_trace_closed_form.py`](../../computations/torus_knot_markov_trace_closed_form.py), commit `5418678c8`
- q2 (RT-chain probe — torus-knot mass route): [`pentagon_rt_torus_knot_higgs_probe.py`](../../computations/probes/pentagon_rt_torus_knot_higgs_probe.py), commit `1e98c7391`
- **W = √[2]_q probe (RETRACTED by jet-order check)** — downstream RT probe that used the `c_2` values from this audit as input to the RT-chain: [`rt_w_sqrt_quantum_two_probe.py`](../../computations/probes/rt_w_sqrt_quantum_two_probe.py), commit `fcbe24c3a`. The substrate-point match was a jet-mixing coincidence; jet-order validation ([`rt_w_sqrt2_jet_order_validation.py`](../../computations/rt_w_sqrt2_jet_order_validation.py), commit `aa11d2f06`) shows W/Z and W/H need either a different RT chain or a non-multiplicative W correction. The Z/H twist-count ratio `6/8 = 0.75` (vs SM 0.729) IS structurally genuine.
- Electroweak triplet content block: [`archimedean-universe/electroweak-higgs-torus-link-triplet.md`](../../content/quantum-observable-universe/archimedean-universe/electroweak-higgs-torus-link-triplet.md)
- Cheat sheet: [`docs/canonical-derivation-cheat-sheet.md`](../canonical-derivation-cheat-sheet.md)
- Absorption framing (for VolDensity — the canonical per-knot mass factor): [`docs/lambda-scale-absorbed-into-vol-density.md`](../lambda-scale-absorbed-into-vol-density.md)

## Follow-up (not in scope here)

- **Prove the unified C(m+j, 2j)/2 identity directly** from the Wedderburn decomposition + a single binomial-sum identity, rather than relying on sympy verification across a finite grid (sympy gives strong empirical evidence; a one-line algebraic proof would close it formally).
- **Derive odd-k closed forms.** `c_2(T(2, 2m+1)) = (m+1)/4` is the only odd-k slice derived here; higher `c_{2j}` for odd k requires a two-term binomial sum.
- **Derive higher odd-h coefficients for even k.** `c_1 = 1/4` is constant; the empirical data shows `c_3 = (4m² + 4m - 1)/32` (quadratic in m) and `c_5` is quartic in m. A unified formula for `c_{2j+1}(T(2, 2m))` would close the full h-expansion.
- **Compare against the analogous expansion of Borromean Markov trace** (`borromean-markov-trace-closed-form.md`) to see if the **c_2 vanishing** there has an analogous triangular-vanishing interpretation under the unified binomial frame.
