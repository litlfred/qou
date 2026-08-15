"""eps_m on the GLOBAL 5_2 Bloch symbols — xi = 2[z1] + [z2], integer coefficients.

Bean qou-y3xv (the final eps_m layer of qou-9p9y). Scope-(a); no fit;
nothing wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 16).

CONTEXT. The root-of-unity decomposition (GSWZ (275)) carries 5-adic
coefficients whose mod-m reductions are not canonical (the m = 24
xi-class was honestly OPEN for exactly that reason, PR #4533). The
GLOBAL Bloch class (GSWZ (270)) has INTEGER coefficients:

    z1 = 1 - alpha^2,  z2 = z1^2 - z1 + 2,  z3 = z1   =>
    xi = 2[z1] + [z2]  in  B(K),  K = Q(alpha)/(alpha^3 - alpha^2 + 1),

with the Bloch condition sum_i z_i ^ (1 - z_i) = 0 in wedge^2 K^x.
This probe computes the CGZ P_zeta classes of the global symbols at
the 5-adic place Q_25, for every m | 24 — the canonical eps_m(xi)
R-side candidate data, free of the coefficient-truncation caveat.

KEY STRUCTURAL FACTS (verified in-probe):

* 1 - z1 = alpha^2 EXACTLY, so cls(1 - z1) = 2 * chi(alpha-class) —
  a closed form for the root-difference law's obstruction.
* Both z1, z2 are 5-adic units in the Q_25 component (their mod-5
  reductions are nonzero), so the construction is UNRAMIFIED: the
  m-th roots live in F = unramified extension containing mu_{624m}
  wait — precisely, containing an m-th root of the Teichmuller part
  (order dividing 624), i.e. mu_N with N = 624m always suffices;
  d = ord_5(N) stays modest (8..96 across m | 24).
* THE BLOCH SHADOW: the chi-character shadow of the wedge^2 condition
  is 2*cls(1 - z1) + cls(1 - z2) = 0 mod m; by the root-difference
  law this is exactly the condition making the xi-class ROOT-CHOICE
  CANONICAL. Posed as a check per m — a falsifiable computational
  shadow of xi in B(K).

WHAT THIS CHECKS (exact arithmetic in (Z/5^8)[x]/(h_d)) — WITH THE
STRUCTURAL-VACUITY FINDING (post-run honesty pass, the #4533 lesson
applied proactively):

1. Field integrity per m (irreducible h_d, zeta_N exact order, alpha
   Hensel-lifted, cubic root verified, z-embeddings exact).
2-3. The alpha^2 identity and Bloch shadow hold — but a diagnostic
   revealed they hold VACUOUSLY here: because 624m | 5^d - 1 by field
   construction, (5^d-1)/m = 0 mod 624, so chi_m kills ALL of mu_624
   — every unit with base Teichmuller data is an m-th power IN F.
   Check 5 makes this explicit (chi(zeta_N) != 0 control passes, so
   the character resolves F-classes; chi(zeta_624) = 0 structurally).
4. Root-difference law for the global symbols (real, non-vacuous at
   the F-level).
5. STRUCTURAL FINDING (the honest deliverable): the all-zero
   "classes" are F-CLASS COLLAPSE, not an eps-triviality statement.
   The CGZ eps-invariant lives in the BASE field: their descent
   P(xi) = a * b^m with a in F_n^x — extracting `a`'s base-field
   class requires the Galois norm/transfer from F down to Q_25(zeta_m),
   NOT the chi of the Kummer field. That descent is the defined next
   increment on qou-y3xv.

Long-compute note: the m = 24 field has degree d = ord_5(624*24); the
probe logs per-m progress (compute-audit discipline) and is run with
tee per AGENTS long-compute rules if wall > 5 min.
"""

import json
import math
import sys
import time

P5 = 5
W = 8
MOD = P5**W

checks = {}
detail = {}


def p5_mulmod(a, b, h):
    d = len(h) - 1
    out = [0] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai:
            for j, bj in enumerate(b):
                out[i + j] = (out[i + j] + ai * bj) % 5
    for i in range(len(out) - 1, d - 1, -1):
        c = out[i]
        if c:
            for j in range(d + 1):
                out[i - d + j] = (out[i - d + j] - c * h[j]) % 5
    return out[:d]


def p5_powmod_x(e, h):
    d = len(h) - 1
    result = [1] + [0] * (d - 1)
    base = ([0, 1] + [0] * (d - 2))[:d] if d > 1 else [0]
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


