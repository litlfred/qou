#!/usr/bin/env python3
"""g-linear-response test for the lepton/brane route-A objects (bean 8we6).

The full-coupling (g=1) scan showed both explicit 4th-strand routes MOVE the
trusted rungs c2^even/c3^even (lepton -8.006->-6.84; brane -8.006->+3.99).  The
stability gate says "in whatever LIMIT removes the coupling"; so the sharp
question is the g->0 linear response: is the 4th strand a PURE-c4 perturbation
(dc2/dg|0 = dc3/dg|0 = 0) or does it contaminate the lower rungs at linear
order?  Interpolated crossing C(g)=(1-g)I+g*P (g=0 -> H3 exactly, verified).

Reads c_k at g=1/10; combines with the exact g=0 (H3) rungs and the g=1 scan to
estimate dc_k/dg|0 ~= (c_k(1/10)-c_k(0))/(1/10).  Heavy (sqrt series) -> tee.
"""
import time
import sympy as sp
import qbeta_h4_nucleon_assembly as A

q = A.q
s = sp.Symbol("s")
KC, NS = 4, 10
q0 = sp.Rational(110998, 100000)

# exact H3 (g=0) rungs from the committed scan
C0 = {2: sp.Float("-8.00641", 20), 3: sp.Float("86.66116", 20), 4: sp.Float("-1819.7407", 20)}


def ladder(dnet, label):
    t0 = time.monotonic()
    sgn = 1 if float(dnet.subs(q, q0)) > 0 else -1
    dnet_reg = sp.cancel(dnet / (q - 1))
    hbar = (q - 1) / q
    b = sp.sqrt(q**4 + q**2 + 1) / (q**2 + 1)
    u = b * hbar**2
    z = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
    h = q - 1 / q
    alpha_eff = (z - 1) * h / 2 - u / 2
    QA = (2 * q + 1 - q**2) * (q + 1) / (2 * q**3)
    Rq = (sgn * dnet_reg / q) / (QA * sp.cos(alpha_eff))
    R1 = sp.simplify(Rq.subs(q, 1))
    logR = sp.series(sp.log(Rq.subs(q, 1 + s) / R1), s, 0, NS + 1).removeO()
    us = sp.series(u.subs(q, 1 + s), s, 0, NS + 1).removeO()
    logR_c = [sp.simplify(logR.coeff(s, i)) for i in range(NS + 1)]
    u_c = [sp.simplify(us.coeff(s, i)) for i in range(NS + 1)]

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
        c[k] = sp.N(ck, 30)
        cku = [sp.expand(ck * t) for t in upow[k]]
        cur = [sp.Integer(1)] + [sp.Integer(0)] * NS
        n = 1
        while n * o <= NS:
            cur = sm(cur, cku)
            for i in range(NS + 1):
                model[i] = sp.expand(model[i] + sp.Integer((-1) ** (n + 1)) * cur[i] / n)
            n += 1
    print(f"  [{label}] done {time.monotonic()-t0:.0f}s", flush=True)
    return c


def dnet_coupled(tn, tp, g):
    return sp.simplify(
        A.augmentation(A.nucleon_nf_coupled(tn, g)) - A.augmentation(A.nucleon_nf_coupled(tp, g))
    )


def main():
    eps = sp.Rational(1, 10)
    for name, tn, tp in [
        ("lepton", ["u", "d", "d", "e"], ["u", "u", "d", "e"]),
        ("brane", ["u", "d", "d", "b"], ["u", "u", "d", "b"]),
    ]:
        dn = dnet_coupled(tn, tp, eps)
        c = ladder(dn, f"{name} g=1/10")
        print(f"\n=== {name} @ g=1/10 ===")
        for k in (2, 3, 4):
            slope = (float(c[k]) - float(C0[k])) / float(eps)
            print(f"  c{k}: g=0 {float(C0[k]):+.5f} -> g=0.1 {float(c[k]):+.5f}   "
                  f"dc{k}/dg|0 ~= {slope:+.4f}")
        s2 = (float(c[2]) - float(C0[2])) / float(eps)
        s3 = (float(c[3]) - float(C0[3])) / float(eps)
        pure = abs(s2) < 0.3 and abs(s3) < 3.0
        print(f"  -> {'PURE-c4 candidate (c2,c3 flat at linear order)' if pure else 'CONTAMINATES c2/c3 at linear order (route fails even perturbatively)'}",
              flush=True)


if __name__ == "__main__":
    main()
