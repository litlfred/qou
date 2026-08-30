#!/usr/bin/env python3
"""The C1 connection matrix's POLE DIVISOR — symbolic, and residue-verified.

Bean `qou-wgnx`, follow-on to `c3_w2_c1_connection_matrix.py`. That script
obtained `P = Y0^-1 Y_inf` and left one thing dangling: `c+` looked constant on
the positive real axis but provably was not, with the deviation growing with
`q` and its law unidentified. This script resolves that, and pins the divisor.

## The divisor is symbolic — nothing here is fitted

Every pole of `P` sits where some `theta_p` in the construction vanishes, and
the zero set of `theta_p` is a single `p`-orbit:

    theta_p(w) = 0   <=>   w in -p^Z

(the `>=` direction is proved in Lean, `QOU/QBeta/C1ConnectionPoles.lean`,
sorry-free, by an involution `n -> 2k-1-n` that fixes the exponent and flips
the sign; the converse is the Jacobi triple product and is NOT proved).

So, with `T = sqrt((p^2-1)/p^3) = sqrt(q-1)/q^(3/4)`:

  | pole on C*/p^Z | locus       | source                              | intrinsic? |
  |----------------|-------------|-------------------------------------|-----------|
  | [-1]           | z in -p^Z   | theta_p(z), the COMMON numerator of |  NO       |
  |                |             | e_t(z) = theta_p(z)/theta_p(z/t)    |           |
  | [-T]           | z in -T p^Z | theta_p(z/T_+)                      |  yes      |
  | [+T]           | z in +T p^Z | theta_p(-z/T)                       |  yes      |

`[-1]` enters through the `0`-side character's common numerator, so it sits in
BOTH columns and is an artifact of how the `0`-side basis was normalised — not
connection data. `[+-T]` are tied to the actual `inf`-side exponents.

## Why this resolves the `c+` puzzle

`c+`'s poles are `[-1]` and `[-T]`, **both on the negative real ray**. The
positive real axis — the only place the earlier script sampled — is maximally
far from them on the torus, so `c+` is flat there to `1e-27` and the residual
wobble is just the tail of those poles. As `q` grows the torus gets shorter and
the tail grows, which is exactly the measured `3.1e-23 -> 0.72` trend.

**The `pi^2` observation is therefore retired.** It was offered as "sits in the
band 8.0..10.5, not identified"; with the mechanism in hand there is no need to
posit a modular constant at all, and no evidence for one.

## The residue theorem confirms the divisor is COMPLETE

On `C*/p^Z` the invariant differential is `dz/z`, so `sum_i Res_{z_i}(f dz/z)`
must vanish. For a simple pole, `Res(f dz/z) = A/z0` with
`A = lim (z-z0) f(z)`, i.e. `A/z0 = eps * f(z0(1+eps))` as `eps -> 0`.

An elliptic function cannot have a single simple pole per fundamental domain,
so finding only one would have PROVED a pole was still missing. Finding two
whose residues cancel proves the divisor is complete.

-- Ref: [manuscript] computations/qbeta/c3_w2_c1_connection_matrix.py
-- Ref: [rsz2013] Asterisque 355 section 3.3 (Ramis-Sauloy-Zhang)
"""
from __future__ import annotations

# PATH BRIDGE — required before the provenance stamp can import
# `qou_substrate` (bean qou-ya1e). That module is not installed and not on
# PYTHONPATH; it is reachable only through `_path_bridge`, which
# `migrate_bare_producer_provenance.py` inserted the stamp WITHOUT. The
# import sits at function scope, so this producer did all its work and then
# died at the save with ModuleNotFoundError. Idiom copied verbatim from
# `qbeta/qbeta_c3_candidate_audit.py`.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

import hashlib
import json
import subprocess
import time
from pathlib import Path

import mpmath as mp

DPS, NG, NH = 130, 500, 60
Q_STR = "1.1099785827513808075916690956"


def theta(p, w, pad=30):
    """Adaptive-window q-theta; see c3_w2_c1_connection_matrix.py for why."""
    lp = mp.log(p)
    n0 = int(mp.nint(mp.log(abs(w)) / lp - mp.mpf(1) / 2))
    W = int(mp.ceil(mp.sqrt(2 * (mp.mp.dps + pad) * mp.log(10) / lp))) + 10
    return mp.fsum(p ** (-mp.mpf(n) * (n + 1) / 2) * w ** n
                   for n in range(n0 - W, n0 + W + 1))


