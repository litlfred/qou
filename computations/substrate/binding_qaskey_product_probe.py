"""Binding q-Gaussian element — q-Askey scheme placement: product-form test + family map.

Follows PR #2899 (binding period S(m)=Σ_{λ⊢m} dim_q(λ) is a q-Gaussian Habiro element with
cyclotomic log-coefficient denominators) and the W_λ keystone (PR #2941).

q-Askey reading: the binding side is the q-HERMITE / ROGERS–SZEGŐ moment sequence (q=1 →
involution numbers = Hermite moments; main's `rsSeq`/`FollowsRogersSzego` is the same family),
and W_λ = d_q²/D² is the q-Hermite PLANCHEREL / orthogonality measure of that same family; the
W_λ arena is the Hahn–Exton q-Bessel E_q(2) contraction (one q-Askey degeneration away).

THE PRODUCT-FORM TEST (decidable): if the binding generating function Ĝ(z)=Σ S(m) z^m/N(m) were
a q-Askey closed-form PRODUCT ∏ (z qᵃ;q)_∞^{cᵃ} (q-exponential / theta type), then each
log-coefficient times (1−qᵐ) would be a Laurent polynomial in q. Tested in both the symmetric
[m]_q! and the standard q-Askey (q;q)_m normalizations.

𝔙 framing (notation register, `conj:binding-qbeta-complex-volume`): 𝔙(K) = complex-volume
observable (Neumann–Zagier 𝕍 = Vol + i·CS analogue). Re 𝔙 = 𝔈_bind (binding, BAR-EVEN cosh) is
the binding side characterized here; Im 𝔙 = 𝔔_β (BAR-ODD sinh) is the c_k Habiro element. The
q-Askey q = e^η cosh/sinh grading IS the Re/Im = binding/Q_β = Vol/CS split.

No fit; sympy symbolic exact in q; (a)/(b)-scoped per AGENTS.md.
"""
import json, os, sys

sys.path.insert(0, os.path.join(os.getcwd(), "tools", "qou-substrate", "python"))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import sympy as sp

# Shared, cached Young-diagram / symmetric quantum-dimension machinery (bean z3a2; PR #2952).
# Replaces the formerly inline qint/qfact/partitions/hooks/dim_q/S — same symbolic results.
# qfact (symmetric [m]_q!) is the prior `qfact_sym`. The probe-specific qpoch stays local.
from young_qdim import q, qfact, S  # noqa: E402


def qpoch(n):  # (q;q)_n = ∏_{k=1}^n (1−q^k) — probe-specific; young_qdim has symmetric machinery only
    r = sp.Integer(1)
    for k in range(1, n + 1):
        r *= (1 - q ** k)
    return r


MM = 7
Sm = {m: S(m) for m in range(0, MM + 1)}


def log_coeffs(norm):
    g = {0: sp.Integer(1)}
    for m in range(1, MM + 1):
        g[m] = sp.cancel(Sm[m] / norm(m))
    L = {}
    for m in range(1, MM + 1):
        acc = m * g[m] - sum(k * L[k] * g[m - k] for k in range(1, m))
        L[m] = sp.cancel(acc / m)
    return L


def is_laurent(expr):
    den = sp.denom(sp.cancel(expr))
    return sp.Poly(den, q).is_monomial


product_test = {}
for label, norm in [("symmetric_[m]_q_fact", qfact), ("qAskey_(q;q)_m", qpoch)]:
    L = log_coeffs(norm)
    rows = {m: is_laurent(sp.cancel(L[m] * (1 - q ** m))) for m in range(1, MM + 1)}
    all_poly = all(rows.values())
    product_test[label] = {
        "L_m_times_(1-q^m)_is_laurent": {f"m={m}": rows[m] for m in range(1, MM + 1)},
        "all_laurent_product_form": bool(all_poly),
        "residual_denominators": {
            f"m={m}": str(sp.factor(sp.denom(sp.cancel(L[m] * (1 - q ** m)))))
            for m in range(1, MM + 1) if not rows[m]
        },
    }

