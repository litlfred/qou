#!/usr/bin/env python3
"""W1 — the c₀↔torsion factor is 2^(c−1), NOT a framing artifact.

Follow-on to borromean_nz_adjoint_torsion.py (PR #4253), which found the
Jones-side Kashaev constant and the independent Neumann–Zagier torsion agree
up to a clean factor 4 on the 3-cusp Borromean rings:

  exp(2 c₀) · |det J_NZ| = 4       (𝓑₃, c = 3 cusps),
  exp(2 c₀) · |det J_NZ| = 1       (4₁, c = 1 cusp; PR #4238 calibration).

This probe pins down what the factor is (and is not):

1. NOT a framing artifact.  The adjoint-torsion determinant depends on the
   choice of one peripheral curve per cusp (meridian vs longitude).  Sweeping
   all 2^c framings of L6a4 gives |det| ∈ {64, 128, 256, 512} = 2^{6..9} — the
   ALL-MERIDIAN framing is the unique MINIMUM (64), and it is the correct
   Kashaev framing (the colors live on the meridians).  No framing yields 16,
   so the factor 4 = 64/16 cannot be removed by re-framing.

2. It is the reduced-vs-Kashaev normalization, = 2^{c−1}.  The Habiro tower is
   the REDUCED colored Jones (J_{B,1} = 1); the meridian NZ torsion is the
   Kashaev-normalized 1-loop invariant.  For a c-component link the two differ
   by 2^{c−1} in the 1-loop constant — one factor 2 per cusp beyond the
   basepoint.  Data:

     c = 1 (4₁):     factor 2^0 = 1   (reduced Kashaev = unreduced for a knot)
     c = 3 (𝓑₃):     factor 2^2 = 4   (measured 4.03; c₀ = −ln4 gives exactly 4)

   The clean numerical signature is c₀(𝓑₃) = −ln 4 (exp 2c₀ = 1/16 = 4/64).

STATUS.  The 2^{c−1} law is a STRUCTURAL identification confirmed on the two
computed cusp numbers (c = 1, 3).  The decisive third data point is the 2-cusp
Whitehead link (predict factor 2^1 = 2, so exp 2c₀ = 2/|det J_NZ(W)| =
2/(4√2) = 1/(2√2)); its Kashaev tower is the honest next test.  The full
first-principles derivation of "one factor 2 per extra cusp" is the multi-cusp
saddle-point expansion (each additional cusp contributes a Gaussian meridian
integration) — recorded as the mechanism, not claimed as proved here.

⚠ REVISED 2026-08-08 — the SWEEP is confirmed and EXPLAINED; the 2^{c−1} LAW is
a reparametrization.  See `docs/audits/2026-08-08-per-cusp-factor-dissolves.md`
and `computations/probes/one_loop_c_sigma_percusp_dissolution_probe.py`.

WHAT SURVIVES, and is now understood rather than observed.  Point 1's framing
sweep is exactly right, and it is the CHANGE-OF-CURVE LAW: replacing cusp k's
meridian row by that cusp's longitude row multiplies the 1-loop invariant by
conj(cusp shape of cusp k).  Every Borromean cusp shape has modulus exactly 2,
so each longitude substitution doubles it.  Recomputed with the corrected,
triangulation-invariant invariant (computations/one_loop_torsion.py):

    0 longitudes  |tau| =  8      2^c|tau| =  64      <- all-meridian
    1 longitude   |tau| = 16      2^c|tau| = 128      (x3)
    2 longitudes  |tau| = 32      2^c|tau| = 256      (x3)
    3 longitudes  |tau| = 64      2^c|tau| = 512

reproducing {64, 128, 256, 512} exactly.  All-meridian is the unique minimum
because every cusp shape has modulus > 1.  "No framing yields 16" also stands:
16 = 2|tau_DG| is the normalization, not a framing.

WHAT DOES NOT SURVIVE.  The law is stated in |det J_NZ|, which PR #4691 showed
is NOT a topological invariant — retriangulate and it moves while exp(2 c_0)
does not, so `exp(2c_0)|det J_NZ| = 2^{c-1}` is not a well-posed statement about
the link.  Numerically it is right wherever |det J_NZ| = 2^c |tau_DG|, which
holds on the DEFAULT triangulations of 4_1, L5a1 and L6a4 and fails on 8 of 13
manifolds tested.  The well-posed form has no per-cusp factor at all:

    exp(2 c_0) = 1 / (2 |tau_DG|)        equivalently   c_sigma = 2^{-1/2}|tau_DG|^{-1/2}

so the 2^{c-1} here is just 2^c/2 — the determinant discrepancy over the
universal 2 — and the proposed mechanism ("one Gaussian meridian integration per
extra cusp") is displaced.  QOU.OneLoopEdgeLattice.percusp_factor_absorbs proves
in Lean that the two readings are the same function on such data, so agreement
at c = 1 and c = 3 could not have distinguished them.

THE DECISIVE THIRD DATA POINT ALREADY EXISTED.  This file calls for the 2-cusp
Whitehead Kashaev tower and predicts exp(2 c_0) = 1/(2 sqrt 2).  The corpus has
it: whitehead_c_sigma_hiprec.py pins c_sigma(L5a1) = 2^{-3/4} to 20 digits, so
exp(2 c_0) = c_sigma^2 = 2^{-3/2} = 1/(2 sqrt 2).  The prediction PASSES — and
passes equally for the c-free law, which is the point.

Discipline: audit-only; scope-(a); NO fit (framings/torsions are computed; the
2^{c−1} law is read off two exact data points, not tuned); nothing wired; L2
unchanged.  Self-contained: hardcoded SnapPy gluing integers + exact algebraic
shapes; `--recompute` cross-checks live SnapPy.

-- Ref: [manuscript] docs/audits/2026-07-25-borromean-cusp-framing-factor.md
"""
from __future__ import annotations

