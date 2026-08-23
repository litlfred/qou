"""Lever-1 fibre kernel, Stage 5: the EXPLICIT q-exponential (Habiro) form of S(m).

Stages 1-4: the binding period S(m)=Σ_{λ⊢m} dim_q(λ) (q=1 → involution numbers I(m)) has
a q-involution SKELETON with an exact cyclotomic (q-1)²·Φ_d correction tower, and is NOT
q-holonomic of small order (≤3). This stage CONSTRUCTS the explicit Habiro-ring object directly,
on the binding side (exact data, no precision floor, unlike the Q_β c_k).

Classical anchor: the involution EGF closes in CLOSED FORM,
    Σ_m I(m) x^m / m! = exp(x + x²/2),
so log of the EGF TRUNCATES at degree 2 (L_1 = 1, L_2 = 1/2, L_{≥3} = 0). The binding period is
the q-deformation. Define the q-exponential generating function in the symmetric q-factorial
[m]_q! = ∏_{k=1}^m [k]_q (matching dim_q's normalisation):

    Ŝ(z) = Σ_m S(m) z^m / [m]_q!  = 1 + Σ_{m≥1} g_m z^m,   g_m = S(m)/[m]_q!.

THE TEST (decidable, no fit): compute the log-series coefficients
    log Ŝ(z) = Σ_{m≥1} L_m z^m
symbolically in q (Newton: L_1=g_1, L_2=g_2-g_1²/2, L_3=g_3-g_1g_2+g_1³/3, …).
- If L_{≥3} VANISH ⇒ Ŝ = exp_q(L_1 z + L_2 z²): a pure q-GAUSSIAN — the exact Habiro element,
  the clean q-analog of exp(x+x²/2).
- If L_{≥3} are nonzero but carry the (q-1)·cyclotomic signature ⇒ the element is a q-Gaussian
  dressed by a cyclotomic (Habiro) correction — the explicit higher structure, exhibited.
- L_1, L_2 must reduce to 1, 1/2 at q=1 (classical sanity).

No fit; sympy symbolic exact in q; (a)/(b)-scoped per AGENTS.md. The Q_β-side element F(q) is a
DIFFERENT, gated object (SW-residue / jet-prolongation keystone conj:qdifference-kernel-
prolongation-symbol; fitting Φ₂ is the forbidden 'seventh ansatz' — 2026-06-09 scope doc). This
constructs the binding-side Habiro element from exact data, which the noise-limited c_k cannot.
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import _path_bridge  # noqa: F401,E402 — wires tools/qou-substrate + tools/pyhecke
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp
import mpmath as mp
from qou_substrate import constants as C

# Shared, cached Young-diagram / symmetric quantum-dimension machinery (bean z3a2; PR #2952).
# Replaces the formerly inline qint/qfact/partitions/hooks/dim_q/S — same symbolic results,
# lru_cache-memoised across calls.
from young_qdim import q, qfact, S  # noqa: E402


MMAX = 8
print(f"Computing S(0..{MMAX}) and q-EGF coefficients g_m = S(m)/[m]_q! ...", flush=True)
Sm = {m: S(m) for m in range(0, MMAX + 1)}
g = {0: sp.Integer(1)}
for m in range(1, MMAX + 1):
    g[m] = sp.cancel(Sm[m] / qfact(m))
    print(f"    g({m}) done", flush=True)

# log Ŝ(z) coefficients via the standard recursion for L = log(1 + Σ g_m z^m):
#   m·L_m = m·g_m - Σ_{k=1}^{m-1} k·L_k·g_{m-k}      (g_0 = 1)
L = {}
for m in range(1, MMAX + 1):
    acc = m * g[m] - sum(k * L[k] * g[m - k] for k in range(1, m))
    L[m] = sp.cancel(acc / m)
    print(f"    L({m}) computed", flush=True)

L_factored = {m: sp.factor(L[m]) for m in range(1, MMAX + 1)}
# classical sanity at q=1
L_at_1 = {m: sp.simplify(L[m].subs(q, 1)) for m in range(1, MMAX + 1)}
classical_ok = bool(L_at_1[1] == 1 and L_at_1[2] == sp.Rational(1, 2)
                    and all(L_at_1[m] == 0 for m in range(3, MMAX + 1)))
truncates_at_2 = all(L[m] == 0 for m in range(3, MMAX + 1))
# do the higher L_m (m>=3) carry a (q-1) factor (Habiro/fibre signature, vanish at q=1)?
def has_root_at_1(expr):
    if expr == 0:
        return True
    num = sp.numer(sp.cancel(expr))
    return sp.Poly(num, q).eval(1) == 0
higher_all_vanish_at_q1 = all(has_root_at_1(L[m]) for m in range(3, MMAX + 1))

from _precision import set_compute_dps  # noqa: E402
set_compute_dps()
q0 = mp.mpf(C.Q_MP) if hasattr(C, "Q_MP") else mp.mpf(str(C.Q))


def ev(e):
    return mp.nstr(mp.mpf(str(sp.N(e.subs(q, q0), 30))), 12)


results = {
    "L_factored": {f"m={m}": str(L_factored[m]) for m in range(1, MMAX + 1)},
    "L_at_q1": {f"m={m}": str(L_at_1[m]) for m in range(1, MMAX + 1)},
    "L_at_q0": {f"m={m}": ev(L[m]) for m in range(1, MMAX + 1)},
    "classical_limit_is_exp_x_plus_x2over2": bool(classical_ok),
    "log_truncates_at_degree_2": bool(truncates_at_2),
    "higher_L_all_vanish_at_q1": bool(higher_all_vanish_at_q1),
}
assertions = {
    "classical_limit_ok": bool(classical_ok),                 # L1=1, L2=1/2, L>=3=0 at q=1
    "L1_L2_reduce_to_1_and_half": bool(L_at_1[1] == 1 and L_at_1[2] == sp.Rational(1, 2)),
    "higher_corrections_vanish_at_q1": bool(higher_all_vanish_at_q1),  # (q-1)| L_{>=3}
}

if truncates_at_2:
    verdict = (
        "EXACT q-GAUSSIAN HABIRO ELEMENT. The binding q-EGF Ŝ(z)=Σ S(m) z^m/[m]_q! has "
        "log Ŝ(z) = L_1 z + L_2 z² with ALL L_{≥3}=0 — i.e. Ŝ = exp_q(L_1 z + L_2 z²), the exact "
        "q-analog of the classical exp(x+x²/2) involution EGF. This IS the explicit lever-1 "
        "binding Habiro element in closed form. Derived, parameter-free."
    )
else:
    verdict = (
        "q-GAUSSIAN SKELETON + CYCLOTOMIC HABIRO DRESSING. The binding q-EGF Ŝ(z)=Σ S(m)z^m/[m]_q! "
        "has log Ŝ = L_1 z + L_2 z² + Σ_{m≥3} L_m z^m with L_1,L_2 → 1,1/2 at q=1 (the classical "
        "exp(x+x²/2) skeleton) and the higher L_{≥3} "
        + ("ALL carrying a (q-1) factor (vanish at q=1) — a pure fibre/q-deformation correction in "
           "the Habiro ring. " if higher_all_vanish_at_q1 else "nonzero already without a uniform "
           "(q-1) factor. ")
        + "So the explicit binding-side object is a q-Gaussian dressed by a higher Habiro "
        "correction (the log-coefficient tower L_{≥3}), constructed here in closed symbolic form. "
        "This is the binding analog of the gated Q_β element F(q); it is NOT that element (the "
        "Q_β F is gated on the SW-residue keystone, fitting Φ₂ forbidden), but it exhibits the "
        "SAME Habiro-ring habitat from exact, non-floor-limited data. (a)-scoped."
    )

witness = {
    "computation": "lever1_binding_habiro_qexponential",
    "description": (
        "Stage 5: constructs the explicit q-exponential (Habiro) generating-function form of the "
        "binding period S(m)=Σ_{λ⊢m} dim_q(λ). Tests whether log of the q-EGF Σ S(m)z^m/[m]_q! "
        "truncates at degree 2 (pure q-Gaussian = clean q-analog of the classical involution EGF "
        "exp(x+x²/2)) or carries a higher cyclotomic/(q-1) Habiro correction. Exact data, no fit."
    ),
    "discipline": (
        "no fit; sympy symbolic exact in q; classical q=1 sanity (L1=1,L2=1/2,L>=3=0); the Q_β "
        "element F(q) is a different gated object (SW-residue keystone; Φ₂ fit forbidden) — this "
        "is the unguarded binding-side construction. (a)/(b)-scoped per AGENTS.md."
    ),
    "auditOnly": "docs/audits/2026-06-27-lever1-qinvolution-cyclotomic-kernel.md",
    "results": results,
    "assertions": assertions,
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
# Payload carries a top-level `assertions` mapping → stamp (not wrap_legacy) preserves it.
WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(os.path.dirname(__file__), "lever1-binding-habiro-qexponential.witness.json")
with open(out, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2)
    f.write("\n")

print(f"\n  classical limit exp(x+x²/2)? {classical_ok}   log truncates at z²? {truncates_at_2}")
print(f"  higher L_(≥3) all vanish at q=1 (carry q-1)? {higher_all_vanish_at_q1}")
for m in range(1, MMAX + 1):
    print(f"    L({m}) = {L_factored[m]}    [q=1: {L_at_1[m]}]")
print(f"\n  VERDICT: {verdict}")
print(f"\nwitness -> {out}")
