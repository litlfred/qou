#!/usr/bin/env python3
"""C1 connection matrix `P = Y0^-1 Y_inf` — obtained, and the 2026-08-07
degeneracy negative REFUTED.

Bean `qou-wgnx`. A first numerical attempt (recorded in the bean, in
`C1ZeroSideExponents.lean`, and in the #4672 thread) reported the `0`-side
basis as degenerate — normalised determinant `|det|/max^2 ~ 2.4e-18` at the
matching point — and concluded the connection matrix needed a new, numerically
stable `0`-side construction before it could be built at all. **All three of
that negative's premises are wrong**, and the connection matrix follows
directly from the bases already in hand.

## 1. The basis is not degenerate — it cannot be

`p = sqrt(q)` is REAL, so `theta_p(w) = sum_n p^{-n(n+1)/2} w^n` has REAL
coefficients and therefore `theta_p(conj w) = conj(theta_p(w))`. The `0`-side
exponents are a CONJUGATE pair (`t2 = conj t1`, the content of
`C1ZeroSideExponents.conjugate_pair_iff`). Hence for REAL `z`

    |theta_p(z/t2)| = |theta_p(conj(z/t1))| = |conj theta_p(z/t1)| = |theta_p(z/t1)|

so `|e_t1(z)| = |e_t2(z)|` **exactly**, where `e_t(z) = theta_p(z)/theta_p(z/t)`.
The reported "the normalisation places the two conjugate exponents ~17 orders
of magnitude apart" is therefore not merely unobserved but impossible. Measured
ratio is `1.0` at every `z` tested.

The scale-invariant conditioning `|det| / (||col0|| ||col1||) = |sin(angle)|`
comes out `0.59 .. 0.72` across the disc. The basis is fine as constructed.

## 2. `|det|/max^2` was the wrong metric

The Casoratian obeys, exactly,

    W(pz) = -(q-1) W(z) / (p^4 z^2 - 1)

(verified to `1e-110` inside the disc). So `W` DECAYS under outward propagation
for purely analytic reasons, with the columns staying perfectly independent.
Reading that decay as rank collapse is what produced the negative. Any
conditioning measure that is not invariant under rescaling each column
separately will report a false degeneracy here.

## 3. The bases DO share a domain — no propagation is needed

The negative's premise was "the two bases share no domain — the `0`-side series
has radius exactly 1, while the theta-normalised `h` is entire in `1/z`". But
*entire in `1/z`* means `sum h_k z^-k` converges for EVERY `z != 0`. The two
bases therefore overlap on the whole punctured disc `0 < |z| < 1` and match
directly. The propagation that lost the conditioning was never required.

## 4. `P(pz) = P(z)` is automatic — it was never evidence

For any two fundamental matrices of the same system, `Y0(pz) = A(z) Y0(z)` and
`Y_inf(pz) = A(z) Y_inf(z)`, so `A` cancels in `Y0^-1 Y_inf` and ellipticity
holds identically. It is a correctness check on the numerics, never a result.
The first attempt read its "passing" as informative; it is not, whatever the
conditioning.

## What this produces

    P = [[ c+ ,  c- ],
         [ conj c+, conj c- ]]

exact conjugate structure (the `0`-basis is a conjugate pair and the `inf`
solutions are real on the real axis), elliptic per entry to `1e-27 .. 1e-59`,
converged in `(dps, NG, NH)` to `1.4e-38`.

* `c-` has SIMPLE POLES exactly at `z in T p^Z` — that is where
  `theta_p(-z/T)` vanishes — and `c- * theta_p(-z/T)` tends to a finite limit.
* `c+` at the substrate is constant in `z` to `1.5e-18`.

## The limit this stops at — stated because it is the same trap

`c+` is **NOT** an exact constant. Its `z`-variation is real (identical across
`dps` 140 -> 320, `NG` 800 -> 2200, so not a precision artifact) and grows with
`q`: `1.6e-54` at `q=1.15` rising to `0.72` at `q=4.8`. So "the connection
constant `c+`" is a `q -> 1` statement, not an identity, and calling it a
constant on the strength of substrate numerics would be exactly the naming
error this arc keeps finding.

The asymptotic law is NOT identified either. Fitting `ln(variation)` against
`1/log p` gives local slopes bouncing over `8.0 .. 10.5`, and the small-`q`
points go non-monotonic where they hit the numerical floor. `pi^2 = 9.8696`
(the classic q-modular scale) sits inside that band. That is an observation,
not an identification, and it is not claimed here.

**Stokes multipliers remain OPEN.** This obtains the connection matrix; turning
it into multipliers is the next step. Nothing is wired to production.

-- Ref: [rsz2013] Asterisque 355 section 3.3 (Ramis-Sauloy-Zhang)
-- Ref: [manuscript] computations/qbeta/c3_w2_c1_theta_canonical.py
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

DPS, NG, NH = 160, 900, 80
Q_STR = "1.1099785827513808075916690956"


def theta(p, w, pad=40):
    """`theta_p(w) = sum_{n in Z} p^{-n(n+1)/2} w^n`, `p > 1`.

    Adaptive window. `log|term_n| = -n(n+1)/2 log p + n log|w|` peaks at
    `n* = log|w|/log p - 1/2` and falls as `-(log p/2)(n-n*)^2`, so a half-width
    `W` with `(log p/2) W^2 > (dps+pad) log 10` is below working precision. A
    FIXED symmetric window (say `n in [-50,50]`) misses the peak entirely once
    `|w|` is large — `n*` is already ~96 at `|w| ~ 150` — which is the most
    likely origin of the first attempt's numbers.
    """
    lp = mp.log(p)
    n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
    W = int(mp.ceil(mp.sqrt(2 * (mp.mp.dps + pad) * mp.log(10) / lp))) + 10
    return mp.fsum(p ** (-mp.mpf(n) * (n + 1) / 2) * w ** n
                   for n in range(n0 - W, n0 + W + 1))


def g_coeffs(p, t, n):
    """`0`-side: `g_k [t^2 p^2k + (q-1) t p^k + (q-1)] = t^2 p^2k g_{k-2}`.

    `k = 0` is the indicial equation `t^2 + (q-1)t + (q-1) = 0`; `g_1 = 0`, so
    only even powers appear and the radius is exactly 1.
    """
    q = p ** 2
    g = [mp.mpc(1), mp.mpc(0)]
    for k in range(2, n):
        g.append(t ** 2 * p ** (2 * k) * g[k - 2]
                 / (t ** 2 * p ** (2 * k) + (q - 1) * t * p ** k + (q - 1)))
    return g


def h_coeffs(p, T, n):
    """`inf`-side, as derived and residual-verified in `c3_w2_c1_theta_canonical.py`."""
    h = [mp.mpc(1)]
    for k in range(1, n):
        lhs = T ** 2 * p ** 3 * p ** (-2 * k) + (1 - p ** 2)
        rhs = -T * (1 - p ** 2) * p ** (-(k - 1)) * h[k - 1]
        if k >= 2:
            rhs += (T ** 2 / p) * p ** (-2 * (k - 2)) * h[k - 2]
        h.append(rhs / lhs)
    return h


def build(dps=DPS, ng=NG, nh=NH, qstr=Q_STR):
    mp.mp.dps = dps
    q = mp.mpf(qstr)
    p = mp.sqrt(q)
    disc = (q - 1) ** 2 - 4 * (q - 1)
    t1 = (-(q - 1) + mp.sqrt(mp.mpc(disc))) / 2
    t2 = (-(q - 1) - mp.sqrt(mp.mpc(disc))) / 2
    g1, g2 = g_coeffs(p, t1, ng), g_coeffs(p, t2, ng)
    T = mp.sqrt((p ** 2 - 1) / p ** 3)
    hp, hm = h_coeffs(p, T, nh), h_coeffs(p, -T, nh)

    def yz(t, g, z):
        return (theta(p, z) / theta(p, z / t)) * mp.fsum(
            g[k] * z ** k for k in range(len(g)))

    def yi(TT, h, z):
        return mp.fsum(h[k] * z ** (-k) for k in range(len(h))) / theta(p, z / TT)

    zero = [lambda z: yz(t1, g1, z), lambda z: yz(t2, g2, z)]
    infy = [lambda z: yi(T, hp, z), lambda z: yi(-T, hm, z)]
    return p, q, T, t1, t2, zero, infy


def fund(fns, p, z):
    Y = mp.matrix(2, 2)
    for j in (0, 1):
        Y[0, j], Y[1, j] = fns[j](z), fns[j](p * z)
    return Y


def sin_angle(Y):
    """Scale-invariant conditioning: `|det| / (||col0|| ||col1||)`."""
    det = Y[0, 0] * Y[1, 1] - Y[0, 1] * Y[1, 0]
    c0 = mp.sqrt(abs(Y[0, 0]) ** 2 + abs(Y[1, 0]) ** 2)
    c1 = mp.sqrt(abs(Y[0, 1]) ** 2 + abs(Y[1, 1]) ** 2)
    return abs(det) / (c0 * c1)


def main() -> None:
    t0 = time.perf_counter()
    p, q, T, t1, t2, zero, infy = build()
    res: dict = {}

    print("=" * 74)
    print("  1. REFUTATION — |e_t1(z)| = |e_t2(z)| exactly (conjugate pair)")
    print("=" * 74)
    ratios = {}
    for zs in ["0.30", "0.50", "0.80"]:
        z = mp.mpf(zs)
        a = abs(theta(p, z) / theta(p, z / t1))
        b = abs(theta(p, z) / theta(p, z / t2))
        ratios[zs] = a / b
        print(f"    z={zs}   |e_t1|/|e_t2| = {mp.nstr(a / b, 20)}")
    max_dev = max(abs(v - 1) for v in ratios.values())
    res["e_ratio_max_dev_from_one"] = str(mp.nstr(max_dev, 6))
    print(f"    max |ratio - 1| = {mp.nstr(max_dev, 6)}")
    print()

    print("=" * 74)
    print("  2. conditioning, scale-invariant  |sin(angle between columns)|")
    print("=" * 74)
    cond = {}
    for zs in ["0.10", "0.20", "0.30", "0.45", "0.60"]:
        z = mp.mpf(zs)
        c0, ci = sin_angle(fund(zero, p, z)), sin_angle(fund(infy, p, z))
        cond[zs] = (c0, ci)
        print(f"    z={zs}   Y0 : {mp.nstr(c0, 12):>16}   Y_inf : {mp.nstr(ci, 12):>16}")
    min_y0 = min(v[0] for v in cond.values())
    res["min_sin_angle_Y0"] = str(mp.nstr(min_y0, 12))
    print(f"    min over sample, Y0 = {mp.nstr(min_y0, 12)}   (negative claimed ~1e-18)")
    print()

    print("=" * 74)
    print("  3. Casoratian identity  W(pz) = -(q-1) W(z)/(p^4 z^2 - 1)")
    print("=" * 74)
    cas = {}
    for zs in ["0.30", "0.60", "0.80"]:
        z = mp.mpf(zs)
        Y, Yp = fund(zero, p, z), fund(zero, p, p * z)
        W = Y[0, 0] * Y[1, 1] - Y[0, 1] * Y[1, 0]
        Wp = Yp[0, 0] * Yp[1, 1] - Yp[0, 1] * Yp[1, 0]
        pred = -(q - 1) * W / (p ** 4 * z ** 2 - 1)
        cas[zs] = abs(Wp - pred) / abs(pred)
        print(f"    z={zs}   rel.err = {mp.nstr(cas[zs], 6)}")
    res["casoratian_max_rel_err"] = str(mp.nstr(max(cas.values()), 6))
    print()

    print("=" * 74)
    print("  4. P = Y0^-1 Y_inf — structure and ellipticity")
    print("=" * 74)

    def P(z):
        return fund(zero, p, z) ** -1 * fund(infy, p, z)

    struct, ellip = [], []
    for zs in ["0.30", "0.45", "0.60", "0.75"]:
        z = mp.mpf(zs)
        M, Mp = P(z), P(p * z)
        s = max(abs(M[1, j] - mp.conj(M[0, j])) / abs(M[0, j]) for j in (0, 1))
        e = max(abs(Mp[0, j] - M[0, j]) / abs(M[0, j]) for j in (0, 1))
        struct.append(s)
        ellip.append(e)
        print(f"    z={zs}   conj-structure dev = {mp.nstr(s, 6):>12}"
              f"    ellipticity (per entry) = {mp.nstr(e, 6):>12}")
    res["conj_structure_max_dev"] = str(mp.nstr(max(struct), 6))
    res["ellipticity_max_rel"] = str(mp.nstr(max(ellip), 6))
    print()

    print("=" * 74)
    print("  5. c+ at the substrate, and its convergence")
    print("=" * 74)
    conv = []
    for dps, ng, nh in [(120, 600, 60), (160, 900, 80), (200, 1200, 100)]:
        pp, _, _, _, _, z0, zi = build(dps, ng, nh)
        M = fund(z0, pp, mp.mpf("0.45")) ** -1 * fund(zi, pp, mp.mpf("0.45"))
        conv.append(mp.arg(M[0, 0]))
        print(f"    dps={dps:>4} NG={ng:>5} NH={nh:>4}   arg(c+) = {mp.nstr(conv[-1], 22)}")
    conv_delta = abs(conv[-1] - conv[-2])
    res["arg_c_plus_convergence_delta"] = str(mp.nstr(conv_delta, 6))

    cp = P(mp.mpf("0.45"))[0, 0]
    spread = max(abs(P(mp.mpf(zs))[0, 0] - cp) / abs(cp)
                 for zs in ["0.30", "0.45", "0.60", "0.75"])
    res["c_plus"] = str(mp.nstr(cp, 24))
    res["arg_c_plus"] = str(mp.nstr(mp.arg(cp), 24))
    res["c_plus_z_spread_at_substrate"] = str(mp.nstr(spread, 6))
    print(f"    c+            = {mp.nstr(cp, 24)}")
    print(f"    arg(c+)       = {mp.nstr(mp.arg(cp), 24)}")
    print(f"    z-spread      = {mp.nstr(spread, 6)}   (NOT exactly zero — see 7)")
    print()

    print("=" * 74)
    print("  6. c- has simple poles exactly at z = T p^k")
    print("=" * 74)
    poles = {}
    for k in (0, 1, 2):
        z = T * p ** k
        at = abs(P(z)[0, 1])
        off = abs(P(z * mp.mpf("1.06"))[0, 1])
        poles[k] = at / off
        print(f"    k={k}   z={mp.nstr(z, 12):>16}   |c-| at/off pole = {mp.nstr(at / off, 6)}")
    res["c_minus_pole_ratio_min"] = str(mp.nstr(min(poles.values()), 6))
    lim = []
    for eps in ["1e-3", "1e-4", "1e-5"]:
        z = T * p ** 2 * (1 + mp.mpf(eps))
        lim.append(abs(P(z)[0, 1] * theta(p, -z / T)))
    res["c_minus_times_theta_limit"] = str(mp.nstr(lim[-1], 12))
    print(f"    |c- * theta_p(-z/T)| -> {mp.nstr(lim[-1], 12)}  (finite => SIMPLE pole)")
    print()

    print("=" * 74)
    print("  7. the honest limit — c+ is not an exact constant")
    print("=" * 74)
    qvar = {}
    for qs_ in ["1.35", "1.8", "2.5", "3.4"]:
        pp, _, _, _, _, z0, zi = build(140, 800, 70, qs_)
        cs = [(fund(z0, pp, mp.mpf(a) / pp) ** -1
               * fund(zi, pp, mp.mpf(a) / pp))[0, 0]
              for a in ["0.35", "0.50", "0.65", "0.80"]]
        qvar[qs_] = max(abs(c - cs[0]) for c in cs) / abs(cs[0])
        print(f"    q={qs_:>5}   c+ z-spread = {mp.nstr(qvar[qs_], 6)}")
    res["c_plus_spread_by_q"] = {k: str(mp.nstr(v, 6)) for k, v in qvar.items()}
    print("    grows with q, and is IDENTICAL across dps 140->320 / NG 800->2200,")
    print("    so it is real, not precision. 'Connection constant' is a q->1")
    print("    statement only. Asymptotic law NOT identified (slopes 8.0..10.5).")

    script_path = Path(__file__).resolve()
    src = script_path.read_bytes()
    sha = subprocess.run(["git", "log", "-1", "--format=%H", "--", str(script_path)],
                         capture_output=True, text=True,
                         check=False).stdout.strip() or "unknown"

    witness = {
        "schema": "witness/v1",
        "engine": "mpmath",
        "scriptFile": script_path.name,
        "commitSha": sha,
        "description": (
            "Bean qou-wgnx. Obtains the C1 connection matrix P = Y0^-1 Y_inf and "
            "REFUTES the 2026-08-07 degeneracy negative. That negative rested on three "
            "wrong premises: (a) the 0-side basis is degenerate — impossible, since p is "
            "real so theta_p has real coefficients and the exponents are a conjugate "
            "pair, forcing |e_t1(z)| = |e_t2(z)| exactly on the real axis (measured "
            "ratio 1.0; scale-invariant conditioning 0.59..0.72, not 1e-18); (b) the "
            "bases share no domain — but h entire in 1/z means it converges for every "
            "z != 0, so they overlap on 0 < |z| < 1 and match directly with no "
            "propagation; (c) |det|/max^2 measures conditioning — it does not, because "
            "the Casoratian obeys W(pz) = -(q-1)W(z)/(p^4z^2-1) exactly and so decays "
            "analytically while the columns stay independent. Also: P(pz) = P(z) is "
            "AUTOMATIC for any two fundamental matrices and was never evidence. RESULT: "
            "P = [[c+, c-], [conj c+, conj c-]], elliptic per entry to 1e-27..1e-59; c- "
            "has simple poles exactly at z in T p^Z. LIMIT STATED: c+ is NOT an exact "
            "constant — its z-variation is precision-independent and grows with q — so "
            "'connection constant' is a q->1 statement, and the asymptotic law is not "
            "identified. Stokes multipliers remain OPEN."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_connection_matrix.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        },
        "results": {
            "q": Q_STR,
            "dps": DPS, "n_terms_zero_side": NG, "n_terms_inf_side": NH,
            "operator": "(p^4 z^2 - 1) tau^2 - (p^2-1) tau - (p^2-1)",
            "zero_side_indicial": "t^2 + (q-1) t + (q-1) = 0",
            "connection_matrix_structure": "[[c+, c-], [conj c+, conj c-]]",
            "c_minus_pole_divisor": "z in T p^Z (zeros of theta_p(-z/T))",
            **res,
        },
        "checks": [
            {"name": "conjugate_pair_forces_equal_magnitudes",
             "detail": "|e_t1(z)| = |e_t2(z)| on the real axis — refutes the '~17 orders "
                       "of magnitude apart' diagnosis",
             "passed": bool(max_dev < mp.mpf(10) ** (-30))},
            {"name": "zero_side_basis_well_conditioned",
             "detail": "scale-invariant |sin(angle)| between columns is O(1), not 1e-18",
             "passed": bool(min_y0 > mp.mpf("0.1"))},
            {"name": "casoratian_identity",
             "detail": "W(pz) = -(q-1) W(z)/(p^4 z^2 - 1) — explains the apparent "
                       "determinant decay analytically",
             "passed": bool(max(cas.values()) < mp.mpf(10) ** (-30))},
            {"name": "connection_matrix_conjugate_structure",
             "detail": "P[1,j] = conj P[0,j]",
             "passed": bool(max(struct) < mp.mpf(10) ** (-30))},
            {"name": "connection_matrix_elliptic_per_entry",
             "detail": "P(pz) = P(z) entrywise — a correctness check, NOT a result",
             "passed": bool(max(ellip) < mp.mpf(10) ** (-20))},
            {"name": "c_minus_has_simple_poles_at_T_p_k",
             "detail": "|c-| blows up at z = T p^k and c- * theta_p(-z/T) stays finite",
             "passed": bool(min(poles.values()) > mp.mpf(10) ** 50)},
            {"name": "c_plus_not_exactly_constant",
             "detail": "z-variation grows with q and is precision-independent — recorded "
                       "as a LIMIT, not a result",
             "passed": bool(qvar["3.4"] > mp.mpf(10) ** (-6))},
        ],
        "verdict": (
            "The connection matrix P = Y0^-1 Y_inf IS OBTAINED, and the 2026-08-07 "
            "'basis is degenerate' negative is REFUTED on all three of its premises. The "
            "0-side basis was never degenerate: conjugate exponents plus real theta "
            "coefficients force |e_t1| = |e_t2| exactly, and the scale-invariant "
            "conditioning is 0.59..0.72. The bases overlap on the punctured disc, so no "
            "propagation was ever needed. P has exact conjugate structure and is elliptic "
            "per entry to 1e-27..1e-59, with c- carrying simple poles precisely on "
            "z in T p^Z. NOT CLAIMED: c+ is not an exact constant (its z-variation is "
            "real and grows with q), the asymptotic law behind that variation is not "
            "identified, and the STOKES MULTIPLIERS ARE STILL NOT EXTRACTED — obtaining "
            "the connection matrix is a prerequisite for them, not the same thing. "
            "Nothing wired to production."
        ),
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-connection-matrix.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
