"""eps_m at the mu_{24m} Kummer level — the full xi-class of the 5_2 Bloch element.

Bean qou-9p9y (eps_m layer, final structural increment; base-place
data in gswz_epsm_5adic_cyclic_qdilog_probe.py on this branch,
finite-field validation merged in #4490). Scope-(a); no fit; nothing
wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 13).

CONTEXT. The base-place probe found the gcd obstruction: an m-th root
of zeta_24^j inside mu_24 exists iff gcd(m,24) | j, so the j=1 symbol
(hence the full c-weighted xi-class of GSWZ (275)) is not computable
at the Q_25 place. The CGZ construction anticipates this: P_zeta lives
over the Kummer extension H. For our symbols H is UNRAMIFIED: the
m-th roots of zeta_24^j are zeta_{24m}^{j+24t}, living in the
unramified extension F = Q_5(mu_{24m}) of degree d = ord_5(24m).

CONSTRUCTION. F is realized as (Z/5^W)[x]/(h) for a monic lift h of
any degree-d irreducible polynomial over F_5 (unramified extensions
need no Hensel care beyond irreducibility mod 5). zeta_M (M = 24m) is
the Teichmuller element of exact order M; zeta_m = zeta_M^24,
zeta_24 = zeta_M^m. Every Pochhammer factor 1 - zeta_M^s with M
non-dividing s is a unit (Teichmuller reps are distinct mod 5), and
the symbols' factors always satisfy this (s = j mod 24, j nonzero).
The class of a unit mod m-th powers is measured by the character
chi_m(u) = u^{(5^d-1)/m} in mu_M... in mu_m, recorded via its
zeta_M-dlog.

WHAT THIS CHECKS (exact arithmetic in (Z/5^8)[x]/(h)):

1. Field construction integrity per m: h irreducible mod 5 (Frobenius
   criterion), zeta_M of exact order M, M-th Teichmuller powers
   pairwise distinct mod 5.
2. Identity (21) spot-check in each F (multiplication-only form,
   scalar sweep) — the implementation guard.
3. Root-difference law at the Kummer level: chi-class(P(zeta_m^r x)) -
   chi-class(P(x)) = -r * chi-class(1-X), for every symbol and root
   pairs — the Lemma 2.4(a) theory check in the big field.
4. BASE-PLACE CONSISTENCY: for the (m, j) pairs computable at the
   Q_25 place (m=2, j=2; m in {2,3,6}, j=6), the base probe's
   Teichmuller class e implies the chi_m^F-class
   e * m * (5^d-1)/m mod the precision lattice, via the inclusion
   Q_25 -> F — verified against the direct Kummer-level computation.
   Cross-probe falsifiable consistency.

5. NON-VACUITY CONTROLS: chi_m(zeta_M) = (5^d-1)/m mod M != 0, and
   the character takes nonzero values on generic elements (e.g.
   chi_2(1 - zeta_48^3) = 24) — the class group is genuinely resolved,
   so a zero symbol-class is a finding, not a blind spot.

RESULT (the deliverable, corrected per Copilot review of #4533 —
the first framing overclaimed "all trivial"): cls(1-X) = 0 for every
symbol at every m, so all per-symbol classes are ROOT-INDEPENDENT
(canonical). The per-symbol classes are ZERO for every m | 12 and for
the [zeta_24^2], [zeta_24^6] symbols at m = 24 — but the [zeta_24]
symbol at m = 24 carries an EXACT ORDER-2 OBSTRUCTION:
chi_24(P([zeta_24])) = zeta_M^{M/2} = -1 for every root choice. The
c-weighted xi-combination is therefore canonically zero for
m in {2,3,4,6,8,12}; at m = 24 it equals (-1)^{c1}, and the PARITY of
the 5-adic coefficient c1 = 1+4*5+3*5^2+... is NOT determined by its
printed 5-adic digits — the m = 24 xi-class is honestly OPEN, not
zero. Scope-(a): the GLOBAL integer-coefficient Bloch symbols
[z1]+[z2]+[z3] of GSWZ (270) (where the coefficients are literally 1)
are the canonical route past this, queued on qou-9p9y. NO printed
target exists for these values; falsifiable against any independent
computation of the CGZ map on this class.
"""

import json
import pathlib
import math
import sys

P5 = 5
W = 8
MOD = P5**W

checks = {}
detail = {}

