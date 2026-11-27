# Σ(2,3,5) Ohtsuki series: Borel resummation at the substrate pin (bean `qou-6gf9`, option 2)

Date: 2026-11-27. Probe: `computations/mu_p_sigma235_borel_resummation_probe.py`
(witness `mu-p-sigma235-borel-resummation.witness.json`, 5/5 assertions).
Lean: `QOU/BraidsAndKnots/PoincareSphereBorelSectors.lean` (sorry-free, no axioms
except `propext` in one lemma; lean-direct v4.24.0 exit 0).

Follows `mu_p_sigma235_ohtsuki_resolution_probe.py`, whose scope section left the
resummation route open.

## Mathematics

1. **Identification (exact).** With `A(q) = Σ_{n≥1} χ₊(n) q^{(n²−1)/120}` (χ₊ = +1 on
   1, 11, 19, 29 and −1 on 31, 41, 49, 59 mod 60), the `q → 1` expansion of
   `(A/2 − 1)/(q(1 − q))` equals the Ohtsuki series of `I(Σ(2,3,5); q)` exactly through
   order 11 (`1, −6, 45, −464, …`). This is lovejoy2026 eq. (LZ0) read as an identity of
   asymptotic expansions. It is computed from Bernoulli-polynomial L-values, independently
   of the Pochhammer expansion.
2. **Borel transform (closed form).** With `q = e^{−t}` and `s(j) = Σ_a χ₊(a) sin(2πja/60)`,
   `B(ξ) = (1/π) Σ_j (s(j)/j)(1 − 30ξ/(π² j²))^{−1/2}`. The singularities are at
   `ξ_j = π² j²/30` on the positive axis, for `j² ≡ 1` or `49 (mod 120)`, which are the
   Chern–Simons values −1/120 and −49/120.
3. **At the pin `q0 > 1` the series is Borel summable, with no ambiguity.** Here `t0 < 0`,
   so the Laplace contour avoids every singularity. The median sum equals the lateral sums
   and equals the unique Borel sum:
   `I_B(q0) = 0.615226114690480398678796272945…`. A Borel–Padé [22/22] check agrees to
   2.6e−23. `I_B` lies between the partial sums 0.340 and 0.884, inside the least-term
   envelope.
4. **On the bar side `1/q0 < 1`, the positive axis is a Stokes line.** The median sum
   equals the convergent false theta to 4e−40. The lateral sums jump by 0.174 (j = 1).
5. **Trans-series sectors at the pin are `exp(−c₁ j²)`, with `c₁ = π²/(30|log q0|) = 3.1530`.**
   j = 1 gives 4.27e−2 and j = 7 gives 7.99e−68. Lean `dualSupport_action_gap` proves that
   no sector has `j²` strictly between 1 and 49.

## Comparison (the measured residual enters only here)

`t_res = 2.1116e−7` (211.16 ppb, live tension witness, CODATA 2022).

| a-priori quantity at q0 | value | / t_res |
|---|---|---|
| Borel sum `I_B(q0)` | 0.6152 | 2.9e6 |
| `|I_B − optimal truncation|` | 0.2692 | 1.3e6 |
| sector j = 1, `e^{−c₁}` | 4.27e−2 | 2.0e5 |
| Stokes jump at `1/q0`, j = 1 | 0.1743 | 8.3e5 |
| sector j = 7, `e^{−49c₁}` | 7.99e−68 | 3.8e−61 |

**Finding, scope (a).** The resummation produces only O(1) values and the sectors
`e^{−c₁ j²}`. The residual sits in the empty gap between j = 1 and j = 7, a gap of 66
decades. So no single quantity produced by this resummation of this series at q0 is of
the residual's size. Under the other corpus convention (Habiro `q = q0²`), `c₁ = 1.5765`,
j = 1 gives 0.207 and j = 7 gives 2.8e−34. The gap still contains `t_res`.

**A coincidence that is not a sector.** `e^{−5c₁} = 1.42e−7` (ratio 0.67). The
trans-series of this series is linear in the sectors `j²`, and 5 is not a square, so
there is no five-instanton term. Choosing the power 5 would be selection against the
target (AGENTS.md, no-fitting rule). It is recorded so that the next agent does not read
it as a lead.

**What this does not exclude (scope (a)).** It does not exclude the Habiro-basis
coefficients themselves, evaluation at roots of unity, other Brieskorn spheres, a
derived formula that multiplies a sector by a separately derived small factor, or
Écalle-type resurgent structure of a different invariant. It does exclude reading the
residual off a single resummed quantity or sector of `I(Σ(2,3,5))` at the q0 pin.
