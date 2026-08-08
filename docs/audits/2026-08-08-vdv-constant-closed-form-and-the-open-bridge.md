# Van der Veen's constant, evaluated — and the bridge to `c_σ` closed

**Date:** 2026-08-08 (rewritten same day; see *Retraction* below) · **Beans:**
`qou-fl4t`, `qou-pn5j`, `qou-vdvS`, `qou-vdvP`, `qou-vdvE`
**Probe:** `computations/probes/one_loop_vdv_constant_closed_form_probe.py`
**Lean:** `QOU/OneLoopPrefactorInvariance.lean` · **Paper:** `prop:one-loop-prefactor-provenance`
**Follows:** `docs/audits/2026-08-08-prefactor-form-what-is-actually-assumed.md`

## The short version

The constant this corpus measures as `c_σ` is the constant `E` in van der Veen's
asymptotic for Whitehead chains. He produces it explicitly and evaluates it only
far enough to show it is nonzero, deferring the rest to a sequel he never wrote.

It is now in closed form for the **whole** `b = 1` family — not two links —
and the bridge to `c_σ` is closed. Writing `n := c+d` and `m := 4a − c + d`:

```
c_σ(W_{a,1,c,d})  =  2^{1/2−n} · (n² + m²)^{−1/4}
```

The consequence for this corpus is the point of the exercise. The law
`c_σ = k·|τ_DG|^{−1/2}` had `k = 2^{−1/2}` **calibrated on `4_1`**, and the
previous audit concluded that calibration was irreducible. It is not: `k` is now
**derived** on the link side, and the law's implied prediction

```
|τ_DG|(W_{a,1,c,d})  =  2^{2n−2} · √(n² + m²)
```

was **pre-registered and then confirmed to 18 digits at three manifolds the
corpus had never tested** — `L8n5` at three cusps, `L10n100` and `L10n103` at
four. The law now holds at 2, 3 and 4 cusps against independently computed
1-loop invariants.

## Retraction — what this file said this morning

The earlier version of this audit, and the probe underneath it, claimed `E`
reduces to a **Gaussian orthant probability** with elementary closed forms
`arctan(√A)/(π√(A/2))` at `n = 1` and an `arcsin` form at `n = 2`, giving
`|Q_∞| = 0.48214876774` and `0.21634689593878`. It also claimed the method
closes "for exactly the two links this corpus uses, and a Whitehead chain with
one more clasp would not".

**All of that is withdrawn.** The correct values are `2^{−1/4}` and `1/2`, and
the integral is elementary for **every** `n`.

The way it was wrong matters more than the fact. Those numbers carried two
checks — agreement with direct quadrature to `1e−72`, and agreement with an
independent evaluation of the un-reduced two-dimensional Step-5 integral. Both
passed. Both were **downstream of van der Veen's Step-3/Step-4 integrand**,
which was taken on trust. They tested the reduction; nothing tested the premise.

The check that catches it is the one that was not run: compute `Q_N` directly
from Lemma 1 and watch what it converges to. It converges to `2^{−1/4}`, not to
`0.482`. That check now runs first in the probe, on 20 chains.

The general lesson is not "verify more" — there were two verifications. It is
that **agreement among quantities derived from the same unchecked input is not
evidence about the input.** The only load-bearing check was against `J_N` itself.

## What van der Veen actually leaves open

His Main theorem gives, for the family `W_{a,b,c,d}`,

```
J_N(W)(e^{2πi/N}) ~ exp{ (1/2π)[ (Vol + iCS)·N + D·log N + E ] },   D = 3π for b = 1
```

The `D` half is a theorem and settles the `N`-power question this corpus had
open (see the previous audit). The `E` half is produced in the proof of Lemma 4
as a `(c+d+1)`-dimensional Gaussian integral. He shows it is nonzero and stops.
His closing paragraph:

> "In the same paper it is also conjectured that the number `E` is determined by
> the Ray-Singer torsion of the complement twisted by the holonomy
> representation. We hope to investigate these conjectures for the Whitehead
> chains in a subsequent publication."

That conjecture (Gukov–Murakami) *is* this corpus's `c_σ ↔ τ` question, for
links, stated as open at the end of the paper the corpus reads its Whitehead
colored-Jones values from.

## Three slips in the published proof

