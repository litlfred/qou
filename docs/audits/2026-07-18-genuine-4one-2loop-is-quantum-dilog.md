# The genuine 4₁ 2-loop is the quantum dilogarithm, not a classical potential — constructive completion of the #3874 correction

**Date:** 2026-07-18 · **Branch:** `claude/phib-genuine-4one-potential-2026-07-18` ·
**Tier:** derived + first-principles numerical (no fit) · **Discipline:** scope-(a) (re-scope, do
not delete #3874's number); no `c_k` wired; L2 unchanged (2/7). **Completes:** the merged #3874
(which showed the naive A₁ ≠ κ₁ but left "what identifies the potential" as the open piece).

## The owner ask

> "genuine Andersen–Kashaev/Dimofte 4₁ potential (fixes all derivatives at once) or to match the
> next invariant κ₁."

The honest answer is that **the genuine object is not a classical potential at all** — it is the
Faddeev quantum dilogarithm / the Andersen–Kashaev state integral (equivalently the Kashaev sum).
Three positive-controlled findings, no fit anywhere.

## A. Ground truth — the physical dimensionless 2-loop, from the Kashaev sum (no fit)

The dimensionless 2-loop of `⟨4₁⟩_N = Σ_{k} |(q)_k|²` (`q = e^{2πi/N}`), extracted by high-precision
Richardson extrapolation (70 dps, N → 3200) of

    ⟨4₁⟩_N = 3^{−1/4} N^{3/2} e^{N·Vol/2π} · (1 + a₁·(2π/N) + …),

converges to

    a₁^phys = 0.0882072…   vs   11/(72√3) = 0.0882063…   (rel err ~1e-5).

So the genuine dimensionless 2-loop is **11/(72√3)**, and

    **κ₁ = 2π · 11/(72√3) = 11√3π/108 = 0.5542165  (coeff of 1/N).**

**Convention resolved.** Ohtsuki's `κ₁ = 11√3π/108` is the coefficient of `1/N`; the
Dimofte–Garoufalidis dimensionless 2-loop `11/(72√3) = 0.08819` is the coefficient of `2π/N`. They
differ by exactly `2π`. (This retires a pre-#3874 confusion where a Kashaev-sum extraction returning
`0.0882` was mistaken for a mismatch against `κ₁`; it is `κ₁/(2π)`, the same object.) The corpus
κ-tower already **is** this physical object.

## B. The naive classical 2-loop is coordinate-dependent ⇒ it cannot be the invariant

For `V(z) = Li₂(z) − Li₂(1/z)` at the geometric saddle, the naive saddle 2-loop
`A₁ = V⁗/(8V''²) − 5V'''²/(24V''³)` takes **four different values in four coordinates**:

| coordinate | saddle | naive `A₁` |
|---|---|---|
| `z` | `e^{iπ/3}` | `1/3 + (17√3/108)·i` (the merged #3874 value) |
| `t` (`z=e^{2πit}`) | `1/6` | `−0.016038·i` (**pure imaginary**) |
| `w` (`z=e^{w}`) | `iπ/3` | `−0.016038·i` (= `t`; affine-equivalent) |
| `s` (`z=1/(1−s)`, Möbius) | `1−e^{−iπ/3}` | `−1/3 + (17√3/108)·i` |

Four coordinates, four values — none equal to the invariant `0.08819`. `t` and `w` agree because
`w = 2πi·t` is an **affine** change (the naive 2-loop is affine-invariant), while the nonlinear
`z ↔ t` and the Möbius `z ↔ s` change it. A quantity that depends on the coordinate is **not a knot
invariant**, so no classical potential's bare 2-loop can be `κ₁`.

> **Self-correction (positive control caught it).** The pre-#3874 exploration recorded that a
> "t-coordinate" potential gives a *real* 2-loop `≈ 0.1008`, seemingly close to `κ₁/(2π)`. That was
> a **computational error**: the true `t`-coordinate naive 2-loop is `−0.016038·i` (real part 0 to
> 65 dps), and its apparent closeness to `κ₁` was illusory. Re-running with a positive control
> surfaced the bug. The record is corrected here.

## C. The genuine object — the quantum dilogarithm

The **coordinate-invariant** 2-loop is the naive Feynman 2-loop **plus** the `ℏ¹` (`b²`)
"quantum-content" correction of the Faddeev quantum dilogarithm `Φ_b` at the saddle
(Dimofte–Garoufalidis, *The quantum content of the gluing equations*). Only that combination is a
knot invariant, and it equals `κ₁` — exactly what finding **A** reads off directly from the sum.
The classical potential `V = Li₂(z) − Li₂(1/z)` supplies the `0`-loop (`Vol`) and, via the Hessian,
the `1`-loop (torsion `3^{−1/4}`), but the `2`-loop `κ₁` receives an irreducible contribution from
the `b²` term of each quantum dilogarithm that no bare classical potential carries.

**So the answer to "genuine potential OR match κ₁" is a single statement:** there is no classical
potential whose bare 2-loop is `κ₁` (it is not even coordinate-invariant); the genuine potential is
the quantum dilogarithm, and its 2-loop — already in the corpus via the Kashaev fit — **is** `κ₁`.

## Scope discipline

- **scope-(a), re-scope not delete.** #3874's `A₁ = 1/3 + (17√3/108)·i` is not retracted: it stands
  as the exact `z`-coordinate naive 2-loop (Lean-certified in
  [`QOU/QBeta/PhibSaddleA1Exact.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/PhibSaddleA1Exact.lean)).
  Only the identification "the 4₁ state-integral 2-loop" was wrong; the discriminator missing from
  #3854/#3874 was **coordinate-invariance**, now supplied.
- **No `c_k` wired; L2 unchanged (2/7).** This is a structural clarification of *which object* the
  2-loop invariant is, not a production wiring.

## Compute

- Probe: [`computations/qbeta/qbeta_phib_genuine_4one_2loop_is_quantum_dilog.py`](../../computations/qbeta/qbeta_phib_genuine_4one_2loop_is_quantum_dilog.py) (exit 0)
- Witness: `computations/qbeta/qbeta-phib-genuine-4one-2loop-is-quantum-dilog.witness.json`

## Cross-references

- The correction this completes: [`2026-07-18-phib-a1-mis-identified-not-ohtsuki-kappa1.md`](2026-07-18-phib-a1-mis-identified-not-ohtsuki-kappa1.md) (#3874)
- The mis-identified merged probe: [`2026-07-17-phib-2loop-bdictionary.md`](2026-07-17-phib-2loop-bdictionary.md) (#3854), [`2026-07-17-phib-2loop-deformed-gluing-f1-feed.md`](2026-07-17-phib-2loop-deformed-gluing-f1-feed.md) (#3859)
- Ohtsuki κ-tower (the physical object): [`2026-07-12-bar-odd-s-three-routes.md`](2026-07-12-bar-odd-s-three-routes.md)
- κ₁ ground-truth producer: `computations/qbeta/qbeta_c3_kashaev_invariant_grounding.py`
