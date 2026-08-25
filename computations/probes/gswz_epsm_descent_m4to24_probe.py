"""eps_m descent sweep for the remaining m | 24 — shift exponents, canonical-root integrality, nu, and the canonical value wherever the data permits.

Bean qou-y3xv (increments 4..24; m = 2 canonical +1 and m = 3 nu-only
landed in PR #4968). Scope-(a); no fit; nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 21).

WHAT THIS SWEEPS (m in {4, 6, 8, 12, 24}, all measured, none assumed):

1. FIELD per m: F = Q_5(mu_{624m}), d = ord_5(624m), base B = Q_25,
   Gamma = <phi_5^2> of order n = d/2 (m | n for every m here, so
   nu = N_{F/B}(c) is automatically root-choice invariant:
   N(zeta_m) = zeta_m^n = 1).
2. SHIFT EXPONENTS r_i in Z/m from sigma(x_i) = zeta_m^{r_i} x_i
   (intrinsic to z_i since sigma fixes zeta_m in mu_24).
3. CANONICAL-ROOT INTEGRALITY: by the Lean-proved shift law (21),
   sigma(P)/P = prod_i [(1-z_i)^{-r_i} prod_{k<r_i}(1-zeta^k x_i)^m]^{n_i}
   with n = (2,1); its canonical m-th root is integral iff
   m | 2 r_1 and m | r_2. Where integral:
       c_canon = prod_i (1-z_i)^{-n_i r_i/m} prod_{k<r_i}(1-zeta^k x_i)^{n_i},
   verified c_canon^m = sigma(P)/P exactly, then the Hilbert-90
   resolvent, the sigma-fixed certificate a = P b^{-m}, and
   eps_m(xi) = chi_B(a), chi_B = teich(.)^{24/m} into the base mu_m.
4. NU where the canonical layer is fractional: an abstract m-th root
   via COMPOSED Sylow roots (m = 2^s 3^t: t cube roots then s square
   roots; Tonelli-Shanks in the 2-Sylow, CRT-split in the 3-Sylow,
   both with runtime-computed valuations), nu = N_{F/B}(c) in mu_m.
   The abstract-layer class is NOT extracted (PR #4968 established it
   sweeps mu_m with the root choice — the abstract layer pins nu only).
5. ALPHA-LINE exact identities re-verified per field: 1-z1 = alpha^2,
   1-z2 = alpha, z1 = -alpha^3 (the Nahm saddle relation in units).

HONESTY: every check can fail (wrong Frobenius, wrong field, wrong
shift law, non-unit resolvent, failed certificate all break specific
checks); obstructed/fractional branches add NO padding checks — the
per-m check count varies by outcome by design. No printed targets
exist; all values are falsifiable candidate data. Long-compute: run
with `python3 -u ... 2>&1 | tee /tmp/gswz_epsm_m4to24.log` (d = 96 at
m = 24 dominates; per-m progress lines are emitted).
"""

import json
import pathlib
import sys
import time

P5 = 5
W = 8
MOD = P5**W

M_LIST = [4, 6, 8, 12, 24]

checks = {}
detail = {}


def ord5_mod(n):
    r, v = 1, 5 % n
    while v != 1:
        v = (v * 5) % n
        r += 1
        assert r <= 200
    return r


# ---------- generic F_5 + ring helpers (as the m2/m3 probes) ----------
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


def irreducible_deg_d(dd, seed):
    import random
    rng = random.Random(seed)
    primes = [p for p in range(2, dd + 1) if dd % p == 0 and all(p % q for q in range(2, p))]
    for _ in range(60000):
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