Each is verified below against `J_N` itself. **None of the three touches the
volume conjecture** — his theorem needs only `Vol`, `D`, and `E ≠ 0`, and all
three survive. They move only the constant, which is the part he did not
evaluate and the only part this corpus cares about.

**1. Lemma 2a is stated with absolute values.** He defines
`n′ = |n − ⌊N/2⌋|`, `k′ = |k − ⌊N/4⌋|` as *distances* and writes
`S_{n,k}·S̃_N^{−1} = exp(−(π/N)(n′² + 2n′k′ + 2k′²))`. But the Taylor expansion
he derives this from,

```
f(π/2 + x, π/4 + y) = f(π/2, π/4) − (x² + 2xy + 2y²) + O(|x|³+|y|³)
```

is **signed**, and the cross term `2xy` is negative on the opposite-sign corner.
Evaluating `log(S_{n,k}/S̃_N)` directly at `n′ > 0, k′ < 0`:

| `n′` | `k′` | true | signed form | absolute form |
|---:|---:|---:|---:|---:|
| 10 | −10 | −0.070920 | −0.078540 | −0.392699 |
| 20 | −20 | −0.300637 | −0.314159 | −1.570796 |
| 30 | −15 | −0.353311 | −0.353429 | −1.767146 |
| 15 | −30 | −0.857281 | −0.883573 | −2.297290 |
| 40 | −25 | −0.660549 | −0.667588 | −3.809181 |

The signed form tracks; the absolute one is off by factors of 3 to 5.

**This is the whole retraction in one line.** The `erfc` factors in Step 6 come
from folding the Step-4 Gaussian onto an orthant, and the fold is an artifact of
the absolute values. With signs restored the integral runs over all of `ℝ^{n+1}`
and is a plain Gaussian — elementary for every `n`, with no orthant ceiling at
`n = 2`. The claim that the method "closes only for the two links this corpus
uses" was an artifact of an error, and the truth is far better.

**2. The expression `4a+c−d` should be `4a−c+d`, in two places.** Step 3 defines
the Gaussian coefficient `A = (c+d) − (4a+c−d)i`; it should be
`(c+d) − (4a−c+d)i`, matching the exponent of `χ` in his own Lemma 1. Of the 20
chains swept, the six with `|4a+c−d| ≠ |4a−c+d|` discriminate, and all six land
on `4a−c+d`.

`4a+c−d` is not an arbitrary wrong expression: it is what the main theorem gives
for `CS` when `c+d = 1`, and **that is wrong too, by the same flip.** Measuring
the N-linear phase directly — `arg(R_{N+1}/R_N) → −qπ/8`, where `CS = −q/8·2π²`:

| chain | `q` measured | derived | main theorem |
|---|---:|---:|---:|
| `W_{0,1,1,0}` | −1.00001 | −1 | **+1** |
| `W_{0,1,0,1}` | +1.00001 | +1 | **−1** |
| `W_{1,1,1,0}` | 2.99999 | 3 | **5** |
| `W_{0,1,2,0}` | −2.00000 | 14 ≡ −2 | **−14 ≡ 2** |
| `W_{0,1,2,1}` | 7.00000 | 7 | **−7** |
| `W_{0,1,3,0}` | 5.00000 | 21 ≡ 5 | **−21 ≡ 11** |
| `W_{1,1,0,2}` | 6.00000 | −10 ≡ 6 | **18 ≡ 2** |

(compared mod 16, since the phase is `e^{−iqπN/8}`). The correct `q` is `4a−c+d`
at `c+d = 1` and `4a+7c−7d` at `c+d ≥ 2`; the main theorem states `4a+c−d` and
`4a−7c+7d`. Same sign flip on `(c−d)` in both branches. The branch difference is
only `φ_N`, which he defines differently in the two cases and which contributes a
linear phase `−8(c−d)` in the second.

So slips in `A` and in `CS` have **one root cause**, not two. His Lemma-4 *proof*
uses the correct `(4a+7c−7d)` when it defines `Q_N`, which is why `Q_∞` is
well defined despite the main theorem's statement.