def irreducible_deg_d(d):
    import random
    rng = random.Random(20260802)
    primes = [p for p in range(2, d + 1) if d % p == 0 and all(p % q for q in range(2, p))]
    for _ in range(6000):
        h = [rng.randrange(5) for _ in range(d)] + [1]
        if h[0] == 0:
            continue
        xp = p5_powmod_x(5**d, h)
        if xp != ([0, 1] + [0] * (d - 2))[: len(xp)]:
            continue
        ok = True
        for p in primes:
            xq = p5_powmod_x(5 ** (d // p), h)
            diff = xq[:]
            if len(diff) > 1:
                diff[1] = (diff[1] - 1) % 5
            else:
                diff = [diff[0], 4]
            if len(p5_gcd(diff, h)) > 1:
                ok = False
                break
        if ok:
            return h
    raise AssertionError(f"no irreducible poly at degree {d}")


class Ring:
    def __init__(self, h):
        self.h = h
        self.d = len(h) - 1

    def mul(self, a, b):
        d = self.d
        out = [0] * (2 * d - 1)
        for i, ai in enumerate(a):
            if ai:
                for j, bj in enumerate(b):
                    out[i + j] = (out[i + j] + ai * bj) % MOD
        for i in range(len(out) - 1, d - 1, -1):
            c = out[i]
            if c:
                for j in range(d + 1):
                    out[i - d + j] = (out[i - d + j] - c * self.h[j]) % MOD
        return out[:d]

    def one(self):
        return [1] + [0] * (self.d - 1)

    def scal(self, n):
        return [n % MOD] + [0] * (self.d - 1)

    def pw(self, a, n):
        r = self.one()
        b = a[:]
        while n:
            if n & 1:
                r = self.mul(r, b)
            b = self.mul(b, b)
            n >>= 1
        return r

    def one_minus(self, t):
        out = [(-c) % MOD for c in t]
        out[0] = (out[0] + 1) % MOD
        return out

    def sub(self, a, b):
        return [(x - y) % MOD for x, y in zip(a, b)]

    def add(self, a, b):
        return [(x + y) % MOD for x, y in zip(a, b)]

    def inv(self, u):
        # Newton from a mod-5 seed found via the (5^d - 2) power trick on
        # the mod-5 reduction is expensive; use full Fermat instead:
        return self.pw(u, 5 ** self.d - 2) if False else self._inv_newton(u)

    def _inv_newton(self, u):
        # seed: invert mod 5 via Fermat in F_{5^d} using p5 machinery
        u5 = [c % 5 for c in u]
        seed5 = self._p5_pow(u5, 5 ** self.d - 2)
        inv = [c % MOD for c in seed5]
        for _ in range(5):
            t = self.mul(u, inv)
            corr = [(-c) % MOD for c in t]
            corr[0] = (corr[0] + 2) % MOD
            inv = self.mul(inv, corr)
        return inv

    def _p5_pow(self, a, e):
        h5 = [c % 5 for c in self.h]
        r = [1] + [0] * (self.d - 1)
        b = a[:]
        while e:
            if e & 1:
                r = p5_mulmod(r, b, h5)
            b = p5_mulmod(b, b, h5)
            e >>= 1
        return r


def ord5(M):
    d, v = 1, 5 % M
    while v != 1:
        v = (v * 5) % M
        d += 1
    return d


MS = [2, 3, 4, 6, 8, 12, 24]

all_field = True
all_a2 = True
all_bloch = True
all_law = True
all_collapse = True
xi_classes = {}
t0 = time.time()
for m in MS:
    N = 624 * m
    d = ord5(N)
    print(f"[{time.time()-t0:7.1f}s] m={m} N={N} d={d} — building field", flush=True)
    h5 = irreducible_deg_d(d)
    R = Ring([c % MOD for c in h5])
    # zeta_N: Teichmuller of exact order N
    zeta_N = None
    for seed_c in range(2, 60):
        g = [seed_c % MOD, 1] + [0] * (R.d - 2)
        u = R.pw(g, (5**d - 1) // N)
        for _ in range(14):
            u2 = R.pw(u, 5**d)
            if u2 == u:
                break
            u = u2
        if R.pw(u, N) == R.one() and all(
            R.pw(u, N // p) != R.one() for p in {2, 3, 13} if N % p == 0
        ):
            zeta_N = u
            break
    field_ok = zeta_N is not None
    # alpha in F: Hensel from the Teichmuller seed zeta_N^{N/624 * 26}...
    # alpha's Q_25-Teichmuller is zeta_624^e_a for some e_a; find by
    # refining from each candidate seed with Newton on the cubic:
    alpha_F = None
    if field_ok:
        z624 = R.pw(zeta_N, N // 624)
        # alpha mod 5 satisfies the quadratic factor; its Teichmuller is a
        # power of zeta_624 whose mod-5 value is a root of the cubic mod 5
        # in F_{5^d} \ F_5. Newton converges from any seed s with
        # cubic(s) = 0 mod 5:
        cand = R.one()
        for e in range(624):
            if e:
                cand = R.mul(cand, z624)
            c5 = [c % 5 for c in cand]
            # evaluate cubic mod 5
            v = p5_mulmod(p5_mulmod(c5, c5, [c % 5 for c in R.h]), c5, [c % 5 for c in R.h])
            w2 = p5_mulmod(c5, c5, [c % 5 for c in R.h])
            val = [(v[i] - w2[i]) % 5 for i in range(R.d)]
            val[0] = (val[0] + 1) % 5
            if all(x == 0 for x in val) and c5[0:2] != [2, 0]:
                # exclude the Q_5-rational root (alpha = 2 mod 5): need the
                # Q_25 component, whose reduction is NOT in F_5
                if any(c5[i] != 0 for i in range(1, R.d)):
                    alpha_F = cand[:]
                    break
        if alpha_F is not None:
            for _ in range(6):
                fa = R.sub(R.mul(R.mul(alpha_F, alpha_F), alpha_F), R.mul(alpha_F, alpha_F))
                fa[0] = (fa[0] + 1) % MOD
                dfa = R.sub(R.mul(R.scal(3), R.mul(alpha_F, alpha_F)), R.mul(R.scal(2), alpha_F))
                alpha_F = R.sub(alpha_F, R.mul(fa, R._inv_newton(dfa)))
            chk = R.sub(R.mul(R.mul(alpha_F, alpha_F), alpha_F), R.mul(alpha_F, alpha_F))
            chk[0] = (chk[0] + 1) % MOD
            field_ok = all(c == 0 for c in chk)
        else:
            field_ok = False
    all_field = all_field and field_ok
    if not field_ok:
        print(f"  m={m}: FIELD FAILED", flush=True)
        continue

    z1 = R.one_minus(R.mul(alpha_F, alpha_F))
    z2 = R.add(R.sub(R.mul(z1, z1), z1), R.scal(2))
    exp_chi = (5**d - 1) // m
    zeta_m = R.pw(zeta_N, N // m)

    def teich(u):
        v = u
        for _ in range(8):
            v2 = R.pw(v, 5**d)
            if v2 == v:
                return v
            v = v2
        return v

    def chi_dlog(u):
        """zeta_N-dlog of chi_m(u) = teich(u^{exp_chi}), or None."""
        v = teich(R.pw(u, exp_chi))
        # chi value lies in mu_m = <zeta_N^{N/m}>; brute-force m values
        t = R.one()
        step = R.pw(zeta_N, N // m)
        for e in range(m):
            if t == v:
                return e * (N // m)
            t = R.mul(t, step)
        return None

    def mth_root(u):
        """An m-th root of unit u in F: teich part via zeta_N-dlog
        (order divides 624 | N/m... root exists since mu_N has index-m
        roots), 1+5x part via binomial (m invertible)."""
        tu = teich(u)
        # dlog of tu in <zeta_624> (order divides 624)
        t = R.one()
        e_t = None
        for e in range(624):
            if t == tu:
                e_t = e
                break
            t = R.mul(t, z624)
        if e_t is None:
            return None
        # teich root: zeta_N^{e'} with e'*m = e_t*(N/624) mod N
        target = (e_t * (N // 624)) % N
        ep = None
        for cand_e in range(N):
            if (cand_e * m) % N == target:
                ep = cand_e
                break
        if ep is None:
            return None
        troot = R.pw(zeta_N, ep)
        # unit part: u / tu = 1 + 5x; its m-th root via Newton on y^m = w
        w = R.mul(u, R._inv_newton(tu))
        y = R.one()
        minv = pow(m, -1, MOD)
        for _ in range(6):
            ym = R.pw(y, m)
            corr = R.mul(R.sub(w, ym), R._inv_newton(R.mul(R.scal(m), R.pw(y, m - 1))))
            y = R.add(y, corr)
        return R.mul(troot, y)

    def dzeta(x):
        r = R.one()
        for k in range(1, m):
            r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, k), x)), k))
        return r

    # per-m collapse diagnostics (computed, not asserted): the control
    # chi(zeta_N) must be nonzero (character resolves F) while
    # chi(zeta_624) must vanish (mu_624 killed => F-collapse)
    _ctrl = chi_dlog(zeta_N)
    _kill = chi_dlog(z624)
    collapse_ok = _ctrl is not None and _ctrl % N != 0 and _kill == 0
    all_collapse = all_collapse and collapse_ok
    print(f"[{time.time()-t0:7.1f}s] m={m} — classes (ctrl={_ctrl}, mu624-kill={_kill})", flush=True)
    # (2) cls(1 - z1) = 2 * chi-class(alpha)
    c1z1 = chi_dlog(R.mul(alpha_F, alpha_F))
    ca = chi_dlog(alpha_F)
    ok_a2 = c1z1 is not None and ca is not None and (c1z1 - 2 * ca) % N == 0
    all_a2 = all_a2 and ok_a2
    # (3) Bloch shadow: 2*cls(1-z1) + cls(1-z2) = 0 mod m (in chi terms:
    # sum of dlogs = 0 mod N)
    c1z2 = chi_dlog(R.one_minus(z2))
    ok_bloch = c1z1 is not None and c1z2 is not None and (2 * c1z1 + c1z2) % N == 0
    all_bloch = all_bloch and ok_bloch
    # (4)+(5) P-classes with root-difference law
    d1inv = R._inv_newton(dzeta(R.one()))
    sym_cls = {}
    for name, zz, c1x in (("z1", z1, c1z1), ("z2", z2, c1z2)):
        x0 = mth_root(zz)
        if x0 is None:
            sym_cls[name] = None
            continue
        e0 = chi_dlog(R.mul(dzeta(x0), d1inv))
        x1 = R.mul(x0, zeta_m)
        e1 = chi_dlog(R.mul(dzeta(x1), d1inv))
        law_ok = (
            e0 is not None and e1 is not None and c1x is not None
            and (e1 - e0 + c1x) % N == 0
        )
        all_law = all_law and law_ok
        sym_cls[name] = e0
    if all(v is not None for v in sym_cls.values()):
        xi_classes[f"m{m}"] = {
            "xi_chi_dlog_zetaN": (2 * sym_cls["z1"] + sym_cls["z2"]) % N,
            "z1_class": sym_cls["z1"],
            "z2_class": sym_cls["z2"],
            "N": N,
            "d": d,
        }
    detail[f"m{m}"] = {"N": N, "d": d, "bloch_shadow": ok_bloch}
    print(f"[{time.time()-t0:7.1f}s] m={m} done: {xi_classes.get(f'm{m}')}", flush=True)

checks["field_construction_all_m"] = all_field
checks["one_minus_z1_alpha_squared_identity_holds"] = all_a2
checks["bloch_shadow_holds"] = all_bloch
checks["root_difference_law_global"] = all_law
# structural-vacuity disclosure, COMPUTED per m (Copilot #4588 fix —
# the first version hardcoded True): chi(zeta_N) != 0 (character
# resolves F) while chi(zeta_624) == 0 (mu_624 killed), for every m.
checks["classes_are_F_collapse_not_eps_data"] = all_collapse

print(json.dumps(checks, indent=1))
print(json.dumps(xi_classes, indent=1))
npass = sum(checks.values())
print(f"{npass}/{len(checks)} checks pass")

import subprocess

_sha = subprocess.run(
    ["git", "rev-parse", "HEAD"], capture_output=True, text=True
).stdout.strip()
witness = {
    "schema": "probe-witness/v1",
    "probe": "gswz_epsm_global_symbols_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_global_symbols_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "GSWZ arXiv:2412.04241v2 eqn (270) (library/arxiv-2412.04241v2/2412.04241v2.pdf); "
        "CGZ arXiv:1712.04887v3 (library/arxiv-1712.04887v3/1712.04887v3.pdf)"
    ),
    "place": "Q_25 place; unramified fields containing mu_{624m}",
    "checks": checks,
    "fields": detail,
    "xi_classes_F_level_all_collapsed": xi_classes,
    "structural_finding": (
        "chi_m kills mu_624 in every constructed field (624m | 5^d-1 "
        "=> (5^d-1)/m = 0 mod 624): the all-zero classes are Kummer-"
        "field collapse, NOT eps-triviality. The eps-invariant is the "
        "BASE-field class of the descended a (CGZ P(xi) = a*b^m); the "
        "Galois norm/transfer descent to Q_25(zeta_m) is the next "
        "increment (bean qou-y3xv)."
    ),
    "scope": (
        "scope-(a): global-symbol machinery built and law-verified in "
        "unramified fields to degree 96; the F-level class question is "
        "answered (structural collapse); the base-descent extraction "
        "of eps_m(xi) remains open and is precisely defined"
    ),
}
with open(
    "computations/probes/gswz_epsm_global_symbols.witness.json", "w"
) as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
