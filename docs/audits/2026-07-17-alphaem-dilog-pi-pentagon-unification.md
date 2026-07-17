# The α_EM `1/(π b₁)` wall and the additive `2/(3π)` correction are the *same* dilogarithm-pentagon shadow

**Date:** 2026-07-17
**Branch:** `claude/alphaem-dilog-1ppq-2026-07-17`
**Scope:** structural synthesis (formalize-first search-narrowing); no `c_k` wired, no tier change.

## Claim

The two `π`-carrying pieces of the α_EM program —

1. the **photon 1-loop determinant measure** `1/(π b₁)` on the Bring Jacobian
   `J(M) = H¹(M;ℝ)/H¹(M;ℤ)` (the *single wall* to 2-loop derivability, per
   [`2026-07-14 alpha-em 2-loop derivability map`](2026-07-14-alpha-em-2loop-derivability-map.md) — the
   zero-mode `1/Area` measure is decisively excluded, `−1419 ppb ~9500σ`), and
2. the **additive Bring zero-mode correction** `2/(3π) = 2g/(4π(g−1))` at `g=4`
   (the summand that closes the singlet gap once the PSLQ-dead multiplicative
   q-rational family is abandoned — see
   [`alpha-em-derivation-open-problems.md`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md)),

carry the **same `π`**, and it is the **pentagon-forced Bloch–Wigner
dilogarithm shadow** — i.e. the α_EM measure wall *is* the AG-dilog keystone
`conj:alg-geom-dilog-equiv` (`qou-evo7`, `lw70`), not a separate problem.

> ## ⚠ Update 2026-07-17 — discriminant probe *weakens* this claim; leading order favours the gauge reading (#3810)
>
> A direct probe ([`alphaem_dilog_bloch_probe.py`](../../computations/alphaem_dilog_bloch_probe.py),
> witness `alphaem-dilog-bloch-probe.witness.json`) tested the claim and came
> back **scope-(a) NEGATIVE for the simplest dilog identification**, and I record
> it faithfully rather than preserve the thesis:
>
> 1. **No clean bare-`D` identification.** No natural Bring / `4₁` / golden
>    Bloch–Wigner value (`D(e^{iπ/3})`, `D(e^{2πi/5})`, Rogers `π²/10`, `π²/15`,
>    Catalan) is a clean low-complexity rational multiple of `2/(3π)` or `1/(8π)`.
> 2. **Decisive — the arithmetic signature is *gauge*, not dilog.** `2/(3π) =
>    (2/3)·(1/π)` carries a **single power of `π`**, the signature of a gauge-loop
>    `1/(4π)` factor. Dilogarithm data carries `π²` (Rogers values) or is an
>    `O(1)` real (`D`). A bare-`D` origin would need `D(z) = 2π/3 = 2.094`, but
>    the nearest natural value `Vol(4₁) = 2.030` misses by 3%.
>
> So **#3810's reading — `1/(πb₁)=1/(8π)` is the standard `½·1/(4π)` gauge loop,
> `b₁=8` a genus-4 coincidence — is favoured at leading order**, and the strong
> form of the claim below ("the two `π`'s *are* the same dilog shadow") is **not
> supported**. What survives is the *weaker* hypothesis: **if** there is dilog
> content, it lives at the **regulator-normalisation** (Beilinson period `π`) or
> the **next-order `Bₙ(ℂ)`** level — not in a bare leading `D`-value. That is now
> the honest open question, and the burden is on the dilog reading to exhibit it.
> The `2/(3π)` "pentagon-forced" assertion in `alpha-em-derivation-open-problems.md`
> inherits the same caveat: it is a single-`π`, gauge-shaped quantity at leading
> order. (The structural bridge below is retained as the *hypothesis that was
> tested*, not as an established result.)

## Why the two `π`'s coincide (the Kronecker-limit / Bloch-Wigner bridge)

The open-problems doc already fixes the origin of the `π` in `2/(3π)`:
Bloch–Suslin pentagon-uniqueness forces **every real-valued archimedean
realization of the substrate pentagon (5-term) data to coincide with the
Bloch–Wigner dilogarithm `D`**, and the `π` in `2/(3π)` is the unique
archimedean shadow of that pentagon data — not an external import.

