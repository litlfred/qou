# D9 audit correction — bar-parity attribution under canonical bar involution

**Date:** 2026-05-24
**Branch:** `claude/duality-d9-d13-d14-d22-2026-05-24`
**Status:** Audit correction. Surfaces a real mis-attribution in the prior D9 audit (`2026-05-24-isospin-categorical-source.md` §3 + `conj:isospin-from-canonical-bowtie.md`) caught by the `verify_isospin_bar_anomaly.py` verification script. **305 ppm empirical match unchanged** — only the bar-parity classification was wrong.

## The mis-attribution

The prior D9 audit (in PR [#1139](https://github.com/litlfred/qou/pull/1139)) and the D9 conjecture block (in PR [#1162](https://github.com/litlfred/qou/pull/1162)) claimed the 305 ppm substrate flavor-split residue is **"bar-anti-symmetric leading order"** under the canonical bar involution `q ↔ q⁻¹`, based on this four-factor decomposition:

| Factor | Claimed parity |
|--------|----------------|
| `ℏ_q² = (q-1)²/q²` | bar-symmetric (anti-sym squared) |
| `h = q − q⁻¹` | bar-anti-symmetric |
| `[2]_q = q + q⁻¹` | bar-symmetric |
| `(1 + ℏ_q³)` | mixed (1 bar-sym, ℏ_q³ bar-anti-sym) |
| **Product (leading)** | **bar-anti-symmetric** (claimed) |

## The bug

`ℏ_q = (q-1)/q` is **NOT** cleanly bar-classifiable under `q ↔ q⁻¹`:

$$
  \mathrm{bar}(\hbar_q) \;=\; \hbar_{q^{-1}} \;=\; \frac{q^{-1} - 1}{q^{-1}} \;=\; q(q^{-1} - 1) \;=\; 1 - q \;\neq\; \pm \hbar_q.
$$

So `ℏ_q` is **mixed** (neither bar-sym nor bar-anti-sym), and `ℏ_q²` is also **mixed** (not bar-symmetric as claimed). The full product `ℏ_q² · h · [2]_q · (1 + ℏ_q³) / 3` evaluates as **mixed** under bar — NOT bar-anti-symmetric.

Verified empirically by [`verify_isospin_bar_anomaly.py`](../../computations/verify_isospin_bar_anomaly.py) at q₀:

| Factor | Computed bar-parity (under q ↔ q⁻¹) |
|--------|--------------------------------------|
| `ℏ_q²` | **mixed** (not bar-symmetric) |
| `h` | bar-anti-symmetric ✓ |
| `[2]_q` | bar-symmetric ✓ |
| `(1 + ℏ_q³)` | mixed ✓ |
| **Product** | **mixed** (not bar-anti-symmetric) |

## The conceptual correction

The deeper issue is that the prior audit **conflated two distinct Z/2 involutions**:

| Involution | Acts on | Acts on q |
|------------|---------|-----------|
| **Bar** (D1) | σᵢ → σᵢ⁻¹ AND q → q⁻¹ | q-inverted |
| **Isospin Z/2** (D9) | σᵢ → σᵢ⁻¹ (on pp/nn pairs) | q **FIXED** |

The 305 ppm residue is the result of the **isospin** Z/2 swap acting on the canonical bowtie interface — NOT the bar involution. The two coincide on Hecke generators (both flip σᵢ ↔ σᵢ⁻¹), but they differ on the q-parameter (bar inverts q, isospin fixes q).

**Correct claim**: the 305 ppm residue is **isospin-Z/2-anti-symmetric** (carries the factor `h = q − q⁻¹` evaluated at fixed q₀, which is the natural "anti-symmetric" generator of the σ↔σ⁻¹ orbit). It is **not** bar-anti-symmetric.

## Impact

| Document | Status | Correction needed |
|----------|--------|-------------------|
| [`docs/audits/2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md) §3 | merged in PR #1139 | replace four-factor "bar parity" decomposition with "isospin Z/2 parity"; remove the claim that ℏ_q² is bar-symmetric |
| [`conj:isospin-from-canonical-bowtie`](../../content/quantum-observable-universe/braids-and-knots/isospin-from-canonical-bowtie.md) | merged in PR #1162 | same correction; replace "bar-anti-symmetric residue" with "isospin-Z/2-anti-symmetric residue" or "h-leading residue under canonical isospin swap" |
| [`docs/duality-tracker.md`](../duality-tracker.md) D9 row | merged in PR #1162 | update the closure-path description to refer to isospin Z/2 not bar |
| [`_li_2_q_util.flavor_split_subleading`](../../computations/_li_2_q_util.py) closed form | unchanged | The 305 ppm match is empirically correct; the FORM of the closed form is correct; only the bar-parity classification was wrong |

## §Slot J discipline self-validation

This is exactly the kind of mis-attribution the §Slot J probe-discipline rule (added in PR [#1139](https://github.com/litlfred/qou/pull/1139)) is meant to catch:

> **Bar-anti-symmetric leakage** — most "anomaly" findings ARE bar-anti-symmetric residuals that should cancel.

The flip side — wrongly claiming a quantity IS bar-anti-symmetric when it's actually mixed under bar — is the same class of bug. The §Slot J discipline requires authors to compute the bar-parity rather than assert it intuitively. This audit doc is the audit-trail of the discipline working: a verification script caught the assertion, the assertion is corrected, and the framework's understanding is sharper.

## What this correction does NOT change

- **305 ppm empirical match** to CODATA Δm/M_N — verified via `verify_isospin_bar_anomaly.py` at relative difference −0.03%
- **The qualitative picture**: the substrate flavor split IS the canonical-isospin Z/2 anomaly at q₀
- **The Lean class structure** in `conj:isospin-from-canonical-bowtie.md` — the regularised crystal functional + class instance approach remains valid; only the parity classification field needs updating

## Cross-references

- [`docs/duality-tracker.md`](../duality-tracker.md) D9 row (will be updated in this PR)
- [`docs/audits/2026-05-24-isospin-categorical-source.md`](2026-05-24-isospin-categorical-source.md) — the doc this corrects
- [`conj:isospin-from-canonical-bowtie`](../../content/quantum-observable-universe/braids-and-knots/isospin-from-canonical-bowtie.md) — the conj block this corrects
- [`.claude/skills/local/canonical-watcher.md`](../../.claude/skills/local/canonical-watcher.md) §Slot J — the discipline rule this correction validates
- [`verify_isospin_bar_anomaly.py`](../../computations/verify_isospin_bar_anomaly.py) — the verification script that surfaced the bug
