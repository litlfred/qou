#!/usr/bin/env python3
"""Route 2, option 1 (beans qou-99qc, qou-pzsi): ropelength Lambda = L / tau on Bring.

Implements preregistration-option1.md. No Q_beta / CODATA / mass input anywhere.

tau(gamma) = 1/2 min d_H(A, hA) over h in Gamma_B = pi_1(Bring) not preserving the
lifted axis A (conjugated to the imaginary axis by bring_loop_energy_probe.loop_setup).
For hA with endpoints e0 = h(0), e1 = h(inf):
    opposite signs or a shared endpoint -> 0 (the loop crosses itself, Lambda = +inf);
    otherwise cosh d = (|e0| + |e1|) / | |e0| - |e1| |.

Search radius (self-certifying, preregistration §3).  Let p on A and p' = h(q) on hA
realise 2*tau.  Left-multiplying h by a power of the loop element moves p by multiples
of L; right-multiplying moves q by multiples of L; neither changes the distance.  So
WLOG d(m, p) <= L/2 and d(q, m) <= L/2 with m = i the segment midpoint, and
    d(m, h m) <= d(m, p) + d(p, p') + d(h q, h m) <= L + 2 tau.
A first pass at R0 = 1.5 L finds 2 tau*.  If L + 2 tau* <= R0 the minimum is certified;
otherwise re-enumerate at L + 2 tau* (>= L + 2 tau_true) and repeat.

Rigorous shortcut for long loops (reported, never used to rank).  A loop with an
embedded collar of half-width tau has collar area 2 L sinh(tau) <= area(Bring) = 12 pi,
so tau <= asinh(6 pi / L) and Lambda >= L / asinh(6 pi / L).  A loop whose lower bound
exceeds the smallest computed Lambda cannot be the minimiser, so its tau is not
enumerated (enumeration cost grows like e^L).

Arithmetic: mpmath mpf at 30 dps; no float64.
"""
import itertools
import json
import sys
from math import gcd, isqrt
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).parent))
import bring_route2_probe as R2  # noqa: E402
import bring_loop_energy_probe as E  # noqa: E402

mp.mp.dps = 30
R2.mp.mp.dps = 30
DIGITS = 25
AREA = 12 * mp.pi  # 4 pi (g - 1), g = 4


def canon(w):
    c = []
    for v in (w, tuple(1 - x for x in w)):
        for k in range(len(v)):
            c.append(v[k:] + v[:k])
    return min(c)


def route2_row(word):
    g = R2.sl2z(list(word))
    fixed = [p for p in ("inf", 0, 1) if R2.act_p1f2(g, p) == p]
    row = {"word": "".join(map(str, word)), "sl2z": g}
    if len(fixed) != 1:
        row["status"] = "no loop (permutation does not fix exactly one point)"
        return row
    h = R2.H_TO_INF[fixed[0]]
    gp = R2.imul(R2.imul(h, g), R2.inv(h))
    M = R2.to_h4(gp)
    hw = R2.rosen_word(M)
    r = R2.h4_5_order(M)
    s, u = R2.delta245()
    trd = R2.word_trace_delta(hw, s, u)
    row["h4_word"] = [list(x) for x in hw]
    row["r_congruence_H4(5)"] = r
    if abs(trd) > 2 + mp.mpf(10) ** -25 and r:
        row["status"] = "loop"
        row["L"] = r * 2 * mp.acosh(abs(trd) / 2)
    else:
        row["status"] = "no loop (elliptic or parabolic in Delta(2,4,5))"
    return row


def axis_distance(h):
    a, b, c, d = h
    tiny = mp.mpf(10) ** -20
    if abs(c) < tiny or abs(d) < tiny:
        return mp.mpf(0)  # shares an endpoint with the axis
    e0, e1 = b / d, a / c
    if (e0 > 0) != (e1 > 0):
        return mp.mpf(0)  # crosses the axis
    x, y = abs(e0), abs(e1)
    return mp.acosh((x + y) / abs(x - y))


def thickness(st):
    L = st["L"]
    R = mp.mpf(3) / 2 * L
    while True:
        ker, nseen = E.enumerate_kernel(st["gens"], R, mp.mpf(1))
        stab = [h for h in ker if E.is_axis_stabiliser(h)]
        tl = {mp.nstr(2 * mp.acosh(abs(h[0] + h[3]) / 2), 20) for h in stab
              if abs(h[0] + h[3]) > 2 + mp.mpf(10) ** -15}
        primitive = all(x == mp.nstr(L, 20) or mp.mpf(x) >= L for x in tl)
        nonstab = [h for h in ker if not E.is_axis_stabiliser(h)]
        d2 = min(axis_distance(h) for h in nonstab)
        if L + d2 <= R:
            return {"tau": d2 / 2, "radius": R, "certified": True, "primitive": primitive,
                    "kernel_elements": len(ker), "delta_elements": nseen}
        R = L + d2


# ---------------------------------------------------------- GL(2,Z) conjugacy (exact)
def cf_period(M):
    """Cyclic CF period of the attracting fixed point of a hyperbolic integer matrix,
    canonicalised; equal periods <=> fixed points GL(2,Z)-equivalent."""
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    tr = a + d
    if c == 0:
        return None
    D = (d - a) ** 2 + 4 * b * c
    sgn = 1 if tr > 0 else -1  # attracting fixed point: eigenvalue c x + d has the sign of tr
    # x = (a - d + sgn*sqrt(D)) / (2c), written as (P + sqrt(D)) / Q
    P, Q = (a - d) * sgn, 2 * c * sgn
    if (D - P * P) % Q:
        P, Q, D = P * abs(Q), Q * abs(Q), D * Q * Q
    seen, terms = {}, []
    rD = isqrt(D)
    for i in range(10000):
        key = (P, Q)
        if key in seen:
            per = terms[seen[key]:]
            rots = [tuple(per[k:] + per[:k]) for k in range(len(per))]
            return min(rots)
        seen[key] = i
        # floor((P + sqrt D) / Q), sqrt D irrational
        aa = (P + rD) // Q if Q > 0 else -((P + rD) // (-Q)) - 1
        terms.append(aa)
        P = aa * Q - P
        Q = (D - P * P) // Q
    raise RuntimeError("CF period not found")