**3. The `b ≥ 2` constant has the wrong sign in the Main theorem.** It states
`E = 2π(c+d)log 2 + …`, but his own Lemma 5 gives the constant as
`exp(−(c+d)log√2 + …)`, i.e. `Re E = −2π(c+d)log 2`. Computing
`|J_N|·N^{−b}·e^{−Vol·N/2π}` from Lemma 1 gives `2^{−(c+d)}` on every case
tested, not `2^{+(c+d)}`. Lemma 5 is right; the Main theorem's transcription
is not.

**Lemma 3 is correct as printed** — `S̃_N ∼ exp((4N/π)Λ(π/4) − ½log 2N)` —
and was verified numerically rather than trusted, because the `s_n` line inside
its own proof drops a factor `2π`. The two extreme terms of
`log S̃_N = −2s_{⌊N/4⌋+⌊N/2⌋} + 2s_{⌊N/4⌋} + s_{⌊N/2⌋}` cancel that factor, so
the lemma survives its own proof's typo. Its constant `2^{−1/2}` per unit of
`c+d` is exactly what cancels the cusp-dependence in the `N`-power and yields
`D = 3π` independent of `c` and `d`.

## The derivation, in one pass

With Lemma 2a's signs restored and `A` corrected, Step 4's integral is

```
Q_∞ = ψ · ∫_{ℝ^{n+1}} exp(−π[ A u²/2 + 2 Σⱼ (vⱼ + u/2)² ]) du dv
```

The `v` integrals are complete Gaussians, `∫_ℝ e^{−2π(v+u/2)²}dv = 2^{−1/2}`,
independent of `u`; the `u` integral is `∫_ℝ e^{−πAu²/2}du = √(2/A)`. So

```
Q_∞ = ψ · 2^{−n/2} · √(2/A) ,      A = n − m i
```

and with Lemma 3 supplying `S̃_N^{c+d} = e^{Vol·N/2π}·2^{−n/2}·N^{−n/2}` against
Lemma 4's `N^{(n+3)/2}`,

```
c_σ = |Q_∞| · 2^{−n/2} = 2^{1/2−n} (n² + m²)^{−1/4}
Re E = 2π[ (1/2 − n)·log 2 − ¼·log(n² + m²) ]
```

## The phase, resolved

`ψ` appears with opposite signs in Lemma 5 and in the retracted probe, and the
modulus verification above cannot tell them apart. It is settled by measuring
the **complex** `Q_N` at `N ≡ 0 (mod 16)` — where van der Veen's CS factor
`e^{(4a+7c−7d)Nπi/8}` is exactly `1`, so nothing is imported:

```
Q_∞ = exp(+i π (4a+3c−3d)/4) · 2^{−n/2} · √(2/A)
```

The `+` sign — Lemma 5's, not the retracted probe's. Across 12 chains the error
against `ψ = exp(+…)` is `4e−7` to `1.1e−6` and falls as `O(1/N)`; against
`ψ = exp(−…)` it is `0.34` to `1.19` on the 9 chains where the two differ
(`ψ` and its conjugate coincide exactly when `4a+3c−3d ≡ 0 mod 4`).

It is independently corroborated by van der Veen himself: his `b ≥ 2` constant
in the main theorem is `E = 2π(c+d)log 2 + (4a+3c−3d)/4·2π²i`, whose **imaginary
part agrees exactly** with the `ψ` above. That is the same formula whose *real*
part is sign-wrong (slip 3) — so the `b ≥ 2` line is right about the phase and
wrong about the logarithm, which is a coherent single-typo story.

So `E` is now complete:

```
Re E = 2π[ (1/2 − n)·log 2 − ¼·log(n² + m²) ]
Im E = π·arctan(m/n) + π²(4a+3c−3d)/2
```

`c_σ` depends on `|Q_∞|` alone, so none of the corpus results above move; the
phase **completes** `E` rather than correcting anything.

## Verification

Against `Q_N` computed directly from Lemma 1 in log space, Richardson-extrapolated
from `N = 1600, 3200`, over 20 chains spanning `c+d ∈ {1,…,4}` and `a ∈ {0,…,3}`:
**0 mismatches, worst relative error `5.0e−06`**, the residual being the
`O(1/N²)` Richardson remainder and growing smoothly with `c+d`.

Against independently computed DG 1-loop invariants (`computations/one_loop_torsion.py`
over SnapPy):

