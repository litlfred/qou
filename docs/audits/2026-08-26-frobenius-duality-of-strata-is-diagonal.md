# The Frobenius duality of curvature-rank strata is diagonal, not anti-diagonal

**Bean:** `qou-xsv8` (all three fix steps). **Scope:** **(b)** structural
exclusion on the *justification*; the invariant is mutual annihilation of
distinct central primitive idempotents, which holds for every linear functional
and every `n`.

## Two blocks, one sentence, same defect

Both assert a Poincaré-type duality pairing *distinct* curvature-rank strata of
the centre `Z(H_n(R,q))`:

| block | asserted |
|---|---|
| `prf:spectral-sequence-collapse` §"Frobenius duality of strata" | `(J^ℓ)^⊥ = J^{N−ℓ}`, "rank-ℓ contributions pair with rank-(N−ℓ) contributions" |
| `prf:quantum-dilogarithm-stratified` Step 1 | `⟨Z^(k), Z^(ℓ)⟩ = 0` whenever **`k + ℓ ≠ N`** |

The second cites the first. Both then read the strata off the **central
primitive idempotents** `e_λ` ("enumerate central idempotents, compute their
GB-depth, bin by depth(λ)").

## Why it cannot hold on that basis

Distinct central primitive idempotents mutually annihilate. So for **any**
linear functional `φ`,

```
φ(e_λ · e_μ)  =  φ(δ_{λμ} · e_λ)
```

and the Gram of `B(x,y) = φ(xy)` restricted to `Z` in the idempotent basis is
`diag(φ(e_λ))` — **diagonal**. Every stratum is **self**-dual; every pair of
*distinct* strata pairs to **zero**. The annihilator of a stratum inside `Z` is
the span of the *complementary* idempotents — a set complement, not a
rank-reindexed stratum.

So the asserted cross-stratum pairing is identically zero exactly where it
claims to be perfect, whenever `ℓ ≠ N − ℓ`.

## Measured, not merely argued

The one-line identity above is not worth "verifying". What is worth measuring is
that the corpus's **own** idempotents, at the one `n` where it has them
explicitly, produce a diagonal Gram with nonzero diagonal — i.e. that the strata
are self-dual, so the cross-stratum pairing is *zero* rather than merely
unproved.

[`computations/probes/centre_frobenius_pairing_is_diagonal_probe.py`](../../computations/probes/centre_frobenius_pairing_is_diagonal_probe.py)
takes the exact `ℚ(q)` idempotent coefficients committed in
`probe-h3-central-idempotents-exact.witness.json` (n = 3, six-word basis) and
computes the Gram **without multiplying in the algebra at all**, via the
symmetrizing-trace duality `τ(T_u T_v) = δ_{u,v⁻¹}`:

```
τ(x y) = Σ_u a_u · b_{u⁻¹}
```

so only the inversion permutation on `S_3` is needed — `(3 4)` in the committed
word order. This computes the Gram **independently of** the orthogonality
assertion `A2` of the source probe, rather than citing it.

Result, exact in `ℚ(q)`:

```
              e_(3)                    e_(2,1)              e_(1,1,1)
e_(3)      1/(q⁶+2q⁴+2q²+1)               0                     0
e_(2,1)           0              2q²/(q⁴+q²+1)                  0
e_(1,1,1)         0                       0          q⁶/(q⁶+2q⁴+2q²+1)
```

- **A1** all six off-diagonal entries are identically `0` in `ℚ(q)`.
- **A2** all three diagonal entries are nonzero — each stratum is self-dual.
- **A3** self-test: `Σ_λ τ(e_λ) = 1`, which is forced by completeness
  `Σ_λ e_λ = 1`. This validates *both* the `τ(T_u T_v) = δ_{u,v⁻¹}` rule and the
  committed coefficients; if either were wrong, A3 fails.
- **A4** `B(e_λ, e_λ) = τ(e_λ) =` the `T_e` coefficient, as it must be for an
  idempotent.
- **A5** at the proton pin: `0.11947…`, `0.65709…`, `0.22344…`, summing to `1`
  to better than `1e-45`.

Exact `ℚ(q)` throughout; the single numeric evaluation Horner-evaluates
integer-coefficient numerator and denominator separately in `mpf`. No `float64`,
and no sympy `Float` substitution — which would have set the working precision
from the literal rather than from `mp.dps`.

## The correction *repairs* Step 4 — it does not break it

This is the part worth carrying forward, because the usual expectation is that
finding a defect costs something downstream. Here it is the opposite.

Step 4 argues that `φ_q^(k)(z_i) ∈ Z^(k)(A)` pairs to zero with any `T_w` whose
`Z^(k)`-projection vanishes. That is exactly `⟨Z^(k), Z^(ℓ)⟩ = 0` for
**`k ≠ ℓ`** — the diagonal statement.

Under Step 1 as written, the pairing was licensed to be **non-zero** at
`ℓ = N − k`. So whenever `N − k ≤ k_⋆(T_w)`, Step 4's truncation **did not
follow** from Step 1. The corrected diagonal statement closes that hole.

## What is NOT claimed

- **Not** that either block's conclusion is false. This is scope (a) on the
  *step*: `prf:quantum-dilogarithm-stratified`'s truncation identity and
  `prf:spectral-sequence-collapse`'s *Practical consequence* both survive — the
  latter uses the Wedderburn sum, not this duality.
- **Not** that `(J^ℓ)^⊥ = J^{N−ℓ}` fails on the whole algebra `A`. Annihilator
  duality on a filtered Frobenius algebra is standard and is untouched here. The
  defect is the **transport** of that statement to the centre's idempotent
  strata.
- **A second refutation I considered and discarded.** `gbDepth_pos`
  (sorry-free) proves the partition grading never occupies degree `0`, and at
  `n = 4` the occupied degrees are `{3, 4}` (`gbDepth [2,2] = 3`, hooks `= 4`),
  so the partners `{1, 0}` required by `ℓ ↔ N − ℓ` are both empty. That looks
  decisive and **is not**: it assumes `N` is the top *occupied* degree. `N` is
  not pinned by the block, and `{3,4}` is symmetric about `3.5`, so `N = 7`
  pairs `3 ↔ 4` and the count objection evaporates. Recorded because it is the
  same shape-vs-object error this bean is about, nearly committed while writing
  about it.

## Why supplying the missing bridge would not have repaired this

The `wpdb` backlog is about a *word*-depth-to-*partition*-depth bridge that does
not exist. Three sessions have gone into it. This defect is **independent of
that bridge**: `φ(e_λ e_μ) = 0` holds whatever the filtration is. Anyone
draining the `wpdb` backlog would have marked these two sites fixed and moved on.

## Recorded as a criterion

Added as **question 5** of `da-arity-conflation` in
[`local/devils-advocate-watcher`](../../.claude/skills/local/devils-advocate-watcher.md):
*"Transported to a basis that destroys the property?"* — a structural property of
a pairing is relative to a basis, so before restating it on a different basis,
check that basis's own multiplication.
