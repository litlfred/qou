# The A=3 amplitude carrier is a √−1: the bar-odd/unit-modulus Pythagorean bridge, and the reframing to a transverse slope

**Date:** 2026-08-09 · **Bean:** `qou-wiub` (A=3 magnitude keystone) / `qou-prjo` (surviving
transverse object) · **Branch:** `claude/z-c-k-f-map-keystone-ub5yix` (redirected — see §Branch
note) · **Tier:** formalize-first (Lean sorry-free, `lean`-direct exit 0) + scope-(a) reframing.
**Scope:** structural — nothing fitted, nothing wired, `1.585` NOT derived.

## The open item this addresses

`A3AntiSelfAdjointLift` (#4611) reduced the A=3 Δ_λ magnitude lift `r* = μ₃/c₃ ≈ 1.585` to
**one** free anti-self-adjoint amplitude `E`, with the even-face factor **affine** in `E`:
`factor = factor_sa − s·E`, `factor_sa ≤ 1`, slope `s = B·D⁻¹/A`. `BirkhoffAmplitudeE` /
`BirkhoffAmplitudeWellPosed` then pinned `E` to the frame-free Birkhoff connection cross-ratio
`E = χ(P)`, and the numeric evaluation found `χ(P)|q₀` is a **pure unit-modulus phase**,
`|χ| = 1` exactly (`c1-chi-magnitude-vs-r-star.witness.json`, dev < 1e-30). That left a
**"genuine type tension"** flagged in `BirkhoffAmplitudeE`'s docstring, OPEN with no instance:
how does a carrier that is a *unit phase* supply the *real* magnitude `r* > 1` the lift needs?

## The bridge (Lean, sorry-free)

[`QOU/QBeta/BirkhoffBarOddPythagorasBridge.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/BirkhoffBarOddPythagorasBridge.lean)
resolves the *type tension* structurally (it does **not** compute `χ(P)`'s value — beans
`qou-wgnx`/`qou-vkg5`). Two corpus facts about `E = χ(P)`:

- **bar-odd** — `σ E = −E` (anti-self-adjoint; `DTIndexAmplitudeE.amplitude_barOdd`);
- **unit-modulus** — `E · σ E = 1` (the `|χ| = 1` numeric).

| Theorem | Content |
|---|---|
| `barOdd_unitModulus_sq_eq_neg_one` | bar-odd + unit-modulus ⇒ **`E² = −1`** (`E·(−E)=1`); the carrier is a √−1 |
| `affine_modulus_quadrature` | for bar-even `fs, s` and `E² = −1`: `(fs − s·E)·σ(fs − s·E) = fs² + s²` (the `−s²E²` cross-term becomes `+s²`) |
| `barOdd_carrier_quadrature` | the combined bridge: unit-modulus phase ⇒ real lift modulus `fs² + s²` |
| `sq_ne_neg_one_of_ordered` | in any ordered field `E² ≠ −1` — the carrier is **not real** (the exact "real E vs unit phase" tension) |
| `modulusReading_gives_pythagorean` | *conditional* on the modulus-reading hypothesis (`structure`, **NO instance**): `r*² = fs² + s²` |

The result is the **elliptic (unit-circle) counterpart** of the *hyperbolic* bar-even/bar-odd
identity `P_m² − Q_m² = (2 cosh η)⁻²` (`BarSymmetricBarAntiSymmetricIdentities`): there the
bar-odd part enters with a `−` (cosh/sinh, difference of squares); here the unit-modulus
carrier enters with a `+` (`E² = −1`, sum of squares). The even/odd = meson/lepton =
self-dual/non-self-dual split reappears, now with the cross-ratio carrier on the **elliptic**
(|χ|=1) branch.

## The reframing (scope-(a) — the value)

Numeric companion
[`birkhoff_barodd_pythagoras_bridge_probe.py`](../../computations/qbeta/birkhoff_barodd_pythagoras_bridge_probe.py)
(6/6, 0 free params). The A=3 lift is `factor = 1 − ρ` (`ρ = B·D⁻¹C/A`); `r* = 1.585` needs
`ρ ≈ −0.585`, and every real **longitudinal** reading `ρ ∈ {±h, ±ℏ_q} ≈ ±0.1` **misses**
(0/4 land `r*`, reproducing `a3_magnitude_berezinian_crossterm_probe.py`). Under the modulus
reading `r* = √(fs² + s²)`, the question turns into:

> why is the **transverse** slope `s = √(r*² − fs²)` an `O(1)` off-block amplitude?

(For `fs = 1`, `s ≈ 1.23` — `O(1)`, **not** `O(h)`.) This **relocates the magnitude datum to
the transverse (imaginary-`q`) direction** — the same object as bean `qou-prjo` (transverse
NA-Stokes surface-curvature) — and explains structurally *why every longitudinal / real-reading
/ `O(h)` probe failed*: they were reading a longitudinal even-face correction where the datum is
a transverse quadrature slope.

## Honesty ledger (STRICT)

- **`1.585` is NOT derived.** `fs` (self-adjoint reduction) and `s = B·D⁻¹/A` are not pinned
  here; the demonstration model `fs = s = 1` gives `√2 ≈ 1.414 ≠ 1.585` — flagged in the
  witness (`placeholder_matches_rstar = false`). Deriving `fs, s` from the branching is bean
  `qou-jqof`.
- **No fit.** `μ₃`/`c₃`/`r*` never inverted; the modulus reading is a `structure` hypothesis
  with **NO instance**; the Pythagorean consequence is *conditional*.
- **Nothing wired**; `free_parameters = 0`; no tier change. Sorry-free, no `native_decide`, no
  trivial-true, no new axiom.
- **What survives / what is proposed.** *Proved:* the carrier is a √−1 and the lift modulus is a
  quadrature (generic algebra). *Proposed (scope-(a)):* the modulus reading + the transverse-slope
  relocation. The proposal is falsifiable — a derived `(fs, s)` with `√(fs²+s²) ≠ r*` refutes the
  modulus reading; a derived transverse `s ≈ 1.23` confirms it.

## Branch note

This branch (`claude/z-c-k-f-map-keystone-ub5yix`, PR #4346) previously held the φ(q₀) bar-odd
**phase-extraction wall-map** — a confirmed *negative* (the branch exponent is information-limited
at n≤44 Masbaum coefficients) whose central keystone object Ψ_LZ was separately Lean-refuted on
main (`592c658fc4`: Ψ_LZ ≠ the Σ(2,3,5) invariant, it is `q^{1/120}·S_JL`). Per that assessment
the phase-extraction line is closed as superseded and the branch is **redirected** to feed the
surviving χ(P) / transverse NA-Stokes lever, which this bridge does.

## Cross-references

- Carrier identification `E = χ(P)`, unit-modulus type tension: `2026-08-08-birkhoff-amplitude-e-crossratio-construction.md`, `QOU/QBeta/BirkhoffAmplitudeE.lean`
- bar-odd `σE = −E`: `QOU/QBeta/DTIndexAmplitudeE.lean` (`amplitude_barOdd`)
- hyperbolic `P²−Q²` counterpart: `QOU/BraidKnot/BarSymmetricBarAntiSymmetricIdentities.lean`
- affine lift + surjectivity fit witness: `QOU/QBeta/A3AntiSelfAdjointLift.lean`, `computations/a3_magnitude_berezinian_crossterm_probe.py`
- surviving transverse object: bean `qou-prjo`; branching derivation of `(fs, s)`: bean `qou-jqof`
