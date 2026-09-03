# Covariance-kernel epic (`qou-x631`) — M₁>0 gap `qou-k5r5`: the tail half of the effective variance bound is Olver-free and citable; the ingested kernel-rate literature narrows the wall to the bulk

**Date:** 2026-08-29 · **Branch:** `claude/m1-k5r5-bessel-rate-citation-2026-08-29` · **Tier:**
primary-source reading of freshly-ingested literature + exact tail/bulk measurement · **Discipline:**
no fit; no fake closure. This closes the **tail half** of the effective variance bound (rigorous,
cited) and narrows the remaining gap to the **bulk sine-kernel rate**, whose machinery is now
in-corpus. **Epic:** `qou-h315`/`qou-x631`; gap `qou-k5r5`.

## Context

`M₁ > 0` all-n reduces (#5896) to the (CS) margin `m(n) = ρ_P(n) − σ_D(n)/σ_A(n) > 0`. The leading
order is closed (`m∞ = 0.300186 > 0`, exact constants #5969) and the exact finite-n margin is positive
through n=40. The single open step is an **effective variance bound**
> `|V_A(θ)/θ² − v_A| ≤ C_A θ^{−p}` (any `p>0`), where `V_A(θ) = ½Σ_{x≠y}(g(x)−g(y))² J(x,y;θ)²`,
`g = G_A` the content-charge weight, `J` the discrete Bessel kernel of the BOO Plancherel descent DPP.

The prior audit (`…-k5r5-the-missing-citation-is-a-kernel-rate.md`) established that the corpus then
held the kernel convergence only as a **rate-free limit** (BOO Thm 3). The owner then ingested 10
papers (commit `f45f79c8`, → `library/` this PR). Reading them changes the status.

## Result 1 — the TAIL half is Olver-free and now *citable* (the requested step (a))

Split the variance at the spectral edge, `x_cut(K) = 2√θ + K θ^{1/6}`:
`V_A = BULK(|x|,|y| ≤ x_cut) + TAIL(|x| > x_cut or |y| > x_cut)`.

**Johansson 2001 (`library/arxiv-math-9906120v3`), Lemma 3.9 (eq. 3.41)** gives the explicit classical
Bessel bound, no Olver uniform asymptotics required: for `x = 2√α + ξα^{1/6}`,
> `|J_x(2√α)| ≤ C α^{−1/6} exp(−¼ min(¼α^{1/6}, |ξ|^{1/2}) |ξ|)`,
i.e. super-exponential decay past the edge (`~ exp(−¼ξ^{3/2})` for `ξ < α^{1/3}/16`). Each kernel entry
`J(x,y) = √θ(J_x J_{y+1} − J_{x+1}J_y)/(x−y)` carries such a factor, while the weight
`(g(x)−g(y))²` is only **polynomial** (`g_A(k) = ±k(k+1)/2`). Super-exponential decay beats any
polynomial, so
> `TAIL(K) ≤ poly(θ) · exp(−¼ K^{3/2}) = o(θ^{−A})` for every `A`, once `K ~ (log θ)^{2/3}`.

Hence the tail is negligible against the `θ^{−1}` remainder, and **the effective bound reduces to the
BULK** (`|x|,|y| ≤ x_cut`) alone. This is exactly the reduction requested: the wall is now the bulk
sine-kernel rate only.

**Measured** (`wlambda_covariance_epic_M1_tail_bulk_split.py`, exact mpmath, NO float64): `TAIL(K)/V_A`
decays super-exponentially, matching the cited bound —

| K | tail/V_A (θ=2000) | tail/V_A (θ=8000) |
|---|---|---|
| 1 | 1.76e−2 | 8.53e−3 |
| 3 | 1.80e−5 | 1.56e−5 |
| 5 | 5.60e−9 | 3.84e−9 |
| 8 | 3.99e−15 | 1.40e−15 |
| 10 | 4.23e−20 | 9.43e−21 |

per-step drop factors *grow* (×22 → ×45 → ×124 → ×2.7e4 → …), the `exp(−¼K^{3/2})` signature. The tail
falls below the `θ^{−1}` remainder scale (~0.068/θ) by K=3–4. So a fixed modest cutoff already isolates
the whole leading term and its `θ^{−1}` remainder inside the bulk.

## Result 2 — the ingested literature supplies the *machinery* for the bulk, and de-Poissonization

- **De-Poissonization is citable.** Johansson Lemma 3.8 (eq. 3.38) bounds the fixed-n vs Poissonized
  distribution functions with an explicit `C/N²` error over the window `N ± 4√N log N`. This is the
  rigorous transfer from the Poissonized Bessel-kernel variance to the fixed-n (CS) quantity — the step
  `finite_n_cs_margin.py` performs heuristically.
- **The bulk rate machinery is now in-corpus.** `library/sm10137-eng` — **Gorbunov, "Rate of
  convergence in the CLT for the determinantal point process with Bessel kernel"** (Sbornik 2024) —
  proves a Berry–Esseen **rate** for linear statistics of the (continuous, hard-edge) Bessel-kernel DPP
  via the Kac–Akhiezer variance formula (Basor–Ehrhardt) and the **Borodin–Okounkov Toeplitz
  identity**, explicitly framed as the *continuous analogue of the discrete (Toeplitz) case*. BOO
  Remark 1.6 already notes the discrete Plancherel case *is* a Toeplitz determinant (Widom). So the
  rate route — Szegő/Borodin–Okounkov strong-limit asymptotics *with error term* for the relevant
  Toeplitz+Hankel determinant — is now represented in the corpus.

**Honest scope.** Gorbunov's kernel is the *continuous hard-edge* Bessel kernel, not BOO's *discrete*
Plancherel descent kernel, so it is **not a drop-in citation** for the bulk of `V_A`. What changed is
the epistemic status of the gap: from *"no rate anywhere in the corpus"* to *"the tail and
de-Poissonization are citable (Johansson), and the bulk-rate machinery is in-corpus (Gorbunov /
Borodin–Okounkov / Widom), needing application to the discrete Plancherel descent variance."* That
application is a real analytic step, not a missing reference.

## Status of `qou-k5r5` after this PR

| ingredient | before | now |
|---|---|---|
| leading margin `m∞` | `0.300186 > 0` (exact) | unchanged |
| exact finite-n `m(n)>0` | `4 ≤ n ≤ 40` | unchanged |
| **tail** of the effective bound | "classical, boundable" (hand-wave) | **cited + measured** (Johansson Lemma 3.9); Olver-free |
| **de-Poissonization** | heuristic Gaussian conditioning | **cited** with `C/N²` (Johansson Lemma 3.8) |
| **bulk** sine-kernel rate | "no rate in corpus" | **machinery in-corpus** (Gorbunov/BO/Widom); application step remains |

The gap is **OPEN** but materially narrowed: the only remaining rigorous step is the bulk sine-kernel
rate for the discrete Plancherel descent variance, and the tools for it are now on hand.

## Result 3 — the leading-margin field is now *proved* (rigorous `V_D` ceiling) and discharged in Lean

The `M1DescentDPPConvergence.DescentDPPMarginConvergence` class has three fields; two are the `Tendsto`
convergences gated on the bulk rate, but the third — `leading_margin_pos : √(V_D/V_A) < 2√6/5` — is a
fact about the *exact limit constants* and is **not** gated on the bulk rate. Because `π` cancels in
the square it is exactly `V_D < 64/(75π²)`, and `V_D` (no closed form) is now bounded **rigorously**:

- **Certified** (`wlambda_covariance_epic_M1_VD_ceiling_rigorous.py`, `mpmath.iv` interval arithmetic,
  NO float64): the partial sum over odd `k = 3…999` encloses to `V_D_partial ∈ [0.0415974805, …]`, and
  an **explicit elementary tail majorant** `R(K) ≤ a²/(2K⁴) + b²/(3K⁶)` (from `|Â_k| ≤ (72/5)/(πk²)`,
  `|Ω̂_k| ≤ (4032/25)/(π²k³)`, both via `k²−4 ≥ (5/9)k²`) gives `R(999) ≤ 1.05e−11`. Hence
  `V_D < 0.0415974806 < 0.0864607 = 64/(75π²)` with margin `0.0449`. This upgrades `m∞ > 0` from
  *measured* to *proved*.
- **Lean** (`M1DescentDPPConvergence.leading_margin_pos_of_VD_ceiling`, sorry-free, `#print axioms`
  clean): given `V_A = 8/(9π²)`, `sigRatioInf² = V_D/V_A`, `rhoInf² = 24/25`, `0 ≤ rhoInf`, and the
  ceiling `V_D < 64/(75π²)`, derives `sigRatioInf < rhoInf` by `π`-cancellation in the square. So the
  `leading_margin_pos` field is discharged modulo the certified numeric ceiling — one of the three
  class fields closed with genuine rigor, leaving only the two bulk-rate `Tendsto`.

## No fake closure

The bulk-application step is not done here, and a *measured* tail decay is corroboration of the *cited*
Johansson bound, not a substitute for it. The tail-half reduction is rigorous (cited bound + polynomial
weight); the leading-margin ceiling is rigorous (certified interval + explicit majorant); the **bulk
correlation/ratio convergence remains genuinely open** (the two `Tendsto` fields). Gap `qou-k5r5` OPEN.

## Compute + sources

- [`wlambda_covariance_epic_M1_tail_bulk_split.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_tail_bulk_split.py) (exit 0; exact mpmath; NO float64).
- Johansson Lemma 3.9 (Bessel tail) + Lemma 3.8 (de-Poissonization): `library/arxiv-math-9906120v3/sections/sec-007-34-asymptotics-of-the-plancherel-measure-theorem.md`.
- Gorbunov bulk-rate machinery: `library/sm10137-eng/`.
- BOO (rate-free bulk limit, Remark 1.6 Toeplitz): `library/arxiv-math-9905032v2` (= published twin `library/s0894-0347-00-00337-4`, `library-duplicate-ledger.json`).

## Cross-references

- Prior gap statement: [`2026-08-29-covariance-kernel-M1-k5r5-the-missing-citation-is-a-kernel-rate.md`](2026-08-29-covariance-kernel-M1-k5r5-the-missing-citation-is-a-kernel-rate.md)
- Leading constants: [`2026-08-29-covariance-kernel-M1-po72-leading-constants.md`](2026-08-29-covariance-kernel-M1-po72-leading-constants.md)
- Epic `qou-h315`/`qou-x631`; gap `qou-k5r5`.
