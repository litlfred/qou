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

---

## B₃(ℂ) closed-form attempt (2026-07-05, follow-up)

**Scope:** the specific route named in
[`docs/coordination/2026-06-13-alpha-em-phase5-rt-ledger.md`](../coordination/2026-06-13-alpha-em-phase5-rt-ledger.md)
— construct the Bloch class `[Z₂] ∈ B₃(ℂ)` from the *ideal-hyperbolic-tetrahedron
cross-ratio data* of Bring's-surface fundamental domain, evaluate the Goncharov /
single-valued trilogarithm regulator `L₃([Z₂])`, and test whether it yields a
**closed form** for the O(α²) coefficient. Companion compute:
[`computations/bring_b3_closed_form_attempt.py`](../../computations/bring_b3_closed_form_attempt.py)
(standalone mpmath, 60 dps; emits no witness — records an open negative).

**Verdict: OPEN.** A genuine, exact, parameter-free B₃(ℂ) value *does* exist in
Bring's arithmetic — but it supplies **no** closed form for the coefficient, and
the obstruction is now identifiable at three sharp levels. No fit was made and no
closure fabricated.

### B.1 The positive nugget — an exact B₃ Bloch value in Bring's √5 arithmetic

Bring's curve is the genus-4 arithmetic curve with automorphism group `S₅`
(order **120** — the RT ledger's "120 symmetries"; *not* PSL₂(11), which is a
misattribution — the maximal genus-4 group is `S₅`). Its natural field of
definition carries `ℚ(√5)`; the natural algebraic points are the golden-ratio
unit `φ = (1+√5)/2` and its powers. The correct arithmetic home for a
*trilogarithm* (weight-3 / B₃) class is therefore the higher-regulator lattice of
`K₅(ℚ(√5))` (Borel/Zagier), whose single-valued trilogarithm generators at
golden-ratio units evaluate **exactly** (verified to 40+ dps):

$$
  \mathcal L_3\!\left(\tfrac{1}{\varphi^{2}}\right) \;=\; \tfrac{4}{5}\,\zeta(3),
  \qquad
  \mathcal L_3\!\left(\tfrac{1}{\varphi}\right)+\mathcal L_3\!\left(-\tfrac{1}{\varphi}\right)
  \;=\; \tfrac{1}{5}\,\zeta(3),
$$

with `1/φ² = (3−√5)/2`, `𝓛₃` the Zagier single-valued (Bloch–Wigner–Ramakrishnan)
trilogarithm. The cyclotomic `L(3,χ₅)` sector (the second Borel generator, `r₁=2`
real places ⇒ `rank K₅(ℚ(√5)) = 2`) satisfies the exact distribution relation
`Im Li₃(ζ₅) = 2·Im Li₃(ζ₅²)`. **This is the object the scaffold asked for**: a
genuine trilogarithm Bloch class, on Bring-natural arithmetic points, with a
closed form. It sharpens the RT-ledger scaffold's "simple multiples of Li₃(ζ₅) or
Li₃(1/φ) do not match" to the *exact* Borel/Zagier lattice `{ζ(3), L(3,χ₅)}`.

### B.2 The negative — the coefficient does not close

The data-demanded next term (muon-`q₀`, 60 dps) is
`T_data = CODATA − bare − 2/(3π) = 5.72836×10⁻⁴`, i.e.
`C_data = T_data/α = 0.0784992 = 0.98645·(1/4π)`.

No **parameter-free** archimedean normalization of the Borel generators
reproduces it. Diagnostic (not a fit): `C_data/[(4/5)ζ(3)] = 0.08163`,
`C_data·π²/ζ(3) = 0.6445` (≠ 2/3), and a **bounded** PSLQ over the *canonical*
generators only —
`{ζ(3), L(3,χ₅)}`, `{ζ(3), L(3,χ₅), π³}`, `{ζ_F(3), α/(4π)}`, tol `10⁻²²`,
maxcoeff `10⁶` — returns **no integer relation** in every case. (This is *not*
the forbidden wide PSLQ scan: it tests only the three canonical Borel/regulator
combinations the geometry would supply, and reports the null honestly.)

### B.3 The three-level obstruction (why it is genuinely OPEN, not a near-miss)

1. **Dimensional/geometric — the scaffold's cycle is ill-posed as stated.**
   `B₃` / the trilogarithm is **3-dimensional** scissors-congruence data: its
   generators are ideal hyperbolic **tetrahedra** (parametrised by a single
   cross-ratio each), living in `ℍ³`. Bring's surface is a **2-real-dimensional**
   hyperbolic surface; its fundamental domain (the regular map `{5,4}`: 12 ideal
   pentagons, 30 edges, 12 vertices) tiles into ideal **triangles**, which are
   `B₂`/dilogarithm data — *not* tetrahedra. There is no canonical 3-manifold or
   ideal-tetrahedron decomposition attached to the 2-surface to supply a B₃
   **cycle** `Z₂ = Σ[z_i]₃`. So the ledger step "construct `[Z₂]` from the ideal
   hyperbolic tetrahedra of the fundamental domain" is *not well-posed* for a
   2-surface — the tetrahedra it invokes do not canonically exist. *(Scope-(a):
   this refutes the construction **as posed**; it does **not** exclude that some
   B₃ class — e.g. from an auxiliary 3-manifold, a mapping torus, or a Goncharov
   cosimplicial/Grassmannian polylog on configurations of ideal vertices — is
   ultimately relevant. §B.1 shows the target arithmetic ring genuinely carries
   B₃ classes.)*

2. **Normalization is unfixed — no forcing analogue of the `n=1` heat kernel.**
   Even granting the arithmetic home, the map `{ζ(3), L(3,χ₅)} → δ(1/α)` needs an
   overall rational × π-power normalization that the geometry does not fix. The
   `n=1` term is *derived* precisely because the heat-kernel zero-mode forces
   `b₁/Area` with **zero** free parameters; the `n=2` analogue is the residue sum
   `a_D^{(2)} = ∮λ_SW^{(2)}` (`prop:jet-sw-tau-decomposition`), and *that
   computation is still never carried out*. Absent it, the B₃ value's coefficient
   is a free choice — matching it to `T_data` would be a single-point fit, which
   the corpus and this task forbid.

3. **Numerical floor — the target is only ~0.5%-determined (sharpened).**
   `T_data ≈ 5.7×10⁻⁴` is a small difference of large numbers (`~137`). Propagating
   the ~3 ppb muon-`q₀` uncertainty (it enters multiplied by `~137`) gives a
   **relative uncertainty of ≈ 0.49% in `C_data`** (probe: `dT/T ≈ 4.9×10⁻³`). The
   headline "1.4% below `1/(4π)`" is therefore only **~2.8×** the `q₀` band, and the
   inter-candidate spread (`1/4π` vs `[2]_q/8π` vs `1/(2π[2]_q)`) sits far below it.
   A 0.5%-uncertain target admits a large family of "clean" B₃ expressions; **no
   closed form can be numerically validated or discriminated** here. This
   strengthens the parent audit's `10⁻⁸`-floor observation: the coefficient is not
   merely under-resolved at `10⁻⁸`, it is under-determined at the **percent** level
   once `q₀` propagation is included.

### B.4 Refutation-scope discipline (AGENTS.md §"Before declaring refuted")

- **(a) Scope-limited negatives:** (i) the specific "tetrahedra-of-the-2-surface"
  cycle is ill-posed as written; (ii) the canonical Borel generators
  `{ζ(3), L(3,χ₅)}`, evaluated parameter-free, do not reproduce `C_data`. Both
  constrain *this construction / these combinations*, not the *ingredient*: a B₃
  class from an auxiliary 3-dimensional or cosimplicial structure is **not**
  excluded, and §B.1 shows the arithmetic genuinely supports weight-3 classes.