def run_m(m):
    t0 = time.time()
    res = {}
    N = 624 * m
    d = ord5_mod(N)
    n_gal = d // 2
    res["field"] = f"d={d}, n_gal={n_gal}, N={N}"
    ck = {}

    h5 = irreducible_deg_d(d, seed=20260811 + m)
    R = Ring([c % MOD for c in h5])
    X = [0, 1] + [0] * (d - 2)

    def hensel_root(seedv):
        y = seedv[:]
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
    sN = X[:]
    for _ in range(n_gal):
        sN = sigma(sN)
    ck["frobenius_wellformed_and_sigma_order"] = (
        all(c == 0 for c in hcheck) and sN == X
    )

    def teich(u):
        v = u
        for _ in range(20):
            v2 = R.pw(v, 5**d)
            if v2 == v:
                return v
            v = v2
        return v

    zeta_N = None
    for seed_c in range(2, 120):
        g = [seed_c % MOD, 1] + [0] * (d - 2)
        u = teich(R.pw(g, (5**d - 1) // N))
        if R.pw(u, N) == R.one() and all(
            R.pw(u, N // p) != R.one() for p in (2, 3, 13)
        ):
            zeta_N = u
            break
    ck["zeta_N_found"] = zeta_N is not None
    z624 = R.pw(zeta_N, N // 624)
    zeta_m = R.pw(zeta_N, N // m)
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
    for _ in range(6):
        fa = R.sub(R.mul(R.mul(alpha_F, alpha_F), alpha_F), R.mul(alpha_F, alpha_F))
        fa[0] = (fa[0] + 1) % MOD
        dfa = R.sub(R.mul(R.scal(3), R.mul(alpha_F, alpha_F)), R.mul(R.scal(2), alpha_F))
        alpha_F = R.sub(alpha_F, R.mul(fa, R.inv(dfa)))
    ck["alpha_sigma_fixed"] = sigma(alpha_F) == alpha_F

    z1 = R.one_minus(R.mul(alpha_F, alpha_F))
    z2 = R.add(R.sub(R.mul(z1, z1), z1), R.scal(2))
    ck["alpha_line_identities"] = (
        R.one_minus(z1) == R.mul(alpha_F, alpha_F)
        and R.one_minus(z2) == alpha_F
        and z1 == R.mul(minus1, R.pw(alpha_F, 3))
    )

    def dzeta(x):
        r = R.one()
        for k in range(1, m):
            r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, k), x)), k))
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
        troot = R.pw(zeta_N, e_t)
        w = R.mul(u, R.inv(tu))
        y = R.one()
        for _ in range(6):
            ym = R.pw(y, m)
            y = R.add(y, R.mul(R.sub(w, ym), R.inv(R.mul(R.scal(m), R.pw(y, m - 1)))))
        return R.mul(troot, y)

    x1 = mth_root_teich_dlog624(z1)
    x2 = mth_root_teich_dlog624(z2)
    ck["mth_roots_exact"] = R.pw(x1, m) == z1 and R.pw(x2, m) == z2
    d1invm = R.pw(R.inv(dzeta(R.one())), 3)
    P = R.mul(R.mul(R.pw(dzeta(x1), 2), dzeta(x2)), d1invm)
    ratio = R.mul(sigma(P), R.inv(P))

    def shift_exp(x):
        s = R.mul(sigma(x), R.inv(x))
        t = R.one()
        for r in range(m):
            if s == t:
                return r
            t = R.mul(t, zeta_m)
        return None

    r1s = shift_exp(x1)
    r2s = shift_exp(x2)
    ck["shift_exponents_in_mu_m"] = r1s is not None and r2s is not None
    res["shift_exponents"] = {"r1": r1s, "r2": r2s}
    integral = (2 * r1s) % m == 0 and (1 * r2s) % m == 0
    res["canonical_root_integral"] = integral

    g24 = R.pw(z624, 26)
    ck["g24_base_generator"] = (
        sigma(g24) == g24
        and R.pw(g24, 24) == R.one()
        and all(R.pw(g24, 24 // p) != R.one() for p in (2, 3))
    )
    gm = R.pw(g24, 24 // m)  # base mu_m generator
    ck["chi_B_nonvacuous_on_base"] = R.pw(gm, m) == R.one() and gm != R.one()
    MU = {}
    t = R.one()
    for e in range(m):
        MU[tuple(t)] = e
        t = R.mul(t, gm)

    def chi_B(u):
        return MU.get(tuple(R.pw(teich(u), 24 // m)))

    def galois_norm(u):
        r = R.one()
        v = u
        for _ in range(n_gal):
            r = R.mul(r, v)
            v = sigma(v)
        return r

    # ---- composed Sylow m-th root (for nu) --------------------------
    M_ORD = 5**d - 1
    v2 = 0
    tmp = M_ORD
    while tmp % 2 == 0:
        v2 += 1
        tmp //= 2
    v3 = 0
    while tmp % 3 == 0:
        v3 += 1
        tmp //= 3
    Q2 = M_ORD >> v2
    Q3 = M_ORD // 3**v3

    g2 = None
    g3 = None
    for seed_c in range(2, 200):
        g = teich([seed_c % MOD, 1] + [0] * (d - 2))
        if g2 is None:
            t2 = R.pw(g, Q2)
            if R.pw(t2, 2 ** (v2 - 1)) != R.one():
                g2 = t2
        if g3 is None:
            t3 = R.pw(g, Q3)
            if R.pw(t3, 3 ** (v3 - 1)) != R.one():
                g3 = t3
        if g2 is not None and g3 is not None:
            break
    ck["sylow_generators_found"] = g2 is not None and g3 is not None

    def sqrt_unit(u):
        tu = teich(u)
        tv = R.pw(tu, Q2)
        x = R.pw(tu, (Q2 + 1) >> 1)
        b = R.mul(R.pw(x, 2), R.inv(tu))
        while b != R.one():
            k = 0
            bb = b
            while bb != R.one():
                bb = R.pw(bb, 2)
                k += 1
            if k == v2:
                return None
            x = R.mul(x, R.pw(g2, 2 ** (v2 - 1 - k)))
            b = R.mul(R.pw(x, 2), R.inv(tu))
        w = R.mul(u, R.inv(tu))
        y = R.one()
        for _ in range(6):
            y = R.add(y, R.mul(R.sub(w, R.pw(y, 2)), R.inv(R.mul(R.scal(2), y))))
        return R.mul(x, y)

    def cbrt_unit(u):
        tu = teich(u)
        inv3v = pow(3**v3, -1, Q3)
        comp_Q = R.pw(tu, (3**v3 * inv3v) % M_ORD)
        comp_3 = R.mul(tu, R.inv(comp_Q))
        k = None
        t = R.one()
        for e in range(3**v3):
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
            y = R.add(y, R.mul(R.sub(w, R.pw(y, 3)), R.inv(R.mul(R.scal(3), R.pw(y, 2)))))
        return R.mul(root_t, y)

    def mth_root_general(u):
        mm = m
        v = u
        while mm % 3 == 0:
            v = cbrt_unit(v)
            if v is None:
                return None
            mm //= 3
        while mm % 2 == 0:
            v = sqrt_unit(v)
            if v is None:
                return None
            mm //= 2
        return v

    c_root = mth_root_general(ratio)
    ck["abstract_mth_root_exists"] = c_root is not None
    if c_root is not None:
        ck["c_pow_m_matches"] = R.pw(c_root, m) == ratio
        nu = galois_norm(c_root)
        nu_dlog = MU.get(tuple(nu))
        ck["nu_in_mu_m"] = nu_dlog is not None
        res["nu_dlog"] = nu_dlog

    # ---- canonical chain where integral ------------------------------
    if integral:
        c_canon = R.one()
        for xi, zi, ni, ri in ((x1, z1, 2, r1s), (x2, z2, 1, r2s)):
            if ri:
                c_canon = R.mul(
                    c_canon, R.pw(R.inv(R.one_minus(zi)), (ni * ri) // m)
                )
                pr = R.one()
                for k in range(ri):
                    pr = R.mul(pr, R.one_minus(R.mul(R.pw(zeta_m, k), xi)))
                c_canon = R.mul(c_canon, R.pw(pr, ni))
        ck["canonical_cocycle_pow_m_is_ratio"] = R.pw(c_canon, m) == ratio

        cks_ = [R.one()]
        acc = R.one()
        v = c_canon
        for k in range(1, n_gal):
            acc = R.mul(acc, v)
            cks_.append(acc)
            v = sigma(v)
        b_res = None
        for seed_c in range(2, 80):
            theta = [seed_c % MOD, 1] + [0] * (d - 2)
            bb = [0] * d
            th = theta
            for k in range(n_gal):
                bb = R.add(bb, R.mul(cks_[k], th))
                th = sigma(th)
            if any(x % 5 != 0 for x in bb):
                b_res = bb
                break
        ck["resolvent_unit_found"] = b_res is not None
        if b_res is not None:
            ck["splice_law_exact"] = R.mul(c_canon, sigma(b_res)) == b_res
            a_val = None
            for aa in (
                R.mul(P, R.pw(R.inv(b_res), m)),
                R.mul(P, R.pw(b_res, m)),
            ):
                if sigma(aa) == aa:
                    a_val = aa
                    break
            ck["descent_certificate_sigma_fixed"] = a_val is not None
            if a_val is not None:
                ck["base_teich_in_mu24"] = R.pw(teich(a_val), 24) == R.one()
                em = chi_B(a_val)
                ck["eps_m_class_defined"] = em is not None
                res["eps_m_dlog"] = em
    else:
        res["canonical_note"] = (
            f"fractional: m | 2r1 is {(2*r1s) % m == 0}, m | r2 is "
            f"{r2s % m == 0} — canonical m-th root needs canonical roots "
            "of base elements on the alpha-line; abstract layer pins nu only"
        )

    res["checks"] = ck
    # String, not a float. A wall-clock timing is provenance, not a measured
    # quantity, but `round(..., 1)` still lands a raw float64 in the witness and
    # the ratchet counts it like any other. Matches the corpus convention set by
    # 4e126c6f41 (35 timing fields across 28 producers).
    res["seconds"] = f"{time.time() - t0:.1f}"
    print(f"[m={m}] d={d} r=({r1s},{r2s}) integral={integral} "
          f"{sum(ck.values())}/{len(ck)} checks  {res['seconds']}s", flush=True)
    return res


t_all = time.time()
results = {}
for m in M_LIST:
    print(f"--- m = {m} ---", flush=True)
    results[m] = run_m(m)

allpass = all(all(r["checks"].values()) for r in results.values())
checks["all_per_m_checks_pass"] = allpass
for m in M_LIST:
    checks[f"m{m}_checks_pass"] = all(results[m]["checks"].values())

print(json.dumps(checks, indent=1))
summary = {
    m: {k: v for k, v in results[m].items() if k != "checks"} for m in M_LIST
}
print(json.dumps(summary, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass  total {round(time.time()-t_all,1)}s")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_descent_m4to24_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_descent_m4to24_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 (library/arxiv-1712.04887v3/1712.04887v3.pdf); GSWZ "
        "arXiv:2412.04241v2 eqn (270); Lean backbone "
        "QOU.Machinery.CyclicQuantumDilog (#4964); m=2/m=3 layers "
        "PR #4968"
    ),
    "checks": checks,
    "per_m": summary,
    "scope": (
        "scope-(a): shift exponents, canonical-root integrality, nu, "
        "and (where integral) the canonical eps_m value, for every "
        "remaining m | 24; fractional cases disclose the exact "
        "divisibility failure and pin nu only; no printed targets exist"
    ),
}
# Anchored to THIS FILE, not the caller's cwd. The literal path resolves only
# when the probe happens to be invoked from the repo root; run from its own
# directory — which is how the regeneration harness invokes every producer — it
# died with FileNotFoundError AFTER completing a 69-second compute, so the work
# was done and thrown away. Same cwd-assumption class as the `parents[2]` bug
# fixed in 12 scripts, and as `ocneanu_param_from_fibre_dimension` on this branch.
_OUT = pathlib.Path(__file__).resolve().parent / "gswz_epsm_descent_m4to24.witness.json"
with open(_OUT, "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
