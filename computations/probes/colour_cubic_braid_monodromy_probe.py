#!/usr/bin/env python3
"""
Probe — Step-2 option C, prune P5 (bean qou-d0qq; plan §B of
docs/audits/2026-09-07-route-c-step3-and-kz-level-plans.md): the BRAID WORD of each
lasso around the six branch points of the colour cubic, and whether it is a half-twist.

`colour_cubic_branch_monodromy_probe.py` (11/11) records only the PERMUTATION in S₃ that
each lasso induces on the three roots X₁(z), X₂(z), X₃(z) of the colour cubic

    P(X, z) = X³ + (z+1)X² + (z²+z+1)X + (z³+z²+z+1)

around each of the six simple branch points (roots of D(z) = 16z⁶+24z⁵+35z⁴+50z³+35z²+24z+16,
Lean: QOU.Mass.ColourCubicDiscriminant).  Option C pulls the sl₂ KZ connection on Conf₃(ℂ)
back along the root map z ↦ {X₁, X₂, X₃}(z), so what matters is the lift of each lasso to
the braid group B₃ = π₁(Conf₃(ℂ)), not its image in S₃.  A simple branch point should give a
half-twist, i.e. a conjugate of σ_i^{±1}; a full twist or a longer word would not.

WHAT IS COMPUTED (mpmath 50 dps for the continuation, sympy exact for every invariant; no
float64 anywhere; no q₀ read — the cubic is a fixed integer polynomial):

  1. The cubic, its discriminant, the six branch points and the six lassos are REUSED from
     colour_cubic_branch_monodromy_probe (P, roots_at, lasso, perm_of, compose imported; the
     branch-point / radius / detour / departure-order construction copied verbatim from its
     main()).  The branch points are cross-checked against that probe's committed witness.
  2. Braid diagram convention.  Strands are the three roots in ℂ; the diagram projects onto
     the axis x(X) = Re(e^{−iθ}X) with height y(X) = Im(e^{−iθ}X), θ = 1/5 (a rotation is
     needed because at the base point z = 0 the roots ±i have EQUAL real part).  Positions
     1, 2, 3 are the strands ordered by increasing x.  A crossing is a change of the x-order of
     two ADJACENT positions i, i+1 and is recorded as σ_i^{ε}, with
         ε = +1  iff the strand initially at position i (smaller x) passes BEHIND (smaller y)
                 the strand initially at position i+1 at the crossing instant,
     so that a counter-clockwise exchange of two roots is a POSITIVE half-twist and a
     counter-clockwise rotation of the whole configuration by 2π is the positive full twist
     Δ².  (The opposite convention inverts every word; it changes no conjugacy verdict.)
  3. Continuation is adaptive: each segment of the sampled lasso is accepted only if the
     nearest-neighbour matching is unambiguous (best match 3× closer than the runner-up, each
     root moved by less than a third of the minimal root separation), the x-order changes by
     at most ONE adjacent transposition, and at such a crossing the height difference has the
     same sign at both ends of the segment (so the sign is unambiguous); otherwise the
     segment is bisected, recursively.  The crossing instant is located by linear
     interpolation of the x-difference, and the height difference there is recorded.
  4. Per lasso j = 1..6 (departure-angle order of the existing probe): the word w_j ∈ B₃; the
     induced permutation (checked against the existing probe's perm_of); the exponent sum
     (abelianisation B₃ → ℤ); the characteristic polynomial of the reduced Burau matrix
     (σ₁ ↦ [[−t,1],[0,1]], σ₂ ↦ [[1,0],[t,−t]], exact over ℤ[t,t⁻¹]); and the Garside data:
     left-normal form Δ^k A₁⋯A_r (hand-rolled permutation-braid algorithm for B₃), the
     super summit set reached by cycling/decycling and closed under conjugation by simple
     elements (Elrifai–Morton), and — when the SSS meets {σ₁, σ₂, σ₁⁻¹, σ₂⁻¹} — an EXPLICIT
     conjugator g with g⁻¹ w_j g = σ_i^{±1}, verified twice: by the normal form (a solution
     of the word problem) and by the Burau matrices.
     (i) transposition, (ii) exponent sum ±1, (iii) Burau char poly = that of σ₁^{±1} are
     NECESSARY conditions for conjugacy to a half-twist; the explicit conjugator is a
     SUFFICIENT certificate.  A negative Garside verdict would rely on the SSS theory.
  5. Global check: the product w_1 w_2 ⋯ w_6 in departure order (first lasso first) is
     compared, as a braid, with the monodromy of an independently continued large loop
     (out along the negative real axis, a counter-clockwise circle of radius 4, back), and
     that loop's normal form is compared with the full twist Δ² (at z → ∞ the roots are
     −z, ±iz and rotate rigidly once).

INTERPRETATION (consequence, not something proved here): if all six are half-twists, the
monodromy generators of the pulled-back KZ connection are conjugates of ϱ(σ_i^{±1}), and
the Hecke quadratic on them follows from Kohno–Drinfeld (ϱ(σ_i) has eigenvalues q, −q⁻¹ in
the framework's normalisation).  If any lasso were not a half-twist that would be a
scope-(a) finding recorded with its word.

Run: PYTHONPATH=computations python3 -u computations/probes/colour_cubic_braid_monodromy_probe.py \\
       2>&1 | tee /tmp/kz-b1-run.log
"""
from __future__ import annotations