- **(b) Structural exclusions:** none newly asserted. The only permanent exclusion
  in play remains the prior 100-dps 54-element **multiplicative** PSLQ (entropy/
  precision bound — admissible (b)), which is *why* the additive/`Bₙ` route exists
  and says nothing against it.

### B.5 The precise remaining step (unchanged in kind, sharper in content)

Evaluate `a_D^{(2)} = ∮λ_SW^{(2)}` on `M_Bring` (equivalently the `n=2`
photon vacuum-polarization spectral sum) and read off its regulator image. The
result would fix the normalization from first principles; the natural target
lattice is now known to be the `K₅(ℚ(√5))` Borel pair `{ζ(3), L(3,χ₅)}`, with the
exact generator `𝓛₃(1/φ²) = (4/5)ζ(3)` as its `ζ(3)`-axis. Until that spectral
computation exists — and until `q₀` is pinned two-to-three orders tighter so the
target is better than 0.5% — the coefficient is **OPEN**. No content block is
changed by this attempt; it records the exact B₃ value, the sharpened
obstruction, and rules out a fabricated closure.

### Files added / read (follow-up)
- **Added:** [`computations/bring_b3_closed_form_attempt.py`](../../computations/bring_b3_closed_form_attempt.py)
- Read: `computations/bring_zero_mode_bloch_hunt.py`,
  `computations/bring_trilog_zeta5_depth_3.py`,
  `computations/bring_d3_goncharov_probe.py`

---

## Auxiliary-3-manifold route

**Scope:** the lead sharpened out of §B.3.1 — since Bring's *surface* (2 real
dimensions) supplies no ideal-tetrahedron data, a genuine `B₃`/trilogarithm class
must come from an **auxiliary 3-manifold** canonically attached to the α_EM
construction. This section works that lead to its end. Companion compute:
[`computations/bring_aux_3manifold_weight_probe.py`](../../computations/bring_aux_3manifold_weight_probe.py)
(standalone mpmath, 50 dps; emits no witness — records an open negative).

**Verdict: OPEN.** The route does *not* close, and the reason is a **new, sharper
obstruction than the §B "dimensional ill-posedness on the 2-surface":** it is a
**weight (regulator-degree) obstruction**. No 3-manifold canonically attached to
Bring's surface can carry the target class, because a 3-manifold period is a
*weight-2* (dilogarithm) regulator while the target is *weight 3* (trilogarithm),
and — decisively — the weight-2 regulator of the relevant field vanishes. No fit
was made and no closure fabricated. The finding **re-scopes** the auxiliary-
3-manifold idea from "compute it" to "(a)-refuted as posed, with one admissible
(b)", and redirects the open step to a genuinely non-3-manifold object.

### C.1 The most principled auxiliary 3-manifold — and why

Three candidates were weighed against the test "canonically attached to the α_EM
construction, **not** chosen to fit":

| Candidate | Canonicity | Hyperbolic? | Verdict |
|---|---|---|---|
| **Unit-tangent / frame bundle** `UT(M_Bring) = \mathrm{PSL}_2(\mathbb R)/\Gamma_{\mathrm{Bring}}` | **Highest** — it *is* the frame bundle of the state bundle `\mathcal S` already in the QOU tuple `(\mathbf C,\varTheta,G,\mathcal S)`; no choices | **No** — Seifert-fibered (`\widetilde{\mathrm{SL}_2}` geometry) | **chosen** (canonical) |
| Mapping torus `M_\varphi` of a Bring automorphism `\varphi\in S_5` | High, but needs a choice of `\varphi` | **No** — the `S_5` automorphisms are *conformal ⇒ finite order*; a periodic mapping torus is Seifert-fibered | rejected (still Seifert) |
| Pseudo-Anosov mapping torus | Low — the pA class is **not** the conformal `S_5` symmetry | Yes | rejected (fit-flavoured *and* wrong weight, below) |

The unit-tangent bundle is the unique principled pick: it is literally the
principal frame bundle `P` / state-bundle geometry named in the archimedean
tuple, so it is *canonically attached to the construction, not to the answer*.
`UT(M_{\mathrm{Bring}})` is an `S^1`-bundle over the genus-4 surface with Euler
number `e = \chi(M_{\mathrm{Bring}}) = 2-2g = -6`.

### C.2 Its scissors / B₃ class — computed, and it is empty

`UT(M_{\mathrm{Bring}})` carries `\widetilde{\mathrm{SL}_2}` geometry, hence:

- **Simplicial (Gromov) volume `= 0`.** Every Seifert-fibered 3-manifold has
  vanishing Gromov norm (the `S^1` action amenably collapses the fundamental
  cycle). So there is **no** ideal-tetrahedron decomposition contributing
  hyperbolic volume, and the `B_2`/`B_3` scissors class is trivial.
- **Chern–Simons invariant `\in \mathbb Q/\mathbb Z`.** For a Seifert space the
  `\widetilde{\mathrm{SL}_2}` Chern–Simons invariant is a rational function of the
  Euler and Seifert data (Kirk–Klassen / Auckly) — a *rational* number, carrying
  no transcendental dilog, let alone trilog.

The mapping tori of the conformal `S_5` automorphisms are periodic and give the
same Seifert conclusion. **The canonical auxiliary 3-manifold therefore supplies
exactly zero transcendental scissors content** — neither the `n=2` dilogarithm
nor the sought `n=3` trilogarithm.

### C.3 The sharp new obstruction — a weight/regulator mismatch (with cited invariants)

Even setting the Seifert-vanishing aside and asking for *any* hyperbolic
3-manifold, the route is blocked at the level of **regulator weight**:

1. **A hyperbolic 3-manifold period is weight 2, never weight 3.** For
   `M = \mathbb H^3/\Gamma`, the complex volume `\mathrm{Vol}(M) + i\,\mathrm{CS}(M)`
   is the image of the fundamental class `[M]\in H_3(\mathrm{PSL}_2\mathbb C)`
   under the **weight-2** (dilogarithm) Borel regulator on
   `K_3(\mathbb C)\cong B_2(\mathbb C)` (Neumann–Zagier; Neumann's complex-volume
   theorem). A 3-manifold's ideal-tetrahedron scissors class is a **dilogarithm**
   sum `\sum \mathcal L_2(z_j)`. A **trilogarithm** (`B_3`, weight 3,
   `K_5`) is *not* the volume or CS invariant of any hyperbolic 3-manifold.
   The RT-Phase-5 scaffold's target is weight 3 — **one weight above** anything a
   3-manifold classical invariant can produce.

2. **The relevant field kills exactly the weight a 3-manifold computes.**
   `\mathbb Q(\sqrt5)` is **totally real** (`r_1 = 2`, `r_2 = 0`). By Borel's
   rank theorem,
   $$
   \operatorname{rank}_{\mathbb Q} K_3(\mathbb Q(\sqrt5)) = r_2 = 0
   \quad(\text{weight 2 / dilog: trivial}),\qquad
   \operatorname{rank}_{\mathbb Q} K_5(\mathbb Q(\sqrt5)) = r_1 + r_2 = 2
   \quad(\text{weight 3 / trilog: rank 2}).
   $$
   The weight-2 regulator — *the one a 3-manifold volume realizes* — is **zero**
   for this field, while all the arithmetic content sits at weight 3. Numerical
   fingerprint (probe, 50 dps):
   - **weight 2 is decomposable/torsion:** `\mathrm{Li}_2(1/\varphi^2)=\pi^2/15-\ln^2\varphi`
     **exactly** (diff `= 0`) — a `\pi^2`-rational value up to a product of logs,
     i.e. the golden Bloch class is torsion (`K_3` rank 0), matching Landen;
   - **weight 3 is genuinely transcendental:** `\mathcal L_3(1/\varphi^2)=\tfrac45\zeta(3)`
     (diff `1.3\times10^{-51}`), the `\zeta(3)`-axis of the rank-2 `K_5`.

   So the geometry a 3-manifold provides (weight 2) is *precisely* the geometry
   `\mathbb Q(\sqrt5)` makes trivial. This is why **no** 3-manifold — Seifert or
   hyperbolic — can host the target: it would have to realize a weight-3 class as
   a weight-2 period, which is impossible, and even its weight-2 output is
   arithmetically empty here.

