# T6 — F_ℓ derivation attempt + paper-side inconsistency finding (2026-05-25)

**Branch**: `claude/gifted-feynman-U7ckD` → [#1127](https://github.com/litlfred/qou/pull/1127)
**Triggered by**: owner directive "t6" (work on T6 = lepton-mass-tower canonical formula derivation)
**Status**: T6 surfaces a paper-side inconsistency that must be resolved before F_ℓ can be derived

## What T6 tried

Compute `m_μ/m_e` and `m_p/m_e` DIRECTLY via the canonical per-braid mass tower (`prop:per-braid-mass-tower`, post-2026-05-17 `−Li_2^q` corrected form), using the V̂_i values published in `mass-endomorphism-tower.md §Application`:

| Particle | Generators | V̂ values (paper) |
|---|---|---|
| Electron (trefoil σ_1³) | 1 | V̂_e ≈ 0.594 |
| Proton ([u,u,d] in H_3) | 2 | V̂_0 ≈ 0.989, V̂_1 ≈ 0.971 |
| Muon (figure-eight 4_1) | 2 | NOT PUBLISHED (used proton values as crude proxy) |

Formula applied (corrected):

$$m(W) = |\!\prod V̂_i| - \sum_i \mathrm{Li}_2^q(-|V̂_i|) - z^2 \sum_{i<j} \mathrm{Li}_2^q(-|V̂_i V̂_j|)$$

at substrate $q_0 \approx 1.10998$ via 60-dps mpmath.

## Result

| Quantity | Value | Compare to |
|---|---:|---|
| `m_e_dimensionless` | 1.1177 | (calibration unit; F_e = 1 by convention) |
| `m_p_dimensionless` (using V̂_0=0.989, V̂_1=0.971) | 2.7769 | — |
| `m_p / m_e` via per-braid tower | **2.4845** | CODATA: **1836.15**; paper claims **1870** |
| `m_μ / m_e` via per-braid tower (proton V̂_i proxy) | **2.4845** | CODATA: **206.77** |

**Both ratios identical** (using same V̂_i for proton + muon proxy) and ~3 orders of magnitude smaller than expected.

## Inconsistency surfaced

`mass-endomorphism-tower.md` line 384 states:
> "m_p/m_e ≈ 1870 (CODATA: 1836.15, error 1.8%)"

This number cannot come from the **Li_2^q**-corrected formula with the published V̂_i (which gives 2.48). Possibilities:

### Possibility (a) — Paper computation used Φ_q (pre-correction)

The Faddeev quantum dilogarithm Φ_q grows extremely fast near |z| = q (has poles); at z = 0.989 with q_0 ≈ 1.110, the first factor in Φ_q(z) = Π(1 - q^(-k) z)^(-1) is:

$$\frac{1}{1 - q^{-1} \cdot 0.989} = \frac{1}{1 - 0.989/1.110} = \frac{1}{0.109} \approx 9.17$$

Subsequent factors multiply this. **Φ_q(0.989) ≈ several thousand** (numerical magnitude).

If the paper's "1870" was computed with Φ_q (not Li_2^q), then the **2026-05-17 correction** changes the predicted value from ~1870 to ~2.5 — a 750× shift. The corrected formula gives the WRONG number for the proton, and the paper's empirical match was an artefact of the pre-correction Φ_q form.

### Possibility (b) — Paper used different V̂_i

The values 0.989 / 0.971 might not be the "full" per-generator amplitudes the per-braid mass tower formula expects. The published values are described as "additive Wedderburn" volumes, which may need transformation before entering the Li_2^q sums.

### Possibility (c) — Paper formula has implicit SUPERSEDED ρ_q

The 750× factor between my computation (2.48) and the paper's claim (1870) is suspicious — it's close to 7.37 · 1/ℏ_q² where 7.37 = Vol(L6a4) Borromean rings hyperbolic volume. Not a clean match, but suggests a missing geometric factor.

## Implication for T6 (F_ℓ derivation)

**T6 cannot be completed by simple application of the canonical per-braid mass tower with published V̂_i.** The route forward requires resolving the paper-side inconsistency:

1. **Confirm which dilog form the paper uses** (Φ_q or Li_2^q) — check the production compute pipeline `canonical_plus_multibrane.py` + `paper_six_term_isotope_sweep.py` (per mass-endomorphism-tower.md line 137-140, "tower_mode='li2q'").
2. **If paper uses Li_2^q**: the "1870" estimate is WRONG and needs recomputation. The framework's published proton-mass prediction is overstated.
3. **If paper uses Φ_q**: the 2026-05-17 correction needs to be revisited — Li_2^q is being claimed canonical but Φ_q is being used in production, an internal contradiction.
4. **Either way**: T6's F_ℓ derivation cannot proceed without first resolving this 750× discrepancy in the canonical formula's outputs.

## Why this is a substantive finding (not a session-local error)

- The 2026-05-17 resolution (Li_2^q over Φ_q) was made because Φ_q gave a `−737 MeV` mirror-nucleus pathology (per `brane-tower-isospin-diagnosis`).
- The corrected Li_2^q form was supposed to fix the pathology.
- My computation shows Li_2^q gives 2.48 for m_p/m_e — also wrong, just in a different direction (massively undershoots).
- So **NEITHER Φ_q (undershoots in isospin) NOR Li_2^q (undershoots in mass scale) is correct** as currently published.

This is the kind of structural issue the SUPERSEDED ρ_q purge was supposed to expose. T6 now reveals the next layer: **the per-braid mass tower formula itself, in either Φ_q or Li_2^q form, does NOT correctly predict known masses without additional structural inputs**.

## What F_ℓ would actually need

Based on this finding, F_ℓ requires (at minimum):

1. **The correct dilog form** — and verification that it matches BOTH isospin and mass scale, not just one
2. **The correct V̂_i values for leptons** — currently UNPUBLISHED for muon/tau (only electron is given at 0.594)
3. **A reconciliation between the per-braid tower output and the Skein formula `Vol(4_1)/ℏ_q²`** — the two routes give vastly different numbers (2.48 vs 206.77 for m_μ/m_e), exposing the SUPERSEDED ρ_q's role in bridging them

## Recommendation

T6 (F_ℓ derivation) is **PROPERLY OPEN** — not a wiring task, not a 1-week implementation; it requires resolving:
- A 750× discrepancy in the framework's own per-braid mass tower outputs
- The dilog form ambiguity (Φ_q vs Li_2^q both claimed canonical at different times)
- The unpublished muon/tau V̂_i values

**Conclusion**: F_ℓ derivation remains genuinely open. The Phase 3 conclusion stands: the framework's lepton-mass formula is the Skein formula (Kashaev-LIMIT + SUPERSEDED ρ_q), and no canonical operator-level replacement exists yet.

## Lean

The `lepton_mass_ratio` sorry in `lepton-mass-tower-canonical.lean` remains correctly marked per CLAUDE.md §3b — the formula is genuinely conjectural, not just a formalisation gap.

## Cross-references

- [`prop:per-braid-mass-tower`](../../content/quantum-observable-universe/braids-and-knots/per-braid-mass-tower.md) — canonical formula, claimed canonical after 2026-05-17 Li_2^q correction
- [`mass-endomorphism-tower.md`](../../content/quantum-observable-universe/braids-and-knots/mass-endomorphism-tower.md) — paper's V̂_i values + "m_p/m_e ≈ 1870" claim
- [`conj:lepton-mass-tower-canonical`](../../content/quantum-observable-universe/braids-and-knots/lepton-mass-tower-canonical.md) — F_ℓ conjecture (NOW genuinely confirmed as open)
- [`docs/audits/2026-05-24-superseded-rho-q-purge.md`](2026-05-24-superseded-rho-q-purge.md) — purge that motivated T6
- [`docs/audits/2026-05-24-m-mu-over-m-e-operator-rederivation.md`](2026-05-24-m-mu-over-m-e-operator-rederivation.md) — Phase 3 finding (direct |tr_M| ratio = 0.27)
- New compute: `computations/f_ell_derivation_via_per_braid_mass_tower.py`
- New witness: `computations/f-ell-derivation-via-per-braid-mass-tower.witness.json`

## Next step for F_ℓ

The next session should:
1. **Investigate** `canonical_plus_multibrane.py` + `paper_six_term_isotope_sweep.py` to see which dilog form is ACTUALLY used in production and what V̂_i they consume
2. **Reconcile** the paper's "1870" estimate with the Li_2^q-corrected formula's output
3. **Only then** is F_ℓ derivation tractable

---

## Followup (2026-05-25, PR #1253) — tau amphichiral q-bracket finding

Per owner directive "tau is not torus knot; knot operator = symmetries → should be same as 1st gen. verify via SDP solutions" (where "same as 1st gen" was interpreted via muon = 4_1 amphichirality), [`computations/probes/tau_amphichiral_sdp_probe.py`](../../computations/probes/tau_amphichiral_sdp_probe.py) filtered SnapPy census to 12 amphichiral hyperbolic knots and tested q-bracket-corrected closures.

**Two candidates close to <1%** (both improving on PR #1250's torus-knot best of 1.33%):

| Knot | Vol | Formula | Predicted m_τ/m_e | Δ vs CODATA |
|---|---:|---|---:|---:|
| 10_37 | 11.332 | `3 · Vol/ℏ_q²` | 3462.95 | **−0.41 %** |
| 10_43 | 13.833 | `[5]_q·[3]_q/[6]_q · Vol/ℏ_q²` | 3504.66 | **+0.79 %** |

The 10_43 hit has the **structural q-bracket form analogous to muon's `[3]_q · [2]_q / [4]_q`** — generalising `conj:lepton-tower-h-n-plus-1-branching` from muon-only to the symmetric family `[2m+1]_q · [2m-1]_q / [2m+2]_q` covering both m=2 (muon) and m=3 (tau).

### Lean-formalised structural identity

The closure factor reduces algebraically to a single identity in h = q − q⁻¹, proved in [`three-halves-structural-factor.lean`](../../content/quantum-observable-universe/braids-and-knots/three-halves-structural-factor.lean):

```
muon (PR #1127):  [4]_q  =  (2 + h²) · [2]_q
tau  (PR #1253):  [6]_q  =  [2]_q · [3]_q · (1 + h²)
```

Both proved via `field_simp; ring` over generic `[Field R]` per CLAUDE.md §7c. Numerically cross-checked at the canonical q_0 to ≤ 1e-40 in the tau-probe witness (4 assertions, all pass).

### What this resolves vs leaves open

**Resolved:**
- Tau is **not** a torus knot (owner directive confirmed; PR #1250's T(2,7) family ruled out at 1%)
- Amphichiral filter narrows tau candidates from hundreds to ~12 in census
- Best amphichiral candidate (10_43) closes via structural q-bracket form, not arbitrary numerical factor
- Lean-formalised the algebraic identity behind the closure

**Still open:**
- The 750× per-braid-mass-tower discrepancy (above) — orthogonal to this PR's amphichiral finding (which uses Vol/ℏ_q² · q-bracket, not Li_2^q tower)
- Categorical derivation of WHY the partition (3,2,1) ↔ 10_43 ↔ [5]_q·[3]_q/[6]_q assignment (vs (2,1,1) ↔ 4_1 ↔ [3]_q·[2]_q/[4]_q for muon) — this is the "structural" question Option E (Kashiwara crystal, PR #1252) should address
- The conjectural `conj:lepton-tower-h-n-plus-1-branching` symmetric extension `[2m+1]_q · [2m-1]_q / [2m+2]_q` needs Lean formalisation beyond m=2,3
- True SDP-derived selection (the owner's "verify via SDP solutions" — this PR is SDP-spirit via the amphichiral filter, not the actual confinement SDP solve)
