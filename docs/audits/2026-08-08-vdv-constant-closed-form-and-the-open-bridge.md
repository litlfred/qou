# Van der Veen's constant, evaluated — and exactly what still stands between it and `c_σ`

**Date:** 2026-08-08 · **Beans:** `qou-fl4t`, `qou-pn5j`, `qou-vdvE`, `qou-vdvS`
**Probe:** `computations/probes/one_loop_vdv_constant_closed_form_probe.py`
**Lean:** `QOU/OneLoopPrefactorInvariance.lean` · **Paper:** `prop:one-loop-prefactor-provenance`
**Follows:** `docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md`

## The short version

The constant this corpus measures as `c_σ` is, up to a normalisation not yet
computed, the constant `E` in van der Veen's asymptotic for Whitehead chains. He
produces it explicitly and then evaluates it only far enough to show it is
nonzero, deferring the rest to a sequel he never wrote. It is a Gaussian orthant
probability, and it closes in elementary functions for exactly the two links this
corpus uses. Both values are now computed.

What that does **not** do is derive `c_σ`. The remaining bridge is named below,
and it is measurably cusp-dependent, so it cannot be inferred from one link.

## What van der Veen actually leaves open

His Main theorem gives, for the family `W_{a,b,c,d}`,

```
J_N(W)(e^{2πi/N}) ~ exp{ (1/2π)[ (Vol + iCS)·N + D·log N + E ] },   D = 3π for b = 1
```

The `D` half is a theorem and settles the `N`-power question this corpus had
open (see the previous audit). The `E` half is produced in the proof of Lemma 4
as a `(c+d+1)`-dimensional Gaussian integral, and **Step 6 reduces it to one
dimension himself**:

```
Q_∞ = C · ∫₀^∞ exp(−π A w²/2) · erfc(√(π/2)·w)^n dw ,
A := (c+d) − (4a+c−d)i ,   n := c+d
```

He then shows the imaginary part is nonzero and stops. His closing paragraph:

> "In the same paper it is also conjectured that the number `E` is determined by
> the Ray-Singer torsion of the complement twisted by the holonomy
> representation. We hope to investigate these conjectures for the Whitehead
> chains in a subsequent publication."

That conjecture (Gukov–Murakami) *is* this corpus's `c_σ ↔ τ` question, for
links, stated as open at the end of the paper the corpus reads its Whitehead
colored-Jones values from.

## Why it closes, and only just

Each `erfc` is a half-space indicator integrated out, so the `n`-fold product
against a Gaussian is an **`(n+1)`-dimensional Gaussian orthant probability**.
Those have elementary closed forms exactly for `n ≤ 2` — bivariate and
trivariate orthant formulas; `n ≥ 3` needs Plackett reduction and has none in
general.

The two links sit precisely inside that window, and a Whitehead chain with one
more clasp would not:

| link | label | `n = c+d` | `A` | closed form |
|---|---|---|---|---|
| Whitehead | `W_{0,1,1,0}` | 1 | `1 − i` | `arctan(√A) / (π√(A/2))` |
| Borromean | `W_{0,1,1,1}` | 2 | `2` (real, since `4a+c−d = 0`) | `½ + (2·arcsin(−1/√3) + arcsin(⅓))/π` |

```
Whitehead   I = 0.3359741489681530919776 + 0.05792312441439105494502 i
Borromean   I = 0.2163468959387854596583
```

Both agree with direct quadrature of his Step-6 integral to `9.1e−72` and
`2.3e−72`. The Whitehead value additionally reproduces an **independent**
evaluation of the un-reduced two-dimensional Step-5 integral — which is what
validates the prefactor `C = 2ψ·2^{−n/2}`, since that is the only place it
enters. That prefactor is a derivation from his text, not a formula he states,
and it is flagged as such in the probe.

## The bridge that remains, and why one link cannot settle it

`Q_∞` is not `c_σ`. Going from one to the other needs

