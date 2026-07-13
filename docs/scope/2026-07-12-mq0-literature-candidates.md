# m(q₀) assignment — literature candidate survey

**Date:** 2026-07-12 · **Axis:** c₃ bar-odd S geometric instantiation
(`conj:algebraic-geometric-dilog-equivalence`; the open instantiation of
`QOU.QBeta.BarOddLadderShape`, PR #3660). · **Tier:** literature scoping —
no candidate is wired, probed, or endorsed here; each is mapped onto the
merged falsification kit.

## The slot being filled

A categorical assignment `q₀ ↦ m` (figure-eight meridian holonomy,
`u_h = 2 log m`) with `Im 𝔙(m(q)) = A(q)/u(q)³` (NZ-leading
`(√3/2)|u_h|² sin 2φ`). The kit any candidate must pass:

| gate | requirement | source |
|---|---|---|
| **G1 values** | `S(μ) = +0.00968298`, `S(p) = −0.03945936` | S-leak audit |
| **G2 floor** | `\|u_h\| ≥ √(2\|S\|/√3)` (proton: `2.05·t`) | #3562 M1 |
| **G3 derivative** | `u³·d/dq[Im 𝔙(m(q))] = A′ ≈ +2.37` at one anchor | #3621 |
| **G4 zero** | `m(q*)` on the real-meridian locus (`Im 𝔙 = 0` at q*, 80.3 % muon-ward) | q* probes |

Excluded already: smooth substrate phases, pole-seeding basins,
gluing-variety branch points, anchor-blind |u| = O(t) laws.

## Candidates

### C1 — Gukov parametrized volume conjecture (color/coupling ratio)

**Mechanism.** `J_N(e^ℏ)` with `u = Nℏ` held fixed; asymptotics live on the
A-polynomial curve with meridian eigenvalue `m = e^{u/2}`; the growth rate is
the u-deformed `Vol + iCS`. Refs: Gukov, *Three-Dimensional Quantum Gravity,
Chern–Simons Theory, and the A-Polynomial* (hep-th/0306165); Dimofte–Gukov,
*QFT and the Volume Conjecture* (1003.4808); *Volume Conjecture: Refined and
Categorified* (1203.2182).

**QOU shape.** `u_h = N·t` with `t = ln q₀` and `N` a categorical color
(e.g. H₃ strand/irrep datum). **Prognosis:** real `u_h` ⇒ `Im 𝔙 = 0`
identically — fails G1 unless the color is complexified (the fibre-level
Im q / ζ₄ channel). By itself: dead; as the real part of C2: load-bearing.

### C2 — Murakami deformed VC (root-of-unity deviation)

**Mechanism.** `J_N` at `q = exp((u + 2πi)/N)`: the limit gives `Vol + iCS`
of the u-deformed (incomplete) structure — a *theorem-grade* explicit
`parameter ↦ m` dictionary for 4₁. Refs: H. Murakami, *…figure-eight knot
and its Dehn surgery spaces* (math/0401084); Murakami, *CS invariant +
Reidemeister torsion of 4₁* (1102.3530); *asymptotics at a real number*
(2109.04664); overview (1002.0126).

**QOU shape.** `u_h` = the log-deviation of the substrate evaluation point
from the nearest root of unity — complex BY CONSTRUCTION (real substrate
offset + imaginary RoU part). Matches #3543's "phase accumulates like a
root of unity" diagnosis; the lever class could enter if the effective `N`
is tied to the ladder rung (`N ~ u⁻³`-scale winding). **Prognosis: the
structurally richest candidate.** Needs: the categorical selection of `N`
(no fit) before any evaluation — formalize-first item.

### C3 — Andersen–Kashaev / Hikami state-integral saddle (Φ_b-native)

**Mechanism.** The 4₁ invariant as a Φ_b state integral; its saddle-point
equation IS the gluing system, and the meridian datum enters as the
integration variable / angle at the saddle. Refs: Kashaev, *hyperbolic
volume from quantum dilogarithm* (q-alg/9601025); Hikami (math-ph/0105039;
math/0604094 — already the corpus's evaluator-validation source); recent:
*VC and quantum hyperbolic invariants: 4₁* (2604.16077), SIGMA 26-002.

**QOU shape.** `m` read off the saddle of the state integral **at the
substrate `b = substrateB(t)`** — every ingredient already built and
validated in-repo (`phi_b_evaluator`, `phiBProd`, battery to 1e−39).
**Outcome (probe `qbeta_c3_phib_quantum_saddle_probe.py`, stage-0):** the
φ-space evaluator machinery validates (V1/V2 to 1e−37/1e−72), but the
saddle stage is **blocked on a branch prescription**: the saddle arguments
sit outside the fundamental strip, where the periodic product-series branch
(Hikami's classical potential) and the quasi-period continuation (the true
Φ_b) differ by a winding factor of size O(2π²/t) ≈ 190 at substrate γ —
the argument-identification question in sharpened, localized form. Fast
G2 prognosis either way: the u = 0 saddle displacement is O(|γ|) = t/2 ≈
0.05, **~2–4× under the feasibility floor** — the u = 0 candidate is
expected to fail regardless; the u ≠ 0 boundary-parametrized integral is
the live continuation.

### C4 — Quantum A-polynomial / AJ annihilator (recurrence kernel)

**Mechanism.** The q-difference operator annihilating the colored Jones
(AJ conjecture) quantizes the A-polynomial; its characteristic roots at the
substrate give holonomy candidates. Refs: the AJ/quantum-VC framing in
1003.4808 §"quantum volume conjecture"; regulator/character-variety view
(math/0604057).

**QOU shape.** Overnight main landing (GAP-3 currency): the recurrence
kernel `R(q,x) = x² − τx + 1` is already derived + formalized in-corpus;
its roots are the knot-operator eigenvalues `e^{±iθ(q₀)}` — but θ is
anchor-smooth (#3600), so C4 alone fails G3; it supplies the *carrier*
(as does the Hopf cubic), not the lever. Compose-only candidate.

## Recommended order (probes, all fit-free)

1. **C3 saddle solve** at `substrateB(t)` for both anchors → run the kit.
   Cheapest decisive test; all infra merged.
2. **C2 dictionary**: formalize the RoU-deviation `u_h` and the categorical
   `N`-selection question (formalize-first — prune before scanning `N`).
3. C1/C4 only as components of the above (real part / carrier).

## Sources

- https://arxiv.org/abs/hep-th/0306165 · https://arxiv.org/abs/1003.4808 ·
  https://arxiv.org/abs/1203.2182
- https://arxiv.org/abs/math/0401084 · https://arxiv.org/abs/1102.3530 ·
  https://arxiv.org/abs/2109.04664 · https://arxiv.org/abs/1002.0126
- https://arxiv.org/abs/q-alg/9601025 · https://arxiv.org/abs/math-ph/0105039 ·
  https://arxiv.org/abs/2604.16077
- https://arxiv.org/abs/math/0604057 · https://arxiv.org/abs/math/0603217
