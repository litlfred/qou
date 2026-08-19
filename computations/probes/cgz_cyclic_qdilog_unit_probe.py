"""CGZ cyclic quantum dilogarithm R_zeta — the eps_m unit machinery, verified vs Theorem 7.4.

Bean qou-9p9y (eps_m layer of the GSWZ membership harness). Scope-(a);
no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 11).

CONTEXT. The GSWZ epsilon_m units (arXiv:2412.04241 eqn (16)) are the
Chern-class map c_{zeta_m} of Calegari-Garoufalidis-Zagier
(arXiv:1712.04887, library/arxiv-1712.04887v3/1712.04887v3.pdf, their [10]). CGZ Theorem
1.6 identifies c_zeta with the COMPUTABLE map R_zeta built from the
cyclic quantum dilogarithm

    D_zeta(x) = prod_{k=1}^{n-1} (1 - zeta^k x)^k         (CGZ eqn (8))
    P_zeta(X) = D_zeta(x)/D_zeta(1),  x^n = X             (CGZ eqn (20))

via R_zeta = c_zeta^gamma with gamma = 2 (their Theorem 7.4 +
conjecture). This probe implements D_zeta / P_zeta / R_zeta in CGZ's
own finite-field realization (their §4.4: for q = -1 mod p, every
element of F_q is an n-th power, H = F_{q^2}, and R_zeta = P_zeta
literally) and verifies it against their printed torsion computation:

**Theorem 7.4 (printed target): R_zeta(eta_zeta) = zeta^2**, where
eta_zeta is the n-torsion element of B(Q(zeta)^+) of eqn (34),

    eta_zeta = sum_{k mod n} ([0] + [((zeta^k - zeta^-k)/(zeta - zeta^-1))^2]),

reduced mod a split prime (CGZ eqn (33) — their Lemma 5.1 route:
q = -1 mod n splits completely in Q(zeta)^+, and reduction of
eta_zeta generates B(F_q) tensor Z_p).

WHAT THIS CHECKS (exact arithmetic in F_{q^2}):

1. Lemma 2.4(a) identity (21): (1-X)^m D_zeta(zeta^m x) / D_zeta(x)
   = prod_{k<m} (1 - zeta^k x)^n — the well-definedness engine of
   P_zeta — verified exactly for a sweep of (m, x).
2. Theorem 7.4 over multiple (n, q): the n-th-power class of
   R_zeta(eta_zeta) equals the class of zeta^2, for n = 5
   (q = 19, 29, 79) and n = 7 (q = 13, 41, 83) — q = -1 mod n,
   q != -1 mod n*p (Lemma 5.1's saturation condition), and
   n^2 not dividing q^2-1 so the class of zeta is primitive.
3. Exponent specificity: R_zeta(eta_zeta) is NOT in the class of
   zeta^j for any j != 2 mod n — the gamma = 2 value is pinned,
   not vacuous (a wrong Bernoulli-type normalization or a
   conjugated zeta would land on j = -2).
4. zeta-primitivity guard: the class map chi(v) = v^{(q^2-1)/n} sends
   zeta to a PRIMITIVE n-th root (the class group is genuinely Z/n
   and the test has full resolution).

DOWNSTREAM (recorded): with D_zeta validated, the 5-adic
eps_m([zeta_24^k]) for the GSWZ 5_2 harness is the same P_zeta
construction run in (Z/5^W)[alpha]-coefficient rings at fibre order
m — queued as the next increment on qou-9p9y.
"""

import json
import sys

checks = {}
detail = {}


