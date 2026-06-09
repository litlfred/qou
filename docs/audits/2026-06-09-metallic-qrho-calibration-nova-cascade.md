# Metallic ladder: S(4) exact result, q↔ρ calibration, φ² literature, collapse cascade

**Date:** 2026-06-09
**Branch:** `claude/wizardly-fermat-amvizc` ([PR #2081](https://github.com/litlfred/qou/pull/2081))
**Follows:** the merged metallic thread #1999 → #2047 → #2049 → #2071 → #2074 → #2076 and the owner's four-option reply (S(4) pickup · q↔ρ calibration · φ² literature check · nova-cascade question).

## 1. S(4) — exact-Gram result (stalled §7.4 thread closed)

The §7.4 infra wall (pyhecke is H₃-only) was bypassed by building
`pyhecke_native` from source in-sandbox (per #2057's recipe, ~40 s) and
assembling the exact word-basis objects from native Hoefsmit characters:
costs `t_i = tr_M(b_i)`, Gram `G_ij = tr_M(b_i·b_j)` (concatenation — no
rank-1 approximation), canonical T_w bases (6 words at n=3, 24 at n=4).
Script: [`metallic_q_s4_exact_lp_sweep.py`](../../folio-assistant/computations/metallic_q_s4_exact_lp_sweep.py);
witness: `metallic-q-s4-exact-lp-sweep.witness.json`. 5/5 validation
assertions (proved n=2 closed forms, silver mpfr regression at 1e-39,
canonical Markov stability, Hecke relation, trace symmetry).

**Findings:**

1. **`S(2) = S(3) = S(4) = {δ_silver}` at the cost-coincidence level.**
   The γ-vs-σ₁ coincidence of the proved n=2 theorem extends exactly:
   at n=3 and n=4 the root sits at `q* = 2.414213562…` with 40-dps
   residuals `< 10⁻³⁷`. **No other metallic ratio appears** — the
   sharpened-(M2) expectation that S(n) might grow with n is refuted
   up to n=4: the ladder's LP-visible rung is silver alone.
2. **The n≥3 active-set flip was a Gram-approximation artifact.** With
   the exact Gram the LP active set is constant across the whole sweep
   at n=3 and n=4 (both conventions). The prior n=3 probe's
   "identity-channel → crossing-channel flip" framing is withdrawn
   (correction noted in the synthesis audit §2 and in the
   [`rem:sdp-degeneracy-at-metallic-coincidence`](../../content/quantum-observable-universe/mass-theory/sdp-degeneracy-at-metallic-coincidence.md)
   block). The n=2 active-set transition stands (its Gram is exact).
3. **Convention anchoring.** The silver coincidence lives in the
   q-Plancherel weight family `y_λ = H_q(λ)²/[n]_q!` (the convention of
   the proved theorem). Under canonical Markov weights
   (`trace_weights_n`) there are **no** metallic coincidences (n=3:
   zero roots; n=4: 12 word-specific roots, none metallic).
   Any physical wiring of the silver mechanism must therefore say
   *which trace normalization the observable uses*.
4. **New exact point: `q = 4` in the canonical convention.** Two of
   the canonical-convention coincidences (`γ` vs `σ₁σ₂σ₁`, and `σ₁`
   vs `σ₁σ₂σ₁σ₃`) sit at `q* = 4` **exactly** (40-dps residuals
   `≈ 10⁻⁴¹`, weights re-derived in mpmath from the Ocneanu defining
   values and cross-checked against the native f64 solver).  `q = 4`
   is not metallic; it is the point where the Wenzl-JM Markov
   parameter turns rational: `z = 1/(√q + 1/√q) = 2/5`.  So the
   canonical convention appears to carry its own arithmetic ladder —
   anchored at rational points of the `z`-parameterization rather
   than integer points of `q − q⁻¹`.  Symbolic proof deferred
   (follow-up 1).
4. All other coincidence roots are word-specific algebraic numbers in
   `(1.2, 1.6)` — the same pattern as the Jones-root nulls of #2047.

### 1.5 q = 4 — PROVEN exact, and NOT metallic (owner follow-up)

Symbolic proof ([`metallic_q4_canonical_coincidence_proof.py`](../../folio-assistant/computations/metallic_q4_canonical_coincidence_proof.py),
exact over `ℚ(s)`, `s = √q`; generator convention locked to
`pyhecke_native` by a 360-case verification, worst rel. err 1.8e-15):

```
t(γ)  − t(σ₁σ₂σ₁)    =  (2 − s) / (s² + 1)
t(σ₁) − t(σ₁σ₂σ₁σ₃)  =  −s(s − 2) / (s² + 1)²
```

Both vanish **iff `s = 2 ⟺ q = 4`**. Verdict on "because metallic?":
**no** — `δ_4 = 2 + √5 ≈ 4.236 ≠ 4`, and **no metallic minimal
polynomial `q² − nq − 1` divides any of the 36 pairwise canonical
numerators** (checked exactly). The mechanism is **s-arithmetic**: the
canonical (Wenzl-JM) convention's coincidence arithmetic lives in
`√q` — the variable its Markov parameter `z = 1/(s + s⁻¹)` is rational
in (`z = 2/5` at `s = 2`) — while the plancherel convention's lives in
`q − q⁻¹` (the metallic ladder). Two conventions, two arithmetic
ladders. The two pairs reduce to ONE primitive identity by Markov
stability (`t(σ₁σ₂σ₁σ₃) = z·t(σ₁σ₂σ₁)`, `t(σ₁) = z·t(γ)`):

```
tr_M(T_{σ₁σ₂σ₁}) = (s² + s − 1)/(s² + 1)  =  1 = tr_M(γ)  ⟺  s = 2.
```

Lean lemma for the factored identities is the natural capstone
(silver_lp_coincidence pattern; `field_simp; ring`-shaped) — queued as
follow-up, sympy certificate in the witness meanwhile.

### 1.6 S(5) — silver-only continues

[`metallic_q_s5_coincidence_sweep.py`](../../folio-assistant/computations/metallic_q_s5_coincidence_sweep.py):
120-word T_w basis, 7 partitions. 139 plancherel coincidence roots,
**exactly one metallic — the same γ-vs-σ₁ pair at δ_silver,
mpfr-exact**; canonical: 92 roots, zero metallic; LP active set
constant at all 22 exact-Gram checkpoints (both conventions). So

```
S(2) = S(3) = S(4) = S(5) = {δ_silver}
```

and the conjectured-general statement sharpens to: *for every n,
`t_pl(γ) − t_pl(σ₁)` vanishes on `q > 1` exactly at `q = δ_silver`* —
an n-indexed family of identities, prime Lean target.

### 1.7 Silver family — closed forms derived (owner follow-up 1)

[`metallic_silver_family_closed_forms.py`](../../folio-assistant/computations/metallic_silver_family_closed_forms.py)
derives `Δ_n(q) = t_pl(γ) − t_pl(σ₁)` exactly for n = 2, 3, 4, 5:

```
Δ_n(q) = (q² − 2q − 1) · C_n(q),   C_n sign-definite on q > 0
```

with every cofactor a (negated) product of polynomials positive on
`q > 0` — e.g. `Δ₃ = −(q²−2q−1)(q²−q+1)(q²+q+1)(q⁴+3q²+1)/(q⁴(q²+1))`.
Notably every cofactor is **palindromic** (bar-invariant): the silver
quadratic carries ALL the bar-breaking of the difference.  So
`t_pl(γ) = t_pl(σ₁) ⟺ q = δ_silver` is now PROVED in closed form at
each n ≤ 5, not just mpfr-verified.  Lean formalization:
`QOU.AlgebraicSubstrate.MetallicSilverFamily` (n = 3, 4, 5;
n = 2 is the existing `silver_lp_coincidence`) +
`QOU.AlgebraicSubstrate.MetallicCanonicalSqrtQ` (the q = 4 identities,
§1.5) — sorry-free source authored this session; build verification
recorded in the PR thread.

### 1.8 √q-ladder census — REFUTED as a family (owner follow-up 2)

Classifying every irreducible factor of the 36 exact canonical
pairwise numerators (from the §1.5 witness — no new scans) into
arithmetic families:

| family | count |
|---|---|
| s-rational (`s ∈ ℚ`) | **2** (both `s − 2`, the proven q = 4 point) |
| `s − s⁻¹ ∈ ℚ` quadratics | **0** |
| `s + s⁻¹ ∈ ℚ` (z-rational) quadratics | **0** |
| q-metallic (`q² − nq − 1`) | **0** |
| irreducible deg 4/8/10 | 10 |

The deg-4/8/10 factors are non-palindromic monic units of `ℤ[s]`
(constant term ±1) — generic algebraic numbers with no z-structure.
**Verdict: `s − s⁻¹ ∈ ℚ` is NOT the canonical analogue of the metallic
equation.  The canonical convention has exactly ONE arithmetic point
in the physical region at n = 4: `s = 2` (q = 4, z = 2/5).**  The
parallel "two conventions, two ladders" picture from §1.5 sharpens to
"two conventions: a metallic LADDER (plancherel) vs a single rational
POINT (canonical, at n = 4)".

## 2. q↔ρ calibration — three corpus-anchored maps

Script: [`metallic_q_rho_calibration.py`](../../folio-assistant/computations/metallic_q_rho_calibration.py);
witness: `metallic-q-rho-calibration.witness.json`. No fits — each map
is an identification anchored in existing corpus structure, reported
tiered:

| Map | Anchor | ρ(φ) | ρ(δ_silver) | ρ(φ²) | ρ(δ_bronze) |
|---|---|---|---|---|---|
| **A** kinetic ℏ_q² (`ℏ_q ∝ ρ^{1/3}`) | q(ρ₀)=q₀ | 57 ρ₀ | **207 ρ₀** | 243 ρ₀ | 348 ρ₀ |
| **B** energy-crossover (corpus gap closure, rel/nonrel) | E_comp closes 934 MeV gap | 7.5–10 ρ₀ | **64–117 ρ₀** | 98–192 ρ₀ | 341–798 ρ₀ |
| **C** coral-tube overlap (\|c_r\| = 0.6–1.0 fm) | spacing = tube scale | 2.4–5.1 ρ₀ | **6.3–29 ρ₀** | 7.6–41 ρ₀ | 13–112 ρ₀ |

**Structural identities found (verified 40+ dps, asserted in the witness):**

- `ℏ_q(φ) = (φ−1)/φ = 1/φ² = q_gold` **exactly** — the deformation
  parameter at the golden rung *is* the corpus deconfinement boundary.
- `φ² + φ⁻² = 3` exactly (Lucas L₂) — the φ² rung's Hecke-scalar sum is
  integer, though φ² is *not* a metallic ratio itself.

**Observational gate (NICER 2024-2026).** Inferred central densities
are `n_c(1.4 M☉) ≈ 2.8 ± 0.3 ρ₀` and `n_c(2.1 M☉) ≈ 3.8 ± 0.7 ρ₀`,
below 5 ρ₀ at 68% even for the heaviest pulsar (J0740+6620, `R ≈
11.4–16.1 km`; J0437-4715 `R ≈ 11.36 km`). Consequences:

- **Under all three maps, no known pulsar hosts a silver-rung core** ⇒
  the framework currently predicts **no NICER mass-radius kink** — and
  none is observed. The synthesis §4.1 framing ("consistent with the
  CFL-core prediction at high mass") is corrected: the calibrated
  prediction is *absence* of the kink in current stars.
- **The golden rung lands inside massive-NS cores under Map C**
  (2.4–5.1 ρ₀) — precisely the band where hyperons appear in standard
  NS physics and in the corpus's own layered table (outer core
  ρ₀–2ρ₀ hyperonic). The φ rung ↔ hyperon-onset identification is the
  live near-term observable of the shallow map.

### 2-bis. φ-rung ↔ hyperon-onset chain (owner item 4)

Under the power-law map the rung-density *ratios* are
anchor-independent: `ρ_φ = ρ_c^β`, `ρ_φ² = ρ_c^γ` with
`β = ln(φ/q₀)/ln(δ_s/q₀) ≈ 0.4850`, `γ ≈ 1.1043`. Identifying the φ
rung with the Λ onset therefore pins the whole ladder
([`metallic_phi_rung_hyperon_onset.py`](../../folio-assistant/computations/metallic_phi_rung_hyperon_onset.py)):

| Λ onset (ρ₀) | ⇒ silver (ρ₀) | ⇒ φ² (ρ₀) | implied \|c_r\| (fm) |
|---|---|---|---|
| 2.0 | 4.18 | 4.85 | 1.14 |
| 2.5 | 6.61 | 8.05 | 0.98 |
| 3.0 | 9.63 | 12.2 | 0.87 |

Three consistency hits, none fitted: (i) the implied coral-tube scale
is fermi-scale, bracketing 1 fm ≈ r_p; (ii) derived silver sits just
*above* all known-pulsar central densities (≤ ~4 ρ₀) — no kink in
current stars, matching non-detection; (iii) silver in the 4–10 ρ₀
band is exactly proto-NS / second-burst territory (§4). Λ-onset
window sources: [strange matter in compact stars (1711.11260)](https://arxiv.org/abs/1711.11260),
[phases of dense matter (1803.01836)](https://arxiv.org/abs/1803.01836),
[ΛNN forces & hyperon puzzle (1612.03758)](https://arxiv.org/abs/1612.03758),
[chiral hyperon suppression (2602.12503)](https://arxiv.org/abs/2602.12503).

## 3. φ² literature check (bar-mirror gCFL/CCS prediction)

Dense-QCD phenomenology places the CFL → gapless-CFL (gCFL) boundary at
`m_s²/2μ_q > Δ` and the crystalline (LOFF/CCS) window adjacent to it —
transitions expected at quark chemical potentials `μ_q ≲ 500 MeV`,
i.e. *just above* neutron-star reach, with the gap itself now
astrophysically constrained (`Δ ≲ 216–457 MeV` at `μ_B = 2.6 GeV`,
[arXiv:2401.16253](https://arxiv.org/abs/2401.16253)). Sources:
[gCFL evaluation (hep-ph/0406137)](https://arxiv.org/abs/hep-ph/0406137),
[gCFL vs mixed phases (hep-ph/0407257)](https://arxiv.org/abs/hep-ph/0407257),
[crystalline CSC strength (0710.0331)](https://arxiv.org/abs/0710.0331),
[CSC crystallography (hep-ph/0606066)](https://arxiv.org/abs/hep-ph/0606066).

**Verdict:** the bar-mirror prediction (second transition at `q = φ²`,
between silver and bronze) is *structurally aligned* with the QCD
expectation that gCFL/CCS sits directly above the CFL onset, and under
Map C its density (7.6–41 ρ₀) falls in the same "just beyond stable
stars" window the QCD literature assigns it. No current observation
pins or excludes it; the discriminating observables remain the
synthesis §4 suite. Nothing to wire — recorded as a literature
consistency check, not a confirmation.

## 4. Collapse cascade — the owner's nova question

Script: [`metallic_cascade_collapse_energy.py`](../../folio-assistant/computations/metallic_cascade_collapse_energy.py);
witness: `metallic-cascade-collapse-energy.witness.json`.

**Is "star gets dense enough → q crosses rungs → cascading burst, then
steady release" what happens?** In-framework: **qualitatively yes** —
collapse is an ascending traversal of the q-ladder
(`prop:bigbang-heatdeath` framing), each rung crossing is first-order
(Milnor `μ̄(123)` jump at silver), and the framework's own
burst/steady decomposition matches the observed phenomenology. The
quantitative pieces:

- **Latent heat at silver:** the Borromean−Hopf branch gap *evaluated
  at* `q = δ_silver` is `17.11 Skein ≈ 21.5 MeV/baryon`.
- **Cascade energy:** `5.7×10⁵² erg` for a 1.4 M☉ core (`4.9–8.2×10⁵²`
  across 1.2–2.0 M☉) — **the same order as, and ~20% of, the observed
  SN 1987A neutrino burst** (`≈3×10⁵³ erg / ~13 s`, standardly
  attributed to proto-NS gravitational binding). The QOU cascade is an
  *additive* contribution currently hidden inside the factor-~2
  uncertainty of the 25-event 1987A sample.
- **Composition before → after:** onion-shell star (H/He/C-O/Si shells,
  ⁵⁶Fe Chandrasekhar core) → proto-neutron star (+ under the shallow
  map, a CFL inner core past silver) + ⁵⁶Ni ejecta. The "strong steady
  release" the owner describes is two things: the **⁵⁶Ni → ⁵⁶Co → ⁵⁶Fe**
  radioactive light curve (ejecta, 6.1 d / 77 d) and the **CFL-gap-
  regulated cooling plateau** of the remnant core
  (`Δ_CFL ≈ 2.5 MeV`, `prop:cfl-neutron-star-observables`).
- **Parity-class bookkeeping** (#2074 closed form, exploratory):
  neutronization `e⁻+p→n+ν_e` flips Z-parity, pushing A≡0 (mod 4)
  nuclei out of the spectrally-positive class (⁵⁶Fe allowed → ⁵⁶Mn
  disallowed) — a QOU-native reading of why e-capture forces bulk
  restructuring. Caveat: admissibility ≠ lifetime ordering (⁵⁶Ni
  decays faster than the disallowed ⁵⁶Co).

**The clean discriminator between the maps:**

| Placement | Prediction |
|---|---|
| **Shallow (Map C)** | heaviest proto-NS cross silver a few 100 ms post-bounce → **delayed second ν̄_e burst** (+ ~6×10⁵² erg/M☉) — the same observable shape as the QCD-transition mechanism of [Sagert et al. 2009](https://arxiv.org/abs/0809.4225) / [Dasgupta et al. 2009](https://arxiv.org/abs/0912.2568), detectable for any galactic SN regardless of oscillation scenario |
| **Deep (Maps A/B)** | no SN core ever crosses (ρ_c ≥ 64 ρ₀): cascade fires only inside BH-forming collapse, swallowed by the horizon → **no second burst in any SN** (consistent with non-detection to date) |

**"Any data like this?"** Yes: (i) SN 1987A is exactly the pre/post
energy accounting the owner asks for (binding-energy budget vs observed
ν + kinetic + light); (ii) the second-burst timing structure is the
standing literature test (next galactic SN: IceCube/Super-K/Hyper-K);
(iii) NICER central-density posteriors gate which map is live (§2).

## 5. Follow-ups (not in this PR)

1. The `q = 4` canonical-convention coincidences (verified exact at
   40 dps, §1.4) — prove symbolically and check whether `√q ∈ ℤ` /
   `z ∈ ℚ` generates a ladder of further exact points (formalize-first
   before any wider scan).
2. S(5)+ via the same native pipeline (24 → 120 words; still feasible).
3. A `conj:`-level content block for the cascade/second-burst
   prediction once a map is preferred (needs owner direction on
   shallow-vs-deep framing).
4. Hyperon-onset ↔ φ-rung identification under Map C (corpus already
   has the hyperonic layer; a quantitative onset-density comparison is
   a one-afternoon probe).

## Cross-links

- Corrected: [`2026-06-09-metallic-q-csc-phase-synthesis.md`](2026-06-09-metallic-q-csc-phase-synthesis.md) §2 (active-set flip), §4.1 (NICER framing)
- Block updated: [`rem:sdp-degeneracy-at-metallic-coincidence`](../../content/quantum-observable-universe/mass-theory/sdp-degeneracy-at-metallic-coincidence.md)
- Witnesses: `metallic-q-s4-exact-lp-sweep` · `metallic-q-rho-calibration` · `metallic-cascade-collapse-energy`
- NICER sources: [PRD 111 (2025) 034005](https://arxiv.org/abs/2412.05923), [Miller et al. J0437 radius](https://arxiv.org/abs/2512.08790), [chiral-EFT + NICER constraints](https://arxiv.org/abs/2407.06790)
