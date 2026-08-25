"""eps_2(xi) by genuine Galois descent — the CGZ splice implemented at m = 2.

Bean qou-y3xv increment 2 (spec merged in #4946; Lean backbone
cyclicQDilog_class_shift merged in #4964). Scope-(a); no fit; nothing
wired; audit:
docs/audits/2026-07-26-tau-coherence-orbit-program-and-habiro-bridge.md
(Addendum 17).

CONTEXT. The Kummer-field classes collapse structurally (#4588:
mu_624 lies in (F^x)^m whenever mu_{624m} is in F), and the norm
route to CGZ's descended `a` is dead ([F:Q_25] = 2m for every m | 24,
#4946). What remains is CGZ's actual mechanism: P(xi) = a * b^m with
a in the base, extracted by an equivariant Hilbert-90 splice. This
probe implements it COMPLETELY for m = 2 — the smallest case, and the
one where the root-of-unity layer showed a genuine order-2 invariant.

THE ALGORITHM (B = Q_25, F = Q_5(mu_1248) of degree d = 8,
Gamma = Gal(F/B) = <sigma>, sigma = phi_5^2, n = [F:B] = 4):

1. sigma via the Hensel-lifted Frobenius: phi_5(x) = the root of h
   with residue seed x^5; sigma = phi_5 ∘ phi_5. Checked:
   h(sigma(x)) = 0 exactly and sigma^4 = id on the generator.
2. P = P(xi) = D(x1)^2 * D(x2) / D(1)^3 from the global-symbol
   machinery (#4588), t = 0 roots.
3. c = sqrt(sigma(P)/P): Teichmuller part by Tonelli-Shanks in the
   2-Sylow of mu_{5^8-1} (v_2(5^8 - 1) = 5; a full-order 2-element is
   found by deterministic-seeded sampling), unit part by Newton.
   Existence is guaranteed by the F-class collapse; c^2 = sigma(P)/P
   is checked exactly.
4. THE OBSTRUCTION INVARIANT nu = N_{F/B}(c) = prod_{k<4} sigma^k(c),
   in mu_2 = {+-1}. Independent of the sqrt choice (the mu_2
   ambiguity eta contributes N(eta) = eta^4 = 1) — nu is the
   H^1(Gamma, mu_2) obstruction class of the descent. Checked: nu is
   +-1 and is invariant under flipping the root choice.
5. If nu = 1: the additive Hilbert-90 resolvent b = sum_k c_k
   sigma^k(theta) with c_0 = 1, c_{k+1} = c * sigma(c_k), theta swept
   deterministically until b is a unit. Then c * sigma(b) = b exactly
   (checked), so sigma(b)/b = c^{-1}... i.e. (sigma(b)/b)^2 =
   (sigma(P)/P)^{-1}; a := P * b^{-2}... — orientation fixed by the
   DESCENT CERTIFICATE below, which is what actually gates.
6. THE DESCENT CERTIFICATE: sigma(a) = a exactly in the ring — a
   genuinely lands in the base B. This is the falsifiable heart: a
   wrong sigma, wrong splice, or wrong orientation fails it.
7. THE CHARACTER: chi_B = teich(.)^{12} = teich(.)^{(25-1)/2}, the
   genuine quadratic character of the base B = Q_25 (a is sigma-fixed,
   so teich(a) lies in the base Teichmuller mu_24; exponent 312 = 0
   mod 24 would be IDENTICALLY 1 on the base — a vacuity an earlier
   version shipped with, self-caught and fixed). theta ambiguities
   move a by base squares, killed by chi_B. BUT the abstract sqrt
   choice c -> -c is NOT killed: it moves a by v^2 with
   sigma(v) = -v, which forces teich(v)^24 = -1, i.e.
   chi_B(v^2) = -1 — the abstract-layer class FLIPS with the root
   choice (asserted as a check). The abstract layer therefore pins
   ONLY nu.
8. THE CANONICAL VALUE (the equivariant splice proper): sigma fixes
   z_i and alpha, and acts on the chosen roots by x_i -> zeta^{r_i}
   x_i (observed data: r_1 = 1, r_2 = 0). The Lean-proved shift law
   (21) (QOU.Machinery.CyclicQuantumDilog, #4964) then gives
   sigma(P)/P as an EXPLICIT product — for m = 2:
   D(-x)/D(x) = (1-x)^2/(1-z) — whose square root is forced (every
   exponent even BEFORE rooting, asserted from the data by
   canonical_root_integral):
       c_canon = [(1-x_1)^2/(1-z_1)]^{r_1} * ...
   No Tonelli choice anywhere. eps_2(xi) := chi_B(a_canon) for the
   c_canon-splice. Remaining choice x_1 -> -x_1 re-runs the whole
   canonical chain on flipped data; invariance is CHECKED, not
   assumed. Non-vacuity control at BASE level: g24 = zeta_624^{26} is
   sigma-fixed of exact order 24 and chi_B(g24) = -1 != 1.

NO printed target exists for eps_2(xi) (honest scope): the value is
candidate data, falsifiable against any independent computation of
the CGZ map on the 5_2 Bloch class. m = 3 (cube-root Tonelli) and the
remaining m | 24 are the natural next increments on qou-y3xv.
"""