import json
import os
import sys
import time
from collections import deque

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from colour_cubic_branch_monodromy_probe import (  # noqa: E402
    P, X, z, roots_at, lasso, perm_of, compose,
)

mp.mp.dps = 50
T0 = time.monotonic()
HERE = os.path.dirname(os.path.abspath(__file__))


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:5.1f}s] {msg}", flush=True)


# ============================================================================
# Braid-diagram projection and adaptive continuation
# ============================================================================
THETA = mp.mpf(1) / 5
ROT = mp.exp(-1j * THETA)
MAXD = 40                      # maximal bisection depth per segment
TIE = mp.mpf("1e-30")          # two strands at the same x at a SAMPLE point → bisect


def xy(r):
    w = ROT * r
    return mp.re(w), mp.im(w)


def order_of(rts):
    """Tuple of strand labels sorted by increasing x; None if two x's tie."""
    xs = [xy(r)[0] for r in rts]
    if min(abs(xs[i] - xs[j]) for i in range(3) for j in range(i + 1, 3)) < TIE:
        return None
    return tuple(sorted(range(3), key=lambda a: xs[a]))


def match(cur, new):
    """Nearest-neighbour matching of the tracked triple `cur` onto the fresh roots `new`,
    with the ambiguity guards of the existing probe; None if ambiguous."""
    assigned, used = [], set()
    sep = min(abs(cur[i] - cur[j]) for i in range(3) for j in range(i + 1, 3))
    for c in cur:
        d = sorted((abs(c - n), j) for j, n in enumerate(new))
        if d[1][0] < 3 * d[0][0]:
            return None
        if d[0][1] in used or d[0][0] > sep / 3:
            return None
        used.add(d[0][1])
        assigned.append(new[d[0][1]])
    return assigned


class Tracker:
    """Continue the three roots along a polyline, emitting braid letters at every crossing."""

    def __init__(self):
        self.letters = []
        self.crossings = []      # (letter, |height difference| at crossing) records
        self.splits = 0
        self.min_sep = mp.inf
        self.min_cross_height = mp.inf

    def advance(self, z0, z1, cur, depth=0):
        new = match(cur, roots_at(z1))
        if new is not None:
            sep = min(abs(new[i] - new[j]) for i in range(3) for j in range(i + 1, 3))
            self.min_sep = min(self.min_sep, sep)
            o0, o1 = order_of(cur), order_of(new)
            if o0 is not None and o1 is not None:
                if o0 == o1:
                    return new
                diff = [p for p in range(3) if o0[p] != o1[p]]
                if len(diff) == 2 and diff[1] == diff[0] + 1 and o0[diff[0]] == o1[diff[1]] \
                        and o0[diff[1]] == o1[diff[0]]:
                    p = diff[0]
                    a, b = o0[p], o0[p + 1]          # a at position p (smaller x) before
                    xa0, ya0 = xy(cur[a]); xb0, yb0 = xy(cur[b])
                    xa1, ya1 = xy(new[a]); xb1, yb1 = xy(new[b])
                    d0, d1 = xa0 - xb0, xa1 - xb1
                    e0, e1 = ya0 - yb0, ya1 - yb1
                    if d0 < 0 < d1 and e0 * e1 > 0:
                        t = d0 / (d0 - d1)
                        es = e0 + t * (e1 - e0)
                        sign = 1 if es < 0 else -1   # left strand passes behind → positive
                        self.letters.append(sign * (p + 1))
                        self.crossings.append((sign * (p + 1), abs(es)))
                        self.min_cross_height = min(self.min_cross_height, abs(es))
                        return new
        if depth >= MAXD:
            raise RuntimeError(f"continuation could not be resolved at depth {MAXD} near z = {mp.nstr(z1, 12)}")
        self.splits += 1
        zm = (z0 + z1) / 2
        mid = self.advance(z0, zm, cur, depth + 1)
        return self.advance(zm, z1, mid, depth + 1)

    def run(self, pts, start):
        cur = list(start)
        for i in range(1, len(pts)):
            cur = self.advance(pts[i - 1], pts[i], cur)
        return cur


