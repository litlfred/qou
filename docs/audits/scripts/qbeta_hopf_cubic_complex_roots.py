#!/usr/bin/env python3
"""
The Hopf-cubic odd carrier: complex roots (the chiral realization) + substrate
evaluation, completing the parity↔chirality dictionary.  Self-contained; NO fit,
NO wiring, NO c_k value changed, NO tier change.  Scope-(a); confirms the corpus
(qbeta-odd-carrier-hopf-cubic.md) and ties it to the amphichirality result (#3482).

Dictionary being closed:
  bar-EVEN (cosh, m_π, CAL-3) ↔ amphichiral 4_1 ↔ CS=0, 𝔙 real ↔ ℚ(√3)  [#3482]
  bar-ODD  (sinh, Q_β, CAL-2) ↔ chiral Hopf   ↔ disc<0, complex roots ↔ cubic S₃ field

Facts checked (all exact / high precision):
  A. C = C_Hopf + C_unknot exactly; disc(C_Hopf)=-76, disc(C)=-152 (both = ·19).
  B. C_Hopf has ONE real + a COMPLEX-CONJUGATE pair (disc<0) — the odd channel's
     complex source is arithmetic (a negative-discriminant cubic), NOT a
     hyperbolic iCS.  Its real part ≈ q0 (flagged, not claimed).
  C. C_Hopf(2) = -2 exactly = J_Hopf(q=1) = the empirical c_3 near-match (classical
     anchor y=2 ⇔ q=1).
  D. At the substrate anchor y0=q0²+q0⁻²≈2.0437: C_Hopf(y0)≈-2.087 ≈ c_3≈-2.07, but
     IDENTICAL at both anchors (anchor-invariant to 1e-8) — so the cubic is the
     FIBRE carrier, and the c_3 cross-anchor SWING is NOT in it (it is the S leak,
     per the rigidity prune SRigidityPrune.no_anchor_invariant_realizes_swing).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "computations", "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def _find_repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


_REPO_ROOT = _find_repo_root()


def _repo_head_sha():
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_REPO_ROOT, text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def cHopf(y):
    return y ** 3 - 6 * y ** 2 + 10 * y - 6


def cUnknot(y):
    return 2 * y ** 2 - 7 * y + 4


def cTotal(y):
    return y ** 3 - 4 * y ** 2 + 3 * y - 2


def disc_cubic(a, b, c):  # y³ + a y² + b y + c
    return 18 * a * b * c - 4 * a ** 3 * c + a ** 2 * b ** 2 - 4 * b ** 3 - 27 * c ** 2


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- A. identity + discriminants ---------------------------------------
    # EXACT coefficient-level check (not a single-point float eval): compare the
    # integer coefficient vectors [y³, y², y¹, y⁰] of C vs C_Hopf + C_unknot.
    C_coeffs = [1, -4, 3, -2]
    Hopf_plus_unknot_coeffs = [1, -6 + 2, 10 + (-7), -6 + 4]  # C_Hopf + C_unknot
    identity_ok = (C_coeffs == Hopf_plus_unknot_coeffs)
    dH = disc_cubic(-6, 10, -6)
    dC = disc_cubic(-4, 3, -2)
    print("=== A. identity + discriminants ===")
    print(f"  C = C_Hopf + C_unknot : {identity_ok}")
    print(f"  disc(C_Hopf) = {dH} = {dH//19}·19 ; disc(C) = {dC} = {dC//19}·19")
    check("sector_identity_C_eq_Hopf_plus_unknot", identity_ok)
    check("disc_Hopf_is_neg76", dH == -76)
    check("disc_total_is_neg152", dC == -152)
    check("prime19_shared_fingerprint", dH % 19 == 0 and dC % 19 == 0)

    # --- B. complex roots (the chiral realization) -------------------------
    roots = mp.polyroots([1, -6, 10, -6], maxsteps=200, extraprec=200)
    real_roots = [r for r in roots if abs(mp.im(r)) < mp.mpf("1e-30")]
    cplx_roots = [r for r in roots if abs(mp.im(r)) >= mp.mpf("1e-30")]
    print("\n=== B. C_Hopf roots (disc<0 ⇒ 1 real + complex pair) ===")
    for r in roots:
        print(f"  {mp.nstr(r,12)}")
    check("one_real_two_complex_roots", len(real_roots) == 1 and len(cplx_roots) == 2)
    # real part of the complex pair ≈ q0 (flagged only)
    q0 = mp.mpf("1.10997858275138")
    cplx_re = mp.re(cplx_roots[0]) if cplx_roots else mp.mpf(0)
    re_near_q0 = abs(cplx_re / q0 - 1)
    print(f"  complex-root real part = {mp.nstr(cplx_re,8)}  vs q0={mp.nstr(q0,8)}  "
          f"(rel {mp.nstr(re_near_q0,3)}; FLAGGED, not claimed)")

    # --- C. classical anchor y=2 (q=1): Hopf sector = c_3 near-match -2 -----
    print("\n=== C. classical anchor y=2 (q=1) ===")
    print(f"  C_Hopf(2) = {mp.nstr(cHopf(mp.mpf(2)),6)}  (= J_Hopf(q=1) = c_3 near-match)")
    check("cHopf_at_2_is_minus2", cHopf(mp.mpf(2)) == -2)

    # --- D. substrate anchor: fibre carrier, NOT the swing -----------------
    print("\n=== D. substrate anchor y0=q0²+q0⁻² (fibre carrier; anchor-invariant) ===")
    # NOTE: these q0 literals are ILLUSTRATIVE substrate-proximate anchors, not a
    # live read of the pinning. The anchor-invariance conclusion is ROBUST to any
    # re-pin: C_Hopf is smooth and y0=q0²+q0⁻² barely moves for ANY q0≈1.11, so a
    # different pin cannot change the "cubic is fibre (invariant), swing is S"
    # result. Kept as literals to preserve the standalone-audit convention
    # (docs/audits/scripts self-contained; no qou_substrate import coupling).
    anchors = {"proton": "1.10997858275138", "muon": "1.10997859555733"}
    ch_vals = {}
    for name, q in anchors.items():
        q = mp.mpf(q); y0 = q ** 2 + q ** -2
        ch_vals[name] = cHopf(y0)
        print(f"  {name}: y0={mp.nstr(y0,10)}  C_Hopf(y0)={mp.nstr(cHopf(y0),8)}  "
              f"(c_3≈{-2.06934 if name=='proton' else -2.02019})")
    # C_Hopf(y0) is anchor-invariant to ~1e-8 (y0 barely moves) ⇒ it is the FIBRE
    # carrier, and the ~2.4% c_3 swing is NOT in it (that is the S leak).
    ch_swing = abs(ch_vals["proton"] / ch_vals["muon"] - 1)
    c3_swing = abs(mp.mpf("-2.06934") / mp.mpf("-2.02019") - 1)
    print(f"  C_Hopf(y0) cross-anchor swing = {mp.nstr(ch_swing,3)}  vs c_3 swing "
          f"{mp.nstr(c3_swing,3)} ⇒ cubic is FIBRE (invariant); swing is the S leak")
    check("cubic_is_fibre_not_swing", ch_swing < mp.mpf("1e-6") < c3_swing)
    # value close to c_3 (fibre-level), within a few %
    check("cHopf_y0_near_c3_fibre_level",
          abs(ch_vals["proton"] / mp.mpf("-2.06934") - 1) < mp.mpf("0.02"))

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        "Parity↔chirality dictionary CLOSED. bar-EVEN ↔ amphichiral 4_1 (CS=0, 𝔙 "
        "real, ℚ(√3); #3482) ; bar-ODD ↔ chiral Hopf ↔ the cubic C_Hopf=y³−6y²+10y−6 "
        "with disc=-76<0 (one real + a COMPLEX-CONJUGATE pair — the odd channel's "
        "complex source is a negative-discriminant cubic, arithmetic, NOT a "
        "hyperbolic iCS). Shared prime-19 fingerprint (disc C=-152). C_Hopf(2)=-2 "
        "exactly = J_Hopf(q=1) = the c_3 near-match; at the substrate y0≈2.0437, "
        "C_Hopf(y0)≈-2.087 ≈ c_3, but ANCHOR-INVARIANT (swing<1e-6 vs c_3's 2.4%) — "
        "confirming the cubic is the FIBRE carrier and the swing is the S archimedean "
        "leak (rigidity prune). Complex-root real part ≈ q0 (flagged only). Confirms "
        "qbeta-odd-carrier-hopf-cubic.md; formalized in HopfCubicOddCarrier.lean. "
        "No fit; no c_k value; no wiring; no tier change."
        if all_passed else
        "INCONCLUSIVE — an identity/discriminant/root/anchor assertion failed."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-hopf-cubic-complex-roots",
        "description": "Hopf-cubic odd carrier: complex roots (chiral realization) + "
                       "substrate eval; closes the parity↔chirality dictionary "
                       "(even=amphichiral 4_1 real / odd=chiral Hopf complex cubic).",
        "audit_only": True,
        "tier": "structural-exact (identities, discriminants, roots; no QOU fit)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "disc_cHopf": dH,
            "disc_cTotal": dC,
            "cHopf_roots": [mp.nstr(r, 12) for r in roots],
            "complex_root_real_part": mp.nstr(cplx_re, 10),
            "cHopf_at_2": mp.nstr(cHopf(mp.mpf(2)), 6),
            "cHopf_at_substrate": mp.nstr(ch_vals["proton"], 8),
            "cHopf_anchor_swing": mp.nstr(ch_swing, 4),
            "c3_anchor_swing": mp.nstr(c3_swing, 4),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: odd-channel chiral Hopf cubic",
            "corpus": "content/.../mass-theory/qbeta-odd-carrier-hopf-cubic.md",
            "even_partner": "self-dual-higgs-real-volume.md (4_1 amphichiral, CS=0)",
            "lean": "QOU.QBeta.HopfCubic (cTotal_eq_cHopf_add_cUnknot, cHopf_at_two, "
                    "cHopf_discriminant_eq, prime_19_divides_both_discriminants)",
            "fibre_vs_leak": "C_Hopf(y0) anchor-invariant ⇒ fibre carrier; swing = S "
                             "(SRigidityPrune.no_anchor_invariant_realizes_swing)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-hopf-cubic-complex-roots.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
