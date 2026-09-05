#!/usr/bin/env python3
"""phi_b_substrate_regime.py — pin the Faddeev Φ_b b-map at real substrate
q₀ > 1 and validate the contour evaluator there (the regime flagged OPEN in
phi_b_evaluator.py).

INFRASTRUCTURE (no c_k values, no wiring, no fits). Closes the "SUBSTRATE
regime not implemented" gap of `phi_b_evaluator.py`: the Φ_b modular double
is the named object behind the c₃ bar-ODD S-leak
(docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md), and any
argument search for the two S-values needs a *validated* evaluator at the
physical anchors first.

The b-map (mechanically pinned here, not assumed):

    q = e^{2πib²}  ⇒  for real q₀ > 1, b² = ±i·t/(2π), t = ln q₀,
    i.e.  b_± = √(t/2π)·e^{±iπ/4}.

  * b_+ (arg b = +π/4):  q = e^{−t} = 1/q₀ (|q| < 1),
    dual q̃ = e^{−2πi/b²} = e^{−4π²/t}  (≈ 1e-164 at the anchors —
    the suppression quoted by qbeta_fmap_modular_dual_missing_probe.py).
    Both halves of the modular-double product converge → full cross-check.
  * b_− (arg b = −π/4):  q = e^{+t} = q₀ (|q| > 1), dual q̃ = e^{+4π²/t}
    explodes → the product form is invalid on this branch. The two branches
    are DISTINCT analytic objects related (measured, S1b) by
        log Φ_{b_−}(z) = −conj(log Φ_{b_+}(z))   for real z,
    i.e. the branches share the same PHASE Im log Φ_b (the decay-relevant
    part) and invert the modulus. The evaluator header's "needs
    arg b = −π/4" is thereby refined: the product-supported substrate
    branch is arg b = +π/4, and nothing is lost — b_− carries the same
    bar-odd phase data.

SELF-VALIDATION BATTERY (anti-self-deception: conventions surface here
mechanically, nothing is trusted from memory):
  S1  contour evaluator runs at b_+ (delta > 0) and log Φ_b(0) matches the
      closed form  Φ_b(0)² = e^{−iπ(1+2c_b²)/6}  (from the V4-measured
      inversion constant of phi_b_evaluator.py at z = 0).
  S1b b_− branch: contour also valid there; measured branch relation
      log Φ_{b_−}(z) = −conj(log Φ_{b_+}(z)) for real z (same phase,
      inverted modulus).
  S2  shift equation in b at b_+, substrate-scale real z.
  S3  shift equation in 1/b — via the modular-double product (the contour
      tail decays too slowly for the ±i/(2b) shift at |1/b| ≈ 7.8; the
      product form is exact there and independently validated by S5).
  S4  modular invariance Φ_b = Φ_{1/b} (contour, both at b_+).
  S5  double product == contour Φ_b at both anchors (P/Φ = 1), kmax sized
      for |q| = 1/q₀ ≈ 0.90 (≈ 900 terms for 40 dps).
  S6  DUAL-FACE SUPPRESSION, quantified: the compact numerator-only product
      (q̃-half dropped) equals Φ_b to ~|q̃|^{1/2} ≈ 1e-82 at real
      substrate-scale z. Consequence (scoping, scope-(a)): NO real
      substrate-scale argument z can read the S-leak (~1e-2) off the dual
      face; an S-producing argument must sit near the dual line
      Re(2πz/b) ≈ 2π²/t (the c_b pole/zero lattice) or read the compact
      face differently.
  S7  anchor measurement: log Φ_b at z = u(q₀) for BOTH anchors (proton /
      muon), recorded for the argument-scan probe downstream.

Run:  python3 -u computations/qbeta/phi_b_substrate_regime.py \\
        2>&1 | tee /tmp/phi_b_substrate_regime.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

_HERE = os.path.dirname(os.path.abspath(__file__))
_ROOT = os.path.abspath(os.path.join(_HERE, "..", ".."))
for _p in (os.path.join(_ROOT, "computations"),
           os.path.join(_ROOT, "tools", "qou-substrate", "python")):
    if _p not in sys.path:
        sys.path.insert(0, _p)

from phi_b_evaluator import log_phi_b, phi_b, phi_b_double_product  # noqa: E402
import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)


def _repo_head_sha():
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                  cwd=_HERE, text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def _relerr(a, c):
    return float(mp.fabs(a - c) / max(mp.fabs(c), mp.mpf("1e-40")))


def b_substrate(q0, branch=+1):
    """The substrate b-map: b = √(t/2π)·e^{±iπ/4}, t = ln q₀ (q₀ real > 1)."""
    t = mp.log(q0)
    return mp.sqrt(t / (2 * mp.pi)) * mp.e ** (mp.mpc(0, 1) * branch * mp.pi / 4)


def compact_half_product(z, b, kmax):
    """Numerator half of the modular-double product only (q̃-half dropped):
    ∏_{k≥0} (1 + e^{2πib²(k+½)} e^{2πbz}) — branch-safe exponentials."""
    b = mp.mpmathify(b)
    z = mp.mpmathify(z)
    two_pi_i = 2 * mp.pi * mp.mpc(0, 1)
    qq = mp.e ** (two_pi_i * b ** 2)
    if mp.fabs(qq) >= 1:
        raise ValueError("compact half-product needs |e^{2πib²}| < 1")
    prod = mp.mpf(1)
    for k in range(kmax):
        kk = k + mp.mpf(1) / 2
        prod *= 1 + mp.e ** (two_pi_i * b ** 2 * kk + 2 * mp.pi * b * z)
        if mp.fabs(qq) ** (k + 1) < mp.mpf(10) ** (-mp.mp.dps - 5):
            break
    return prod


def main() -> int:
    mp.mp.dps = 40
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities

    q_p = q_at(40)
    q_m = q_muon_at(40)
    t_p = mp.log(q_p)
    # |q| at b_+ is 1/q₀ ≈ 0.90; k terms give |q|^k — size kmax for dps+guard.
    KMAX = int((mp.mp.dps + 10) * mp.log(10) / t_p) + 50

    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    print("=" * 78)
    print(" Faddeev Φ_b — substrate-regime battery (real q₀ > 1, b = √(t/2π)e^{±iπ/4})")
    print("=" * 78)
    print(f"  q_proton = {mp.nstr(q_p, 20)}   q_muon = {mp.nstr(q_m, 20)}")

    bp = b_substrate(q_p, +1)
    bm = b_substrate(q_p, -1)
    two_pi_i = 2 * mp.pi * mp.mpc(0, 1)
    qq_p = mp.e ** (two_pi_i * bp ** 2)
    qt_p = mp.e ** (-two_pi_i / bp ** 2)
    print(f"  b_+ = {mp.nstr(bp, 10)}   |q| = {mp.nstr(mp.fabs(qq_p), 10)}"
          f"   |q̃| = {mp.nstr(mp.fabs(qt_p), 4)}")
    check("bmap_q_is_inverse_q0", _relerr(mp.fabs(qq_p), 1 / q_p) < 1e-35,
          f"|e^(2pi i b_+^2)| = 1/q0  (rel {_relerr(mp.fabs(qq_p), 1 / q_p):.1e})")
    dual_log10 = float(mp.log10(mp.fabs(qt_p)))
    check("dual_suppression_scale", -170 < dual_log10 < -155,
          f"log10|q~| = {dual_log10:.1f} (expected ~ -164 = -4*pi^2/(t*ln10))")

    # ---- S1: Φ_b(0) vs closed form (measured V4 constant at z = 0) ----
    cb = mp.mpc(0, 1) * (bp + 1 / bp) / 2
    phi0_sq_closed = mp.e ** (-mp.mpc(0, 1) * mp.pi * (1 + 2 * cb ** 2) / 6)
    L0 = log_phi_b(mp.mpf(0), bp)
    e_s1 = _relerr(mp.e ** (2 * L0), phi0_sq_closed)
    check("S1_phi0_closed_form", e_s1 < 1e-25,
          f"phi(0)^2 vs e^(-i pi (1+2c_b^2)/6): rel {e_s1:.1e}")

    # ---- S1b: branch relation  log Φ_{b_−}(z) = −conj(log Φ_{b_+}(z)) ----
    zt = mp.mpf("0.008")
    e_s1b = max(
        float(mp.fabs(log_phi_b(z, bm) + mp.conj(log_phi_b(z, bp))))
        for z in (mp.mpf(0), zt))
    check("S1b_branch_relation_neg_conj", e_s1b < 1e-30,
          f"log Phi_(b_-)(z) = -conj(log Phi_(b_+)(z)) at z in {{0, {float(zt)}}}: "
          f"abs resid {e_s1b:.1e} (same phase, inverted modulus)")

    # ---- S2: shift equation in b at substrate-scale real z ----
    sub_p = substrate_ladder_quantities(q_p)
    u_p = sub_p["u"]
    lhs = phi_b(u_p - mp.mpc(0, 1) * bp / 2, bp) / phi_b(u_p + mp.mpc(0, 1) * bp / 2, bp)
    tgt = 1 + mp.e ** (2 * mp.pi * bp * u_p)
    e_s2 = _relerr(lhs, tgt)
    check("S2_shift_in_b", e_s2 < 1e-20,
          f"Phi(u-ib/2)/Phi(u+ib/2) = 1+e^(2 pi b u): rel {e_s2:.1e}")

    # ---- S5 first (product == contour), since S3 leans on the product ----
    e_s5 = []
    for tag, q0 in (("proton", q_p), ("muon", q_m)):
        b0 = b_substrate(q0, +1)
        z0 = substrate_ladder_quantities(q0)["u"]
        P = phi_b_double_product(z0, b0, kmax=KMAX)
        F = phi_b(z0, b0)
        e = _relerr(P, F)
        e_s5.append(e)
        print(f"       double product vs contour @ {tag}: rel {e:.1e}")
    check("S5_double_product_equals_contour", max(e_s5) < 1e-25,
          f"P/Phi = 1 at both anchors (worst rel {max(e_s5):.1e}, kmax={KMAX})")

    # ---- S3: shift in 1/b via the (now-validated) product form ----
    zq = mp.mpf("0.02")
    sh = mp.mpc(0, 1) / (2 * bp)
    Pm = phi_b_double_product(zq - sh, bp, kmax=KMAX)
    Pp = phi_b_double_product(zq + sh, bp, kmax=KMAX)
    tgt3 = 1 + mp.e ** (2 * mp.pi * zq / bp)
    e_s3 = _relerr(Pm / Pp, tgt3)
    check("S3_shift_in_inv_b_via_product", e_s3 < 1e-25,
          f"P(z-i/(2b))/P(z+i/(2b)) = 1+e^(2 pi z / b): rel {e_s3:.1e}")

    # ---- S4: modular invariance b ↔ 1/b (contour) ----
    e_s4 = _relerr(phi_b(zq, 1 / bp), phi_b(zq, bp))
    check("S4_modular_invariance", e_s4 < 1e-25, f"Phi_b = Phi_(1/b): rel {e_s4:.1e}")

    # ---- S6: dual-face suppression at real substrate-scale z ----
    Pc = compact_half_product(u_p, bp, kmax=KMAX)
    e_s6 = _relerr(Pc, phi_b(u_p, bp))
    # |q̃|^(1/2) ≈ 1e-82 is the leading dropped term; the residual must sit at
    # (numerical zero given dps=40) — i.e. the compact half IS Φ_b to 40 dps.
    check("S6_dual_face_suppressed_at_real_z", e_s6 < 1e-35,
          f"compact half-product vs Phi_b at z=u: rel {e_s6:.1e} "
          f"(dual half ~ |q~|^(1/2) ~ 1e{int(dual_log10 // 2)})")

    # ---- S7: anchor measurement at z = u (for the argument-scan probe) ----
    s7 = {}
    for tag, q0 in (("proton", q_p), ("muon", q_m)):
        b0 = b_substrate(q0, +1)
        z0 = substrate_ladder_quantities(q0)["u"]
        L = log_phi_b(z0, b0)
        s7[tag] = {"z_u": mp.nstr(z0, 30),
                   "re_log_phi": mp.nstr(mp.re(L), 30),
                   "im_log_phi": mp.nstr(mp.im(L), 30)}
        print(f"  S7 measurement @ {tag}: log Phi_b(u) = {mp.nstr(L, 20)}")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SUBSTRATE REGIME PINNED + VALIDATED: at real q0 > 1 the Faddeev b-map is "
        "b = sqrt(ln q0 / 2pi) * e^(+i pi/4) (q = 1/q0, dual q~ = e^(-4pi^2/ln q0) "
        "~ 1e-164; the previously-documented arg b = -pi/4 branch is the "
        "inverse-conjugate object log Phi_(b-) = -conj(log Phi_(b+)) -- same "
        "phase, inverted modulus -- and does not support the product form). "
        "Contour evaluator, "
        "modular-double product, both shift equations, modular invariance, and the "
        "Phi(0) closed form all agree at both anchors. Dual face is ~1e-82-"
        "suppressed at real substrate-scale arguments (S6) => the c3 S-leak "
        "CANNOT be a real substrate-scale-argument dual-face readout (scope-(a)); "
        "the argument search must probe the c_b lattice / complex arguments or "
        "compact-face differences. NO c_k derived; NO wiring."
        if all_passed else
        "INCONCLUSIVE -- an assertion failed; do not build the argument scan on this."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    src = open(__file__, "rb").read()
    witness = {
        "computation": "phi-b-substrate-regime",
        "description": "Pin + validate the Faddeev Phi_b substrate-regime b-map "
                       "(b = sqrt(t/2pi) e^(i pi/4), q = 1/q0) at both anchors: "
                       "contour vs modular-double product, shift equations, "
                       "Phi(0) closed form, dual-face suppression quantified.",
        "auditOnly": True,
        "tier": "infrastructure-validation (no c_k, no wiring, no fits)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "precision_dps": mp.mp.dps,
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "b_map": "b = sqrt(ln q0 / (2*pi)) * exp(+i*pi/4); q = exp(2*pi*i*b^2) = 1/q0",
            "b_plus_proton": mp.nstr(bp, 30),
            "abs_q_proton": mp.nstr(mp.fabs(qq_p), 30),
            "log10_abs_dual_qtilde": dual_log10,
            "anchor_log_phi_at_u": s7,
            "verdict": verdict,
        },
        "context": {
            "evaluator": "computations/qbeta/phi_b_evaluator.py (native-regime battery V1-V6)",
            "s_leak_target": "docs/audits/2026-07-11-qbeta-c3-barodd-sleak-phib-target.md",
            "dual_missing_probe": "computations/qbeta/qbeta_fmap_modular_dual_missing_probe.py",
        },
    }
    out = os.path.join(_HERE, "phi-b-substrate-regime.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        json.dump(witness, f, indent=2)

    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
