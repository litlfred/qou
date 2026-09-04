# Covariance-kernel epic (`qou-x631`) — M₁>0 `qou-k5r5`: a weight bug of mine, and the retraction of my own retraction

**Date:** 2026-09-03 · **Branch:** `claude/m1-k5r5-weight-bug-fix-2026-09-03` · **Tier:** correction of
merged content (PR #6463) · **Discipline:** the erroneous claim was mine, was merged, and is corrected
here at the producer rather than annotated around. **Epic:** `qou-x631`; gap `qou-k5r5`.

## What was wrong

PR #6463 (merged, `8ddfeaf`) reported that the `Var(Σ|c|)` remainder
`d(θ) := V_A(θ)/θ² − 8/π²` has rate **`θ^{-1/2}`** with coefficient **`C_A ≈ 0.857`** and **positive**
sign, and on that basis **retracted** the prediction — made in the same session — that the corpus's
oscillatory Euler–Maclaurin tool yields a `θ^{-1}` rate with explicit constant `TV(g″)/48`.

**All three of those figures were a bug in my probe.** The `Σ|c|` linear-statistic weight was written

```python
kk = abs(k); v = mp.mpf(kk * (kk + 1)) / 2; return v if k >= 0 else -v      # WRONG
```

i.e. `|k|(|k|+1)/2`, which **symmetrises the negative half**. The descent set is the *shifted* lattice
`D(λ) = {λᵢ − i}`, whose natural involution is `x ↔ −1−x`, not `x ↔ −x`. The canonical weight is
`k(k+1)/2` with **signed** `k`:

| k | −5 | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 |
|---|---|---|---|---|---|---|---|---|---|
| canonical | −10 | −6 | −3 | −1 | **0** | 0 | 1 | 3 | 6 |
| my buggy version | −15 | −10 | −6 | −3 | −1 | 0 | 1 | 3 | 6 |

so the canonical weight satisfies `g(−1) = 0` and `g(−k) = −g(k−1)`, and mine forced `g(−k) = −g(k)`.

## The tell I had and missed

Chasing the discrepancy, I first attributed it to the truncation `M` (mine `2√θ+10θ^{1/6}+24` = 118 at
θ=1000; the reference probe's `2√θ+12θ^{1/6}+20` = 121). **That explanation was impossible on its face
and I should have seen it immediately:** every term of `V_A = ½Σ(g(x)−g(y))²J(x,y)²` is a product of
two squares, hence non-negative, so a sum over *more* indices cannot be *smaller*. My `M=118` run gave
`V_A/θ² = 0.8379` against the reference `M=121` run's `0.8105`. A larger value from a smaller index set
falsifies "truncation is the only difference" without any further computation.

## Corrected measurement — the prediction stands

With the canonical weight, the probe reproduces
[`wlambda_covariance_epic_M1_tvok_remainder_rate.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_tvok_remainder_rate.py)
**exactly** (θ=1000 → `−6.64223e-5` in both, every printed digit):

| θ | 250 | 500 | 1000 | 2000 | 4000 |
|---|---|---|---|---|---|
| `d(θ)` | −2.579e−4 | −1.345e−4 | −6.642e−5 | −3.432e−5 | −1.690e−5 |
| exponent | — | 0.9393 | 1.018 | 0.9526 | **1.022** |
| `θ·d` | −0.06449 | −0.06725 | −0.06642 | −0.06864 | **−0.06760** |

Rate **`θ^{-1}`**, `c₁ ≈ −0.0678`, sign **negative** (`V_A/θ²` approaches `8/π²` from *below*). This
**confirms** bean `qou-tvok` STEP 2, which #6463 wrongly reported as disagreeing with it in both rate
and sign. My earlier "flagged, not adjudicated — they may be measuring different objects" hedge was
also wrong: the two probes compute the *same* quantity with the *same* method, so there was never a
second object to appeal to.

**Consequently the EM-osc prediction is un-retracted.** The corpus tool
`QOU.MathlibExt.abs_integral_sub_composite_le_osc` bounds `|∫ − composite|` by `h³/12·(g″(a) − g″(b))`
with **no factor of `k`** — the per-cell oscillations telescope, so the remainder tracks `TV(g″)`
rather than the cell count, on `C²` hypotheses only. With the bulk grid `h = 1/(2√θ)` that gives

> `|d| ≤ h²·TV(g″)/12 = TV(g″)/(48θ)` — the measured `θ^{-1}` rate, with explicit `C_A = TV(g″)/48`.

**Falsifiable target:** a Route-1 derivation must yield `TV(g″) ≥ 48·|c₁| ≈ 3.25`, an O(1) number
(`C_A` is a *bound* and `c₁` a *limit*, so `C_A ≥ |c₁|` is required, not equality — landing near 3.25
**from above** is the test). Computing `TV(g″)` from the variance density is the remaining step.

**Closure arithmetic improves accordingly.** At `θ^{-1}`, `m(n) ≥ m_∞ − C/n > 0` needs only
`N₀ = ⌈C/m_∞⌉ ≤ 78`, i.e. **`C ≤ 23.4`** — far weaker than the `C ≤ 2.65` a conservative `n^{-1/2}`
reading demands.

> **🛑 CORRECTED 2026-09-03 (PR #6500).** The sentence above is **wrong** and is retracted. The `θ^{-1}` rate is `V_A`'s, **not the (CS) margin's** — the margin `m(n) = ρ_P − σ_D/σ_A` is a ratio of square roots of variances plus a correlation, and no one has propagated the one rate into the other. What is **proved** (PR #5929) is `|m(n) − m_∞| ≤ C·n^{-1/2}`, so `N₀ = (C/m_∞)²` — *squared* — and the requirement is `C ≤ m_∞·√79 = 2.6681`. That is **the** requirement under the bound in hand, not "a conservative reading" of it. The route is nonetheless in better shape than either number suggested: the empirical envelope over `n ≥ 13` is `C_emp = 0.0580`, a **46× headroom** under the already-proved shape. See [`…-margin-envelope-retraction.md`](2026-09-03-covariance-kernel-M1-k5r5-margin-envelope-retraction.md).

## Blast radius — what else carried the bug

The same `gA` appeared in the two other probes I wrote this session. Both were re-run with the
canonical weight; **both conclusions are robust**, the numbers moving only in the 2nd–3rd digit:

| probe | quantity | before (buggy) | after (canonical) | conclusion |
|---|---|---|---|---|
| `…_pointwise_bound_insufficiency` | `U/V` at θ=78 | 45.65 | **45.59** | unchanged — pointwise route needs ~~`K < 0.058` … ~17× short~~ **`K < 0.17115`, ~5.8× short (PR #6528)** |
| `…_deep_tail_rigorous_majorant` | far-tail share, θ=100 / 256 / 640 | 1.7 / 1.6 / 1.1 ×10⁻³⁸·V_A | **1.79 / 1.62 / 10.7** ×10⁻³⁸·V_A | unchanged — far tail rigorously negligible |

Those two survive because their claims are structural (a growing ratio; a super-exponentially small
tail) rather than dependent on the weight's precise values. Only the `θ^{-1/2}` claim was weight-borne,
and it is the one that was wrong.

## Corrected artifacts

- Probe [`…_em_osc_constant_prediction.py`](../../computations/deltalambda/wlambda_covariance_epic_M1_em_osc_constant_prediction.py)
  — weight fixed, conclusion inverted to `θ^{-1}` + `TV(g″) ≈ 3.25` target, correction history in the
  docstring.
- Probes `…_pointwise_bound_insufficiency.py`, `…_deep_tail_rigorous_majorant.py` — weight fixed,
  figures refreshed.
- Audit [`2026-09-03-…-deep-tail-rigorous-need-lit-localised.md`](2026-09-03-covariance-kernel-M1-k5r5-deep-tail-rigorous-need-lit-localised.md)
  — far-tail table refreshed to the canonical-weight numbers.
- Bean `qou-k5r5` — the `θ^{-1/2}` entry corrected in place.

## Status of `qou-k5r5`

Gap **OPEN**, and slightly *better* placed than #6463 left it: the remainder rate is `θ^{-1}` (not the
worse `θ^{-1/2}`), the required constant is ~~`C ≤ 23.4` (not 2.65)~~ **`C ≤ 2.6681` — see the
correction above; the `23.4` is retracted** — and the EM-osc route has a concrete
falsifiable target `TV(g″) ≈ 3.25`. The remaining step is unchanged in kind: compute `TV(g″)` for the
variance density and check it lands above that, which needs no literature.

## Cross-references

- The retracted claim: PR #6463 (`8ddfeaf`), superseded by this note.
- Reference probe: `wlambda_covariance_epic_M1_tvok_remainder_rate.py`; bean `qou-tvok` STEP 2.
- Epic `qou-x631`; gap `qou-k5r5`.
