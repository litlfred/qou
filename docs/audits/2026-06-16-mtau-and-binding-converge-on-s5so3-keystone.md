# m_τ Path A + categorical binding both reduce to the s5-so3 keystone (redirect)

> **Beans.** [`mtxi`](../../.beans/mtxi--mtau-path-a-operator-branching.md) (option 2, m_τ),
> [`g3pl`](../../.beans/g3pl--gap-a3-binding-converges-s5so3.md) (option 3, binding) — parent `qz9k`.
> **Discipline.** Corpus-grep (done — this redirect *is* the result of it): both tasks turn out
> to be largely **already-run / underdetermined**. NO fitting. Reports a redirect to the live
> keystone + one critical-distance flag, not a fresh probe.

## TL;DR

The user picked "pursue m_τ Path A" (option 2) and "open the GAP-A-3 P_λ probe" (option 3).
Corpus-grep shows **both are subsumed by a single already-localized open object** — the
**S₅↔SO(3) fibre action** (`conj:s5-so3-fiber-action`). Re-running a GAP-A-3 probe, or
attacking m_τ via the per-braid ξ_ℓ(q) Path A, would redo refuted / known-underdetermined
work. The genuine open keystone is the **geometric fibre map / cross-algebra functor
H₅(q)→H₃(q)**, and the live concrete attack on it is the 2026-06-13 operator-valued
branching — whose "closes the gaps" framing is **overstated** (see §4).

## 1. Option 3 (GAP-A-3 binding P_λ) — already run + the axis is closed

