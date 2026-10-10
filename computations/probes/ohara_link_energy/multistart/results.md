# Results — multi-start firming of the flowed upper bounds (phases 1 and 2 complete — see §0 for the final numbers)

Pre-registration: `preregistration.md`, written before any new energy value. `../ohara_lib.py` was
imported unchanged (same energy, normalisation with the round circle = 4, guard and certificates). No
Q_beta, CODATA value or mass number appears anywhere. **All values are upper bounds**: each is the
spectral energy of an explicit smooth curve whose link type is certified, and each comes from a
local minimum of a guarded flow. Whether a minimiser exists for these 2-component links is **open**
(Freedman–He–Wang Thm B covers prime knots only).

**Status at hand-back:** phase 1 (61 starts, N = 64/128/256) is finished. Phase 2 (N = 512
continuations, `ids_phase2.txt`, 11 jobs) is **still running** under nohup and writes
`logs/phase2.done` when it ends. Then run `python3 ms_analyse.py`, which merges the `*_p2` runs and
fills the pre-registered error bars. Until that has run, every error bar below is **POST-HOC**: it
uses the N = 256 cluster spread and the measured discretisation bias (§3) in place of
|E(512) − E(256)|.


## 0. FINAL (phase 2 at N = 512 analysed; `ms_analyse.py` → `results.json`; supersedes the post-hoc bars in §5)

N = 512 continuations (cap 2000, tol 1e-8), all certified:

| run | E(256) → E(512) | stop |
|---|---|---|
| nuc9_s11 | 234.189 → 234.212 | conv |
| A_s11 | 290.962 → **290.937** | conv |
| A_s10 (POST-HOC) | 291.384 → 291.140 | conv |
| B_s09 | 291.591 → 292.065 | conv |
| B_s08 (POST-HOC) | 293.540 → 292.736 | conv |
| B_s09 from its N=128 curve (POST-HOC) | 290.625 (N128) → **290.817** | conv |
| G_s05 | 314.216 → 314.491 | conv |
| G_s07 (POST-HOC) | 311.710 → **311.093** | **cap** |
| G_s09 | 316.669 → 316.915 | conv |
| G_s12 | 316.582 → 320.937 | conv |
| hopf_c1 | 47.4823 → 47.4792 (E12 19.73950, 1.5e-5 above 2π²) | conv — calibration PASS |

