# ⁴He ν_SDP = 2, not 3 — the monotone {sc(n)=A−1} family is refuted by binding (2026-08-02)

Branch `claude/q-deformed-saddle-offsets-bdn992` (PR #4598). Resolves bean qou-k2xr,
the decisive datum flagged in `2026-08-02-ppq-attack-vectors-roast.md` §Roast 2.

## The question

Agent 5's ν_SDP survey found every honest categorical count collapses to
sc(n) = #self-conjugate blocks = #partitions into distinct odd parts, and that
**sc(3A) = A−1 (the Lean-proved bond count) for all A ≤ 6** — so on the census-knot
data {²H:1, ³H:2, ³He:2} ν_SDP is indistinguishable from the bond count A−1. Every
such *monotone* count predicts **⁴He ν_SDP = 3** (sc(12) = A−1 = 3). But the corpus
*assumes* ρ_F(⁴He) = 2 (extrapolated, no census knot). ⁴He is the decisive datum: 3
kills-or-saves the whole monotone family.

## The arbiter: ⁴He binding data

⁴He has no census knot; the corpus uses the doubly-magic closure
(`magic-A-binding-formula.md`):

  `B(⁴He) = ρ_F · m_e · A · 8G`,  `8G = Vol(L6a4) = 7.32772` (Catalan),  `A·8G = 29.311`.

Here **ρ_F IS the ν_SDP in question** (the magic-regime structural prefactor;
`conj:kashaev-density-equals-sdp-multiplicity` identifies ρ_F = ν_SDP). So the
experimental binding independently pins it:

| ρ_F | B_pred (MeV) | vs B_AME = 28.296 |
|-----|--------------|-------------------|
| 1 | 14.98 | −47.1% |
| **2** | **29.96** | **+5.9%** |
| 3 | 44.93 | **+58.8%** |

**Data-implied ρ_F(⁴He) = B_AME/(m_e·A·8G) = 1.889 → 2.** Accounting for the
Coulomb repulsion (Z=2 reduces the observed binding; adding back ~0.8 MeV of strong
binding) pushes the strong-only ρ_F to ≈ 1.94 — closer still to 2, and further from 3.

## Verdict (scope-(a))

**⁴He ν_SDP = 2, decisively NOT 3.** ρ_F = 3 overshoots the binding by +59%; no
reading of the data supports 3.

Consequences:

1. **The monotone family {sc(n) = A−1} is REFUTED.** It predicts 3; the data says ~2.
   So ν_SDP is **not** the bond count A−1 in disguise — the sc(3A) = A−1 degeneracy
   (Agent 5 / Roast 2) is a *mathematical coincidence that breaks at the first
   doubly-magic nucleus* (A=4), not at A=7 as the pure partition-count divergence
   suggested. The binding is the physical arbiter the pure count could not provide.
2. **ν_SDP is regime-dependent, not a single monotone count.** It equals A−1 (= sc(n))
   for the linear-chain census-knot atoms (²H, ³H, ³He), but the **doubly-magic**
   ⁴He — a closed shell, not a linear chain — has its own ρ_F ≈ 2. This is physically
   coherent: the corpus *already* switches from the census-knot volume to the magic
   `A·8G` closure precisely because the linear-chain bond picture fails at ⁴He
   (`magic-A-binding-formula.md`: "an assumption that breaks for doubly-magic nuclei").
   So ⁴He was never in the domain of the A−1 count.

## Sub-roast (honesty)

ρ_F(⁴He) = 2 is **not derived** — the magic-A block states "the derivation of the ρ_F
prefactor … remain[s] open." And the data-implied value is **1.889**, not the integer
2; the corpus rounds. The 6% residual (1.89 vs 2) is absorbed by Coulomb + the fact
that `A·8G` is a *magic-volume proxy*, not a real hyperbolic knot volume. So "2" is a
corpus-rounded empirical prefactor for ⁴He, and whether the true ν_SDP(⁴He) is the
integer 2 or a non-integer ~1.9 (which would itself break the ν_SDP ∈ ℤ_{>0}
identification) is not settled by this. What IS settled: it is ~2, and **3 is
excluded.**

## Net for the ν_SDP program

- The elegant "ν_SDP = bond count A−1" reframing (Roast 2) is **wrong past the
  linear-chain regime** — refuted at the first test (⁴He).
- ν_SDP is regime-dependent: a bond count in the linear-chain regime, a magic-closure
  prefactor in the doubly-magic regime. A single categorical count for both is
  **not** in the corpus and would have to reproduce the regime switch — a harder
  target than "which integer."
- This does not close `conj:kashaev-density-equals-sdp-multiplicity`; it removes a
  false simplification and sharpens the open problem to: *derive the regime-dependent
  ρ_F (A−1 vs ~2) from the confinement structure.*

## Orthogonality note (coordination)

The concurrent sibling A=4 work
(`2026-08-02-a4-interface-magnitude-one-scalar-gate.md`,
`A4InterfaceMagnitude.lean`, merged to main) concerns the Δ_λ **magnitude** scalar
`m` (the ⁴He complete-graph interface operator `det(I+G) = (1−5m²)(1−m²)`, a one-scalar
reachability gate) — a *different* quantity from the ρ_F integer prefactor treated
here. The two are complementary (magnitude vs multiplicity); no overlap.
