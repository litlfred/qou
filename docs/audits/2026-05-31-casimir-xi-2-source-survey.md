# Audit: ξ_2 structural source survey + notation cleanup

**Date.** 2026-05-31
**Block.** [`conj:casimir-epsilon-vacuum`](../../content/quantum-observable-universe/appendix-surreals/casimir-epsilon-vacuum.md)
**User question.** "Explore additional things for β_2? What is β_2 notation? Is it conflating with other notation?"

## Notation cleanup — `β_k` → `ξ_k`

`β` is heavily overloaded in QOU:

| Use | Meaning |
|---|---|
| `β_n^q` | Carlitz q-Bernoulli numbers |
| `β_λ` | Frobenius pairing weight (also written `y_λ`) |
| `β` (decay) | Weak-decay context: `Q_β`, CAL-2, electron from neutron decay |
| `β`-particle | Electron / positron in β decay |
| `β_k` (mine) | Substrate-correction coefficients of Casimir series |

**Decision: rename `β_k → ξ_k`** for the Casimir substrate-correction series. `ξ` is unused in QOU notation register.

Updated master equation:

$$
\frac{F_{\mathrm{Cas}}}{A} \;=\; -\,\frac{\pi^{2}\,\hbar c}{240\,d^{4}} \cdot \Bigl(\xi_{0} + \xi_{2}\,h^{2} + \xi_{4}\,h^{4} + \cdots\Bigr)
$$

with `ξ_0 = 1`, `ξ_{odd} = 0`, `ξ_{even ≥ 2}` open.

## Structural sources surveyed for ξ_2

Four candidate sources investigated:

### Source A — Borromean linking_weight expansion

`linking_weight_A(q) = 5/2 + 3h²/4` from
[`prop:hoefsmit-binding-amplitude`](../../content/quantum-observable-universe/braids-and-knots/proton-mass-substrate-identity.md)
suggests `ξ_2 = 3/4` IF Casimir scales through Borromean.

**NOT APPLICABLE.** Casimir is built from N DISJOINT unknots
(per the Hoefsmit additivity probe). `linking_weight(N · ⊙) = 1`
for disjoint components, NO h² expansion. The 3/4 coefficient is
specific to *linked* Borromean rings.

### Source B — Wedderburn rank-2 Markov-trace contribution

For `n` disjoint unknots, `tr_M(1)|_{H_n(q)} = \sum_λ y_λ(q) \cdot \dim V_λ`.

At classical limit (`q → 1`), this equals `1` (identity has trace 1 in any representation). At substrate:

| n | `tr_M(1)|_{H_n}` at substrate | classical | ratio | h²-coef |
|---|---|---|---|---|
| 2 | 0.9946 | 1.0000 | 0.9946 | **−0.124** |
| 3 | 0.9839 | 1.0000 | 0.9839 | **−0.369** |
| 4 | (need computation) | 1.0000 | — | — |

`ξ_2` candidates: `−0.124` (n=2) or `−0.369` (n=3) — they **disagree** by 3×, so the n-dependence doesn't decouple cleanly.

### Source C — q-Casimir element on spin-1 representation

The q-Casimir element of `U_q(sl_2)` has eigenvalue `[j]_q [j+1]_q` on the spin-j module. For `j = 1`:

`[1]_q · [2]_q = 1 · [2]_q = 2.0109 vs classical 1·2 = 2.0`

Ratio: 1.0054, h² coefficient: **+0.125**

This is the "natural" q-Casimir, but it's a 3D-rotational quantity, not a vacuum-energy quantity. Connection to plate-Casimir is indirect.

### Source D — Carlitz q-Bernoulli `β_4^q`

Already in earlier probe: `β_4^q at substrate = −0.0274` vs classical `B_4 = −1/30 = −0.0333`.

Ratio 0.823 → h² coefficient: **−4.04**

This is the "natural q-Bernoulli" route. Off from all other candidates by orders of magnitude.

## Summary of candidates

| Source | ξ_2 candidate | Status |
|---|---|---|
| A — Borromean linking_weight | `3/4 = 0.75` | NOT APPLICABLE |
| B (n=2) — Wedderburn trivial+sign | `−0.124` | Structural but n-dependent |
| B (n=3) — Wedderburn including standard | `−0.369` | Different from B (n=2) |
| C — q-Casimir element on spin-1 | `+0.125` | Different sign |
| D — Carlitz q-Bernoulli β_4^q | `−4.04` | Orders of magnitude off |

**Five sources give values spanning a factor of ~32 (from −4.04 to +0.75), with both signs.** No agreement.

## Honest reading

`ξ_2` is **structurally underdetermined** at present. Different "natural" QOU primitives give wildly different h² coefficients. Without a principled argument that picks ONE source as the correct one, ξ_2 cannot be derived.

This is the same conclusion as the prior sweeps, now expressed in cleaner notation:

- Bar-symmetry: forces ξ_{odd} = 0 ✓
- Rank-0 tree-level: forces ξ_0 = 1 ✓
- Higher even-rank: **OPEN** — multiple structural candidates, no a-priori selection principle

The Casimir prefactor `π²/240` at leading order is derived. The substrate correction `ξ_2 h²` (~few percent at substrate) is genuinely open — five candidate sources give five different values.

## What WOULD pin down ξ_2

To force a unique ξ_2 value, QOU would need one of:

1. **A specific construction of N_⊙(A, d)** that maps each plate mode to a specific Wedderburn block of a specific Hecke algebra. The block structure would then determine which y_λ(q) appears at h² order.

2. **A categorical regularization scheme** (beyond standard ζ-reg) that's intrinsically QOU — one that commutes with the Hecke decomposition. This would select one q-zeta over others.

3. **An auxiliary observable that constrains ξ_2**. For example, if some related QOU prediction (perhaps Lamb shift or vacuum polarization) shares the same ξ_2 and has a known measured value, that pins it down.

Until one of these lands, the conjecture's prediction is:

```
F_Cas/A at substrate  =  -π²ℏc/(240 d⁴) · (1 + ξ_2 h² + …)
                      ≈  -π²ℏc/(240 d⁴) · (1 + ξ_2 · 0.044 + …)
```

with `ξ_2 ∈ [-4, +1]` from the candidate survey. Depending on |ξ_2|, the QOU prediction at substrate deviates from textbook by **anywhere from −18% to +3%**. Current experimental tolerance (~1%) cannot distinguish; **a ~0.1% precision Casimir experiment could narrow ξ_2 to a specific value**, which would be a major experimental test of QOU.

## Status update

| Sub-problem | Status |
|---|---|
| 1 (existence of N_⊙) | Open |
| 2 (A/d³ scaling) | Derived at rank 0 |
| 3 (ξ_0 = 1, ξ_{odd} = 0) | **DERIVED** (rank-0 + bar-symmetry) |
| 4 (ξ_2, ξ_4, … even-rank corrections) | OPEN — 5 candidate sources, no consensus |

The notation cleanup (`β → ξ`) makes the open content sharper: it's the even-rank coefficients of the `h`-graded substrate-correction series, NOT the prefactor itself.