| manifold | chain | cusps | `|τ_DG|` predicted | agreement | status |
|---|---|---|---|---|---|
| `L5a1` | `W_{0,1,1,0}` | 2 | `√2` | `1.9e−61` | corpus value |
| `L6a4` | `W_{0,1,1,1}` | 3 | `8` | exact | corpus value |
| `L8n5` | `W_{0,1,2,0}` | 3 | `8√2` | `1.8e−71` | **pre-registered** |
| `L10n100` | `W_{0,1,2,1}` | 4 | `16√10` | `2.7e−71` | **pre-registered** |
| `L10n103` | `W_{0,1,3,0}` | 4 | `48√2` | `1.8e−71` | **pre-registered** |

The last three were predicted from the closed form *before* the manifolds were
located — they were then found by searching for the family's volume
`8(c+d)Λ(π/4)` at the right cusp number, and their 1-loop invariants computed.
This is the check that the previous round lacked: a prediction that could have
failed, at a cusp number never tested, against a quantity computed by machinery
that knows nothing about colored Jones.

`c_σ(L5a1)` derived is `2^{−3/4}`, agreeing with the corpus's extrapolated
measurement to `3.1e−21` — i.e. to the full width of that measurement.
`c_σ(L6a4)` derived is exactly `1/4`; the corpus's `0.2508724811` is a finite-`N`
tower fit and agrees to its own `0.35%` accuracy, which is why `τ_DG` rather
than `c_σ` is the test at three cusps.

## What this changes in the assumption ledger

The previous audit's conclusion — *"`k = 2^{−1/2}` cannot be lifted from the
literature formula; it remains calibrated on `4_1`, and that calibration is not
redundant"* — was right about DGLZ and wrong about the outcome. DGLZ's constant
still cannot be lifted, because of the convention offsets that audit documents.
But it does not have to be: **van der Veen's asymptotic supplies `c_σ` directly
on the Jones side, with no convention to reconcile**, and the resulting `k`
agrees with the `4_1` calibration.

So the calibration is now *redundant on the link side* — corroborated rather
than required. What is **not** established:

* ~~**The knot side.**~~ **Closed the same day — see below.** `4_1` is not a
  Whitehead chain, but it does not need to be.
* **`c_σ ∝ |τ|^{−1/2}` in general.** What is shown is that the derived Jones-side
  constant and the independently computed DG invariant satisfy that relation on
  five manifolds at three cusp numbers. That is a much stronger test than the
  corpus had, and it is not a proof.
* **The phase of `E`.** Untouched.

## The `a`-dependence, confirmed — the phase-driven half

Every confirmation in the table above has `a = 0`. That matters, because **`a`
enters van der Veen's Lemma 1 only through the phase `χ^{4a−c+d}`**: the modulus
of the summand does not know about `a`, and the whole `a`-dependence of
`|τ_DG|` is manufactured by interference in the `n`-sum. If the closed form were
right for the wrong reason, this is where it would show.

Testing it needs reframing, not a new manifold. `Vol(W_{a,b,c,d}) = 8(c+d)Λ(π/4)`
is independent of `a`, so by Thurston–Jørgensen the chains cannot be infinitely
many distinct manifolds — and scanning `OrientableCuspedCensus(cusps=2)` at
octahedral volume returns only `m129` (`|τ| = √2`) and `m125` (`|τ| = √8`, and
`8 = 1+m²` has no integer solution, so it is not in the family). No manifold
carries the `a ≠ 0` values. They are one complement, reframed.

So `one_loop_torsion.one_loop` was extended to general `(p,q)` peripheral curves
(`_curve_row`): the log-form gluing equation of a peripheral curve is *linear* in
its homology class, so the row of `pμ + qλ` is `p·mer + q·lon` of the two rows
SnapPy returns. Legacy `0`/`1` still agrees; `self_test()` stays green at
`c = 1, 2, 3`. Framing by `μ − aλ` on one cusp:

| chain | | `τ²` predicted | `a = 0, 1, −1, 2, −2` |
|---|---|---|---|
| `W_{a,1,1,0}` | `n=1, m=4a−1` | `1 + (4a−1)²` | 2, 10, 26, 50, 82 |
| `W_{a,1,1,1}` | `n=2, m=4a` | `64(1 + 4a²)` | 64, 320, 320, 1088, 1088 |

