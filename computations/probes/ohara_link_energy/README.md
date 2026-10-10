# O'Hara / Möbius link energy of the candidate closures — route 1 (beans `qou-pzsi`, `qou-99qc`)

Owner, 2026-10-10: work the energy / O'Hara selection principle by route 1. That means computing the **link** Möbius energy of the canonical closed-braid embedding of each candidate braid word, then flowing it down. Owner, same day: *"Multi-start first"*, then *"record as bean notes + probe PR"*.

**Numerical evidence only.** Every energy below is an **upper bound**: a local minimum reached by gradient flow, in float64. No Q_β, CODATA or mass number enters any computation or ordering.

The candidates are 2-component **links**. Freedman–He–Wang Theorem B covers prime **knots**, so whether minimisers exist here is **open**.

## What is here

| path | what |
|---|---|
| `ohara_lib.py` | energy (self + mutual, normalised so a round circle is 4), closed-braid embedding, flow, topology guard |
| `calibrate.py`, `calibration_G1_G3.json` | the calibration gates: Hopf mutual energy is 2π² (Agol–Marques–Neves); Möbius invariance |
| `braid_topology.py`, `braid_topology.json` | per-candidate components, linking numbers, and the conjugacy finding |
| `run_candidate.py`, `analyse.py`, `results.{md,json}`, `preregistration.md` | route 1: one flow per start |
| `multistart/` | multi-start search: 61 + 11 starts, its own pre-registration, the final ranking |

Run each script from its own directory, e.g. `cd computations/probes/ohara_link_energy && python3 calibrate.py`. The `multistart/` scripts import the library from `..`.

## Findings

1. **Topology, checked by hand.** With `σ₁ = gen0` and `σ₂ = gen1`, `NUC9 = (σ₁σ₂)³·σ₁²σ₂`, and `(σ₁σ₂)³ = Δ²` is central.
   - `σ₁²σ₂·σ₁σ₂ = σ₁³σ₂σ₁ ~ σ₁⁴σ₂` and `σ₁²σ₂·σ₁σ₁ ~ σ₁⁴σ₂`. So **`gluon_s0_s1` ≅ `gluon_s0_s0` = `nuc11_interleaved`**.
   - `σ₁²σ₂σ₂σ₁ ~ σ₁³σ₂²` and `σ₁²σ₂³ ~ σ₁³σ₂²` (conjugation by Δ). So **`gluon_s1_s0` ≅ `gluon_s1_s1`**.
   - The four gluon dressings therefore close to **two** links, not four.
   - The probe confirms this with matching Jones and Alexander polynomials.
2. **Calibration.** Hopf gives `8 + 4π² = 47.4784` against 47.48 from flow; the mutual term is ≥ 2π², within 0.012 %. The trefoil gives 74.42; the literature value ≈ 74.4 was not found in `library/`, so it is unverified.
3. **Ranking after multi-start** (`multistart/results.md`). Class A is `{gluon_s1_s0 ≅ gluon_s1_s1}`; class B is `{gluon_s0_s1 ≅ gluon_s0_s0 = nuc11_interleaved}`.

   | pair | gap | combined error | separated? |
   |---|---|---|---|
   | nuc9 < A | 56.7 | 1.1 | yes |
   | nuc9 < B | 57.9 | 0.9 | yes |
   | A < gen_grouped | 23.6 | 1.0 | yes |
   | B < gen_grouped | 22.4 | 0.7 | yes |
   | **A vs B** | 1.1 | 1.2 | **no** |

   - Route 1's single-start gap of 4.8 between A and B was an artefact: every start fell into one of B's four local minima.
   - `gen_grouped` did not converge: 12 different minima from 12 starts.
4. **The discrete flow undercounts by a shape-dependent amount**, about 0.4–0.8 at N=256 and more for `gen_grouped`. That limits how finely minima can be ranked. The upper bounds themselves are unaffected.
5. **The limit of the whole approach.** This is a link-type quantity, so it can **never** separate `gluon_s0_s1` from `nuc11_interleaved`: they are the same link. Telling them apart needs data beyond the closure.

## Post-hoc changes, disclosed

- The route-1 flow method was changed after pre-registration while debugging the Hopf calibration: Möbius-mode projection, L-BFGS, a curvature term, a per-pair guard, and a running-minimum stop.
- The 0.177 error floor in route 1 was set after seeing data.
- The multistart error bars come from its pre-registered analysis (`ms_analyse.py`).
- Route-1 starts do not bit-reproduce, because `ohara_lib.py` was edited a minute after the route-1 queue began.