Pre-registered estimates (best start's finest N; err = max(|E512−E256|, lowest-cluster spread) + quad):

| class | estimate ± err | certified UB | distinct minima |
|---|---|---|---|
| nuc9 | **234.21 ± 0.42** | 234.19 | 1 |
| A | **290.94 ± 0.69** | 290.94 | 1 |
| B | **292.06 ± 0.47** (pre-reg start B_s09) | **290.82** (POST-HOC run) | 4 |
| G | 314.49 ± 0.27 (G_s05) — **not converged** | 311.09 (capped run) | 12 |

Separation (pre-registered rule): nuc9 < A, nuc9 < B, A < G, B < G all SEPARATED. **A vs B NOT separated**
(gap 1.13 vs combined err 1.16 on the pre-registered estimates). On the certified upper bounds, B (290.82) is
*below* A (290.94). **The route-1 ordering A < B does not survive.**

G fails the pre-registered convergence criterion: its best run (s07) hit the cap, and its lowest cluster has one
member. |E512−E256| for s05 is 0.27, which by itself passes. G_s12 rose by 4.4 between N=256 and N=512, which is
the bias mechanism of §3.

## 1. Calibration (same batch, same code): PASS
| start | E_tot N=256 | E12 N=256 | target |
|---|---|---|---|
| hopf_c1 σ1² | 47.4823 | 19.74065 | 8+4π² = 47.47842; 2π² = 19.73921 |
| hopf_c2 σ0σ0σ1 (3 strands) | 47.4839 | 19.74116 | |
| hopf_c3 Möbius image | 47.4805 | 19.74004 | |
| trefoil_c1 σ1³ | 74.4230 | — | ≈74.4 (**from memory; not in qou library/, searched — unverified**) |
| trefoil_c2 σ0³σ1 (3 strands) | 74.4179 | — | |
E12 ≥ 2π² in every case, and the deviation is ≤ 0.012 %.

## 2. Per class (N = 256, M = 16N spectral; every listed start has topology certified at start/end/fine interpolant, with lk unchanged)
Per-start tables: `results.json` → `starts`, or run `python3 ms_analyse.py`.

| class | link | starts (conv/total) | distinct minima | best UB (start) | lowest-cluster spread | route-1 | lowered beyond route-1 err? |
|---|---|---|---|---|---|---|---|
| nuc9 | T(2,3)∪U lk3 | 14/14 | **1** | **234.19** (s11 Möbius) | 0.42 (234.19–234.61) | 234.50±0.28 | yes, barely (by 0.03) |
| A {s1_s0≅s1_s1} | T(2,5)∪U lk3 | 14/14 | **1** | **290.96** (s11 Möbius) | 0.69 (290.96–291.65) | 291.15±0.38 | no |
| B {s0_s1≅s0_s0} | T(2,3)∪U lk4 | 14/14 | **4** | **291.59** (s09, Markov-stabilised 4-strand) | — | 295.90±0.32 | **YES, by 4.3** |
| G gen_grouped | T(2,7)∪U lk2 | 12/13 (+1 start not generable) | **12 (every converged start distinct)** | **311.71** (s07 Δ-conjugate, guard-stopped); lowest converged 314.22 (s05) | — | UB 316.09 | UB lowered by 4.4 |

The four B minima are the main new finding:

| B cluster | starts | E_tot | E_knot | E_unknot | E12 |
|---|---|---|---|---|---|
| low | s09 (stab top) | 291.59 | 92.8 | 8.2 | 95.3 |
| low (same shape, d_shape 0.03, not relaxed) | s08 (braid-relation rewrite) | 293.54 | 94.7 | 8.4 | 95.2 |
| route-1 minimum | 11 starts, among them every canonical, Möbius and perturbed start | 295.70–295.99 | 86.7 | 12.2 | 98.5 |
| third shape | s05 (gluon_s0_s0 word) | 295.99 | 88.5 | 8.2 | 99.6 |

Two further facts about B:
- **POST-HOC:** the N = 128 curve of B_s09 is a certified smooth curve with E = **290.62** (quadrature 2e-13). It lies outside the pre-registered UB set, which covers N ≥ 256 only.
- B_s08 and B_s09 have the same shape (d_shape 0.03) but energies 1.95 apart. Under the §4 rule (same shape, |ΔE| > 0.4) that is a flow/stopping failure for B_s08, not a distinct minimum. Phase 2 continues B_s08 at N = 512.

**Conjugate-word test.** nuc9 and A pass: every word reaches the single cluster, with per-word minima within 0.42 and 0.69. Strictly, A's 0.69 exceeds the pre-registered 0.4 tolerance, and since every A start shares one shape cluster, the §4 rule would make that a method failure rather than a pass. B passes for the corpus words: gluon_s0_s1 gives 295.71 and gluon_s0_s0 gives 295.99, with Δ 0.28 (different shapes). The lower B minimum was reached **only from the Markov-stabilised start and the braid-relation rewrite**, never from a corpus word.

## 3. Why the flow cannot do better than ≈ ±0.5 (A/B) or ±2 (G): discretisation bias (diagnostic, prereg §6)
`ms_gdiag.py` → `gdiag_B.json`, `gdiag_G.json`. The discrete flow functional is E_poly(N) ≈ E_spectral − c(shape)/N. It is first order in 1/N and **shape-dependent**:

| curves | c (≈ shape constant) | bias at N=256 | bias at N=512 |
|---|---|---|---|
| nuc9, B route-1 minimum | ≈ 95–100 | −0.37 to −0.39 | −0.17 |
| A_s11, B_s08, B_s09 | ≈ 185–205 | −0.72 to −0.81 | −0.32 to −0.37 |
| G curves | ≈ 560–960 | −2.2 to −3.7 | −1.0 to −1.7 |

The flow therefore minimises E − c(shape)/N, so at fixed N it prefers shapes it under-counts. That
explains route 1's anomaly, and also B_s09 and several G starts: their spectral energy *rose* from
N = 128 to N = 256 (290.62 → 291.59). It also explains why the cluster spreads reach about 0.4–0.7.
The upper bounds are unaffected, because each is a spectral evaluation of a certified curve. The
**ranking at the sub-unit level** is affected.

## 4. G (gen_grouped): NOT converged
G reached 12 different minima from 12 converged starts, spanning 314.2–326.1. 9 of the 13 N = 64
runs stopped on the guard. s07 (311.71) stopped on the guard at N = 256. s14 (ε = 0.15
perturbation) changed topology in all 30 draws, so no start could be generated.

The reason is §3: the bias is −2 to −4 at N = 256 and varies by about 1–1.5 between shapes. The
T(2,7) component (2 strands, 7 crossings) gets the same N as the unknot, so the tight clasps are
under-resolved. The bias varies between shapes by more than the energy differences between minima,
so the flow cannot rank them.

What would converge it, and was not done: N ≥ 1024 (bias ≈ 0.5), or N per component proportional
to strand count, or flowing the spectral functional itself. The last two are method changes that
need a new pre-registration. Phase 2 (N = 512 for G_s05, G_s12, G_s09, plus G_s07 POST-HOC) is
running.

## 5. Ranking (upper bounds; POST-HOC error bars = cluster spread or measured bias variation)
- nuc9 **≤ 234.19** (±0.4)
- A **≤ 290.96** (±0.7)
- B **≤ 291.59** at N = 256, and ≤ 290.62 for the certified N = 128 curve (POST-HOC) (±0.8)
- G **≤ 311.71** (not converged; ±≥2)

| pair | separated? |
|---|---|
| nuc9 vs A/B | yes (gap ≈ 57) |
| A/B vs G | yes (gap ≥ 19, even granting G's error) |
| **A vs B** | **NOT separated**: gap 0.63 against a combined error of ≈ 1.5; B's best certified curve (290.62) is *below* A's best |

**The route-1 ordering A < B does not survive.** Route 1's 4.8 gap was an artefact of every start
landing in the B minimum at 295.9.

## 6. Limitations
- Only upper bounds from local minima. Lower minima may still exist, especially for B, whose low basin was found by 1 of 14 starts, and for G.
- Error bars are POST-HOC until phase 2 is analysed.
- The shape invariant uses a conformal balancing of the arclength measure, whose uniqueness is not proven. The full d_shape matrices are in `results.json`.
- Route-1 bit-reproduction failed: the s01 starts differ from route-1 values by ≤ 0.6. The route-1 queue started at 09:05:51 and `ohara_lib.py` was edited at 09:06:44, so some route-1 runs used a pre-edit library.
- Everything is float64.

## Files
- Design: `preregistration.md`, `ms_words.py`/`.json` (exact topology of the representatives), `ms_lib.py`, `make_plan.py`/`ms_plan.json`
- Runs: `ms_run.py`, `queue.sh`, `runs/`, `curves/`, `logs/`
- Analysis: `ms_analyse.py` → `results.json`, `shape_cache.json`; `ms_gdiag.py` → `gdiag_*.json`
