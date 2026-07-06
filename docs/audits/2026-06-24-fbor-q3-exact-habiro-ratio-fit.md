# F_Bor `/q³` is exact; the `habiro_ratio` is the fit — and Li₂^q can't source it

**Date:** 2026-06-24
**Bean:** `ovud` ("wire Li₂^q brane-tower into production F_Bor")
**PR:** #2691
**Probe:** [`computations/li2q_fbor_expansion_probe.py`](../../computations/li2q_fbor_expansion_probe.py)
+ [`li2q-fbor-expansion-probe.witness.json`](../../computations/li2q-fbor-expansion-probe.witness.json)

## Context

The owner asked, after the canonical-mass derivation review: *"why not wire
up Φ_q / Li₂^q rather than `/q³`? or use a better approximation based on the
expansion?"* This audit answers it and **reframes the premise** — `/q³` is
not a fit.

## Findings

### 1. `/q³` is the exact q-factorial balancing (NOT a fit)

Symbolically (sympy, residual = 0):

```
[3]_q! / q³  =  1 + 2q⁻² + 2q⁻⁴ + q⁻⁶
```

a bounded Laurent polynomial in `q⁻²`. Therefore

```
F_Bor(q) = |tr_M(β_Bor)| · [3]_q!/q³
```

is a **fully exact closed form** — `|tr_M(β_Bor)|` is the Lean-proved
Borromean Markov trace `(4+h²−3h⁴−h⁶)/(h²+4)`, and `[3]_q!/q³` is exact
balancing. There is no `/q³` fit to remove, and no Li₂^q tower can
"replace" an exact balancing (a category error).

### 2. The fit is the `habiro_ratio`, not `/q³`

Production [`m_p_substrate_identity_50dps.py`](../../computations/m_p_substrate_identity_50dps.py)
applies, *after* the exact F_Bor:

```
habiro_ratio = (1 + 46u⁴)(1 + 4u⁵)(1 − 29u⁶),   u = b·ℏ_q² ≈ 0.008517
```

Layer sizes at q₀:

| quantity | value | m_p error |
|---|---|---|
| F_Bor (exact) | 4.46914 | — |
| m_p = 2·m_μ·F_Bor − 12·m_e (**F_Bor alone**) | 938.27186 | **−242 ppb** |
| `habiro_ratio` | 1 + 2.42e-7 | — |
| m_p × `habiro_ratio` (**production**) | 938.272088 | **+0.0004 ppb** |

The `habiro_ratio` supplies exactly `+2.42e-7` (= +242 ppb), cancelling
F_Bor's −242 ppb residual to the q₀-pinning floor. The leading term
`46u⁴ = 2.42e-7` *is* essentially the whole correction (u⁵/u⁶ are ~100×/10⁴×
smaller). The integer coefficients `{46, 4, 29}` have **no derivation trail**
(checked: `git log -S`, docs, witnesses) and land m_p on CODATA to the
pinning floor — the signature of a CODATA-anchored near-match / fit.

### 3. Li₂^q can NOT source the correction — it is term-6, not terms-2/3

The Li₂^q brane-tower is terms 2/3 of the 6-term mass formula:
`Σ_i −Li₂^q(−|V̂_i|)`. For the proton the per-generator volumes are O(1)
(`|V̂| ≈ 0.989, 0.971`), so the tower evaluates to **O(1)**:

```
Σ_i −Li₂^q(−|V̂_i|) = 1.6183      vs   46u⁴ = 2.42e-7
```

a 10⁷ scale mismatch. The `habiro_ratio` is therefore the **term-6 Habiro
residue tail**, not the Li₂^q brane-tower — consistent with its name and
with the *integer* coefficients (Habiro polynomials are integral).

### 4. Deriving `{46,4,29}` = the open Q_β c_k / keystone problem

The term-6 Habiro residue tail for the mass sector is the same open object
as the Q_β c_k ladder: a Habiro element whose archimedean evaluation at q₀
must reproduce the coefficients. Deriving `{46,4,29}` from first principles
is gated on the same s5-so3 keystone (`beans s5bb`, kernel `F(q)`/`R(q,ξ)`)
and subject to the same 14 refuted-class history. It is **not** closeable by
a Li₂^q-tower reparametrisation.

## Verdict (scope-limited, per AGENTS.md "before declaring refuted")

- (a) **`/q³` is exact** — proved, not a scope-limited claim.
- (a) **The Li₂^q brane-tower (terms 2/3), *alone*, does not source the
  `habiro_ratio` correction** — it is the wrong scale (O(1) vs O(1e-7)).
  This does not exclude Li₂^q from the mass formula (it is terms 2/3 of the
  6-term form); it locates the `+242 ppb` correction in term-6 instead.
- The principled derivation of the `{46,4,29}` term-6 coefficients is
  **open**, gated on the s5bb keystone — same as Q_β c_k.

## Discipline

Exploratory probe. No production rewire, no fit added or removed, no
registry tier change, Δ_λ gate untouched. The production `habiro_ratio`
stays as-is pending the keystone; this audit only *characterises* it
honestly (CODATA-anchored near-match, not a derived series).
