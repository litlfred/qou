#!/usr/bin/env python3
"""z2bn lever-1 τ-derivation — THIRD probe: PF-monodromy SL₂ synthesis.

Synthesises three threads on the binding-τ keystone operator `M`
(`a_D^(n+2) = τ a_D^(n+1) − a_D^(n)`):
  (i)   sibling #2755 conjecture: `M` = the Bring Picard–Fuchs operator;
  (ii)  this session's Probe 2 (#2768): `M` is NOT a classical d/dz jet — it must be q-difference;
  (iii) the 2026-06-24 monodromy-integrality audit: the topological PF monodromy is SL₂(ℤ),
        integer-trace, but τ ∉ ℤ.

Result (no fit — every quantity is derived):
  • `M ∈ SL₂`: transfer matrix !![τ,−1;1,0] has det = 1 (eigenvalues multiply to 1, sum to τ).
  • `τ` is a rational function of the QUANTUM INTEGER `[2]_q = q+q⁻¹` ALONE:
        τ = 3(3[2]²+2)/(4([2]+2)),    hence BAR-EVEN (τ(q⁻¹)=τ(q)).
    A classical-jet trace would be a function of q with no reason to collapse onto [2]_q —
    so the [2]_q-form is the Hecke / q-difference fingerprint (corroborates Probe 2).
  • `τ > 2 ∀q>0`, min `21/8` at q=1 (since [2]≥2 by AM-GM and 9[2]²−8[2]−10>0 for [2]≥2)
    ⇒ `M` is HYPERBOLIC (λ₊>1) = extensive binding. The topological PF monodromy at the I₁
    nodal fibres (Δ deg-6 squarefree, #2755 Step 1) is PARABOLIC (trace exactly 2).
  • τ ∉ ℤ ⇒ M ∉ SL₂(ℤ): (b)-EXCLUSION of the topological-monodromy identification.

Net: `M` is a real / q-difference `SL₂(ℝ)` operator with bar-even trace `τ([2]_q)>2` — NOT the
arithmetic SL₂(ℤ) monodromy. Constructing the explicit q-difference PF operator with this trace is
the open keystone. Lean: QOU/Mass/TauQuantumIntegerForm.lean (3 thms, sorry-free).
"""
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()
import json
import sympy as sp
import mpmath as mp

q = sp.symbols('q', positive=True)
b = sp.symbols('b')  # [2]_q
tau = 3*(3*q**4 + 8*q**2 + 3)/(4*q*(q+1)**2)
tau_b = 3*(3*b**2 + 2)/(4*(b + 2))

# (1) SL2: det of transfer matrix
M = sp.Matrix([[tau, -1], [1, 0]])
det_M = sp.simplify(M.det())

# (2) quantum-integer form + bar-even
qint_identity = sp.simplify(tau - tau_b.subs(b, q + 1/q))           # == 0
bar_even = sp.simplify(tau.subs(q, 1/q) - tau)                       # == 0

# (3) τ>2: numerator of τ-2 over [2]
tau2_num_b = sp.expand(3*(3*b**2 + 2) - 2*4*(b + 2))                # 9b²−8b−10
min_q = sp.solve(sp.numer(sp.together(sp.diff(tau, q))), q)
min_q = [c for c in min_q if c.is_positive]

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
tau_f = sp.lambdify(q, tau, 'mpmath')
q0 = mp.mpf('1.10997859555733471')
tau0 = tau_f(q0); lamp0 = (tau0 + mp.sqrt(tau0**2 - 4))/2

assert det_M == 1 and qint_identity == 0 and bar_even == 0
print("det M =", det_M, "(SL₂) | [2]-form identity:", qint_identity, "| bar-even:", bar_even)
print("τ−2 numerator over [2]: %s (roots %s); [2]≥2 ⇒ τ>2, min τ=21/8 at q=%s"
      % (tau2_num_b, [str(r) for r in sp.solve(tau2_num_b, b)], min_q))
print("q₀: τ=%.6f  λ₊=%.6f (>1 extensive)  λ₋=%.6f" % (float(tau0), float(lamp0), float(1/lamp0)))

out = {
  "description": ("z2bn lever-1 τ third probe (PF-monodromy SL₂ synthesis): M∈SL₂ with bar-even trace "
                  "τ([2]_q)>2 (hyperbolic), excluding the SL₂(ℤ) topological monodromy; q-difference PF "
                  "indicated. No fit."),
  "transfer_matrix": "!![tau,-1;1,0]", "det_M": int(det_M), "sl2": True,
  "tau_quantum_integer_form": "3*(3*[2]^2+2)/(4*([2]+2)), [2]=q+1/q",
  "qint_form_identity_residual": int(qint_identity), "tau_bar_even_residual": int(bar_even),
  "tau_minus_2_numer_over_qint2": str(tau2_num_b),
  "tau_gt_2_all_q": True, "tau_min": "21/8", "tau_min_at_q": "1",
  "tau_at_q0": float(tau0), "lambda_plus_at_q0": float(lamp0), "lambda_minus_at_q0": float(1/lamp0),
  "classical_PF_monodromy": "SL2(Z), parabolic trace 2 at I1 nodal fibres (Delta deg6 squarefree, #2755 Step1)",
  "exclusion": ("(b): tau not in Z (even tau(1)=21/8) => M not in SL2(Z) => M is NOT the topological PF "
                "monodromy. M is a real/q-difference SL2(R) operator with bar-even trace tau([2]_q)."),
  "open_keystone": "explicit q-difference PF operator with trace tau([2]_q); owner-gated",
  "lean": "QOU/Mass/TauQuantumIntegerForm.lean (tau_quantum_integer_form, tau_bar_even, transfer_det_one; sorry-free)",
  "no_fit": True,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
wpath = WitnessBuilder.wrap_legacy(
    "z2bn-pf-monodromy-synthesis", out,
    script_path=__file__, engine="sympy", start_time=_T0,
).save()
print("witness ->", wpath)
