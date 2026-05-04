# Structural reconciliation: atomic-braid-mass ↔ six-term theorem

**Date:** 2026-05-04
**Scope:** PR #534 follow-up (option 1 from "what's next" menu).
Per user direction: "Reconcile structure: derive how `M = constituent + α·Σ ln|V|` (atomic-braid-mass) and `M = T1 + T2 + T3 + T4 + T5 + T6` (six-term theorem) are the same equation in two notations."

## TL;DR — they are NOT the same equation

The two formulas describe **different observables**:

- `prop:atomic-braid-mass` is an **atomic-mass formula** with **CODATA inputs** (m_p, m_n, m_e). Gives the atomic mass M(Z, N) directly with a small categorical correction. **0.18% mean error** because most of the mass is in the CODATA constituent sum.

- `thm:knot-mass-formula-unified` is a **vortex/particle mass formula** with **only categorical inputs** (q_0, m_e). Computes the categorical mass m(ϱ) of an arbitrary braid-class without CODATA proton/neutron inputs.

They are **not equivalent** at the level of inputs. They become consistent only at the **conceptual layer**: both are derivations of the categorical mass identity `m(K) = m_e · ρ_K · |tr_M(T_w)|` (`prop:categorical-mass-markov`), but they expose different parts of the structure.

## Decomposition by inputs

| Formula | Inputs | Output |
|---------|--------|--------|
| `prop:atomic-braid-mass` | q_0, m_e, **m_p (CODATA), m_n (CODATA)**, atomic braid β | atomic mass M(Z, N) |
| `thm:knot-mass-formula-unified` | q_0, m_e, vortex braid β_K | categorical mass m(ϱ_K) |

For the atomic-braid-mass formula, three of the four numerical inputs (m_e, m_p, m_n) are CODATA values. The formula's only categorical content is the per-generator volumes |V̂_i^full| of the atomic braid and the multiplicative scale α = m_e · 8G. Writing it out:

```
M_atomic(Z, N) = Z·m_p_CODATA + N·m_n_CODATA + Z·m_e_CODATA  ← inputs (3 CODATA + 1 categorical)
              + α · Σ_i ln|V̂_i^full|                          ← categorical correction
```

The "+α · Σ ln|V|" correction adds nuclear binding (the difference between sum-of-free-constituents and the bound atomic mass) plus tiny atomic binding (electron-proton interaction). Empirically the correction is ~−0.04 MeV for proton up to ~−7 MeV for ⁴He. This is small relative to the constituent sum (~1000-4000 MeV), so the formula's accuracy is dominated by the CODATA inputs being correct.

For the six-term theorem, NONE of the inputs are CODATA particle masses. The theorem computes m(ϱ_K) from braid-only data plus q_0 and m_e:

```
m(ϱ_K) = T1 + T2 + T3 + T4 + T5 + T6
       = |tr_M(T_w)|                                       ← canonical Markov trace
       + Σ_i (-Li_2^q(-|V̂_i^full|))                       ← single-gen brane tower
       + z² Σ_{i<j} (-Li_2^q(-|V̂_i V̂_j|))                ← pair-gen brane tower
       + m_e · τ(C_dim_q)                                   ← Frobenius co-Casimir
       + a_K · 𝒞_K                                          ← chirality factor
       + Σ_{ℓ≥2} Res / (q_0 - ζ_ℓ)                         ← cyclotomic tail
```

This computes mass FROM SCRATCH categorically. To predict atomic masses with this formula, one would compute m(ϱ_proton), m(ϱ_neutron), m(ϱ_electron) separately, then combine via some atomic-binding rule.

## Why the implementations diverge

`paper_six_term_isotope_sweep.py` runs the six-term theorem applied directly to the atomic braid (not nucleon-by-nucleon). With proton mass calibration `E_0 = M_p_CODATA / m_p_hecke_atom`, this implicitly assumes:

```
m_atomic(ϱ) ≈ E_0 · (T1 + T2 + T3 + T4) + T6_MeV
```

i.e., the entire atomic mass is captured by the six-term sum scaled by E_0. That is too aggressive: the six-term sum at proton level is ~10⁶ Hecke-units (dominated by T2), so E_0 ≈ 10⁻³ MeV/Hecke, and at deuteron level the six-term sum is ~1.6×10⁶ which when scaled gives ~1480 MeV (vs CODATA 1876 — −21% error).