1. the **constant** in van der Veen's Lemma 3 for the maximal term `S̃_N`, and
2. the normalisation between his `J` and the reduced `J'` this corpus measures.

Neither is done. The size of what is missing is visible:

```
|Q_∞| / c_σ  =  0.8108743408   at c = 2  (Whitehead)
             =  0.8623779498   at c = 3  (Borromean)
```

**Not a single constant** — and that is expected rather than alarming, because
`S̃_N` enters the bridge raised to the `(c+d)` power. It does mean the bridge
cannot be guessed from the Whitehead link alone, which is the trap to avoid: a
single-link fit would look like a clean ratio and would be wrong at `c = 3`.

## Literature status — recorded so it is not re-searched

* **No van der Veen sequel exists.** His subsequent work moves to spin networks
  (with Garoufalidis) and then to algorithmic knot invariants (with Bar-Natan,
  and Murakami–van der Veen). Nothing evaluates `E` or connects it to torsion.
* **Nobody else has published this constant for a multi-cusped link in this
  setting** — the colored Jones of a link in `S³` at `e^{2πi/N}`.
* **Ka Ho Wong, arXiv:1912.10638**, is directly on van der Veen's family and is
  the near miss: it proves the exponential **growth rate** only, at
  `e^{2πi/(N+1/2)}`. Full text checked — no occurrence of "1-loop",
  "subleading" or "constant term".
* **Pandey–Wong arXiv:2105.08805** is the strongest existing multi-cusped
  result: the Asymptotic Expansion Conjecture for fundamental shadow link pairs,
  with the 1-loop term the adjoint twisted Reidemeister torsion. But it is the
  **relative Reshetikhin–Turaev** invariant in the Chen–Yang setting at
  `e^{2πi/(N+1/2)}` — a different invariant at a different root of unity — so it
  does not close van der Veen's `E`. Its companion, arXiv:2308.06643, supplies
  the 1-loop = adjoint torsion identity for those complements.
* **Ohtsuki–Takata 2015** is now read at full text and it settles the exponent
  convention: Theorem 1.1 is `ω²(D) = ± 𝕋(K)/(2√−1)`, so `ω` is a constant times
  `√𝕋` — the `+1/2` power, with the constant *pinned*. That agrees with DGLZ and
  dissolves the `τ^{+1/2}` vs `|τ|^{−1/2}` worry raised in the previous audit:
  this corpus simply works in the reciprocal variable. Two-bridge **knots**
  only, and the paper's own caveat is that the asymptotics are rigorous only for
  hyperbolic knots up to 7 crossings.

## What is formal now

`QOU/OneLoopPrefactorInvariance.lean`, sorry-free:

* `exponent_normalisation_invariant` — rescaling `c ↦ A·c` leaves the two-point
  exponent unchanged. This is the reason the form transports across every one of
  DGLZ's convention offsets and the constant does not, and it is why the "the
  `/2` IS our `k`" claim had to be retracted rather than merely doubted.
* `k_const_iff_exponent_neg_half` — `c₁√τ₁ = c₂√τ₂ ⟺ p = −1/2`. The
  `k_c`-constancy checks were exponent measurements all along.
* `normalisation_step_trivial_of_k_agree` — what licences reading `k₁ = k₂` as a
  bound on a missing cusp-dependent step.

## Recommended action

1. **`qou-vdvS` — compute Lemma 3's `S̃_N` constant.** This is the whole bridge,
   and it is bounded work in one published proof rather than research.
2. **`qou-vdvE` — then compare against `|τ_DG|^{−1/2}`.** If it lands, `c_σ` for
   the Whitehead link stops being calibrated and becomes derived *on the Jones
   side*, independently of the torsion story — and it would be the first
   evaluation of van der Veen's `E`.
3. Do **not** fit the bridge on the Whitehead link alone. The `c`-dependence
   above is exactly the shape of error this arc has already made twice.
