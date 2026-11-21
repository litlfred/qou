"""fivetwo_chirality_frame_vs_snappy_probe.py

Bean qou-lrvc: WHICH chirality is the Rolfsen-table 5_2 in the frame derived in
two_bridge_cusp_rows_apoly_probe.py (#6985)?  The derived frame is
  lambda = the cusp class dying in H_1(M);  mu = the unique complement whose
  filling admits no nondegenerate representation (Property P certificate);
  lambda oriented so Im(t_lambda / t_mu) > 0 for the Im z > 0 solution,
and in it the Farey-word triangulation RL of K(7,3) has A-polynomial
  A = L^3 + L^2 (M^10 - M^8 + 2M^4 + 2M^2 - 1) + L(-M^14 + 2M^12 + 2M^10 - M^6 + M^4) + M^14,
cusp shape t_lambda/t_mu = 2.49024... + 2.97945... i and boundary slopes
{-10, -4, 0}.  The library held no source that fixes the chirality convention.

Two held-in-sandbox sources settle it (route table, sandbox-egress.md):

 (1) Culler's census A-polynomials, library/A_census.tgz (owner upload,
     source https://homepages.math.uic.edu/~culler/Apolynomials/), computed
     in SnapPy's (mu, lambda) framing for the census manifold K3_2 = m015 =
     SnapPy's '5_2'.  Compared EXACTLY (sympy) with the derived polynomial.
 (2) SnapPy 3.3.2 (pip, route 2), whose Manifold('5_2') is the Rolfsen-table
     knot as SnapPy digitises it.  Its cusp shape (longitude/meridian) at
     quad-double precision, its normal boundary slopes, its identification
     with m015 / K3_2, and its mirror's, compared with the derived frame.

The comparison is a DISCRETE decision (tau vs -conj(tau); slopes {0,4,10} vs
{0,-4,-10}); SnapPy's high-precision cusp shape is still carried as an mpf
string and matched to 40 digits so the agreement is checkable, not merely
sign-level.  Mirror image: A_{mirror K}(L, M) = A_K(1/L, M) up to a unit
(Cooper-Culler-Gillet-Long-Shalen), equivalently M -> 1/M by the reciprocal
symmetry; the cusp shape goes tau -> -conj(tau); slopes negate.

Audit-only; scope-(a); no q, no anchor.  What it does NOT do: it does not say
which chirality GGM's S+/S- factorisations (FiveTwoDTSpectrumSplit) belong to
-- that needs GGM's own orientation convention, which their papers do not
state relative to a table.
"""
from __future__ import annotations

import json
import os
import re
import sys
import tarfile
import tempfile
import time

import mpmath as mp

# 5_2's volume as the corpus derived it (aomega-m3 floor-remainder witness), read
# rather than typed: the geometric volume is the largest of the conjugate volumes.
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                       "aomega-m3-floor-remainder-from-derived-shape-fields.witness.json")) as _fh:
    _VOLS52 = json.load(_fh)["data"]["fivetwo"]["conjugate_volumes"]
with mp.workdps(50):
    _CORPUS_VOL_52 = max(mp.mpf(v) for v in _VOLS52)
import sympy as sp

mp.mp.dps = 50
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = HERE
while ROOT != os.path.dirname(ROOT):
    if os.path.exists(os.path.join(ROOT, "AGENTS.md")):
        break
    ROOT = os.path.dirname(ROOT)
sys.path.insert(0, os.path.join(ROOT, "computations"))

DERIVED = os.path.join(HERE, "two-bridge-cusp-rows-apoly.witness.json")
CENSUS = os.path.join(ROOT, "library", "A_census.tgz")


def qd(x):
    """SnapPy quad-double -> mpf via its decimal string ('3.65... E-64' carries a space)."""
    return mp.mpmathify(str(x).replace(" E", "e").replace("E", "e").replace(" ", ""))