3. **This supersedes and explains §B's dimensional finding.** §B said "a
   2-surface has no ideal tetrahedra." The deeper reason a 3-manifold does not
   rescue it: ideal tetrahedra in `\mathbb H^3` are **weight-2** (dilog) data —
   they compute `K_3`, not `K_5`. Climbing from a surface to a 3-manifold climbs
   from weight ~1 (area, `\pi`) to weight 2 (dilog), **not** to weight 3. The
   trilogarithm is two rungs up from the surface and one rung above every
   3-manifold.

### C.4 Where the real weight-3 class does live (the redirect)

The `K_5(\mathbb Q(\sqrt5))` class `\{\zeta(3), L(3,\chi_5)\}`, with the exact
generator `\mathcal L_3(1/\varphi^2)=\tfrac45\zeta(3)` (§B.1, re-confirmed above),
is **real** — but its geometric home is **not** a 3-manifold. Its admissible
realizations are:

- **A Goncharov weight-3 regulator on a configuration of the 5 golden points.**
  Bring's `S_5` symmetry acts on 5 marked points (the quintic's roots / the `\{5,4\}`
  map data); the weight-3 regulator of `K_5` is a Grassmannian/cosimplicial
  polylogarithm on such configurations, **not** an ideal-tetrahedron sum. This is
  a 4- or higher-dimensional volume in Goncharov's sense, not a 3-manifold.
- **The Reshetikhin–Turaev / Chern–Simons *2-loop* perturbative invariant** of
  the auxiliary Seifert manifold. Perturbative CS carries `\zeta(3)` at two loops
  even when the *classical* volume vanishes — matching the physics fact that
  `\zeta(3)` first appears in QED at two loops (`a_D^{(2)}` order). This is the
  "Reshetikhin–Turaev two-loop track" already named in
  [`prop:photon-ir-zero-mode-bring`](../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md);
  the present finding says it is the *only* surviving weight-3 route, since the
  classical scissors route is weight-obstructed.

### C.5 Does it yield a parameter-free O(α²) coefficient? — No; the precise remaining step

No. The canonical 3-manifold gives a *zero* (Seifert), and no 3-manifold can give
the weight-3 target at all (§C.3). The data-demanded coefficient
`C_{\mathrm{data}}\approx0.986\cdot(1/4\pi)` is therefore **not** produced here,
and — consistent with §B.3 item 3 — it remains only `~0.5%`-determined once the
`~3` ppb muon-`q_0` uncertainty is propagated, so even a candidate weight-3 form
could not be numerically discriminated. The precise remaining step, sharpened:

> Evaluate the `n=2` object `a_D^{(2)}` **as a weight-3 regulator that is not a
> 3-manifold period** — either the Goncharov weight-3 configuration polylog on the
> five golden points, or the RT/CS **2-loop** perturbative invariant of
> `UT(M_{\mathrm{Bring}})` — and read off its image on the `K_5(\mathbb Q(\sqrt5))`
> lattice `\{\zeta(3), L(3,\chi_5)\}` (`\zeta(3)`-axis fixed by
> `\mathcal L_3(1/\varphi^2)=\tfrac45\zeta(3)`). Only that computation fixes the
> normalization from first principles; until it exists — and until `q_0` is pinned
> two-to-three orders tighter — the coefficient is **OPEN**.

### C.6 Refutation-scope discipline (AGENTS.md §"Before declaring refuted")

- **(a) Scope-limited negatives.** (i) The canonical auxiliary 3-manifold
  `UT(M_{\mathrm{Bring}})` is Seifert-fibered and contributes zero transcendental
  scissors content; (ii) mapping tori of the conformal `S_5` automorphisms are
  periodic ⇒ Seifert ⇒ volume 0. These refute *these constructions*, not the
  weight-3 *ingredient*: the `K_5(\mathbb Q(\sqrt5))` class exists and may enter
  via a Goncharov or RT-2-loop route (§C.4).
- **(b) Structural exclusion — one, newly asserted, with cited invariants.**
  *No hyperbolic-3-manifold scissors/volume/CS class can realize a `B_3`
  (trilogarithm) value.* Cited invariants: **(i)** the Neumann–Zagier
  complex-volume theorem (a 3-manifold period is the weight-2 dilog regulator on
  `K_3`), a proved regulator-degree fact; **(ii)** Borel's rank theorem giving
  `\operatorname{rank}K_3(\mathbb Q(\sqrt5))\otimes\mathbb Q = 0` (a proved
  dimension/rank bound). Together these exclude the *3-manifold-scissors
  realization of a `B_3` class on `\mathbb Q(\sqrt5)`* as a structural
  impossibility — an admissible `(b)` (proved-invariant exclusion), and precisely
  the kind AGENTS.md permits. **The excluded object is the realization method, not
  the ingredient:** the trilogarithm class itself stands (§B.1, §C.3 item 2).

### C.7 Files added / read
- **Added:** [`computations/bring_aux_3manifold_weight_probe.py`](../../computations/bring_aux_3manifold_weight_probe.py)
- Read: `content/quantum-observable-universe/brings-surface/jet-sw-tau-decomposition.md`,
  `docs/coordination/2026-06-13-alpha-em-phase5-rt-ledger.md`,
  `content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md`

---

## Session-2: mapping-torus + residue

**Date:** 2026-07-06 (RESEARCH bean `9un2`)
**Scope:** push past the weight-2 wall on the two Session-2 leads — (A) a genuine
`B₃`/trilogarithm class from the **mapping torus** of a substrate automorphism
(does a canonical pseudo-Anosov / infinite-order map exist?), and (B) direct
evaluation of the residue `∮λ_SW^{(2)}` to **decide the fork** (clean trilog/ζ(3)
Bloch world vs a genuine 2-loop QFT effect with no clean closed form).
Companion compute:
[`computations/bring_mapping_torus_residue_weight_probe.py`](../../computations/bring_mapping_torus_residue_weight_probe.py)
(standalone mpmath, 50 dps; emits no witness — records an open structural finding).

**Headline.** Both leads are worked to an honest verdict, and the session's new
value-add is a corpus cross-reference the parent §C **missed**: the substrate
*does* carry a canonical **hyperbolic** element (the lever-1 binding monodromy
`B`, `tr B = 2.6424 > 2`) — §C only considered the finite-order `S₅` surface
maps. Running that hyperbolic element through the mapping-torus construction
still fails, for a **new** reason (Sol geometry), and the fork **resolves toward
the 2-loop-QFT side**.

- **LEAD A — STRUCTURALLY-CLOSED** (three converging cited invariants).
- **LEAD B — fork RESOLVED (2-loop side); coefficient OPEN.** The classical
  `∮λ_SW^{(2)}` is weight-1 (q-algebraic) and *cannot* be the weight-3 target;
  so it does not decide the coefficient by evaluation — the coefficient is
  intrinsically a weight-3 = 2-loop object with **no classical closed form**, and
  the additive `~4 ppm`-level prediction is the honest ceiling.

### S2.1 LEAD A — the mapping torus of a substrate automorphism

