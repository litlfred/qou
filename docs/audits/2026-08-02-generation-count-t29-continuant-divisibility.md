# Three generations: deriving the T(2,9) exclusion (Route A)

**Date:** 2026-08-02
**Branch:** `claude/sm-appendix-roast-2026-08-01` (PR #4456)
**Bean:** `qou-x4qm` (GAP: three-generation structure)
**Status:** normal-form derivation landed, sorry-free Lean twin; physical
bridge + mass map remain open (scope-(a)).

## What was open

The sibling probe `generation_count_t29_truncation_probe.py`
(`generation-count-t29-truncation.witness.json`) localised *"why three
generations"* to a single lemma: the genus bound
`g(T(2,n)) = (n-1)/2 ≤ 4` (`torus-embeddable-complete-proof`, **proved**)
admits the odd coprime windings `n ∈ {3,5,7,9}` — **four** knots — while
the corpus assigns generations to `n ∈ {3,5,7}` — **three**. So the
generation count *is* the exclusion of `T(2,9)`.

A corpus-wide grep found the primality condition (`odd primes`) exactly
once, as an **underived parenthetical** on line 1 of
`lepton-meson-torus-knot-dictionary.md`. The probe named three routes and
marked **Route A — derive primality** as "the one with an actual payoff
(3 generations, not merely ≤ 4)", but did not run it.

## What was derived (Route A)

The `σ`-coefficient `bₙ` of the Gröbner–Shirshov normal form of
`T(2,n) = σ₀ⁿ` in `H₂(q)` — the Morgan–Voyce continuant of
`prop:lepton-continuant-recurrence`,
`b₀=0, b₁=1, b_{n+1}=h·bₙ+b_{n-1}`, `h = q−q⁻¹` — satisfies the
**Fibonacci-polynomial divisibility**

```
b_a ∣ b_n   (in ℤ[h])   ⟺   a ∣ n.
```

Consequences on the genus-admissible window `{3,5,7,9}` (exact `ℤ[h]`
arithmetic — no `q₀`, no floats):

| winding `n` | prime? | `bₙ` vs `b₃` | reading |
|---|---|---|---|
| 3 | ✓ | — | generation 1 |
| 5 | ✓ | `b₅ = b₃·(h²+2) − 1` (unit remainder) | non-harmonic |
| 7 | ✓ | `b₇ = b₃·(h⁴+4h²+2) − 1` (unit remainder) | non-harmonic |
| 9 | ✗ (`3·3`) | `b₉ = b₃·(h⁶+6h⁴+9h²+1)` (**`b₃ ∣ b₉`**) | **harmonic of gen 1** |

`9 = 3·3` is the **unique composite** in the window, and `b₉` factors
through `b₃` — the precise, exact form of the candidate reason
*"`σ⁹ = (σ³)³` is a harmonic of generation 1"*. The prime windings
`3,5,7` are mutually non-divisible. So **the generation windings are
exactly the odd windings whose continuant coefficient does not factor
through a smaller one — the odd primes.** The asserted `(odd primes)` is
now derived at the normal-form level.

### Artifacts

- **Lean (sorry-free, `lean`-direct exit 0):**
  `content/quantum-observable-universe/lean/QOU/Archimedean/lepton_continuant_generation_exclusion.lean`
  — `t29_harmonic_of_first_generation` / `b3_dvd_b9`, `not_b3_dvd_b5`,
  `not_b3_dvd_b7`, `three_generation_windings_are_the_nonharmonic_ones`.
  Reuses the canonical `morganVoyceB` from `lepton_continuant_recurrence`;
  non-divisibility via the unit-remainder → non-unit (`compute_degree!`)
  argument.
- **Derivation probe (5/5 assertions):**
  `computations/generation_t29_continuant_divisibility_derivation.py` →
  `generation-t29-continuant-divisibility.witness.json`.
- **Prose:** the dictionary authorNote upgraded `caveat` (asserted) →
  `refined-framing` (derived).

## Honest scope — (a), not (b)

Per the repo's "refuted/ruled-out" discipline, this is a **scope-(a)**
result: it derives the *factorisation / harmonic distinction on the
normal-form coefficient*. It is **not** a scope-(b) structural exclusion
of `T(2,9)` as a physical state:

1. **`T(2,9)` is a genuine prime knot of genus 4.** Torus knots `T(2,n)`
   with `gcd(2,n)=1` are prime for every odd `n`; `9` composite does not
   make the *knot* composite. The factorisation is of the continuant
   *coefficient* `bₙ`, not of the knot.
2. **The `net → mass` map is still open.** The sibling probe recorded its
   `net`-ratio validation as **FAILED** (net ratios are `O(1)`, observed
   lepton ratios `O(10²)`) and did *not* patch it with a fitted scale. So
   this derivation cannot yet say what `T(2,9)` would *weigh*, only that
   its normal-form data is not independent of generation 1.

## Residual gap (still `qou-x4qm`)

The physical bridge **"normal-form-independent winding ⟹ physical
generation"** is the remaining content: *why* should a coefficient
factoring through a smaller winding forbid an independent fibre / mass
assignment? Plus the `net → mass` map (Route B) for any numerical
falsification against the LEP bounds (no 4th charged lepton below
~45 GeV; `N_ν = 2.984 ± 0.008`). Both stay open. What is closed is the
corpus's asserted-not-derived primality parenthetical.
