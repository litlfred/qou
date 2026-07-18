# α_EM per-loop measure: adjudicating the bare `1/π` — the three candidate origins, their π-powers, and the decision

**Date:** 2026-07-18 · **Axis:** α_EM per-loop measure `1/(π·b₁)=1/(8π)` · **Tier:**
adjudication (scope-(a) on value, (b)-structural on the π-power; **no fit; no `α_k`
wired; `1/(8π)` stays a phase-4 identification**) · **Branch:**
`claude/alpha-em-perloop-pi-origin-2026-07-18` · **Probe:**
[`alpha_em_pi_origin_adjudication_probe.py`](../../computations/alpha_em/alpha_em_pi_origin_adjudication_probe.py)
· **Witness:**
[`alpha-em-pi-origin-adjudication.witness.json`](../../computations/alpha_em/alpha-em-pi-origin-adjudication.witness.json).

## The single remaining open factor

The photon per-loop measure is `1/(π·b₁) = 1/(8π)`, `b₁ = dim H¹(M_Bring) = 2g = 8`
(genus-4 Bring, `Jac(Bring) ~ E⁴`). Two factors, two homes:

- **`1/b₁` — SETTLED.** The area-free Betti count `ζ_{Δ₁}(0) = −b₁` (#3834), the
  3500σ forcedness of the integer `8` (#3831), merged as the derived count (#3895).
- **`1/π` — the ONLY open factor.** Its π-power is required to be **exactly −1** (a
  **bare** `1/π`): the sharpened three-axis constraint from #3870/#3882/#3889 rules
  out `1/(2π)` (power −1 but with a spurious `2`) and `π²` (power −2).

Three candidate archimedean origins were floated across the sweep but never
adjudicated on the π-power axis to a single answer. This is that adjudication — a
well-posed decision, not a wide search.

## Method — compute the exact π-power each candidate's 1-loop determinant produces

For each candidate the probe computes the **exact π-power** of the correct
1-loop-**determinant** normalization at the physical `d = 2` (the photon loop lives
strictly on the 2-surface — the zero-mode doc's dimensional-reduction argument rules
out `M_g × S¹`), and compares to the required `−1`. The value is never solved from
CODATA; no `π` is inserted by hand to reach `8π`.

**Controls (all pass, exit 0).** The derived zero-mode `1/(12π) = b₁/Area`
(Gauss–Bonnet `Area = 4π(g−1) = 12π`); `ζ_{Δ₁}(0) = −b₁` via the rank-independent
Epstein `ζ_Λ(0) = −1`; the `ζ'_{S¹}(0)` machinery `det'(−d²/dx²)_{S¹_L} = L²`
(`ζ_{S¹}(0)=−1`, `ζ'_{S¹}(0)=−2 ln L`, verified at `L=1,2,3.5`).

## The three candidates and their π-powers

| # | candidate | 1-loop-determinant normalization | **π-power** | `−1`? | derived? |
|---|-----------|----------------------------------|-------------|-------|----------|
| **(2)** | (2π)-Gaussian per-mode | `(2π)^{½ζ_{Δ₁}(0)} = (2π)^{−b₁/2}` (+ spurious `2^{−b₁/2}`) | **`−b₁/2 = −4`** | ✗ | ✓ (standard) |
| **(1)** | open-dilog (Rogers / Bloch–Wigner) | Rogers `L(z) = rational·π²`; Bloch–Wigner `D(z) = O(1)` | **`+2` / `0`** | ✗ | ✗ |
| **(3)** | 4π heat-kernel (proper-time determinant) | `(4πs)^{−d/2}\|_{d=2} = 1/(4π)` | **`−d/2 = −1`** | ✓ | ✓ (heat kernel is a theorem) |

Details:

- **Candidate (2) — π-power `−4`, EXCLUDED.** The flat-torus Maxwell / Gaussian
  per-mode measure has each harmonic mode contribute one `(2π)^{½}`, so the whole
  oscillator measure regularizes to `(2π)^{½ζ_{Δ₁}(0)} = (2π)^{−b₁/2}`: π enters to
  power `−b₁/2 = −4`, **linear in `b₁`**, with a spurious `2^{−b₁/2}` (the measure is
  `2π`, not `π`). Not `−1`. This is the merged #3870 result, reproduced here as a
  control.

- **Candidate (1) — π-power `+2` (Rogers) or `0` (D), and the only `−1` route is
  conjectural.** The Rogers dilogarithm values on the golden points are clean
  rational multiples of **`π²`** (`L(1)=π²/6`, `L((√5−1)/2)=π²/10`,
  `L((3−√5)/2)=π²/15` — verified to `1e−25`); the Bloch–Wigner `D(e^{iπ/3})=Cl₂(π/3)≈1.0149`
  is an `O(1)` real (π-power `0`). Neither is `−1`. A bare `1/π` would require the
  **conjectural** higher-Bloch-group regulator / Beilinson period
  (`conj:dilogarithm-archimedean-limit`, `conj:alg-geom-dilog-equiv`), so candidate
  (1) supplies **no derived `−1`**. (This confirms the merged `alphaem-dilog-bloch-probe`
  reading: single-π is the *gauge* signature; `π²`/`O(1)` is the *dilog* signature.)

- **Candidate (3) — π-power `−1`, DERIVED.** The 1-loop **determinant** is the
  ζ-regularized proper-time object `log det Δ = −∫(ds/s) Tr e^{−sΔ}`, whose small-`s`
  heat kernel is `Tr e^{−sΔ} ~ (4πs)^{−d/2}[a₀+a₁s+…]`. The per-loop proper-time
  Gaussian normalization is the prefactor `(4π)^{−d/2}`; at `d=2` this is `(4π)^{−1}
  = 1/(4π)` — a **single bare `π`, power `−1`**. This is standard heat-kernel theory,
  not conjectural. **Contrast** the momentum-space loop convention `∫d^d k/(2π)^d =
  (2π)^{−d}`, π-power `−d = −2` at `d=2` (the `4π²` "π²" reading): that is the
  loop-**integral** bookkeeping, **not** the determinant — the determinant definition
  **selects** the heat-kernel `(4πs)^{−d/2}` route, hence `−1`, not `−2`. This
  *tests and confirms* (rather than assumes) the #3889 audit's "`1/π` is the
  archimedean 1-loop det" claim, and *sharpens* it: the correct power is `−1` from the
  heat-kernel Gaussian, not `−2` from the momentum `4π²`.

## Decision (pre-stated rule)

> CANONICAL = the unique candidate giving π-power exactly `−1` from a **derived**
> 1-loop normalization.

Exactly **one** candidate — **(3), the 4π heat-kernel** — yields a derived π-power
`−1`. Candidate (2) gives `−4` (derived but wrong power); candidate (1) gives `+2`/`0`
(its `−1` route is conjectural). Therefore:

**The `1/π` ORIGIN closes to the archimedean 2D heat-kernel `(4πs)^{−d/2}` at `d=2`
(`= 1/(4π)`)** — the universal one-loop proper-time determinant normalization. The
π-power axis of `1/(8π)` is **settled at `−1`, archimedean-heat-kernel origin**;
candidates (1) and (2) are excluded on the π-power.

## Is the per-loop `π` the same as the zero-mode Gauss–Bonnet `π`?

**Same mechanism, distinct value.** Both descend from the one heat-kernel
`(4πs)^{−d/2}` (both π-power `−1`), but:

- **Zero-mode** (`1/(12π) = b₁/Area`, proved, #2114): the heat-kernel `4π` combines
  with the Gauss–Bonnet `∫R dA = 4πχ` in the `a₁` Seeley coefficient
  (`ζ_Δ(0)=χ/6`), where the `4π`s **cancel**, leaving the geometric **Area π =
  12π** (`−2πχ = 4π(g−1)`). The zero-mode's π is **geometrically dressed**.
- **Per-loop**: the heat-kernel `4π` stays a **bare** loop normalization `1/(4π)` —
  **undressed** (no `∫R` cancellation).

They differ in value by the topological factor `Area/(π·b₁) = 12π/8π = 2(g−1)/g =
3/2` (the merged pi-decomposition #3882's separation, reproduced exactly here). So
the answer to "same Gauss–Bonnet π or distinct heat-kernel π?" is: **the same
heat-kernel origin, but a distinct π-value — the per-loop π is the bare `4π`, NOT the
zero-mode's dressed Area `12π`.**

## Honest residual (non-π) — the full `1/(8π)` is NOT thereby derived

The π-power closing does **not** derive the whole measure. The derived heat-kernel
bare form is `1/(4π)` (one loop, one mode). Reaching `1/(π·b₁) = 1/(8π)` requires the
**reciprocal-in-`b₁` democratic average** — the rational coefficient `4 ↔ b₁`, or
equivalently the `8π = 2·(4π)` multiplicity `2`. That is a **count/coefficient**
question, **not** a π-power ambiguity, and it remains the ledger's separately-tracked
**"multiplicity `2` vs `b₁` / why reciprocal"** wall. The forcedness result (3500σ,
`8 = b₁`, not `2·4`) and the `ζ_{Δ₁}(0)=−b₁` count both point the coefficient toward
`b₁`, but deriving the exact reciprocal normalization from the bare `1/(4π)` is the
open item.

**Net:** the π-power axis of `1/(8π)` **CLOSES** (`−1`, archimedean heat-kernel,
candidate 3); the coefficient/count axis **stays open** (separately tracked). The
`1/π` **origin question** — "which of the three archimedean π's, at power `−1`" — is
answered: the heat-kernel, not the dilog, not the (2π)-Gaussian.

## Scope discipline (anti-laundering)

No CODATA read; no convention tuned toward `8π`; the `−1` is **forced** by the
1-loop-determinant definition (heat-kernel proper-time), not chosen to make `1/(8π)`
work. Candidate (1)'s conjectural status is recorded faithfully (it is *not* counted
as a derived `−1`). The residual coefficient wall is stated as open, not papered
over. No `α_k` wired; no fit; no tier change; `1/(8π)` stays a phase-4
identification.

## Cross-references

- π-decomposition (leaned (U), left the fine question open — this note sharpens it to `−1` via the three-way π-power adjudication): [`2026-07-18-alpha-em-pi-decomposition.md`](2026-07-18-alpha-em-pi-decomposition.md)
- Three-reading reconciliation (R1 status / R2 loop / R3 dilog): [`2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md`](2026-07-18-alpha-em-pi-origin-three-reading-reconciliation.md)
- Candidate (2) flat-torus Maxwell (`(2π)^{−b₁/2}`): [`2026-07-18-alpha-em-flat-torus-maxwell-perloop.md`](2026-07-18-alpha-em-flat-torus-maxwell-perloop.md)
- Candidate (3) heat-kernel `4π²` claim (tested, sharpened to `−1` here): [`2026-07-18-alpha-em-smatrix-perloop-quantum-dimension.md`](2026-07-18-alpha-em-smatrix-perloop-quantum-dimension.md), [`2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md`](2026-07-17-alpha-em-bring-jacobian-zeta-determinant.md)
- Candidate (1) dilog signature (`π²`, single-π = gauge): [`2026-07-17-alphaem-dilog-pi-pentagon-unification.md`](2026-07-17-alphaem-dilog-pi-pentagon-unification.md)
- Derived zero-mode calibration `1/(12π)`: [`../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean`](../../content/quantum-observable-universe/lean/QOU/Archimedean/PhotonIRZeroMode.lean), [`../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md`](../../content/quantum-observable-universe/predicted-spectra/photon-ir-zero-mode-bring.md)
- Derivability map / the wall: [`2026-07-14-alpha-em-2loop-derivability-map.md`](2026-07-14-alpha-em-2loop-derivability-map.md)
- Ledger: [`../coordination/alpha-em.md`](../coordination/alpha-em.md)
