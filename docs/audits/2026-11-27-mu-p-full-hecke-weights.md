# μ–p residual: projector insertions on 4₁ under the full Ocneanu trace do not force the w² dressing

Date: 2026-11-27. Bean `qou-6gf9` (compute-accuracy C3, epic `qou-myts`). Follows PR #9445.
Owner choice (decision card, 2026-11-27): "both" routes for the μ–p residual. This audit
covers the full Hecke weights; the open-worldline route is a separate thread.
Lean: `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/MuPFullHeckeWeights.lean`.
Probe: `computations/probes/mu_p_full_hecke_weights_probe.py`, witness
`computations/probes/mu-p-full-hecke-weights.witness.json`.

## Question

PR #9445 (audit `2026-11-27-mu-p-projector-insertion-w-order.md`) tested the photon
projector `e_i = (q − σ_i)/[2]_q`, inserted once or twice into `4₁ = (σ₁σ₂⁻¹)²`, under the
SU(2) Markov weights (`y₁₁₁ = 0`). It found no member with vanishing `O(w⁰)` and `O(w¹)`,
and a free `w²` coefficient once both are cancelled by choice. It listed one class as not
covered: insertions in the full Hecke algebra `H₃` with `y₁₁₁ ≠ 0`.

This audit runs that class. The Markov trace is the Ocneanu trace on all of `H₃`, and its
parameter `z` stays **symbolic**. The question is the same: does any covariant observable
have vanishing `O(1)` and `O(w)` and a forced `w²` coefficient that matches
`−(3α/4π)·w²`, with `w = q + q⁻¹ − 2`?

**Scope fence.** Convention D (owner ruling 2026-08-15) is `y₁₁₁ = 0` and stays canonical.
The full trace is a comparison family. No value of `z` is chosen because it fits: that would
be selection against the target (AGENTS.md, "No fitting"). α appears only in the comparison
section and in no proof.

## Setup

`H₃` has three conjugacy classes and three irreducibles, `(3)`, `(2,1)` and `(1,1,1)`. So
`tr 1 = 1`, `tr σ₁ = z` and `tr σ₁σ₂ = z²` fix the trace. The weights in `K(q, z)` are

- `y₃ = (qz+1)(q³z+qz+1)/den`,
- `y₂₁ = −q(z−q)(qz+1)(q²+1)/den`,
- `y₁₁₁ = q²(z−q)((q²+1)z − q³)/den`,

with `den = (q²+1)(q⁴+q²+1)` (Lean `ocneanu_one`, `ocneanu_sigma1`, `ocneanu_sigma1sigma2`).
The sign weight vanishes at the SU(2) point `z = q³/(q²+1)`, which is convention D's `z_D`
(`trace-convention-registry.md`; audit `2026-09-05-which-z-does-the-qbeta-spectral-bridge-intend.md`).
There the weights are exactly #9445's (`su2_weights`). The excised convention C,
`z = 1/(q^{1/2}+q^{-1/2})`, belongs to a different normalisation of `σ` and is not used here. It also vanishes at `z = q`, the trivial-only trace.

`e_i` kills `(3)` and acts as 1 on `(1,1,1)`, and `χ_(111)(4₁) = 1`. So every insertion
correlator is `(y₂₁·tr₃(…) + y₁₁₁)/tr_M(4₁)`. The observables are #9445's four: the
bar-symmetric single `⟨e₁⟩+⟨e₂⟩`, all singles `S₁`, all doubles `D`, and connected doubles `C`.

## Results (exact; claim, then evidence)

1. **Closed forms in ℚ(q, z).** `tr_M(4₁) = W(q,z)/q³`. The single insertion is
   `⟨e₁⟩+⟨e₂⟩ = −(z−q)·R(q,z)/((q²+1)·W(q,z))`, with
   `W = q⁶z − q⁵z² + q⁵ − 4q⁴z + 3q³z² − 2q³ + 4q²z − qz² + q − z` and
   `R = q⁷z + q⁶ − 2q⁵z − 2q³z − 2q² + qz + 1`. Evidence: Lean `trM41Z_eq`, `pairCorrZ_eq`,
   both built from the matrices. The probe gives `D` and `C` the same way. Single insertions
   are slot-independent here too.
2. **The SU(2) point reproduces #9445.** Lean `pairCorrZ_su2` shows that at
   `z = q³/(q²+1)` the correlator equals #9445's `pairCorr`. The probe reproduces #9445's
   whole Taylor table at `N = 2` (Lean `suN_at_two`).
3. **Every observable carries the factor `(z − q)`.** At `z = q` only the trivial
   representation survives. The projectors kill it, so every insertion correlator is 0 at
   every order (Lean `pairCorrZ_degenerate`; probe assertion
   `every_observable_has_factor_z_minus_q`).
4. **Leading terms.** At `q = 1` the four observables are `(z−1)/z`, `4(z−1)/z`,
   `(z−1)(17z−3)/z²` and `7(z−1)(z+1)/z²` (Lean `pairCorrZ_at_one` for the first).
