# The A≥3 per-rep θ_λ magnitude — derive-or-refute (R2-d)

**Date:** 2026-07-13 · **Branch:** `claude/mass-binding-errors-9zqpal` ·
**Type:** FORMALIZE-FIRST derive-or-refute of the cheat-sheet 🔴 open gate
("the per-rep highest-weight j=n/2 collapse of θ_λ saturates; needs the full
per-rep θ_λ magnitude"). **No fit, no tuning, no wiring.**
**Probe:** [`computations/deltalambda/theta_lambda_magnitude_kernel_probe.py`](../../computations/deltalambda/theta_lambda_magnitude_kernel_probe.py)
(witness `theta-lambda-magnitude-kernel-probe.witness.json`, 5/5 assertions).

## 1. Hypothesis class (stated precisely)

The binding carrier is `B = m_e · Σ_λ w_λ · 𝒜 · f(θ_λ)` with `f` linear at
leading order, `w_λ` a fixed Markov weighting (`y_λ` or `y_λ·dim_λ`, both
canonical conventions in the corpus), and **𝒜 the open magnitude** — either

- **sub-class (i), scalar-𝒜:** one derived dimensionless amplification
  (the "find the derived constant near 270" reading of the gate), or
- **sub-class (ii), kernel-𝒜:** a per-block `𝒜_λ` (a λ-structured kernel).

Known anchors (all corpus, zero fit): scalar-trace collapse
`B_D = m_e·Vol(𝓑₃)·Δtr` (+0.19 %, `Δtr_D = 0.59524`); highest-weight
collapse `B_D = μ₀·ℏ_q·J_q²(3)` (−9 %); bare per-λ mirror phase undershoots
the 0.7638 MeV ³H−³He split by a large factor (audit #3738 quotes ~270×).
The ±9 % gap between the two proved collapses is the **inter-scheme
truncation band** — the honest error budget any linear-order closure gets.

## 2. The invariants (found BEFORE numerics — compute-author §3.3)

**I1 — cross-observable rigidity.** A scalar 𝒜 must simultaneously equal
`B_AME(K)/(m_e·S_w(K))` for K ∈ {D, T, ³He, ⁴He} *and*
`split_AME/(m_e·ΔS_w(mirror))`, within the ±9 % band. This is finite
arithmetic on cached canonical witnesses
(`binding-reeb-phase-decomposition` θ_λ vectors +
`chi-*-h*-at-q0-50dps` y_λ) — the whole sub-class is decided at once,
without scanning constants.

**I2 — evaluation level (fibre vs observable).** The volume-conjecture /
Kashaev growth `e^{Vol·N/2π}` is the **|q| = 1 root-of-unity** asymptotic of
the colored Jones (fibre level). The binding observable is evaluated at
**real q₀** (archimedean level), where large-rep growth is the
`q₀^{±writhe}` growth channel — already present as the arccosh channel of
the Reeb decomposition. Per the AGENTS.md Im(q) two-level rule, a per-λ
kernel `𝒜_λ = e^{Vol·N_λ/2π}` at real q₀ has **no structural warrant**;
`Vol` enters the real-q₀ trace only through the full-contraction
semiclassics (which is exactly the proved +0.19 % route). Prediction
registered before the run: the per-color kernel over-amplifies.

**I3 — dimension.** θ_λ is dimensionless; any scale is
`m_e × (derived dimensionless 𝒜)`. This makes I1 a test on pure numbers.

## 3. Result 1 — the "~270×" target is ILL-POSED (convention-dependent)

Reproducing the bare mirror sum under the four coexisting conventions:

| mirror bare-sum convention | m_e·S (MeV) | amplification needed |
|---|--:|--:|
| `Σ y_λ·(θ_atom^T − θ_atom^He3)` | +0.00116 | **659×** |
| `Σ y_λ·(Δθ^T − Δθ^He3)` | +0.00396 | **193×** |
| `Σ y_λ·\|θ_atom^T − θ_atom^He3\|` | +0.00444 | **172×** |
| `Σ y_λ·dim_λ·(\|Δθ^T\| − \|Δθ^He3\|)` | +0.05896 | **13×** |

The quoted "~270×" is one member of a **13×–662× family**. "Enumerate
derived constants near 270 and pick the match" is therefore not a
well-posed derivation target; the well-posed targets are the
per-observable amplifications under a *fixed* weighting (next section).

## 4. Result 2 — INVARIANT I1 REFUTES the scalar-𝒜 sub-class (scope-(a))

Required 𝒜 = B/(m_e·Σ w_λ|Δθ_λ|), from cached canonical witnesses:

| observable | 𝒜_req (w = y_λ·dim_λ) | 𝒜_req (w = y_λ) |
|---|--:|--:|
| D | 6.043 | 51.3 |
| T | 18.99 | 829 |
| ³He | 19.91 | 860 |
| ⁴He | 63.05 | 21 983 |
| mirror (³H−³He) | 12.95 | 608 |
| **dispersion max/min** | **10.4×** | **429×** |
| band allowed (±9 %) | ≤ 1.18 | ≤ 1.18 |

**Verdict:** under *every* weighting the required amplification disperses
an order of magnitude (or two) across observables — **no single derived
constant can serve**, killing the entire scalar-𝒜 sub-class at once:
1/ℏ_q² ≈ 101.9, 1/ℏ_q³ ≈ 1028, e^{Vol(𝓑₃)}/2π ≈ 242, e^{Vol(8₁₁)}/2π ≈ 632,
[3]_q! ≈ 6.12, [5]_q! ≈ 131, F_Bor ≈ 4.469, μ₀/m_e ≈ 3.19, Vol powers,
q₀ powers — all of them, without testing each against AME.
**Scope-(a) phrasing:** the scalar-𝒜 linear carrier, *alone as the sole
mechanism*, does not reproduce the numbers as-is; this constrains
magnitudes/combinations, not ingredients (any of these constants may still
appear inside a λ- or A-structured closure).

### Candidate table (documentation; match = within ±9 % of a required 𝒜)

| candidate | value at q₀ | matches ~270×? | matches which observable? | structural tie to θ_λ? |
|---|--:|:-:|---|---|
| 1/ℏ_q | 10.093 | no | — | substrate q-Planck; no magnitude tie |
| 1/ℏ_q² | 101.86 | no | — | muon-anchor c_q² — guardrail: belongs to Vol(4₁), not binding |
| 1/ℏ_q³ | 1028.1 | no | — | none |
| [3]_q! | 6.121 | no | **D only** (+1.3 %) | per-nucleon H₃ Poincaré factor (F_Bor normaliser) — guarded datum |
| [5]_q! | 131.3 | no | — | none at H₉ |
| μ₀/m_e | 3.189 | no | — | per-crossing scale (derived) |
| F_Bor | 4.469 | no | — | mass chain, not binding |
| Vol(𝓑₃) | 7.328 | no | — | semiclassical contraction only |
| Vol(𝓑₃)/ℏ_q | 73.96 | no | — | composite, no single-object tie |
| e^{Vol(𝓑₃)}/2π | 242.2 | **−11 % of 273** | — | **none at real q₀** (I2: Kashaev at non-integer color) |
| e^{Vol(8₁₁)}/2π | 631.7 | no | mirror(y-only) — one member of the ill-posed family | same I2 objection |
| e^{Vol(𝓑₃)/2π} | 3.210 | no | — (but see §6) | per-color Kashaev rate — fibre level |

None matches all observables (probe assertion
`no_candidate_matches_all_observables = 0`). The two single-observable
matches are guarded data, not closures.

## 5. Result 3 — the Kashaev per-color kernel is REFUTED numerically (as I2 predicted)

One pre-named kernel, no alternatives tried (no shape-probing):
`𝒜_λ = exp(Vol(K_bind)·N_λ/2π)`, `N_λ = λ₁−λ₂+1` (the sl₂ color of the
two-row quotient — the color the volume conjecture actually quantifies).

| | B_pred (MeV) | B_AME (MeV) | rel |
|---|--:|--:|--:|
| D | 26.69 | 2.225 | **+1100 %** |
| T | 1011.7 | 8.482 | +11 828 % |
| ³He | 401.1 | 7.718 | +5097 % |
| ⁴He | 3.4×10⁸ | 28.296 | +10⁹ % |
| mirror | 610.7 | 0.7638 | +79 855 % |

Deuteron band ±9 % **violated** ⇒ kernel refuted, **scope-(a)** (this
kernel, alone, at this evaluation level). The structural reading stands:
the root-of-unity growth applied at real q₀ double-counts what the
arccosh growth channel already carries — the categorical Im(q) two-level
rule, vindicated numerically.

## 6. The well-scoped PARTIAL — 𝒜 is geometric in A (a derived constraint)

Read directly off the I1 table (no new inputs): the per-added-nucleon
amplification ratios under w = y·dim are

`𝒜(T)/𝒜(D) = 3.143 · 𝒜(³He)/𝒜(D) = 3.295 · 𝒜(⁴He)/𝒜(T) = 3.320 · 𝒜(⁴He)/𝒜(³He) = 3.167`

— mutually consistent to ~6 % (probe assertion
`geometric_in_A_pattern_ratio_scatter`). **The missing magnitude is not a
constant: it grows geometrically, ≈ ×3.2 per added nucleon** — an
exponential extensivity, the same direction as the jet-filtration
super-exponential mechanism (2026-07-03 audit). This is the genuine
derived output of this track: any future θ_λ closure must reproduce
𝒜(A) ≈ 6.0 · 3.2^{A−2} on {D, T, ³He, ⁴He}.

**Numerology guard (identification degenerate).** Four derived constants
sit inside the ±3 % ratio scatter: π = 3.1416, [3]_q = 3.0437,
μ₀/m_e = 3.1889, **e^{Vol(𝓑₃)/2π} = 3.2099** (the per-color Kashaev rate
re-entering at the per-*nucleon* — not per-color — level). Four data
points cannot discriminate; picking one would be post-hoc selection.
The composite guarded formula `𝒜(A) = [3]_q!·(e^{Vol(𝓑₃)/2π})^{A−2}`
reproduces all four **absolute** bindings to ≤ 3.5 % (D +1.3 %, T +3.4 %,
³He −1.3 %, ⁴He +0.02 %) but **fails the mirror difference (+52 %)** —
differences amplify the absolute residuals. Classification: **GUARDED
DATUM** (post-hoc shape at 4 points, degenerate identification, mirror
open); not derived, not wired, per the anti-fit discipline. It is
falsifiable parameter-free at A = 6: it predicts 𝒜(⁶Li) ≈ 650.

## 7. Honest classification

| item | verdict |
|---|---|
| scalar-𝒜 sub-class (any single derived constant, incl. every "~270" candidate) | **REFUTED, scope-(a)** — cross-observable dispersion 10.4× (y·dim) / 429× (y) vs the ±9 % band; constrains combinations, not ingredients |
| "the ~270× target" itself | **ill-posed** — convention-dependent (13×–662×) |
| Kashaev per-color kernel e^{Vol·N_λ/2π} at real q₀ | **REFUTED, scope-(a)** — +1100 % on the deuteron; I2 (fibre-vs-observable) predicted it |
| geometric-in-A constraint 𝒜(A) ≈ 6.0·3.2^{A−2} | **derived PARTIAL** — a rigidity constraint on any closure (no fit; read off cached data) |
| [3]_q! ≈ 𝒜(D) (+1.3 %), e^{Vol(𝓑₃)/2π} ≈ ratio, composite formula (≤3.5 % absolutes) | **guarded data** — structural tie unproven, identification degenerate, mirror does not close; NOT wired |
| the gate | **still open** — narrowed: the object is A-structured (geometric growth), not a scalar; and not the root-of-unity kernel at q₀ |

No AME/CODATA inversion was performed anywhere; all 𝒜_req values are
*reported requirements* (diagnostic quotients), never inputs to a wired
formula.

## 8. What would close it next

1. **Derive the ×3.2/nucleon ratio** from the categorical data — the
   discriminating test among the degenerate candidates is A = 6 (⁶Li,
   H₁₈ θ_λ vectors; predicted 𝒜 ≈ 650 under e^{Vol/2π}, ≈ 605 under π,
   ≈ 630 under μ₀/m_e — a 50-dps θ_λ extraction at H₁₈ separates them).
   Requires the ⁶Li chi/θ witnesses (long compute; tee-log discipline).
2. **Connect to the jet-filtration weight w_n(K)** (2026-07-03 audit,
   option 2): a per-nucleon geometric factor is exactly what a
   q-difference kernel `G(qx;q) = R(q,x)G(x;q)` produces; test whether a
   *derived* `R(q,x)` yields ratio ≈ 3.2 at q₀ — that would be a
   derivation, not a selection.
3. **Mirror residual is a separate object** — the composite formula's
   +52 % mirror failure confirms the redirect audit (#3738): the split
   rides the geometric/Milnor EM channel, not the strong-magnitude
   channel; closing 𝒜(A) does not close the mirror.
4. **Formalize the I1 rigidity as a small Lean lemma** (finite
   arithmetic over the witness data — the §3.4 formalize-the-refutation
   pattern) so the scalar-𝒜 class cannot be silently re-proposed.

## Provenance

Probe: `theta_lambda_magnitude_kernel_probe.py` (cached inputs:
`binding-reeb-phase-decomposition.witness.json`,
`chi-{deuteron,tritium,helium-3,helium-4}-h{6,9,12}-at-q0-50dps.witness.json`;
5/5 assertions). Corpus: `binding_a3plus_full_theta_assembly.py` (ρ_need
cross-checked: 𝒜(D)·m_e = 3.0875 MeV matches its `rho_need_computed`),
`binding_endomorphism_deuteron.py` (+0.19 %),
`binding_qhamiltonian_rotational_scale.py` (−9 %),
[`2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md`](2026-07-03-theta-lambda-via-reeb-nastokes-jet-filtration.md),
[`2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md`](2026-07-13-a3-split-borromean-redirect-and-deuteron-coupling.md),
[`../coordination/binding-scale-is-hyperbolic-volume.md`](../coordination/binding-scale-is-hyperbolic-volume.md)
(C_knot = 5.852 retraction — no anchor inversion repeated here).
EXPLORATORY — audit + witness only; no production wiring.