# ============================================================================
# B₃: exact word-level invariants
# ============================================================================
def word_str(w):
    if not w:
        return "e"
    return " ".join(f"s{abs(a)}" + ("" if a > 0 else "^-1") for a in w)


def inv_word(w):
    return [-a for a in reversed(w)]


def perm_of_word(w):
    """Positions (0-indexed) → strand labels after applying the word to arr = identity."""
    arr = [0, 1, 2]
    for a in w:
        i = abs(a) - 1
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return tuple(arr)


t, x = sp.symbols("t x")
BURAU = {
    1: sp.Matrix([[-t, 1], [0, 1]]),
    2: sp.Matrix([[1, 0], [t, -t]]),
}
BURAU[-1] = BURAU[1].inv()
BURAU[-2] = BURAU[2].inv()


def burau(w):
    M = sp.eye(2)
    for a in w:
        M = M * BURAU[a]
    return M.applyfunc(sp.cancel)


def charpoly(M):
    return sp.expand(sp.cancel((M - x * sp.eye(2)).det()))


# ---- Garside structure of B₃ via permutation braids --------------------------------
def pmul(p, q):  # (p*q)(i) = p(q(i)); word a1 a2 ↦ s_{a1} * s_{a2}
    return tuple(p[q[i]] for i in range(3))


E3 = (0, 1, 2)
S = {1: (1, 0, 2), 2: (0, 2, 1)}
W0 = (2, 1, 0)                       # permutation of Δ = σ₁σ₂σ₁


def length(p):
    return sum(1 for i in range(3) for j in range(i + 1, 3) if p[i] > p[j])


def perm_of_pos_word(w):
    p = E3
    for a in w:
        p = pmul(p, S[a])
    return p


SIMPLE_WORD = {}
for w_ in ([], [1], [2], [1, 2], [2, 1], [1, 2, 1]):
    SIMPLE_WORD[perm_of_pos_word(w_)] = list(w_)
assert len(SIMPLE_WORD) == 6 and SIMPLE_WORD[W0] == [1, 2, 1]


def starting_set(p):   # {i : σ_i left-divides the simple element p}
    return [i for i in (1, 2) if length(pmul(S[i], p)) < length(p)]


def finishing_set(p):  # {i : σ_i right-divides p}
    return [i for i in (1, 2) if length(pmul(p, S[i])) < length(p)]


def tau_perm(p):       # Δ-conjugation σ_i ↦ σ_{3-i} on permutation braids
    return pmul(W0, pmul(p, W0))


def tau_word(w):
    return [(3 - abs(a)) * (1 if a > 0 else -1) for a in w]


DELTA_OVER_INV = {1: [1, 2], 2: [2, 1]}      # Δ σ₁⁻¹ = σ₁σ₂, Δ σ₂⁻¹ = σ₂σ₁


def positive_normal_form(pos):
    """Left-normal form Δ^m A₁⋯A_r of a positive word by local left-weighting."""
    fac = [S[a] for a in pos]
    changed, guard = True, 0
    while changed:
        changed = False
        guard += 1
        if guard > 10000:
            raise RuntimeError("left-weighting did not terminate")
        for j in range(len(fac) - 1):
            A, B = fac[j], fac[j + 1]
            while True:
                cand = [i for i in starting_set(B) if i not in finishing_set(A)]
                if not cand:
                    break
                i = cand[0]
                A, B = pmul(A, S[i]), pmul(S[i], B)
                changed = True
            fac[j], fac[j + 1] = A, B
    while fac and fac[-1] == E3:
        fac.pop()
    m = 0
    while fac and fac[0] == W0:
        fac.pop(0)
        m += 1
    for j in range(len(fac) - 1):        # sanity: the result is left-weighted
        assert all(i in finishing_set(fac[j]) for i in starting_set(fac[j + 1]))
    assert all(f not in (E3, W0) for f in fac)
    return m, tuple(fac)