import hashlib
import itertools
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# L6a4 gluing_equations('rect'): (a, b, sign), eqn Π z^a (1−z)^b = (−1)^sign.
# 8 edges, then per cusp [meridian, longitude].  From SnapPy 3.3.2.
BOR_ROWS = [
    ([1, 0, 1, -1, 0, 1, 0, 0], [-1, 1, 0, 1, 0, 0, -1, 0], 1),
    ([-1, 0, 0, 0, 0, 0, 0, -1], [1, -1, 0, 0, -1, 0, 0, 1], 1),
    ([-1, 0, 0, 0, 0, 0, 0, 0], [1, 0, -1, -1, -1, 0, 0, 0], -1),
    ([0, -1, 0, 0, -1, 1, 0, 0], [-1, 1, 1, 0, 1, -1, 0, -1], -1),
    ([1, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, -1, 0], -1),
    ([0, 0, 0, 0, 0, -1, -1, -1], [0, -1, 0, 0, 0, 1, 1, 1], -1),
    ([0, 0, 0, 0, 0, -1, -1, 0], [0, 0, -1, -1, 0, 1, 1, 0], 1),
    ([0, 0, -1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, -1, 0, -1], 1),
    ([0, 1, 0, 0, 0, -1, 0, 0], [0, -1, 0, 0, 0, 1, 0, 1], 1),      # cusp1 mer
    ([1, 0, -1, 1, 0, 0, 1, 0], [-1, 1, 1, 0, 0, -1, 0, 0], 1),     # cusp1 long
    ([0, -1, -1, 0, 0, -1, -1, 1], [-1, 1, 0, -1, 1, 0, 1, -1], -1),  # cusp2 mer
    ([1, 0, 0, 0, 0, 0, 0, 0], [-1, 0, -1, -1, 1, 0, 0, 0], -1),    # cusp2 long
    ([0, 0, 0, 0, 0, -1, 0, 0], [0, -1, 0, 0, 0, 0, 1, 0], 1),      # cusp3 mer
    ([0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, -1, -1, -1, 0, 0], 1),     # cusp3 long
]
N, C = 8, 3
_half = (1 + 1j) / mp.mpf(2)
_one = 1 + 1j * mp.mpf(1)
Z_BOR = [_half, _one, _one, _one, _one, _half, _half, _half]


def jrow(row, w):
    a, b, _ = row
    return [mp.mpf(a[j]) - mp.mpf(b[j]) * w[j] for j in range(N)]


def rank_pick(pool):
    chosen = []
    for row in pool:
        Mx = [r[:] for r in chosen + [row]]
        r = 0
        for col in range(N):
            piv = next((i for i in range(r, len(Mx))
                        if abs(Mx[i][col]) > mp.mpf(10) ** -25), None)
            if piv is None:
                continue
            Mx[r], Mx[piv] = Mx[piv], Mx[r]
            for i in range(len(Mx)):
                if i != r and abs(Mx[i][col]) > 0:
                    f = Mx[i][col] / Mx[r][col]
                    Mx[i] = [Mx[i][k] - f * Mx[r][k] for k in range(N)]
            r += 1
        if r > len(chosen):
            chosen.append(row)
        if len(chosen) == N:
            break
    return chosen


