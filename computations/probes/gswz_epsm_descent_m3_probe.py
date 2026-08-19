"""eps_3(xi) by the equivariant CGZ descent — m = 3, with the ambiguity subgroup measured.

Bean qou-y3xv (increment 3; m = 2 executed in this PR #4968 with the
canonical-cocycle construction). Scope-(a); no fit; nothing wired;
audit: docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 18).

WHAT m = 3 ADDS OVER m = 2 (all measured, not assumed):

1. FIELD: mu_{624*3} = mu_1872 needs d = ord_5(1872) = 12
   (1872 = 2^4 * 3^2 * 13; ord mod 16 = 4, mod 9 = 6, mod 13 = 4).
   B = Q_25, Gamma = <sigma> = <phi_5^2> of order 6.
2. SHIFT EXPONENTS r_i are intrinsic to z_i: sigma permutes the three
   cube roots of the sigma-fixed z_i by x -> zeta_3^{r_i} x with the
   SAME r_i for every root choice (sigma fixes zeta_3 in mu_24). So
   r_i = 0 iff z_i has a sigma-fixed (= base) cube root.
3. CANONICAL-ROOT INTEGRALITY is a 3-divisibility question: by the
   Lean-proved shift law (21), sigma(P)/P = prod_i [(1-z_i)^{-r_i} *
   prod_{k<r_i}(1-zeta_3^k x_i)^3]^{n_i} with n = (2,1); its CANONICAL
   cube root needs n_i * r_i = 0 mod 3 PER FACTOR — with n in {1,2}
   that forces r_i = 0. So either both r_i = 0 (direct descent:
   sigma(P) = P, a = P) or the canonical construction is obstructed at
   this layer (disclosed; the abstract nu is still computed via a
   Tonelli cube root when one exists).
4. THE AMBIGUITY SUBGROUP: even in the direct case the value
   chi_B(P) is x_i-choice covariant: x_i -> zeta_3 x_i multiplies P by
   [D(zeta_3 x_i)/D(x_i)]^{n_i} = [(1-z_i)^{-1}(1-x_i)^3]^{n_i}, so
   eps_3 moves by chi_B(1-z_i)^{-n_i} (the (1-x_i)^{3 n_i} part is a
   base cube when r_i = 0 — killed). The covariance is CHECKED
   exactly, and the subgroup A = <chi_B(1-z_1), chi_B(1-z_2)> <= mu_3
   is measured:
   - A = 1: eps_3(xi) in mu_3 is fully well-defined.
   - A = mu_3: only the class in mu_3/A = 1 survives — the honest
     statement is then that eps_3 requires an external pinning of the
     x_i (the deterministic teich-dlog convention gives a
     CONVENTIONAL value, reported as such, never as an invariant).
5. CHARACTER: chi_B = teich(.)^8 = teich(.)^{(25-1)/3}, values in the
   base mu_3 = <g24^8>; base-level non-vacuity control
   chi_B(g24) = omega != 1.

NO printed target exists (honest scope): every reported quantity is
falsifiable against any independent computation of the CGZ map on the
5_2 Bloch class. m | 24 beyond 3 queued on qou-y3xv.
"""

import json
import pathlib
import sys

P5 = 5
W = 8
MOD = P5**W
m = 3
N = 624 * m  # 1872
d = 12       # ord_5(1872)
n_gal = 6    # [F : Q_25] = d / 2

checks = {}
detail = {}


# ---------- F_5 helpers + field construction (as m=2 probe) ----------
def p5_mulmod(a, b, h):
    dd = len(h) - 1
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % 5
    for i in range(len(out) - 1, dd - 1, -1):
        c = out[i]
        if c:
            for j in range(dd + 1):
                out[i - dd + j] = (out[i - dd + j] - c * h[j]) % 5
    return out[:dd]


def p5_powmod_x(e, h):
    dd = len(h) - 1
    result = [1] + [0] * (dd - 1)
    base = [0, 1] + [0] * (dd - 2)
    while e:
        if e & 1:
            result = p5_mulmod(result, base, h)
        base = p5_mulmod(base, base, h)
        e >>= 1
    return result


