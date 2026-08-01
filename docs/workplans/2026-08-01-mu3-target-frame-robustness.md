# Work-plan — is the μ₃ (A=3 magnitude) target frame-robust?

**Branch:** `claude/mu3-target-frame-robustness-2026-08-01` · **Axis:** Δ_λ / A=3
magnitude gate · **Discipline:** frame-artifact detection, honest scope, no fit.

## Question

The A=3 magnitude gate is stated as a **1.6× gap**: the categorical 3-body handle
`c₃ ≈ 0.63·μ₃`, where the target is

    μ₃ = M(3) − 3·μ₂ = M(3) − 0 = ρ_strong(3) − ρ_grad(3) ≈ +0.4708,

the 3-body simplex coefficient of the graded-subtracted residual
`M(A) = ρ_strong(A) − ρ_grad(A)`, `ρ_grad(A) = [A]_q!/[2]_q!`
(`deltalambda_kappa_interface_residual_simplex_probe.py`).

**μ₃ is a residual after a baseline subtraction** — exactly the structure that made
`g₂ = 1 + r` frame-flattered (r swung 12× under equally-motivated conventions;
PR #4319 thread). Every sibling is trying to *close* the 1.6× gap **assuming μ₃ is
the target**. No one is asking: **is μ₃ = 0.4708 itself frame-robust, or is the
"1.6× gap" an artifact of the baseline `ρ_grad` / simplex-basis convention?**

## What is genuinely frame-independent vs convention-dependent

- **Frame-INDEPENDENT (physical):** the AME ratios `ρ_strong(A) = B(A)/B(²H)`
  — fixed data, no convention.
- **Convention-DEPENDENT (the two knobs):**
  1. the **baseline** `ρ_grad(A)` (here `[A]_q!/[2]_q!`) subtracted to form `M(A)`;
  2. the **basis** `C(A,k)` (edges/triangles/tetrahedra) the residual is expanded in.

μ₃ is fully determined by `M(3), M(4)` and the basis (a fixed 3×3 linear solve once
μ₂ = M(2) = 0 is imposed). So the only freedom is knobs 1–2. **Test whether μ₃
swings under equally-motivated choices of each.**

## Steps (microcommits)

1. **[this]** work-plan.
2. **Probe** `mu3_target_frame_robustness_probe.py` — compute μ₃ under the canonical
   `ρ_grad = [A]!/[2]!` AND under 3–4 alternative-but-equally-valid baselines
   (`[A]_q` linear, `q^{binom}` area-law, symmetric `[A]_q!/([2]!)` variants, no
   subtraction) × alternative simplex conventions (include-μ₂-free vs
   deuteron-forced). Report the **spread** of μ₃ and of the implied gap ratio
   `c₃/μ₃`. Exact (mpmath), audit-only, q₀ from the muon-canonical layer.
3. **Audit doc** — honest verdict:
   - **robust** (μ₃ spread ≪ the 1.6× gap) ⇒ mild confirmation the gate is
     well-defined; the 1.6× is a real target. Scope-(a) positive.
   - **swings** (μ₃ spread ≳ the gap) ⇒ major reframing: the "1.6× A=3 magnitude
     gap" is baseline-convention-dependent, like g₂'s r. Scope-(a); redirect the
     sibling closure attempts.

## Scope

DERIVED: a frame-robustness measurement of the μ₃ target (spread under
equally-motivated baseline/basis conventions). NOT a closure of the gap; NOT a new
weight. AME enters only as fixed targets — never inverted. No fit; nothing wired.