The parent §C rejected mapping tori because the genus-4 Bring **surface**
automorphisms are the conformal group `S₅`, **all finite order** (Hurwitz:
conformal automorphisms of a compact Riemann surface form a finite group), so
their mapping tori are Seifert-fibered (vol 0). That is correct but **incomplete**:
it never asked whether the substrate carries *any* canonically-hyperbolic map.
It does. The **lever-1 binding monodromy**
([`2026-06-24-lever1-binding-monodromy-hyperbolicity.md`](2026-06-24-lever1-binding-monodromy-hyperbolicity.md),
[`…-lever1-lambda-sw-no-shortcut.md`](2026-06-24-lever1-lambda-sw-no-shortcut.md))
is the abelianised `λ_SW` / Gauss–Manin monodromy `B` on the rank-2 Hodge factor
(`= H¹` of the color elliptic curve `E_q`,
[`brings-surface/color-elliptic.md`](../../content/quantum-observable-universe/brings-surface/color-elliptic.md)):

$$
\operatorname{tr}B \;=\; \frac{a_D^{(2)}+a_D^{(4)}}{a_D^{(3)}}
\;=\; \frac{3\,(3q^4+8q^2+3)}{4\,q\,(q+1)^2}
\;=\; 2.6423863\ldots > 2,\qquad \det B = 1\ \text{(proved)}.
$$

Both forms agree to `|diff| = 0` at `q₀` (probe). `|tr B| > 2 ⇒ B` is
**hyperbolic in `SL₂(ℝ)`**, rapidity `θ_binding = arccosh(tr B/2) = 0.78145`,
`λ = e^{θ} = 2.18465`. So the substrate really does offer a hyperbolic object —
exactly what a pseudo-Anosov mapping-torus lead wants. It still does not build a
hyperbolic 3-manifold, on **three independent cited invariants**:

1. **(A1) Sol, not hyperbolic.** `B` is a rank-2 `SL₂` monodromy of an
   **elliptic (genus-1)** factor. Suspended as an automorphism of the elliptic
   fibre `T²`, a `|tr| > 2` (Anosov) element gives a **Sol-geometry** torus
   bundle. **Torus bundles are never hyperbolic** (geometrization): every
   `T²`-bundle has Gromov/simplicial volume `0` — Euclidean if `|tr| < 2`, Nil if
   `|tr| = 2`, Sol if `|tr| > 2`. No ideal tetrahedra, no `B₂`/`B₃` scissors
   content. *Cited invariant: the Thurston geometry / Gromov-norm-vanishing
   classification of `T²`-bundles.*
2. **(A2) `B` is not a mapping class at all.** `tr B = 2.6424 ∉ ℤ`
   ([integrality audit](2026-06-24-lever1-color-eq-monodromy-integrality.md)) so
   `B ∉ SL₂(ℤ)` — it is not even a genuine `T²` automorphism; it is a **real
   connection holonomy**, which suspends to no canonical 3-manifold. The only
   genuine surface diffeomorphisms are the finite-order `S₅` ones → Seifert →
   vol 0 (parent §C). The "bar-involution ∘ Dehn-twist" and "Reeb/geodesic return
   map" candidates named in the lead are either finite-order (bar-involution is an
   order-2 involution) or have Seifert suspension (the geodesic-flow suspension of
   `M_Bring` *is* the Seifert unit-tangent bundle `UT(M_Bring)`, parent §C.1); a
   genuine pseudo-Anosov would require an **ad-hoc choice of filling curve** to
   twist along — precisely the "fit-flavoured, not canonical" move the parent §C
   flagged. **No canonical pseudo-Anosov exists.**
3. **(A3) A hyperbolic 3-manifold would be weight-2 anyway** (parent §C.3,
   re-confirmed: `Li₂(1/φ²) = π²/15 − ln²φ` exactly ⇒ `K₃(ℚ(√5))⊗ℚ = 0`, while
   `𝓛₃(1/φ²) = (4/5)ζ(3)` genuine ⇒ `K₅` rank 2). The lead's premise —
   *"its ideal-tetrahedron scissors class IS the genuine `B₃` object"* — is
   **false**: an `ℍ³` ideal-tetrahedron scissors class is `B₂` (weight-2
   dilogarithm; Neumann–Zagier), **not** `B₃`.

**LEAD A verdict: STRUCTURALLY-CLOSED.** No substrate automorphism builds a
hyperbolic 3-manifold: the finite-order `S₅` maps give Seifert; the one
canonically-**hyperbolic** object `B` is not a mapping class and, generously
suspended, gives **Sol** (vol 0); and any hyperbolic 3-manifold is weight-2
regardless. *(b)-exclusion of the mapping-torus **realization method**, cited
invariants (A1) Thurston/Gromov `T²`-bundle classification, (A2)
`SL₂(ℤ)`-integrality failure, (A3) Neumann–Zagier weight-2 + Borel
`rank K₃(ℚ(√5)) = 0`. Scope-(a) on the ingredient: the weight-3
`K₅(ℚ(√5))` class still exists — it simply is not a 3-manifold period.)*

### S2.2 LEAD B — evaluate `∮λ_SW^{(2)}` (the fork-decider)

The corpus fixes `λ_SW = x\,dz` on `E_q`, and by `prop:sw-period-residue-sum` the
prolonged periods `a_D^{(n)} = ∮λ_SW^{(n)}` are an **algebraic residue sum** —
q-rational. The three **production-wired** anchors are exact q-rationals (probe,
verified at `q₀`):

| anchor | closed form | value at `q₀` |
|---|---|---:|
| `a_D^{(2)}` | `1` | `1.000000000` |
| `a_D^{(3)}` | `(q+1)²/(3q)` | `1.336965623` |
| `a_D^{(4)}` | `(3q²+4+3q⁻²)/4` (Family-A) | `2.532779664` |

So the classical `λ_SW` residue tower lives at **weight ≤ 1**: a residue of a
meromorphic 1-form / an abelian-integral period is algebraic, and the wired
anchors *are* q-rational. It reproduces the **tree / bare** content
`q[9]_q[10]_q` and the multiplicative q-rational family — exactly the family the
100-dps 54-element PSLQ already `(b)`-excluded from closing the α gap.

The data-demanded next term is **weight 3**, one-to-two rungs higher:

- `T_data = CODATA − bare − 2/(3π) = 5.72836×10⁻⁴`, `C_data = T_data/α = 0.0784992`
  (`= 0.986·(1/4π)`).
- Its arithmetic home is the weight-3 `K₅(ℚ(√5))` lattice `{ζ(3), L(3,χ₅)}` with
  the exact generator `𝓛₃(1/φ²) = (4/5)ζ(3)` (§B.1). `C_data/[(4/5)ζ(3)] = 0.0816`,
  `C_data/ζ(3) = 0.0653` — not clean; bounded PSLQ over both `{1, q, q⁻¹}`
  (weight-1 algebraic) and `{ζ(3), L(3,χ₅)}` (weight-3 Borel) returns **no
  relation** (honest null, not a wide scan).

**A weight-1 object cannot equal a weight-3 object** (transcendence-weight
grading) unless its coefficient is zero. Therefore `∮λ_SW^{(2)}`, evaluated
**classically**, is q-algebraic and **does not decide the coefficient** — it
yields the tree periods, not the correction. This is the same weight-jump that
killed the real-`q` `c_3` family (parent framing / PR #1821, `dc₃/dq ≈ 4.6×10⁶`
impossible for smooth real `f`): the correction is not a smooth q-algebraic
function.

**Fork resolution.** The fork was: clean trilog/ζ(3) ⇒ Bloch world; non-polylog ⇒
genuine 2-loop QFT with no clean closed form. The weight analysis shows the two
horns **merge at weight 3 = two loops**: the target's home *is* ζ(3) (the exact
`(4/5)ζ(3)` Bloch value exists), **and** ζ(3) is precisely the object that first
enters QED at **two loops**. What is decisively excluded is the *third*,
tacitly-hoped-for possibility — that `∮λ_SW^{(2)}` is a directly-evaluable
**classical** residue delivering the coefficient the way `2/(3π)` came from the
`n=1` Hodge zero-mode. It is not: that residue is weight-1 algebraic, two weights
below the target. The exact `(4/5)ζ(3)` is real but is **not** a classical-residue
output; its normalization into `δ(1/α)` is a genuine **2-loop** (Goncharov
weight-3 configuration regulator, or RT/CS 2-loop perturbative invariant)
computation, not a scissors-congruence evaluation.

