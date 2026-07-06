# KLR tranche-2 Composite-1 (Demazure × q-Poch) preflight RUN — results (BUILD NOT AUTHORISED)

**Companion to** the [Composite-4 preflight run results](2026-06-06-qbeta-klr-composite4-preflight-run-results.md). Same template, applied to cont. 9 [Option C / Composite 1 (Demazure × q-Pochhammer mixed trace)](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md#composite-1-demazure-x-q-pochhammer-mixed-trace) (5-7 session infra build). Verdict: **standard-Demazure variant REFUTED at u² by SIGN** ⇒ cont. 9 Option C not authorised in its natural reading.

## Result

[`qbeta_klr_composite1_preflight_run.py`](../../computations/qbeta/qbeta_klr_composite1_preflight_run.py) computes `[u²]F = (q;q)_2 · Σ_{ℓ(w)=2} D_w(ω₁; sl_3)` at both anchors (mp 65-dps), using the explicit Demazure-character formula from
[`qbeta_chain4_demazure_fund_weights.py`](../../computations/qbeta/qbeta_chain4_demazure_fund_weights.py)
(`D_w(ω_j; q) = Σ_S q^{Σ(a_k − 1)}`, the Joseph/Andersen unsigned Demazure):

| anchor | `(q;q)_2` | sign | `Σ D_w(ω₁; sl_3)` at ℓ=2 | `[u²]F` | vs `c_2 = -1` |
|---|---|---|---|---|---|
| proton | `+2.55208e-02` | `+` | `+5.4520096197` | **`+1.39140e-01`** | **SIGN MISMATCH** |
| muon | `+2.55208e-02` | `+` | `+5.4520096737` | **`+1.39140e-01`** | **SIGN MISMATCH** |

Both anchors identical to 9 figs (q-independent in this regime). 2 assertions pass (sign-refutation + u² positivity, both anchors).

## Why the sign refutation is decisive

| component | value | sign at q₀ > 1 |
|---|---|---|
| `(q;q)_2 = (1−q)(1−q²)` | `2 negatives × 1 = +` | **POSITIVE** |
| `Σ_{ℓ(w)=2} D_w(ω₁; sl_3)` | sum of q-monomials `q^{Σ(a_k−1)}` | **POSITIVE** (sum of non-negative powers) |
| `[u²]F = (q;q)_2 · Σ` | product of two positives | **POSITIVE** |
| **Target `c_2 = -1`** | proved (PR #1887) | **NEGATIVE** |

The sign positivity of standard Demazure characters is a **fundamental property** (Joseph/Andersen): they are sums of positive q-monomials with non-negative weights. This is convention-robust:

- **The Y_k renormalisation from §3c does NOT rescue**: `Y_k = q^{−k(k+1)/4}·(q;q)_k` inherits the sign of `(q;q)_k` (the prefactor `q^{−k(k+1)/4} > 0` for q > 0). So sign analysis is unchanged.
- **No global rescaling rescues**: a single constant `C` such that `C·[u²]F = -1` would be `C < 0`, but `c_3 ≈ -2.07 < 0` and `[u³]F = (q;q)_3·Σ_{ℓ(w)=3} D_w` is `(-) · (+) = -` (since `(q;q)_3` flips sign at q > 1 for odd k). So `c_3` already matches sign without rescaling; a global `C < 0` would flip c_3 too. **Contradiction.**

## What the magnitude side adds (for the record)

`|[u²]F| = 0.139` vs `|c_2| = 1` ⇒ off by ~7× even ignoring sign. Closer than Composite 4's ~92× gap (the larger Demazure character sum makes up some), but still not consistent with cross-anchor rigidity (cont. 11 sweep) at smaller λ. Larger λ could theoretically close the magnitude — but the sign barrier remains regardless of λ.

## Honest caveat (untested variant)

The Demazure-Lusztig characters (q-difference operators T_i with signed coefficients) can produce signed Demazure characters. This UNTESTED variant might survive the sign refutation. **It would require a separate preflight scope**:
- Specify the Demazure-Lusztig convention used
- Compute Σ_{ℓ(w)=2} D_w^{DL}(λ) and check sign + magnitude at q₀
- This preflight refutes only the natural (Joseph/Andersen) reading of cont. 9 Option C, not the generalised one

## Combined preflight outcome (Composite 4 + Composite 1)

Both cont. 9 single-Option preflights done in one session each. Combined effect on the KLR-infra roadmap:

| Option | Preflight | Verdict | Saved infra |
|---|---|---|---|
| **B** (Composite 4 Wenzl × q-Poch) | PR #1914 §3c + RUN | REFUTED at u² magnitude (~92×) | 5-6 sessions |
| **C** (Composite 1 Demazure × q-Poch, standard) | this RUN | REFUTED at u² sign | 5-7 sessions |
| **A** (accept residue A as CAL-3-anchored) | reinforced by 3 corpus closures + 2 preflight refutations | viable | — |
| **D** (Composite 3 Type-B folded crystal) | not yet preflighted | unknown | 12-17 sessions (if authorised) |
| **C-Lusztig** (Demazure-Lusztig variant) | untested | unknown | separate scope needed |

**Total infra saved by the 2 preflights:** ~10-13 sessions of Lean + `pyhecke` build that would have failed at u^2.

## Cross-refs

- Sibling Composite-4 RUN: [`2026-06-06-qbeta-klr-composite4-preflight-run-results.md`](2026-06-06-qbeta-klr-composite4-preflight-run-results.md).
- Master KLR-infra roadmap: [`2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md`](2026-06-03-qbeta-residue-a-klr-crystal-infra-scope.md).
- Demazure character evaluator + crystal model: [`qbeta_chain4_demazure_fund_weights.py`](../../computations/qbeta/qbeta_chain4_demazure_fund_weights.py).
- cont. 11 1281-sweep (already included `Demazure(2,1) × (q;q)_k` 2-factor combinations): [`qbeta_composite_crossanchor_2factor_sweep.py`](../../computations/qbeta/qbeta_composite_crossanchor_2factor_sweep.py).
- Witness: [`qbeta-klr-composite1-preflight-run.witness.json`](../../computations/qbeta/qbeta-klr-composite1-preflight-run.witness.json).
