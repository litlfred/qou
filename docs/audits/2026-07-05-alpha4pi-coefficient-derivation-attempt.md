# Deriving the next-order α/(4π) coefficient of 1/α_EM — structural attempt

**Date:** 2026-07-05
**Scope:** KNOWN-OPEN problem. Attempt to *derive* (not fit) the next-order
additive correction to `1/α_EM` — the `~α/(4π)` term — as a higher-order
structural analog of the *derived* `2/(3π)` photon IR zero-mode, per the open
sub-problem "lift the next-order `α/(4π)` term to a higher Bloch group
`B_n(ℂ)`" in
[`alpha-em-derivation-open-problems.md`](../../content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md).
**Verdict:** **PARTIAL (predominantly OPEN)** — one factor continues the
template structurally; the operative coefficient is not derived.

---

## 0. Executive summary

- The additive decomposition is
  `1/α_EM = q[9]_q[10]_q  +  2/(3π)  +  (next-order term)`, where the first two
  terms are derived (tree-level force-carriers; photon IR zero-mode on Bring's
  surface `M_4`) and the third is the target.
- The target term is `≈ α·C` with `C ≈ 1/(4π) ≈ 0.0796`. Two corpus candidates:
  **C_A = [2]_q/(8π)** (the `H(q)` Habiro ansatz,
  [`alpha_em_4pi_fixed_point_solve.py`](../../computations/alpha_em_4pi_fixed_point_solve.py))
  and **C_B = 1/(2π[2]_q)** (the open-problems alternative).
- **Diagnostic finding (below):** at the canonical muon `q₀` the data *requires*
  `C_req ≈ 0.98645·(1/4π)` — i.e. **1.36 % below** a round `1/(4π)`. Candidate
  `C_A` sits **0.54 % above** `1/(4π)` (wrong side); candidate `C_B` sits 0.54 %
  below (right side, but only ~40 % of the needed deficit). The Habiro
  `(1−h²α)` deformation supplies a further −0.032 % (two orders too small). No
  proposed q-structure reaches the required 1.36 % deficit; the exponent solving
  `(2/[2]_q)^k = 0.98645` is `k ≈ 2.51` (non-integer). Discrimination between the
  candidates lives at the `~10⁻⁸` relative level in `1/α`, **below the
  framework's own reliability floor** (`q₀` known to ~3 ppb; `σ_α ≈ 1.1 ppb`).
- **Structural finding:** the one piece that genuinely continues the `2/(3π)`
  argument one order up is the **denominator** `8π = π·b₁`, where
  `b₁ = 2g = 8 = dim H¹(M_Bring)` is *the same* Betti number that produces the
  `n=1` zero-mode (`b₁/Area`). The **numerator** `[2]_q` and the loop
  normalization are **not** derived — they are matched to the Habiro element, and
  the required `n=2` Seiberg–Witten prolonged-period residue sum is never
  evaluated. So the coefficient supported by the *structural thread* is
  `C_A = [2]_q/(8π)`, but that same thread does not close, and `C_A` is on the
  wrong numerical side of the data.

---

## 1. Target coefficient and the two candidate forms (diagnostic only)

Compute at the canonical muon-anchored `q₀` used by the `computations/` layer
(`q-pinning-50-digit.witness.json`),
`q₀ = 1.1099785955573347198997632204832250266562084087801536866079`, in 60-dps
mpmath. `[2]_q = q+q⁻¹`, `h = q−q⁻¹`, `g = 4`, `b₁ = 2g = 8`,
`α = 1/137.035999084`.

| Quantity | Value |
|---|---:|
| `[2]_q` | `2.0108968691190758` |
| bare `q[9]_q[10]_q` | `136.82321965722218` |
| `2/(3π) = 2g/(4π(g−1))` | `0.21220659078919378` |
| bare `+ 2/(3π)` | `137.03542624801137` |
| CODATA `1/α` | `137.035999084` |
| residual after `2/(3π)` (rel.) | `−4.180×10⁻⁶` |

**Required next term** = `CODATA − (bare + 2/3π) = 0.000572836`. Writing it as
`α·C_req`:

| Coefficient | value | ratio to `1/(4π)` | side |
|---|---:|---:|---|
| **C_req (data-demanded)** | `0.0784992` | **0.98645** | — |
| `1/(4π)` (round QED) | `0.0795775` | `1.00000` | — |
| **C_A = [2]_q/(8π)** (Habiro `H`) | `0.0800110` | `1.00545` | **above** (wrong) |
| **C_B = 1/(2π[2]_q)** | `0.0791462` | `0.99458` | below (too small) |

Full `1/α` and residual per candidate (all *overshoot* CODATA):

| form | predicted `1/α` | residual (rel.) |
|---|---:|---:|
| `+ α/(4π)` | `137.03600695` | `+5.74×10⁻⁸` |
| `+ α·[2]_q/(8π)` (C_A) | `137.03601012` | `+8.05×10⁻⁸` (worst) |
| `+ α/(2π[2]_q)` (C_B) | `137.03600381` | `+3.45×10⁻⁸` (best) |

**Reading (diagnostic, not a fit):** numerically `C_B` is marginally best and
`C_A` marginally worst, but *all three overshoot* and *none* reaches the
required `0.98645·(1/4π)`. The residual gap is `≈10⁻⁸` relative — one to two
orders below the `q₀` uncertainty (~3 ppb) and the CODATA `σ_α` (~1.1 ppb).
**At this precision the framework cannot distinguish `1/(4π)`, `[2]_q/(8π)`, and
`1/(2π[2]_q)`; the "which candidate" question is below the noise floor.** This
is exactly what the open-problems block warned ("the coefficient `1/(4π)` is a
numerical near-match … and may refine to `1/(2π[2]_q)`").

The Habiro self-consistency route (`1/α = T + α·H·(1−h²α)`, the cubic solved in
`alpha_em_4pi_fixed_point_solve.py`) does not rescue this: `(1−h²α) = 0.99968`,
a −0.032 % correction, whereas the data wants −1.36 %. Two orders too small.

---

## 2. The structural derivation attempt

### 2.1 The template that *is* derived — `2/(3π)` at jet order `n=1`

[`prop:photon-ir-zero-mode-bring`](../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md)
derives the first correction from the Lagrangian, not by fit:

> The zero-momentum photon two-point function on the genus-`g` hyperbolic
> UV-completing surface `M_g` is governed by `ker Δ₁`. By Hodge theory
> `dim ker Δ₁ = b₁(M_g) = 2g`; the heat-kernel zero-mode contributes one
> constant mode `1/Vol` per harmonic generator, so
> `δ(1/α)_IR = b₁/Area = 2g/(4π(g−1))`. Gauss–Bonnet fixes
> `Area = −2πχ = 4π(g−1)` at curvature `−1`; at `g=4`, `= 8/(12π) = 2/(3π)`.

This is theorem-grade: Hodge decomposition + heat-kernel zero-mode + Gauss–Bonnet,
each a cited/Lean-closed step. It uses **only** topological (`b₁`) and
archimedean (`π`, `Area`) data — no fitted constant. This is the object the
`α/(4π)` term must imitate one order higher.

### 2.2 What the next order *would* need — jet order `n=2`

[`prop:jet-sw-tau-decomposition`](../../content/quantum-observable-universe/brings-surface/jet-sw-tau-decomposition.md)
grades the Archimedean functor as `τ = Σ_{n≥0} a_D^{(n)}`, with `a_D^{(0)}` the
electron period, `a_D^{(1)}` the IR zero-mode (§2.1), and each higher term an
"algebraic residue sum" `∮ λ_SW^{(n)}` of the prolonged Seiberg–Witten
differential. A genuine derivation of the `α/(4π)` term is the claim
`a_D^{(2)} = α·C` with `C` the sought coefficient — i.e. **evaluate the `n=2`
prolonged-period residue sum** and read off `C`.

**That evaluation is not carried out anywhere in the corpus.** The jet block
states `a_D^{(n)}` is a residue sum but never computes `a_D^{(2)}`; the
photon-IR block obtains the `n=2` form by *analogy*, not from `λ_SW^{(2)}`.

### 2.3 The one genuine structural thread — the denominator `8π = π·b₁`

The photon-IR block's substantive lead: the Schwinger-like `n=2` coefficient,
written `C_A = [2]_q/(8π)`, has

```
8π  =  π · dim H¹(M_Bring)  =  π · b₁ ,     b₁ = 2g = 8.
```

This is **the same Hodge datum** `b₁` that drives the `n=1` numerator. In the
`n=1` term `b₁` sits in the numerator over `Area = 4π(g−1)`; in the `n=2` term
`b₁` would sit in the denominator as `π·b₁`. Their placements are algebraically
dual (the Lean note `photon_selfEnergy_betti_product` records that
`[b₁/(4π(g−1))]·[π·b₁] = b₁²/(4(g−1))`, `π`-free — `64/12 = 16/3`).

**Honest classification of this thread:**

- *Real content:* `b₁ = 8` is genuinely the Bring first Betti number; that the
  same invariant appears in both corrections is dimensionally natural and is the
  correct *shape* for a one-order-up Hodge continuation. Numerator `[2]_q/2 → 1`
  at `q→1`, so `C_A → 1/(4π)`, recovering the round QED number in the classical
  limit — the right boundary condition.
- *What it does NOT establish:* `8π = π·b₁` is, at bottom, the identity `8 = 8`.
  It is *consistent with* `b₁` controlling the `n=2` denominator, but it does not
  *prove* the `n=2` loop coefficient is `1/(π·b₁)`. To promote consistency to
  derivation one must show, from the `n=2` Laplacian/`λ_SW^{(2)}` spectrum, that
  the self-energy normalization is `1/(π·b₁)` and the numerator is exactly
  `[2]_q` — neither is done. The block itself is explicit: *"Establishing that
  bridge — and the `−h²α` fermion-loop end-to-end — remains open (the
  Reshetikhin–Turaev two-loop track and the Bloch-class identification)."*

### 2.4 The `B_n(ℂ)` lift — the named open sub-problem

The `2/(3π)` reconciliation (that its `π` is a legitimate archimedean shadow, not
an external import) runs through `B₂(ℂ)`: Bloch–Suslin pentagon-uniqueness forces
every real archimedean realization to coincide with the Bloch–Wigner
dilogarithm `D` (the `B₂` regulator), per
[`prop:archimedean-functor-uniqueness`](../../content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md).
The open ask is whether `α/(4π)` is the analogous **`B₃(ℂ)` (trilogarithm /
higher-regulator)** class on Bring's surface.

**No such class is constructed in the corpus.** What exists toward it is (a) the
elementary `8π = π·b₁` observation (§2.3) and (b) the Habiro-element framing
`H(ζ₄)=0` (a cyclotomic modular zero,
[`prop:alpha-em-habiro-bar-involution`](../../content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md)),
proposed as *the candidate bridge* between the Hodge (`b₁/Area`) and
dilogarithm (`τ_arch`-via-`D`) realizations. A bridge candidate is not a
constructed `B₃` regulator. **The `B₂→B₃` lift for the next order is open.**

### 2.5 The precise missing step

> Evaluate the `n=2` prolonged Seiberg–Witten period `a_D^{(2)} = ∮ λ_SW^{(2)}`
> on `M_Bring` (equivalently, the one-loop photon self-energy / vacuum
> polarization on the genus-4 hyperbolic surface) and identify the resulting
> class in `B₃(ℂ)` (trilogarithm regulator). This computation would fix both the
> numerator (test the `[2]_q` Hecke-`q`-dimension claim) and the denominator
> normalization (test `1/(π·b₁)`) *from first principles*, replacing the
> current numerical match. Until it is done, only the classical-limit value
> `1/(4π)` and the `π·b₁` denominator-shape are structurally supported.

---

## 3. Refutation-scope discipline (AGENTS.md §"Before declaring refuted")

No result here is written as "refuted" / "ruled out" in scope-`(b)` (structural
exclusion) terms. Classifying the negatives:

- **(a) Scope-limited negative — the candidate coefficients, alone, at current
  precision, do not reproduce the data-demanded `C_req`.** The three candidates
  (`1/4π`, `[2]_q/8π`, `1/(2π[2]_q)`) all overshoot; the required
  `0.98645·(1/4π)` matches no low-degree q-power (`(2/[2]_q)^{2.51}`). This
  constrains *magnitudes*, not *ingredients*: it does **not** exclude a q-valued
  next-order coefficient. Indeed the discrimination is below the framework's
  reliability floor (`~10⁻⁸` rel. vs. `q₀`/`σ_α` at `~10⁻⁹`), so a future `q₀`
  re-pin or a genuine `a_D^{(2)}` computation could land anywhere in the current
  spread. **Not a dead end — an under-resolved coefficient.**

- **(b) Structural exclusion — the only one cited, and it is *prior* corpus
  work, not new:** the *multiplicative* q-rational family for the correction was
  decisively excluded by the 100-dps PSLQ scan over a 54-element basis
  (invariant cited: PSLQ search-space entropy vs available precision — an
  entropy/precision bound, the admissible `(b)` category). Crucially, that
  exclusion is *why the additive route exists*; it says nothing against an
  additive `B_n(ℂ)` coefficient. The additive next-order coefficient is
  therefore genuinely **(a)-open**, not `(b)`-excluded.

I ran **no new wide PSLQ / numerical scan** for a closed form (formalize-first
discipline: the multiplicative scan is already `(b)`-excluded, and a single-point
additive fit is explicitly disallowed and would not constitute a derivation). The
§1 numerics are a *diagnostic* comparing two pre-existing candidates, not a search
for a new one.

---

## 4. Verdict

**PARTIAL (predominantly OPEN).**

- **Derived (inherited template):** `2/(3π)` at `n=1` — solid Hodge/Gauss–Bonnet.
- **Partial (this attempt's finding):** the next-order denominator continues the
  template structurally — `8π = π·b₁` with `b₁ = 8 = dim H¹(M_Bring)` the same
  Betti number, and the classical limit `[2]_q/2 → 1` recovers the round `1/(4π)`.
  This is the correct *shape* for a one-order-up Hodge/Bloch continuation and
  identifies `C_A = [2]_q/(8π)` as the coefficient the structural thread points
  to.
- **Open (the operative content):**
  1. the `n=2` prolonged-period residue sum `a_D^{(2)}` is never evaluated, so
     the loop normalization `1/(π·b₁)` and the numerator `[2]_q` are matched, not
     derived;
  2. no `B₃(ℂ)` higher-regulator class realizing `α/(4π)` on Bring's surface is
     constructed (the named open sub-problem);
  3. numerically the data demands `C ≈ 0.986·(1/4π)`, which the structurally
     favored `C_A` misses on the wrong side, while the discrimination is below the
     framework's reliability floor — so even the *numerics* cannot currently
     confirm any candidate.

**Which candidate the argument supports:** the *structural thread* (§2.3) favors
**`C_A = [2]_q/(8π)`** (denominator `π·b₁`, numerator the Hecke 2-channel
q-dimension). The *bare numerics* (§1) marginally favor `C_B = 1/(2π[2]_q)`.
Neither is derived, and the two disagree at `q ≠ q₀` — the classic signature
(cf. Form A vs Form B in the open-problems block) of a single-point coincidence
rather than a shared function of `q`. **The honest statement is that the
coefficient is `1/(4π)` at the ~1 % / classical-limit level with a derived
`π·b₁` denominator, and is otherwise open.**

The canonical statement remains the additive form with the `α/(4π)` term flagged
as a numerical near-match pending the `n=2` `a_D^{(2)}` / `B₃(ℂ)` computation. No
change to any content block is warranted by this attempt; it records the precise
open step and rules a fabricated closure out.

---

### Files read
- `content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md`
- `content/quantum-observable-universe/predicted-spectra/em-coupling-chern-simons.md`
- `content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md`
- `content/quantum-observable-universe/predicted-spectra/em-coupling-bring-zero-mode.md`
- `content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md`
- `content/quantum-observable-universe/brings-surface/jet-sw-tau-decomposition.md`
- `computations/alpha_em_4pi_fixed_point_solve.py`, `computations/q-pinning-50-digit.witness.json`
