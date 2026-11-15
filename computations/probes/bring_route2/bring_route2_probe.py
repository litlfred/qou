#!/usr/bin/env python3
"""Route 2 (beans qou-99qc, qou-pzsi): braid word -> closed geodesic on Bring's surface.

Implements preregistration.md section 1 exactly. Prints lengths only: no energy, no
selection, and no Q_beta / CODATA / mass input anywhere.

Arithmetic:
  * B_3 -> SL(2,Z), the reduction mod 2, and the Gamma_0(2) conjugation are exact (int).
  * The H_4 element and its Rosen reduction are exact over Z[sqrt 2]: an element
    p + q*sqrt2 is stored as the integer pair (p, q). The comparisons needed to choose
    the nearest multiple are made with mpmath at 80 dps, which only *selects* n; the
    reduction is then verified exactly.
  * The S_5 order r is exact (permutations), and is cross-checked against the
    choice-free congruence test g^r in H_4(5) (Kattan-Singerman (3.1)), done exactly.
  * The Delta(2,4,5) traces and the Bring lengths use mpmath at 80 dps (no float64).
"""
import itertools
import json
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 80

# ---------------------------------------------------------------- candidates
NUC9 = [0, 1, 0, 1, 0, 1, 0, 0, 1]
CANDIDATES = {
    "nuc9": NUC9,
    "nuc11_interleaved": NUC9 + [0, 0],
    "gluon_s0_s1": NUC9 + [0, 1],
    "gluon_s1_s0": NUC9 + [1, 0],
    "gluon_s1_s1": NUC9 + [1, 1],
    "gluon_s0_s0": NUC9 + [0, 0],
    "nuc11_gen_grouped": [0] * 7 + [1] * 4,
}
CONJUGATE_PAIRS = [("gluon_s0_s1", "gluon_s0_s0"), ("gluon_s1_s0", "gluon_s1_s1")]


# ---------------------------------------------------------------- integer SL(2,Z)
def imul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


T = [[1, 1], [0, 1]]
L = [[1, 0], [-1, 1]]
GEN = {0: T, 1: L}


def sl2z(word):
    M = [[1, 0], [0, 1]]
    for g in word:
        M = imul(M, GEN[g])
    return M


def inv(M):
    return [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]


def act_p1f2(M, pt):
    """Action mod 2 on P^1(F_2) = {'inf', 0, 1}, z -> (az+b)/(cz+d)."""
    a, b, c, d = (x % 2 for x in (M[0][0], M[0][1], M[1][0], M[1][1]))
    if pt == "inf":
        return "inf" if c == 0 else (a * c) % 2  # a/c with c=1
    num, den = (a * pt + b) % 2, (c * pt + d) % 2
    return "inf" if den == 0 else num % 2


H_TO_INF = {"inf": [[1, 0], [0, 1]], 0: [[0, -1], [1, 0]], 1: [[0, -1], [1, -1]]}


# ---------------------------------------------------------------- Z[sqrt2] exact
class Z2:
    __slots__ = ("p", "q")

    def __init__(self, p, q=0):
        self.p, self.q = p, q

    def __add__(s, o):
        return Z2(s.p + o.p, s.q + o.q)

    def __sub__(s, o):
        return Z2(s.p - o.p, s.q - o.q)

    def __mul__(s, o):
        return Z2(s.p * o.p + 2 * s.q * o.q, s.p * o.q + s.q * o.p)

    def __neg__(s):
        return Z2(-s.p, -s.q)

    def __eq__(s, o):
        return s.p == o.p and s.q == o.q

    def val(s):
        return mp.mpf(s.p) + mp.mpf(s.q) * mp.sqrt(2)

    def __repr__(s):
        return f"({s.p}{'+' if s.q >= 0 else '-'}{abs(s.q)}√2)"


def zmul(A, B):
    return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
            [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]


S_H = [[Z2(0), Z2(-1)], [Z2(1), Z2(0)]]
I_H = [[Z2(1), Z2(0)], [Z2(0), Z2(1)]]


def U_pow(n):
    return [[Z2(1), Z2(0, n)], [Z2(0), Z2(1)]]


def is_pm_identity(M):
    for s in (1, -1):
        if M[0][0] == Z2(s) and M[1][1] == Z2(s) and M[0][1] == Z2(0) and M[1][0] == Z2(0):
            return True
    return False


