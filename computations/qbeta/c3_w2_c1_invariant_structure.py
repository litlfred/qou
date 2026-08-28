#!/usr/bin/env python3
"""Structure of the invariant `chi` off the real axis — and a PRECISION WARNING.

Bean `qou-wgnx`, follow-on to `c3_w2_c1_connection_invariant.py`, which
established `chi = P00 P11/(P01 P10)` and characterised it ON THE REAL AXIS.
This examines it off-axis, corrects one reading of the earlier result, and
records the settings needed to do so.

## PRECISION WARNING — read before extending any of these scripts off-axis

The sibling scripts run at `DPS=120, NG=500, NH=60`, which is ample on the real
axis but **NOT** off it. The `inf`-side truncation error is
`|h_k z^-k| ~ |T/z|^k p^{-k(k-1)/2}`, about `1e-48` at `|z| = 0.42, k = 60` —
the same size as the quantities being measured there. At those settings a scan
of `chi` at `z = 0.42i` returns `log10|chi| = -45.8`; the converged value is
**-73.4468**. The first number is pure truncation noise.

Diagnostic that catches it: `P(pz) = P(z)` is an ALGEBRAIC identity (both `Y0`
and `Y_inf` satisfy `Y(pz) = A(z)Y(z)`, so `A` cancels), so any measured
deviation is numerical error and nothing else. At `DPS=120/NH=60` that
deviation is `1.1` at `z = 0.42i` — i.e. no signal at all. At
`DPS=200, NG=800, NH=110` it is `7e-66`, and at `DPS=400/NH=230`, `3e-329`.
**Always check entrywise ellipticity of `P` before believing an off-axis
number.**

## The reflection law — why `|chi| = 1` on the real axis is not deep

The operator has real coefficients, so conjugation swaps the two `0`-side
solutions (they are a conjugate pair) while fixing the `inf`-side ones (real).
That swaps `P`'s rows, giving

    chi(conj z) = 1 / conj(chi(z))        (verified to 1e-167)

On the real axis `z = conj z`, so `|chi|^2 = 1` — **automatic**. The earlier
report of `|chi| = 1` there is therefore a consequence of this symmetry, not
independent information about the connection. What the real axis does carry is
`arg chi = 2(arg c+ - arg c-)`.

## What `chi` looks like off the axis

* `|chi|` is essentially independent of `|z|`: constant to ~10 digits across a
  full `p`-period along `arg z = pi/2`.
* `log|chi|` is **exactly linear in `arg z`** out to `arg/pi ~ 0.4`, with slope
  `-52.3047` per radian. That equals `-2 pi / (log p * ln 10)` to all printed
  digits — i.e. `chi` behaves like `z^(i * 2 pi / log p)` in that sector. (It
  cannot BE that: `z^(i lambda)` is not single-valued on `C*`.)
* It then **saturates** at `-73.4468`, with the bend beginning near
  `arg/pi = 0.447`. That is `arg(-t2)/pi = 0.446975` — a `0`-side exponent
  direction.

Power-like behaviour in sectors, switching across rays fixed by the exponents,
is the signature of a **theta quotient**: which term dominates the theta series
changes across those rays. So `chi` is presumably a ratio of `theta_p`'s in the
exponents and `T`.

**NOT determined here: chi's divisor, hence not its closed form.** An elliptic
function is fixed by its divisor up to a constant, so that is what a closed form
needs, and the sector data above constrains but does not supply it. Stokes
multipliers remain OPEN.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_connection_invariant.py
-- Ref: [rsz2013] Asterisque 355 section 3.3 (Ramis-Sauloy-Zhang)
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

DPS, NG, NH = 200, 800, 110
Q_STR = "1.1099785827513808075916690956"


def theta(p, w, pad=40):
    lp = mp.log(p)
    n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
    W = int(mp.ceil(mp.sqrt(2 * (mp.mp.dps + pad) * mp.log(10) / lp))) + 10
    return mp.fsum(p ** (-mp.mpf(n) * (n + 1) / 2) * w ** n
                   for n in range(n0 - W, n0 + W + 1))


def build(dps=DPS, ng=NG, nh=NH):
    mp.mp.dps = dps
    q = mp.mpf(Q_STR)
    p = mp.sqrt(q)
    disc = (q - 1) ** 2 - 4 * (q - 1)
    t1 = (-(q - 1) + mp.sqrt(mp.mpc(disc))) / 2
    t2 = (-(q - 1) - mp.sqrt(mp.mpc(disc))) / 2

    def gc(t):
        g = [mp.mpc(1), mp.mpc(0)]
        for k in range(2, ng):
            g.append(t ** 2 * p ** (2 * k) * g[k - 2]
                     / (t ** 2 * p ** (2 * k) + (q - 1) * t * p ** k + (q - 1)))
        return g

    T = mp.sqrt((p ** 2 - 1) / p ** 3)

    def hc(TT):
        h = [mp.mpc(1)]
        for k in range(1, nh):
            lhs = TT ** 2 * p ** 3 * p ** (-2 * k) + (1 - p ** 2)
            rhs = -TT * (1 - p ** 2) * p ** (-(k - 1)) * h[k - 1]
            if k >= 2:
                rhs += (TT ** 2 / p) * p ** (-2 * (k - 2)) * h[k - 2]
            h.append(rhs / lhs)
        return h

    g1, g2, hp, hm = gc(t1), gc(t2), hc(T), hc(-T)

    def yz(t, g, z):
        return (theta(p, z) / theta(p, z / t)) * mp.fsum(
            g[k] * z ** k for k in range(len(g)))

    def yi(TT, h, z):
        return mp.fsum(h[k] * z ** (-k) for k in range(len(h))) / theta(p, z / TT)

    return (p, q, T, t1, t2,
            [lambda z: yz(t1, g1, z), lambda z: yz(t2, g2, z)],
            [lambda z: yi(T, hp, z), lambda z: yi(-T, hm, z)])


def main() -> None:
    t0 = time.perf_counter()
    p, q, T, t1, t2, zero, infy = build()
    res: dict = {}

    def Pm(zero, infy, pp, z):
        Y0, Yi = mp.matrix(2, 2), mp.matrix(2, 2)
        for j in (0, 1):
            Y0[0, j], Y0[1, j] = zero[j](z), zero[j](pp * z)
            Yi[0, j], Yi[1, j] = infy[j](z), infy[j](pp * z)
        return Y0 ** -1 * Yi

    def chi(z):
        M = Pm(zero, infy, p, z)
        return M[0, 0] * M[1, 1] / (M[0, 1] * M[1, 0])

    zc = mp.mpf("0.42") * mp.expjpi(mp.mpf(1) / 2)

    print("=" * 74)
    print("  1. PRECISION WARNING — the same point at several settings")
    print("=" * 74)
    print(f"  {'dps':>5} {'NG':>6} {'NH':>5}   {'P ellipticity dev':>20}  {'log10|chi|':>16}")
    conv = []
    for dps, ng, nh in [(120, 500, 60), (200, 800, 110), (300, 1200, 170)]:
        pp, _, _, _, _, z0, zi = build(dps, ng, nh)
        A, B = Pm(z0, zi, pp, zc), Pm(z0, zi, pp, pp * zc)
        dev = max(abs(B[i, j] - A[i, j]) / abs(A[i, j])
                  for i in range(2) for j in range(2))
        val = mp.log10(abs(A[0, 0] * A[1, 1] / (A[0, 1] * A[1, 0])))
        conv.append((dev, val))
        print(f"  {dps:>5} {ng:>6} {nh:>5}   {mp.nstr(dev, 6):>20}  {mp.nstr(val, 12):>16}")
    res["coarse_setting_ellipticity_dev"] = str(mp.nstr(conv[0][0], 6))
    res["coarse_setting_log10_chi"] = str(mp.nstr(conv[0][1], 12))
    res["converged_log10_chi"] = str(mp.nstr(conv[-1][1], 12))
    print("  -> the coarse row has NO signal; its value is truncation noise.")
    print()

    print("=" * 74)
    print("  2. reflection law   chi(conj z) = 1 / conj(chi(z))")
    print("=" * 74)
    refl = []
    for zs, ang in [("0.42", "0.5"), ("0.38", "0.3"), ("0.45", "0.8")]:
        z = mp.mpf(zs) * mp.expjpi(mp.mpf(ang))
        d = abs(chi(mp.conj(z)) - 1 / mp.conj(chi(z))) / abs(1 / mp.conj(chi(z)))
        refl.append(d)
        print(f"    |z|={zs} arg/pi={ang}   rel.dev = {mp.nstr(d, 6)}")
    res["reflection_law_max_dev"] = str(mp.nstr(max(refl), 6))
    print("    => |chi| = 1 on the real axis is AUTOMATIC, not independent data.")
    print()

    print("=" * 74)
    print("  3. |chi| is |z|-independent, and log|chi| is linear in arg z")
    print("=" * 74)
    rad = [mp.log10(abs(chi(mp.mpf("0.40") * p ** (mp.mpf(i) / 6)
                              * mp.expjpi(mp.mpf(1) / 2)))) for i in range(7)]
    res["radial_spread_at_arg_pi_over_2"] = str(mp.nstr(max(rad) - min(rad), 6))
    print(f"    spread of log10|chi| over one p-period at arg=pi/2 : "
          f"{mp.nstr(max(rad) - min(rad), 6)}")
    slope = None
    print(f"    {'arg/pi':>8}  {'log10|chi|':>18}  {'/linear':>10}")
    for a_s in ["0.0625", "0.125", "0.25", "0.375", "0.44", "0.47", "0.5"]:
        a = mp.mpf(a_s)
        v = mp.log10(abs(chi(mp.mpf("0.41") * mp.expjpi(a))))
        if slope is None:
            slope = v / a
        print(f"    {a_s:>8}  {mp.nstr(v, 14):>18}  {mp.nstr(v / (slope * a), 8):>10}")
    per_rad = slope / mp.pi
    pred = -2 * mp.pi / (mp.log(p) * mp.log(10))
    res["slope_per_radian"] = str(mp.nstr(per_rad, 12))
    res["predicted_slope_z_pow_i_2pi_over_logp"] = str(mp.nstr(pred, 12))
    print(f"\n    slope per radian                = {mp.nstr(per_rad, 12)}")
    print(f"    -2 pi/(log p ln 10)             = {mp.nstr(pred, 12)}")
    print(f"    rel. difference                 = {mp.nstr(abs(per_rad - pred)/abs(pred), 6)}")
    print(f"    saturation bend near arg/pi     ~ 0.447")
    print(f"    arg(-t2)/pi                     = {mp.nstr(mp.arg(-t2)/mp.pi, 12)}")
    res["arg_minus_t2_over_pi"] = str(mp.nstr(mp.arg(-t2) / mp.pi, 12))
    res["slope_rel_diff"] = str(mp.nstr(abs(per_rad - pred) / abs(pred), 6))

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
            "Bean qou-wgnx. Off-axis structure of the connection invariant chi, plus a "
            "PRECISION WARNING for the sibling scripts. (1) At DPS=120/NG=500/NH=60 — the "
            "settings of c3_w2_c1_connection_invariant.py, ample on the real axis — an "
            "off-axis evaluation at z = 0.42i has entrywise P-ellipticity deviation ~1.1, "
            "i.e. NO signal, and reports log10|chi| = -45.8 where the converged value is "
            "-73.4468. Since P(pz) = P(z) is an algebraic identity, that deviation is a "
            "pure error meter and must be checked before believing any off-axis number. "
            "(2) REFLECTION LAW chi(conj z) = 1/conj(chi(z)), verified to 1e-167, because "
            "the real-coefficient operator makes conjugation swap the two 0-side solutions "
            "and hence P's rows. Consequently |chi| = 1 on the real axis is AUTOMATIC, not "
            "independent connection data — a correction to how the earlier result reads. "
            "(3) Off-axis, |chi| is independent of |z| to ~10 digits and log|chi| is "
            "exactly linear in arg z with slope -2 pi/(log p ln 10), i.e. chi behaves like "
            "z^(i 2 pi/log p) in a sector, then SATURATES with the bend near arg/pi = "
            "0.447 = arg(-t2)/pi, a 0-side exponent direction. Sector-wise power behaviour "
            "switching across exponent rays is the signature of a theta quotient. NOT "
            "DETERMINED: chi's divisor, hence not its closed form. Stokes multipliers "
            "remain OPEN."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_invariant_structure.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        },
        "results": {
            "q": Q_STR, "dps": DPS, "NG": NG, "NH": NH,
            "reflection_law": "chi(conj z) = 1 / conj(chi(z))",
            "consequence": "|chi| = 1 on the real axis is automatic",
            "off_axis_behaviour": "z^(i 2 pi / log p) in a sector, saturating near arg(-t2)",
            "divisor_determined": False,
            **res,
        },
        "checks": [
            {"name": "coarse_settings_have_no_off_axis_signal",
             "detail": "entrywise P-ellipticity deviation is O(1) at DPS=120/NH=60, so the "
                       "off-axis value there is noise",
             "passed": bool(conv[0][0] > mp.mpf("0.01"))},
            {"name": "converged_settings_are_elliptic",
             "detail": "P(pz) = P(z) entrywise at DPS>=200",
             "passed": bool(conv[1][0] < mp.mpf(10) ** (-40))},
            {"name": "reflection_law",
             "detail": "chi(conj z) = 1/conj(chi(z))",
             "passed": bool(max(refl) < mp.mpf(10) ** (-100))},
            {"name": "log_abs_chi_slope_matches_two_pi_over_log_p",
             "detail": "slope per radian equals -2 pi/(log p ln 10)",
             "passed": bool(abs(per_rad - pred) / abs(pred) < mp.mpf(10) ** (-8))},
        ],
        "verdict": (
            "Off the real axis chi behaves like z^(i 2 pi/log p) in a sector — log|chi| "
            "linear in arg z with slope matching -2 pi/(log p ln 10) exactly, and |z|-"
            "independent — then saturates, the bend sitting at arg(-t2), a 0-side exponent "
            "direction. Sector-wise power behaviour switching across exponent rays is the "
            "signature of a theta quotient, so chi is presumably a ratio of theta_p's in "
            "the exponents and T. TWO CORRECTIONS TO EARLIER READINGS: |chi| = 1 on the "
            "real axis follows from the reflection law chi(conj z) = 1/conj(chi(z)) and is "
            "not independent data; and the sibling scripts' settings, though ample on the "
            "real axis, carry NO off-axis signal — always check entrywise P-ellipticity "
            "first, since P(pz) = P(z) is an algebraic identity and therefore a pure error "
            "meter. NOT DETERMINED: chi's divisor, hence not its closed form; an elliptic "
            "function is fixed by its divisor up to a constant and the sector data "
            "constrains but does not supply it. Stokes multipliers remain OPEN."
        ),
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-invariant-structure.witness.json"
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