**25 framings, 0 mismatches**, on every cusp of both manifolds. Two things came
out that were not put in: the Borromean values are identical on all three cusps,
and symmetric under `a ↦ −a` — both forced by `m = 4a` entering as `m²`.

Formally (`vdv_tau_sq`), `τ² = 16^{n−1}(n² + m²)`, so **every `b = 1` chain has
integer `τ²`** — which is why that table is integers rather than numerical
near-misses — and `n² + m² = \mathrm{normSq}(n − mi)`
(`vdv_radical_is_gaussian_norm`), so the radical is a **norm from `Z[i]`** rather
than an accident.

## The knot side, closed — and why the method has exactly two homes

**What made the link case work was not van der Veen.** It was that his critical
point sits at `(π/2, π/4)`, a *rational* point in units of π, because those
complements are glued from **regular ideal octahedra** (`Vol = 8(c+d)Λ(π/4)`).
The rest of the argument — state-sum → Lobachevsky potential → critical point →
Hessian, with `|Q_∞|² ∝ 1/det(Hess)` — does not care which link it is.

**So look for the other regular ideal polyhedron.** `4_1` is two regular ideal
*tetrahedra*, and Kashaev's invariant is a one-variable sum of the same shape:

```
⟨4_1⟩_N = Σ_k |(q;q)_k|² = Σ_k ∏_{j≤k} 4sin²(jπ/N) = Σ_k e^{−2 s_k}
```

— the *same* `s_k` whose expansion was already verified for Lemma 3. Feeding it
through, with `θ = kπ/N`:

| ingredient | value |
|---|---|
| saddle `Λ′(θ) = −log(2 sin θ) = 0` | `2 sin θ* = 1`, so `θ* = 5π/6` |
| leading value `(2N/π)Λ(π/6)` | `= Vol·N/2π`, since `Vol(4_1) = 4Λ(π/6)` |
| Stirling `2N sin θ*` | `N` |
| Hessian `Λ″(θ*) = −cot θ*` | `√3`, giving `√(N/√3)` |

```
⟨4_1⟩_N ~ 3^{−1/4}·N^{3/2}·e^{Vol·N/2π}
```

so `c_σ(4_1) = 3^{−1/4}` **and** the power `N^{3/2}` are derived. Numerically,
Richardson at `N = 32000, 64000` gives `0.759835685682` against
`3^{−1/4} = 0.759835685652` — relative `4.0e−11`, and the corpus's own
extrapolated value agrees to `4.5e−18`.

**A rigidity worth stating.** In one variable the saddle condition *is*
`2 sin θ* = 1`, so the Stirling factor is pinned to `1` and

```
c_σ = |cot θ*|^{−1/2} = 3^{−1/4}
```

with no freedom at all. `3^{−1/4}` is a property of *one summation variable*,
not of `4_1`.

**And `k = 2^{−1/2}` never depended on any of it.** Since
`c_σ = 2 sin θ*·|cot θ*|^{−1/2}` and `|τ_DG| = |cot θ*|/2`, the Hessian cancels
in `k := c_σ·|τ|^{1/2}` **before it is evaluated**:

```
k² = (2 sin θ*)²/2 = 1/2
```

using only the saddle condition — no trace field, no cusp number, no manifold.
The `4_1` calibration the whole `c_σ` arc rested on was never carrying
information. This is `k_sq_eq_half_of_saddle`, and it is the sharpest thing in
this file.

**`τ_DG` is the Hessian.** `|τ_DG|(4_1) = |cot θ*|/2 = √3/2` reproduces the
corpus's independently computed value exactly. That is the DG/Gukov–Murakami
claim exhibited in the smallest case, not assumed.

**Why exactly two closed-form families.** The saddle sits at a root-of-unity
shape precisely for the regular ideal polyhedra:

| | shape | trace field | `|τ_DG|` |
|---|---|---|---|
| tetrahedral (`4_1`) | `e^{iπ/3}` | `Q(ζ₃) = Q(√−3)` | `√3/2` |
| octahedral (`W_{a,1,c,d}`) | `i` | `Q(ζ₄) = Q(i)` | `2^{2n−2}\|A\|`, `A = n − mi ∈ Z[i]` |

