# The ³H/³He mirror split as pp-Coulomb, on the Lean strong-split-zero premise: parameter-free radius lands it — but it is a PARTIAL, and the magnitude wall is untouched

**Date:** 2026-07-18 · **Branch:** `claude/deltalambda-coulomb-mirror-2026-07-18` ·
**Type:** FINDING (reproducible, no fit, nothing wired). Δ_λ magnitude front,
scope-(a) PARTIAL. Attacks the refined "the mirror split is Coulomb, not strong"
hypothesis named by the merged-in-flight Lean invariant (PR #3986) and the
2026-07-18 attack-vector map.

Probe: [`computations/deltalambda/deltalambda_coulomb_mirror_split_probe.py`](../../computations/deltalambda/deltalambda_coulomb_mirror_split_probe.py)
(witness [`deltalambda-coulomb-mirror-split.witness.json`](../../computations/deltalambda/deltalambda-coulomb-mirror-split.witness.json),
7/7 assertions pass, mpmath at the production floor, exit 0).

## 0. The hypothesis and the proved premise

The magnitude front's three convergent probes bracket the ³H/³He mirror binding
ratio (unsigned graph 1.00× #3952, signed triangle-flux det 2.42× #3953, AME
target 1.10×). The refined hypothesis: **the mirror split is NOT strong — it is
the Coulomb repulsion of ³He's two protons.**

That the strong sector gives ³H = ³He *exactly* is now **machine-verified**:

> `QOU.MassTheory.isospinExchange_det_mirror_invariant` — the global proton↔neutron
> mirror `s ↦ −s` fixes every entry of the isospin-signed strong exchange matrix
> (`(−sᵢ)(−sⱼ) = sᵢsⱼ`), so its determinant — and any strong binding functional of
> it — is mirror-invariant. The strong ³H/³He split is **exactly 0**.
> Scope-(b) structural exclusion. Sorry-free, `lean`-direct exit 0. PR #3986
> (open, not yet on `main` at time of writing).

On this proved premise, `B(³H) − B(³He) = E_C(³He)` (³H has Z=1 ⇒ no proton pair ⇒
E_C = 0). So the **entire** mirror split is EM: a clean, decisive forward test of a
parameter-free Coulomb term.

## 1. The parameter-free Coulomb construction (every input traced)

`E_C = coef · α_EM · Z(Z−1) · ℏc / R`, with:

| factor | value / form | source | tier |
|---|---|---|---|
| **α_EM** | `1/(q₀·[9]_q·[10]_q) = 1/136.823` (bare, −0.155% vs CODATA) | `prop:alpha-em-categorical-trace-ratio` | **DERIVED** (bare) |
| **Z(Z−1)** | exact discrete-proton pair count (self-energy of Z unit protons) | combinatorial | **EXACT** |
| **R(A)** | `λ̄_π·A^{1/3}`, `λ̄_π = ℏc/m_π = 1.41382 fm` ⇒ `ℏc/R = m_π/A^{1/3}` — **no empirical r₀** | `m_π` = CAL-3; radius law from the volume-extensivity / Yukawa-range argument | **PARAMETER-FREE MODULO SELECTION** |
| **coef** | `3/5` (uniform charged sphere) OR `1/2` (single discrete pp pair) | classical Euclidean electrostatics | **MODEL ASSUMPTION** (both reported) |

The radius is the crux, and it is **not** the empirical `r₀ = 1.2 fm` of the
existing [`computations/coulomb_energy.py`](../../computations/coulomb_energy.py).
It is the framework's own **pion Compton wavelength** `λ̄_π = ℏc/m_π`, whose
provenance is the hyperbolic-volume machinery:

- **Scale class** (why m_π): the inter-nucleon bond is the `Vol(Hopf) = 0` 2-body
  channel, and CAL-3 is corpus-defined as *exactly* the Vol=0 meson scale — so
  the W-plane (m_e, m_μ, m_p) contributions vanish identically on the bond channel
  and the length unit is `ℏc/m_π` (pion-radius audit
  [`2026-07-13-pion-radius-and-vol-to-radius-gaps.md`](2026-07-13-pion-radius-and-vol-to-radius-gaps.md) GAP 1).
- **A^{1/3}** from volume extensivity: the categorical `Vol ∝ A`, so a fixed
  volume per nucleon gives `R ∝ Vol^{1/3} ∝ A^{1/3}` (same audit, GAP 2).

**Two named underived caveats** (both from that audit — this is the anti-laundering
triple-check the task demands):

1. The radius coefficient is set to **exactly 1** — a **Yukawa SELECTION** among the
   four framework mass scales, *not* a derivation. GAP 1 measures it at
   0.985 ± 0.069 (consistent with 1, but undiscriminable at the 7% binding
   systematics scatter). The length-scale selection table (probe output) shows m_π
   is the closest to 1 (0.900 for the A=3 pair alone), the mass extremes m_e (246×)
   and m_p (0.13×) are excluded by orders of magnitude, and m_μ (1.19×) is the
   nearest rival — a **soft** 2-bit selection.
2. The `A^{1/3}` volume→radius extensivity step is **GAP 2 OPEN** (the
   hyperbolic-complement volume is a topological invariant, not a Euclidean spatial
   volume; the ⁴He `Vol₄` single-reading is negative).

## 2. Forward-test outcome (no fit; α_EM and R fixed before comparison)

### 2a. The split — the AME value BRACKETS between the two geometries

| geometry | coef | E_C(³He) | pred/AME (0.764) |
|---|---|---:|---:|
| uniform charged sphere | 3/5 | **0.8487 MeV** | **1.111×** |
| single discrete pp pair | 1/2 | **0.7073 MeV** | **0.926×** |
| AME split | — | 0.7638 MeV | 1.000× |

`pairwise 0.707 < AME 0.764 < uniform-sphere 0.849` — the two classical geometries
bracket the data, and **both land near ~0.76 MeV** with a parameter-free radius.
The pp-Coulomb is the right sign, order, and (to a geometry factor) magnitude.

### 2b. The mirror RATIO `B(³H)/B(³He)` — reproduced from Coulomb alone

AME 1.099; pred (3/5) 1.111 (+1.1%); pred (1/2) 1.091 (−0.7%). The target **~1.10×
mirror ratio is reproduced from Coulomb alone** (strong part = 0 by PR #3986).

### 2c. The absolute magnitude ratios ρ = B/B_D — UNTOUCHED (the real wall)

`ρ_4 = 12.72`, `ρ_3He = 3.47`, `ρ_3H = 3.81` are **isospin-even STRONG** quantities.
The Coulomb term shifts them only by `E_C/B ≤ 0.11` (³He 0.110, ⁴He 0.027) and
**cannot supply them**. These ratios *are* the open Δ_λ magnitude wall — this probe
leaves them exactly where they were. This is the clean boundary the "simultaneous"
forward test exposes: the isospin-**odd** split is Coulomb (lands); the isospin-
**even** magnitudes are strong (open).

### 2d. The direct `R ∝ Vol(K)^{1/3}` route is blocked for a mirror pair

The corpus link IDs make ³H = 8₁₁ (a **knot**, 1 cusp) and ³He = L6a4 = Borromean
(a **link**, 3 cusps) — *different* hyperbolic volumes for an isospin mirror, which
would give the two mirrors different radii, contradicting isospin symmetry. So a
direct `Vol^{1/3}` radius is **not** the mirror-symmetric object; the `A^{1/3}`
extensivity form (same A=3 ⇒ same R) is. (pion-radius audit GAP 2: cusp-count ∝ A
fails on the corpus's own links.)

## 3. Relation to prior work (corpus-grep, run before any claim)

- **`mirror_split_continuum_em_probe.py` (2026-07-13)** already ran *exactly* this
  construction across 8 T_z mirror pairs A=3–39: `split_AME/split_pred = 0.985 ±
  0.069`, verdict **(ii) PARTIAL** (radius coefficient=1 selection + volume→radius
  step underived). This probe **reconfirms** it via its exact code path (the A=3
  pred 0.8487 matches to 10⁻⁹) — it does **not** claim a new crack. What is *new*
  here: (i) the **Lean scope-(b) premise** (strong split = 0 exactly, PR #3986),
  which the 2026-07-13 probe *assumed*; (ii) the **two-geometry bracketing**
  (3/5 vs 1/2) making the AME value sit between the models; (iii) the explicit
  **magnitude-wall-untouched** statement separating the isospin-odd/even parts.
- **`charge_coulomb_tn3he_derived.py`** (2026-06-03): the *categorical* Coulomb
  ratio `tanh(ln q₀)·B_pp = 0.238 MeV` covers only 31% (3.2× short). That is the
  q₀-only route; the present route is the continuum/geometric one, which lands the
  magnitude but at the cost of the radius-coefficient selection.
- **`charge_symmetric_coulomb_binding.py`** (2026-07-11): got the split to 0.998
  (1.3×) using the **empirical** `r₀ = 1.2 fm`. Swapping in the parameter-free
  `λ̄_π = 1.414 fm` (larger radius ⇒ smaller E_C) improves the 3/5 split from
  1.31× to **1.11×** *and* removes the one empirical input.

## 4. Verdict (anti-fit / anti-laundering, STRICT)

**(a) PARTIAL — not a wall-crack; the magnitude wall is untouched.**

> The ³H/³He mirror split is **proved pure-EM** (PR #3986, scope-(b)). A
> parameter-free-modulo-selection Coulomb term lands E_C(³He) at 0.71–0.85 MeV,
> bracketing the AME split 0.764 MeV between the pairwise (0.93×) and uniform-sphere
> (1.11×) geometries, and reproduces the ~1.10× mirror ratio from Coulomb alone.
> It is a **PARTIAL, not a crack**, because two inputs remain underived selections:
> the radius coefficient = 1 (a soft 2-bit Yukawa selection, GAP 1, undiscriminable
> at the 7% scatter) and the 3/5-vs-1/2 geometry model factor. It **matches** the
> known 2026-07-13 continuum-EM PARTIAL, adding the Lean premise + geometry
> bracketing, not a new result. The **absolute magnitude ratios ρ = B/B_D** — the
> real Δ_λ magnitude wall — are isospin-even STRONG quantities the Coulomb term
> cannot supply (E_C/B ≤ 11%); they stay **OPEN**.

Anti-laundering triple-check (task requirement): α_EM (derived) and R (pion-Compton,
CAL-3) are fixed *before* comparison; the Coulomb scale is never solved from the
deficit. The single open number (radius coefficient) is set to 1 by the Yukawa
selection, not fitted. Because that selection and the geometry factor are underived,
the classification is (a) PARTIAL *regardless* of how close the number lands.
**Not derived ⇒ not wired:** no production change, no tier change, no content-block
edit; nothing is canonical.

## 5. What would close it (for the next agent)

1. **Derive the radius coefficient = 1** (not select it): a quantization statement
   ("one CAL-3 quantum per bond") from the Hopf-channel Hecke structure — the
   multiplicity-one Frobenius reciprocity `⟨Res V_(2,1), V_(2)⟩ = 1` of
   `frobenius-lepton-meson-bridge` is the named candidate (pion-radius audit GAP 1
   next-step 2). This upgrades the split from PARTIAL to derived.
2. **Derive the geometry factor** — whether the correct object is the uniform-sphere
   3/5 or the discrete-pair 1/2 (or a categorical interpolant) — from the brane
   charge distribution, rather than importing a classical electrostatic model.
3. The magnitude wall (ρ) is untouched by any Coulomb work — it needs the strong
   Δ_λ magnitude closure (Vectors 1/2 of the 2026-07-18 attack-vector map: the K₄
   coordination-graph collective term, the icosahedral `1/√5` S-matrix bridge).

## Files

- probe: [`computations/deltalambda/deltalambda_coulomb_mirror_split_probe.py`](../../computations/deltalambda/deltalambda_coulomb_mirror_split_probe.py) (new)
- witness: [`computations/deltalambda/deltalambda-coulomb-mirror-split.witness.json`](../../computations/deltalambda/deltalambda-coulomb-mirror-split.witness.json) (new, audit-only, 7/7 pass)
- this audit: `docs/audits/2026-07-18-deltalambda-coulomb-mirror-split.md`
- Lean premise: [`content/quantum-observable-universe/lean/QOU/MassTheory/IsospinMirrorInvariance.lean`](https://github.com/litlfred/qou/blob/claude/isospin-mirror-invariance-lean-2026-07-18/content/quantum-observable-universe/lean/QOU/MassTheory/IsospinMirrorInvariance.lean) (PR #3986, sorry-free)
- context consumed (unchanged): `2026-07-18-deltalambda-attack-vector-map.md`,
  `2026-07-13-pion-radius-and-vol-to-radius-gaps.md`,
  `2026-07-13-mirror-split-one-third-mechanism-probe.md`,
  `2026-06-03-charge-coulomb-tn3he-derived.md`,
  `2026-07-11-charge-symmetric-coulomb-binding-benchmark.md`,
  [`computations/deltalambda/mirror_split_continuum_em_probe.py`](../../computations/deltalambda/mirror_split_continuum_em_probe.py),
  [`computations/coulomb_energy.py`](../../computations/coulomb_energy.py)