def normal_form(word):
    """Left-normal form (k, (A₁,…,A_r)) of an arbitrary word in σ₁^{±1}, σ₂^{±1}."""
    k, pos = 0, []
    for a in word:
        if a > 0:
            pos.append(a)
        else:
            k -= 1
            pos = [3 - b for b in pos] + DELTA_OVER_INV[-a]
    m, fac = positive_normal_form(pos)
    return (k + m, fac)


def nf_word(nf):
    k, fac = nf
    w = ([1, 2, 1] * k) if k >= 0 else ([-1, -2, -1] * (-k))
    for f in fac:
        w = w + SIMPLE_WORD[f]
    return w


def nf_str(nf):
    k, fac = nf
    return f"Δ^{k} · " + (" · ".join("(" + word_str(SIMPLE_WORD[f]) + ")" for f in fac) if fac else "e")


def conj(nf, g):            # g⁻¹ · nf · g
    return normal_form(inv_word(g) + nf_word(nf) + g)


def cycle(nf):
    k, fac = nf
    if not fac:
        return nf, []
    A1 = fac[0] if k % 2 == 0 else tau_perm(fac[0])
    g = SIMPLE_WORD[A1]
    return conj(nf, g), g


def decycle(nf):
    k, fac = nf
    if not fac:
        return nf, []
    g = inv_word(SIMPLE_WORD[fac[-1]])   # conjugation by A_r: A_r · nf · A_r⁻¹
    return conj(nf, g), g


def inf_sup(nf):
    return nf[0], nf[0] + len(nf[1])


def free_reduce(w):
    out = []
    for a in w:
        if out and out[-1] == -a:
            out.pop()
        else:
            out.append(a)
    return out


def _climb(nf, g_tot, step, better):
    """Apply `step` up to 8 times; commit the chain only if it improves (Elrifai–Morton:
    an improvement, if one exists, occurs within a bounded number of iterations)."""
    trial_nf, trial_g = nf, []
    for _ in range(8):
        nf2, g = step(trial_nf)
        trial_nf, trial_g = nf2, trial_g + g
        if better(nf2, nf):
            return nf2, g_tot + trial_g, True
    return nf, g_tot, False


def super_summit_set(word):
    """Elrifai–Morton: cycle until inf stops rising, decycle until sup stops falling
    (alternating to a fixed point), then close under conjugation by simple elements.
    Returns the SSS as a dict nf → conjugator word g with g⁻¹ w g = nf."""
    nf = normal_form(word)
    g_tot = []
    while True:
        nf, g_tot, up = _climb(nf, g_tot, cycle, lambda a, b: a[0] > b[0])
        nf, g_tot, down = _climb(nf, g_tot, decycle,
                                 lambda a, b: inf_sup(a)[1] < inf_sup(b)[1] and a[0] >= b[0])
        if not (up or down):
            break
    target = inf_sup(nf)
    sss = {nf: free_reduce(g_tot)}
    queue = deque([nf])
    while queue:
        cur = queue.popleft()
        for p, s in SIMPLE_WORD.items():
            if p == E3:
                continue
            nxt = conj(cur, s)
            if inf_sup(nxt) == target and nxt not in sss:
                sss[nxt] = free_reduce(sss[cur] + s)
                queue.append(nxt)
    return sss


HALF_TWISTS = {normal_form([1]): [1], normal_form([2]): [2],
               normal_form([-1]): [-1], normal_form([-2]): [-2]}


