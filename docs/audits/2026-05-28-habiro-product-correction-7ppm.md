# Audit: Habiro correction product (1+ℏ²)(1−ℏ²/p(n)) closes to 7.8 ppm

**Date:** 2026-05-28

## Finding

The Habiro normalization bridge has a product correction:

```
Habiro ≈ tr_M × (n!/[n]_q!) × (Vol(4₁)/ℏ²) × (1+ℏ²)(1−ℏ²/p(n))
```

where p(n) = p(9) = 30 is the number of partitions of 9 (= number
of Wedderburn blocks in H₉(q)).

| Level | Correction | Residual |
|-------|-----------|----------|
| 0 | bare | 9495 ppm |
| 1 | ×(1+ℏ²) | 319 ppm |
| **2** | **×(1+ℏ²)(1−ℏ²/p(n))** | **7.8 ppm** |

This is a **41× improvement** over the (1+ℏ²) correction alone,
and a **1218× improvement** over the bare bridge.

## Product structure

Expanding:
```
(1+ℏ²)(1 − ℏ²/30) = 1 + (29/30)ℏ² − ℏ⁴/30
```

This gives:
- c₂ = 29/30 ≈ 0.9667 (observed: 0.9671 — match to 0.04%)
- c₄ = −1/30 ≈ −0.0333

## Algebraic mechanism

The Habiro sum uses **(q;q)_m = Π(1−q^k)** while the Markov trace
uses **(u;u)_m = Π(1−u^k)** with u=√q, divided by denom=4u²¹+4u¹⁹.

The key identity: **(1−q^k) = (1−u^k)(1+u^k)** since q=u².

Therefore:
```
hab_A / hab_B = <Π_{k=1}^m (1+u^k)>_{Habiro}
bridge = denom × <Π(1+u^k)>_{Habiro} ≈ 127.73
```

The Plancherel × Vol/ℏ² × (1+ℏ²)(1−ℏ²/30) approximation to this
bridge holds to 7.8 ppm. The 30 = p(9) coincidence (number of
partitions of 9 = number of Wedderburn blocks) remains suggestive
but the direct mechanism is the Pochhammer convention ratio.

## Remaining 7.8 ppm

The third correction factor c₃ ≈ 0.000796 has PSLQ candidates:
- 1/(2·p(n)²) = 1/1800 ≈ 0.000556 → residual 2.4 ppm
- 1/p(n)² = 1/900 ≈ 0.00111 → residual −3.1 ppm

Both are structurally motivated (powers of p(n)), but neither is
exact. The 7.8 ppm residual at ℏ⁶ order may need the full H₉
character theory for closure.

## Cross-references

- Prior: `2026-05-28-habiro-residual-319ppm.md` (Level 1)
- Prior: `2026-05-27-habiro-normalization-decomposition.md` (Level 0)
- Compute: `habiro_correction_product_verify.py`
- Witness: `habiro-correction-product.witness.json`