**LEAD B verdict: fork RESOLVED toward the 2-loop-QFT side; the coefficient
remains OPEN as a 2-loop object.** There is **no classical closed-form residue**
for it; the honest current ceiling is the additive prediction at the
`~4 ppm`/`~57 ppb`-residual level. *Refutation scope (STRICT): `(b)`-excluded (cited
invariant = transcendence-weight grading) is only "the **classical** `λ_SW`
residue equals the coefficient". Whether a genuine 2-loop weight-3 computation
yields a clean closed form is `(a)`-OPEN — not claimed refuted.*

### S2.3 What is now sharp (net of the session)

- The parent §C's "mapping tori are Seifert because `S₅` is finite" is **upgraded**:
  the substrate's *one* canonical hyperbolic map (`B`, `tr = 2.6424`) also fails,
  via **Sol** geometry — so the closure holds even against the hyperbolic element
  the earlier sections did not consider.
- The three weight rungs are now explicit end-to-end: **`n=1` surface** →
  weight-1 (`π`, area; `2/(3π)`, DERIVED); **`n=2` classical 3-manifold /
  `λ_SW` residue** → weight-2 dilog / weight-1 algebraic (both **below** target);
  **target O(α²)** → weight-3 ζ(3) = **2-loop**. The gap the framework must cross
  is a genuine **loop** rung, not a scissors evaluation.
- The precise remaining step is unchanged in kind but now **doubly** motivated:
  evaluate `a_D^{(2)}` **as a weight-3 2-loop regulator** (Goncharov config
  polylog on the five golden points, or the RT/CS 2-loop invariant of
  `UT(M_Bring)`) landing on `{ζ(3), L(3,χ₅)}` — and pin `q₀` two-to-three orders
  tighter so the `~0.5%`-determined target can discriminate a candidate. Until
  then the coefficient is **OPEN**. No content block is changed; the session
  records the hyperbolic-`B` → Sol closure, the residue weight-1 finding, and the
  fork resolution, and rules out a fabricated closure.

### S2.4 Files added / read (Session-2)
- **Added:** [`computations/bring_mapping_torus_residue_weight_probe.py`](../../computations/bring_mapping_torus_residue_weight_probe.py)
- Read: `docs/audits/2026-06-24-lever1-binding-monodromy-hyperbolicity.md`,
  `docs/audits/2026-06-24-lever1-lambda-sw-no-shortcut.md`,
  `docs/audits/2026-06-24-lever1-trB-geometric-target.md`,
  `content/quantum-observable-universe/mass-theory/prolonged-periods-fixed-depth.md`,
  `content/quantum-observable-universe/mass-theory/cl3-zeta5-geometric-realization.md`,
  `content/quantum-observable-universe/brings-surface/color-elliptic.md`,
  `content/quantum-observable-universe/brings-surface/jet-sw-tau-decomposition.md`

---

## Session-3: 2-loop weight-3 attempt

**Date:** 2026-07-06 (RESEARCH bean `9un2`, continuation)
**Scope:** Session-2 *proved* the O(α²) coefficient is a genuine weight-3 = 2-loop
object (arithmetic home `{ζ(3), L(3,χ₅)}`, exact generator `𝓛₃(1/φ²) = (4/5)ζ(3)`)
and that the classical `λ_SW` residue — being weight-1 — cannot be it. Session-3
attempts the **actual 2-loop step**: does the *categorical 2-loop* — the `O(α²)`
term of the Habiro/Schwinger self-coupling `H(q) = [2]_q(1 − h²α)` — produce a
`ζ(3)·(rational in q)` with the data-demanded normalization
`C_data ≈ 0.98645·(1/4π)`, using the derived weight-3 home? Companion compute:
[`computations/bring_2loop_weight3_coefficient_probe.py`](../../computations/bring_2loop_weight3_coefficient_probe.py)
(standalone mpmath, 60 dps; emits no witness — records an open structural finding).

**Verdict: OPEN — the categorical 2-loop does NOT yield the ζ(3) coefficient.**
The self-coupling's *own* second-order term is structurally the **wrong weight**
(it is weight-1, a fibre-level q-deformation, not weight-3 ζ(3)); no
parameter-free weight-3 normalization built from the structurally-available
rationals hits `C_data`; and the deficit below `1/(4π)` is only `~2.8σ` over the
q₀ floor, so no clean weight-3 refinement is even numerically resolvable. The
exact missing ingredient is now pinned. No fit, no fabricated closure.

### S3.1 The self-coupling's own `O(α²)` term is weight-1 — and ~40× too small

Expanding the fixed-point self-coupling,
`δ(1/α) = α·H·(1 − h²α) = α·H − α²·(H·h²)`, with `H = [2]_q/(8π)`. The
**coefficient of `α²`** is `−H·h² = −[2]_q h²/(8π)` — a **q-rational over `π`**,
i.e. **weight 1** (`h = q − q⁻¹`, `[2]_q = q + q⁻¹` are weight-0 algebraic;
dividing by `π` is weight-1, the same rung as the `n=1` term `2/(3π)`). It is
**not** `ζ(3)` (weight 3). Numerically (probe, 60 dps, muon-`q₀`):

| quantity | value |
|---|---:|
| `O(α)` piece `α·H` | `5.8387×10⁻⁴` |
| `O(α²)` coefficient `−H·h²` (**weight 1**) | `−3.4970×10⁻³` |
| `O(α²)` piece `−H·h²·α²` | `−1.8622×10⁻⁷` |
| fractional 2nd-order shift `−h²` | `−0.0319 %` |
| **data-demanded deficit** below `1/(4π)` | `−1.3551 %` (**42.5× larger**) |

So the Habiro factor's second-order term is **both the wrong transcendence weight
and ~40× too small** to be the sought 2-loop `ζ(3)` object. This is the
**fibre-vs-observable wall** (AGENTS.md §"Im(q) at fibre vs observable level"):
`[2]_q(1 − h²α)` is a *fibre-level* q-deformation whose Taylor coefficients are
weight-≤1 q-rationals — exactly what one expects of a formal `q`-series — **not**
an archimedean 2-loop regulator. The parent §1 already noted the `(1 − h²α)`
correction is `−0.032 %` "two orders too small"; §S3.1 sharpens *why*: it is not
merely small, it is the wrong arithmetic weight, so no re-tuning of the Habiro
element (higher `h²ᵏαᵏ` terms, all weight-1) can ever supply the weight-3 target.

### S3.2 No parameter-free weight-3 normalization hits `C_data`