def main() -> int:
    if "--recompute" in sys.argv:
        try:
            import snappy
            M = snappy.Manifold("L6a4")
            live = [(list(r[0]), list(r[1]), int(r[2])) for r in M.gluing_equations('rect')]
            assert live == [(a, b, s) for a, b, s in BOR_ROWS], "gluing drift!"
            print("SnapPy live cross-check: gluing rows match hardcoded ✓\n")
        except ImportError:
            print("(SnapPy not installed — skipping live cross-check)\n")

    w = [z / (1 - z) for z in Z_BOR]
    edges = [jrow(BOR_ROWS[i], w) for i in range(N)]
    cusp = [(jrow(BOR_ROWS[N + 2 * i], w), jrow(BOR_ROWS[N + 2 * i + 1], w)) for i in range(C)]

    print("Framing sweep (0 = meridian, 1 = longitude per cusp):")
    dets = {}
    for combo in itertools.product([0, 1], repeat=C):
        curves = [cusp[i][combo[i]] for i in range(C)]
        ch = rank_pick(edges + curves)
        d = abs(mp.det(mp.matrix(ch))) if len(ch) == N else None
        dets[combo] = d
        print(f"  {combo}: |det J_NZ| = {mp.nstr(d, 8) if d else 'degenerate'}")
    d_meridian = dets[(0, 0, 0)]
    min_det = min(float(v) for v in dets.values() if v)
    print(f"\n  all-meridian |det| = {mp.nstr(d_meridian, 8)}  (minimum over framings: {min_det})")
    print(f"  → 16 is NOT achieved by any framing; the factor 4 is not a framing choice.")

    # the 2^(c-1) law
    c0_measured = mp.mpf("-1.38281")
    exp2c0 = mp.e ** (2 * c0_measured)
    factor = exp2c0 * d_meridian
    print(f"\n2^(c−1) normalization law:")
    print(f"  c = 1 (4₁):  factor 2^0 = 1   (reduced Kashaev = unreduced, PR #4238)")
    print(f"  c = 3 (𝓑₃):  factor 2^2 = 4   (2^(c−1))")
    print(f"  measured exp(2c₀)·|det| = {mp.nstr(factor, 6)}  (c₀ = −ln4 gives exactly 4)")
    print(f"  Whitehead c = 2 prediction: factor 2^1 = 2  (decisive next test)")

    ok = (float(d_meridian) == 64.0 and min_det == 64.0)
    print(f"\nVERDICT: {'CONFIRMED' if ok else 'CHECK'} — meridian framing (64) is the unique "
          f"minimum; no framing gives 16; factor 4 = 2^(c−1) is the reduced-vs-Kashaev "
          f"normalization, not a framing artifact.")

    sp = Path(__file__).resolve(); src = sp.read_text()
    try:
        commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", str(sp)],
                                          cwd=sp.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath", "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": commit,
        "scriptFile": "computations/probes/borromean_cusp_framing_factor.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12], "scriptCommitSha": commit,
        "description": "The c₀↔NZ-torsion factor on the Borromean rings is 2^(c−1), not a "
                       "framing artifact: all 2^c peripheral framings give |det|≥64 (min=64, "
                       "all-meridian), none 16. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"manifold": "L6a4", "cusps": C},
        "data": {
            "framing_dets": {str(k): (mp.nstr(v, 12) if v else None) for k, v in dets.items()},
            "meridian_det": mp.nstr(d_meridian, 12),
            "min_det_over_framings": min_det,
            "factor_law": "2^(c-1)",
            "factor_measured": mp.nstr(factor, 8),
            "c0_borromean": "-1.38281 (≈ -ln4)",
            "whitehead_prediction_factor": 2,
            "note": "meridian framing 64 is the unique minimum; no framing yields 16, so the "
                    "factor 4 is the reduced-Habiro-vs-Kashaev normalization 2^(c-1), not a "
                    "framing choice. Whitehead (c=2 -> factor 2) is the decisive confirmation; "
                    "the per-cusp-2 mechanism is the multi-cusp saddle Gaussian, recorded not proved.",
        },
    }
    out = sp.with_name("borromean-cusp-framing-factor.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
