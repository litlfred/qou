# c_11+ attempt — holonomic test + the data-level blocker (verdict)

**Date:** 2026-06-04
**PR:** (this branch — `claude/qbeta-ck-holonomic-c11-attempt-2026-06-04`)
**Status:** DONE — c_11+ blocked at the data level; the precision floor proves
only c_2,c_3 are data-determined, so the keystone is a framework derivation
(multi-anchor superseded)
**Builds on:** kernel deepening (#1839), c6-c10 cross-anchor falsification (on main)

## The attempt (formalize-first)

Step 2 (#1823) + the Lean grounding proved the c_k are **not** low-order
constant-coefficient C-finite ⇒ `F(u)` is **not** a low-degree rational. The
next structural class up — which **subsumes** the cosh-avatar /
generating-function hypothesis (#1824) — is **holonomic (D-finite)**: do the c_k
satisfy a *polynomial*-coefficient recurrence `∑_i p_i(n)·c_{n-i} = 0`? A
positive low-order fit would **predict c_11+** outright. This is a structural
class test, not a free fit (compute-author §3.3).

Probe:
[`qbeta_ck_holonomic_recurrence_guess.py`](../../computations/qbeta/qbeta_ck_holonomic_recurrence_guess.py).

## Result

| window | order | deg | σ_min/σ_max (col-normalised, direct SVD) | holonomic? |
|---|---|---|---|---|
| applied c2..c7 | 1 | 1 | 2.8e-2 | no |
| full c2..c10 | 1 | 1 | 1.0e-7 | no |
| full c2..c10 | 1 | 2 | 6.5e-10 | no |
| full c2..c10 | 2 | 1 | 1.3e-8 | no |

No clean low-order holonomic recurrence.

**Method note (Copilot review, PR #1844).** The singular values are now
computed by a *direct* SVD of the *column-normalised* matrix, not via
eigenvalues of `MᵀM`. Forming `MᵀM` squares the condition number; combined
with the erratic free rung `c_10 ≈ 1e8`, that had pushed the apparent
smallest-SV *below* its true value (old `1.0e-11` at `o1d2`) — biasing the test
toward a holonomic-*looking* signal. The corrected values are *larger*
(`6.5e-10` at `o1d2`) and sit ~15 orders **above** a genuine recurrence floor:
a true D-finite recurrence in the given ~25-digit `c_k` would drive
`σ_min/σ_max → ~1e-25` (well below, at the `compute_dps = 70` now used). So the
no-holonomic verdict rests on sound numerics, not a conditioning artifact. The
residual near-degeneracy at `o1d2` is the expected structure of a short
Vandermonde-like system with weak over-determination (`n_eq = 8`, `n_unk = 6`)
plus one erratic value — not a recurrence.

## The honest verdict — blocked at the DATA level

This is **not decisive** for `F`'s holonomicity, because the only **independent**
rungs are unreliable. Per the just-landed
[c6-c10 cross-anchor falsification](2026-06-04-c6-c10-crossanchor-biascorrected-falsification.md):

- the canonical extraction **imposes** closed forms at **c_2..c_7** (so their
  recovery is self-consistency, not independent data);
- **c_8..c_10** are extracted **freely from a single anchor** — and c_8 (first
  free rung) is erratic, breaking the Pell-Lucas continuation.

So the structural tests (constant-kernel, holonomic, generating-function) all run
into the **same wall**: there is no reliable, scale-comparable, independent c_8+
data to test against. A negative result is therefore consistent with *either* `F`
non-holonomic *or* free-rung extraction noise.

## The deeper layer — WHY the data is blocked (the unifying result)

The "blocked at the data level" verdict above has a precise, *information-
theoretic* cause that subsumes this whole campaign. Probe:
[`qbeta_ck_extraction_precision_floor.py`](../../computations/qbeta/qbeta_ck_extraction_precision_floor.py).

The c_k are read off `R(u) = Q_β / (Q_A·cos α_eff) = ∏_k (1 + c_k·u^k)`. The
*only* noisy input is the **measured** neutron Q-value (Q_A and cos α_eff are
framework-computed to ~`1e-50`), so `R`'s relative precision is
`σ_R ≈ 6e-7` (AME2020: ≈ 0.48 eV / 782.3 keV). Since `∂ ln R / ∂ c_k ≈ u^k`,
each rung is extracted with absolute uncertainty

```
σ(c_k) = σ_R / u^k        (measurement noise ÷ that rung's lever u^k).
```

With `u = b·ℏ_q² ≈ 0.00852`, `u^k` underflows fast (`u^3 ≈ 6.2e-7 ≈ σ_R`,
`u^4 ≈ 5.3e-9 ≪ σ_R`), so `σ(c_k)` explodes. A rung is *data-determined* only
when `σ(c_k)/|c_k| < 1`:

| k | u^k | σ(c_k) = σ_R/u^k | σ(c_k)/\|c_k\| | data-determined? |
|---|---|---|---|---|
| 2 | 7.3e-5 | 8.3e-3 | **0.8 %** | yes |
| 3 | 6.2e-7 | 0.97 | **49 %** (marginal) | yes |
| 4 | 5.3e-9 | 1.1e+2 | 101× | no |
| 7 | 3.3e-15 | 1.8e+8 | 2.3e7× | no |
| 10 | 2.0e-21 | 3.0e+14 | 2.8e6× | no (the "1e8" is noise) |

**Only `c_2` and `c_3` clear the floor** (`k_max = 3`); robust across a `σ_R`
scan down to `1e-8` (a hypothetical 100× better than AME — still `k_max = 3`).
This single fact explains the **entire** campaign:

- the **registry tiers** (`c_2` proved / `c_3` near-match / `c_4+` fitted) —
  they track `σ(c_k)/|c_k|` crossing 1 between `c_3` and `c_4`;
- the **4-significant-figure ceiling** — it *is* `σ_R`;
- the **erratic free rungs** — `c_8..c_10` have `σ(c_k)/|c_k| ≫ 1`, so they are
  fitting noise (this is the c6-c10 falsification, *derived*);
- **every failed structural test** (real-q, root-of-unity, rational, holonomic,
  generating-function) — all were run against below-floor data.

## The genuine unblock — a framework derivation, not an extraction

The earlier candidate unblock (a **multi-anchor extraction** of `Q_N2(q)`) is
**superseded** by the floor result. Averaging `N` independent anchors cuts
`σ(c_k)` only by `√N`, so reaching `σ(c_4)/|c_4| < 1` needs `N ≈ 1e4`
**independent physical** Q_β measurements. There is *one* neutron Q-value; the
other q-anchors derive from the same calibration inputs, and `u` barely varies
across them (so the q-dependence lever for `c_4` is itself below floor).
Multi-anchor is necessary-but-wildly-insufficient.

⇒ **The `c_k ≥ 4` keystone is necessarily a canonical *framework derivation*
(deriving the `c_k` from the Hecke / SDP structure), not a data extraction at
any anchor count or precision.** The productive direction is the Q_β Habiro
element (parallel α_EM `[2]_q·(1−h²α)`, PR #1511), whose archimedean evaluation
*predicts* the `c_k` rather than fitting them.

## Net (the keystone is now precisely located AND its blocker proved)

- **Refuted** (this campaign): real-q forms, root-of-unity, low-order rational
  (constant kernel), the SDP cos-factor zero, and now low-order holonomic on the
  current data.
- **Blocker** (now *proved*, not just observed): `σ(c_k) = σ_R/u^k`; only `c_2`,
  `c_3` are above the measured-Q_β floor — `c_4+` cannot be extracted at any
  anchor count or precision.
- **Unblock** (corrected): not multi-anchor (insufficient by ~`1e4`×) but a
  **canonical framework derivation** of the `c_k` (Habiro element / SDP
  structure), which the floor leaves as the *only* path.

## Guards

TIERED; structural-class test (not a fit); ℏ_q/q₀ from canonical witnesses;
diagnostic-only; tiers governed by the
[c_k/d_k registry](../coordination/ck-dk-canonical-registry.md).
