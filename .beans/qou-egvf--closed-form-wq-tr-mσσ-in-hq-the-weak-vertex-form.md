---
# qou-egvf
title: 'closed form: W(q) = tr_M((σ₁σ₂)⁵) in H₃(q) — the weak-vertex form factor, Wedderburn-derived under convention D'
status: completed
type: task
priority: normal
created_at: 2026-09-04T12:58:15Z
updated_at: 2026-09-04T13:16:39Z
---

Follow-on to qou-jk6k's one-level-down GAP. Exact result (sympy, convention D: h = q − 1/q, z = q³/(q²+1), Ocneanu basis values [1,z,z,z²,z²,hz²+z]):

  tr_M((σ₁σ₂)⁵) = q²(q¹² + q⁸ − 1)/(q² + 1)²

Wedderburn: (σ₁σ₂)⁵ = Δ²·(σ₁σ₂)², Δ² trivial on (2,1) (content sum 0), χ₍₂₁₎((σ₁σ₂)⁵) = −1 (eigenvalues ω, ω̄), χ₍₃₎ = q¹⁰; weights y₍₃₎ = (q⁴+1)/(q²+1)², y₍₂₁₎ = q²/(q²+1)², y₍₁₁₁₎ = 0 (SU(2)-type, as convention D is TL). Cross-check: numerator q²(q¹²+q⁸−1) = q²²·V_{T(3,5)}(q⁻²) with V = t⁴+t⁶−t¹⁰ (10_124). W(q₀) ≈ 1.18748 at the proton pin.

Finding: the published W(q₀) ≈ 0.7036 in obs/hadron-half-life-verification.md is reproduced by NEITHER convention (D 1.1875, C 0.9063); its source is the deprecated convention-C hecke_division pipeline (computations/_deprecated/t35-full-calculation.py, (σ₃σ₄)⁵ on 5 strands). Content NOT edited here — published-value change, owner pass needed (same posture as the fig-8 0.182→0.280 case).

Plan: Lean carrier on Archimedean/HeckeH3 seminormal matrices (Wedderburn functional, six basis values, closed form); producer computations/markov/weak_vertex_t35_trace.py via the canonical tr_M_word at the proton pin + witness; audit note.


## Result (2026-09-04)

DONE on branch claude/weak-vertex-t35-trace-2026-09-04:
- Lean QOU/Braiding/WeakVertexT35TraceClosedForm.lean (sorry-free, lean-direct exit 0, axioms propext/choice/Quot.sound only): seminormal (2,1) matrices + relations, (σ₀σ₁)³ = 1 on (2,1), χ₂₁((σ₀σ₁)⁵) = −1, six Ocneanu basis values of the Wedderburn functional (y3=(q⁴+1)/(q²+1)², y21=q²/(q²+1)², y111=0), weakVertexTrace_eq, Jones identity numerator = q²²·V_{10_124}(q⁻²), W(1)=1/4, 1.187 < W(q₀) < 1.188.
- Producer computations/markov/weak_vertex_t35_trace.py → weak-vertex-t35-trace.witness.json, 9/9 assertions, proton pin stamped. W_D(q₀) = 1.18748061314596264610711583007920…; W_C = 0.9063… (labelled comparison).
- Audit docs/audits/2026-09-04-weak-vertex-t35-trace-closed-form.md with the owner decision frame on the published 0.7036 (reproduced by neither convention; source = deprecated C hecke_division pipeline; NOT reproduced this session; content NOT edited).

Still open (owner): whether to replace 0.7036 / '11 % reduction' in obs:hadron-half-life-verification and close item 2 of rem:hadron-half-life-fermi — recommendation option 1 as a follow-on tranche with the half-life table re-derived in the same edit.


PR #6664 opened 2026-09-04 (lean 41f39732ceb, audit fc1cf16306a, producer c1ee4cf0aa1). Precision gates: red rows all pre-existing corpus baselines, none naming the new files. Waiting on owner merge permission; the content-block correction (0.7036 → 1.1875 + item 2 of the Fermi remark) is the framed follow-on decision, not done here.
