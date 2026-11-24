#!/usr/bin/env python3
"""qbeta_habiro_integrality_kill_test.py — PROBE 1 (§3.A of
docs/audits/2026-07-11-qbeta-ck-untested-avenues-and-literature.md).

QUESTION. Is the Q_β precision ladder

    L(q) = Π_{k≥2} (1 + c_k · u(q)^k),   u = b(q)·ℏ_q²,  ℏ_q = (q−1)/q

the q = 1 Taylor expansion of a Habiro-ring element? Habiro injectivity +
integrality (arXiv:math/0209324): a genuine element of Ẑ[q] has INTEGER
coefficients α_n in the (q−1)-basis Z[[q−1]]. Because b(1) = √3/2, the
odd-u^k rungs generate coefficients in ℚ(√3); the secondary criterion is
algebraic integrality in O_{ℚ(√3)} = Z[√3] (3 ≡ 3 mod 4, so the maximal
order IS Z[√3]).

CLOSED FORM OF b (Hoefsmit b, from probe_q_beta_operator_valued_N3.py
d1·d2 + 1 and the (H²+3)/(H²+4) form in qbeta_root_of_unity_probe.py —
verified equal symbolically below):

    b(q)² = (q⁴ + q² + 1) / (q² + 1)²   ∈ ℚ(q)   (rational!)
    b(q)  = √( (q²+q+1)(q²−q+1) ) / (q²+1),  b(1) = √3/2.

So b ∈ (√3/2)·ℚ[[q−1]]: even rungs contribute rational coefficients, odd
rungs contribute √3·ℚ coefficients. Coefficient ring: ℚ(√3), O_K = Z[√3].

NORMALIZATIONS TESTED (exactly three — no scanning):
  (a) bare ladder L(q);
  (b) prefactor-dressed F(q) = P(q)·L(q), where P(q) = Q_base(q)/m_e is the
      q-DEPENDENT dimensionless prefactor of the ladder (read off the N3
      producer): Q_base = Q_A·cos(α − u/2),
      Q_A/m_e = |q²−2q−1|(q+1)/(2q³) = (1+2q−q²)(q+1)/(2q³) near q=1,
      α = (z−1)(q−1/q)/2, z = √q/(q+1);
  (c) basis change h = q−1 ↔ ℏ_q: VERIFIED symbolically (not assumed) that
      ℏ = h/(1+h) and h = ℏ/(1−ℏ) both lie in Z[[·]] with unit linear term,
      hence Z[√3][[h]] = Z[√3][[ℏ_q]] and integrality is basis-invariant.

EMPIRICAL INPUTS (tiered — see docs/coordination/ck-dk-registry.json):
  c_2 = −1  PROVED Taylor-exact (Lean, PR #1602) — orders h⁴, h⁵ of L carry
            ZERO uncertainty.
  c_3       full-absorption sequential extraction after the proved c_2
            (the qbeta_ck_cache.py convention: c_3 = (Q_AME/Q_N2 − 1)/u³),
            computed HERE per anchor:
              proton q₀ from qou_substrate.constants (0.06-ppb pin),
              muon   q₀ from q-pinning-50-digit.witness.json.
  c_4, c_5  have NO scheme-independent empirical value: once c_3 absorbs the
            single CODATA residual, sequential extraction returns c_4 = c_5
            = 0 identically; every recorded c_4/c_5 number presupposes a
            structural choice at a lower rung (extended-ck imposes c_3 = −2;
            the registry c_4 = −0.97157 is a CODATA-residual fit). We run a
            documented SENSITIVITY variant with the recorded extended-ck
            central values (c_4 = −2.5379, c_5 = −164.93, witness
            qbeta-decay-sdp-extended-ck) purely to demonstrate that orders
            h⁸+ are unresolvable — it adds no information (see below).

UNCERTAINTY MODEL (honest resolvability):
  σ_exp(Q_β) ≈ 780 ppb (docs/precision-goals.md CAL-2 floor; the 7.8-ppb L2
  target is σ_exp/100). Propagated: σ(c_k) = σ_rel(Q)/u^k, i.e.
  σ(c_3) ≈ 1.26, σ(c_4) ≈ 148, σ(c_5) ≈ 1.7e4. Anchor systematic:
  |c_3(proton) − c_3(muon)| computed here. An order n is RESOLVABLE when the
  total propagated σ on the tested coefficient part is < 0.5 (can decide the
  nearest integer). Consequences, stated up front:
    orders 4,5   → EXACT (c_2 proved): fully resolvable, zero uncertainty;
    orders 6,7   → c_3 enters: σ_exp-propagated ≈ 0.4–0.5 → marginal (≈1σ);
                   anchor spread alone ≈ 0.02 → resolvable under the
                   anchor-systematic-only reading;
    orders 8–11  → c_4/c_5 enter: σ ≳ 80 → UNRESOLVABLE at any current
                   precision; reported for completeness only.

KILL CRITERION (pre-stated, from the task):
  If under NO tested normalization the resolvable α_n are within uncertainty
  of integers / Z[√3]-integers (beyond trivially-forced low orders), verdict
  = NEGATIVE, scope-limited (a): "the ladder is not the q=1 Taylor expansion
  of a Habiro-ring element under the natural normalizations" — NOT a
  structural (b) exclusion (a different normalization/prefactor outside the
  natural set, or a non-Habiro analytic object per §3.B state integrals,
  remains open). If integer-compatible → GATE-PASSED.

DISCIPLINE: no fitted forms, no c_k value proposals, tiered language.
Run:
  python3 -u computations/probes/qbeta_habiro_integrality_kill_test.py
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))          # computations/
import _path_bridge  # noqa: F401, E402 — cluster path bridge

from _precision import set_compute_dps, fmt  # noqa: E402

set_compute_dps()  # canonical mpmath dps (≥ 50-dps floor + guard digits)

import mpmath as mp  # noqa: E402
import sympy as sp  # noqa: E402

T0 = time.time()
OUT_DPS = 50
SIGMA_REL_QBETA = mp.mpf("7.8e-7")  # 780 ppb CAL-2 floor (precision-goals.md)

# ---------------------------------------------------------------------------
# Anchors (both pins of the ONE substrate modulus — AGENTS.md §q₀ anchor conv.)
# ---------------------------------------------------------------------------
sys.path.insert(0, str(HERE.parent.parent / "tools" / "qou-substrate" / "python"))
import qou_substrate.constants as _qsc  # noqa: E402

Q0_PROTON = mp.mpf(_qsc.Q_50_DIGIT_STR)

with (_path_bridge.witness_path("q-pinning-50-digit.witness.json", HERE.parent)).open() as fh:
    Q0_MUON = mp.mpf(json.load(fh)["derived_50_digit"]["q"])

from codata_constants import M_E_MEV, M_P_MEV_VALIDATION, M_N_MEV_VALIDATION  # noqa: E402

M_E = mp.mpf(str(M_E_MEV))
Q_AME = mp.mpf(M_N_MEV_VALIDATION) - mp.mpf(M_P_MEV_VALIDATION) - M_E

# Cross-check targets are READ FROM the committed N3 witness, further down --
# see the block above `xchecks`. The three literals that used to sit here were
# snapshots of the retired-muon-pin chain and had gone stale (bean qou-l4q3).
EXTENDED_CK_C4 = mp.mpf("-2.5378659117940255569454500193524358506536471385217")
EXTENDED_CK_C5 = mp.mpf("-164.92966962997120315189506117224341793666720626325")

# ---------------------------------------------------------------------------
# Step 1 — symbolic machinery: exact series in h = q − 1 over ℚ(√3)[c3,c4,c5]
# ---------------------------------------------------------------------------
N_ORD = 12  # keep h^0 .. h^11 (u^5 = O(h^10), so c_5 appears at orders 10, 11)

h = sp.symbols("h")
q = 1 + h
c3s, c4s, c5s = sp.symbols("c3 c4 c5")
SQRT3 = sp.sqrt(3)


def trunc(e):
    """Expand and truncate a polynomial/series expression to degree < N_ORD."""
    e = sp.expand(e)
    return sp.Add(*[e.coeff(h, n) * h ** n for n in range(N_ORD)])


def ser(expr):
    """Exact sympy series of a closed-form expression, truncated to N_ORD."""
    return trunc(sp.series(expr, h, 0, N_ORD).removeO())


print("=" * 92)
print("  PROBE 1 — Habiro-integrality kill-test of the Q_β c_k ladder")
print("=" * 92)
print(f"\n[{time.time()-T0:6.1f}s] symbolic: b(q) closed form + ring check")

# b(q) three ways — verify they agree symbolically (algebraic preflight)
qq = sp.symbols("qq", positive=True)
b2_producer = (qq ** 3 / (qq ** 2 + 1)) * (-1 / (qq * (qq ** 2 + 1))) + 1  # d1·d2 + 1
b2_hform = ((qq - 1 / qq) ** 2 + 3) / ((qq - 1 / qq) ** 2 + 4)             # (H²+3)/(H²+4)
b2_rational = (qq ** 4 + qq ** 2 + 1) / (qq ** 2 + 1) ** 2
assert sp.simplify(b2_producer - b2_rational) == 0, "b² producer form mismatch"
assert sp.simplify(b2_hform - b2_rational) == 0, "b² (H²+3)/(H²+4) form mismatch"
assert sp.simplify(b2_rational.subs(qq, 1) - sp.Rational(3, 4)) == 0
print("    b(q)² = (q⁴+q²+1)/(q²+1)²  [three forms agree symbolically]; b(1) = √3/2")
print("    ⇒ coefficient ring ℚ(√3); O_K = Z[√3]  (3 ≡ 3 mod 4)")

b_series = ser(sp.sqrt(b2_rational.subs(qq, q)))
hbar_series = ser((q - 1) / q)                 # = h/(1+h)
u_series = trunc(b_series * hbar_series ** 2)  # u = b·ℏ_q², O(h²)

# Ladder L(q) = Π (1 + c_k u^k), c_2 = −1 exact, c_3..c_5 symbolic
u_pows = {1: u_series}
for k in range(2, 6):
    u_pows[k] = trunc(u_pows[k - 1] * u_series)

CKS = {2: sp.Integer(-1), 3: c3s, 4: c4s, 5: c5s}
L_series = sp.Integer(1)
for k, ck in CKS.items():
    L_series = trunc(L_series * (1 + ck * u_pows[k]))

# Prefactor P(q) = (Q_A/m_e)·cos(α − u/2)   [dimensionless, q-dependent]
QA_over_me = (1 + 2 * q - q ** 2) * (q + 1) / (2 * q ** 3)  # |q²−2q−1| = 1+2q−q² near q=1
z_expr = q ** 3 / (q ** 2 + 1)   # convention D (was C: sqrt(q)/(q+1))
alpha_expr = (z_expr - 1) * (q - 1 / q) / 2
t_series = trunc(ser(alpha_expr) - u_series / 2)  # argument of cos, O(h)
t_sq = trunc(t_series * t_series)
cos_series = sp.Integer(1)
t_pow = sp.Integer(1)  # t^{2m}, iterated with truncation (no direct big powers)
for m in range(1, N_ORD // 2 + 1):
    t_pow = trunc(t_pow * t_sq)
    cos_series += sp.Integer(-1) ** m * t_pow / sp.factorial(2 * m)
cos_series = trunc(cos_series)
P_series = trunc(ser(QA_over_me) * cos_series)
F_series = trunc(P_series * L_series)  # normalization (b)

print(f"[{time.time()-T0:6.1f}s] symbolic: L, P, F expanded to O(h^{N_ORD})")

# --- (c) basis invariance h ↔ ℏ_q, verified symbolically -------------------
hb = sp.symbols("hb")
hbar_of_h = [sp.series(h / (1 + h), h, 0, N_ORD).removeO().coeff(h, n) for n in range(N_ORD)]
h_of_hbar = [sp.series(hb / (1 - hb), hb, 0, N_ORD).removeO().coeff(hb, n) for n in range(N_ORD)]
basis_fwd_integer = all(c == sp.floor(c) for c in hbar_of_h)   # ℏ = h − h² + h³ − …
basis_bwd_integer = all(c == sp.floor(c) for c in h_of_hbar)   # h = ℏ + ℏ² + ℏ³ + …
# round trip = identity
roundtrip = sp.series((hb / (1 - hb)).subs(hb, h / (1 + h)), h, 0, N_ORD).removeO()
basis_roundtrip_ok = sp.simplify(roundtrip - h) == 0
unit_linear = (hbar_of_h[1] == 1) and (h_of_hbar[1] == 1)
basis_invariant = basis_fwd_integer and basis_bwd_integer and basis_roundtrip_ok and unit_linear
print(f"    (c) ℏ_q = h/(1+h) ∈ Z[[h]]: {basis_fwd_integer};  "
      f"h = ℏ/(1−ℏ) ∈ Z[[ℏ]]: {basis_bwd_integer};  round-trip id: {basis_roundtrip_ok}")
print("        ⇒ Z[√3][[h]] = Z[√3][[ℏ_q]] — integrality is basis-invariant (verified, not assumed)")


def split_sqrt3(expr):
    """expr (rational-linear in c3,c4,c5 over ℚ(√3)) → (A, B) with expr = A + B√3."""
    e = sp.expand(expr)
    return e.coeff(SQRT3, 0), e.coeff(SQRT3, 1)


def lin_parts(expr):
    """expr linear in c3,c4,c5 → dict of exact Rational coefficients."""
    e = sp.expand(expr)
    d = {}
    d["const"] = sp.Rational(e.subs({c3s: 0, c4s: 0, c5s: 0}))
    for name, s in (("c3", c3s), ("c4", c4s), ("c5", c5s)):
        coeff = sp.expand(e.coeff(s))
        assert not coeff.free_symbols & {c3s, c4s, c5s}, "nonlinear in c_k below h^12?"
        d[name] = sp.Rational(coeff)
    return d


def series_table(poly):
    """Per-order n: {A: linparts, B: linparts} with coeff_n = A + B√3."""
    tab = {}
    for n in range(N_ORD):
        A, B = split_sqrt3(poly.coeff(h, n))
        tab[n] = {"A": lin_parts(A), "B": lin_parts(B)}
    return tab


TAB_L = series_table(L_series)
TAB_F = series_table(F_series)

# sanity: leading structure of the bare ladder
assert TAB_L[4]["A"] == {"const": sp.Rational(-3, 4), "c3": 0, "c4": 0, "c5": 0}
assert TAB_L[4]["B"]["const"] == 0 and TAB_L[4]["B"]["c3"] == 0
print(f"    sanity: bare-ladder α_4 = −3/4 exactly (c_2 = −1 proved, b(1)² = 3/4) ✓")
print(f"[{time.time()-T0:6.1f}s] symbolic tables built")

# ---------------------------------------------------------------------------
# Step 2 — empirical c_3 per anchor (full-absorption extraction, cache conv.)
# ---------------------------------------------------------------------------


def R2mp(r):
    r = sp.Rational(r)
    return mp.mpf(r.p) / mp.mpf(r.q)


def chain(q0):
    """The N3-producer chain at anchor q0 → dict of mpf quantities."""
    zq = q0**3 / (q0**2 + 1)
    H = q0 - 1 / q0
    alpha = (zq - 1) * H / 2
    hbar = (q0 - 1) / q0
    b = mp.sqrt(q0 ** 4 + q0 ** 2 + 1) / (q0 ** 2 + 1)
    u = b * hbar ** 2
    QA = M_E * mp.fabs(q0 ** 2 - 2 * q0 - 1) * (q0 + 1) / (2 * q0 ** 3)
    QN1 = QA * mp.cos(alpha - u / 2)
    QN2 = QN1 * (1 - u ** 2)  # c_2 = −1 (proved)
    c3 = (Q_AME / QN2 - 1) / u ** 3
    return {"q0": q0, "b": b, "u": u, "QA": QA, "QN1": QN1, "QN2": QN2, "c3": c3}


CH = {"proton": chain(Q0_PROTON), "muon": chain(Q0_MUON)}

# ---------------------------------------------------------------------------
# Cross-checks against the committed N3 witness.
#
# TWO DEFECTS FIXED HERE (bean qou-l4q3), and they compound:
#
#   1. WRONG ANCHOR. These compared `CH["muon"]` against a witness that is
#      PROTON-pinned. `q-beta-operator-valued-N3.witness.json` moved to the
#      experimental pin under the 2026-08-07 owner directive ("all production
#      code defaults to the experimental (proton) anchor") and this probe never
#      followed, so the check was comparing two anchors -- the layer straddle
#      AGENTS.md forbids, sitting inside a cross-check. Measured at 60 dps, the
#      probe's own chain reproduces that witness at the PROTON anchor to
#      1.6e-61 (b) / 8.7e-52 (QN2) / 2.3e-43 (c3), and misses at the muon
#      anchor by 3.4e-10 / 2.4e-8 / 0.0497. No tolerance is widened: the
#      residuals clear the unchanged 1e-25 / 1e-25 / 1e-20 floors by 20+
#      orders of magnitude.
#
#   2. FROZEN COPIES. The references were three hardcoded literals, snapshotted
#      from the N3 chain as it stood on 2026-07-11 -- i.e. at the RETIRED muon
#      pin (b matches that pin to 5.3e-19). A copy cannot track its source, so
#      the check went stale silently and the failure was read as a defect in
#      this probe. They are now READ FROM THE WITNESS at run time, which is
#      what makes the cross-check a cross-check.
#
# The guard was working the whole time -- it was correctly reporting that its
# own references had gone stale. Diagnosis: bean qou-l4q3.
# ---------------------------------------------------------------------------
with (_path_bridge.witness_path(
        "q-beta-operator-valued-N3.witness.json", HERE.parent)).open() as fh:
    _n3 = json.load(fh)
_n3 = _n3.get("data", _n3)
N3_WITNESS_B = mp.mpf(str(_n3["hoefsmit_b"]))
N3_WITNESS_QN2 = mp.mpf(str(_n3["Q_N2"]))
N3_WITNESS_C3 = mp.mpf(str(_n3["c_3_empirical_additive"]))

xchecks = [
    ("b_matches_N3_witness", CH["proton"]["b"] - N3_WITNESS_B, mp.mpf("1e-25")),
    ("QN2_matches_N3_witness",
     CH["proton"]["QN2"] - N3_WITNESS_QN2, mp.mpf("1e-25")),
    ("c3_matches_N3_witness_additive",
     CH["proton"]["c3"] - N3_WITNESS_C3, mp.mpf("1e-20")),
]
print(f"\n[{time.time()-T0:6.1f}s] empirical extraction (c_2 = −1 imposed; c_3 full-absorption)")
for name, delta, tol in xchecks:
    ok = mp.fabs(delta) < tol
    print(f"    xcheck {name}: |Δ| = {mp.nstr(mp.fabs(delta), 3)}  (tol {mp.nstr(tol,2)})  "
          f"{'✓' if ok else '✗ FAIL'}")

C3 = {a: CH[a]["c3"] for a in CH}
C3_SPREAD = mp.fabs(C3["proton"] - C3["muon"])
U_MU = CH["muon"]["u"]
SIG_C3_EXP = SIGMA_REL_QBETA / U_MU ** 3
SIG_C4_EXP = SIGMA_REL_QBETA / U_MU ** 4
SIG_C5_EXP = SIGMA_REL_QBETA / U_MU ** 5
print(f"\n    c_3(proton q₀) = {mp.nstr(C3['proton'], 30)}")
print(f"    c_3(muon   q₀) = {mp.nstr(C3['muon'], 30)}")
print(f"    anchor spread |Δc_3| = {mp.nstr(C3_SPREAD, 6)} "
      f"({mp.nstr(100*C3_SPREAD/mp.fabs(C3['muon']), 3)} %)")
print(f"    σ_exp propagation (780 ppb on Q_β): σ(c_3) ≈ {mp.nstr(SIG_C3_EXP, 4)}, "
      f"σ(c_4) ≈ {mp.nstr(SIG_C4_EXP, 4)}, σ(c_5) ≈ {mp.nstr(SIG_C5_EXP, 4)}")
print("    ⇒ c_4/c_5 carry NO scheme-independent empirical content "
      "(sequential extraction after empirical c_3 gives 0 identically;")
print("      recorded values presuppose imposed lower-rung forms; σ_exp ≥ 148 anyway)")

# ---------------------------------------------------------------------------
# Step 3+4 — numeric α_n per normalization × anchor + integrality distances
# ---------------------------------------------------------------------------

# data modes: primary (well-defined empirical content) + sensitivity
MODES = {
    "primary": {"c4": mp.mpf(0), "c5": mp.mpf(0),
                "note": "c_3 empirical per anchor; c_4=c_5=0 (full-absorption scheme "
                        "— the only scheme-independent empirical content)"},
    "sensitivity-extended-ck": {"c4": EXTENDED_CK_C4, "c5": EXTENDED_CK_C5,
                                "note": "recorded extended-ck central values "
                                        "(scheme-dependent: extraction imposed c_3=−2 "
                                        "at rung 3); demonstrates h⁸⁺ unresolvability"},
}


def eval_lin(parts, c3v, c4v, c5v):
    val = R2mp(parts["const"]) + R2mp(parts["c3"]) * c3v \
        + R2mp(parts["c4"]) * c4v + R2mp(parts["c5"]) * c5v
    sig_exp = (mp.fabs(R2mp(parts["c3"])) * SIG_C3_EXP
               + mp.fabs(R2mp(parts["c4"])) * SIG_C4_EXP
               + mp.fabs(R2mp(parts["c5"])) * SIG_C5_EXP)
    sig_anchor = mp.fabs(R2mp(parts["c3"])) * C3_SPREAD  # c_4/c_5 anchor spread undefined
    return val, sig_exp, sig_anchor


def dist_int(x):
    return mp.fabs(x - mp.nint(x))


def analyze(tab, c3v, c4v, c5v, n_lo, label):
    """Per order n: value A+B√3, distances to Z and Z[√3], resolvability."""
    rows = []
    for n in range(n_lo, N_ORD):
        A, sA_exp, sA_anc = eval_lin(tab[n]["A"], c3v, c4v, c5v)
        B, sB_exp, sB_anc = eval_lin(tab[n]["B"], c3v, c4v, c5v)
        sig_exp = sA_exp + sB_exp * mp.sqrt(3)
        sig_anc = sA_anc + sB_anc * mp.sqrt(3)
        exact = (sig_exp == 0)
        # ℤ test: need B ≈ 0 and A ≈ integer
        dist_Z = max(dist_int(A), mp.fabs(B) * mp.sqrt(3))
        # Z[√3] test: A ≈ integer and B ≈ integer
        dist_OK = max(dist_int(A), dist_int(B))
        resolvable_exp = exact or (sig_exp < mp.mpf("0.5"))
        resolvable_anc = exact or (sig_anc < mp.mpf("0.5"))
        tol_exp = mp.mpf("1e-30") if exact else 2 * sig_exp
        tol_anc = mp.mpf("1e-30") if exact else 2 * sig_anc
        rows.append({
            "n": n,
            "A": mp.nstr(A, 30), "B": mp.nstr(B, 30),
            "sigma_exp": fmt(mp.mpf(0) if exact else sig_exp),
            "sigma_anchor": fmt(mp.mpf(0) if exact else sig_anc),
            "exact_from_proved_c2": bool(exact),
            "dist_to_Z": fmt(dist_Z),
            "dist_to_ZSqrt3": fmt(dist_OK),
            "resolvable_sigma_exp": bool(resolvable_exp),
            "resolvable_anchor_only": bool(resolvable_anc),
            # compatibility judged against the uncertainty of the SAME reading
            # under which the order counts as resolvable (2σ tolerance):
            "compat_exp": bool(min(dist_Z, dist_OK) <= tol_exp),
            "compat_anchor": bool(min(dist_Z, dist_OK) <= tol_anc),
        })
    return rows


def print_rows(rows, label):
    print(f"\n  {label}")
    print(f"    {'n':>2}  {'A (rational part)':>24}  {'B (√3 part)':>24}  "
          f"{'d(Z)':>10}  {'d(Z[√3])':>10}  {'σ_exp':>9}  {'σ_anchor':>9}  res?")
    for r in rows:
        res = "EXACT" if r["exact_from_proved_c2"] else (
            "yes" if r["resolvable_sigma_exp"] else
            ("anchor-only" if r["resolvable_anchor_only"] else "NO"))
        # The row fields are `fmt` strings (lossless); render via mp.nstr.
        print(f"    {r['n']:>2}  {r['A'][:24]:>24}  {r['B'][:24]:>24}  "
              f"{mp.nstr(mp.mpf(r['dist_to_Z']), 4):>10}  "
              f"{mp.nstr(mp.mpf(r['dist_to_ZSqrt3']), 4):>10}  "
              f"{mp.nstr(mp.mpf(r['sigma_exp']), 3):>9}  "
              f"{mp.nstr(mp.mpf(r['sigma_anchor']), 3):>9}  {res}")


RESULTS = {}
for mode, mspec in MODES.items():
    RESULTS[mode] = {}
    for anchor in ("proton", "muon"):
        c3v = C3[anchor]
        rows_a = analyze(TAB_L, c3v, mspec["c4"], mspec["c5"], 4, "bare")
        rows_b = analyze(TAB_F, c3v, mspec["c4"], mspec["c5"], 1, "dressed")
        RESULTS[mode][anchor] = {"bare_ladder_L": rows_a, "prefactor_dressed_PL": rows_b}
        if mode == "primary":
            print("\n" + "-" * 92)
            print(f"  MODE={mode}  ANCHOR={anchor}  (c_3 = {mp.nstr(c3v, 20)}, c_4=c_5=0)")
            print_rows(rows_a, "(a) bare ladder L(q) = Π(1+c_k u^k), coefficients of h^n")
            print_rows(rows_b, "(b) dressed F(q) = P(q)·L(q), P = (Q_base/m_e)")

# ---------------------------------------------------------------------------
# Step 5 — verdict per normalization × anchor (kill criterion, pre-stated)
# ---------------------------------------------------------------------------


def verdict_for(rows):
    """Two readings, each judged self-consistently (resolvability AND 2σ
    compatibility from the same uncertainty source):
      σ_exp reading   — total experimental uncertainty (780 ppb on Q_β);
      anchor reading  — anchor-systematic only (treats the CODATA central
                        value as exact; the corpus's cross-anchor framing).
    NEGATIVE iff a resolvable order fails both Z and Z[√3] at 2σ."""
    out = {}
    for reading, res_key, comp_key in (
            ("sigma_exp", "resolvable_sigma_exp", "compat_exp"),
            ("anchor_only", "resolvable_anchor_only", "compat_anchor")):
        fails = [r["n"] for r in rows if r[res_key] and not r[comp_key]]
        passes = [r["n"] for r in rows if r[res_key] and r[comp_key]]
        v = "NEGATIVE" if fails else ("GATE-PASSED" if passes else "UNRESOLVABLE")
        out[reading] = {"verdict": v, "failing_resolvable_orders": fails,
                        "integer_compatible_resolvable_orders": passes}
    return out


print("\n" + "=" * 92)
print("  VERDICTS (kill criterion pre-stated in module docstring)")
print("=" * 92)
VERDICTS = {}
for mode in RESULTS:
    VERDICTS[mode] = {}
    for anchor in RESULTS[mode]:
        VERDICTS[mode][anchor] = {}
        for norm in RESULTS[mode][anchor]:
            vd = verdict_for(RESULTS[mode][anchor][norm])
            VERDICTS[mode][anchor][norm] = vd
            for reading, r in vd.items():
                print(f"  [{mode:>24}] [{anchor:>6}] [{norm:>20}] "
                      f"[{reading:>11}] → {r['verdict']:11}  "
                      f"fail@{r['failing_resolvable_orders']}  "
                      f"pass@{r['integer_compatible_resolvable_orders']}")

overall_negative = all(
    VERDICTS[m][a][n][rd]["verdict"] == "NEGATIVE"
    for m in VERDICTS for a in VERDICTS[m] for n in VERDICTS[m][a]
    for rd in VERDICTS[m][a][n])

SCOPE = (
    "NEGATIVE, scope-limited (a): the ladder is not the q=1 Taylor expansion of a "
    "Habiro-ring element under the natural normalizations tested (bare L; Q_base/m_e-"
    "dressed P·L; h vs ℏ_q basis is invariant so covered). This is NOT a structural (b) "
    "exclusion: it constrains these normalizations only — a non-Habiro analytic object "
    "(state integral / resummation, audit §3.B) or a different, structurally-motivated "
    "normalization remains open. Downstream: GSWZ descent (audit Appendix A) is gated on "
    "this result and dies with it under these normalizations."
    if overall_negative else
    "MIXED / GATE-PASSED under at least one normalization — see per-normalization table; "
    "integer-compatibility at resolvable orders would warrant the GSWZ descent follow-up."
)
print(f"\n  OVERALL: {'NEGATIVE (all normalizations × anchors × modes)' if overall_negative else 'MIXED'}")
print(f"  Scope: {SCOPE}")

# ---------------------------------------------------------------------------
# Witness emission
# ---------------------------------------------------------------------------
payload = {
    "description": (
        "PROBE 1 (audit 2026-07-11 §3.A): Habiro-integrality kill-test of the Q_β "
        "precision ladder. Symbolically Taylor-expands L(q) = Π_{k=2..5}(1+c_k·u^k), "
        "u = b(q)·ℏ_q², in h = q−1 over ℚ(√3)[c_3,c_4,c_5] (exact sympy series), plugs "
        "c_2 = −1 (PROVED) + per-anchor empirical c_3 (full-absorption extraction at "
        "proton and muon q₀ pins), and tests Habiro integrality (Z[[q−1]], secondary "
        "Z[√3] = O_{Q(√3)}) of the coefficients against propagated uncertainty "
        "(σ_exp(Q_β) = 780 ppb; anchor systematic). Normalizations: (a) bare L; "
        "(b) P·L with the q-dependent dimensionless prefactor P = (Q_base/m_e) = "
        "|q²−2q−1|(q+1)/(2q³)·cos(α−u/2); (c) h ↔ ℏ_q basis invariance VERIFIED "
        "symbolically. No fitted forms; no c_k value proposals (flip-flop guard)."
    ),
    "auditOnly": "Hypothesis-class test (not a c_k derivation); not in refuted classes C1–C14.",
    "data": {
        "hoefsmit_b_closed_form": "b(q)^2 = (q^4+q^2+1)/(q^2+1)^2 (rational in q); b(1) = sqrt(3)/2",
        "coefficient_ring": "Q(sqrt(3)); ring of integers O_K = Z[sqrt(3)] (3 = 3 mod 4)",
        "ladder": "L(q) = prod_{k=2..5} (1 + c_k u^k), u = b hbar_q^2, hbar_q = (q-1)/q",
        "prefactor": "P(q) = |q^2-2q-1|(q+1)/(2q^3) * cos(alpha - u/2), alpha = (z-1)(q-1/q)/2, z = sqrt(q)/(q+1)",
        "basis_invariance_h_vs_hbar": {
            "hbar_of_h_integer_series": bool(basis_fwd_integer),
            "h_of_hbar_integer_series": bool(basis_bwd_integer),
            "roundtrip_identity": bool(basis_roundtrip_ok),
            "unit_linear_terms": bool(unit_linear),
            "conclusion": "Z[sqrt3][[h]] = Z[sqrt3][[hbar_q]]; integrality basis-invariant (verified symbolically)",
        },
        "anchors": {
            "proton_q0": mp.nstr(Q0_PROTON, OUT_DPS),
            "muon_q0": mp.nstr(Q0_MUON, OUT_DPS),
        },
        "codata_chain": {
            "m_e_MeV": mp.nstr(M_E, 15),
            "Q_AME_MeV": mp.nstr(Q_AME, 30),
            "sigma_rel_Qbeta": "7.8e-7 (780 ppb CAL-2 floor, docs/precision-goals.md)",
        },
        "empirical_c3": {
            "convention": "full-absorption sequential extraction after proved c_2=-1 "
                          "(qbeta_ck_cache.py convention: c_3 = (Q_AME/Q_N2 - 1)/u^3)",
            "proton": mp.nstr(C3["proton"], OUT_DPS),
            "muon": mp.nstr(C3["muon"], OUT_DPS),
            "anchor_spread_abs": mp.nstr(C3_SPREAD, 12),
            "anchor_spread_pct": fmt(100 * C3_SPREAD / mp.fabs(C3["muon"])),
            "sigma_exp_c3": fmt(SIG_C3_EXP),
            "sigma_exp_c4": fmt(SIG_C4_EXP),
            "sigma_exp_c5": fmt(SIG_C5_EXP),
            "c4_c5_status": "no scheme-independent empirical value (full absorption at rung 3 "
                            "forces 0; recorded values presuppose imposed lower-rung forms; "
                            "sigma_exp >= 148 makes orders h^8+ unresolvable regardless)",
        },
        "resolvable_order_analysis": {
            "orders_4_5": "EXACT — depend only on proved c_2 = -1 and exact b(q) series; zero uncertainty",
            "orders_6_7": "c_3 enters; sigma_exp-propagated ~0.4-0.5 (marginal ~1sigma); "
                          "anchor-systematic-only ~0.02 (resolvable under that reading)",
            "orders_8_11": "c_4/c_5 enter; sigma >= ~80: UNRESOLVABLE at current experimental precision",
        },
        "series_tables": RESULTS,
        "symbolic_low_order_exact": {
            "bare_alpha_4": "-3/4 (exact; c_2 proved, b(1)^2 = 3/4)",
            "bare_alpha_5": str(sp.nsimplify(TAB_L[5]["A"]["const"])),
            "dressed_F_low_orders_const": {
                str(n): {"A": str(TAB_F[n]["A"]["const"]), "B_sqrt3": str(TAB_F[n]["B"]["const"])}
                for n in range(0, 8)
            },
        },
    },
    "verdicts": VERDICTS,
    "overall_verdict": ("NEGATIVE" if overall_negative else "MIXED"),
    "scope_classification": SCOPE,
}

# mpf end to end -- `float(delta)` truncated cross-check residuals as small as
# 5e-71 to 17 digits on the way into the witness, i.e. the assertion recorded
# less than the check measured.
ASSERTIONS = [
    ("b_squared_three_forms_agree_symbolically", mp.mpf(1), mp.mpf(1), mp.mpf(0),
     "sympy simplify == 0 (exact)"),
    ("basis_invariance_h_hbar_verified",
     mp.mpf(1) if basis_invariant else mp.mpf(0), mp.mpf(1), mp.mpf(0),
     "hbar=h/(1+h), h=hbar/(1-hbar) both in Z[[.]] with unit linear term; round-trip id"),
    ("bare_alpha4_equals_minus_three_quarters_exact",
     R2mp(TAB_L[4]["A"]["const"]), mp.mpf("-0.75"), mp.mpf(0),
     "exact sympy rational; c_2 = -1 Lean-proved (PR #1602)"),
] + [
    (name, delta, mp.mpf(0), tol,
     "committed witness cross-check (q-beta-operator-valued-N3.witness.json)")
    for name, delta, tol in xchecks
]

try:
    from witness_base import WitnessBuilder, q0_comparison  # noqa: E402
    builder = WitnessBuilder.wrap_legacy(
        "qbeta-habiro-integrality-kill-test", payload,
        script_path=__file__, engine="sympy+mpmath")
    for name, computed, expected, tol, source in ASSERTIONS:
        builder.add_assertion(name, computed, expected,
                              tolerance=tol, source=source)
    out_path = builder.save(q0_comparison(
        muon=Q0_MUON, proton=Q0_PROTON,
        reason="computes empirical c_3 and Habiro integrality tests at BOTH pins on purpose (CH['proton'], CH['muon'], and |c_3(proton) - c_3(muon)| anchor spread); bean qou-fl0a",
    ))
except Exception as exc:  # fall back to plain JSON (exemplar probe pattern)
    from datetime import datetime, timezone
    payload.update({
        "engine": "sympy+mpmath",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "computation": "qbeta-habiro-integrality-kill-test",
        "scriptFile": Path(__file__).name,
        "precisionMetadata": {"compute_dps": mp.mp.dps, "output_dps": OUT_DPS},
        "assertions": [
            {"name": n_, "computed": c_, "expected": e_, "tolerance": t_,
             "passed": bool(abs(c_ - e_) <= max(t_, 0.0)), "source": s_}
            for n_, c_, e_, t_, s_ in ASSERTIONS
        ],
        "witness_builder_fallback_reason": repr(exc),
    })
    payload["allPassed"] = all(a["passed"] for a in payload["assertions"])
    out_path = HERE / "qbeta-habiro-integrality-kill-test.witness.json"
    with open(out_path, "w") as f:
        json.dump(payload, f, indent=2, default=str)

print(f"\n[{time.time()-T0:6.1f}s] witness → {out_path}")
