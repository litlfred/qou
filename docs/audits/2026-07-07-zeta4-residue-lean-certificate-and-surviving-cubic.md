# ζ₄-residue odd-channel route — Lean certificate of the scope-(b) exclusion + the surviving cubic

**Date:** 2026-07-07
**Branch / PR:** `claude/c-3-request-x7eg34` / [#3467](https://github.com/litlfred/qou/pull/3467)
**Lean:** [`QOU/QBeta/QBetaZeta4ResidueRefutation.lean`](../../content/quantum-observable-universe/lean/QOU/QBeta/QBetaZeta4ResidueRefutation.lean) (5 lemmas, sorry-free, `lean`-direct exit 0)
**Hardens:** [`2026-07-04-zeta4-fibre-cyclotomic-refutation.md`](2026-07-04-zeta4-fibre-cyclotomic-refutation.md) (bean `0zr0`)
**Registry:** [`ck-dk-canonical-registry.md`](../coordination/ck-dk-canonical-registry.md) KC9 · **no tier change, nothing wired.**

## Task

Owner: "try the named route — the ζ₄-residue / complex-volume structure (KC9,
sibling #3437) feeding through KC18's Markov higher-crossing weight."

## Corpus-grep first (STRICT): the ζ₄-**residue** route is already refuted

Per the anti-over-claim discipline, before re-running I checked what is already
in the corpus. The ζ₄-**residue** route (the specific claim that the shared
ζ₄=i residue is `Φ₄ = q²+1`) was **refuted 2026-07-04, scope-(b)**, from both
ends:

- **s-adic level — vacuous** ([fixed-ring vacuity](2026-07-04-fixed-ring-vacuity-ladder-membership.md)):
  `Fix(σ) = ℚ(√3)[[ũ]] = ℚ(√3)[[h²]]` (one order-2 generator), so
  bar-even/odd ladder-*membership* is an identity. (This also flags the 08ds
  `h·D(ũ)+h³·F(ũ)` "refutation" as a truncation artifact, not structure.)
- **fibre-Laurent level — Φ₄ absent** ([ζ₄-fibre-cyclotomic](2026-07-04-zeta4-fibre-cyclotomic-refutation.md)):
  the ζ₄ *grading* holds (odd carrier supported on odd `q`-powers) but the
  ζ₄ *residue* does not — `(q²+1) ∤ num(q)`.

So the disciplined move is **not** to re-run a refuted numerical search. It is
to (i) **harden the refutation's cited invariant into Lean** (the refuted-
declaration discipline requires a scope-(b) exclusion to prove its invariant;
it previously lived only in a sympy witness), and (ii) **pin the surviving
open object**.

## The Lean certificate (this PR)

The bar-odd part of the net decay-width carrier is `Δ_odd(q) = num(q)/(4q⁷)`,
`num(q) = q¹⁴ − 5q¹² + 10q¹⁰ − 16q⁸ + 16q⁶ − 10q⁴ + 5q² − 1`. All lemmas are
exact `ring`/`linear_combination` identities over a generic `CommRing` (§7c):

| lemma | statement | meaning |
|---|---|---|
| `numOdd_factor` | `num = (q²−1)·R₁₂` | cyclotomic content is **exactly** `q²−1` (the trivial `Φ₁·Φ₂`) |
| `numOdd_phi4_quot` | `num + 64 = (q²+1)·Q` | exact division by `Φ₄` leaves constant remainder `−64` |
| `numOdd_at_phi4_root` | `q²+1 = 0 ⇒ num = −64` | at `q = i`, `num = −64 ≠ 0` ⇒ **`Φ₄ ∤ num`** — the ζ₄-residue is absent |
| `R12_eq_trace_cubic_shift` | `R₁₂ = (q⁴+1)³ − 4q²(q⁴+1)² + 3q⁴(q⁴+1) − 2q⁶` | division-free `R₁₂ = q⁶·C(q²+q⁻²)` |
| `R12_eq_cubic_trace` (`Field`) | `R₁₂ = q⁶·C(q²+q⁻²)`, `C(y)=y³−4y²+3y−2` | literal collapse to a **cubic in the trace variable** `y = q²+q⁻²` |

Independently cross-checked by exact integer/Laurent polynomial arithmetic
(no sympy needed): factorisation, the `−64` remainder, and the division-free
trace-cubic form all verify.

## What survives — the open object is a cubic, not a root of unity

The odd carrier's non-cyclotomic substance is the irreducible cubic
`C(y) = y³ − 4y² + 3y − 2` in the **bar-even loop-trace variable**
`y = q²+q⁻² = 2cosh 2λ` (S₃ Galois, disc `−152 = −2³·19`; real root
`y₀ ≈ 3.270 ⇒ q ≈ 1.71`). It is **not** a root-of-unity object (consistent with
the Φ₄ exclusion) and **not** a constituent-knot Jones invariant (2026-07-04
T1, scope-(a)). The remaining open Laurent/Habiro question — is `C(y)` a
knot-invariant specialization of the 14-strand net braid `Δ_net` (denominator
`4q⁷`)? — is now pinned to a concrete degree-3 object, the honest next target.

## §4 — the cubic is a **degree-3** obstruction, disjoint from every quadratic anchor