The atomic-braid-mass formula sidesteps this by **using CODATA inputs for the constituent sum** and only fitting α to the binding correction (which is ~MeV scale and tractable). This is why it works at 0.18%.

## What is the same

Both formulas use:

- The **same q-deformed structures**: per-generator volumes V̂_i^full, q-dilogarithm, q-integers
- The **same binding scale** α = m_e · 8G ≈ 3.7445 MeV (`prop:binding-scale-catalan`)
- The **same Wedderburn weights** w_λ = dim_q(λ)² / [n]_q!

What differs is the **structural decomposition of the total mass**:

- atomic-braid-mass writes mass as: `M = (free constituents from CODATA) + (categorical correction)`
- six-term theorem writes mass as: `M = (six categorical terms with no CODATA inputs)`

## Reconciliation derivation (sketch)

To make the formulas formally consistent, one needs to show that the six-term theorem applied to a free constituent (proton or neutron) reproduces its CODATA mass — i.e., that the six-term theorem is **categorically self-calibrating**:

```
m_proton_six_term(q_0, m_e) ?= m_p_CODATA = 938.272 MeV
m_neutron_six_term(q_0, m_e) ?= m_n_CODATA = 939.565 MeV
```

If yes, the atomic-braid-mass formula reduces to the six-term theorem applied to the combined atomic braid (with extra inter-constituent corrections from per-pair and per-jet contributions). If no, the atomic-braid-mass formula must be re-derived to use six-term's nucleon predictions internally rather than CODATA inputs.

**Empirical status:** the six-term theorem (in any of the five `tower_mode` variants) does not reproduce m_p_CODATA without proton calibration. With proton calibration (E_0 fit to proton), it reproduces other atomic masses to 17.7-66.8% mean error depending on tower_mode (Path B's defect-binding model with α = m_e · 8G works at 0.34%, but uses a different formula structure — see `path-b-defect-binding-probe.witness.json`).

So the categorical predictions are not yet self-calibrating to CODATA. The atomic-braid-mass formula's accuracy comes from the CODATA constituent inputs, not from the categorical machinery.

## Recommendation

The two formulas are not directly equivalent and should be presented as **complementary**, not competing:

1. **`prop:atomic-braid-mass`** (atomic-mass formula): use for **atomic-mass predictions with sub-1% accuracy**. Take CODATA m_p, m_n, m_e as inputs. Add α · Σ ln|V̂_i^full| as the categorical binding correction. Production-ready.

2. **`thm:knot-mass-formula-unified`** (vortex-mass theorem): the **deeper categorical statement**. Computes mass from braid-only inputs without CODATA. Currently has structural issues at q_0 evaluation (the Φ_q→Li_2^q correction in PR #534 partially fixes this, but the additive sum doesn't reach sub-1% accuracy without per-particle calibration). **Open derivation question:** show that m_proton_six_term = m_p_CODATA categorically (i.e., the formula is self-calibrating).

3. The two are **consistent at the categorical-mass-identity level** (`prop:categorical-mass-markov`): m(K) = m_e · ρ_K · |tr_M(T_w)| is the foundation. atomic-braid-mass derives ρ_K implicitly via the CODATA-input convention; six-term theorem derives ρ_K explicitly via the spectral-sequence decomposition.

The reconciliation is at the LOGICAL level (both serve the categorical mass identity); they are not the same EQUATION.

## Files

- `prop:atomic-braid-mass`: `content/quantum-observable-universe/particle-interactions/atomic-braid-mass.md`
- `thm:knot-mass-formula-unified`: `content/quantum-observable-universe/braids-and-knots/knot-mass-formula-unified.md`
- `prop:categorical-mass-markov`: `content/quantum-observable-universe/braids-and-knots/categorical-mass-markov.md`
- `prop:binding-scale-catalan`: `content/quantum-observable-universe/braids-and-knots/binding-scale-catalan.md`
- Computation: `paper_six_term_isotope_sweep.py` (six-term, 5 tower_mode variants)
- Computation: `atomic_braid_mass_paper_formula.py` (paper's working zero-fit formula)
- Computation: `path_b_defect_binding_probe.py` (defect-binding alternative)

## Refs

- PR #524 brane-tower-isospin-diagnosis (the −737 MeV pathology)
- PR #534 (this PR — Φ_q → Li_2^q correction)
- gist: https://gist.github.com/litlfred/b3459bf9143dd03234a9fc55c370f6f4