import json
import pathlib
import sys
import time

P5 = 5
W = 8
MOD = P5**W
m = 2
N = 624 * m  # 1248
n_gal = 4    # [F : Q_25] = 2m

checks = {}


# ---------- F_5 helpers + field construction (as in #4588) ----------
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
    base = [0, 1] + [0] * (d - 2)
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
    rng = random.Random(20260810)
    primes = [p for p in range(2, d + 1) if d % p == 0 and all(p % q for q in range(2, p))]
    for _ in range(6000):
        h = [rng.randrange(5) for _ in range(d)] + [1]
        if h[0] == 0:
            continue
        if p5_powmod_x(5**d, h) != [0, 1] + [0] * (d - 2):
            continue
        ok = True
        for p in primes:
            xq = p5_powmod_x(5 ** (d // p), h)
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
        """Evaluate an R-element (list of scalars as x-coefficients) at
        a ring element `at` — used to apply Galois maps."""
        r = [0] * self.d
        for c in reversed(coeffs):
            r = self.mul(r, at)
            r[0] = (r[0] + c) % MOD
        return r


d = 8
h5 = irreducible_deg_d(d)
R = Ring([c % MOD for c in h5])
X = [0, 1] + [0] * (d - 2)

# Frobenius phi_5: x -> Hensel root of h with residue x^5
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
s4 = X[:]
for _ in range(n_gal):
    s4 = sigma(s4)
checks["frobenius_wellformed_and_sigma_order4"] = (
    all(c == 0 for c in hcheck) and s4 == X
)

# ---------- Teichmuller, zeta_N, alpha, symbols (as #4588) ----------
def teich(u):
    v = u
    for _ in range(10):
        v2 = R.pw(v, 5**d)
        if v2 == v:
            return v
        v = v2
    return v


zeta_N = None
for seed_c in range(2, 60):
    g = [seed_c % MOD, 1] + [0] * (d - 2)
    u = teich(R.pw(g, (5**d - 1) // N))
    if R.pw(u, N) == R.one() and all(
        R.pw(u, N // p) != R.one() for p in (2, 3, 13)
    ):
        zeta_N = u
        break
z624 = R.pw(zeta_N, N // 624)

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

z1 = R.one_minus(R.mul(alpha_F, alpha_F))
z2 = R.add(R.sub(R.mul(z1, z1), z1), R.scal(2))
zeta_m = R.pw(zeta_N, N // m)  # = -1


def dzeta(x):
    r = R.one()
    for k in range(1, m):
        r = R.mul(r, R.pw(R.one_minus(R.mul(R.pw(zeta_m, k), x)), k))
    return r


def mth_root_teich_dlog624(u):
    """m-th root of a unit whose Teichmuller lies in <zeta_624>."""
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
d1inv3 = R.pw(R.inv(dzeta(R.one())), 3)
P = R.mul(R.mul(R.pw(dzeta(x1), 2), dzeta(x2)), d1inv3)

# ---------- sqrt in F (Tonelli-Shanks on the Teichmuller part) -------
Q_ODD = (5**d - 1) >> 5  # 5^8-1 = 2^5 * Q_ODD
assert Q_ODD % 2 == 1 and (5**d - 1) == (Q_ODD << 5)

# full-order 2-element (deterministic seed sweep)
g2 = None
for seed_c in range(2, 80):
    g = teich([seed_c % MOD, 1] + [0] * (d - 2))
    t2 = R.pw(g, Q_ODD)
    if R.pw(t2, 2 ** 4) != R.one():
        g2 = t2
        break
checks["two_sylow_generator_found"] = g2 is not None


def sqrt_unit(u):
    """Square root of a unit u in F (or None): Tonelli-Shanks on the
    Teichmuller part + Newton on the 1+5R part."""
    tu = teich(u)
    # Tonelli-Shanks in mu_{5^d-1}
    tv = R.pw(tu, Q_ODD)          # 2-Sylow part
    r_exp = (Q_ODD + 1) >> 1
    x = R.pw(tu, r_exp)           # candidate sqrt of tu * (2-Sylow corr)
    # correct x by powers of g2 until x^2 = tu
    b = R.mul(R.pw(x, 2), R.inv(tu))
    c2 = g2
    e = 2 ** 4
    while b != R.one():
        # find least k with b^{2^k} = 1
        k = 0
        bb = b
        while bb != R.one():
            bb = R.pw(bb, 2)
            k += 1
        if k == 5:
            return None  # non-residue
        gk = R.pw(c2, 2 ** (4 - k))
        x = R.mul(x, gk)
        b = R.mul(R.pw(x, 2), R.inv(tu))
    # unit part
    w = R.mul(u, R.inv(tu))
    y = R.one()
    for _ in range(6):
        y = R.add(y, R.mul(R.sub(w, R.pw(y, 2)), R.inv(R.mul(R.scal(2), y))))
    return R.mul(x, y)


ratio = R.mul(sigma(P), R.inv(P))
c_root = sqrt_unit(ratio)
checks["sqrt_of_sigmaP_over_P_exists"] = c_root is not None
checks["c_squared_matches"] = c_root is not None and R.pw(c_root, 2) == ratio

# ---------- obstruction nu = N(c) in {+-1}, root-choice invariant ----
def galois_norm(u):
    r = R.one()
    v = u
    for _ in range(n_gal):
        r = R.mul(r, v)
        v = sigma(v)
    return r


minus1 = R.scal(-1)
nu = galois_norm(c_root)
nu_flip = galois_norm(R.mul(c_root, minus1))
checks["nu_in_mu2"] = nu in (R.one(), minus1)
checks["nu_root_choice_invariant"] = nu == nu_flip
nu_is_one = nu == R.one()

detail = {"nu_obstruction": "+1" if nu_is_one else "-1"}

# ---------- Hilbert-90 splice + descent machinery --------------------
def descend_and_class(c, Pv):
    """Resolvent b for the cocycle c, splice law, sigma-fixed
    certificate, base character. Returns (splice_ok, cert_ok,
    teich_in_mu24, class_str or None)."""
    cks = [R.one()]
    acc = R.one()
    v = c
    for k in range(1, n_gal):
        acc = R.mul(acc, v)
        cks.append(acc)
        v = sigma(v)
    b_res = None
    for seed_c in range(2, 60):
        theta = [seed_c % MOD, 1] + [0] * (d - 2)
        bb = [0] * d
        th = theta
        for k in range(n_gal):
            bb = R.add(bb, R.mul(cks[k], th))
            th = sigma(th)
        if any(x % 5 != 0 for x in bb):  # unit
            b_res = bb
            break
    if b_res is None:
        return (False, False, False, None)
    # splice law: c * sigma(b) = b, so sigma(b^2)/b^2 = c^{-2} =
    # P/sigma(P); the certificate adjudicates the orientation directly.
    splice_ok = R.mul(c, sigma(b_res)) == b_res
    a_val = None
    for aa in (R.mul(Pv, R.pw(R.inv(b_res), 2)), R.mul(Pv, R.pw(b_res, 2))):
        if sigma(aa) == aa:
            a_val = aa
            break
    if a_val is None:
        return (splice_ok, False, False, None)
    # a sigma-fixed => teich(a) in mu_24 (base Teichmuller). The genuine
    # quadratic character of B = Q_25 is teich(.)^{(25-1)/2} =
    # teich(.)^12 — NOT ^312, which is 0 mod 24 and hence IDENTICALLY 1
    # on the base (the vacuity an earlier version shipped with).
    ta = teich(a_val)
    in24 = R.pw(ta, 24) == R.one()
    chiB = R.pw(ta, 12)
    if chiB == R.one():
        cls = "+1"
    elif chiB == minus1:
        cls = "-1"
    else:
        cls = None
    return (splice_ok, True, in24, cls)


if nu_is_one:
    # --- abstract layer: the Tonelli root pins ONLY the obstruction ---
    # The abstract descent value FLIPS with the root choice c -> -c
    # (a = P b^{-2} changes by v^2 with sigma(v) = -v, forcing
    # teich(v)^24 = -1, i.e. chi_B(v^2) = -1). So chi_B(a) from an
    # arbitrary Tonelli branch is NOT an invariant; the invariant of
    # this layer is nu alone. The flip is asserted as a check — if the
    # ambiguity analysis were wrong, this fails.
    sp1, ct1, in24_1, cls_plus = descend_and_class(c_root, P)
    sp2, ct2, in24_2, cls_minus = descend_and_class(R.mul(c_root, minus1), P)
    checks["resolvent_unit_found"] = ct1 and ct2
    checks["splice_law_exact"] = sp1 and sp2
    checks["descent_certificate_sigma_fixed"] = ct1 and ct2
    checks["base_teich_in_mu24"] = in24_1 and in24_2
    checks["abstract_class_flips_with_root"] = (
        cls_plus is not None
        and cls_minus is not None
        and cls_plus != cls_minus
    )
    detail["abstract_layer"] = (
        f"chi_B(a) = {cls_plus} for c, {cls_minus} for -c: root-dependent "
        "by structure (NOT the invariant); the abstract layer pins nu only"
    )

    # --- CANONICAL layer: the equivariant cocycle from the Lean-proved
    # shift law (21) — no Tonelli choice anywhere -----------------------
    # sigma fixes z_i and acts on the chosen roots by x_i -> zeta^{r_i}
    # x_i; then sigma(P)/P = prod_i [D(zeta^{r_i} x_i)/D(x_i)]^{n_i}
    # with each factor an EXPLICIT product by (21):
    #   D(-x)/D(x) = (1-x)^2 / (1-z)   (m = 2, r = 1).
    # With multiplicities n = (2, 1) the square root is forced:
    #   c_canon = prod_i [(1-x_i)^2/(1-z_i)]^{n_i * r_i / ...} — every
    # exponent even before rooting iff n_i * r_i is even for the
    # fractional (1-z_i) part; asserted below from the DATA, not
    # assumed.
    def shift_exp(x):
        s = R.mul(sigma(x), R.inv(x))
        if s == R.one():
            return 0
        if s == minus1:
            return 1
        return None

    r1s = shift_exp(x1)
    r2s = shift_exp(x2)
    checks["frobenius_root_shift_in_mu2"] = r1s is not None and r2s is not None
    # integrality of the canonical root: each (1-z_i)^{n_i r_i} must
    # have even exponent (n_1, n_2) = (2, 1) => need n_i * r_i even.
    checks["canonical_root_integral"] = (2 * r1s) % 2 == 0 and (1 * r2s) % 2 == 0
    c_canon = R.one()
    for xi, zi, ni, ri in ((x1, z1, 2, r1s), (x2, z2, 1, r2s)):
        if ri:
            num = R.pw(R.one_minus(xi), ni)          # (1-x_i)^{n_i}
            den = R.pw(R.inv(R.one_minus(zi)), ni // 2)  # (1-z_i)^{-n_i/2}
            c_canon = R.mul(c_canon, R.mul(num, den))
    checks["canonical_cocycle_squares_to_ratio"] = R.pw(c_canon, 2) == ratio
    sp3, ct3, in24_3, cls_canon = descend_and_class(c_canon, P)
    checks["canonical_splice_and_certificate"] = sp3 and ct3 and in24_3
    checks["canonical_class_defined"] = cls_canon is not None
    detail["eps2_xi_class_canonical"] = cls_canon

    # --- x_1-root-choice invariance of the CANONICAL value -------------
    # x_1 -> -x_1 changes P by the shift law; the canonical chain is
    # re-run from scratch on the flipped data and must agree.
    x1b = R.mul(minus1, x1)
    r1b = shift_exp(x1b)
    Pb = R.mul(R.mul(R.pw(dzeta(x1b), 2), dzeta(x2)), d1inv3)
    ratio_b = R.mul(sigma(Pb), R.inv(Pb))
    c_canon_b = R.one()
    for xi, zi, ni, ri in ((x1b, z1, 2, r1b), (x2, z2, 1, r2s)):
        if ri:
            num = R.pw(R.one_minus(xi), ni)
            den = R.pw(R.inv(R.one_minus(zi)), ni // 2)
            c_canon_b = R.mul(c_canon_b, R.mul(num, den))
    checks["canonical_cocycle_b_squares_to_ratio"] = (
        R.pw(c_canon_b, 2) == ratio_b
    )
    sp4, ct4, in24_4, cls_canon_b = descend_and_class(c_canon_b, Pb)
    checks["canonical_value_x1_root_invariant"] = (
        sp4 and ct4 and cls_canon_b == cls_canon
    )
    detail["eps2_xi_class_canonical_x1_flipped"] = cls_canon_b
else:
    # obstructed branch: the splice/descent checks are NOT applicable and
    # are deliberately NOT added to `checks` (no hardcoded-True padding —
    # the check count differs by outcome, and that is honest). The
    # invariant carried forward IS nu.
    detail["eps2_xi_class_canonical"] = (
        "OBSTRUCTED (nu = -1): no F-level descent; the invariant IS nu"
    )

# non-vacuity: chi_B resolves the BASE group. g24 = zeta_624^26 is
# sigma-fixed (sigma acts by ^25; 624 | 24*26) of exact order 24, i.e.
# a generator of the base Teichmuller mu_24, and chi_B(g24) =
# g24^12 = -1 != 1. (The old control zeta_624^312 = -1 only showed the
# character nontrivial on F-level units — zeta_624 is not in B.)
g24 = R.pw(z624, 26)
checks["g24_base_generator"] = (
    sigma(g24) == g24
    and R.pw(g24, 24) == R.one()
    and all(R.pw(g24, 24 // p) != R.one() for p in (2, 3))
)
checks["chi_B_nonvacuous_on_base"] = R.pw(g24, 12) == minus1

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
    "probe": "gswz_epsm_descent_m2_probe",
    "engine": "python3-int-exact",
    "scriptFile": "gswz_epsm_descent_m2_probe.py",
    "commitSha": _sha,
    "beans": ["qou-y3xv", "qou-9p9y"],
    "source": (
        "CGZ arXiv:1712.04887v3 §2-3 descent (library/arxiv-1712.04887v3/1712.04887v3.pdf); "
        "GSWZ arXiv:2412.04241v2 eqn (270); Lean backbone "
        "QOU.Machinery.CyclicQuantumDilog (merged #4964)"
    ),
    "field": "F = Q_5(mu_1248), d = 8; base B = Q_25; Gamma = <phi_5^2>, n = 4",
    "checks": checks,
    "result": detail,
    "scope": (
        "scope-(a): the CGZ Galois descent implemented completely at "
        "m = 2 for the global 5_2 Bloch class xi = 2[z1] + [z2]; the "
        "sigma-fixed certificate gates the extraction; no printed "
        "target exists — falsifiable against any independent "
        "computation; m = 3 and general m | 24 queued"
    ),
}
with open(pathlib.Path(__file__).resolve().parent / "gswz_epsm_descent_m2.witness.json", "w") as f:
    json.dump(witness, f, indent=1)

sys.exit(0 if npass == len(checks) else 1)