def build():
    mp.mp.dps = DPS
    q = mp.mpf(Q_STR)
    p = mp.sqrt(q)
    disc = (q - 1) ** 2 - 4 * (q - 1)
    t1 = (-(q - 1) + mp.sqrt(mp.mpc(disc))) / 2
    t2 = (-(q - 1) - mp.sqrt(mp.mpc(disc))) / 2

    def gc(t):
        g = [mp.mpc(1), mp.mpc(0)]
        for k in range(2, NG):
            g.append(t ** 2 * p ** (2 * k) * g[k - 2]
                     / (t ** 2 * p ** (2 * k) + (q - 1) * t * p ** k + (q - 1)))
        return g

    T = mp.sqrt((p ** 2 - 1) / p ** 3)

    def hc(TT):
        h = [mp.mpc(1)]
        for k in range(1, NH):
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

    return (p, q, T,
            [lambda z: yz(t1, g1, z), lambda z: yz(t2, g2, z)],
            [lambda z: yi(T, hp, z), lambda z: yi(-T, hm, z)])


def main() -> None:
    t0 = time.perf_counter()
    p, q, T, zero, infy = build()
    res: dict = {}

    def ent(z, j):
        Y0, Yi = mp.matrix(2, 2), mp.matrix(2, 2)
        for k in (0, 1):
            Y0[0, k], Y0[1, k] = zero[k](z), zero[k](p * z)
            Yi[0, k], Yi[1, k] = infy[k](z), infy[k](p * z)
        return (Y0 ** -1 * Yi)[0, j]

    # one fundamental annulus holding all three poles
    z_m1, z_mT, z_pT = -p ** (-17), -(T * p ** 6), T * p ** 6
    ratio = abs(z_mT) / abs(z_m1)
    print("=" * 74)
    print("  1. the three poles, and that they share ONE fundamental domain")
    print("=" * 74)
    print(f"    [-1] -> z = {mp.nstr(z_m1, 14)}   (= -p^-17)")
    print(f"    [-T] -> z = {mp.nstr(z_mT, 14)}   (= -T p^6)")
    print(f"    [+T] -> z = {mp.nstr(z_pT, 14)}   (=  T p^6)")
    print(f"    radii ratio = {mp.nstr(ratio, 10)}  <  p = {mp.nstr(p, 10)}  -> same domain")
    res["pole_radii_ratio"] = str(mp.nstr(ratio, 10))
    res["T"] = str(mp.nstr(T, 20))
    print()

    print("=" * 74)
    print("  2. they really are poles — magnitude at vs. just off")
    print("=" * 74)
    blow = {}
    for lbl, z0, j in [("[-1] in c+", z_m1, 0), ("[-T] in c+", z_mT, 0),
                       ("[-1] in c-", z_m1, 1), ("[+T] in c-", z_pT, 1)]:
        at = abs(ent(z0 * (1 + mp.mpf("1e-9")), j))
        off = abs(ent(z0 * mp.mpf("1.04"), j))
        blow[lbl] = at / off
        print(f"    {lbl:>12}   |f| at/off = {mp.nstr(at / off, 8)}")
    res["min_pole_blowup"] = str(mp.nstr(min(blow.values()), 8))
    print()

    print("=" * 74)
    print("  3. RESIDUE THEOREM on C*/p^Z   —   sum_i Res(f dz/z) = 0")
    print("=" * 74)
    print("    Res(f dz/z) = A/z0 = eps * f(z0(1+eps)).  A leftover that falls")
    print("    LINEARLY in eps is the O(eps) truncation of the estimate, i.e. the")
    print("    exact sum is zero.")
    conv = {}
    for j, name, poles in [(0, "c+", [("[-1]", z_m1), ("[-T]", z_mT)]),
                           (1, "c-", [("[-1]", z_m1), ("[+T]", z_pT)])]:
        print(f"\n    {name}")
        ratios = []
        for eps_s in ["1e-6", "1e-7", "1e-8"]:
            eps = mp.mpf(eps_s)
            vals = [eps * ent(z0 * (1 + eps), j) for _, z0 in poles]
            tot = sum(vals)
            mx = max(abs(v) for v in vals)
            ratios.append(abs(tot) / mx)
            print(f"      eps={eps_s}   |sum|/max = {mp.nstr(abs(tot) / mx, 8)}")
        # linear decay => each 10x smaller eps gives 10x smaller leftover
        # `ratios` are mpf at the working precision; the decay factors were
        # float()-ed here and then round()-ed into the witness, so a 10x-linearity
        # check computed at 50 dps was published — and tested — at f64.
        decay = [ratios[i] / ratios[i + 1] for i in range(len(ratios) - 1)]
        conv[name] = decay
        print(f"      decay factors per 10x eps : "
              f"{[round(float(d), 3) for d in decay]}"
              f"   (10 = exactly linear)")
    res["residue_decay_factors"] = {k: [mp.nstr(x, 12) for x in v]
                                    for k, v in conv.items()}
    linear_ok = all(abs(d - 10) < 1 for v in conv.values() for d in v)
    print()

    print("=" * 74)
    print("  4. why c+ looked constant — both its poles are on the NEGATIVE ray")
    print("=" * 74)
    for zs in ["0.30", "0.45", "0.60", "0.75"]:
        z = mp.mpf(zs)
        print(f"    z=+{zs}   |c+| = {mp.nstr(abs(ent(z, 0)), 12)}")
    print(f"    z={mp.nstr(z_mT, 8)} (= -T p^6, a pole)   "
          f"|c+| = {mp.nstr(abs(ent(z_mT * (1 + mp.mpf('1e-9')), 0)), 8)}")
    print("    -> the positive axis is maximally far from [-1] and [-T] on the")
    print("       torus, so c+ is flat there. No modular constant needed; the")
    print("       earlier pi^2 observation is retired as unnecessary.")

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
            "Bean qou-wgnx. Pins the POLE DIVISOR of the C1 connection matrix and "
            "resolves the c+ near-constancy left open by c3_w2_c1_connection_matrix.py. "
            "The divisor is SYMBOLIC: every pole sits where a theta_p vanishes, and "
            "theta_p's zero set is the single p-orbit -p^Z. So c+ has simple poles at "
            "[-1] and [-T], c- at [-1] and [+T], with T = sqrt(q-1)/q^(3/4). [-1] comes "
            "from the COMMON numerator theta_p(z) of the 0-side character and therefore "
            "sits in both columns — a normalisation artifact, not connection data; "
            "[+-T] are tied to the inf-side exponents and are intrinsic. VERIFIED by the "
            "residue theorem on C*/p^Z: an elliptic function cannot have one simple pole "
            "per fundamental domain, and the two residues of each entry cancel with a "
            "leftover falling LINEARLY in eps (the O(eps) truncation of the limit "
            "estimate), so the divisor is complete. This also explains the c+ puzzle: "
            "both of its poles lie on the NEGATIVE real ray, which is why sampling only "
            "the positive axis made it look constant, and why the deviation grows with "
            "q. The pi^2 observation from the previous script is RETIRED as unnecessary."
        ),
        "computation": {
            "script": "computations/qbeta/c3_w2_c1_pole_divisor.py",
            "scriptCommitSha": sha,
            "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        },
        "results": {
            "q": Q_STR,
            "theta_zero_locus": "theta_p(w) = 0  <=>  w in -p^Z",
            "lean_partial_proof": "QOU/QBeta/C1ConnectionPoles.lean (>= direction, sorry-free)",
            "lean_not_proved": "converse (Jacobi triple product); that zeros are poles of P",
            "divisor_c_plus": "simple poles at [-1] and [-T]",
            "divisor_c_minus": "simple poles at [-1] and [+T]",
            "artifact_pole": "[-1] — common numerator theta_p(z) of the 0-side character",
            **res,
        },
        "checks": [
            {"name": "all_three_poles_in_one_fundamental_domain",
             "detail": "radii ratio < p, so the residue theorem applies to them together",
             "passed": bool(ratio < p)},          # mpf vs mpf, not mpf vs f64
            {"name": "poles_are_genuine",
             "detail": "|f| blows up at each candidate relative to just off it",
             "passed": bool(min(blow.values()) > mp.mpf(10) ** 6)},
            {"name": "residue_sum_vanishes_linearly",
             "detail": "leftover falls ~10x per 10x smaller eps => exact sum is zero => "
                       "divisor COMPLETE",
             "passed": bool(linear_ok)},
        ],
        "verdict": (
            "The pole divisor of the C1 connection matrix is SYMBOLIC and COMPLETE: c+ "
            "has simple poles at [-1] and [-T], c- at [-1] and [+T], all of them zeros "
            "of a theta_p, whose zero set is the single orbit -p^Z. The residue theorem "
            "on C*/p^Z confirms completeness (two cancelling residues per entry; a lone "
            "simple pole would have been impossible). The [-1] pole is a normalisation "
            "artifact of the 0-side character, shared by both columns; only [+-T] carry "
            "connection data. This also RESOLVES the c+ near-constancy: both its poles "
            "lie on the negative real ray, so the positive axis — the only region "
            "previously sampled — is maximally far from them. The pi^2 observation is "
            "retired as unnecessary. STILL OPEN: the Stokes multipliers themselves, and "
            "the converse of the theta zero locus (Jacobi triple product). Nothing "
            "wired to production."
        ),
        "durationMs": int((time.perf_counter() - t0) * 1000),
    }
    out = script_path.parent / "c3-w2-c1-pole-divisor.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=1) + "\n")
    print(f"\nwrote {out}")


if __name__ == "__main__":
    main()
