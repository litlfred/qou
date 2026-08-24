#!/usr/bin/env python3
"""
HIGH-PRECISION α* determination: pin down the optimal blend
parameter to many significant digits, then test candidate
closed forms exhaustively.

Strategy:
  1. Use mpmath bisection (not scipy) at dps=50 to get α* to
     ~15+ correct digits.
  2. Test candidates: G/3, G/π, q-algebraic forms, simple rationals,
     volume ratios, BCH-type expressions.
  3. Identify the candidate that matches α* to highest precision.

This is the BLOCKING input for formal derivation: we need to know
*exactly* what α* equals before we can prove it.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — Phase 5, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys, json, warnings
from pathlib import Path
from datetime import datetime, timezone
from itertools import combinations

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))
from witness_base import WitnessBuilder  # noqa: E402

import mpmath as mp
from _precision import set_compute_dps, fmt  # noqa: E402
set_compute_dps()

from hecke_core import (_PROTON_G0, _PROTON_G1, _NEUTRON_G0, _NEUTRON_G1,
                          h as H_A_F, z as Z_MARKOV)
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from experimental_constants import M_P_MEV, M_N_MEV

Q0 = Q_MP; QI = Q_INV_MP  # was f64 roundtrip
z_m = mp.mpf(str(float(Z_MARKOV)))
h_f = float(H_A_F)
hQ = Q0 - QI
D = Q0**4 + 4*Q0**2 + 1
w_s = Q0**2/D; w_t = (Q0**2+1)**2/D; w_a = Q0**2/D


def Phi_q(v, max_it=3000):
    if not isinstance(v, mp.mpf): v = mp.mpf(str(float(v)))
    if v >= 1: return mp.mpf('inf')
    p = mp.mpf(1); c = mp.mpf(1)/Q0
    for _ in range(max_it):
        t = mp.mpf(1) - c*v
        if abs(t) < mp.mpf('1e-50'): return mp.mpf('inf')
        p /= t
        if abs(c*v) < mp.mpf('1e-70'): break
        c /= Q0
    return p


def S_chain(chain):
    out = []
    for c, d in chain:
        cf, df = float(c), float(d)
        if abs(cf-1)<1e-10 and abs(df)<1e-10: out.append((1.0, -h_f))
        elif abs(cf-1)<1e-10 and abs(df+h_f)<1e-10: out.append((1.0, 0.0))
        else: out.append((c, d))
    return out


def sym_alt(chain):
    s = a = mp.mpf(1)
    for c, d in chain:
        s *= (mp.mpf(c)*Q0 + mp.mpf(d))
        a *= (-mp.mpf(c)/Q0 + mp.mpf(d))
    return s, a


def std_za_b(chain):
    zv = mp.mpf(1)/(mp.sqrt(Q0)+mp.sqrt(QI))
    a = mp.mpf(0); b = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        a, b = a*(cm*hQ+dm)+b*cm, a*cm+b*dm
    return zv*a + b


def std_det(chain):
    Dv = mp.mpf(1)
    for c, d in chain:
        cm, dm = mp.mpf(c), mp.mpf(d)
        Dv *= (dm*(cm*hQ + dm) - cm*cm)
    return Dv


def V_blend(chain, alpha):
    s_o, a_o = sym_alt(chain)
    s_s, a_s = sym_alt(S_chain(chain))
    std_o = std_za_b(chain); std_s = std_za_b(S_chain(chain))
    std_frob = (std_o + std_s) / 2
    std_det_v = mp.sqrt(mp.fabs(std_det(chain)))
    std_bl = alpha * std_frob + (1 - alpha) * std_det_v
    return w_s*((s_o+s_s)/2) + w_t*std_bl + w_a*((a_o+a_s)/2)


def tower(V_list):
    abs_V = [mp.fabs(v) for v in V_list]
    n = len(abs_V)
    prod = mp.mpf(1)
    for v in abs_V: prod *= v
    total = prod
    for k in range(1, n+1):
        for sub in combinations(range(n), k):
            pv = mp.mpf(1)
            for i in sub: pv *= abs_V[i]
            if pv >= 1: continue
            span = max(sub)-min(sub) if k >= 2 else 0
            total += z_m**(2*span) * Phi_q(pv)
    return total


def err_n_mp(alpha):
    """Return mpmath error (in %)."""
    a = alpha if isinstance(alpha, mp.mpf) else mp.mpf(str(alpha))
    Vp0 = V_blend(_PROTON_G0, a); Vp1 = V_blend(_PROTON_G1, a)
    Vn0 = V_blend(_NEUTRON_G0, a); Vn1 = V_blend(_NEUTRON_G1, a)
    mp_v = tower([Vp0, Vp1]); mn_v = tower([Vn0, Vn1])
    if mp_v == 0: return mp.mpf('nan')
    E0 = mp.mpf(str(M_P_MEV)) / mp_v
    mn_MeV = mn_v * E0
    return (mn_MeV - mp.mpf(str(M_N_MEV))) / mp.mpf(str(M_N_MEV)) * 100


def main() -> int:
    print("=" * 100)
    print("HIGH-PRECISION α* DETERMINATION (dps=50)")
    print("=" * 100)
    print(f"  q_0 = {Q0_FLOAT}")
    print(f"  M_p = {M_P_MEV},  M_n = {M_N_MEV}")
    print()

    # Bisection to high precision
    a_lo = mp.mpf('0.30')
    a_hi = mp.mpf('0.32')
    e_lo = err_n_mp(a_lo); e_hi = err_n_mp(a_hi)
    print(f"  Bracket: err({a_lo}) = {float(e_lo):+.6f}%, err({a_hi}) = {float(e_hi):+.6f}%")
    if e_lo * e_hi >= 0:
        # The bracket is hardcoded and no longer contains the root. Say WHERE
        # the root actually is instead of just that it is missing: the old
        # message reported nothing actionable, and it went to stdout, so a
        # harness capturing stderr recorded rc=1 with an empty error.
        #
        # This does NOT move the bracket. err_n_mp is monotone here, so the
        # scan is a diagnostic, not a search -- re-centring it would replace a
        # PUBLISHED alpha* and needs a deliberate decision, not a silent widen.
        # See bean qou-2zjp: the committed alpha* = 0.30580743... is a
        # CONVENTION-C value, and the root moved +14.741% when convention D
        # landed (z 0.4993 -> 0.6127, commit 6086572c4e). This producer imports
        # `z as Z_MARKOV`, so it consumes the parameter that moved.
        print("  ERROR: no sign change in bracket", file=sys.stderr)
        print(f"  bracket [{a_lo}, {a_hi}]: err = {mp.nstr(e_lo, 6)}%, "
              f"{mp.nstr(e_hi, 6)}% -- same sign, so no root inside",
              file=sys.stderr)
        prev = None
        for i in range(0, 41):
            a = mp.mpf(i) / 50
            try:
                e = err_n_mp(a)
            except Exception:  # noqa: BLE001 - a diagnostic must not itself crash
                prev = None
                continue
            if (prev is not None and mp.isfinite(e) and mp.isfinite(prev[1])
                    and (e > 0) != (prev[1] > 0)):
                print(f"  the root is between {mp.nstr(prev[0], 4)} and "
                      f"{mp.nstr(a, 4)}, outside the hardcoded bracket. "
                      f"Do NOT widen without reading bean qou-2zjp: the "
                      f"committed alpha* is convention-C and re-centring "
                      f"changes a published value.", file=sys.stderr)
                break
            prev = (a, e)
        else:
            print("  no sign change anywhere in [0, 0.8] either", file=sys.stderr)
        return 1
    for it in range(80):
        a_mid = (a_lo + a_hi) / 2
        e_mid = err_n_mp(a_mid)
        if e_mid * e_lo < 0:
            a_hi = a_mid; e_hi = e_mid
        else:
            a_lo = a_mid; e_lo = e_mid
        if abs(a_hi - a_lo) < mp.mpf('1e-30'):
            break
    alpha_star = (a_lo + a_hi) / 2
    print(f"  α* = {mp.nstr(alpha_star, 25)}")
    print(f"  err_n(α*) = {mp.nstr(err_n_mp(alpha_star), 5)} %")
    print()

    # Candidate closed forms
    G = mp.catalan
    pi = mp.pi
    e = mp.e
    q = Q0; qi = QI

    candidates = [
        # Catalan-based
        ('G/3', G/3),
        ('G·8/24 (Vol(B_3)/|S_4|)', 8*G/24),
        ('G/π', G/pi),
        ('G/e', G/e),
        ('G·π/9.4...', None),
        ('2G/(2π)', G/pi),
        ('(4G-1)/9.66...', None),
        # Pi/e based
        ('1/π', 1/pi),
        ('e/9', e/9),
        ('π/10', pi/10),
        ('π²/32', pi**2/32),
        ('1/(π·√(...))', None),
        # Simple rationals
        ('1/3', mp.mpf(1)/3),
        ('11/36', mp.mpf(11)/36),
        ('7/23', mp.mpf(7)/23),
        ('19/62', mp.mpf(19)/62),
        # q-algebraic (acknowledged PSLQ-search basis — no CAL-4 disguise)
        ('1/[3]_q', 1/(q**2 + 1 + qi**2)),
        ('1/(2·[2]_q)', 1/(2*(q + qi))),
        ('(q-1)/(q+1)', (q-1)/(q+1)),  # noqa: P31 — generic q-rational basis element
        ('h_q/[3]_q', hQ/(q**2 + 1 + qi**2)),
        ('h_q²/[2]_q²', hQ**2/(q+qi)**2),
        ('1/(q+q⁻¹+1)', 1/(q + qi + 1)),
        ('1 - 2/[3]_q', 1 - 2/(q**2 + 1 + qi**2)),
        # Volume / dimension ratios
        ('Vol(4_1)/|...| = 4G/...', None),
        ('1/π · (1+ε)', None),
        # Catalan-pi mixes
        ('G·(π-1)/π·...', None),
        ('(G+1/π)/2', (G + 1/pi)/2),
        ('G·(1-1/π²)', G*(1 - 1/pi**2)),
        # Try elliptic / theta
        ('K(1/√2)/...', None),  # K = π/2 · 2F1(1/2,1/2;1;1/2)
        # Simple trig
        ('sin(π/10)', mp.sin(pi/10)),
        ('cos(π·2/5)', mp.cos(2*pi/5)),
        ('1/(2cos(π/5))', 1/(2*mp.cos(pi/5))),
    ]

    rows = []
    for name, val in candidates:
        if val is None:
            continue
        v_mp = mp.mpf(val) if not isinstance(val, mp.mpf) else val
        diff = v_mp - alpha_star
        rel = abs(diff) / alpha_star
        rows.append((name, v_mp, diff, rel))

    # Sort by closeness
    rows.sort(key=lambda r: r[3])

    print(f"  Candidates ranked by closeness to α*:")
    print(f"  {'name':<30} {'value':<22} {'diff':<22} {'rel ppm':>15}")
    for name, val, diff, rel in rows[:20]:
        print(f"  {name:<30} {mp.nstr(val,18):<22} {mp.nstr(diff,8):<22} {float(rel*1e6):>15.3f}")
    print()

    # Polynomial integer relation search via PSLQ (mpmath identify)
    print(f"  Attempting integer-relation identification via mpmath.identify:")
    try:
        ident = mp.identify(alpha_star, [G, pi, mp.mpf(1)/pi, G/pi, 1/G],
                              ['pi', 'G'], tol=mp.mpf('1e-25'))
        print(f"    identify result: {ident}")
    except Exception as ex:
        print(f"    identify failed: {ex}")

    # PSLQ on (α*, G, 1/π, 1, π)
    print(f"\n  PSLQ on (α*, G, 1/π, 1, π):")
    try:
        rel = mp.pslq([alpha_star, G, 1/pi, mp.mpf(1), pi],
                       tol=mp.mpf('1e-25'), maxcoeff=10**6)
        print(f"    relation: {rel}")
        if rel:
            terms = [('α*', rel[0]), ('G', rel[1]), ('1/π', rel[2]),
                     ('1', rel[3]), ('π', rel[4])]
            print(f"    {' + '.join(f'{c}·{n}' for n,c in terms)} ≈ 0")
            # Solve for α*
            if rel[0] != 0:
                expr = (-rel[1]*G - rel[2]/pi - rel[3] - rel[4]*pi) / rel[0]
                print(f"    => α* = {mp.nstr(expr, 25)}")
                print(f"    diff = {mp.nstr(expr - alpha_star, 8)}")
    except Exception as ex:
        print(f"    PSLQ failed: {ex}")

    # Also try (α*, G, π, 1) only
    print(f"\n  PSLQ on (α*, G, π, 1):")
    try:
        rel = mp.pslq([alpha_star, G, pi, mp.mpf(1)],
                       tol=mp.mpf('1e-25'), maxcoeff=10**6)
        print(f"    relation: {rel}")
    except Exception as ex:
        print(f"    PSLQ failed: {ex}")

    # PSLQ on (α*, G) only (test if α* is rational multiple of G)
    print(f"\n  PSLQ on (α*, G):")
    try:
        rel = mp.pslq([alpha_star, G], tol=mp.mpf('1e-20'), maxcoeff=10**6)
        print(f"    relation: {rel}")
        if rel and rel[1] != 0:
            ratio = -mp.mpf(rel[0])/mp.mpf(rel[1])
            print(f"    => α*/G = {mp.nstr(ratio, 25)}")
    except Exception as ex:
        print(f"    PSLQ failed: {ex}")

    # PSLQ on (α*, G, q_0, h_q)
    print(f"\n  PSLQ on (α*, G, q, h_q):")
    try:
        rel = mp.pslq([alpha_star, G, Q0, hQ],
                       tol=mp.mpf('1e-22'), maxcoeff=10**6)
        print(f"    relation: {rel}")
    except Exception as ex:
        print(f"    PSLQ failed: {ex}")

    witness = {
        'computation': 'alpha-high-precision',
        'description': (
            'Bisect α* at dps=50 then run PSLQ to identify '
            'closed form for the optimal blend coefficient.'
        ),
        'timestamp': datetime.now(timezone.utc).isoformat(),
        'q_0': Q0_FLOAT,
        'alpha_star': mp.nstr(alpha_star, 25),
        'alpha_star_float': float(alpha_star),
        'G_over_3': float(G/3),
        'diff_G_over_3_ppm': float(abs(alpha_star - G/3)/alpha_star * 1e6),
        'best_candidates': [(n, mp.nstr(v, 18), float(r)) for n,v,d,r in rows[:10]],
    }
    out = WitnessBuilder.wrap_legacy("alpha-high-precision", witness, script_path=__file__, engine="mpmath").save()
    print(f"\n  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