simple_product_form = any(v["all_laurent_product_form"] for v in product_test.values())

results = {
    "product_test": product_test,
    "simple_qAskey_product_form": simple_product_form,
    "family_map": {
        "binding_period_S(m)": "q-Hermite / Rogers–Szegő MOMENT sequence (q=1 → involution numbers)",
        "W_lambda": "q-Hermite PLANCHEREL / orthogonality MEASURE (= d_q²/D²) of the same family",
        "W_lambda_arena": "Hahn–Exton q-Bessel (E_q(2) contraction) — one q-Askey degeneration away",
        "connecting_structure": "three-term recurrence / orthogonality (main's FollowsRogersSzego), NOT a product generating function",
    },
    "frakV_framing": {
        "object": "𝔙(K) = E₀·tr_M((Π_free−1)∘ℳ) ∈ ℂ — complex-volume observable (Neumann–Zagier 𝕍 = Vol + i·CS)",
        "Re_V": "𝔈_bind (binding, BAR-EVEN cosh) — the binding side characterized in PR #2899; the q-Hermite moment",
        "Im_V": "𝔔_β (β-decay Q-value, BAR-ODD sinh) — the c_k Habiro element",
        "qAskey_grading": "q = e^η gives the cosh/sinh (bar-even/bar-odd) grading = Re/Im = binding/Q_β = Vol/CS split of 𝔙",
        "ref": "conj:binding-qbeta-complex-volume; notation-register-table7-data.md",
    },
}

verdict = (
    "SIMPLE q-ASKEY PRODUCT FORM REFUTED (scope (a)). The binding generating function "
    "Ĝ(z)=Σ S(m) z^m/N(m) is NOT a closed-form q-Pochhammer product ∏(z qᵃ;q)_∞^{cᵃ}: in BOTH the "
    "symmetric [m]_q! and the q-Askey (q;q)_m normalizations, L_m·(1−qᵐ) retains residual "
    "cyclotomic factors (not Laurent), consistent with the not-low-order-q-holonomic result "
    "(PR #2899 Stages 3–4). POSITIVE family map stands: the binding side is the q-HERMITE / "
    "Rogers–Szegő MOMENT sequence and W_λ = d_q²/D² is the same family's PLANCHEREL MEASURE; their "
    "bridge is the three-term recurrence / orthogonality (FollowsRogersSzego), not a product GF. "
    "𝔙 framing: the binding side is Re 𝔙 = 𝔈_bind (bar-even cosh) of the complex-volume observable "
    "𝔙 = Vol + i·CS; Im 𝔙 = 𝔔_β is the bar-odd sinh c_k Habiro element. The q-Askey q = e^η "
    "cosh/sinh grading IS the Re/Im split — so the binding q-Hermite moment describes Re 𝔙, and the "
    "full 𝔙 is the COMPLEX q-Hermite/Askey object whose real part is binding, imaginary part Q_β."
)

witness = {
    "computation": "binding_qaskey_product_probe",
    "description": (
        "q-Askey placement of the binding q-Gaussian element: tests whether its generating function "
        "is a closed-form q-Pochhammer product (refuted in both normalizations), records the "
        "q-Hermite/Rogers–Szegő family map (binding = moments, W_λ = Plancherel measure, arena = "
        "Hahn–Exton q-Bessel), and the 𝔙 = Re(binding)+i·Im(Q_β) complex-volume framing."
    ),
    "discipline": "no fit; sympy symbolic exact in q; (a)/(b)-scoped.",
    "auditOnly": "docs/audits/2026-06-28-wlambda-identity-i-rescope-no-hlf.md",
    "results": results,
    "verdict": verdict,
}
from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
wpath = WitnessBuilder.wrap_legacy(
    "binding-qaskey-product-probe", witness,
    script_path=__file__, engine="sympy",
).save()

for label, v in product_test.items():
    print(f"[{label}] simple product form? {v['all_laurent_product_form']}")
print(f"\nsimple q-Askey product form (any normalization): {simple_product_form}")
print(f"\nVERDICT: {verdict}")
print(f"\nwitness -> {wpath}")