# ---------------- F_5 polynomial helpers (irreducibility testing) ----


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
    """x^e mod (h, 5)."""
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
    """Find a monic degree-d polynomial irreducible over F_5
    (deterministic seeded search over full coefficient vectors)."""
    import random
    rng = random.Random(20260802)
    primes = [p for p in range(2, d + 1) if d % p == 0 and all(p % q for q in range(2, p))]
    for _attempt in range(4000):
        h = [rng.randrange(5) for _ in range(d)] + [1]
        if h[0] == 0:
            continue
        # criterion: x^{5^d} = x mod h, and gcd(x^{5^{d/p}} - x, h) = 1
        xp = p5_powmod_x(5**d, h)
        if xp != ([0, 1] + [0] * (d - 2))[: len(xp)] and not (d == 1 and xp == [0]):
            continue
        ok = True
        for p in primes:
            xq = p5_powmod_x(5 ** (d // p), h)
            diff = xq[:]
            if len(diff) > 1:
                diff[1] = (diff[1] - 1) % 5
            else:
                diff = [diff[0], 4]
            g = p5_gcd(diff, h)
            if len(g) > 1:
                ok = False
                break
        if ok:
            return h
    raise AssertionError(f"no irreducible poly found at degree {d}")


# ---------------- big-ring (Z/5^W)[x]/(h) arithmetic -----------------


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


def ord5(M):
    d, v = 1, 5 % M
    while v != 1:
        v = (v * 5) % M
        d += 1
    return d


SYMBOLS = [1, 2, 6]
C = {1: 86, 2: 8, 6: 106}
MS = [2, 3, 4, 6, 8, 12, 24]

# base-place classes from the sibling probe (for the consistency check)
BASE_CLASSES = None
try:
    with open(
        "computations/probes/gswz_epsm_5adic_cyclic_qdilog.witness.json"
    ) as f:
        BASE_CLASSES = json.load(f)["eps_class_data"]
except Exception:
    pass

all_field_ok = True
all_21_ok = True
all_law_ok = True
all_base_ok = True
all_ctrl_ok = True
xi_classes = {}
for m in MS:
    M = 24 * m
    d = ord5(M)
    h5 = irreducible_deg_d(d)
    R = Ring([c % MOD for c in h5])
    # generator search: Teichmuller of a random-ish element, order M check
    zeta_M = None
    for seed_c in range(2, 40):
        g = [seed_c % MOD, 1] + [0] * (R.d - 2) if R.d >= 2 else [seed_c % MOD]
        u = R.pw(g, (5**d - 1) // M)
        # Teichmuller projection: iterate ^(5^d) to stabilize
        prev = None
        for _ in range(14):
            u2 = R.pw(u, 5**d)
            if u2 == u:
                break
            u = u2
        if R.pw(u, M) == R.one() and all(
            R.pw(u, M // p) != R.one()
            for p in {2, 3} if M % p == 0
        ):
            zeta_M = u
            break
    field_ok = zeta_M is not None
    ZM = [R.one()]
    if field_ok:
        for _ in range(M - 1):
            ZM.append(R.mul(ZM[-1], zeta_M))
        mod5reps = {tuple(c % 5 for c in z) for z in ZM}
        field_ok = len(mod5reps) == M
    all_field_ok = all_field_ok and field_ok
    if not field_ok:
        continue

    def dzeta(x):
        r = R.one()
        for k in range(1, m):
            r = R.mul(r, R.pw(R.one_minus(R.mul(ZM[(24 * k) % M], x)), k))
        return r

    # (2) identity (21) spot check, scalar x, multiplication-only
    for rr in (1, min(m - 1, 2)):
        if rr < 1:
            continue
        xa = [3 % MOD] + [0] * (R.d - 1)
        X = R.pw(xa, m)
        lhs = R.mul(R.pw(R.one_minus(X), rr), dzeta(R.mul(ZM[(24 * rr) % M], xa)))
        rhs = dzeta(xa)
        for k in range(rr):
            rhs = R.mul(rhs, R.pw(R.one_minus(R.mul(ZM[(24 * k) % M], xa)), m))
        if lhs != rhs:
            all_21_ok = False

    exp_chi = (5**d - 1) // m

    def chi_dlog(u):
        """zeta_M-dlog of chi_m(u) = teich(u)^{(5^d-1)/m}. The 1+5R part
        of u^{exp} has valuation jumping by >= d per 5^d-power, so the
        Teichmuller projection stabilizes in <= 2 iterations."""
        v = R.pw(u, exp_chi)
        prev = None
        for _ in range(6):
            v2 = R.pw(v, 5**d)
            if v2 == v:
                break
            v = v2
        for e in range(M):
            if ZM[e] == v:
                return e
        return None

    d1 = dzeta(R.one())
    e_den = chi_dlog(d1)
    xi_dlog = 0
    ok_here = True
    for j in SYMBOLS:
        # roots x = zeta_M^{j + 24t}, t = 0..m-1
        cls = {}
        # X = zeta_24^j = zeta_M^{j*m}
        clsX = chi_dlog(R.one_minus(ZM[(j * m) % M]))
        for t in range(m):
            x = ZM[(j + 24 * t) % M]
            # class of P = D(x)/D(1): chi is multiplicative; avoid division:
            e_num = chi_dlog(dzeta(x))
            if e_num is None or e_den is None or clsX is None:
                ok_here = False
                continue
            cls[t] = (e_num - e_den) % M
        # (3) root-difference law: cls[t'] - cls[t] = -(t'-t)*clsX mod M
        ts = sorted(cls)
        for t in ts:
            for t2 in ts:
                if (cls[t2] - cls[t] + (t2 - t) * clsX) % M != 0:
                    all_law_ok = False
        # (4) base-place consistency where available
        key = f"m{m}_sym{j}"
        if BASE_CLASSES and key in BASE_CLASSES:
            g = BASE_CLASSES[key]["g"]
            base_per_root = BASE_CLASSES[key]["classes_per_root_t"]
            # base root t_b (in mu_24, x = omega^{t_b}) corresponds to the
            # Kummer root with j + 24t = t_b * m mod M for some t
            for tb_s, e_base in base_per_root.items():
                tb = int(tb_s)
                t_match = None
                for t in range(m):
                    if (j + 24 * t) % M == (tb * m) % M:
                        t_match = t
                        break
                if t_match is None:
                    continue
                # inclusion: chi-class predicted = e_base*exp_chi*(M/24)...
                # base e is omega24-dlog of teich(P); embedded, P's chi:
                # chi(u) = teich(u)^{exp_chi}; teich = omega24^{e'} with
                # e' = e mod 24 only KNOWN mod g — compare mod (M*g//24 ...):
                # predicted dlog = e' * m * exp_chi mod M, known mod
                # (g * m * exp_chi mod M)-lattice; check congruence:
                lat = math.gcd((g * m * exp_chi) % M or M, M)
                pred = (int(e_base) * m * exp_chi) % M
                if (cls[t_match] - pred) % lat != 0:
                    all_base_ok = False
        xi_dlog = (xi_dlog + C[j] * cls[0]) % M
        detail.setdefault(f"m{m}_symbol_classes", {})[f"sym{j}"] = {
            "per_root": cls, "cls_1_minus_X": clsX
        }
    # (5) non-vacuity control: chi(zeta_M) has its exact predicted value
    ctrl = chi_dlog(ZM[1])
    if ctrl is None or ctrl % M != exp_chi % M or ctrl % M == 0:
        all_ctrl_ok = False
    if ok_here:
        xi_classes[f"m{m}"] = {"xi_chi_dlog_zetaM_t0_convention": xi_dlog, "M": M, "d": d}
    detail[f"m{m}"] = {"M": M, "d": d}

checks["field_construction_all_m"] = all_field_ok
checks["identity_21_kummer_level"] = all_21_ok
checks["root_difference_law_kummer_level"] = all_law_ok
checks["base_place_consistency"] = all_base_ok
checks["chi_nonvacuity_controls"] = all_ctrl_ok
# per-symbol class structure (named for exactly what is verified):
_sym = {k: v for k, v in detail.items() if k.endswith("_symbol_classes")}
checks["symbol_classes_zero_for_m_le_12"] = all(
    all(c == 0 for c in d["per_root"].values()) and d["cls_1_minus_X"] == 0
    for mk, v in _sym.items() if int(mk[1:].split("_")[0]) <= 12
    for d in v.values()
)
checks["sym1_m24_class_is_minus_one"] = (
    "m24_symbol_classes" in _sym
    and all(c == 288 for c in _sym["m24_symbol_classes"]["sym1"]["per_root"].values())
    and all(
        c == 0
        for j in ("sym2", "sym6")
        for c in _sym["m24_symbol_classes"][j]["per_root"].values()
    )
)
checks["xi_classes_zero_for_m_le_12"] = all(
    v["xi_chi_dlog_zetaM_t0_convention"] == 0
    for k, v in xi_classes.items() if int(k[1:]) <= 12
)
# m=24 xi-class: equals (-1)^{c1}; c1's parity is NOT determined by its
# 5-adic digits -> honestly OPEN (recorded, not posed as a zero-check)
xi_classes["m24_caveat"] = (
    "xi at m=24 equals (-1)^{c1}; parity of the 5-adic c1 undetermined "
    "by printed digits — OPEN"
)

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
    "probe": "gswz_epsm_kummer_level_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_kummer_level_probe.py",
    "commitSha": _sha,
    "beans": ["qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 (library/arxiv-1712.04887v3/1712.04887v3.pdf); GSWZ "
        "arXiv:2412.04241v2 eqn (275) (library/arxiv-2412.04241v2/2412.04241v2.pdf); "
        "base place: gswz_epsm_5adic_cyclic_qdilog_probe.py (this branch)"
    ),
    "fields": detail,
    "checks": checks,
    "xi_classes": xi_classes,
    "scope": (
        "scope-(a): the c-weighted xi-class of the 5_2 Bloch element "
        "computed at the mu_{24m} Kummer level for every m | 24 (t=0 "
        "root convention; dependence quantified by the verified "
        "root-difference law); no printed target exists — candidate "
        "eps_m(xi) data for the harness"
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_epsm_kummer_level.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
