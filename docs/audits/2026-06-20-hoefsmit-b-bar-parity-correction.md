# Hoefsmit ladder base `b(q)` is bar-EVEN — correction to the criterion-2b prune (2026-06-20)

**Status:** correction — fixes a misidentified `b(q)` in the just-landed
Q_β criterion-2b bar-parity prune. The prune's **verdict survives**; its
**mechanism** (and one compute script + witness) was wrong and is corrected here.

## The error

The criterion-2b prune
([`2026-06-20-qbeta-barparity-criterion-2b-prune.md`](2026-06-20-qbeta-barparity-criterion-2b-prune.md),
commits `f246fae2` / `e73d42bf` / `27e45c68`; compute
[`qbeta_barparity_kernel_criterion_prune.py`](../../computations/qbeta/qbeta_barparity_kernel_criterion_prune.py))
used

```
b(q) = (q − q⁻¹)/(q + q⁻¹)        ← bar-ODD, and WRONG
```

as the Hoefsmit ladder base, concluding `b` is bar-odd ⇒ `u = b·ℏ_q²` is
bar-odd-covariant (`u ↦ −q²·u`) ⇒ a bar-even kernel forces
`c_k(q⁻¹) = (−1)^k q^{−2k} c_k(q)`, and that the ladder is "parity-split."

That `b` is **not** the canonical Hoefsmit base. It is contradicted three
independent ways.

## Three-way refutation

1. **Substrate value.** CLAUDE.md and the mainstream `c_k` probes pin
   `u = b·ℏ_q² ≈ 0.00852`. At `q₀ ≈ 1.1099785955573347`,
   `ℏ_q² ≈ 0.0098172`, so:
   - canonical `b = √(q⁴+q²+1)/(q²+1) ≈ 0.86758` → `u ≈ 0.0085172` ✓
   - prune `b = (q−q⁻¹)/(q+q⁻¹) ≈ 0.10396` → `u ≈ 0.0010206` ✗ (off ~8×)

2. **Corpus convention.** The mainstream `hoefsmit_b` (≥5 probes:
   `c_3_categorical_derivation_attempt.py`, `qbeta_c3_three_rung_probe.py`,
   `mmu_kashiwara_cos_factor_probe.py`,
   `qbeta/qbeta_composite_operator_first_test.py`,
   `qbeta_c3_v9_style_probe.py`) all return
   `√((h²+3)/(h²+4))`, `h = q − q⁻¹` — which equals `√(q⁴+q²+1)/(q²+1)`.
   `SilverAnchorGrounding.lean` grounds the same `b² = (q⁴+q²+1)/(q²+1)²`.
   The `(q−q⁻¹)/(q+q⁻¹)` form appears only in the prune script and its
   companion comparison utility.

3. **Bar-parity (symbolic + Lean).** `h = q − q⁻¹` is bar-odd, so `h²` is
   bar-even, so `b² = (h²+3)/(h²+4)` is **bar-even**, so `b(q⁻¹) = b(q)`.
   Verified in Lean (sorry-free, `lean`-direct exit 0):
   [`QOU.QBeta.hoefsmitBSq_bar_even`](../../content/quantum-observable-universe/lean/QOU/QBeta/HoefsmitBBarParity.lean).

## The correct covariance

Since `b` is bar-even and `ℏ_q = 1 − q⁻¹` is bar-odd-covariant
(`ℏ_q(q⁻¹) = −q·ℏ_q(q)`, so `ℏ_q²(q⁻¹) = q²·ℏ_q²(q)`):

```
u(q⁻¹) = +q²·u(q)        (bar-EVEN-covariant — NO sign)
```

verified in Lean: `QOU.QBeta.uSq_bar_covariance` (`u²(q⁻¹) = q⁴·u²(q)`).
A bar-even kernel `F(q) = Σ c_k u^k` therefore forces the **unsigned** law

```
c_k(q⁻¹) = q^{−2k} c_k(q)        (no (−1)^k).
```

## Impact

- **Verdict UNCHANGED.** Criterion 2(b) still cannot be imposed: under the
  corrected law, `c₂ = −1` gives residual `q^{−4} − 1 ≠ 0`, and both `c₃`
  candidates (`−2 − ℏ_q²`, `J_Hopf(q)`) also violate it. So the prune of
  "F bar-even in u" stands.
- **Mechanism CORRECTED.** There is **no "parity-split ladder."** `u` is
  uniformly bar-even-covariant (`+q²`, no per-rung sign), so the prune
  follows purely from the `c_k` values failing the unsigned law — not from
  any bar-oddness of `u`. The redirect "Type-B only as the bar-odd
  companion" rested on the wrong `u` parity and should be re-derived.

## Changes in this PR

- **Lean** (new, sorry-free): `QOU/QBeta/HoefsmitBBarParity.lean` —
  `hoefsmitBSq_eq_h`, `hoefsmitBSq_bar_even`, `hbarQ_bar_odd_covariant`,
  `uSq_bar_covariance`. Registered in `QOU.lean`.
- **Compute fix:** `qbeta_barparity_kernel_criterion_prune.py` rewritten to
  the canonical bar-even `b`, corrected covariance (`+q²`) and law (no
  `(−1)^k`); witness regenerated (`b_bar_parity: even`,
  `u_is_bar_even_covariant_plus_q2: true`). Verdict text preserved
  (unchanged conclusion) with a correction note.
- **Compute fix:** `qbeta_c3_jhopf_q0_vs_q1_comparison.py::hoefsmit_b` →
  canonical `√((h²+3)/(h²+4))`.

## Not changed (flagged for the author)

The prune's narrative `.md`
([`2026-06-20-qbeta-barparity-criterion-2b-prune.md`](2026-06-20-qbeta-barparity-criterion-2b-prune.md))
still states `b` bar-odd / `u ↦ −q²u` / the `(−1)^k` law / "parity-split."
Its **verdict** is correct, but the **mechanism** paragraphs need the
author's revision per this correction. Left untouched to avoid rewriting a
sibling's narrative unilaterally.
