# Bar-oddness discriminates the two `Q_β` elements — `Δ_S` carries it on the whole admissible span, `Δ_L` only at zero

**Date:** 2026-09-07 · **Beans:** `qou-99qc` (Option E), `qou-avt5`, `qou-e58e`, `qou-37j2`
**Probe:** [`qbeta_bar_odd_element_discriminator_probe.py`](../../computations/qbeta/qbeta_bar_odd_element_discriminator_probe.py) — 13/13, exact over ℚ(q)
**Tier:** an exclusion of `Δ_L` **within the admissible span over ℚ** (§4); scope-(a) outside it (§4a).
**Nothing wired, no functional adopted, no element declared canonical.**

Continues [the bar-parity finding](2026-09-07-bar-parity-separates-the-admissible-qbeta-functionals.md),
which closed the *functional* column for `Δ_S`. That document's own "what was NOT done" said the
`Δ_L` column had not been recomputed. This does it, and the answer is stronger than expected: the
same parity **also separates the two elements**, and on the whole admissible span rather than at
the two sampled points.

---

## 1. Why this is a physics test, not an aesthetic one

The criterion needs a reason, and the corpus supplies one it measured rather than posited.

[`2026-08-19-bar-involution-is-isospin-conjugation.md`](2026-08-19-bar-involution-is-isospin-conjugation.md)
(`qou-e58e`) establishes that **`bar: q ↦ 1/q` IS proton↔neutron conjugation**:

> `L(Z, N; q) − L(N, Z; 1/q) = δ(q)`, with `δ` independent of `(Z,N)`

verified over **11 nuclei at five values of `q`**, spread `7.9e-24` at `q₀`. And at bond level the
identification is exact — `p–p` carries `1/z`, `n–n` carries `1/z̄`, so **`p ↔ n` under bar is
exactly `z ↔ z̄`.**

`Q_β` is the **neutron-minus-proton** decay Q-value, and its element is `Δ = 𝓑_n − 𝓑_p` — a p↔n
**difference**. Under a conjugation that swaps `p` and `n`, a difference reverses sign. So the
element's trace should be **bar-odd**:

> `bar(N) = −N`, where `N(z) = tr_M(Δ)(z)`

No anchor, no experimental input, no fitted quantity enters. It is an identity in `ℚ(q)`.

## 2. The two elements

Both taken from committed artifacts, not rebuilt:

| element | what it is | `tr_M` in `z` |
|---|---|---|
| `Δ_S` | Gröbner–Shirshov **normal-form** difference `NF(n) − NF(p)` | **affine**: `h²/2 − hz` |
| `Δ_L` | the eleven-crossing raw **word** difference `β_n − β_p` | **quadratic** (fork-pricing witness) |

The degree difference is itself structural and was not put in by hand.

## 3. The result

**`Δ_S`** — `bar(N) = −N ⟺ bar(z) = z − h`. **One** branch:

| `z` | `bar(z)` | bar-odd | admissible under D |
|---|---|:--:|:--:|
| `z = q` (augmentation) | `1/q` | **✓** | ✓ |
| `z_D = q³/(q²+1)` (Markov D) | `1/(q(q²+1))` | **✓** | ✓ |
| `z = 1` (published) | `1` | ✗ | ✗ |
| `z_C = √q/(q+1)` (excised C) | `√q/(q+1)` | ✗ | ✗ |

**Bar-oddness holds for exactly the two admissible functionals.**

**`Δ_L`** — the criterion is quadratic, giving two branches
`bar(z) ∈ {−z, (q⁴z + 2q³ − 2q + z)/(q⁴+1)}`. **None of the four satisfies either — the admissible
pair included.**

> So under the isospin reading, **`Δ_S` paired with an admissible functional is bar-odd; `Δ_L`
> paired with an admissible functional is not.**

That is a structural preference for `Δ_S` in a question the decision document records as **open and
independent of the functional question** — reached without touching a number, and therefore not a
selection against the data.

## 4. The whole admissible span — and this is the statement that matters

Testing only the two Markov points **under-claims**. The decision document records (§2, fact 3)
that the admissible **traces** form a **2-dimensional space** which those two points span. So the
real question is whether *any* combination is bar-odd. Measured:

| element | `bar(A) + A` (augmentation defect) | `bar(B) + B` (`z_D` defect) | verdict |
|---|---|---|---|
| **`Δ_S`** | `0` | `0` | **every** admissible trace is bar-odd |
| **`Δ_L`** | `−(q−1)²(q+1)²(q²+1)³/(4q⁵)` | `−(q−1)²(q+1)²(q²+1)(q⁴+1)/(4q⁵)` | **only the zero trace** |

The `Δ_L` row is an exclusion, not a sample: the two defects have ratio `(q²+1)²/(q⁴+1)`, which is
**q-dependent**, so they are not proportional over ℚ and `a·dA + b·dB = 0` forces `a = b = 0`.

> **`Δ_S` carries bar-oddness on the entire admissible trace space; `Δ_L` carries it nowhere but
> at zero.**

## 4a. 🛑 What is still not settled

**Coefficients in `ℚ(q)` were not tested.** If the span is taken over `ℚ(q)` rather than `ℚ`, `bar`
acts on the coefficients too and the condition becomes a functional equation in two unknowns,
generically solvable. Scaling a trace by `f(q)` rescales `Q_β` itself, so it is a *different
physical claim* rather than merely a wider search — but it is untested either way.

**Non-admissible `z`.** `Δ_L`'s second branch is **involution-consistent** (`B̄(B(z)) − z = 0`
identically), so some `z` outside the admissible set may make it bar-odd. Irrelevant to the physics
— an inadmissible functional is excluded on other grounds — but it means *"`Δ_L` can never be
bar-odd"* is **not** what was shown. Branch `bar(z) = −z` is vacuous for a positive Markov
parameter throughout.

**And the premise is load-bearing.** If bar is *not* p↔n conjugation, the criterion loses its
motivation and this reduces to an observation about two rational functions. That reading is
`qou-e58e`'s, measured, and is cited rather than assumed — but it is the hinge.

## 5. Calibration, and a defect it found

The `Δ_L` closed form reproduces the committed fork-pricing witness's own `Q_pred` to **8.5e-51** at
60 dps — byte-exact, so the algebra is the corpus's own.

It did **not** reproduce that witness's `err_pct` to `1e-12`, and chasing that found the reason is
not the algebra:

```
Q_β reference implied by the witness :  0.7823334093099085
codata_constants.Q_BETA_MEV today    :  0.78233341          <- EIGHT significant figures
relative difference                  :  8.8e-10
```

**A truncated reference in a corpus that computes at 60 dps** — the same class as the `σ = 0.15`
rounding fixed in the α_EM producer earlier today (`0.15` was a 2 % truncation of `0.15325`). My
tolerance was simply tighter than the reference's own precision. **Recorded, not fixed here** — it
is a `codata_constants` question, not this probe's.

## 6. What was NOT done

- **No functional adopted, no element declared canonical.** The seven-option decision is the
  owner's (`qou-99qc`), and this changes none of the arithmetic in its grid.
- **No search for a branch-2 solution** on `Δ_L`, and no test of `ℚ(q)` coefficients — §4a.
- **No claim that bar-oddness is sufficient** for admissibility; the sibling document already
  refuted that on `Δ_S` by exhibiting a passing non-root.
- **`Q_BETA_MEV` not touched.**

-- Ref: [manuscript] beans qou-99qc, qou-avt5, qou-e58e, qou-37j2