5. **SU(N) family, `N` symbolic.** This is the natural bar-covariant one-parameter slice,
   `z = q^N/[N]_q`, which is HOMFLY with `a = q^N`. The exact `w`-Taylor data are:

   | observable | O(1) | O(w) | O(w²) |
   |---|---|---|---|
   | ⟨e₁⟩+⟨e₂⟩ | 1 − N | 10N(N²−1)/3 | −7N(N²−1)(52N²−63)/30 |
   | S₁ | −4(N−1) | 40N(N²−1)/3 | −14N(N²−1)(52N²−63)/15 |
   | D | (N−1)(3N−17) | −(N²−1)(33N²−200N+51)/3 | (N²−1)(2408N⁴−14560N³+903N²+17640N−4995)/60 |
   | C | −7(N²−1) | (N²−1)(167N²−51)/3 | −(N²−1)(56456N⁴−75629N²+14985)/180 |

   At `N = 2` this is #9445's table. `O(1) = O(w) = 0` holds only at `N = 1` for `S₁` and
   `D`, and at `N = ±1` for `C` (Lean `suN_vanishing_forces_degenerate`). `N = 1` is the
   trivial-only trace and `N = −1` is the sign-only trace (`sign_only_weights`). On both, the
   observable is identically zero or constant, so its `w²` coefficient is 0, not a dressing.
   The coefficient matrix on `(1, S₁, D, C)` has rank 3 over ℚ(N). For every `N` off
   `{0, ±1}` and off the roots of `7N⁴ + 126N² − 621`, every `w²` value is reached by a
   combination of `1, S₁, D` with vanishing `O(1)` and `O(w)` (Lean `suN_w2_not_forced`).
   This is the same non-forcing #9445 found at `N = 2`.
6. **General bar-covariant `z`.** Bar-covariance of the trace, `tr(x̄) = bar(tr x)`, makes `z`
   of the form `sinh h·(1 + 2κ(h))` with `κ` odd and `q = eʰ`. Truncating,
   `κ = c/h + k₁h + k₃h³`. Every observable is then even in `h` (probe assertion
   `bar_covariant_families_are_even_in_h`). For the single insertion, `O(1) = 0` forces
   `c = 1/2`, then `O(w) = 0` forces `k₁ = 1/6`, and the remaining coefficient is
   `O(w²) = (90k₃ + 1)/45 = 2(k₃ + 1/90)` (Lean `general_z_low_orders`, `general_z_w2_eq`,
   `general_z_w2_free`). `c = 1/2`, `k₁ = 1/6`, `k₃ = −1/90` is exactly `z = q`. So the
   members with vanishing `O(1)` and `O(w)` are the traces that agree with the degenerate
   trivial-only trace through order `h³`. Their `w²` coefficient is twice the trace's own
   `h⁴` departure from it. Lean `pairCorrZ_eq_mul` and `F_one_one` make this structural:
   `⟨e₁⟩+⟨e₂⟩ = (z − q)·F` with `F(1,1) = 1`.

## Comparison (this is where the empirical claim lives; no proof uses it)

Under a general `z`, the target `−3α/4π = −1.742 × 10⁻³` (CODATA α) is reachable: take
`k₃ = (45·(−3α/4π) − 1)/90`, a shift of `−8.71 × 10⁻⁴` from the trivial-trace value. That is
a choice of trace made to hit the number, which is selection. It is reported to show that the
class can reproduce any `w²` coefficient, not as a candidate. In the SU(N) slice no `N` gives
vanishing `O(1)` and `O(w)` with a nonzero `w²`.

## Verdict and scope

**Scope (a).** The full-Hecke projector-insertion class on 4₁ does not derive
`−(3α/4π)·w²`. Freeing `z` (`y₁₁₁ ≠ 0`) adds non-forcing rather than removing it:

- in the natural SU(N) slice, `O(1)` and `O(w)` vanish together only on the degenerate traces
  `N = ±1`, where every correlator is trivial;
- in the general bar-covariant family, the `w²` coefficient of any member with vanishing
  `O(1)` and `O(w)` is a free Taylor coefficient of `z`.

This bars a derivation through this class. It is not a structural exclusion (b) of a `w²`
dressing from every construction. The candidate stays an unwired working assumption.

The sibling open-worldline route (PR #9492) closed in scope (a) the same day: with unknot
normalisation the radius grows to 2, but the `w²` coefficient is still unforced. With both
routes #9445 left open now run, the projector-insertion programme gives no derivation of the
candidate.

## Corpus-grep note

Searched: `docs/audits` (mu-p, Ocneanu, y_111, full Hecke), bean `qou-6gf9` (full body), and
#9445's audit and probe. #9445 lists `y₁₁₁ ≠ 0` as "not covered". No prior audit treats the
insertion class under a symbolic Ocneanu `z`.
