#!/usr/bin/env python3
"""Scan c2/c3/c4^even ladder for H3 baseline + the 3 route-A H4 objects (bean 8we6).

Stability gate: an H4 object is VALID only if c2^even ~= -8.00641 and
c3^even ~= +86.66116 (the trusted H3 rungs).  c4^even is then the genuine new
rung.  Uses the exact ladder from qbeta_c3even_exact_sseries_probe.py.
Heavy (sqrt series, deg-16 rational per object) -> run backgrounded with tee.
"""
import time
import sympy as sp
import qbeta_h4_nucleon_assembly as A

q = A.q
s = sp.Symbol("s")
KC, NS = 4, 10
q0 = sp.Rational(110998, 100000)


def ladder(dnet, label):
    t0 = time.monotonic()
    dn0 = float(dnet.subs(q, q0))
    sgn = 1 if dn0 > 0 else -1
    dnet_reg = sp.cancel(dnet / (q - 1))
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    Qb = sgn * dnet_reg / q
    Rq = Qb / (QA * sp.cos(alpha_eff))
    R1 = sp.simplify(Rq.subs(q, 1))
    logR = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, NS + 1).removeO()
    us = sp.series(u.subs(q, 1 + s), s, 0, NS + 1).removeO()
    logR_c = [sp.simplify(logR.coeff(s, i)) for i in range(NS + 1)]
    u_c = [sp.simplify(us.coeff(s, i)) for i in range(NS + 1)]
    print(f"  [{label}] series done in {time.monotonic()-t0:.0f}s", flush=True)

    def sm(a, bb):
        return [sp.expand(sum(a[i] * bb[n - i] for i in range(n + 1))) for n in range(NS + 1)]

    upow = {1: u_c}
    for k in range(2, KC + 2):
        upow[k] = sm(upow[k - 1], u_c)
    c = {}
    model = [sp.Integer(0)] * (NS + 1)
    for k in range(2, KC + 1):
        o = 2 * k
        ck = sp.simplify((logR_c[o] - model[o]) / upow[k][o])
        c[k] = ck
        cku = [sp.expand(ck * t) for t in upow[k]]
        cur = [sp.Integer(1)] + [sp.Integer(0)] * NS
        n = 1
        while n * o <= NS:
            cur = sm(cur, cku)
            sgn2 = sp.Integer((-1) ** (n + 1))
            for i in range(NS + 1):
                model[i] = sp.expand(model[i] + sgn2 * cur[i] / n)
            n += 1
    return {k: sp.N(v, 30) for k, v in c.items()}, sgn


def dnet_of(tn, tp):
    return sp.simplify(A.augmentation(A.nucleon_nf(tn)) - A.augmentation(A.nucleon_nf(tp)))


def main():
    objs = [
        ("H3 (ref)", ["u", "d", "d"], ["u", "u", "d"]),
        ("H4 lepton", ["u", "d", "d", "e"], ["u", "u", "d", "e"]),
        ("H4 brane", ["u", "d", "d", "b"], ["u", "u", "d", "b"]),
    ]
    rows = []
    for name, tn, tp in objs:
        t0 = time.monotonic()
        dn = dnet_of(tn, tp)
        c, sgn = ladder(dn, name)
        rows.append((name, c, sgn, A.max_word_len(A.nucleon_nf(tn))))
        print(f"[{name}] sgn={sgn} maxlen={rows[-1][3]}  c2={float(c[2]):+.5f} "
              f"c3={float(c[3]):+.5f} c4={float(c[4]):+.4f}  ({time.monotonic()-t0:.0f}s)",
              flush=True)
    print("\n=== SUMMARY ===")
    print(f"{'object':12s} {'c2^even':>13s} {'c3^even':>13s} {'c4^even':>13s}")
    for name, c, sgn, ml in rows:
        print(f"{name:12s} {float(c[2]):+13.5f} {float(c[3]):+13.5f} {float(c[4]):+13.4f}")
    print("\nGATE target: c2=-8.00641, c3=+86.66116")
    for name, c, sgn, ml in rows:
        if name == "H3 (ref)":
            continue
        g2 = abs(float(c[2]) + 8.00641) < 0.05
        g3 = abs(float(c[3]) - 86.66116) < 0.5
        verdict = "PASS (valid object)" if (g2 and g3) else "FAIL (lower rung moved -> object wrong)"
        print(f"  {name}: c2 gate {'ok' if g2 else 'X'}, c3 gate {'ok' if g3 else 'X'} -> {verdict}")


if __name__ == "__main__":
    main()
