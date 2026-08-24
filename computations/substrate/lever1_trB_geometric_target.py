#!/usr/bin/env python3
"""lever1_trB_geometric_target.py
==================================

Turn the open lever-1 identification `a_D^(n) = lw(n−1)` (SW prolonged period =
selection-rule value, #1765) into a CONCRETE, falsifiable geometric target, and
record a sharp tension the torus shortcut surfaces.

Background. The depth-2 `det B = 1` recurrence `a_{n+2} = τ·a_{n+1} − a_n` is
PROVED (`prop:sl2-prolongation-recurrence`), so the kernel `R = x² − τx + 1` has
ONE unknown `τ = tr B`. `unified_tau_odd_partner_solve.py` solves `τ` from the
THREE selection-rule values `a_D^(2)=1, a_D^(3)=(q+1)²/(3q), a_D^(4)=Family-A` —
but those are ASSUMED from the rule, not computed geometrically. The geometric
side (`a_D^(n) = φ(Mⁿv₀)`, Gauss–Manin period of Bring's curve) is uncomputed.

This probe (no fit; symbolic + mpmath only):

  (T) THE TARGET. The identification holds IFF the geometric Bring W-plane
      monodromy trace equals
          tr B = (a_D^(2)+a_D^(4))/a_D^(3) = 3(3q⁴+8q²+3)/(4q(q+1)²).
      A single checkable number (2.6424 at q₀).

  (S) THE TORUS SHORTCUT FAILS. The substrate torus E_q has GEOMETRIC prolonged
      periods P_m = cosh((2m+1)η₀)/(2cosh η₀) (η₀=log q₀) with τ_torus =
      (P₁+P₃)/P₂ = 2cosh(2η₀) = q₀²+q₀⁻². We verify that recurrence, then show
      τ_binding (2.6424) ≠ τ_torus (2.0437): the binding W-plane is NOT the
      substrate torus — it is a genuinely separate genus-4 (Bring) object.

  (X) THE TENSION (for the keystone). The cheat-sheet frames `H¹(Bring) = 2W`
      with W the substrate W-plane. If that W is literally the substrate torus's
      H¹, τ_binding should equal τ_torus — it does not. So EITHER (a) the W-plane
      is a distinct Bring-specific rank-2 factor (period ≠ torus), OR (b) the
      rule's a_D values are not the geometric periods (a_D ≠ lw) — a fork the
      genus-4 Bring period (Sage, `lever1_bring_period_trB.sage`) resolves.

Honest status: `tr B` is the trace of the q-FAMILY Gauss–Manin MONODROMY
(`a_D^(n)=φ(Mⁿv₀)`); a single FIXED curve has a period lattice but no monodromy,
so `tr B(q₀)` is gated on the q-family matrix `M` (the s5-so3 keystone,
owner-gated) — NOT merely on a tool. Sage (now installed) supplies the fixed-curve
geometric input and settles the rank-2 question EXACTLY: `H^{1,0}(Bring)` is the
4-dim irreducible A₅ standard rep, so any rank-2 `W` is an isogeny/CM factor of
`Jac(Bring)`, not an A₅-subrep of the forms (see `lever1_bring_period_trB.sage`).
This probe states the target + the torus tension.
"""
from __future__ import annotations

import json
import pathlib

import sympy as sp
import mpmath as mp

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
Q0 = mp.mpf("1.1099785955573347198997632204832250266562084087802")

results: dict = {}
asserts: list[tuple[str, bool]] = []


def check(name, ok):
    asserts.append((name, bool(ok)))
    print(f"  [{'ok' if ok else 'FAIL'}] {name}")


# ── (T) the concrete target tr B = (a2+a4)/a3 ────────────────────────────────
q = sp.Symbol("q", positive=True)
a2, a3, a4 = sp.Integer(1), (q + 1) ** 2 / (3 * q), (3 * q ** 2 + 4 + 3 / q ** 2) / 4
trB = sp.simplify((a2 + a4) / a3)
# Closed form, guarded symbolically identical to trB, evaluated directly in
# mpmath at the 40-dps Q0 — no sympy→str→mpmath round-trip (Gemini #2701).
assert sp.simplify(trB - 3 * (3 * q ** 4 + 8 * q ** 2 + 3) / (4 * q * (q + 1) ** 2)) == 0
trB_q0 = 3 * (3 * Q0 ** 4 + 8 * Q0 ** 2 + 3) / (4 * Q0 * (Q0 + 1) ** 2)
print("(T) target tr B = (a_D^(2)+a_D^(4))/a_D^(3)")
print(f"    symbolic = {trB}")
print(f"    at q₀    = {mp.nstr(trB_q0, 12)}")
results["target_trB_symbolic"] = str(trB)
results["target_trB_at_q0"] = mp.nstr(trB_q0, 20)

