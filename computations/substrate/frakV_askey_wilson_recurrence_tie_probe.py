"""𝔙 holomorphic tie — do (binding, Q_β) ride ONE Askey-Wilson 3-term recurrence? (bean 1jrh)

Compute-side exercise of the sorry-free Lean mechanism
`QOU.MassEndomorphism.recurrence_invol_descent` (binding-qbeta-complex-volume.lean):
a 3-term recurrence  V_{n+1} = c·V_n − V_{n−1}  with a **bar-even** multiplier
(σc = c, σ: q ↦ q⁻¹) descends to BOTH parity channels — the bar-even (binding)
and bar-odd (Q_β) ladders satisfy the SAME recurrence. The bar-even hypothesis
is *necessary*: with a bar-odd multiplier the parity channels cross-couple.

The decisive, in-reach instance is the 2-strand Hecke tower (the Hopf/deuteron
bond word σ₁², eigenvalues q², q⁻²):

  (1) EXACT (sympy, symbolic weights w±): the Hopf-power tower
      V_n = tr_M((σ₁²)^n) = w₊·q^{2n} + w₋·q^{−2n} satisfies
      V_{n+1} = (q²+q⁻²)·V_n − V_{n−1} — one 3-term recurrence whose
      multiplier c = q²+q⁻² is BAR-EVEN. This is the continuous
      q-ultraspherical (Chebyshev) special case of the Askey-Wilson
      recurrence, x = (q²+q⁻²)/2 = cos θ under q² = e^{iθ}.
  (2) EXACT descent: the bar-even part E_n = (V_n + V̄_n)/2 (binding channel)
      and bar-odd part O_n = (V_n − V̄_n)/2 (Q_β channel) EACH satisfy the
      same recurrence — the holomorphic tie at the H₂/Hopf level.
  (3) EXACT necessity: the FULL ladder tr_M(σ₁^m) (eigenvalues q, −q⁻¹) has
      multiplier q − q⁻¹ (BAR-ODD); its parity channels do NOT individually
      satisfy that recurrence — they cross-couple (E ↔ O), exactly the
      failure the Lean hypothesis σc = c excludes.
  (4) NUMERIC at the canonical muon-q₀ (50 dps, mpmath): (1)-(3) residuals.

Scope (honest): this CONFIRMS the tie for the 2-strand/Hopf (deuteron-bond)
tower — the structural mechanism. It does NOT close the descent for the full
nuclear tr_M assembly (kernels OPEN/GATED per the 2026-06-28 gap map), and the
observable-level match stays degenerate (Im(q₀)=0). No fit anywhere: the
multiplier is forced by the eigenvalues, never solved from data.

Complementary scope (sibling, main ad28b5a9): the PHYSICAL c_k-ladder AW
identification is GATED on c₃^even (under-determined, 4 AW params vs ≤2
trusted rungs — docs/audits/2026-07-02-1jrh-aw-one-recurrence-formalize-first-prune.md).
This probe is the mechanism half at a tower where no identification exists.
"""
import json
import os

import sympy as sp
from mpmath import mp
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

# ---------------------------------------------------------------- exact layer
q = sp.symbols("q", positive=True)
wp, wm = sp.symbols("w_plus w_minus")  # symbolic Markov weights (weight-independent claims)
n = sp.symbols("n", integer=True, nonnegative=True)


def bar(expr):
    """Bar involution q ↦ q⁻¹."""
    return sp.simplify(expr.subs(q, 1 / q))


# (1) Hopf-power tower V_n = w₊ q^{2n} + w₋ q^{−2n}; multiplier c₂ = q² + q⁻².
def V_hopf(k: int):
    return wp * q ** (2 * k) + wm * q ** (-2 * k)


c_even = q**2 + q**-2
rec_even_holds = all(
    sp.simplify(V_hopf(k + 1) - (c_even * V_hopf(k) - V_hopf(k - 1))) == 0 for k in range(1, 6)
)
c_even_bar_even = sp.simplify(bar(c_even) - c_even) == 0

# (2) parity descent on the Hopf tower. The bar involution acts on the tower
# function (q ↦ 1/q swaps the eigen-lines), so E_n, O_n mix w±:
#   E_n = ((w₊+w₋)/2)(q^{2n}+q^{−2n}),  O_n = ((w₊−w₋)/2)(q^{2n}−q^{−2n}).
def E_hopf(k: int):
    return sp.expand((V_hopf(k) + bar(V_hopf(k))) / 2)


def O_hopf(k: int):
    return sp.expand((V_hopf(k) - bar(V_hopf(k))) / 2)


descent_even_channel = all(
    sp.simplify(E_hopf(k + 1) - (c_even * E_hopf(k) - E_hopf(k - 1))) == 0 for k in range(1, 6)
)
descent_odd_channel = all(
    sp.simplify(O_hopf(k + 1) - (c_even * O_hopf(k) - O_hopf(k - 1))) == 0 for k in range(1, 6)
)