def p5_gcd(a, b):
    def norm(p):
        p = p[:]
        while p and p[-1] == 0:
            p.pop()
        return p
    a, b = norm(a), norm(b)
    while b:
        inv = pow(b[-1], -1, 5)
        r = norm(a)
        while len(r) >= len(b):
            c = (r[-1] * inv) % 5
            off = len(r) - len(b)
            for j in range(len(b)):
                r[off + j] = (r[off + j] - c * b[j]) % 5
            r = norm(r)
            if not r:
                break
        a, b = b, r
    return a


def irreducible_deg_d(dd):
    import random
    rng = random.Random(20260811)
    primes = [p for p in range(2, dd + 1) if dd % p == 0 and all(p % q for q in range(2, p))]
    for _ in range(20000):
        h = [rng.randrange(5) for _ in range(dd)] + [1]
        if h[0] == 0:
            continue
        if p5_powmod_x(5**dd, h) != [0, 1] + [0] * (dd - 2):
            continue
        ok = True
        for p in primes:
            xq = p5_powmod_x(5 ** (dd // p), h)
            diff = xq[:]
            diff[1] = (diff[1] - 1) % 5
            if len(p5_gcd(diff, h)) > 1:
                ok = False
                break
        if ok:
            return h
    raise AssertionError("no irreducible poly")


class Ring:
    def __init__(self, h):
        self.h = h
        self.d = len(h) - 1

    def mul(self, a, b):
        dd = self.d
        out = [0] * (2 * dd - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    out[i + j] = (out[i + j] + ai * bj) % MOD
        for i in range(len(out) - 1, dd - 1, -1):
            c = out[i]
            if c:
                for j in range(dd + 1):
                    out[i - dd + j] = (out[i - dd + j] - c * self.h[j]) % MOD
        return out[:dd]

    def one(self):
        return [1] + [0] * (self.d - 1)

    def scal(self, v):
        return [v % MOD] + [0] * (self.d - 1)

    def pw(self, a, e):
        r = self.one()
        b = a[:]
        while e:
            if e & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            e >>= 1
        return r

    def sub(self, a, b):
        return [(x - y) % MOD for x, y in zip(a, b)]

    def add(self, a, b):
        return [(x + y) % MOD for x, y in zip(a, b)]

    def one_minus(self, t):
        out = [(-c) % MOD for c in t]
        out[0] = (out[0] + 1) % MOD
        return out

    def _p5_pow(self, a, e):
        h5 = [c % 5 for c in self.h]
        r = [1] + [0] * (self.d - 1)
        b = [c % 5 for c in a]
        while e:
            if e & 1:
                r = p5_mulmod(r, b, h5)
            b = p5_mulmod(b, b, h5)
            e >>= 1
        return r

    def inv(self, u):
        seed5 = self._p5_pow(u, 5 ** self.d - 2)
        iv = [c % MOD for c in seed5]
        for _ in range(5):
            t = self.mul(u, iv)
            corr = [(-c) % MOD for c in t]
            corr[0] = (corr[0] + 2) % MOD
            iv = self.mul(iv, corr)
        return iv

    def eval_poly(self, coeffs, at):
        r = [0] * self.d
        for c in reversed(coeffs):
            r = self.mul(r, at)
            r[0] = (r[0] + c) % MOD
        return r


h5 = irreducible_deg_d(d)
R = Ring([c % MOD for c in h5])
X = [0, 1] + [0] * (d - 2)


def hensel_root(seed):
    y = seed[:]
    for _ in range(6):
        hy = R.eval_poly([c % MOD for c in R.h], y)
        dh = [0] * (len(R.h) - 1)
        for i in range(1, len(R.h)):
            dh[i - 1] = (i * R.h[i]) % MOD
        dhy = R.eval_poly(dh, y)
        y = R.sub(y, R.mul(hy, R.inv(dhy)))
    return y


PHI_X = hensel_root(R.pw(X, 5))


def phi(u):
    return R.eval_poly(u, PHI_X)


def sigma(u):
    return phi(phi(u))


hcheck = R.eval_poly([c % MOD for c in R.h], PHI_X)
s6 = X[:]
for _ in range(n_gal):
    s6 = sigma(s6)
checks["frobenius_wellformed_and_sigma_order6"] = (
    all(c == 0 for c in hcheck) and s6 == X
)

# ---------- Teichmuller, zeta_N, alpha, symbols ----------------------
def teich(u):
    v = u
    for _ in range(14):
        v2 = R.pw(v, 5**d)
        if v2 == v:
            return v
        v = v2
    return v


zeta_N = None
for seed_c in range(2, 80):
    g = [seed_c % MOD, 1] + [0] * (d - 2)
    u = teich(R.pw(g, (5**d - 1) // N))
    if R.pw(u, N) == R.one() and all(
        R.pw(u, N // p) != R.one() for p in (2, 3, 13)
    ):
        zeta_N = u
        break
checks["zeta_N_found"] = zeta_N is not None
z624 = R.pw(zeta_N, N // 624)
zeta_3 = R.pw(zeta_N, N // 3)
minus1 = R.scal(-1)

alpha_F = None
cand = R.one()
for e in range(624):
    if e:
        cand = R.mul(cand, z624)
    c5 = [c % 5 for c in cand]
    h5m = [c % 5 for c in R.h]
    v3 = p5_mulmod(p5_mulmod(c5, c5, h5m), c5, h5m)
    w2 = p5_mulmod(c5, c5, h5m)
    val = [(v3[i] - w2[i]) % 5 for i in range(d)]
    val[0] = (val[0] + 1) % 5
    if all(x == 0 for x in val) and any(c5[i] != 0 for i in range(1, d)):
        alpha_F = cand[:]
        break
checks["alpha_residue_found"] = alpha_F is not None
for _ in range(6):
    fa = R.sub(R.mul(R.mul(alpha_F, alpha_F), alpha_F), R.mul(alpha_F, alpha_F))
    fa[0] = (fa[0] + 1) % MOD
    dfa = R.sub(R.mul(R.scal(3), R.mul(alpha_F, alpha_F)), R.mul(R.scal(2), alpha_F))
    alpha_F = R.sub(alpha_F, R.mul(fa, R.inv(dfa)))
checks["alpha_sigma_fixed"] = sigma(alpha_F) == alpha_F

z1 = R.one_minus(R.mul(alpha_F, alpha_F))
z2 = R.add(R.sub(R.mul(z1, z1), z1), R.scal(2))
checks["z_sigma_fixed"] = sigma(z1) == z1 and sigma(z2) == z2
# The Bloch-symbol structure closes on the alpha-line EXACTLY:
# 1 - z1 = alpha^2 by construction, and 1 - z2 = -(z1^2 - z1 + 1)
# = alpha (since alpha^4 - alpha^2 + 1 = -alpha from the minimal
# polynomial). So the whole shift-law cocycle obstruction is a power
# of alpha: sigma(P)/P = (1 - x2)^3 / alpha for r = (0, 1).
checks["one_minus_z1_is_alpha_sq"] = R.one_minus(z1) == R.mul(alpha_F, alpha_F)
checks["one_minus_z2_is_alpha"] = R.one_minus(z2) == alpha_F


def dzeta(x):
    r = R.one()
    for k in range(1, m):
        r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_3, k), x)), k))
    return r


def mth_root_teich_dlog624(u):
    tu = teich(u)
    t = R.one()
    e_t = None
    for e in range(624):
        if t == tu:
            e_t = e
            break
        t = R.mul(t, z624)
    assert e_t is not None
    target = (e_t * (N // 624)) % N
    ep = next(ce for ce in range(N) if (ce * m) % N == target)
    troot = R.pw(zeta_N, ep)
    w = R.mul(u, R.inv(tu))
    y = R.one()
    for _ in range(6):
        ym = R.pw(y, m)
        y = R.add(y, R.mul(R.sub(w, ym), R.inv(R.mul(R.scal(m), R.pw(y, m - 1)))))
    return R.mul(troot, y)


x1 = mth_root_teich_dlog624(z1)
x2 = mth_root_teich_dlog624(z2)
checks["cube_roots_exact"] = R.pw(x1, 3) == z1 and R.pw(x2, 3) == z2
d1inv3 = R.pw(R.inv(dzeta(R.one())), 3)
P = R.mul(R.mul(R.pw(dzeta(x1), 2), dzeta(x2)), d1inv3)

# ---------- shift exponents (intrinsic to z_i) -----------------------
def shift_exp(x):
    s = R.mul(sigma(x), R.inv(x))
    for r in range(3):
        if s == R.pw(zeta_3, r):
            return r
    return None


r1s = shift_exp(x1)
r2s = shift_exp(x2)
checks["frobenius_root_shift_in_mu3"] = r1s is not None and r2s is not None
detail["shift_exponents"] = {"r1": r1s, "r2": r2s}

# canonical cube root of sigma(P)/P is integral iff n_i * r_i = 0 mod 3
# per factor, n = (2, 1); with n in {1,2} that means r_i = 0.
canonical_integral = r1s == 0 and r2s == 0
detail["canonical_root_integral"] = canonical_integral

# ---------- character + base controls --------------------------------
g24 = R.pw(z624, 26)
checks["g24_base_generator"] = (
    sigma(g24) == g24
    and R.pw(g24, 24) == R.one()
    and all(R.pw(g24, 24 // p) != R.one() for p in (2, 3))
)
omega = R.pw(g24, 8)  # base mu_3 generator
checks["omega_order_3"] = R.pw(omega, 3) == R.one() and omega != R.one()
checks["chi_B_nonvacuous_on_base"] = R.pw(g24, 8) != R.one()

MU3 = {tuple(R.one()): 0, tuple(omega): 1, tuple(R.pw(omega, 2)): 2}


def chi_B(u):
    """teich(.)^8 with the base-membership gate: returns the mu_3 dlog
    (0/1/2) or None if the value is not in the base mu_3."""
    return MU3.get(tuple(R.pw(teich(u), 8)))


# ---------- abstract nu via a Tonelli cube root ----------------------
M_ORD = 5**d - 1
V3 = 0
_t = M_ORD
while _t % 3 == 0:
    V3 += 1
    _t //= 3
checks["three_sylow_valuation_is_2"] = V3 == 2
Q3 = M_ORD // 3**V3

g3 = None
for seed_c in range(2, 100):
    g = teich([seed_c % MOD, 1] + [0] * (d - 2))
    t3 = R.pw(g, Q3)
    if R.pw(t3, 3 ** (V3 - 1)) != R.one():
        g3 = t3
        break
checks["three_sylow_generator_found"] = g3 is not None


def cube_root_unit(u):
    """Cube root of a unit in F (or None): CRT split of the Teichmuller
    part into order-Q3 and 3-Sylow components + Newton on 1+5R."""
    tu = teich(u)
    inv9 = pow(3**V3, -1, Q3)
    comp_Q = R.pw(tu, (3**V3 * inv9) % M_ORD)
    comp_3 = R.mul(tu, R.inv(comp_Q))
    k = None
    t = R.one()
    for e in range(3**V3):
        if t == comp_3:
            k = e
            break
        t = R.mul(t, g3)
    if k is None or k % 3 != 0:
        return None
    root_t = R.mul(R.pw(comp_Q, pow(3, -1, Q3)), R.pw(g3, k // 3))
    w = R.mul(u, R.inv(tu))
    y = R.one()
    for _ in range(6):
        y3 = R.pw(y, 3)
        y = R.add(y, R.mul(R.sub(w, y3), R.inv(R.mul(R.scal(3), R.pw(y, 2)))))
    return R.mul(root_t, y)


ratio = R.mul(sigma(P), R.inv(P))


def galois_norm(u):
    r = R.one()
    v = u
    for _ in range(n_gal):
        r = R.mul(r, v)
        v = sigma(v)
    return r


c_root = cube_root_unit(ratio)
checks["cube_root_of_sigmaP_over_P_exists"] = c_root is not None
if c_root is not None:
    checks["c_cubed_matches"] = R.pw(c_root, 3) == ratio
    nu = galois_norm(c_root)
    nu_dlog = MU3.get(tuple(nu))
    checks["nu_in_mu3"] = nu_dlog is not None
    # root ambiguity zeta_3^j c changes nu by zeta_3^{6j} = 1
    nu_b = galois_norm(R.mul(c_root, zeta_3))
    checks["nu_root_choice_invariant"] = nu == nu_b
    detail["nu_obstruction_dlog"] = nu_dlog

# ---------- direct descent (both r_i = 0) ----------------------------
if canonical_integral:
    # sigma(P) = P follows from r_i = 0 via the shift law — checked
    # directly, and it IS the descent certificate (a = P).
    checks["direct_descent_sigma_P_fixed"] = sigma(P) == P
    e3 = chi_B(P)
    checks["chi_B_P_in_base_mu3"] = e3 is not None
    detail["eps3_conventional_dlog"] = e3

    # ambiguity subgroup A = <chi_B(1-z_1), chi_B(1-z_2)> <= mu_3
    a1 = chi_B(R.one_minus(z1))
    a2 = chi_B(R.one_minus(z2))
    checks["ambiguity_generators_in_base_mu3"] = a1 is not None and a2 is not None
    detail["ambiguity_generators_dlog"] = {"chiB_1mz1": a1, "chiB_1mz2": a2}
    amb_trivial = a1 == 0 and a2 == 0
    detail["ambiguity_subgroup"] = "trivial" if amb_trivial else "mu_3 (full)"

    # covariance check: x1 -> zeta_3 x1 multiplies P by
    # [(1-z1)^{-1} (1-x1)^3]^2; with r1 = 0, (1-x1) is base so the
    # cube part is chi_B-trivial: predicted shift = -2*a1 mod 3.
    x1b = R.mul(zeta_3, x1)
    Pb = R.mul(R.mul(R.pw(dzeta(x1b), 2), dzeta(x2)), d1inv3)
    checks["covariant_P_sigma_fixed"] = sigma(Pb) == Pb
    e3b = chi_B(Pb)
    checks["x1_twist_covariance_exact"] = (
        e3 is not None
        and e3b is not None
        and a1 is not None
        and (e3b - e3) % 3 == (-2 * a1) % 3
    )
    detail["eps3_after_x1_twist_dlog"] = e3b

    if amb_trivial:
        detail["eps3_xi_class"] = f"omega^{e3} (WELL-DEFINED: ambiguity subgroup trivial)"
    else:
        detail["eps3_xi_class"] = (
            f"omega^{e3} CONVENTIONAL under the teich-dlog root pinning; "
            "the x_i-choice ambiguity subgroup is all of mu_3, so no "
            "pinning-free invariant survives at m = 3 (honest scope: "
            "the invariant content is nu + the covariance law, both "
            "checked; a canonical pinning would need extra structure, "
            "e.g. CGZ's square-argument eta-elements)"
        )
else:
    # canonical layer obstructed: with n = (2,1), some n_i * r_i != 0
    # mod 3 — the shift-law cube root is fractional per factor. No
    # padding checks; the honest carries are r_i and nu above.
    detail["eps3_xi_class"] = (
        f"CANONICAL-LAYER OBSTRUCTED: r = ({r1s}, {r2s}) with n = (2,1) "
        "gives per-factor exponents not divisible by 3; a canonical "
        "cube root of sigma(P)/P needs canonical cube roots of the "
        "base elements (1-z_i) — queued (CGZ square-argument route)"
    )

print(json.dumps(checks, indent=1))
print(json.dumps(detail, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_descent_m3_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_descent_m3_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 §2-3 descent (uploads/1712.04887v3.pdf); "
        "GSWZ arXiv:2412.04241v2 eqn (270); Lean backbone "
        "QOU.Machinery.CyclicQuantumDilog (merged #4964)"
    ),
    "field": "F = Q_5(mu_1872), d = 12; base B = Q_25; Gamma = <phi_5^2>, n = 6",
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a): m = 3 equivariant descent with the shift exponents, "
        "canonical-root integrality, ambiguity subgroup, and x_1-twist "
        "covariance all MEASURED; the value is reported as well-defined "
        "only if the ambiguity subgroup is trivial, else as conventional "
        "under the stated pinning; no printed target exists"
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_epsm_descent_m3.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