# ── (S) torus geometric recurrence + shortcut comparison ─────────────────────
eta0 = mp.log(Q0)
P = [mp.cosh((2 * m + 1) * eta0) / (2 * mp.cosh(eta0)) for m in range(1, 6)]
tau_torus = (P[0] + P[2]) / P[1]
tau_torus_closed = 2 * mp.cosh(2 * eta0)
recur_ok = all(abs(tau_torus * P[i + 1] - P[i] - P[i + 2]) < mp.mpf("1e-30")
               for i in range(len(P) - 2))
print("\n(S) torus geometric prolonged-period recurrence + shortcut")
print(f"    τ_torus = (P₁+P₃)/P₂ = {mp.nstr(tau_torus, 12)}  (= 2cosh2η₀ = {mp.nstr(tau_torus_closed, 12)})")
print(f"    torus recurrence a_{{n+2}}=τa_{{n+1}}−a_n holds: {recur_ok}")
check("(S) torus geometric recurrence holds (τ=2cosh2η₀)", recur_ok)
shortcut_match = abs(trB_q0 - tau_torus) < mp.mpf("1e-6")
print(f"    τ_binding {mp.nstr(trB_q0, 8)}  vs  τ_torus {mp.nstr(tau_torus, 8)}  →  "
      f"match: {shortcut_match}  (diff {mp.nstr(abs(trB_q0 - tau_torus), 4)})")
check("(S) torus shortcut FAILS (binding W-plane ≠ substrate torus)", not shortcut_match)
results["tau_torus_at_q0"] = mp.nstr(tau_torus, 20)
results["torus_shortcut_matches"] = bool(shortcut_match)

# ── (X) is τ_binding a torus at shifted modulus? (q₀^k+q₀^-k) ─────────────────
# Analytic larger root of z + 1/z = τ ⟺ z² − τz + 1 = 0 (Gemini #2701) —
# exact, no solver convergence dependency.
x = (trB_q0 + mp.sqrt(trB_q0 ** 2 - 4)) / 2
k = mp.log(x) / mp.log(Q0)
k_int = abs(k - mp.nint(k)) < mp.mpf("0.01")
print(f"\n(X) τ_binding = q₀^k+q₀^-k with k = {mp.nstr(k, 8)}  (integer k? {bool(k_int)})")
print("    → not a clean torus-at-shifted-modulus; genuinely Bring-genus-4.")
results["tau_binding_as_qk_exponent"] = mp.nstr(k, 12)
results["tau_binding_is_integer_torus_power"] = bool(k_int)
check("(X) τ_binding is NOT q₀^k+q₀^-k for integer k (distinct geometric object)", not k_int)

all_passed = all(ok for _, ok in asserts)
verdict = (
    "TARGET RECORDED + TORUS SHORTCUT REFUTED. The lever-1 identification "
    "a_D^(n)=lw(n−1) reduces to ONE checkable geometric number: the Bring "
    "W-plane monodromy trace tr B = 3(3q⁴+8q²+3)/(4q(q+1)²) = 2.6424 at q₀. The "
    "easy geometric handle FAILS — τ_torus = 2cosh2η₀ = 2.0437 ≠ 2.6424, and "
    "τ_binding ≠ q₀^k+q₀^-k for integer k — so the binding W-plane is a genuinely "
    "separate genus-4 Bring object, not the substrate torus. TENSION for the "
    "keystone: if H¹(Bring)=2W with W the substrate, τ_binding should equal "
    "τ_torus; it does not, so either W is a distinct Bring factor or a_D≠lw. tr B "
    "is the trace of the q-FAMILY Gauss–Manin MONODROMY; a fixed curve has no "
    "monodromy, so tr B(q₀) is gated on the q-family matrix M (s5-so3 keystone, "
    "owner-gated). Sage settles the rank-2 question EXACTLY: H^{1,0}(Bring) is the "
    "4-dim irreducible A₅ standard rep (no A₅-invariant rank-2 form-subspace; W is "
    "an isogeny/CM factor of Jac(Bring)). No fit."
)
print("\n" + ("ALL CHECKS PASS" if all_passed else "SOME FAILED"))
print("VERDICT:", verdict)

witness = {
    "computation": "lever1_trB_geometric_target",
    "description": ("Concrete geometric target for the lever-1 a_D=lw identification "
                    "(tr B = 3(3q⁴+8q²+3)/(4q(q+1)²)), the torus-shortcut-fails finding "
                    "(τ_binding ≠ τ_torus), and the W-plane≠substrate tension. The genuine "
                    "tr B needs the Bring genus-4 period (Sage script provided)."),
    "discipline": "no fit; symbolic+mpmath; TOOL-gated on Sage not owner-gated; states target + tension",
    "auditOnly": "docs/audits/2026-06-24-lever1-trB-geometric-target.md",
    "sage_script": "computations/substrate/lever1_bring_period_trB.sage",
    "results": results,
    "assertions": {n: ok for n, ok in asserts},
    "allPassed": all_passed,
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = pathlib.Path(__file__).name
out = pathlib.Path(__file__).resolve().parent / "lever1-trB-geometric-target.witness.json"
out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
print(f"\nwitness → {out}")