The genuine QED 2-loop object that carries `ζ(3)` with a **clean rational** is the
Petermann–Sommerfield electron `g−2` coefficient
`a^{(4)} = 197/144 + π²/12 − (π²/2)ln2 + (3/4)ζ(3)` — the `ζ(3)` enters at
**two loops** with rational **`3/4`**. (This is the concrete basis for
Session-2's "ζ(3) first enters QED at two loops.") Testing whether `C_data`
matches a **parameter-free** weight-3 normalization built only from the
structurally-available rationals — `3/4` (`g−2` two-loop), `4/5` (the Bloch
generator `𝓛₃(1/φ²) = (4/5)ζ(3)`), `1` — over the **derived** denominators
`{4π, 8π = π·b₁ (b₁=8), π², π³}` (probe, ratios to `C_data = 0.0784992`):

| candidate | value | ratio to `C_data` |
|---|---:|---:|
| `(3/4)ζ(3)/(4π)` | `0.0717425` | `0.9139` |
| `(4/5)ζ(3)/(4π)` | `0.0765253` | `0.9749` |
| `ζ(3)/(4π)` | `0.0956566` | `1.2186` |
| `(3/4)ζ(3)/π³` | `0.0290761` | `0.3704` |
| `(4/5)ζ(3)/π³` | `0.0310145` | `0.3951` |
| `ζ(3)/π³` | `0.0387682` | `0.4939` |
| `(3/4)ζ(3)/(π·b₁)` | `0.0358712` | `0.4570` |
| `ζ(3)/π²` | `0.1217938` | `1.5515` |

The nearest, `(4/5)ζ(3)/(4π)` (Bloch generator over the round QED denominator),
is **2.5 % low** — five times the `~0.49 %` noise floor (§S3.3), so **not** a
match. A **bounded** PSLQ over the canonical weight-3 Borel generators only —
`{ζ(3)/π³, L(3,χ₅)/π³}`, `{ζ(3), L(3,χ₅), 1/(4π)}`, and
`{δ, ζ(3), L(3,χ₅), α/π}` for the deficit `δ` — returns **no integer relation**
in every case (tol `10⁻²⁴`, maxcoeff `10⁶`). *(This is not the forbidden wide
scan: it tests only the three canonical Borel/regulator combinations the geometry
supplies, and reports the null honestly.)* **No parameter-free weight-3 form is
forced.**

### S3.3 The deficit below `1/(4π)` is not a resolvable higher-loop correction

Write `C_data = (1/4π)(1 − δ)`, `δ = 0.013551` (`1.355 %`). Two independent
reasons this cannot currently be a *clean* weight-3 refinement of `1/(4π)`:

1. **Magnitude.** A genuine 2-loop correction to a 1-loop coefficient is
   `O(α/π) ≈ 0.23 %`. The deficit is `δ = 5.83×(α/π)` — **~6× too large** to be
   a natural next-loop QED correction to a `1/(4π)` leading term. (Since the
   framework already reads the *whole* `α·C` term as `O(α²)`-fractional = 2-loop,
   a `1.355 %` shift *inside* it would have to be a 3-loop `O(α/π)` effect, which
   is `~0.23 %` — off by `5.8×`.)
2. **Resolution.** Propagating the physical `~3 ppb` muon-`q₀` uncertainty
   (q₀ sensitivity `d ln(bare)/d ln q = 6.84`, entering the `~137` bare term)
   gives `σ(C_data)/C_data ≈ 0.49 %` (probe: direct `q₀ → q₀(1+3\text{ppb})`
   re-evaluation). So `δ = 1.355 %` is only **`~2.8σ`** over the q₀ band, and the
   inter-candidate spread (`1/4π` vs `[2]_q/8π` vs `(4/5)ζ(3)/4π`) sits below it.
   A `~0.5 %`-uncertain, `2.8σ` deficit **cannot discriminate or validate** any
   clean weight-3 expression.

This confirms and sharpens the parent §B.3.3 / Session-2 floor: the coefficient
is under-determined at the **percent** level once q₀ propagation is included, so
even a *correct* weight-3 closed form could not be numerically confirmed here
without a two-to-three-order tightening of q₀.

### S3.4 The exact missing ingredient

The categorical 2-loop, **as instantiated by the Habiro self-coupling
`[2]_q(1 − h²α)`, is the wrong object**: its `O(α²)` term is a weight-1 q-rational
(§S3.1), not the weight-3 `ζ(3)` the target requires. The self-coupling supplies
only the **1-loop dressing** (the `α·H` term recovering the round `1/(4π)` in the
classical limit). The genuine 2-loop `ζ(3)` must come from a **separate,
weight-3 categorical diagram** with no realization inside the fibre-level
q-deformation:

> **Missing ingredient (sharpened).** Evaluate the **2-loop categorical
> self-energy / vacuum-polarization coefficient** — the categorical analog of the
> QED `g−2` two-loop `(3/4)ζ(3)` — as a genuine **weight-3 regulator**: the
> Reshetikhin–Turaev / Chern–Simons **2-loop perturbative invariant** of the
> Seifert manifold `UT(M_Bring)` (perturbative CS carries `ζ(3)` at two loops even
> when the classical volume vanishes), **or** the Goncharov weight-3 configuration
> polylog on the five golden `S₅` points, landing on the `K₅(ℚ(√5))` lattice
> `{ζ(3), L(3,χ₅)}` with `ζ(3)`-axis fixed by `𝓛₃(1/φ²) = (4/5)ζ(3)`. That
> computation — **not** any term of `[2]_q(1 − h²α)` — is what would fix the
> normalization from first principles. Until it exists (and until q₀ is pinned
> two-to-three orders tighter so the `~0.5 %`-determined target can discriminate a
> candidate), the coefficient is **OPEN**.

This is the same "RT/CS 2-loop track" already named in
[`prop:photon-ir-zero-mode-bring`](../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md)
and parent §C.4; Session-3's contribution is to **exclude the last remaining
"cheap" route** — that the answer falls out of the second-order term of the
existing self-coupling ansatz — and to identify *why* (weight mismatch), so no
future session re-attempts the Habiro-`O(α²)` closure.

### S3.5 Refutation-scope discipline (AGENTS.md §"Before declaring refuted")

- **(b) Structural exclusion — one, with cited invariant.** *The `O(α²)` term of
  the Habiro self-coupling `[2]_q(1 − h²α)` cannot be the target 2-loop
  coefficient.* Cited invariant: the **transcendence-weight grading** — its `α²`
  coefficient `−[2]_q h²/(8π)` is weight-1 (a q-rational over `π`), while the
  target is weight-3 (`ζ(3)`); a weight-1 object equals a weight-3 object only if
  its coefficient is zero. This excludes the **Habiro-`O(α²)` realization
  method**, and by extension every higher `h²ᵏαᵏ` term of the same ansatz (all
  weight-1). It does **not** exclude the weight-3 *ingredient*: the
  `K₅(ℚ(√5))` class `{ζ(3), L(3,χ₅)}` exists (§B.1) and may enter via the RT/CS
  2-loop or Goncharov route (§S3.4).
- **(a) Scope-limited negatives.** (i) No parameter-free weight-3 normalization
  from `{3/4, 4/5, 1} × {4π, 8π, π², π³}` reproduces `C_data` (nearest is `2.5 %`
  off, `5×` the floor); (ii) bounded PSLQ over the canonical Borel generators
  forces no relation. Both constrain *these combinations at this precision*, not
  the ingredient.
- **No wide scan / no single-point fit was run.** §S3.2 tests only the finitely
  many structurally-motivated candidates and the three canonical Borel PSLQ
  bases, and reports the nulls. The `(4/5)ζ(3)·a_D^{(4)}/π³` type of triple-factor
  coincidence (numerically within `0.07 %` of `C_data`) was **deliberately not**
  promoted: it is a post-hoc single-point match with no structural motivation for
  the `a_D^{(4)}/π³` normalization, and it fails the discrimination floor — exactly
  the numerology trap the task and AGENTS.md forbid.

### S3.6 Net of the session

- The **last "cheap" route is closed:** the O(α²) coefficient does **not** fall
  out of the second-order term of the existing self-coupling `[2]_q(1 − h²α)` —
  that term is weight-1 and `~40×` too small. The self-coupling is a 1-loop
  dressing only.
- The **weight ladder is now complete and diagnostic:** `n=1` surface →
  **weight 1** (`2/(3π)`, DERIVED); the Habiro self-coupling's own `O(α²)` term →
  **weight 1** (q-rational/`π`, this session); classical `λ_SW` residue →
  **weight 1** (Session-2); a 3-manifold period → **weight 2** (§C); the
  **target** → **weight 3 = 2-loop** `ζ(3)`. Every "classical" or "fibre-level"
  object the framework offers sits at weight ≤ 2; the target is one genuine
  **loop rung** above all of them.
- The precise remaining step is **unchanged in kind** but now with the last
  alternative eliminated: the coefficient must be the genuine **2-loop weight-3**
  RT/CS or Goncharov regulator on `{ζ(3), L(3,χ₅)}` (§S3.4), and q₀ must be pinned
  `~10²–10³×` tighter before any candidate is numerically discriminable
  (`~0.49 %` floor, `2.8σ` deficit). Until then the coefficient is **OPEN**.

No content block is changed by this attempt; the session records the
Habiro-`O(α²)` weight-1 closure, the parameter-free weight-3 nulls, the
`2.8σ` resolution floor, and the sharpened missing ingredient, and rules out a
fabricated closure.

### S3.7 Files added / read (Session-3)
- **Added:** [`computations/bring_2loop_weight3_coefficient_probe.py`](../../computations/bring_2loop_weight3_coefficient_probe.py)
- Read: `content/quantum-observable-universe/predicted-spectra/alpha-em-derivation-open-problems.md`,
  `content/quantum-observable-universe/braids-and-knots/alpha-em-habiro-bar-involution.md`,
  `computations/alpha_em_4pi_fixed_point_solve.py`,
  `computations/bring_mapping_torus_residue_weight_probe.py`

---

## Session-4: perturbative CS 2-loop on UT(M_Bring)

**Date:** 2026-07-06 (RESEARCH bean `9un2`, continuation)
**Scope:** the **sole remaining lead** named by every prior session — the
*perturbative Chern–Simons 2-loop invariant* of the canonical auxiliary
3-manifold `UT(M_Bring)`. Sessions §C / 2 / 3 excluded every classical route and
concluded "the answer must be a genuine 2-loop weight-3 object; perturbative CS
carries `ζ(3)` at two loops even at zero classical volume — evaluate it on
`UT(M_Bring)`." Session-4 does exactly that evaluation, as far as it is honestly
pinnable. Companion compute:
[`computations/bring_perturbative_cs_2loop_probe.py`](../../computations/bring_perturbative_cs_2loop_probe.py)
(standalone mpmath, 60 dps; emits no witness — records an open structural finding).

**Verdict: OPEN — and the sole surviving lead is RE-SCOPED.** The
perturbative-CS-2-loop-on-`UT(M_Bring)` route *as posed* does **not** carry a
Bring-specific weight-3 `ζ(3)` coefficient. The lead rested on a genuine physics
fact ("`ζ(3)` first enters QED at two loops") conflated with a *different*
CS/topological-string object; examined concretely on the actual Seifert data,
the route fails at **three** cited levels. This closes the last standing avenue as
written and redirects the open step. No fit; no fabricated closure.

### S4.1 Seifert data of UT(M_Bring) (explicit) + the Lawrence–Rozansky integrand

`UT(M_Bring) = UT(Σ₄) = \mathrm{PSL}_2(ℝ)/Γ_{Bring}` is the unit tangent bundle of
Bring's genus-4 surface (`\mathrm{Aut} = S₅`, order 120). Its Seifert data is
choice-free:

| datum | value |
|---|---:|
| base genus `g` | `4` |
| # exceptional fibres `n` | `0` (an honest `S¹`-bundle, not an orbifold fibration) |
| Euler number `e = χ(Σ₄) = 2−2g` | `−6` (the UT bundle of a surface has `e = χ`) |
| `b₁ = dim H¹(Σ₄) = 2g` | `8` |
| geometry | `\widetilde{\mathrm{SL}_2}` (Seifert-fibered, Gromov volume 0) |

For SU(2) CS on a genus-`g` Seifert circle-bundle of Euler number `e`, the
**trivial-connection ("perturbative") contribution** to `Z` is the
Lawrence–Rozansky / Verlinde Gaussian contour integral (Lawrence–Rozansky 1999,
*Comm. Math. Phys.* 205; Beasley–Witten 2005 non-abelian localization,
*J. Diff. Geom.* 70; Blau–Thompson):

```tex
Z^{\mathrm{triv}}(M) \;\sim\; \int dy \; \exp\!\Big( \tfrac{i\,e\,y^{2}}{2\hbar} \Big)\,
      \big( 2\sinh(y/2) \big)^{\,2-2g},
      \qquad \hbar = \frac{2\pi i}{k+2}.
```

The base-genus power is the Verlinde S-matrix factor `(S_{0j})^{2-2g}`. At `g=4`
the exponent is `2−2g = −6`: a **negative** power, i.e. an **order-6 pole at
`y=0`** (the trivial connection). This single sign is the crux of the whole
finding.

**Level / gauge dictionary.** The substrate gauge group is the categorical SU(2);
the level enters only through `\hbar = 2\pi i/(k+2)` with `q = \exp(\hbar)`, and the
q₀-analytic continuation puts the substrate `q₀` in the *fibre-level* formal
variable. Crucially, **the level/`q₀` dictionary never has to be pinned for this
verdict**: the obstructions below are all at the level of *which transcendental
constants the integral can produce*, independent of the value of `k` or `q₀`.
(This is the honest place the dictionary would matter — and it turns out not to
rescue the route, so it is not the blocker.)

### S4.2 (O1) `b₁ = 8` — UT(M_Bring) is not a rational homology sphere, so the 2-loop invariant is not even defined

`H₁(UT(Σ_g);ℤ) = ℤ^{2g} ⊕ ℤ/|e|`, so `b₁(UT(Σ₄)) = 2g = 8 ≠ 0`. The negative
integrand power `2−2g = −6` is precisely the analytic signature: the WRT
genus-`g` sum `Σ_j (S_{0j})^{2-2g}` **diverges** at the trivial connection
`j → 0` for every `g ≥ 1`, because the moduli space of flat SU(2) connections has
**positive dimension** — the `2g = 8`-dimensional Jacobian-torus directions
`H¹(Σ₄;ℝ) ⊗ \mathfrak{t}`. The perturbative Gaussian's Hessian is therefore
**degenerate** (8 zero modes), and the standard perturbative-CS 2-loop / LMO /
Ohtsuki invariant — whose construction *requires a rational homology sphere*
(Aarhus integral, `b₁ = 0`) — is **not defined** for `UT(M_Bring)`. This is the
same `b₁ = 8` that grounds the *derived* `n=1` term `b₁/\mathrm{Area}` and the
`n=2` denominator `π·b₁`; here the very same Betti number **obstructs** the
perturbative expansion the lead wanted to run.

*Cited invariants:* the Verlinde `(S_{0j})^{2-2g}` divergence at `j→0`
(reducible-connection non-isolation), and `\dim \mathcal M_{\mathrm{flat}} > 0`
for a genus-`g ≥ 1` base.

### S4.3 (O2) The Seifert fibre-sum produces only EVEN zetas — all rational, no ζ(3)

Even granting a regularization of (O1), the *content* the integral can generate
is fixed by the expansion of its integrand. Writing `x = y/2` and using
`\sinh x / x = \prod_{n\ge1}(1 + x^2/n^2\pi^2)`:

```tex
\log\!\frac{2\sinh(y/2)}{y}
   \;=\; \sum_{m\ge 1} \frac{(-1)^{m-1}}{m}\,
         \frac{\zeta(2m)}{(4\pi^{2})^{m}}\; y^{2m},
   \qquad \frac{\zeta(2m)}{\pi^{2m}} = \frac{|B_{2m}|\,2^{2m-1}}{(2m)!}\in\mathbb Q.
```

Every coefficient is a **rational number** (verified `m=1..5`: `ζ(2)/π²=1/6`,
`ζ(4)/π⁴=1/90`, …; the even-zeta series reproduces
`\log(2\sinh(y/2)/y)` to `|{\rm diff}| = 0` at `y=0.5`). Only **even** zeta
values appear, and each is rational-times-`π^{2m}`. Hence the
**manifold-specific perturbative series** of the trivial-connection integral is a
power series in `\hbar` with **rational** coefficients: the "2-loop" term is a
rational (Dedekind-sum / framing) number — **weight ≤ 2**, exactly the
Session-2 / §C weight verdict — and contains **no `ζ(3)`** (no odd zeta) at all.
The Seifert data of `UT(M_Bring)` therefore cannot supply a weight-3 coefficient
by this expansion, whatever the level.

### S4.4 (O3) The genuine 2-loop CS invariant is θ-graph = rational·Casson; the only ζ(3) in CS is a *universal* constant-map term

Two more precise facts finish the route:

1. **The genuine perturbative 2-loop CS invariant** (Axelrod–Singer configuration
   integral / the θ-graph, = the degree-1 part of the LMO invariant) of a
   *rational homology sphere* is a **rational multiple of the Casson–Walker
   invariant** (times a universal group factor). It is **not** `ζ(3)` — a 2-loop
   3-manifold invariant is a rational/Casson number. So the phrase "the 2-loop CS
   invariant carries `ζ(3)`" does **not** describe a manifold 2-loop invariant.

2. **The `ζ(3)` that genuinely appears "in Chern–Simons theory"** is the
   **constant-map / group-volume** term of the topological-string dual
   (Gopakumar–Vafa; the resolved-conifold constant map), whose arithmetic home is
   `ζ'(-2) = -ζ(3)/(4\pi^2)` (verified to 63 dps). This term is **universal**:
   it is proportional to the Euler characteristic / `\dim G`, it sits at
   **genus-0 order `g_s^{-2}`** in the topological-string counting (a *different*
   loop-count than the QED two-loop `g-2` `(3/4)ζ(3)`), and its overall
   normalization into `δ(1/α)` is exactly the **unfixed** piece. It therefore
   carries **no Bring-`b₁`-specific data** — the same "normalization is unfixed"
   wall as §B.3.2 / §S3.4, now seen to be the *only* place `ζ(3)` lives in the CS
   framework at all.

So the lead conflated (i) a genuine QED physical fact — `ζ(3)` at two loops in
`g-2` — with (ii) a CS/top-string `ζ(3)` that is a genus-0 *universal constant*,
and (iii) a "2-loop CS manifold invariant" that is actually rational·Casson. None
of the three is a Bring-specific weight-3 coefficient.

### S4.5 Structural-form diagnostic (constant-map shape; NOT a fit)

Granting the universal constant-map shape `∝ (2−2g)/2 · ζ(3)` = `3·ζ(3)` (with
`|χ|/2 = 3`) and testing only the **structurally-motivated** numerators
`{|χ|·ζ(3), (|χ|/2)·ζ(3), (4/5)ζ(3), ζ(3)}` over the **derived** denominators
`{4π, 8π=π·b₁, π², π³, (4π)², (4π)³}` against
`C_data = 0.0784992 = 0.98645·(1/4π)`: the nearest candidate is
`(4/5)ζ(3)/(4π) = 0.076525`, ratio `0.9749` — **2.51 % low**, `≈ 5×` the
`~0.49 %` q₀ noise floor. **No parameter-free constant-map form is forced.** (This
repeats §S3.2's null with the specific `|χ|=6` / `2−2g=−6` constant-map factor
added; it remains a null — reported honestly, not promoted.)

### S4.6 Refutation-scope discipline (AGENTS.md §"Before declaring refuted")

- **(b) Structural exclusions — two, each with a cited invariant.**
  **(b-i)** *The manifold-specific perturbative trivial-connection series of
  `UT(M_Bring)` cannot produce `ζ(3)`.* Cited invariant: the even-zeta rationality
  `\zeta(2m)/\pi^{2m} = |B_{2m}|2^{2m-1}/(2m)! \in \mathbb Q` (Euler; a proved
  arithmetic identity) — the `\sinh` fibre-sum generates only rational-weight-≤2
  coefficients, and a weight-1/2 object equals a weight-3 object only if its
  coefficient is zero (transcendence-weight grading). **(b-ii)** *The genuine
  perturbative 2-loop CS invariant of a QHS is rational·Casson, not `ζ(3)`.* Cited
  invariant: the Axelrod–Singer / LMO degree-1 identification of the θ-graph with
  the Casson–Walker invariant (a proved theorem). Both exclude the *route as
  posed* (this Seifert manifold, this classical perturbative object), **not** the
  weight-3 ingredient: the `K₅(ℚ(√5))` class `{ζ(3), L(3,χ₅)}` still exists (§B.1).
- **(a) Scope-limited negatives.** (i) `b₁ = 8` obstructs the standard
  perturbative construction (regularization-dependent, not a permanent
  impossibility of *some* equivariant/family invariant); (ii) no parameter-free
  constant-map form hits `C_data` at current precision.
- **No wide scan / no single-point fit.** §S4.5 tests only the finitely many
  structurally-motivated constant-map candidates and reports the null. The whole
  section is a structural evaluation of the *named* lead, not a search.

### S4.7 Net of the session — the lead is closed as posed; where the open step now points

- The **sole remaining lead is re-scoped from "compute it" to "(a)-refuted as
  posed, with two cited (b)-exclusions."** Perturbative CS 2-loop on
  `UT(M_Bring)` does not carry a Bring-specific `ζ(3)`: (O1) `b₁=8` ⇒ not a QHS ⇒
  the invariant is undefined; (O2) the fibre-sum is even-zeta/rational; (O3) the
  genuine 2-loop invariant is rational·Casson and the only CS `ζ(3)` is a
  universal constant-map term.
- **The weight ladder is now closed on the CS side too.** Every object the
  framework's *geometry* offers — surface (`weight 1`), classical 3-manifold
  period (`weight 2`), `λ_SW` residue (`weight 1`), Habiro self-coupling `O(α²)`
  (`weight 1`), **and now the Seifert perturbative CS series (`weight ≤ 2`,
  rational)** — sits at weight `≤ 2`. The weight-3 `ζ(3)` target is a genuine loop
  rung above all of them, and it does **not** descend from the classical or
  perturbative-Seifert geometry of `UT(M_Bring)`.
- **The one surviving *ingredient* (not route) unchanged:** the real weight-3
  `K₅(ℚ(√5))` class `{ζ(3), L(3,χ₅)}` with `𝓛₃(1/φ²) = (4/5)ζ(3)`. Its only
  admissible homes are now (a) the **Goncharov weight-3 configuration polylog on
  the five golden `S₅` points** (a `K₅`/higher-Grassmannian regulator, *not* any
  3-manifold or Seifert-CS object), or (b) a genuinely **equivariant / family**
  2-loop invariant of the *non-isolated* flat-connection moduli (the `b₁=8`
  Jacobian torus) — an object outside the standard QHS perturbative theory. Both
  require the `n=2` `a_D^{(2)}` normalization to be fixed from first principles,
  and both need q₀ pinned `~10²–10³×` tighter before any candidate is numerically
  discriminable (`~0.49 %` floor, `2.8σ` deficit). Until then the coefficient is
  **OPEN**.

No content block is changed by this attempt; the session records the explicit
Seifert data, the LR trivial-connection integrand, the `b₁=8` non-QHS
obstruction, the even-zeta/rational fibre-sum, the θ-graph/constant-map placement
of `ζ(3)`, and the re-scoping of the last standing lead — and rules out a
fabricated closure.

### S4.8 Files added / read (Session-4)
- **Added:** [`computations/bring_perturbative_cs_2loop_probe.py`](../../computations/bring_perturbative_cs_2loop_probe.py)
- Read: `computations/bring_aux_3manifold_weight_probe.py`,
  `computations/wenzl-lr-convention-adapter.witness.json`,
  `content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md`,
  `docs/coordination/alpha-em.md`