- The GAP-A-3 §4 spin channel `P_λ(D)=m_{1/2}(λ)^4` was **run and REFUTED** (rel_err **3211×**;
  `computations/probes/gap_a3_deuteron_mixed_plethystic_probe.py`, witness assertion
  `mixed_plethystic_m_half_fourth_power_refuted_as_expected`, 2026-06-05, PR #1870).
- The **GAP-A-4 mass-multiplier axis is CLOSED across all probe layers** — 4 transplant
  routes R1–R4 refuted, **22 no-fit closures** total
  ([`2026-06-05-gap-a4-final-retrospective.md`](2026-06-05-gap-a4-final-retrospective.md) §2,§6;
  T2–T18 probe arc in `computations/probes/gap_a4_*`).
- The retrospective's verdict: *"The framework's open derivation math is now reduced to one
  categorical conjecture"* — `conj:s5-so3-fiber-action` (the τ-image Dirac/SW PDE).

**⇒ Do NOT open a fresh GAP-A-3 P_λ workplan.** The binding-side open math = the keystone (§3).

## 2. Option 2 (m_τ Path A, ξ_ℓ derivation) — underdetermined + partially superseded

A fresh corpus-map of the per-braid mass tower (this session) found:

- `Vol_q^tower(K)` is a Markov-trace Laurent polynomial (electron ≈ 0.628, muon ≈ 0.857 at q₀),
  **not** the Jones polynomial or hyperbolic volume
  ([`mass-endomorphism-tower.md`](../../content/quantum-observable-universe/mass-endomorphism/rho-k-graded-expansion.md) chain).
- The lepton per-generator `V̂_i` values are **unpublished** (only the H₃ atomic case is), and the
  witness `f-ell-derivation-via-per-braid-mass-tower` records **"FAR — >50% from CODATA; the
  per-braid mass tower with PROTON V̂_i does NOT give the muon mass."**
- The stated constraints (bar-symmetry `P_avg`, Im(q)-robustness, Kashaev recovery, the three-cal
  consistency `F_e(q₀)=1`, `F_μ(q₀)=206.77`) are **necessary but not sufficient**: bar-even
  functions form an infinite subring, and Kashaev recovery pins only the `q→1` limit. The corpus
  offers **no candidate functional form** for ξ_ℓ.

**⇒ Path A is structurally underdetermined; only the forbidden Path-B fit would "close" it.** The
live lepton-mass framing is no longer ξ_ℓ·Vol_q^tower but the **operator-valued generation
branching** (§3): electron = ℓ=1 → icosahedral T₁ ⊂ S₅ block (3,1,1); muon = ℓ=2 → H ⊂ (3,2);
**tau = ℓ=3** (SO(3)↓I of the dim-7 harmonic). All three need the same open functor.

## 3. The keystone both reduce to: `conj:s5-so3-fiber-action`

`S₅ ⊃ A₅ ≅ I ⊂ SO(3)` ties the partition-wise Wedderburn action on H₅(q) (combinatorial) to
SO(3) rotations on Bring's quintic surface (geometric). Formalized as a **scaffold + conditional
class** with the **geometric fibre map left OPEN**:

- [`S5SO3FiberAction.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/S5SO3FiberAction.lean)
  — partitions-of-5 indexing + `dim² = |S₅| = 120` check; *"the geometric realization (mapping each
  partition of 5 to a specific A₅ rotation on Bring) is the open structural step."*
- [`GapA4MuonBranching.lean`](../../content/quantum-observable-universe/lean/QOU/BraidsAndKnots/GapA4MuonBranching.lean)
  — `GenerationBranchingFunctor.project : H5 → H3` (the cross-algebra functor) and `GapA4MuonMass`
  (the Wedderburn-correction structure) — both **abstract classes / structures awaiting the
  functor**.

This is the **single open object** for: per-atom mass multiplier λ(K) (GAP-A-4), per-partition
binding Δ_λ (GAP-A-3), and the lepton tower ξ_ℓ / m_τ (option 2). They are one problem.

## 4. Critical-distance flag — the 2026-06-13 "Formal Resolution" is overstated

[`2026-06-13-gap-a4-operator-valued-muon-branching.md`](2026-06-13-gap-a4-operator-valued-muon-branching.md)
§5 ("Formal Resolution: The Exact (1,1,1) Sign-Block Subtraction") states the difference between
the electron and muon fibre traces is the exact removal of the sign rep (1,1,1), with
`χ^{(1,1,1)}(β_Bor) = ((-q)(-q^{-1}))^3 = 1`. **The identity is correct** (sign rep `σ_i↦-q^{-1}`,
`σ_1^{-1}σ_2 ↦ (-q)(-q^{-1}) = 1`, cubed = 1). **But the surrounding "closes" language overclaims:**

- §5 ("closes precision gaps CCR-9/CCR-10 by proving…", "1ppq gaps closed") is **in tension with
  the same doc's §4** ("Next Steps & Proof Obligations": *compute the Wedderburn action, derive the
  functor `conj:s5-so3-fiber-action`, prove analytic closure of the 210 ppb shift*). §4 says the
  thing is open; §5 says it is closed.
- §5.3 itself hedges ("the c_k recursion ladder … **likely** map to the … (1,1,1,1) sign-block over
  H₄"). A single exact trace value (`χ=1`) is **necessary, not sufficient**: resolving the 210 ppb
  muon gap needs the *correction factor* `F(E_{(3,2)}, q₀)` of §3, which needs the **open functor**.

**Read §5 as a promising candidate mechanism, not a closure.** Per the canonical-no-negative /
tiered-reporting discipline, "exact (1,1,1) subtraction" is at most a **lead** until it passes the
formalize-first gate (§5).

## 5. Link to this session's `qkhc` (Q_β Stage C)

§5.3 proposes the **c_k ladder as exact (1,1,1,1) sign-block subtraction over H₄(q)**. This is a
*candidate Stage-C mechanism* for the kernel R(q,ξ) of
[`qkhc`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md) — and it must clear the
**formalize-first gate** before counting:

1. **Refuted-class check.** A 1-d-block trace subtraction over H₄ is adjacent to **C12**
   (trace-level Markov-stabilization, refuted, PR #1850) — show it is *not* a C12 member
   ([`refuted-class-map`](2026-06-04-qbeta-ck-refuted-class-map-and-open-axis.md)).
2. **Anchor-stability** (proton+muon swing < 1%) and **bar-evenness** (`q↦q⁻¹`) — the χ=1 value is
   bar-even and anchor-independent (promising), but the *full* `Σ_λ W_λ χ^λ(β)` correction must be
   too. Recall (this session's `qkhc` result): the c_k live in the **q-holonomic argument
   recurrence**, so any sign-block model must reproduce that, not a constant-coefficient ladder.

## 6. Recommended next step (single keystone, owner-gated)

The productive direction for **all three** (m_τ, binding Δ_λ, mass λ(K)) is the **geometric fibre
map of `conj:s5-so3-fiber-action`** — discharging the `GenerationBranchingFunctor.project : H5→H3`
class with a derived functor (mapping each partition of 5 to an A₅ rotation on Bring's surface),
then evaluating the Wedderburn correction. This is multi-session, owner-gated research that
overlaps the merged GAP-A-4 chain + `conj:s5-so3-fiber-action`; coordinate before opening a probe
branch. **Not** a per-braid ξ_ℓ fit, **not** a 7th Δ_λ ansatz, **not** a GAP-A-3 re-run.

## 7. Cross-references

- [`2026-06-05-gap-a4-final-retrospective.md`](2026-06-05-gap-a4-final-retrospective.md) — 22 closures → one conjecture
- [`2026-06-13-gap-a4-operator-valued-muon-branching.md`](2026-06-13-gap-a4-operator-valued-muon-branching.md) — the live attack (§4 flag above)
- [`2026-06-04-gap-a3-brane-tower-level-selection-scope.md`](2026-06-04-gap-a3-brane-tower-level-selection-scope.md) — the GAP-A-3 P_λ scope (channel refuted)
- [`lepton-mass-tower-canonical.md`](../../content/quantum-observable-universe/mass-theory/lepton-mass-tower-canonical.md) — Path A (ξ_ℓ underdetermined)
- `S5SO3FiberAction.lean`, `GapA4MuonBranching.lean` — the keystone formalization (open functor)
- [`2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md) — `qkhc` (the sign-block c_k lead must clear its gate)
- [`2026-06-16-koide-tau-forcing-assessment.md`](2026-06-16-koide-tau-forcing-assessment.md) — `k9td` (Koide stays a fit; QOU's real generation structure is the icosahedral ℓ-degree, not Z/3)