def to_h4(g):
    """D^-1 g D for g in Gamma_0(2): [[a,b],[c,d]] -> [[a, b*sqrt2],[(c/2)*sqrt2, d]]."""
    a, b, c, d = g[0][0], g[0][1], g[1][0], g[1][1]
    assert c % 2 == 0
    return [[Z2(a), Z2(0, b)], [Z2(0, c // 2), Z2(d)]]


def rosen_word(M):
    """Write M (in H_4) as a word in S, U^n. Returns list of ('S',) / ('U', n), with
    M == product of the word, verified exactly. Reduction: M <- S U^{-n} M with
    n = round((a/c)/sqrt2), which shrinks |c| by a factor <= sqrt2/2."""
    word_rev = []
    cur = [row[:] for row in M]
    for _ in range(10000):
        a, c = cur[0][0], cur[1][0]
        if c == Z2(0):
            # cur = +-[[1, n sqrt2],[0, 1]]
            sgn = 1 if cur[0][0] == Z2(1) else -1
            b = cur[0][1]
            n = sgn * b.q
            assert b.p == 0 and cur[1][1] == Z2(sgn)
            word_rev.append(("U", n))
            break
        n = int(mp.nint((a.val() / c.val()) / mp.sqrt(2)))
        # cur = U^n S^-1 * (S U^-n cur); S^-1 = -S = S projectively
        word_rev.append(("U", n))
        word_rev.append(("S",))
        cur = zmul(S_H, zmul(U_pow(-n), cur))
    else:
        raise RuntimeError("Rosen reduction did not terminate")
    # M = U^{n1} S U^{n2} S ... ; word_rev already in left-to-right order
    word = [w for w in word_rev if not (w[0] == "U" and w[1] == 0)]
    # exact round trip
    P = I_H
    for w in word:
        P = zmul(P, S_H if w[0] == "S" else U_pow(w[1]))
    assert is_pm_identity(zmul(P, zinv(M))), "Rosen round trip failed"
    return word


def zinv(M):
    return [[M[1][1], -M[0][1]], [-M[1][0], M[0][0]]]


# ---------------------------------------------------------------- H_4(5) membership (exact)
def in_h4_5(M):
    """Kattan-Singerman (3.1): even element [[a, b sqrt2],[c sqrt2, d]] with
    a == d == +-1 mod 5 and b == c == 0 mod 5 (a, b, c, d in Z for an even element)."""
    a, bq, cq, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if a.q or d.q or bq.p or cq.p:
        return False  # odd element (or not of even shape)
    for s in (1, -1):
        if (a.p - s) % 5 == 0 and (d.p - s) % 5 == 0 and bq.q % 5 == 0 and cq.q % 5 == 0:
            return True
    return False


def h4_5_order(M, cap=200):
    P = I_H
    for r in range(1, cap + 1):
        P = zmul(P, M)
        if in_h4_5(P):
            return r
    return None


# ---------------------------------------------------------------- S_5 image (exact)
def pcomp(a, b):  # apply b then a? use right action: (a*b)(x) = b(a(x))
    return tuple(b[a[i]] for i in range(5))


def porder(p):
    e, q, k = tuple(range(5)), p, 1
    while q != e:
        q, k = pcomp(q, p), k + 1
    return k


def generated_size(gens):
    e = tuple(range(5))
    seen, frontier = {e}, [e]
    while frontier:
        nxt = []
        for x in frontier:
            for g in gens:
                y = pcomp(x, g)
                if y not in seen:
                    seen.add(y)
                    nxt.append(y)
        frontier = nxt
    return len(seen)


def s5_epimorphisms():
    rho = (1, 2, 3, 4, 0)  # 5-cycle, image of U
    out = []
    for perm in itertools.permutations(range(5)):
        if porder(perm) != 2:
            continue
        if porder(pcomp(perm, rho)) == 4 and generated_size([perm, rho]) == 120:
            out.append(perm)
    return rho, out


def word_image_order(word, s, u):
    p = tuple(range(5))
    for w in word:
        if w[0] == "S":
            p = pcomp(p, s)
        else:
            n = w[1] % 5
            for _ in range(n):
                p = pcomp(p, u)
    return porder(p)


# ---------------------------------------------------------------- Delta(2,4,5) in PSL(2,R)
def delta245():
    phi = 2 * mp.cos(mp.pi / 5)
    x = phi / 2
    z = (-mp.sqrt(2) + mp.sqrt(phi ** 2 - 2)) / 2
    y = z + mp.sqrt(2)
    s = mp.matrix([[0, -1], [1, 0]])
    u = mp.matrix([[x, y], [z, x]])
    return s, u


def word_trace_delta(word, s, u):
    P = mp.eye(2)
    for w in word:
        P = P * (s if w[0] == "S" else u ** (w[1] % 10))  # u^10 = I in SL
    return P[0, 0] + P[1, 1]


# ---------------------------------------------------------------- main
def main():
    s, u = delta245()
    checks = {}
    checks["det_u_is_1"] = bool(abs(mp.det(u) - 1) < mp.mpf(10) ** -70)
    checks["tr_u_is_2cos_pi5"] = bool(abs(u[0, 0] + u[1, 1] - 2 * mp.cos(mp.pi / 5)) < mp.mpf(10) ** -70)
    su = s * u
    checks["tr_su_is_2cos_pi4"] = bool(abs(abs(su[0, 0] + su[1, 1]) - mp.sqrt(2)) < mp.mpf(10) ** -70)

    rho, sigmas = s5_epimorphisms()
    checks["s5_epimorphism_exists"] = len(sigmas) > 0

    rows = {}
    for name, w in CANDIDATES.items():
        g = sl2z(w)
        tr = g[0][0] + g[1][1]
        fixed = [p for p in ("inf", 0, 1) if act_p1f2(g, p) == p]
        row = {"word": w, "sl2z": g, "trace_sl2z": tr, "p1f2_fixed": [str(p) for p in fixed]}
        if len(fixed) != 1:
            row["status"] = "out of scope (permutation does not fix exactly one point)"
            rows[name] = row
            continue
        h = H_TO_INF[fixed[0]]
        gp = imul(imul(h, g), inv(h))
        assert gp[1][0] % 2 == 0
        M = to_h4(gp)
        word = rosen_word(M)
        row["gamma0_2_rep"] = gp
        row["h4_word"] = [list(x) for x in word]
        r_cong = h4_5_order(M)
        r_s5 = sorted({word_image_order(word, sg, rho) for sg in sigmas})
        row["r_congruence_H4(5)"] = r_cong
        row["r_s5_over_all_epimorphisms"] = r_s5
        trd = word_trace_delta(word, s, u)
        row["trace_delta245"] = mp.nstr(trd, 40)
        row["trace_abs_delta245"] = mp.nstr(abs(trd), 30)
        if abs(trd) > 2 + mp.mpf(10) ** -60:
            r = r_cong
            ell = 2 * mp.acosh(abs(trd) / 2)
            row["type_delta245"] = "hyperbolic"
            row["orbifold_length"] = mp.nstr(ell, 40)
            row["bring_length"] = mp.nstr(r * ell, 40) if r else None
        else:
            row["type_delta245"] = "elliptic or parabolic (no closed geodesic)"
        rows[name] = row

    for a, b in CONJUGATE_PAIRS:
        # PSL(2,R): the trace is defined only up to sign, so compare |tr|.
        ta, tb = rows[a].get("trace_abs_delta245"), rows[b].get("trace_abs_delta245")
        checks[f"conjugate_pair_{a}~{b}"] = (
            ta is not None and ta == tb
            and rows[a].get("r_congruence_H4(5)") == rows[b].get("r_congruence_H4(5)"))
    checks["r_s5_matches_congruence"] = all(
        (r.get("r_congruence_H4(5)") is None) or r.get("r_s5_over_all_epimorphisms") == [r["r_congruence_H4(5)"]]
        for r in rows.values() if "h4_word" in r)

    for name, r in rows.items():
        print(f"{name:20s} trZ={r['trace_sl2z']:>4}  fixed={r['p1f2_fixed']}  "
              f"r={r.get('r_congruence_H4(5)')} r_S5={r.get('r_s5_over_all_epimorphisms')}  "
              f"|trΔ|={r.get('trace_abs_delta245', '-')}  "
              f"{r.get('type_delta245', r.get('status'))}  L_Bring={r.get('bring_length', '-')}")
    print("S5 epimorphisms (sigma choices):", len(sigmas))
    for k, v in checks.items():
        print(("PASS " if v else "FAIL ") + k)
    out = {"description": "Route 2 (qou-99qc): braid word -> Bring geodesic, lengths only. See preregistration.md.",
           "mp_dps": mp.mp.dps, "mpmath": mp.__version__, "rows": rows, "checks": checks}
    Path(__file__).with_name("results.json").write_text(json.dumps(out, indent=1, default=str))
    sys.exit(0 if all(checks.values()) else 1)


if __name__ == "__main__":
    main()
