# c₃ bar-odd S: the pole→cusp map in explicit coordinates — phase tractability

**Date:** 2026-07-11 · **Axis:** Q_β c₃ (bar-odd `S`) · **Tier:** structural + measurement (scope-(a)).
**No c_k wired; registry untouched; §8 flip-flop guard respected; m(q₀) NOT fitted.**
**Probe:** [`qbeta_c3_barodd_pole_cusp_phase_probe.py`](../../computations/qbeta/qbeta_c3_barodd_pole_cusp_phase_probe.py).
**Lean (this session):** [`QOU/QBeta/CuspShapeBarParity.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/CuspShapeBarParity.lean).

Lays the pole→cusp map (`conj:algebraic-geometric-dilog-equivalence`) out in **all
four coordinates**, ties each to the categorical-action complex volume
`𝔙 = E₀·tr_M((Π_free−1)∘𝓜)` (`binding-qbeta-complex-volume.lean`: `𝔈_bind = Re 𝔙`,
`𝔔_β = Im 𝔙`), and asks whether the phase `φ(q₀)` is tractable.

## The four explicit coordinates (each with a proved Lean anchor)

| # | coordinate | value at complete point | Lean anchor | 𝔙 role |
|---|---|---|---|---|
| 1 | **pole** `x = q^{-k}` | real, root of `(x;q)_n` | `qPochDenom_eq_zero_at_pole` / `denomPolyLocal_eq_zero_at_pole` (proved) | seeds `tr_M` |
| 2 | **cusp shape** `ω = e^{iπ/3}` | root of `Φ₆(z)=z²−z+1` (ℚ(√−3)) | `CuspShapeBarParity` (proved, this session) | Re/Im split |
| 3 | **deformation** `u = 2 log m` | `0` (complete) | — (open: `q₀↦u`) | `S = Im[−(τ/4)u²]` |
| 4 | **ED** `z_ED = √q − 1/√q` | `barOdd(√q)` | `barOdd` (`BarParityZeta4Swap`) | approach to `𝒮_p` |

**The key proved tie (coord 2 = the `𝔙` split at the complete point).** For the
cusp shape `ω = e^{iπ/3}`, `CuspShapeBarParity` proves — over a generic field, no
archimedean structure:

- `barEven ω = ω + ω⁻¹ = 1` — the **`Re 𝔙 = Vol`** coordinate (rational, amphichiral,
  anchor-stable; the solved `−Vol(4₁)`).
- `(barOdd ω)² = (ω − ω⁻¹)² = −3` — the **`Im 𝔙 = CS`** coordinate; `barOdd ω = √−3`
  is the **Neumann–Zagier cusp modulus `τ`** that drives `CVol(u)=Vol−(τ/4)u²+…`.
- `ω³ = −1`, `ω⁶ = 1` — primitive sixth root of unity (the RoU the bar-odd phase
  accumulates in).

So the two faces of `𝔙` are exactly the two bar-parity coordinates of the ONE cusp
shape, proved (cross-checked numerically to `10⁻⁴¹`).

## Target (measured, anchor-blind witness)

`S = c₃ + Vol(4₁)`: `S(muon) = +0.00968298`, `S(proton) = −0.03945936` (sign flip).

## Findings

**A. Base phase and cusp modulus are EXACT** (coord 2, Lean-proved): the `π/3`
shape argument and the `√−3` modulus are not fitted — they are the cyclotomic
`Φ₆` / trace-field data.

**B. The magnitude scale is PARAMETER-FREE and ~4% at leading NZ.** With
`(√3/2)|u|²` (√3 = cusp shape) and the natural bar-odd coordinates:

| `\|u\|` | `(√3/2)\|u\|²` | vs `\|S\|` | rel |
|---|---|---|---|
| `z_ED = barOdd(√q₀) = 0.10439` | `0.0094370` | `\|S(muon)\| = 0.0096830` | **−2.54%** |
| `HA = barOdd(q₀) = 0.20906` | `0.0378507` | `\|S(proton)\| = 0.0394594` | **−4.08%** |

with `HA / z_ED = barEven(√q₀) = 2.0027` (the bar-EVEN partner) and
`(HA/z_ED)² = 4.011 ≈ |S(proton)/S(muon)| = 4.08`.

**C. No single smooth `|u|` serves both anchors.** Required `sin(2φ) = S/[(√3/2)|u|²]`
exceeds 1 by ~4% at one anchor (`z_ED`: 1.026 muon; `HA`: −1.043 proton) — the
leading-NZ shortfall + the smooth-|u| wall (ratio 1 vs −4.08, bean `qou-yucw`).

**D. The sign flip is a well-posed geometric condition.** `S(muon) > 0 > S(proton)`
⇒ (IVT, assuming continuity) a substrate `q*` with `S = 0` ⇔ `u` real ⇔ **real
meridian holonomy** (real Dehn filling). That `q*` is tractable to state/solve.

**E. Near-singular phase function.** The gluing-Newton `Vol` is extremal at the
complete point (`dVol/du = 0` for real `u`, confirmed), so the observable
sensitivity lives entirely in the imaginary (CS) direction; the `dc₃/dq ≈ 4.66×10⁶`
wall (PR #1821) makes `φ(q₀)` the near-singular `Φ_q`-pole-seeded Newton, not a
smooth closed form.

## Verdict

- **Tractable / exact:** the base phase `π/3` and cusp modulus `√−3` (Lean-proved),
  and the parameter-free magnitude scale `(√3/2)|u|²` (~4% leading NZ).
- **Open (near-singular):** the **phase function** `φ(q₀) = arg u(q₀)` — the open
  pole→cusp Newton (`conj:algebraic-geometric-dilog-equivalence`). Smooth `u(q₀)` is
  excluded (bean `qou-yucw`); the phase carries the sign-flip.
- **Concrete next step (well-posed, not a fit):** seed the figure-8 gluing Newton
  with the actual substrate pole `q₀^{-k}` and read the emergent complex shape's
  phase. This probe sets that up and quantifies its sensitivity.

## Follow-up (pole-seed Newton) — the phase is a BRANCH SELECTOR

**Probe:** [`qbeta_c3_barodd_pole_seed_newton_probe.py`](../../computations/qbeta/qbeta_c3_barodd_pole_seed_newton_probe.py).
**Lean:** the golden-branch contrast added to `CuspShapeBarParity.lean`
(`goldenShape_barOdd = 1`, `goldenShape_barEven_sq = 5`).

Seeding Thurston's figure-8 gluing Newton with the **actual** real substrate pole
`q₀^{-k}` gives a decisive, tightly-structured answer:

1. **The complete gluing `(z(z−1))² = 1` has exactly two branches** `z(z−1) = ±1`:
   - `z²−z+1 = 0` → **cusp** `e^{iπ/3}` (complex; hyperbolic; disc `−3`; `barOdd² = −3` = √−3 = CS);
   - `z²−z−1 = 0` → **golden ratio** `φ = (1+√5)/2` (real; **degenerate**, Vol = 0; disc `+5`; `barEven² = +5` = √5, no CS).
2. **The literal real pole `q₀^{-1} = 0.90092` seeds the Newton onto the golden branch**
   (`z = 1.6180339887 = φ`, real, Vol = 0) — **never the hyperbolic cusp.** A real pole
   cannot reach the cusp.
3. **The bar-parity roles swap between the branches**, and the swap is exactly the
   discriminant sign flip `−3 ↦ +5` (both proved in `CuspShapeBarParity`): the special
   coordinate is **imaginary** (`√−3` = CS) on the cusp and **real** (`√5`) on the golden
   branch. So CS = bar-odd `S` turns on **only off the real (golden) axis** — i.e. only
   under complexification.

**Consequence.** The phase `φ(q₀)` is precisely the **branch selector**: it complexifies
the real pole seed to move the special coordinate from the real `√5` (golden, no CS) to
the imaginary `√−3` (cusp, CS). No real datum can supply it — that *is* the open
`conj:algebraic-geometric-dilog-equivalence`.

**Additional (independent confirmation of the landed geometry-side negative).** The full
Rogers-dilog complex-volume CS at the substrate meridian scale (`|u| ~ HA`, any phase) is
`~1.7×10⁻⁵` — **~2350× below** the measured `|S| ~ 0.01–0.04`. So the leading-NZ
`(√3/2)|u|²` magnitude "match" (~4%) is a leading-order artifact; the *actual* figure-8
complex-volume deformation is orders too small. **`S` is not the leading CS deformation of
`4₁` alone** — reproducing, via an independent computation, the parallel-landed
geometry-side clean negative (`main 1a4894b8`, "magnitude-only"; `827b43e4` Kashaev
grounding, `CS(4₁)=0`).

## Cross-references
- NZ gap: [`2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md`](2026-07-11-qbeta-c3-barodd-nz-deformation-gap.md).
- Target: [`2026-07-11-qbeta-c3-barodd-sleak-phib-target.md`](2026-07-11-qbeta-c3-barodd-sleak-phib-target.md).
- `𝔙` definition: [`binding-qbeta-complex-volume.lean`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean).
- AGENTS.md §"Before declaring refuted (a)/(b)"; §"Im(q) at fibre vs observable level".
