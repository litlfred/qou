# b_αα VolDensity scaling — the α–α bond does not carry the proton's ℏ_q² enhancement (scope-a)

**Date:** 2026-08-19 · **Arc:** bk-crossing-coordination, open item 3b (derive `b_αα ≈ 2.41 MeV`) · **PR:** #5346 (Lane 2)
**Probe:** [`computations/b_alpha_alpha_voldensity_scaling_probe.py`](../../computations/b_alpha_alpha_voldensity_scaling_probe.py)
**Witness:** [`computations/b-alpha-alpha-voldensity-scaling.witness.json`](../../computations/b-alpha-alpha-voldensity-scaling.witness.json) (allPassed)
**Follows:** the bare-`tr_M` NEGATIVE probe [`c_alpha_alpha_categorical_via_jones_markov.py`](../../computations/c_alpha_alpha_categorical_via_jones_markov.py) (m_e·|tr_M(7²_1)| undershoots 22.7×).
**Discipline:** scope-**(a)** (route tested alone, not structurally excluded); no fit (nothing tuned — `b_emp` is an external AME residual); no wiring; q₀ proton-anchored (no muon-cache straddle).

## Question

The bare Markov-trace route for the α–α coupling undershoots ~22.7×; the literature value
`m_e·Vol(7²_1) ≈ 2.43 MeV` uses `Vol` **directly**, with no `ℏ_q²` scaling — dimensionally
inconsistent with the proton mass `m_p = m_e·Vol(𝓑₃)·ρ/ℏ_q²`. The one untried substrate-pure
route (named by the prior probe and the arc audit) is to apply the **proton VolDensity
convention** `Vol/ℏ_q² × linking_weight` to the α–α interface link 7²_1.

## Result (at the proton-anchored q₀; nothing tuned)

| route | `b_αα` (MeV) | × empirical (2.416) |
|---|--:|--:|
| bare `tr_M`  `m_e·|tr_M(7²_1)|` | 0.107 | 0.044 (22.7× **small**) |
| literature  `m_e·Vol(7²_1)` | 2.427 | 1.005 (matches; **no ℏ_q²**) |
| full VolDensity H₄  `m_e·Vol/ℏ_q²·lw₄` | 626.1 | **259×** big |
| full VolDensity H₃  `m_e·Vol/ℏ_q²·lw₃` | 330.5 | 137× big |

**Result 1 — scope-(a) refutation of the full proton-VolDensity route.** Transplanting the proton
convention (with the `ℏ_q² ≈ 0.0098` Planck enhancement that lifts `Vol(𝓑₃)` to the GeV proton
mass) overshoots the α–α bond by **259×** (H₄ linking weight) / 137× (H₃). Neither the bare-trace
undershoot nor the full-VolDensity overshoot derives `b_αα`; the naive convention transplant fails
in both directions.

**Result 2 — the dimensional discrepancy is quantified exactly: `ρ_αα ≈ ℏ_q²`.** The α–α per-block
density the AME value implies,

$$\rho_{\alpha\alpha} \;:=\; \frac{b_{\rm emp}\,\hbar_q^2}{m_e\,\mathrm{Vol}(7^2_1)} \;=\; 0.9955\,\hbar_q^2,$$

i.e. `ℏ_q²` to 0.45%. So the literature `m_e·Vol(7²_1)` **is** the VolDensity form
`m_e·Vol·ρ/ℏ_q²` with a density `ρ_αα = ℏ_q²` that cancels the denominator, placing the α–α binding
at the bare hyperbolic-volume scale. The proton carries an O(1) density `ρ_p = linking_weight ≈
2.53` (ℏ_q²-independent); the two differ by exactly one `ℏ_q²` rung: `ρ_p/ρ_αα ≈ 259 ≈ ρ_p/ℏ_q²`.

## Open (numerology guard — magnitudes not interpreted)

> **CORRECTION (2026-08-21, [forward test](2026-08-21-binding-hbarq-rung-forward-test.md)).** The
> "binding residuals are ℏ_q²-suppressed" phrasing below over-generalised. `ρ_implied/ℏ_q² = M_need`
> is a *definitional* identity, so `ρ_αα ≈ ℏ_q²` is only the single-bond `M ≈ 1` case; multi-bond
> bindings have `M_need` = 2.0 (³H), 7.6 (⁴He), i.e. `ρ_binding = M·ℏ_q²`. What survives non-circular:
> the mass multiplier is O(1/ℏ_q²) (ρ_p O(1), classical) while binding is O(1) so `ρ_binding = M·ℏ_q²`
> is O(ℏ_q²) (quantum) — a scaling separation, not a magnitude coincidence. Result 1 (259×) is
> unaffected.

`ρ_αα ≈ ℏ_q²` **restates** the numerical match `b_αα = m_e·Vol` as a density identity; it is **not**
a derivation. Deriving `b_αα` requires a first-principles reason the α–α interface density is `ℏ_q²`
— that binding residuals sit two `ℏ_q`-powers below the rest-mass VolDensity. That is a scope-(a)
observation and a **forward, testable** hypothesis (other bond scales — the deuteron, per-isotope
`b_αα` for larger interface links — should show the same `ℏ_q²` suppression relative to their
VolDensity), but it is not established here. No production wiring; the α-cluster recursion's
`C_ALPHA_ALPHA` is unchanged.
