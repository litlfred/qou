# ⁴He multi-nucleon interface operator — research state (2026-06-01)

**Date:** 2026-06-01
**PR:** TBD (claude/he4-multi-nucleon-interface-operator-2026-06-01)
**Status:** RESEARCH-STATE DOCUMENTATION (no closure attempt).
Updates research-queue item `research-multi-nucleon-interface-operator`.

## TL;DR

⁴He binding is currently predicted by `prop:magic-A-binding-formula`:

```
B(⁴He) = ρ_F · m_e · A · 8G   with A=4, ρ_F=2 (postulated)
       = 2 · m_e · 4 · 8G ≈ 29.956 MeV
       vs experimental:           28.296 MeV
       relative miss:             +5.87% (1.66 MeV)
```

This is dramatically better than the alpha-shift formula (-79% miss
per `prop:binding-alpha-shift-extension`) because alpha-shift assumes
a single hyperbolic force-carrier knot per nucleus — an assumption
that breaks for doubly-magic nuclei.

The **+5.87% residual** is the open derivation gap. Two structural
holes:

1. **Why `ρ_F = 2`** for ⁴He? The formula's `ρ_F` is currently
   postulated, not derived from substrate. Open conjecture
   `conj:magic-numbers-bring` references the Bring-magic-numbers
   chain; `prop:gravity-spectral-prefactor` references the `8G`
   universal residue prefactor. Neither pins `ρ_F = 2` from first
   principles.

2. **Why the +5.87% residual?** The magic-A formula treats the nucleus
   as `A` nucleons × universal residue `8G`, without any per-nucleon-
   interface correction. Per
   `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md`:
   "⁴He requires the multi-nucleon interface operator, not just the
   mirror" (referring to the A=3 mirror-pair structure that closes T
   / ³He per PR #1615 Option-E thread).

## What's been ruled out

| Mechanism | Status | Why |
|---|---|---|
| `B(A) = E₀ · q⁻ᴬ · Δtr · A(A-1)/2` | RETRACTED PR #1386 | Backhanded q-factorial fit; `Δtr(⁴He)/Δtr(D) = 0.67`, not the 12.7 the q-factorial implied |
| Single-nucleon Δ_λ derivation | RULED OUT per audit `2026-05-26-...` | Misses the multi-nucleon interface |
| q-dependent algebraic Δ_λ at Cat layer | RULED OUT per audit `2026-05-26-...` | Mixes Cat and Alg layers |
| Mirror-pair symmetry (Option-E v9) | DOESN'T APPLY to A=4 | No canonical mirror partner for ⁴He |

## What's UNTESTED but on the table

### Candidate 1: ρ_F = [2]_{q^(1/2)} at q_0

`[2]_{q^(1/2)} = q^(1/2) + q^(-1/2)`. At q_proton ≈ 1.110, this is
≈ 2.0021. **Surprisingly close to 2.**

But wait — that's a NUMERICAL near-match. Per CLAUDE.md "Don't propose
a seventh fit-based ansatz", a near-match to ρ_F = 2 without structural
justification is the trap.

Pre-stated failure signature: if `ρ_F = [2]_{q^(1/2)}` is wired, does
it close the +5.87% residual? Let me check numerically:

  At q_proton: [2]_{q^(1/2)} ≈ 2.00211
  Use in B(⁴He) = [2]_{q^(1/2)} · m_e · 4 · 8G
              = 2.00211 · 0.5110 · 4 · 8 · 0.91596... [Catalan]
              ≈ 29.988 MeV
              vs experimental 28.296 — **STILL +5.97% off**

So [2]_{q^(1/2)} doesn't close the gap — it just slightly shifts the
near-2 value. Mech NOT viable as the missing structure.

### Candidate 2: per-nucleon interface multiplier `(1 - δ_int)`

Where `δ_int` is an inter-nucleon interface deficit. Numerically:
`δ_int = 1 - B_exp/B_pred = 1 - 28.296/29.956 = 0.0554` (5.54%).

What's 0.0554 in substrate? Possibilities:
- `h² · q ≈ 0.0438 · 1.11 = 0.0486` (12% off — wrong)
- `(q-1)/q² ≈ 0.110/1.232 = 0.0892` (61% off — wrong)
- `ℏ_q² · [2]_q / 2 ≈ 0.0098 · 2.011 / 2 = 0.00984` (82% off — wrong)
- `h̃² ≈ 0.011` (80% off — wrong)

None hit cleanly. **Refutes per-nucleon `δ_int` as simple substrate
function.** Mech NOT viable.

### Candidate 3: Interface operator on H_3 × H_3 → H_6 (the ⁴He braid)

