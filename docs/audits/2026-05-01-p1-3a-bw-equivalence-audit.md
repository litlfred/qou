# P1.3a audit — BW vs Wenzl-bridge vs LP-shadow-price equivalence

**Pair**: [`2026-05-01-math-framework-workplan.md`](2026-05-01-math-framework-workplan.md) §P1.3a
**Branch**: `claude/audit-math-framework-FXlp2`
**Tooling**:
[`computations/bw_wenzl_shadow_equivalence.py`](../../computations/bw_wenzl_shadow_equivalence.py)
**Witness**:
[`2026-05-01-p1-3a-bw-equivalence.witness.json`](2026-05-01-p1-3a-bw-equivalence.witness.json)

## Headline

🟢 **Equivalence verified symbolically.** The three derivation paths
in the QOU paper produce coefficients that are **rationally related
by explicit factors of $h = q - q^{-1}$**, all reducing to the same
Wedderburn-block invariant $w_\lambda = \dim_q(\lambda)^2 / [n]_q!$:

| Path | Form | Relationship to $w_\lambda$ |
|------|------|----------------------------|
| **BW (Bethe–Weizsäcker / hook-weight)** | $\beta_\lambda = -\tfrac12 w_\lambda$ | unsigned mass coefficient with $\frac12$ |
| **LP shadow-price** | $C_\lambda = w_\lambda \cdot h/2$ | LP dual variable (Frobenius positivity) |
| **Wenzl-bridge** | $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$ | sign tracks content sum $\kappa_\lambda = \sum c(x)$ |

For self-conjugate partitions ($\kappa_\lambda = 0$), $y_\lambda = w_\lambda$ exactly. The
ratios are:

| Ratio | Value | Notes |
|-------|-------|-------|
| BW / shadow-price | $-1/h$ | extra factor of $h$ in the LP dual |
| BW / Wenzl-bridge | $-1/2$ | the BW ½ from Wigner T=0 doubling |
| shadow / Wenzl-bridge | $h/2$ | the LP-dual scaling by Hecke generator |

## Verification

The script symbolically evaluates each form for the two
Hook-relevant partitions:

### λ = (2, 2) ⊢ 4 — used in BW-8 (Wigner T=0 pairing) and BW-11 (T=1 pairing)

```
dim_q((2,2))       = (q⁴ + 1)/q²
w_((2,2))          = (q⁶ + q²) / (q⁸ + 3q⁶ + 4q⁴ + 3q² + 1)
H_q((2,2))         = (q⁴-1)² (q⁶-1) / [q⁴ (q²-1)³]

BW / shadow-price  = -q / (q²-1)         = -1/h     ✓
BW / Wenzl-bridge  = -1/2                = -1/2     ✓
shadow / Wenzl     = (q²-1) / (2q)       = h/2      ✓
```

All three ratios are **identities** (not approximations). The
three forms are not independent results — they are the same
Wedderburn-block weight $w_{(2,2)}$ scaled by explicit factors.

### λ = (3, 2, 1) ⊢ 6 — next-level (BW-7 Wigner-2)

```
C_{(3,2,1)} = [2]·[4]·[6]·h / (2·[3]³·[5])    (explicit closed form
                                                 in shadow_price_c_321_q0.py)
            = w_{(3,2,1)} · h/2                (via Wigner-2 prop)

C_explicit − C_via_w = 0                       ✓ (sympy simplifies exactly)
```

## Implication

The earlier "three candidate derivation paths" framing in workplan
P1.3a was over-stated. There is **one** Wedderburn-block invariant
$w_\lambda$, and three notations:

1. **BW form** packages it as a signed mass coefficient $\beta_\lambda$.
2. **LP shadow-price** packages it as the LP-dual variable $C_\lambda$ (multiplied by $h$ which is the Hecke generator scalar — this is the algebraic gradient of the Frobenius-positivity constraint).
3. **Wenzl-bridge** tracks the same invariant with a content-sum sign: $y_\lambda = (-1)^{\kappa_\lambda} w_\lambda$.

For BW-8 / BW-11 (both based on $\lambda = (2,2)$), the agreement is exact and symbolic.

## Status

🟢 **P1.3a closed.** No independent fits across the three paths;
each is a notational repackaging of the same $w_\lambda$. The
"keep all three as parallel ladders" option is the right one — they
are kept as **alternative views** of the same underlying
algebraic-combinatorial fact.

## Action — none required

Both BW-8 and BW-11 are derived (P1.2 / P1.3 marked ✅ landed). The
shadow-price view (`prop:mass-coefficient-shadow-price`) and the
Wenzl-bridge view (`prop:y-lambda-closed-form-wenzl-bridge`) remain
in the paper as cross-checks; the equivalence is now symbolically
verified.

If a future block introduces a NEW BW-style coefficient via one of
these three forms, the same equivalence pattern should hold; the
script `bw_wenzl_shadow_equivalence.py` can be rerun on the new
partition to confirm.