In the link case `A` is literally a **Gaussian integer** and `|A| = √(n²+m²)` is
the square root of its norm — that is the arithmetic content of the closed form.
And those two are the only imaginary quadratic fields with extra units, the two
Bianchi cases. For a general knot the trace field is a general number field and
`det(Hess)` is an algebraic number in it with no reason to have a radical
expression. **The obstruction to extending the method is arithmetic, not
analytic.**

### Where the `√5` actually is — and it is not a third polyhedron

The first draft of this section guessed that a `√5` would need a regular ideal
**dodecahedron** (the Aitchison–Rubinstein knots) and beaned that. **That was
too narrow a reading of the pattern.** The polyhedra are how a `Z[ζ]` norm shows
up *here*; they are not the mechanism.

The mechanism is the norm. And a norm from `Z[ζ₅]` needs no 5-fold polyhedron —
it arises from a **cyclic branched cover**, through the classical

```
|H₁(Σ_d(K))| = ∏_{j=1}^{d−1} |Δ_K(ζ_d^j)| = |Res(Δ_K, (t^d−1)/(t−1))|
```

which is a norm from `Z[ζ_d]` in exactly the way `|A| = √(n²+m²)` is a norm from
`Z[i]`. Computed for the two torus knots the `brings-surface` chapter names:

| knot | `d` | `\|H₁(Σ_d)\|` | manifold |
|---|---:|---:|---|
| `T_{2,3}` trefoil | 5 | 1 | **Poincaré homology sphere** `Σ(2,3,5) = S³/2I` |
| `T_{2,5}` cinquefoil | 2 | 5 | lens space `L(5,q)` |

and the WRT invariant of `L(5,q)` is a Gauss sum, with `Σ_k ζ₅^{k²} = √5` — the
corpus's Bring constant, verified rather than asserted.

The corpus already had half of this. `klein-bring-icosahedral-bridge` states
`P(V)/A₅ ≅ S²(2,3,5)`, the base of the Seifert fibration `S³/2I → S²(2,3,5)`.
What was missing is that the trefoil the *same chapter* calls the electron is the
**branch locus** of that cover, and that `|2I| = 120 = |S₅| = |Aut(Bring)|`.

**The trap, stated before anyone writes it into the paper.** `Σ(2,3,5)` is
spherical and `T_{2,3}`, `T_{2,5}` have zero simplicial volume — the colored
Jones grows polynomially, and `c_σ` as this corpus defines it is not the same
object. So this `√5` is *not* a `c_σ`, and there is no Lobachevsky saddle
anywhere near it. Two `√5`s of cyclotomic origin are not automatically the same
`√5`. The right analogue of `Q_∞` in that world is Lawrence–Zagier's asymptotic
expansion of the WRT invariant of `Σ(2,3,5)` as an Eichler integral of a
half-integral-weight modular form — registered as `lawrence-zagier-1999`, **not
yet read at full text**, and beaned as `qou-lz235`. The likely outcome is that
the two constants are different objects that merely share the field `Q(ζ₅)`,
and establishing that cleanly is worth as much as a connection would be.

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
* **Ohtsuki–Takata 2015** is read at full text and it settles the exponent
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
* `vdv_c_sigma_iff_tau` — the derived `c_σ` satisfies the corpus's law exactly
  when `|τ| = 2^{2n−2}√(n²+m²)`. This is what makes the pre-registered `τ_DG`
  predictions a *consequence* of the closed form rather than a separate fit.

## Recommended action

1. **`qou-vdvT` — extend `one_loop_torsion.py` to general peripheral curves.**
   The `a`-twisted chains `W_{a,1,c,d}` are the same manifolds as `W_{0,1,c,d}`
   with a different framing (their volume is independent of `a`), so the
   `a`-dependence of `|τ_DG| = 2^{2n−2}√(n²+m²)` is a sharp, cheap test of the
   change-of-curve law — but `one_loop(M, curves=…)` currently accepts only
   meridian or longitude, not `μ + aλ`.
2. **`qou-vdvE` — report the corrections upstream.** Three slips in a published
   AGT paper, none affecting its theorem, all affecting the constant that a
   named open conjecture is about — and one of them (the `(c−d)` flip) also
   misstates `CS` in both branches of the main theorem. This is worth writing
   to the author.
3. Do **not** treat the `4_1` leg as covered. The derivation is link-side only.