⁴He's atom braid `lithium6-canonical-3A` style (per PR #1289) for
A=4 would live in B_12 (4 nucleons × 3 strands). The "multi-nucleon
interface operator" would be the unitary mapping H_3 ⊗ H_3 ⊗ H_3
⊗ H_3 → H_12 with the appropriate Wedderburn restriction.

The dominant Wedderburn partition for ⁴He per PR #1289 audit is
`(4,4,4)` (rectangular) — confirmed PSD-dominant at d_λ=462. The
y_λ contribution from (4,4,4) at q_proton is +1.26e-6 (tiny). The
trace-dominant partitions for ⁴He are 2-row long-string partitions:
[9,3] 32%, [8,4] 26%, [10,2] 15%, [11,1] 11%, [7,5] 11% — total 95%
of |tr_M|.

The interface operator must respect this dominance structure. UNDERIVED.

**This is the actual research direction** but is genuinely research-grade
hard. Recorded in research-queue with the candidate-fishing trap
explicit.

## Recommended next-session attack (NOT this session)

1. **Identify the categorical operator** that produces the (4,4,4)
   Wedderburn PSD dominance at ⁴He from the H_3 ⊗ H_3 ⊗ H_3 ⊗ H_3
   tensor factorization. The Pieri rule + Littlewood-Richardson
   coefficients give a structured answer; the question is which
   restriction to the dominant block is canonical.
2. **Compare** the predicted ρ_F (= some categorical invariant of
   this restriction) at q_proton AND q_muon. Cross-anchor test
   per fibre/observable distinction (CLAUDE.md §Canonical chain
   2026-06-01 framing).
3. **If matches at both anchors AND has structural justification**:
   wire as conditional theorem extending magic-A-binding-formula
   to derive ρ_F.
4. **If not**: add as ruled-out mechanism #N to the audit list.

## Results of the H_3^4 Tensor Fusion Attack (2026-06-13)

Following the recommended attack, we computed the Littlewood-Richardson fusion of four bosonic nucleons: `[3] ⊗ [3] ⊗ [3] ⊗ [3]`. 
The results exactly recovered the trace-dominant 2-row partitions identified in PR #1289, plus a unique (4,4,4) block:
- **(9,3)**: multiplicity 10
- **(8,4)**: multiplicity 11
- **(10,2)**: multiplicity 6
- **(11,1)**: multiplicity 3
- **(7,5)**: multiplicity 9
- **(4,4,4)**: multiplicity 1 (unique)

This provides structural justification that the 2-row trace-dominance and the (4,4,4) PSD-dominance both emerge natively from the H_3^4 nucleon tensor product. However, extracting `ρ_F ≈ 1.8891` from these blocks (via ratios of dimensions, Wenzl traces, or LR multiplicities) failed to yield a canonical, structurally-justified q-dependent invariant. 
**Status:** The `H_3^4` tensor fusion correctly generates the H_12 topological support for ⁴He, but the scalar invariant `ρ_F` cannot be naively extracted from these multiplicities without falling into the "8th-ansatz fit-trap". This mechanism is recorded as incomplete/ruled-out for directly yielding `ρ_F`.

## Anti-pattern guard (CRITICAL)

DO NOT:
- ❌ Wire `ρ_F = [2]_{q^(1/2)}` as the derivation just because it's
  numerically near 2 (it doesn't even close the +5.87% residual)
- ❌ Search for a substrate function matching the 5.54% residual
  exactly — that's the 8th-ansatz fit-trap
- ❌ Restart the q-factorial ratio approach (already RETRACTED PR #1386)
- ❌ Promote magic-A-binding-formula's ρ_F=2 from postulated to
  derived without structural derivation

DO:
- ✓ Identify the categorical multi-nucleon interface operator from
  first principles
- ✓ Verify cross-anchor before any wiring
- ✓ Add ruled-out mechanisms to this audit list

## Cross-refs

- `content/quantum-observable-universe/mass-theory/magic-A-binding-formula.md` (current production formula)
- `docs/audits/2026-05-26-delta-lambda-binding-formula-closure.md`
- `conj:magic-numbers-bring` (conjecture for `ρ_F` derivation)
- `prop:gravity-spectral-prefactor` (8G universal residue)
- `prop:diagrammatic-double-magic-lr-fusion` (LR-fusion at doubly-magic)
- PR #1386 (RETRACTED q-factorial ratio attempt)
- PR #1289 (⁴He Wedderburn dominance: (4,4,4) PSD, [9,3]/[8,4]/[10,2]/[11,1]/[7,5] trace)
- `.beans/research-queue.json` — `research-multi-nucleon-interface-operator`
- CLAUDE.md §Canonical chain Im(q) fibre vs observable (2026-06-01)