# (3) FULL ladder tr_M(σ₁^m): eigenvalues q, −q⁻¹ ⇒ char. recurrence
#     x_{m+1} = (q − q⁻¹)·x_m + x_{m−1}; multiplier is BAR-ODD.
def V_full(k: int):
    return wp * q**k + wm * (-(q**-1)) ** k


c_full = q - q**-1
rec_full_holds = all(
    sp.simplify(V_full(k + 1) - (c_full * V_full(k) + V_full(k - 1))) == 0 for k in range(1, 6)
)
c_full_bar_odd = sp.simplify(bar(c_full) + c_full) == 0


def E_full(k: int):
    return sp.expand((V_full(k) + bar(V_full(k))) / 2)


def O_full(k: int):
    return sp.expand((V_full(k) - bar(V_full(k))) / 2)


# With a bar-odd multiplier the descent must FAIL channel-wise: the residual of
# the E-channel recurrence is exactly the cross-coupling into the O-channel.
full_E_residuals = [
    sp.simplify(E_full(k + 1) - (c_full * E_full(k) + E_full(k - 1))) for k in range(1, 4)
]
descent_fails_full_E = all(r != 0 for r in full_E_residuals)
# Cross-coupling identity: E_{m+1} = c_odd·O_m + E_{m−1} (bar of c flips sign).
cross_coupling_holds = all(
    sp.simplify(E_full(k + 1) - (c_full * O_full(k) + E_full(k - 1))) == 0 for k in range(1, 6)
)

# -------------------------------------------------------------- numeric layer
mp.dps = 65
# q_0 from `q_parameter` -- the RUNNING SCRIPT's anchor -- rather than a direct
# read of q-pinning-50-digit.witness.json (routed 2026-09-03, bean `qou-aj91`).
# The direct read hardcoded muon and made QOU_Q0_ANCHOR inert here, which is
# what put this producer in the UNSOUND-ENV-BYPASS group: unmeasurable rather
# than held for cause. This stem stays listed `ideal_muon`, and q_parameter
# derives that anchor from q_muon_at(70), byte-identical to 70 digits with the
# value this read returned -- so no number moves; only the mechanism does.
from q_parameter import Q_50_DIGIT_STR  # noqa: E402 -- anchor-aware
q0 = mp.mpf(Q_50_DIGIT_STR)

# canonical H₂ Jones–Markov weights at n=2: y_(2) = q/[2]_q, y_(1,1) = q⁻¹/[2]_q
two_q = q0 + 1 / q0
w_plus = (q0 / two_q, "y_(2) = q/[2]_q")
w_minus = (1 / (q0 * two_q), "y_(11) = q^-1/[2]_q")


def v_hopf_num(k):
    return w_plus[0] * q0 ** (2 * k) + w_minus[0] * q0 ** (-2 * k)


def v_hopf_bar_num(k):
    # bar: q0 ↦ 1/q0 in BOTH weights and eigenvalues
    tb = 1 / q0 + q0
    wpb = (1 / q0) / tb
    wmb = q0 / tb
    return wpb * q0 ** (-2 * k) + wmb * q0 ** (2 * k)


c2_num = q0**2 + q0**-2
res_even, res_E, res_O = [], [], []
for k in range(1, 8):
    V = [v_hopf_num(k - 1), v_hopf_num(k), v_hopf_num(k + 1)]
    Vb = [v_hopf_bar_num(k - 1), v_hopf_bar_num(k), v_hopf_bar_num(k + 1)]
    E = [(V[i] + Vb[i]) / 2 for i in range(3)]
    O = [(V[i] - Vb[i]) / 2 for i in range(3)]
    res_even.append(abs(V[2] - (c2_num * V[1] - V[0])))
    res_E.append(abs(E[2] - (c2_num * E[1] - E[0])))
    res_O.append(abs(O[2] - (c2_num * O[1] - O[0])))

TOL = mp.mpf("1e-45")
num_tower_ok = max(res_even) < TOL
num_E_ok = max(res_E) < TOL
num_O_ok = max(res_O) < TOL

assertions = {
    "exact_hopf_tower_3term_recurrence": bool(rec_even_holds),
    "exact_multiplier_q2_plus_qm2_is_bar_even": bool(c_even_bar_even),
    "exact_descent_binding_channel_same_recurrence": bool(descent_even_channel),
    "exact_descent_qbeta_channel_same_recurrence": bool(descent_odd_channel),
    "exact_full_ladder_multiplier_is_bar_odd": bool(c_full_bar_odd),
    "exact_full_ladder_recurrence": bool(rec_full_holds),
    "exact_bar_odd_multiplier_descent_FAILS_channelwise": bool(descent_fails_full_E),
    "exact_bar_odd_cross_coupling_E_to_O": bool(cross_coupling_holds),
    "numeric_q0_tower_recurrence_below_1e-45": bool(num_tower_ok),
    "numeric_q0_binding_channel_below_1e-45": bool(num_E_ok),
    "numeric_q0_qbeta_channel_below_1e-45": bool(num_O_ok),
}