def analyse(word, label):
    """All exact invariants of one braid word."""
    perm = perm_of_word(word)
    fixed = sum(1 for i in range(3) if perm[i] == i)
    expsum = sum(1 if a > 0 else -1 for a in word)
    M = burau(word)
    cp = charpoly(M)
    cp_target = charpoly(burau([1] * expsum if expsum >= 0 else [-1] * (-expsum)))
    nf = normal_form(word)
    sss = super_summit_set(word)
    hit = [h for h in HALF_TWISTS if h in sss]
    cert = None
    if hit:
        h = hit[0]
        g = nf_word(normal_form(sss[h]))       # reduce the accumulated conjugator to its normal-form word
        target = HALF_TWISTS[h]
        # verify the certificate twice: normal form (word problem) and Burau
        ok_nf = normal_form(inv_word(g) + word + g) == normal_form(target)
        ok_burau = (burau(inv_word(g) + word + g) - burau(target)).applyfunc(sp.cancel) == sp.zeros(2)
        cert = {"target": word_str(target), "g": word_str(g), "verified_normal_form": ok_nf,
                "verified_burau": ok_burau}
    res = {
        "label": label,
        "word": word_str(word),
        "letters": list(word),
        "length": len(word),
        "perm_from_word": list(perm),
        "is_transposition": fixed == 1,
        "exponent_sum": expsum,
        "exponent_sum_pm1": abs(expsum) == 1,
        "burau_charpoly": str(cp),
        "burau_charpoly_sigma1_pow_expsum": str(cp_target),
        "burau_charpoly_matches_half_twist": (abs(expsum) == 1) and sp.expand(cp - cp_target) == 0,
        "burau_det": str(sp.factor(M.det())),
        "normal_form": nf_str(nf),
        "inf_sup_canonical_length": [nf[0], nf[0] + len(nf[1]), len(nf[1])],
        "super_summit_set": sorted(nf_str(s) for s in sss),
        "sss_meets_half_twists": bool(hit),
        "conjugacy_certificate": cert,
    }
    res["necessary_conditions_pass"] = res["is_transposition"] and res["exponent_sum_pm1"] \
        and res["burau_charpoly_matches_half_twist"]
    res["half_twist_established"] = bool(cert) and cert["verified_normal_form"] and cert["verified_burau"]
    return res