def parse_culler(text):
    """Culler's .apoly format: 'A_K := (term)*(poly) + (term)*(poly) ...;' -> sympy in L, M."""
    L, M = sp.symbols("L M")
    body = text.split(":=", 1)[1].strip().rstrip(";")
    body = body.replace("^", "**")
    return sp.expand(sp.sympify(body, locals={"L": L, "M": M}))


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update(kw)
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    L, M = sp.symbols("L M")
    with open(DERIVED) as fh:
        dw = json.load(fh)
    d = dw["data"]
    A52 = sp.expand(sp.sympify(d["fivetwo_apoly"], locals={"L": L, "M": M}))
    A41 = sp.expand(sp.sympify(d["fourone_apoly"], locals={"L": L, "M": M}))
    tau52 = mp.mpmathify(d["fivetwo_cusp_shape_lambda_over_mu"].strip("()").replace(" ", ""))
    slopes52 = sorted(int(s) for s in d["fivetwo_boundary_slopes_derived"])

    # ---- (1) Culler's census polynomials ---------------------------------------
    print("[1] Culler census A-polynomials (library/A_census.tgz)")
    with tarfile.open(CENSUS) as tf, tempfile.TemporaryDirectory() as td:
        tf.extractall(td)
        K32 = parse_culler(open(os.path.join(td, "apolys", "K3_2.apoly")).read())
        K21 = parse_culler(open(os.path.join(td, "apolys", "K2_1.apoly")).read())
    print(f"    K3_2 (5_2): {K32}")
    print(f"    K2_1 (4_1): {K21}")
    # 4_1 control: identical
    check("fourone-derived-equals-culler-K2_1-exactly", sp.expand(A41 - K21) == 0)
    # 5_2: Culler = L^3 * A(1/L, M) exactly, i.e. the MIRROR (L -> 1/L)
    mirrorL = sp.expand(sp.cancel(L**3 * A52.subs(L, 1 / L)))
    same = sp.expand(A52 - K32) == 0
    mirr = sp.expand(mirrorL - K32) == 0
    check("fivetwo-culler-K3_2-is-the-derived-polynomial-under-L->1/L (mirror), not equal",
          mirr and not same, same=same, mirror=mirr)

    # ---- (2) SnapPy's Rolfsen-table 5_2 -----------------------------------------
    import snappy
    print(f"\n[2] SnapPy {snappy.__version__}: Manifold('5_2') (Rolfsen table as digitised by SnapPy)")
    Mf = snappy.Manifold("5_2")
    ident = [str(x) for x in Mf.identify()]
    print(f"    identify: {ident}")
    check("snappy-5_2-identifies-as-m015-and-K3_2",
          any(s.startswith("m015") for s in ident) and any(s.startswith("K3_2") for s in ident),
          identify=ident)
    Hp = Mf.high_precision()
    sh = Hp.cusp_info()[0]["shape"]
    tau_sn = mp.mpc(qd(sh.real()), qd(sh.imag()))
    print(f"    cusp shape lambda/mu (quad-double): {mp.nstr(tau_sn, 45)}")
    print(f"    derived                             : {mp.nstr(tau52, 45)}")
    tol = mp.mpf(10) ** -38
    is_same = abs(tau_sn - tau52) < tol
    is_mirror = abs(tau_sn - (-mp.conj(tau52))) < tol
    check("snappy-5_2-cusp-shape-is-MINUS-CONJUGATE-of-derived (mirror), to 38 digits",
          is_mirror and not is_same,
          snappy=mp.nstr(tau_sn, 45), derived=mp.nstr(tau52, 45),
          diff_mirror=mp.nstr(abs(tau_sn + mp.conj(tau52)), 5))
    sl = sorted(int(p) * int(q) for (p, q) in Mf.normal_boundary_slopes())  # q = +-1 here
    print(f"    normal boundary slopes: {sl}   derived: {slopes52}")
    check("snappy-5_2-slopes-are-negatives-of-derived", sl == sorted(-s for s in slopes52),
          snappy=sl, derived=slopes52)
    Mm = snappy.Manifold("5_2")
    Mm.reverse_orientation()
    shm = Mm.high_precision().cusp_info()[0]["shape"]
    tau_mir = mp.mpc(qd(shm.real()), qd(shm.imag()))
    slm = sorted(int(p) * int(q) for (p, q) in Mm.normal_boundary_slopes())
    print(f"    mirror of snappy 5_2: shape {mp.nstr(tau_mir, 30)}, slopes {slm}")
    check("mirror-of-snappy-5_2-matches-derived-frame-exactly (shape to 38 digits, slopes)",
          abs(tau_mir - tau52) < tol and slm == slopes52)
    vol_sn = qd(Hp.volume())
    check("snappy-5_2-volume-matches-corpus", abs(vol_sn - _CORPUS_VOL_52) < mp.mpf(10) ** -18,
          snappy=mp.nstr(vol_sn, 25))
    # 4_1 control (amphichiral): shape purely imaginary, slopes +-4
    F = snappy.Manifold("4_1").high_precision()
    shf = F.cusp_info()[0]["shape"]
    tau41 = mp.mpc(qd(shf.real()), qd(shf.imag()))
    check("fourone-snappy-shape-2sqrt3i-matches-derived",
          abs(tau41 - mp.mpc(0, 2 * mp.sqrt(3))) < mp.mpf(10) ** -25, snappy=mp.nstr(tau41, 30))

    verdict = (
        "In the derived (mu by the filling test, lambda homological, Im tau > 0) frame the "
        "Farey-word triangulation RL of K(7,3) is the MIRROR of SnapPy 3.3.2's Rolfsen-table "
        "5_2 (= census m015 = Culler's K3_2): SnapPy's cusp shape is -conj(tau_derived) to 38 "
        "digits, its slopes are {0,4,10} against the derived {0,-4,-10}, and Culler's "
        "A_{K3_2} is the derived polynomial under L -> 1/L exactly; reversing SnapPy's "
        "orientation reproduces the derived frame exactly. The 4_1 control agrees identically "
        "(amphichiral). So 'Rolfsen's 5_2, as SnapPy digitises it' is settled: the derived "
        "triangulation carries the OTHER chirality. Still open: which of GGM's S+/S- attaches "
        "to which chirality, since GGM state no table-relative orientation."
    )
    print(f"\n verdict: {verdict}")

    from qou_substrate.witness import WitnessBuilder as _WB
    witness = {
        "name": "fivetwo-chirality-frame-vs-snappy",
        "description": "Which chirality the Rolfsen-table 5_2 (SnapPy 3.3.2, Culler census) is in the "
                       "derived (mu, lambda, Im tau > 0) frame of #6985: the mirror.",
        "computation": "fivetwo-chirality-frame-vs-snappy",
        "engine": "python+snappy",
        "scriptFile": os.path.basename(__file__),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-09-06-two-bridge-layering-from-farey-word.md",
        "parameters": {
            "derived_witness": os.path.basename(DERIVED),
            "derived_scriptHash": dw.get("scriptHash"),
            "census_tarball": "library/A_census.tgz",
            "snappy_version": snappy.__version__,
        },
        "data": {
            "culler_K3_2": str(K32), "culler_K2_1": str(K21),
            "derived_A52": str(A52), "derived_A41": str(A41),
            "snappy_5_2_cusp_shape": mp.nstr(tau_sn, 45),
            "derived_5_2_cusp_shape": mp.nstr(tau52, 45),
            "snappy_5_2_slopes": sl, "derived_5_2_slopes": slopes52,
            "snappy_5_2_identify": ident,
            "relation": "mirror",
        },
        "verdict": verdict,
        "assertions": assertions,
    }
    _WB.stamp_staleness_metadata(witness, script_path=__file__, engine=None, q0_anchor=False)
    out = os.path.join(HERE, "fivetwo-chirality-frame-vs-snappy.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
    nfail = sum(1 for a in assertions if not a["passed"])
    print(f"\n witness: {out}\n assertions: {len(assertions) - nfail}/{len(assertions)} passed")
    return 1 if nfail else 0


if __name__ == "__main__":
    raise SystemExit(main())
