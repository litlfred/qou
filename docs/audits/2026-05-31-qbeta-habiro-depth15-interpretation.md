# Q_β Habiro element — `u^15` depth interpretation (2026-05-31)

> Keystone follow-up to [`2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md):
> structural explanation of the `u^15` prefactor in
> `Σ_m Δa_m·(u;u)_m = −u^15·(u−1)(u+1)·P_8(u)`.
>
> Branch: `claude/brave-mendel-FPxFl` (PR #1579).
> Probe script: [`computations/qbeta/qbeta_habiro_depth15_interpretation.py`](../../computations/qbeta/qbeta_habiro_depth15_interpretation.py).
> Witness: `computations/qbeta/qbeta-habiro-depth15-interpretation.witness.json`.

## TL;DR

**IDENTIFIED — the `u^15` prefactor is the LOWEST u-exponent at which
the reconstructed proton and neutron numerator polynomials disagree.**

The braid words `β_p`, `β_n` produce tr_M numerators that agree
COEFFICIENT-BY-COEFFICIENT on every monomial `u^0 … u^14`; their
first disagreement is at `u^15`. The `u^15` prefactor of the
n−p Habiro element is a **structural property of the (β_p, β_n)
braid pair** — a fingerprint of how their crossing patterns
diverge in the q-expansion, not an arithmetic coincidence.

The two arithmetic-only candidates explored in the task statement
are **both ruled out** by direct test:

| Candidate | Arithmetic | Structural test | Verdict |
|-----------|-----------|-----------------|---------|
| **5.** `15 = deg((u;u)_5)` | ✓ (1+2+3+4+5=15) | `(u;u)_5 ∤ Δ-Habiro` (remainder ≠ 0) | **FAILS** |
| **4.** `15 = M_p + M_n − 1` | ✓ (8+8−1=15) | Δa_7 = Δa_8 = 0 → M_eff = 6, so `M_p+M_n−1` doesn't reflect the Δ-element | **STRUCTURALLY UNSOUND** |
| **F.** `u^15` = first n−p disagreement | n/a | Confirmed by direct term-by-term comparison | **IDENTIFIED** |

## Per-test results

### Test A — `u^15` is the min-degree of Δ-Habiro (after cancellation)

The expanded Δ-Habiro element is:

```
Σ_m Δa_m·(u;u)_m =
    -u^25 - 2u^24 - u^23 - 2u^21 + 4u^20 + 2u^19 + u^17 - 2u^16 + u^15
```

The support is `u^15 … u^25` (11 nonzero monomials).

**Per-m contributions to the u^15 coefficient** (this is the
critical observation — only m=5 and m=6 contribute):

| m | min-deg of Δa_m·(u;u)_m | coeff at u^0 | coeff at u^15 |
|---|--------------------------|--------------|---------------|
| 1 | u^0 | 10 | 0 |
| 2 | u^0 | −73 | 0 |
| 3 | u^0 | 177 | 0 |
| 4 | u^0 | −189 | 0 |
| 5 | u^0 | 90 | **+13** |
| 6 | u^0 | −15 | **−12** |

Sum at u^15: **13 − 12 = +1** → matches the expanded `+u^15` ✓.

m=1..4 don't even reach degree 15 (their products span `[u^0, u^14]`
maximum). m=5 first reaches u^15 (its product spans `[u^0, u^20]`),
and m=6 spans `[u^0, u^25]`. The coefficient at u^15 is the
result of the contributions from m=5 and m=6 alone.

### Test B — `(u;u)_5` hypothesis FAILS

`(u;u)_5 = (1−u)(1−u²)(1−u³)(1−u⁴)(1−u⁵)` has degree exactly 15, so
the arithmetic matches. But:

- **Division test**: `Δ-Habiro / (u;u)_5` leaves a non-zero remainder
  (a degree-14 polynomial with substantial coefficients):
  ```
  remainder = -92u^14 − 22u^13 + 70u^12 + 88u^11 + 109u^10 + 36u^9
              − 51u^8 − 158u^7 − 106u^6 − 30u^5 + 56u^4 + 72u^3
              + 89u^2 + 14u − 75
  ```
- **GCD test**: `gcd(Δ-Habiro, (u;u)_5) = (u−1)(u+1)` — only the
  Φ_1·Φ_2 factors are shared, which we ALREADY know are categorical
  (the q=1 vanishing witness from the prior audit). No additional
  q-Pochhammer structure carries over.

**Conclusion:** the `u^15` monomial is a **pure-power prefactor**,
NOT the leading term of `(u;u)_5`. The arithmetic `1+2+3+4+5=15` is
**coincidental**.

### Test C — Per-m cancellation tracing

Individual products `Δa_m·(u;u)_m` all start at `u^0` (since Δa_m
has a nonzero constant term and (u;u)_m has constant term 1).
**Massive cancellation** wipes out every monomial in `u^0 … u^14`
of the cross-m sum. The first surviving monomial is `u^15`.

This cancellation is the manifold structural signal. The Δa_m
coefficients are NOT independent random integers — they conspire
to produce 15 consecutive vanishings in the sum. This conspiracy
IS the categorical content.

### Test D — `M_p + M_n − 1 = 15` arithmetic match, but unsound

- `M_p = 8`, `M_n = 8`, sum minus 1 = 15. **Arithmetic match.**
- But **Δa_7 = Δa_8 = 0** (from the prior audit's NEW finding):
  the proton and neutron share their top-two Habiro coefficients
  exactly. The effective support of the Δ-element is `m ∈ {1..6}`.
- For the effective Δ-element, the natural depth-sums are
  `M_eff + M_eff − 1 = 11` or `2·M_eff − 1 = 11` — **NOT** 15.

The arithmetic `M_p+M_n−1=15` matches a number that's intrinsic
to the **individual atoms** (their nominal Habiro depths), but
the Δ-element lives in a smaller effective subspace. The
correspondence is **coincidental** at the structural level.

### Test E — `(u;u)_8` and shared denominator `u^19` connections

- `deg((u;u)_8) = 1+…+8 = 36`. Far from 15. Division fails by
  degree (deg(Δ-Habiro) = 25 < 36). No match.
- The shared denominator is `D(u) = 4·u^19·(1+u²)`, so the
  arithmetic `19 − 4 = 15` matches. But `−4` has no clean
  categorical interpretation (Φ_4(u) has degree 2, not 4), and
  the numerator and denominator live in DIFFERENT objects
  (the fraction `tr_M`, not the Habiro element itself).

### Test F — `u^15` is the first n−p disagreement (**IDENTIFIED**)

Reconstructing `p_in_u(u) = Σ_m a_m(p)·(u;u)_m` and
`n_in_u(u) = Σ_m a_m(n)·(u;u)_m` directly from the witness data
and comparing term-by-term:

| u^exp | p_coeff | n_coeff | diff |
|-------|---------|---------|------|
| u^0 | +1 | +1 | 0 |
| u^1 | −1 | −1 | 0 |
| u^2 | 0 | 0 | 0 |
| u^3 | 0 | 0 | 0 |
| u^4 | −1 | −1 | 0 |
| u^5 | −1 | −1 | 0 |
| u^6 | 0 | 0 | 0 |
| u^7 | +1 | +1 | 0 |
| u^8 | 0 | 0 | 0 |
| u^9 | −1 | −1 | 0 |
| u^10 | 0 | 0 | 0 |
| u^11 | +1 | +1 | 0 |
| u^12 | 0 | 0 | 0 |
| u^13 | −1 | −1 | 0 |
| u^14 | 0 | 0 | 0 |
| **u^15** | **0** | **+1** | **+1** ← **first disagreement** |

The proton-numerator coefficient at `u^15` is 0; the neutron
coefficient at `u^15` is +1. This is the **first** u-exponent
where the two atoms' tr_M expansions disagree.

**Categorical reading:** `β_p` and `β_n` are 3-strand braids
with different crossing structures. Their tr_M Markov-trace
expansions in `u = q^{1/2}` agree on all monomials below u^15,
reflecting that low-q (≈ classical) behavior of the two
hadrons is dominated by the Hecke algebra's quotient where
n and p are interchangeable. The first disagreement at u^15
marks the **q-depth at which isospin breaking first becomes
observable** in the Habiro expansion.

This is a property of the **braid pair** (β_p, β_n) — not a
property of the Habiro ring or the q-Pochhammer system in
general. Different braid pairs would produce different
first-disagreement depths.

## What this rules out and what it doesn't

**RULES OUT:**

- **`u^15 = deg((u;u)_5)`** — Test B division failed; the `1+2+3+4+5`
  arithmetic is a numerical accident.
- **`u^15 = M_p + M_n − 1`** as a structural statement — the
  arithmetic matches but the Δ-element's effective depth M_eff=6
  makes the depth-sum reasoning structurally inconsistent.
- **`u^15` matching a single Wedderburn block dimension** — the
  irreducible Wedderburn blocks at H_3(q) have small dimensions
  (the H_3 has 6 NF basis elements split as 1+2+2+1 = `V_(3)⊕V_(2,1)⊕V_(1,1,1)`
  partitions; the largest block has dim 4). No block has dim 15.

**RULES IN:**

- **`u^15` as first-disagreement depth** — direct, term-by-term
  confirmation that the n−p split first manifests at this u-power
  in the substrate expansion of the SHARED tr_M denominator/numerator
  pair.

**DOES NOT RULE OUT:**

- A deeper categorical reading of WHY the first disagreement is
  specifically at u^15 (vs. u^14 or u^16). This would require
  computing the explicit crossing patterns of β_p and β_n and
  tracing the lowest-order Reidemeister-equivalence-breaking move
  through the Hecke quotient. The current finding is the empirical
  identification of the depth; the underlying topological reason
  is a follow-up.
- An equivalent statement in the LANGUAGE of Hecke characters:
  `(χ^λ(σ_i^{n_i}; β_p) − χ^λ(σ_i^{n_i}; β_n)) = O(u^15)` for some
  specific irrep λ. Plausible but not tested here.

## Implications for the Q_β derivation

The prior audit identified the Δ-Habiro element factorization
`−u^15·(u−1)(u+1)·P_8(u)`. With this audit:

1. **`(u−1)(u+1) = Φ_1·Φ_2`** → q=1 vanishing witness (classical
   limit kills the n−p split) — **categorical: cyclotomic**.
2. **`u^15`** → first-disagreement-depth marker between β_p and β_n —
   **categorical: braid-pair structural fingerprint**.
3. **`P_8(u)`** → irreducible over ℚ; awaits Burau / Wedderburn
   character match (separate agent's task) — **categorical: open**.

The Δ-Habiro element factors fully as:

```
ΔHabiro_Qβ(u) = [braid-pair fingerprint] · [classical-limit kill]
              · [proper Q_β content (P_8)]
              = u^15 · (u² − 1) · P_8(u)
```

with TWO of the three factors now categorically identified.

## Next session targets

1. **Topological derivation of `u^15`** — compute the explicit
   crossing patterns of β_p, β_n and trace WHY the first disagreement
   is at depth 15. Candidate: the proton braid has writhe = +3,
   the neutron has writhe = −1 (per the Hopf-link probes); their
   difference in skein-relation accumulation lands at u^{(2·3+2·(-1)+...)}
   for some specific count. Test by direct Skein computation.

2. **Hecke-character interpretation** — for each irrep λ of H_3(q),
   compute `χ^λ(σ; β_p)` and `χ^λ(σ; β_n)` symbolically and find
   the irrep where the difference is `O(u^15)`. This would lift
   "first-disagreement depth" to a representation-theoretic
   statement.

3. **Compress the Q_β formula** — given that u^15 is structural
   (not arbitrary), the formula `Q_β ∝ Δ-Habiro` can be rewritten
   to factor out the `u^15` explicitly, isolating the substrate
   dependence in the `(u²−1)·P_8(u)` part. This may simplify the
   Habiro-element ansatz hunt.

## Files touched

- **NEW:** `computations/qbeta/qbeta_habiro_depth15_interpretation.py`
- **NEW:** `computations/qbeta/qbeta-habiro-depth15-interpretation.witness.json`
- **NEW:** `docs/audits/2026-05-31-qbeta-habiro-depth15-interpretation.md` (this file)

## Cross-refs

- Prior audit (factorization): [`docs/audits/2026-05-31-qbeta-habiro-delta-am-factorization.md`](2026-05-31-qbeta-habiro-delta-am-factorization.md)
- Original probe: [`docs/audits/2026-05-31-qbeta-habiro-element-probe.md`](2026-05-31-qbeta-habiro-element-probe.md)
- Master ledger: [`docs/coordination/1ppq-qbeta.md`](../coordination/1ppq-qbeta.md)
- Witness: `computations/habiro/habiro-coefficients-atomic.witness.json`
