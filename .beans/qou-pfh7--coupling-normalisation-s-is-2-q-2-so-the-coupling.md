---
# qou-pfh7
title: 'coupling normalisation: s² IS [2]_q − 2, so the coupling is a classical-value deviation — and W − W(1) vanishes at the wrong ORDER'
status: completed
type: task
priority: normal
created_at: 2026-09-05T06:17:05Z
updated_at: 2026-09-05T06:26:29Z
---

Owner "merge and coupling renorm" (2026-09-05). The open item qou-ix74 left: what normalisation relates the derived weak-vertex trace W(q) to the single-crossing coupling s² the decay rate actually uses.

Entry measurement (sympy, exact) — the pattern is DERIVED, not assumed:
- s² = (q^{1/2} − q^{−1/2})² = [2]_q − 2 EXACTLY. So the corpus's own single-crossing coupling is the q-dimension MINUS ITS CLASSICAL VALUE, [2]_1 = 2. That is what makes it vanish at q = 1 and stop beta decay classically, and it is the pattern any W-based replacement must follow.
- W(1) = 1/4 and W'(1) = 5, so W − W(1) vanishes to FIRST order in (q−1): W − 1/4 = 5(q−1) + (93/4)(q−1)² + …
- s² vanishes to SECOND order: s² = (q−1)² − (q−1)³ + …

So the two objects have different vanishing orders, which is a structural obstruction no q-independent constant can fix, and it prunes the whole family c·(W − W(1)). An order-matching bridge needs one factor vanishing as (q−1) (h, ℏ_q, s, q−1 are the corpus's candidates).

Plan: Lean the identity and the two vanishing orders (formalize-first pruning); probe the order-matched bridge candidates and report the residual honestly; audit doc. Do NOT fit a coefficient.


## Result (2026-09-05)

Branch `claude/weak-vertex-coupling-normalisation-2026-09-05`. One positive, one proved negative.

**POSITIVE — s² is derived, not conventional.** s² = (q^{1/2} − q^{−1/2})² = [2]_q − [2]_1 EXACTLY: the decay-rate coupling is the SU_q(2) fundamental dimension minus its classical value, which is why the rate vanishes at q = 1. First derivation of the SHAPE of s² in the corpus. Lean `sSq_eq_twoQ_sub_two`. This is what motivates the candidate family c·(W − W(1))·X — motivation derived, not assumed, so it is not the defined-residual failure mode.

**NEGATIVE — that family is excluded, scope-(b).** s² vanishes to 2nd order at q=1 (s²''(1)=2); W − W(1) to 1st (W'(1)=5). A bridge repairs the order, so order does not decide. What decides: the ratio RUNS — R(q) = (q+1)(4q¹²+4q¹⁰+8q⁸+8q⁶+8q⁴+7q²+1)/(4(q²+1)²), R → 5 at q→1, 8.5242 at q₀, 65.269 at 3/2, 695.91 at 2 — so no normalisation CONSTANT can absorb it. Required c is 100/69591 at q=2 vs 86528/5647625 at q=3/2. Lean `no_constant_rescaling`, `candidateRatio_two`, `candidateRatio_three_halves`, decided at two rational points. Every order-matched bridge (h, ℏ_q, s, q−1, h/2) carries leading coefficient W'(1)=5 times its own, never s²'s 1.

Producer `markov/weak_vertex_coupling_normalisation_probe.py` 7/7; both Lean files lean-direct exit 0, axioms clean; §7c split done on the gate's demand; precision gates 0 NEW dirty.

STILL OPEN (the real remainder): a W-based coupling of another SHAPE is untested — a ratio against another trace in the tower (the trefoil is the natural denominator, the corpus already reads the electron off its three crossings), a Jones-normalised object (V_K(1) = 1 for EVERY knot, so V − 1 has its normalisation fixed by topology rather than chosen), or a bar-parity component. What would settle it is deriving the coupling's normalisation from the rate formula's own construction, not another scan.

FOLLOW-UP: the same §7c mixed-content flag is latent in the two files merged earlier in this arc (WeakVertexT35TraceClosedForm, WeakVertexSubstitutionScale); unflagged only because the gate inspects changed files. Mechanical, name-preserving, not done here.
