# Φ₁ has a closed form — and no real *z* makes it the recorded column

**Date:** 2026-09-12
**Beans:** `qou-1jw9` (does the formula's own `M_i` constructor reproduce the table?), `qou-jgg0`
**Probes:**
[`phi1_is_chain_additive_iff_z_is_an_eigenvalue_probe.py`](../../computations/probes/phi1_is_chain_additive_iff_z_is_an_eigenvalue_probe.py) — 20/20 (the algebraic obstruction)
[`phi1_closed_form_and_no_z_reproduces_it_probe.py`](../../computations/probes/phi1_closed_form_and_no_z_reproduces_it_probe.py) — 19/19 (this document)

---

## 0. What was open

`thm:wedderburn-mass-formula` defines three invariants. Two of them closed:
[`phi_allpairs_reconstruction.py`](../../computations/phi_allpairs_reconstruction.py)
reproduces Φ₂ and Φ₃ on 19 of 19 non-hydrogen rows of the Z=1–20 table, and
records in its own header that **"Φ₁ is NOT closed here"**. Φ₁ has been the
standing gap under every reading of the atomic braid.

The reason it resisted was established earlier the same day: with
`f(M) = z·M₁₂ + M₂₂`, the identity `f(AB) = f(A)·f(B)` holds only when
`c(z² − hz − 1) = 0` — i.e. `z ∈ {q, −1/q}`, the eigenvalues of `σ`. `det` and
the sym/alt eigenvalue ratio *are* multiplicative, which is exactly why Φ₂ and
Φ₃ collapsed to per-pair sums and Φ₁ did not.

That explained the resistance. It did not evaluate Φ₁.

## 1. Φ₁ is closed

Every crossing in Table 1 is `c·σ + d·1` in the **same**
`σ = [[h,1],[1,0]]` (trace `h = q − 1/q`, determinant −1, eigenvalues `q` and
`−1/q`). Diagonalising with `V = [[q, −1/q],[1,1]]`:

    M_i = V · diag(P_i, Q_i) · V⁻¹,
    P_i = Π_{j>i} (c q + d)  = Π λ^sym,
    Q_i = Π_{j>i} (−c/q + d) = Π λ^alt,

    (M_i)₁₂ = (P_i − Q_i)/(q + 1/q),
    (M_i)₂₂ = (P_i/q + q Q_i)/(q + 1/q),

so

    Φ₁(z) = Σ_i ln| P_i·(z + 1/q) + Q_i·(q − z) |  −  (n−1)·ln(q + 1/q).

Verified against the literal 2×2 matrix product to **3.1e-39** on He, Li and C
(probe check 4). Φ₁ is therefore closed in exactly the per-pair data that closed
Φ₂ and Φ₃ — Table 1's `(c, d)` and the all-pairs counts. What it is not is
per-pair **additive**.

At `z = q` the second term vanishes and Φ₁ degenerates to `Σ_{i<j} ln|c q + d|`;
at `z = −1/q` the first does. So the eigenvalues are precisely the `z` at which
the closed form collapses to a single factor — the algebraic obstruction,
confirmed numerically (check 5, agreement 3.3e-39).

## 2. Order-independence, and a prediction of mine that was wrong

Because all six crossing matrices are polynomials in one `σ`, they **commute
exactly** — max commutator `0` over all 81 ordered pairs (check 2). The transfer
algebra is `ℝ[x]/(x² − hx − 1)`, commutative.

So [`wedderburn_Mi_constructor_test.py`](../../computations/wedderburn_Mi_constructor_test.py)'s
retraction — *"an ALL-PAIRS braid with no ordering dependence"* — is correct, and
correct for a stronger reason than it gives: it holds for Φ₁ too, not only for
the two multiplicative invariants.

**🛑 I predicted the opposite.** Reasoning from the non-multiplicativity of `f`,
I expected Φ₁ to depend on the strand arrangement and on the order of `j` inside
`M_i`, and said so before measuring. Measured: identical to 10 digits across five
arrangements (`p,n,e` / `e,p,n` / `p,e,n` / `n,p,e` / `e,n,p`) and both `j`-orders,
on He, C and Ca; spread 1.3e-39. **Non-multiplicativity of `f` does not imply
order dependence of Φ₁**, because the matrices being multiplied commute. The
inference was invalid, and the conclusion I drew from it was false.

## 3. No real *z* reproduces the recorded column

Φ₁(z) has `n−1` poles — one per generator, where the argument vanishes — so it
is **unbounded below**, and neither a sign argument nor a growth argument
settles the question on its own. The honest test is consistency: **one parameter
against 19 constraints.**

Minimising the worst relative miss over all 19 rows:

| | best *z* | worst relative miss | worst row |
|---|---|---|---|
| `A+Z` reading (canonical) | ≈ 1.05 | **≈ 5.2 (520 %)** | Ar |
| `A` reading (electron-free) | ≈ 1.1 | **≈ 6.4 (640 %)** | Ar |

**Quote the order of magnitude, not the minimiser.** The reported best `z` and
its miss move with the scan grid — a 2001-point scan gives `z = 1.0537` / 5.24, a
401-point scan `z = 0.926` / 5.84 — because the function is pole-ridden and the
basin is shallow. What is robust across resolutions is that the best achievable
miss is several hundred per cent, never near zero.

The three documented `z` are far worse still, and fail in two independent ways:

- **Sign.** Φ₁ > 0 at convention C, convention D and `z = q` on every row from
  B upward; every recorded value is negative (He −5.559 … Ca −55.937).
- **Growth.** Φ₁ is Θ(n²) — its per-pair density `Φ₁/C(n,2)` varies only 6.1×
  across `n = 6..60`. The recorded column's density varies 12.4× and *falls*
  monotonically (−0.371 at He → −0.032 at Ca), i.e. Θ(n).

## 4. What this relocates

The sibling probe
[`beta3_deviation_is_isolated_to_the_coefficient_probe.py`](../../computations/probes/beta3_deviation_is_isolated_to_the_coefficient_probe.py)
established that the recorded **Φ₃** column *is* the theorem's Φ₃, at the
documented anchor: `w·ln q₀` with `w = −2Z − N(N−1)` an exact integer.

Putting the two together: the recovered producer `atom-mass-complete-wedderburn`
agrees with the published formula on **Φ₂ and Φ₃** and disagrees on **Φ₁**. Two
of three invariants are shared. So the `β₃ = 0.0499` vs `h_A² = 0.0437073`
departure (14.2 %) and the Φ₁ disagreement sit on the same object, and neither is
explained by the anchor — the table is neither the formula's output nor unrelated
to it.

## 5. Scope — what is **not** established

- **Scope-(a) turning on a named class, not a universal exclusion.** What is
  excluded is the theorem's own Φ₁, on the all-pairs reading, with Table 1's
  crossing values, for any **real** `z`, on the `A+Z` and `A` strand contents.
- **Not excluded:** a different `M_i` reading (the adjacent-suffix reading is
  separately refuted in `wedderburn_Mi_constructor_test.py`), a complex `z`, a
  different crossing table, or the possibility that the recorded Φ₁ column is
  some other quantity entirely.
- **The quark-level readings (`3A`, `3A+Z`) are not testable here.** Table 1's
  rows are nucleon- and electron-typed; there is no quark-level crossing table to
  evaluate.
- **No replacement is proposed.** Solving the table for the `z` or the
  coefficient that reproduces it, and adopting it, is the fit the owner's
  2026-09-05 directive forbids. The scan reports that no `z` works and stops.
- **Φ₁ being closed does not make the mass formula accurate.** It makes Φ₁
  *evaluable*; §3 is the measurement of what that evaluation gives.

## 6. Open, and staying open

`qou-1jw9` and `qou-jgg0` both stay open (rule 13a). Still open:

- what the recorded Φ₁ column actually is, if not the theorem's Φ₁;
- the `β₃` vs `h_A²` authoring question, which is the owner's call;
- whether a quark-level crossing table would change §3;
- `qou-jgg0`'s `3A+Z` third cell.
