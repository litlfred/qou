# α_EM 2-loop: what is derivable — the map, and the single load-bearing wall

**Date:** 2026-07-14 · **Branch:** `claude/canonical-derivation-c-k-n00n2h` ·
**Probe:** [`alpha_em_loop_measure_consistency_probe.py`](../../computations/alpha_em_loop_measure_consistency_probe.py)
(+ witness) · **Tier:** derivability audit (one exact consistency measurement) ·
**Scope:** (a); nothing wired; window used only to falsify.

Answers the owner's question — *what, in the α_EM 2-loop program, is actually
derivable vs. empirical vs. a genuine wall* — by tracing each factor of

$$
  \frac{1}{\alpha_{EM}} = \underbrace{q[9]_q[10]_q}_{\text{tree}}
    + \underbrace{\frac{b_1}{\mathrm{Area}}}_{\text{zero-mode}}
    + \underbrace{\frac{\alpha[2]_q}{\pi b_1}}_{\text{1-loop}}
    - \underbrace{\frac{\alpha^2[3]_q}{(\pi b_1)^2}}_{\text{2-loop } (\theta)}
    + \cdots,
    \qquad b_1 = 2g = 8,\ \mathrm{Area} = 4\pi(g{-}1) = 12\pi.
$$

## The map

| factor | value | status | why |
|---|---|---|---|
| **tree** `q[9]_q[10]_q` | 136.823… | **derived** | Bring genus-4 force-carrier uniqueness `{T_{2,9},T_{3,5}}` → `[9]_q[10]_q` |
| **zero-mode measure** `1/Area` per mode | `1/(12π)` | **derived (proved)** | heat-kernel: one constant mode `1/Vol` per harmonic generator (#1444 / `photon-ir-zero-mode-bring`); Gauss–Bonnet `Area = −2πχ = 4π(g−1)` |
| **zero-mode count** `b₁` | 8 | **derived (proved)** | Hodge: `dim ker Δ₁ = b₁ = 2g` |
| **graph grammar** (loop L ↦ bare Penrose `[L+1]_q`) | — | **derived** | reproduces the established 1-loop `[2]_q` exactly; θ-graph is the unique 1PI 2-loop topology, `θ(1,1,2)=[3]_q` (validated evaluator) |
| **loop resummation** `Σ(−1)^L[L+1]_q x^L = 1/((1+qx)(1+q⁻¹x))` | — | **derived** | standard q-integer generating function; factors into the two braiding channels `e₊`(q), `e₋`(q⁻¹) of `A⊗A` — the loop tower is the geometric series of the two singlet/adjoint idempotents |
| **per-loop measure** `1/(π b₁) = 1/(8π)` | 0.0398 | **⚠ NOT derived — the wall** | see below |
| **global dressing sign** (the `−` alternation) | — | **not derived** | consistent with one dressed-propagator convention; underived |

## The single load-bearing wall — and it is NOT the zero-mode measure

The per-loop measure `1/(8π)` was labeled "= `1/(π·dim H¹)`, parallel to the
zero-mode" (phase 4). **The consistency probe shows that parallel is unsound
— and isolates the real target.** The heat-kernel principle the zero-mode
*proof* uses gives per-mode measure `1/Area = 1/(12π)`. Propagating **that**
(proved) measure consistently through the same ladder:

| per-loop measure | 1-loop residual (proton) | 2-loop residual | status of the measure |
|---|---|---|---|
| `1/(π b₁) = 1/(8π)` | **+1.67 ppb** | **−0.20 ppb (1.3σ)** | **underived** (phase-4 identification) |
| `1/Area = 1/(12π)` | −1419 ppb | −1419 ppb | **proved** (heat-kernel) |

The proved measure `1/Area` fails at **1-loop already** (−1419 ppb, ~9500σ).
So:

1. **The two IR corrections use genuinely different geometric factors.** The
   zero-mode carries `b₁` in the *numerator* over the *Area*; the loops carry
   `b₁` in the *denominator* with a bare `π`. They are not one measure, and
   the working 1-loop term (`[2]_q/(8π)`, the +0.313 ppb form-B headline)
   *requires* the `1/(π b₁)` factor — `1/Area` is decisively excluded by data.
2. **The θ-graph 1.3σ hit is contingent on the underived `1/(8π)`, not on any
   proved measure.** It is a real, sharp, parameter-free *candidate* (the best
   in the corpus), but it does not inherit the zero-mode's proof.
3. **Closing α_EM to ≤ σ_α ⇒ deriving `1/(π b₁)` specifically.** The
   discriminant `1/Area` (−1419 ppb) vs `1/(π b₁)` (works) shows the loop
   measure is set by the **Betti number** `b₁` (a mode *count*), **not** the
   area — the RT-derivation target is now precise: *why is the photon 1-loop
   normalization the count of harmonic 1-forms `b₁`, not the surface area?*

## Where a genuine derivation would come from (scoped, not done)

The photon is the U(1) gauge field; its space of flat connections modulo
gauge is the **Jacobian torus** `J(M) = H¹(M;ℝ)/H¹(M;ℤ)`, of real dimension
`b₁ = 2g`. The 1-loop photon determinant on `M_Bring` is normalized by the
Jacobian data — a `b₁`-dimensional volume — which is why the loop measure is
governed by `b₁` (mode count) rather than `Area`. Turning "governed by `b₁`"
into the exact `1/(π b₁)` is the RT shadow-world 1-loop determinant
computation on the genus-4 Jacobian — the honest multi-week item. **This audit
does not do it; it isolates it** and removes the false comfort that the
zero-mode proof already covers it.

## Net answer to "what is derivable"

- **Derivable now (mostly done):** tree, zero-mode (count + `1/Area` measure),
  the graph grammar, the resummation. Four of the ~six ingredients.
- **The one wall:** the per-loop measure `1/(π b₁)` — a *different* object from
  the proved zero-mode measure, empirically fixed by the working 1-loop term,
  and the sole load-bearing input for the θ-graph candidate. Plus the global
  sign (a convention, lighter).

Isolating this changes the program's framing: it is no longer "derive the
2-loop coefficient" (the θ-graph *dictates* `[3]_q`) but "derive the **photon
1-loop determinant normalization** `1/(π b₁)` on the Bring Jacobian" — one
computation that certifies **every** loop order at once.

## Cross-references

- θ-graph candidate: [`2026-07-14-alpha-em-theta-graph-two-loop-candidate.md`](2026-07-14-alpha-em-theta-graph-two-loop-candidate.md)
- Schwinger tier check: [`2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md`](2026-07-14-alpha-em-phase3-schwinger-coefficient-exact-check.md)
- Proved zero-mode: `predicted-spectra/photon-ir-zero-mode-bring.md`, `QOU.Archimedean.PhotonIRZeroMode`
- Phase-4 identification (the imprecise "same measure" narrative): `alpha_em_rt_phase4_bring_measure.py`