verdict = (
    "HOLOMORPHIC TIE CONFIRMED at the H₂/Hopf (deuteron-bond) level: the Hopf-power "
    "tower and BOTH its parity channels (binding bar-even, Q_β bar-odd) ride ONE "
    "Askey-Wilson (continuous q-ultraspherical/Chebyshev) 3-term recurrence with the "
    "bar-even multiplier c = q²+q⁻² — exactly recurrence_invol_descent. The bar-even "
    "hypothesis is NECESSARY: the full ladder's bar-odd multiplier q−q⁻¹ cross-couples "
    "the channels (E_{m+1} = c·O_m + E_{m−1}), so channel-wise descent fails. "
    "Scope-limited: 2-strand instance only; the full nuclear 𝔙 assembly stays OPEN/GATED."
)

witness = {
    "description": (
        "Askey-Wilson 3-term recurrence tie for (binding, Q_β) — compute-side exercise of the "
        "sorry-free recurrence_invol_descent at the H₂/Hopf tower; exact (sympy, symbolic "
        "weights) + 50-dps numeric at the canonical muon-q₀."
    ),
    "bean": "1jrh",
    "leanCert": (
        "QOU.MassEndomorphism.recurrence_invol_descent (binding-qbeta-complex-volume.lean, "
        "sorry-free); self-dual locus: QOU.Mass.ComplexVolumeFibreDescent.barFixed_qbeta_zero"
    ),
    "discipline": (
        "no fit — the multiplier is forced by the crossing eigenvalues (q², q⁻²), never solved "
        "from data; sympy exact with SYMBOLIC weights w± (weight-independent); mpmath 65 dps "
        "compute / tol 1e-45; muon-q₀ canonical (computations layer, AGENTS.md two-layer rule)."
    ),
    "q0_source": "q_parameter (manifest-resolved; this stem is `ideal_muon`, so the canonical muon pin). Was a direct read of computations/q-pinning-50-digit.witness.json until 2026-09-03.",
    "results": {
        "hopf_multiplier": "c = q² + q⁻² (bar-even; x = cosθ Chebyshev/q-ultraspherical node)",
        "full_ladder_multiplier": "q − q⁻¹ (bar-odd; descent fails channel-wise, cross-couples)",
        "cross_coupling_identity": "E_{m+1} = (q−q⁻¹)·O_m + E_{m−1} (exact)",
        "numeric_max_residuals": {
            "tower": mp.nstr(max(res_even), 8),
            "binding_channel": mp.nstr(max(res_E), 8),
            "qbeta_channel": mp.nstr(max(res_O), 8),
        },
        "h2_weights": {"w_plus": w_plus[1], "w_minus": w_minus[1]},
    },
    "assertions": assertions,
    "allPassed": bool(all(assertions.values())),
    "verdict": verdict,
}

from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)

WitnessBuilder.stamp_staleness_metadata(witness, script_path=__file__, engine="sympy+mpmath")
witness["scriptFile"] = os.path.basename(__file__)
out = os.path.join(
    os.path.dirname(__file__), "frakV-askey-wilson-recurrence-tie-probe.witness.json"
)
# Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
# `os.replace` it into position. `open(..., "w")` TRUNCATES before the
# dump runs, so any exception in between leaves the committed witness
# empty or partial -- the shape that emptied 22 witnesses to zero bytes
# in one `producer_importability_audit` run. `os.replace` is atomic on
# POSIX within a filesystem, hence a SIBLING temp file.
_wpath_sidu = out
_wtmp_sidu = str(_wpath_sidu) + ".tmp"
with open(_wtmp_sidu, "w", encoding="utf-8") as f:
    json.dump(witness, f, indent=2, ensure_ascii=False)
    f.write("\n")

_os_sidu.replace(_wtmp_sidu, _wpath_sidu)
print("EXACT: tower rec", rec_even_holds, "| c bar-even", c_even_bar_even)
print("EXACT descent: E-channel", descent_even_channel, "| O-channel", descent_odd_channel)
print("EXACT necessity: bar-odd multiplier fails channel-wise", descent_fails_full_E,
      "| cross-coupling E→O", cross_coupling_holds)
print("NUMERIC max residuals: tower", mp.nstr(max(res_even), 5),
      "E", mp.nstr(max(res_E), 5), "O", mp.nstr(max(res_O), 5))
print("\nVERDICT:", verdict)
print("\nwitness ->", out)