# ============================================================================
def main() -> int:
    print("=" * 76)
    print(" Step-2 C / P5 — braid words of the six lassos of the colour cubic")
    print("=" * 76)

    # ---- Garside machinery self-tests (exact) ---------------------------------
    st_braid = normal_form([1, 2, 1]) == normal_form([2, 1, 2]) == (1, ())
    st_inv = normal_form([1, 2, 1, -1, -2, -1]) == (0, ()) and normal_form([1, -1]) == (0, ())
    st_full = normal_form([1, 2, 1, 1, 2, 1]) == (2, ()) and normal_form([1, 2] * 3) == (2, ())
    st_central = normal_form([1, 2, 1, 1, 2, 1, 2]) == normal_form([2, 1, 2, 1, 1, 2, 1])
    rnd = [1, -2, 1, 1, 2, -1, -1, 2, 2, -2, 1]
    st_burau_nf = (burau(rnd) - burau(nf_word(normal_form(rnd)))).applyfunc(sp.cancel) == sp.zeros(2)
    st_burau_rel = (burau([1, 2, 1]) - burau([2, 1, 2])).applyfunc(sp.cancel) == sp.zeros(2)
    sss1 = super_summit_set([1])
    st_sss = set(sss1) == {normal_form([1]), normal_form([2])}
    st_not_conj = not (set(super_summit_set([1, 2, 1, 1, 2, 1])) & set(HALF_TWISTS)) \
        and not (set(super_summit_set([1, 1])) & set(HALF_TWISTS)) \
        and not (set(super_summit_set([1, 2])) & set(HALF_TWISTS))
    g_test = [1, 2, -1, 2, 1, -2, -2, 1]
    st_conj_known = HALF_TWISTS.keys() & set(super_summit_set([2, 1, -2])) \
        and HALF_TWISTS.keys() & set(super_summit_set(inv_word(g_test) + [-2] + g_test))
    chk_garside = all([st_braid, st_inv, st_full, st_central, st_burau_nf, st_burau_rel, st_sss,
                       st_not_conj, bool(st_conj_known)])
    log(f"Garside self-tests: braid rel {st_braid}, inverses {st_inv}, Δ² {st_full}, Δ² central {st_central}, "
        f"Burau∘NF {st_burau_nf}, Burau braid rel {st_burau_rel}, SSS(σ₁)={{σ₁,σ₂}} {st_sss}, "
        f"Δ²/σ₁²/σ₁σ₂ not half-twists {st_not_conj}, σ₂σ₁σ₂⁻¹ ~ σ₁ {bool(st_conj_known)}")
    log(f"Burau charpoly(σ₁) = {charpoly(BURAU[1])};  charpoly(σ₁⁻¹) = {charpoly(BURAU[-1])}")

    # ---- branch points and lassos, as in colour_cubic_branch_monodromy_probe.main() ----
    D = sp.discriminant(P, X)
    Dp = sp.Poly(-D, z)
    chk_disc = sp.expand(-D - (16 * z ** 6 + 24 * z ** 5 + 35 * z ** 4 + 50 * z ** 3 + 35 * z ** 2 + 24 * z + 16)) == 0
    bps_mp = [mp.mpc(mp.mpf(str(sp.re(r))), mp.mpf(str(sp.im(r)))) for r in Dp.nroots(n=60)]
    prior_path = os.path.join(HERE, "colour-cubic-branch-monodromy.witness.json")
    chk_bps_prior = None
    prior_perms = None
    if os.path.exists(prior_path):
        with open(prior_path) as fh:
            prior = json.load(fh)
        prior_bps = [mp.mpmathify(s["z"].replace(" ", "")) for s in prior["data"]["branch_points"]]
        chk_bps_prior = len(prior_bps) == 6 and all(abs(a - b) < mp.mpf("1e-30") for a, b in zip(bps_mp, prior_bps))
        prior_perms = {e["k"]: tuple(e["perm"]) for e in prior["data"]["lasso_permutations_in_departure_order"]}
    log(f"discriminant exact {chk_disc}; six branch points match the committed witness to 1e-30: {chk_bps_prior}")

    base_roots = roots_at(mp.mpf(0))
    base_order = order_of(base_roots)
    chk_base_generic = base_order is not None
    base_pos = {a: base_order.index(a) for a in range(3)}
    log(f"base roots {[mp.nstr(r, 8) for r in base_roots]}; projection θ = 1/5; x-order (labels) {base_order}; "
        f"x = {[mp.nstr(xy(r)[0], 8) for r in base_roots]}")

    DETOUR = mp.mpf("0.2")
    info = []
    for k in range(6):
        zk = bps_mp[k]
        others = [abs(zk - bps_mp[j]) for j in range(6) if j != k]
        r = min(others) / 4
        blocked = any(abs(mp.arg(bps_mp[j]) - mp.arg(zk)) < mp.mpf("0.05") and abs(bps_mp[j]) < abs(zk)
                      for j in range(6) if j != k)
        det = DETOUR if blocked else mp.mpf(0)
        info.append((k, r, det, mp.arg(zk) + det))
    ordered = sorted(info, key=lambda t_: t_[3])
    order = [t_[0] for t_ in ordered]

    # ---- continuation with braid recording --------------------------------------
    results = []
    all_perm_consistent = True
    all_perm_prior = True
    for j, (k, r, det, dep) in enumerate(ordered, start=1):
        zk = bps_mp[k]
        pts = lasso(zk, r, n_rad=400, n_circ=800, detour=det)
        tr = Tracker()
        end = tr.run(pts, base_roots)
        p_labels = perm_of(base_roots, end)
        res = analyse(tr.letters, f"lasso {j} around z_{k}")
        res.update({"k": k, "j": j, "radius": mp.nstr(r, 20), "detour": mp.nstr(det, 5),
                    "departure_angle": mp.nstr(dep, 30), "z_k": mp.nstr(zk, 40),
                    "perm_labels_existing_convention": list(p_labels),
                    "bisections": tr.splits, "min_root_separation": mp.nstr(tr.min_sep, 15),
                    "min_height_gap_at_crossing": mp.nstr(tr.min_cross_height, 15),
                    "crossing_heights": [[c[0], mp.nstr(c[1], 12)] for c in tr.crossings]})
        # strand a ends at position base_pos[p_labels[a]]; from the word: arr.index(a)
        arr = res["perm_from_word"]
        consistent = all(arr.index(a) == base_pos[p_labels[a]] for a in range(3))
        res["perm_word_consistent_with_continuation"] = consistent
        all_perm_consistent &= consistent
        if prior_perms is not None:
            same = prior_perms.get(k) == p_labels
            res["perm_matches_committed_witness"] = same
            all_perm_prior &= same
        results.append(res)
        log(f"lasso {j} z_{k}: word = {res['word']}  (len {res['length']}, {tr.splits} bisections, "
            f"min sep {mp.nstr(tr.min_sep, 6)}, min |Δy| at crossing {mp.nstr(tr.min_cross_height, 6)})")
        log(f"     perm(word) {arr} | labels-perm {p_labels} consistent {consistent} | exp sum {res['exponent_sum']} "
            f"| Burau charpoly {res['burau_charpoly']} | NF {res['normal_form']}")
        log(f"     SSS = {res['super_summit_set']} ; necessary {res['necessary_conditions_pass']} ; "
            f"certificate {res['conjugacy_certificate']} ; ESTABLISHED {res['half_twist_established']}")

    chk_all_transp = all(r_["is_transposition"] for r_ in results)
    chk_all_expsum = all(r_["exponent_sum_pm1"] for r_ in results)
    chk_all_burau = all(r_["burau_charpoly_matches_half_twist"] for r_ in results)
    chk_all_necessary = all(r_["necessary_conditions_pass"] for r_ in results)
    chk_all_established = all(r_["half_twist_established"] for r_ in results)
    sss_sigma = {nf_str(normal_form([1])), nf_str(normal_form([2]))}
    chk_sss = all(set(r_["super_summit_set"]) == sss_sigma for r_ in results)

    # ---- global check: product vs loop at infinity ---------------------------
    product = []
    for r_ in results:
        product = product + r_["letters"]
    nf_prod = normal_form(product)
    R = mp.mpf(4)
    n1, n2 = 400, 1600
    out = [-R * mp.mpf(i) / n1 for i in range(n1 + 1)]
    circ = [R * mp.exp(1j * (mp.pi + 2 * mp.pi * mp.mpf(i) / n2)) for i in range(1, n2 + 1)]
    big = out + circ + out[::-1][1:]
    tr_inf = Tracker()
    end_inf = tr_inf.run(big, base_roots)
    perm_inf = perm_of(base_roots, end_inf)
    nf_inf = normal_form(tr_inf.letters)
    chk_inf_full_twist = nf_inf == (2, ())
    chk_prod_eq_inf = nf_prod == nf_inf
    chk_prod_burau = (burau(product) - burau(tr_inf.letters)).applyfunc(sp.cancel) == sp.zeros(2)
    log(f"product of the six words (departure order): {word_str(product)}  → NF {nf_str(nf_prod)}")
    log(f"loop at infinity (R = 4, {tr_inf.splits} bisections): word {word_str(tr_inf.letters)} → NF {nf_str(nf_inf)}; "
        f"labels-perm {perm_inf}; full twist Δ² {chk_inf_full_twist}; product == loop {chk_prod_eq_inf} "
        f"(Burau agrees {chk_prod_burau})")
    # the two distinct transpositions and the S₃ product, as in the existing probe
    prod_perm = (0, 1, 2)
    for r_ in results:
        prod_perm = compose(tuple(r_["perm_labels_existing_convention"]), prod_perm)
    chk_perm_prod_id = prod_perm == (0, 1, 2)

    checks = [
        ("Garside/Burau machinery self-tests (braid relation, Δ² central, SSS(σ₁) = {σ₁,σ₂}, non-half-twists rejected)", chk_garside),
        ("discriminant and six branch points reproduce the committed branch-monodromy witness", chk_disc and bool(chk_bps_prior)),
        ("base point z = 0 is generic for the projection x = Re(e^{-i/5} X): three distinct x", chk_base_generic),
        ("every lasso word induces the same permutation as direct root continuation (perm_of)", all_perm_consistent),
        ("every lasso permutation equals the committed witness's (departure order, k-labels)", all_perm_prior),
        ("(i) every lasso word induces a transposition", chk_all_transp),
        ("(ii) every lasso word has exponent sum ±1", chk_all_expsum),
        ("(iii) every lasso word's reduced-Burau char poly equals that of σ₁^{±1}", chk_all_burau),
        ("every lasso word's super summit set is exactly {σ₁, σ₂} (a conjugacy invariant; Elrifai–Morton)", chk_sss),
        ("every lasso word is conjugate to σ_i^{±1}: explicit conjugator verified by normal form and Burau", chk_all_established),
        ("loop at infinity is the positive full twist Δ² (roots −z, ±iz rotate once)", chk_inf_full_twist),
        ("product of the six lasso words in departure order equals the loop at infinity (normal form + Burau)", chk_prod_eq_inf and chk_prod_burau),
        ("ordered product of the six permutations is the identity (existing probe's check)", chk_perm_prod_id),
    ]
    print()
    ok = 0
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    signs = [r_["exponent_sum"] for r_ in results]
    verdict = (
        f"All six lassos lift to half-twists: each word is conjugate in B₃ to σ_i^{{±1}} (exponent sums "
        f"{signs}), with an explicit conjugator verified by the Garside normal form and the Burau "
        f"representation. Consequence (Kohno–Drinfeld, not proved here): the monodromy generators of the "
        f"sl₂ KZ connection pulled back along the root map are conjugates of ϱ(σ_i^{{±1}}), so they satisfy "
        f"the Hecke quadratic (σ − q)(σ + q⁻¹) = 0. The loop at infinity is the full twist Δ² and equals "
        f"the ordered product of the six half-twists."
        if chk_all_established and chk_inf_full_twist and chk_prod_eq_inf else
        "NOT all six lassos are half-twists, or the global check failed — scope (a): see per-lasso words.")
    wb = WitnessBuilder("colour-cubic-braid-monodromy", engine="mpmath+sympy", _script_path=__file__)
    wb.set_description(
        "Step-2 option C, prune P5 (audit 2026-09-07 §B): the braid word in B₃ of each of the six lassos "
        "of colour_cubic_branch_monodromy_probe around the simple branch points of the colour cubic, by "
        "adaptive analytic continuation of the three roots (mpmath 50 dps, projection x = Re(e^{-i/5}X), "
        "positive crossing = counter-clockwise exchange), with exact conjugacy invariants (permutation, "
        "exponent sum, reduced-Burau characteristic polynomial) and the Garside left-normal form / super "
        "summit set with an explicit verified conjugator to σ_i^{±1}. Global check: the product of the six "
        "words in departure order equals the independently continued loop at infinity, which is the full "
        "twist Δ². No q₀ read; every number is mpmath or exact sympy.")
    wb.set_content_block("conj:hecke-monodromy-step-two")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0",
                         expected="1", tolerance="0.5", source="mpmath 50 dps continuation / exact sympy")
    wb.add_parameter("cubic", "X^3 + (z+1)X^2 + (z^2+z+1)X + (z^3+z^2+z+1)")
    wb.add_parameter("base_point", "z = 0")
    wb.add_parameter("projection", "x = Re(e^{-i theta} X), y = Im(e^{-i theta} X), theta = 1/5")
    wb.add_parameter("sign_convention",
                     "sigma_i^{+1} iff the strand initially at position i (smaller x) passes behind "
                     "(smaller y) the strand at position i+1; counter-clockwise exchange is positive; "
                     "loop at infinity is then +Delta^2")
    wb.add_parameter("burau", "reduced Burau of B_3: s1 -> [[-t,1],[0,1]], s2 -> [[1,0],[t,-t]]")
    wb.add_parameter("lasso_sampling", "n_rad = 400, n_circ = 800 as in the existing probe, then adaptive bisection")
    wb.add_parameter("loop_at_infinity", "0 -> -4 along the negative real axis, counter-clockwise circle |z| = 4, back")
    wb.add_data("lasso_words_in_departure_order", results)
    wb.add_data("six_words", [{"j": r_["j"], "k": r_["k"], "word": r_["word"], "letters": r_["letters"]}
                              for r_ in results])
    wb.add_data("product_word", {"word": word_str(product), "letters": product, "normal_form": nf_str(nf_prod)})
    wb.add_data("loop_at_infinity", {"word": word_str(tr_inf.letters), "letters": list(tr_inf.letters),
                                     "normal_form": nf_str(nf_inf), "perm_labels": list(perm_inf),
                                     "bisections": tr_inf.splits,
                                     "min_root_separation": mp.nstr(tr_inf.min_sep, 15)})
    wb.add_data("burau_charpoly_sigma1", str(charpoly(BURAU[1])))
    wb.add_data("burau_charpoly_sigma1_inv", str(charpoly(BURAU[-1])))
    wb.add_data("verdict", verdict)
    wb.add_caveat("(i)-(iii) are NECESSARY conditions for conjugacy to a half-twist; conjugacy is ESTABLISHED "
                  "only by the explicit conjugator g (g^-1 w g = sigma_i^{+-1} checked in the Garside normal form, "
                  "a solution of the word problem, and in the Burau representation, faithful for n = 3). "
                  "A negative Garside verdict would rely on the super-summit-set theory (Elrifai-Morton).")
    wb.add_caveat("Continuation is numerical (50 dps) with ambiguity guards and adaptive bisection; the words "
                  "are discrete data. The projection direction theta = 1/5 is a choice; a different generic "
                  "projection changes the words by conjugation and the sign convention by global inversion, "
                  "neither of which affects the verdicts.")
    wb.add_caveat("Consequence stated, not proved: Kohno-Drinfeld (kohno1987) gives the Hecke quadratic on "
                  "rho(sigma_i^{+-1}); this probe only establishes that the lasso lifts are conjugates of such.")
    out = wb.save({"q0Anchor": "independent",
                   "q0AnchorReason": ("the colour cubic is a fixed integer polynomial; its branch points, "
                                      "lassos and braid words carry no q and no substrate pin is read.")})
    print(f"  witness -> {os.path.relpath(out, os.path.join(HERE, '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