def fq2_ctx(q):
    """F_{q^2} = F_q[s]/(s^2 - D), D a non-residue. Elements (a, b)."""
    D = None
    for d in range(2, q):
        if pow(d, (q - 1) // 2, q) == q - 1:
            D = d
            break
    assert D is not None

    def mul(u, v):
        a, b = u
        c, e = v
        return ((a * c + b * e * D) % q, (a * e + b * c) % q)

    def pw(u, n):
        r = (1, 0)
        b = u
        while n:
            if n & 1:
                r = mul(r, b)
            b = mul(b, b)
            n >>= 1
        return r

    def inv(u):
        # u^(q^2-2)
        return pw(u, q * q - 2)

    return D, mul, pw, inv


def find_omega(q, n, mul, pw):
    """Element of exact order n in F_{q^2}^x (n | q+1)."""
    # try s + c for small c until (q^2-1)/n power has order n
    for a in range(1, q):
        for b in range(1, q):
            g = (a, b)
            w = pw(g, (q * q - 1) // n)
            if w != (1, 0):
                # order divides n (n prime here) => exact order n
                return w
    raise AssertionError("no order-n element")


def run_case(n, q):
    D, mul, pw, inv = fq2_ctx(q)
    assert (q + 1) % n == 0 and (q * q - 1) % (n * n) != 0
    w = find_omega(q, n, mul, pw)
    assert pw(w, n) == (1, 0) and w != (1, 0)

    def dzeta(x):
        """D_zeta(x) = prod_{k=1}^{n-1} (1 - w^k x)^k, x in F_{q^2}."""
        r = (1, 0)
        for k in range(1, n):
            t = mul(pw(w, k), x)
            r = mul(r, pw(((1 - t[0]) % q, (-t[1]) % q), k))
        return r

    # (1) identity (21): (1-X)^m D(w^m x)/D(x) = prod_{k<m}(1 - w^k x)^n
    ok21 = True
    for m in range(1, n):
        for xa in (2, 3, q - 2):
            x = (xa, 0)
            X = pw(x, n)
            lhs = mul(
                pw(((1 - X[0]) % q, (-X[1]) % q), m),
                mul(dzeta(mul(pw(w, m), x)), inv(dzeta(x))),
            )
            rhs = (1, 0)
            for k in range(m):
                t = mul(pw(w, k), x)
                rhs = mul(rhs, pw(((1 - t[0]) % q, (-t[1]) % q), n))
            if lhs != rhs:
                ok21 = False

    # class map chi: F_{q^2}^x -> mu_n
    def chi(v):
        return pw(v, (q * q - 1) // n)

    chi_w = chi(w)
    prim = chi_w != (1, 0)  # n prime => primitive if != 1

    # eta_zeta reduction: symbols [0] + [Y_k], Y_k = ((w^k-w^-k)/(w-w^-1))^2
    ninv = pow(n, -1, q - 1)  # unique n-th root exponent in F_q^x

    def nth_root_fq(Xa):
        """x in F_q with x^n = Xa (all of F_q^x are n-th powers)."""
        return pow(Xa, ninv, q)

    w_inv = pw(w, n - 1)
    d1 = mul(w, ((q - w_inv[0]) % q, (q - w_inv[1]) % q))
    d1 = (d1[0] % q, d1[1] % q)
    # d1 = w - w^{-1}; build Y_k in F_q
    base = ((w[0] - w_inv[0]) % q, (w[1] - w_inv[1]) % q)
    base_sq = mul(base, base)
    assert base_sq[1] == 0  # (w - w^{-1})^2 in F_q
    V = inv(dzeta((1, 0)))  # P_zeta(0) = D_zeta(1)^{-1}
    for k in range(1, n):
        wk, wmk = pw(w, k), pw(w, n - k)
        num = ((wk[0] - wmk[0]) % q, (wk[1] - wmk[1]) % q)
        num_sq = mul(num, num)
        assert num_sq[1] == 0
        Yk = (num_sq[0] * pow(base_sq[0], q - 2, q)) % q
        yk = nth_root_fq(Yk)
        V = mul(V, mul(dzeta((yk, 0)), inv(dzeta((1, 0)))))

    chi_V = chi(V)
    # find j with chi(V) = chi(w)^j
    jfound = None
    t = (1, 0)
    for j in range(n):
        if chi_V == t:
            jfound = j
            break
        t = mul(t, chi_w)
    return ok21, prim, jfound


cases = [(5, 19), (5, 29), (5, 79), (7, 13), (7, 41), (7, 83)]
all21 = True
allprim = True
alltwo = True
for n, q in cases:
    ok21, prim, j = run_case(n, q)
    detail[f"n{n}_q{q}"] = {"identity21": ok21, "zeta_primitive": prim, "gamma_exponent": j}
    all21 = all21 and ok21
    allprim = allprim and prim
    alltwo = alltwo and (j == 2)

checks["lemma24_identity_21_exact"] = all21
checks["zeta_class_primitive_all_cases"] = allprim
checks["theorem74_R_eta_eq_zeta_squared"] = alltwo
checks["gamma_exponent_specific"] = alltwo and all(
    d["gamma_exponent"] not in (None,) and d["gamma_exponent"] == 2
    for d in detail.values()
)

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

witness = {
    "schema": "probe-witness/v1",
    "probe": "cgz_cyclic_qdilog_unit_probe",
    "beans": ["qou-9p9y"],
    "source": "CGZ arXiv:1712.04887v3 eqns (8)/(20)/(21)/(33)/(34), §4.4, Theorem 7.4; library/arxiv-1712.04887v3/1712.04887v3.pdf",
    "checks": checks,
    "cases": detail,
    "scope": (
        "scope-(a): cyclic-quantum-dilog unit machinery (the eps_m "
        "realization, R = c^2) implemented and verified vs CGZ printed "
        "Theorem 7.4 over 6 finite-field cases; 5-adic eps_m on the GSWZ "
        "5_2 symbols is the next increment"
    ),
}
with open("computations/probes/cgz_cyclic_qdilog_unit.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