The wall `π` has the *same* source, through the flat-torus determinant:

- `J(M)` is a **flat torus** `ℝ^{b₁}/Λ` (`b₁ = 2g = 8` at `g=4`). The photon
  1-loop normalization is `det' Δ` on this torus.
- For a flat torus, `det' Δ` is governed by the **Kronecker limit formula** /
  Epstein zeta function: the regularized determinant is a `π`-normalized
  modular object (`log|η|` at genus 1; the higher-rank Epstein/`SL(b₁,ℤ)`
  analogue for the Bring Jacobian). The `ζ`-anomaly `ζ_{Δ¹}(0) = −b₁` (Track 3's
  first structural check, [`three-front-attack`](2026-07-17-three-front-attack-specs.md)) is the
  flat-torus statement "no interior heat coefficient, so `ζ(0) = −#(harmonic
  1-forms) = −b₁`", which is what puts `b₁` under the `π`.
- The Kronecker limit formula's constant term is a **dilogarithm** (Bloch–Wigner
  `D` / Rogers `L`) evaluation — the same `D` that pentagon-uniqueness forces.
  So the torus-determinant `π` in `1/(π b₁)` is the Bloch–Wigner shadow, exactly
  as for `2/(3π)`.

Both `π`'s therefore descend from one object: the pentagon-coherent substrate
data realized archimedeanly as `D` on the Bring Jacobian.

## Consequence — the α_EM closure is a Bloch-group computation, not a q-rational search

This *narrows the search* (formalize-first):

- **Ruled out (already):** the 100-dps PSLQ scan over the 54-element q-rational
  basis (incl. `π, ζ(3), log 2`) found no relation — the multiplicative
  q-rational family cannot close the `1.55×10⁻³` gap. Any block-diagonal Gram
  deformation stays in that dead family.
- **The live route** is the two open computations the open-problems doc names,
  now seen as **one problem with the AG-dilog keystone**:
  (i) identify the explicit **Bloch-group class** `[z] ∈ B(ℂ)` on Bring's
  surface whose `D([z])` is the `2/(3π)` (and, at next order, `1/(π b₁)`)
  shadow; (ii) lift the `α/(4π)` term to a **higher Bloch group** `B_n(ℂ)`.
  Closing `conj:alg-geom-dilog-equiv` (the cyclic-dilog pentagon / monodromy
  datum) is exactly what supplies the archimedean `D`-evaluation both `π`'s need.

So the two most-active 1ppQ fronts — the α_EM per-loop measure (#3812/#3814) and
the algebraic-geometric dilogarithm equivalence (#3773/#3807) — are **the same
wall viewed from two sides**. Progress on the Bloch-class identification feeds
both.

## Scope discipline (critical distance)

- This is a **structural connection + search-narrowing**, not a closure: the
  explicit Bloch-group class on Bring's surface is **not** identified here, and
  the Kronecker-limit-formula → `D` bridge is stated at the level of the
  standard flat-torus determinant theory, not formalized. Marking it as the
  mechanism is a *direction*, subject to the anti-laundering rule — a `D([z])`
  matching `2/(3π)` must be **derived** from an identified class, not fitted.
- The claim is falsifiable: if the explicit Bring Bloch class, once identified,
  gives `D([z]) ≠ 2/(3π)` (or the higher lift `≠ 1/(π b₁)`-consistent), the
  unification fails and the two `π`'s are coincidental. Named kill-criterion.
- No `c_k` value; wires nothing; no tier change. `1/α_bare = q[9]_q[10]_q`
  (−0.155%) stays the derived headline; the correction stays open.

## Coordination

Complementary to the active fronts — coordinate intent on #3812/#3814 (α_EM
per-loop measure) and #3773/#3807 (AG-dilog). This audit supplies the *bridge*
(the two `π`'s share the Bloch-Wigner origin); those PRs carry the constructive
attacks.

-- Ref: [manuscript] content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md