def gl2z_class(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    tr = a + d
    if abs(tr) > 2:
        return ("hyp", abs(tr), cf_period(M))
    if abs(tr) == 2:
        s = 1 if tr > 0 else -1
        return ("par", s, gcd(gcd(abs(a - s), abs(b)), gcd(abs(c), abs(d - s))))
    return ("ell", tr)


def main():
    checks = {}
    classes = {}
    for w in itertools.product((0, 1), repeat=11):
        classes.setdefault(canon(w), []).append(w)
    checks["class_count_is_94"] = len(classes) == 94
    seen = {canon(tuple(v)) for v in R2.CANDIDATES.values() if len(v) == 11}
    fresh = [c for c in sorted(classes) if c not in seen]
    s_mp, u_mp = R2.delta245()
    rho, sigmas = R2.s5_epimorphisms()

    # reproduction check (preregistration §6.1)
    for name in ("gluon_s1_s0", "nuc11_gen_grouped"):
        row = route2_row(tuple(R2.CANDIDATES[name]))
        ref = json.loads(Path(__file__).with_name("results.json").read_text())["rows"][name]["bring_length"]
        checks[f"reproduce_L_{name}"] = mp.nstr(row["L"], DIGITS) == mp.nstr(mp.mpf(ref), DIGITS)

    rows = [route2_row(c) for c in fresh]
    loops = sorted([r for r in rows if r["status"] == "loop"], key=lambda r: r["L"])
    best = None
    for r in loops:
        L = r["L"]
        r["Lambda_lower_bound"] = L / mp.asinh(6 * mp.pi / L)
        if best is not None and r["Lambda_lower_bound"] > best * (1 + mp.mpf(10) ** -DIGITS):
            r["Lambda"] = "not enumerated: lower bound exceeds the computed minimum"
            print(f"{r['word']} L={mp.nstr(L, 10)} skipped (bound {mp.nstr(r['Lambda_lower_bound'], 8)})", flush=True)
            continue
        st = E.loop_setup(r["word"], s_mp, u_mp, sigmas[0], rho, row=r)
        checks[f"loop_L_matches_{r['word']}"] = mp.nstr(st["L"], DIGITS) == mp.nstr(L, DIGITS)
        th = thickness(st)
        r.update({k: v for k, v in th.items()})
        checks[f"radius_certified_{r['word']}"] = th["certified"]
        if th["tau"] == 0 or not th["primitive"]:
            r["Lambda"] = mp.inf
        else:
            r["Lambda"] = L / th["tau"]
            best = r["Lambda"] if best is None else min(best, r["Lambda"])
        print(f"{r['word']} L={mp.nstr(L, 12)} tau={mp.nstr(th['tau'], 12)} "
              f"Lambda={mp.nstr(r['Lambda'], 15)} |ker|={th['kernel_elements']}", flush=True)

    finite = [r for r in loops if isinstance(r.get("Lambda"), mp.mpf) and r["Lambda"] != mp.inf]
    key = lambda v: mp.nstr(v, DIGITS)  # noqa: E731
    lam_min = min(r["Lambda"] for r in finite)
    winners = [r for r in finite if key(r["Lambda"]) == key(lam_min)]
    wclasses = {}
    for r in winners:
        wclasses.setdefault(gl2z_class(r["sl2z"]), []).append(r["word"])
    lam_pass = len(wclasses) == 1
    l_min = loops[0]["L"]
    l_winners = [r for r in loops if key(r["L"]) == key(l_min)]
    lclasses = {}
    for r in l_winners:
        lclasses.setdefault(gl2z_class(r["sl2z"]), []).append(r["word"])

    def ranks(vals):
        from collections import Counter
        return sorted(Counter(vals).items(), key=lambda kv: mp.mpf(kv[0]))

    summary = {
        "fresh_classes": len(fresh), "loops": len(loops),
        "no_loop": len(rows) - len(loops),
        "Lambda_min": key(lam_min), "Lambda_minimisers": [r["word"] for r in winners],
        "Lambda_minimiser_distinct_GL2Z_classes": len(wclasses),
        "Lambda_PASS": lam_pass,
        "Lambda_value_multiplicities": ranks([key(r["Lambda"]) for r in finite]),
        "L_min": key(l_min), "L_minimisers": len(l_winners),
        "L_minimiser_distinct_GL2Z_classes": len(lclasses),
        "L_PASS": len(lclasses) == 1,
        "L_value_multiplicities": ranks([key(r["L"]) for r in loops]),
        "self_crossing": [r["word"] for r in loops if r.get("Lambda") == mp.inf],
    }
    print(json.dumps(summary, indent=1, default=str))
    for k, v in checks.items():
        if not v:
            print("FAIL " + k)
    print("checks:", sum(checks.values()), "/", len(checks), "pass")

    def ser(r):
        out = {}
        for k, v in r.items():
            out[k] = mp.nstr(v, DIGITS) if isinstance(v, mp.mpf) else v
        return out

    Path(__file__).with_name("results_option1.json").write_text(json.dumps(
        {"recipe": "preregistration-option1.md", "mp_dps": mp.mp.dps, "summary": summary,
         "checks": checks, "rows": [ser(r) for r in rows]}, indent=1, default=str) + "\n")
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
