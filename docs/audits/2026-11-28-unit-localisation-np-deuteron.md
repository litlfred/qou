# One energy unit cannot fix both the n−p split and the deuteron

**Date:** 2026-11-28 · **Beans:** `qou-91w7` (energy unit), `qou-myts` (accuracy epic)
**Probe:** [`computations/probes/unit_localisation/unit_localisation_probe.py`](../../computations/probes/unit_localisation/unit_localisation_probe.py) → `result.json` (mpmath 50 dps, no float64)

## 1. Question

Is the energy unit the single source of the n−p and deuteron misses? Every route on record reads an energy as `U × (dictionary energy)`, where the dictionary energy is `−ln(trace)`, so both observables are linear in `U`.

## 2. Inputs (all from `main`, nothing chosen)

- Flavour cell of `m_n − m_p`: `U · 2 ln q`, with the exponent 2 forced (`NucleonSplitFullTower.markov_forces_K`).
- EM piece of `m_n − m_p`: −0.7571 MeV (Form-B α × V³ all-pairs trace, audit 2026-11-24 E07). This is a model term, conditional on the Form-B premise classes.
- Deuteron: `U · (−ln r)`, where `r` = 0.998497 is the γγ `V(2)³` trace ratio (`gg-deuteron-bond.witness.json`).
- Five units on record: `E₀`, `E₀` tower, `E_osc`, `m_e/ℏ_q²` and the electron log unit `m_e/|ln τ_e|`.

## 3. Result

| unit | U (MeV) | n−p total (MeV) | factor needed, n−p | deuteron (keV) | factor needed, ²H |
|---|---|---|---|---|---|
| `E₀` | 4.186 | 0.116 | 2.35 | 6.30 | 353 |
| `E₀` tower | 4.227 | 0.125 | 2.32 | 6.36 | 350 |
| `E_osc` | 42.25 | 8.06 | 0.233 | 63.5 | 35.0 |
| `m_e/ℏ_q²` | 52.05 | 10.11 | 0.189 | 78.3 | 28.4 |
| `m_e/|ln τ_e|` | 1.383 | −0.468 | 7.10 | 2.08 | 1069 |

**The ratio of the two required factors is 150.54 for every unit,** because `U` cancels. It equals `[B(²H)/(−ln r)] / [(Δm_np − EM)/(2 ln q)]`.

## 4. What this localises (scope (a))

- No linear energy unit fixes both observables. Whichever unit makes n−p right leaves the deuteron short by a factor of about 150.
- So **the n−p miss can be a unit problem, but the deuteron miss cannot**. The deuteron's error sits in its trace ratio, that is, in the bond word: the γγ bond V³ is a near-identity at q₀.
- None of the five units on record gives n−p either. The units closest to it miss by ×2.35 (too small) and ×4.3 (too large).

This is a statement about linear-in-log units and the words on record. A unit that depends on the observable, or a bond word other than V³, falls outside it.

## 5. Not done

The precision gates did not run: the light environment has no `qou_substrate`. The probe is mpmath from start to finish, with no float arithmetic.