`C(y) = y³−4y²+3y−2` is monic with constant term `−2`, so (rational root
theorem) any rational root lies in `{±1, ±2}`. All four are nonzero —
`C(1)=−2, C(−1)=−10, C(2)=−4, C(−2)=−32` — so **`C` has no rational root and is
irreducible over `ℚ`**; its root generates a genuine degree-3 field. Every
substrate **quadratic** anchor sits at a *rational* trace value `y = q²+q⁻²`,
and `C` misses each:

| anchor | trace value `y = q²+q⁻²` | `C(y)` |
|---|---|---|
| golden `φ` | **3** (`φ²+φ⁻² = 3` exactly) | `−2` |
| silver `1+√2` | **6** | `88` |
| classical `q=1` | **2** | `−4` |
| `√3` (`q²=3`) | `10/3` | `16/27` |

A degree-≤2 substrate number can never be a root of an irreducible cubic, so
**no quadratic-anchor / real-q closure can resolve the odd carrier** — the
structural reason the KC-refuted real-q `c_3` class keeps failing: it searches a
degree-≤2 space for a degree-3 object. Any genuine odd-channel closure must
either supply the cubic field of `C` or route through the archimedean
evaluation (KC18), not a quadratic anchor.

These evaluations are Lean-certified (`cubicC_one/neg_one/two/neg_two`,
`cubicC_golden`, `cubicC_silver`, `cubicC_rrt_candidates_all_nonzero` — the
computational content of the RRT check; `lean`-direct exit 0).

**Numerical aside (NOT a claim, numerology-flagged).** `C(3) = −2` coincides
with the `c_3 → −2` q=1 shadow value; the golden anchor's trace value is exactly
`y = 3`. Recorded as a coincidence pending any derivation — it is *not* wired,
*not* a structural identification, and does not survive the corpus over-claim
gates as anything more than an observation.

## §5 — where the degree-3 comes from: the **Hopf (double-crossing) sector**

Probe [`qbeta_odd_carrier_sector_decomposition.py`](../../computations/qbeta/qbeta_odd_carrier_sector_decomposition.py)
→ [witness](../../computations/qbeta/qbeta-odd-carrier-sector-decomposition.witness.json)
(7/7, exact ℚ-Laurent arithmetic, no sympy/floats/fit) decomposes the bar-odd
carrier over the four **knot sectors** of the H₃ normal-form basis
`{𝟏, σ₀, σ₁, σ₀σ₁, σ₁σ₀, σ₀σ₁σ₀}` (reading the neutron/proton amplitudes
exactly from `free-neutron-decay.witness.json`):

| knot sector | crossings | bar-odd contribution in `y = q²+q⁻²` | arithmetic |
|---|---|---|---|
| virtual (σ₀, σ₁) | 1 | **0** | bar-even |
| trefoil (σ₀σ₁σ₀) | 3 | **0** | bar-even |
| unknot (𝟏) | 0 (identity) | `C_unknot(y) = 2y² − 7y + 4` | quadratic, disc `17`, `ℚ(√17)` |
| **Hopf (σ₀σ₁ + σ₁σ₀)** | **2** | **`C_Hopf(y) = y³ − 6y² + 10y − 6`** | **cubic, irreducible, disc `−76 = −2²·19`** |

with `C = C_Hopf + C_unknot` exactly. **The degree-3 field is sourced entirely
by the Hopf-link (double-crossing) sector**; the identity contributes only a
quadratic, and the odd-crossing sectors (virtual, trefoil) vanish. So the cubic
is **not** a 3-dim representation (H₃'s Wedderburn blocks are `1, 2, 1` — none
is 3-dim) and **not** a single knot invariant — it is specifically the
**2-crossing isospin amplitude difference** (refining the KC18 identification of
the odd channel with the Markov crossing term). The discriminant prime **19** is
shared by `C_Hopf` (`−76`) and the total `C` (`−152 = −2³·19`) — the arithmetic
fingerprint of the sector.

Lean-certified y-level identities (`cubicC_sector_decomp`,
`cubicC_Hopf_rrt_candidates_all_nonzero`, sorry-free); the amplitude-level
sector attribution is the exact-arithmetic witness above.

**Consequence for the search.** The productive remaining direction for the c_3
odd channel is the **Hopf-sector cubic field** (the disc-`19` `S₃` object)
routed through the archimedean evaluation (KC18) — **not** a fibre real-q /
quadratic-anchor formula (excluded, §4), and **not** a ζ₄-residue (excluded,
§1–§3). Any candidate must supply the cubic field of `C_Hopf`.

## Discipline

Scope-(b) exclusion (cited invariant: the exact ℚ[q] factorisation, now
Lean-certified). No `c_k` value, no fit, no wiring, no registry tier change
(flip-flop guard §8). The bar-odd `c_3` channel remains open; this narrows,
does not close it — and now **localises** it to the Hopf-sector cubic.

## Cross-references

- ζ₄ refutation (the invariant this certifies): [`2026-07-04-zeta4-fibre-cyclotomic-refutation.md`](2026-07-04-zeta4-fibre-cyclotomic-refutation.md)
- KC18 Markov eval-map: [`2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md`](2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md)
- complex-volume conjecture (sibling #3437): [`conj:binding-qbeta-complex-volume`](../../content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.md)
- Im(q) fibre-vs-observable wall: AGENTS.md §"Im(q) at fibre vs observable level"
