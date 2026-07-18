# c_k^odd from the categorical fibre — corpus + literature attack map (2026-07-18)

Scoping synthesis (corpus grep + external literature) for the "derive a
c_k^odd from the fibre without routing through S = Q_β/E₀" program. Three
independent research legs (route-3 substrate-q₀ scoping, route-2 corpus
scoping, external literature search). No wiring; no fit; this is a map.

## The two structural facts everything else hangs on

**1. The swing's *value* is proved measurement-limited.** Sorry-free
`QOU.QBeta.SRigidity.no_anchor_invariant_realizes_swing` (scope-(b)): no
anchor-invariant fibre datum equals the c₃ carrier `S` (2.44 % proton/muon
swing, sensitivity ~3.84e6). Same-day direct measurements close the residual
openings: the 4₁ deformed Stokes amplitude is **real to the rung floor**
(odd-phase NULL, scope-(a), commit `f95c8f6730`), and the 5₂ anchor-dependent
quantum volume has `max |d𝔙/dq| = 1.47` — **O(1) vs the 3.84e6 required**
(`qbeta-5two-quantum-volume.witness.json`). A fibre derivation can supply the
**shape** of the bar-odd numerator `N_odd` (simple zero at q\*, slope
A′(q\*) ≈ +2.37, per the Im 𝔙_q→N_odd capstone scope doc); it cannot supply
the **value** below the experimental-Q_β floor (`dq*/dQ_β ≈ −0.54`). The gate
arithmetic is now Lean-recorded
([`MeasurementLimitedFloor.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/MeasurementLimitedFloor.lean)).

**2. 4₁ is amphichiral ⇒ its bar-odd channel vanishes identically.** The bar
involution on quantum knot invariants acts as mirror image
(`J_K(q⁻¹) = J_{K*}(q)`); 4₁ ≅ 4₁\* forces every fibre-level 4₁ invariant —
colored Jones, Kashaev, Ohtsuki series, Stokes data — to be **bar-even**.
This is the structural *reason* behind the odd-phase NULL: the session
measured a symmetry-forced zero. **The odd datum must come from a chiral
knot; 5₂ is canonical** (smallest chiral hyperbolic knot; the second worked
example in the entire relevant literature: GGM Stokes tables
[arXiv:2007.10190](https://arxiv.org/abs/2007.10190),
[2111.04763](https://arxiv.org/abs/2111.04763), Garoufalidis–Kashaev state-
integral factorization [1304.2705](https://arxiv.org/abs/1304.2705),
Garoufalidis–Zagier cocycles [2111.06645](https://arxiv.org/abs/2111.06645),
GSWZ Habiro-ring-of-a-number-field running example
[2412.04241](https://arxiv.org/abs/2412.04241)).

## Literature facts (external)

- **GGM Stokes matrices are pairs of integer-coefficient q-series**, one
  entry = the DGG 3D index; tabulated for 4₁ **and 5₂**. The raw Stokes
  constants are integers (BPS counts); the anchor-independent *real*
  constant must be an **evaluation of the Stokes q-series at q₀**, not a raw
  integer.
- **The Habiro ring has no archimedean evaluation off roots of unity**
  (generic elements converge nowhere off roots of unity). Real-q₀ access
  goes through (a) Borel–Laplace median resummation of the q→1 series
  (Costin–Garoufalidis resurgence proved for torus-knot families,
  [2304.07001](https://arxiv.org/abs/2304.07001)) or (b) the two-variable
  holomorphic-block / descendant q-series lifts, which converge for |q|≠1.
- **The bar-odd projection of the block/Stokes data is unstudied** — the
  literature works the symmetric pairings (state integral, index); the
  antisymmetric (chirality-odd) pairing is definable from published 5₂ data
  but has no named treatment. Genuine opening.
- **GZ quantum-modularity cocycle entries at the real-q ray are computable,
  calibration-free constants** (state-integral built, hundreds of digits for
  4₁/5₂/(−2,3,7)) — a third cross-check route.

## Ranked attack options

| # | attack | object / computation | feasibility |
|---|---|---|---|
| **A1** | **Chirality-difference state integral for 5₂** | `Z_{5₂}(ℏ₀) − Z_{5₂*}(ℏ₀)` (Andersen–Kashaev Φ_b product, 1-dim integral, explicit in 1304.2705) evaluated by mpmath quadrature at real `ℏ₀ = ln q₀` | **session-computable** — the cleanest genuinely fibre-level bar-odd real number at q₀ |
| **A2** | **Bar-odd projection of the 5₂ GGM Stokes / index q-series** | antisymmetric combination of the tabulated integer q-series pair under the q↔q⁻¹ swap; evaluate at `q₀⁻¹ ≈ 0.9009` (geometric convergence) | **session-computable** — published integer coefficients |
| **A3** | **Capstone-carrier falsification on 5₂** | extend `qbeta_5two_quantum_volume_probe.py`: does any `u³·(smooth)` normalization carry `Im 𝔙_q(5₂)` (O(1), no zero at q\*) to `N_odd` (O(1e-8), simple zero at q\*, slope +2.37)? expected **fail** → narrows the capstone carrier to the categorical H₅(q) Markov trace, not the analytic NZ saddle | **session-computable** falsification |
| **A4** | **Median Borel–Laplace of the 5₂ bar-odd perturbative series** | mirror-difference Ohtsuki series, Borel–Padé + median resummation on the real ray; cross-check vs A1 via resurgence | needs-serious-work |
| **A5** | **5₂ H₅(q) categorical Markov-trace 𝔙_q** | build the fibre-level (pre-archimedean) 5₂ datum to feed the quantum-modularity two-route rigidity | needs-serious-work (the flagged G3 obstacle) |
| **A6** | **GSWZ Habiro-ring-of-number-field element for 5₂** | Frobenius + Bloch-group formulation; no archimedean evaluation exists in the literature | open-problem; nothing to run today |

**Pruned (do not re-attack):** any 4₁ odd datum (symmetry-forced zero); any
anchor-invariant datum as the swing *value* (scope-(b) Lean); the winding
lattice, branch-point tuning, ratio/W_λ routes (prior scope-(b)); route 3's
substrate-q₀ is not session-closable (missing categorical level-N selection
principle — the open problem itself).

## Session results (updated as attacks land)

- **A3 LANDED (falsification confirmed, scope-(a)).**
  [`qbeta_5two_capstone_carrier_falsification_probe.py`](../../computations/probes/qbeta_5two_capstone_carrier_falsification_probe.py)
  + witness, 6/6: the 5₂ NZ-saddle bar-odd datum
  `B(q)=[𝔙(m=q)−𝔙(m=1/q)]/2` is smooth and **nonvanishing at q\***
  (`|B(q*)|=0.149`, 0 sign changes on a ±2e-8 grid straddling the anchor
  window); pushing the simple zero into the `u³` normalization's smooth
  factor would need log-slope ≈ 4×10⁸ (not smooth). Writhe data
  (capstone's writhe-2 **and** the corrected #3892 writhe-4 `½(q⁴−q⁻⁴)=0.43`)
  fail identically. **The capstone carrier is not the analytic NZ-saddle
  datum** — narrows to the categorical H₃(q) Markov-trace 𝔙_q (A5).
- **Braid landmine (respect in all 5₂ work):** the pre-#3892 corpus "5₂"
  braid `[1,1,1,-2,1,-2]` is actually **6₂** (det 11, writhe 2); canonical
  5₂ is `[1,1,1,2,-1,2]` (det 7, writhe 4). The capstone's
  `D_odd = ½(q²−q⁻²)` is the 6₂-era form; the corrected 5₂ datum is
  `½(q⁴−q⁻⁴) = sinh(2u_sub)`.
- **Classical bar-odd home already built:** `qbeta_5two_jones_barodd_probe.py`
  (validated TL₃ Kauffman bracket; `V(5₂)_odd ≠ 0`, O(1) at q₀,
  anchor-smooth — the bar-odd home, not the swing). A5's remaining core is
  the **categorical/quantum** 𝔙_q(5₂), which is H₃(q)-sized (B₃ braid), not
  H₅ as first beaned.

## Honest prize statement

Even a successful A1/A2 yields a **derived, anchor-independent bar-odd
fibre constant of 5₂** — which would make the *form* of the odd channel a
prediction and feed the Im 𝔙_q→N_odd capstone — but the Q_β *value*
remains experimental-Q_β-limited (the L2 100× target stays out of reach by
the measurement floor, per `MeasurementLimitedFloor.lean`). Comparison to
observed only; no ontological claims.
