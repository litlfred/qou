# s5-so3 fiber-action keystone — combinatorial backbone VERIFIED; the functor is IDENTIFIED, its q-deformed closure is OPEN

> **Bean.** [`s5bb`](../../.beans/s5bb--s5so3-keystone-backbone-verify.md) (parent `qz9k`).
> **Discipline.** Formalize-first verification (decidable backbone only); critical-distance
> applied fairly. Corrects a stale framing in this session's own merged synthesis doc.

## 1. Correction to the merged synthesis doc (`#2345`)

[`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md)
(merged) described the keystone functor as "the open H₅→H₃ geometric fibre map … awaiting the
functor." That is **stale**. The 2026-06-13 functor-resolution audit
([`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md))
**identifies** the missing functor as the symmetric-group restriction **Res^{S₅}_{S₃}**
(geometrically: the Borromean 3-strand structure embedded in the 5-strand Bring color-tube).
The corrected status is three-tiered (§3 below): the functor is **identified**, its combinatorial
backbone is now **verified**, and its q-deformed closure is **open**.

## 2. What is now verified (self-checking compute, 14/14)

[`computations/probes/s5so3_branching_backbone_verify.py`](../../computations/probes/s5so3_branching_backbone_verify.py)
(witness `s5so3-branching-backbone-verify.witness.json`) verifies the *decidable*
(q=1 / classical-character) backbone of the functor-resolution doc:

| # | Claim | Method | Result |
|---|-------|--------|--------|
| C1 | `(3,2)↓S₃ = (3)+2(2,1)`; `(3,1,1)↓S₃ = (3)+2(2,1)+(1,1,1)`; **difference = (1,1,1)** | iterated removable-box rule (S₅→S₄→S₃) + dim checks | ✅ |
| C2 | `(3,1,1)↓A₅ = T₁⊕T₂` (hosts electron ℓ=1, T₁); `(3,2)↓A₅ = H`, `(2,2,1)↓A₅ = H` (host muon ℓ=2) | A₅ character inner products + **orthonormality self-check** on the A₅ table | ✅ |
| C3 | `χ^{(3)}(β_Bor)=1`, `χ^{(1,1,1)}(β_Bor)=1`, `χ^{(2,1)}(β_Bor)=2−3h⁴−h⁶` ⇒ **h⁴ lives exclusively in the (2,1) block** | exact 1-dim reps + an independent 2×2 Hecke rep (braid + Hecke relations **self-checked**) | ✅ |

`β_Bor = (σ₁⁻¹σ₂)³`, `h = q − q⁻¹`. C3 cross-checks the existing GAP-A-4 T15 result
(`χ^{(2,1)} = 2 − 3h⁴ − h⁶`) from an independent rep; the trace is basis-invariant, so no
Markov-convention drift enters. The "exclusively in (2,1)" conclusion follows because **both**
1-dimensional blocks evaluate to the constant `1` on the Borromean braid (no h-dependence).

## 3. The three-tier status

| Tier | Statement | Evidence |
|------|-----------|----------|
| **VERIFIED** | the combinatorial backbone — Res^{S₅}_{S₃} branchings, the (1,1,1) difference, the S₅↓A₅ generation indexing, and h⁴-localization in (2,1) | this compute (C1–C3) |
| **IDENTIFIED** | the functor is `Res^{S₅}_{S₃}`; ℓ=2 changes the Wedderburn trace weighting from the `(3,1,1)` to the `(3,2)` block over H₅(q) | resolution-doc §2–§3, now backbone-verified |
| **OPEN** | the q-deformed shift `E_{(3,2)}` vs `E_{(3,1,1)}` at q₀; the geometric `partition→A₅-rotation` map; whether the reweighting reproduces the 210 ppb muon tension | resolution-doc §4 (its own next-steps) |

## 4. Critical-distance note (fair reading)

Unlike the 2026-06-13 operator-branching doc's §5 ("Formal Resolution … closes CCR-9/CCR-10 …
1ppq gaps closed"), which this session flagged as overstated, the **functor-resolution doc is
appropriately scoped**: its title says "Identified", and its §4 lists the open obligations
honestly. Identifying the functor as Res^{S₅}_{S₃} *is* a genuine advance, and its combinatorial
content checks out (C1–C3). The remaining overclaim risk is only in conflating "functor
identified + backbone verified" with "210 ppb resolved" — which §4 itself does **not** do. The
q-deformed evaluation is the real open problem.

## 5. Link to `qkhc` (Q_β Stage C)

The same (1,1,1)-sign-block structure is the 2026-06-13 lead for the c_k ladder (proposed as an
`(1,1,1,1)` subtraction over H₄(q)). C3 here confirms the **q=1** value (`χ^{(1,1,1)}(β_Bor)=1`),
but recall the `qkhc` result
([`2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md)):
the c_k live in the **q-holonomic argument recurrence**, so a sign-block model for c_k must
reproduce that q-deformation, not just the classical χ=1 value — and must clear the refuted-class
C12 (trace-level) check. The backbone verified here is necessary, not sufficient, for the c_k lead.

## 6. Next concrete step (owner-gated)

Resolution-doc §4 step 2: evaluate the algebraic shift in the H₃(q) Markov trace induced by the
ℓ=2 (`E_{(3,2)}`) vs ℓ=1 (`E_{(3,1,1)}`) projector at q₀. This needs the H₅(q) Wedderburn
projectors (`pyhecke_native`; sandbox-blocked) and overlaps the merged GAP-A-4 chain — coordinate
before opening a probe branch. The formalize-first gate applies: any candidate shift must be
bar-even and anchor-stable, and must *derive* (not fit) the 210 ppb.

## 7. Cross-references

- [`2026-06-13-s5-so3-fiber-action-functor-resolution.md`](2026-06-13-s5-so3-fiber-action-functor-resolution.md) — identifies Res^{S₅}_{S₃} (backbone verified here)
- [`2026-06-13-gap-a4-operator-valued-muon-branching.md`](2026-06-13-gap-a4-operator-valued-muon-branching.md) — the §5 "closes" overstatement (this session's flag)
- [`2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md`](2026-06-16-mtau-and-binding-converge-on-s5so3-keystone.md) — the synthesis doc this corrects
- `S5SO3FiberAction.lean`, `GapA4MuonBranching.lean` — the keystone scaffold (open `partition_to_rotation` + `GenerationBranchingFunctor`)
- [`2026-06-16-qbeta-kernel-hunt-stage-c-scope.md`](../scope/2026-06-16-qbeta-kernel-hunt-stage-c-scope.md) — `qkhc` (the c_k sign-block lead's gate)
