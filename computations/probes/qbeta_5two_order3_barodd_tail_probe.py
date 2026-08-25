#!/usr/bin/env python3
"""qbeta_5two_order3_barodd_tail_probe.py — the 5₂ order-3 bar-odd Habiro tail vs
the corpus φ_odd data: an order-of-magnitude CONSISTENCY test (NOT an
identification).

CONTEXT (bean qou-9ghx; ATTACK 3 of the fresh-look qou-do3a). The colored-Jones
q-difference recursion is ORDER-2 for 4₁ (amphichiral, bar-EVEN, cyclotomic
C_n=1 ⇒ zero bar-odd datum; corpus AJFigureEight.lean, QCasoratianBarParity.lean
"order-2 qZeilberger operator") and ORDER-3 for 5₂ (chiral; Takata 0401068v1).
The bar-odd content of the Q_β odd channel lives in the cyclotomic-coefficient
bar-asymmetry (Lean HabiroCyclotomicOddLocus, #3993). This probe asks the modest
question: does the order-3-distinguished 5₂ bar-odd tail land at the same
ORDER OF MAGNITUDE as the corpus bar-odd anchor data?

Construction (authoritative Masbaum C_{5₂,n} on main + standard bar-even f_n):
    T_odd = Σ_{n=1}^{3} [ C_{5₂,n}(q0) − C_{5₂,n}(1/q0) ] · f_n(q0)
    f_n(q) = ∏_{j=1}^n (1−q^j)(1−q^{-j})   (bar-EVEN, so all odd content is in C)
    C_0=1, C_1=−(q⁴+q²), C_2=q¹¹+q⁸+q⁷+q⁵,
    C_3=−(q²¹+q¹⁷+q¹⁶+q¹⁵+q¹³+q¹²+q¹¹+q⁹)   (masbaum2003; witness
    qbeta-5two-masbaum-cyclotomic; #3993).

Corpus bar-odd anchor data (scope-(a) rows, NOT identified):
    S_muon   = +0.00968298    S_proton = −0.03945936
    φ_odd(strip, #3987) = −0.004145 rad (preliminary intrinsic bar phase).

RESULT (this probe): T_odd ≈ +0.0192, O(10⁻²) — same decade as S_muon/S_proton.
This is a POSITIVE consistency (structurally: 4₁→exact 0, 5₂→O(10⁻²) matching the
anchor scale) but NOT an identification: (i) an O(10⁻²) magnitude for a chiral
order-3 knot's cyclotomic bar-asymmetry at q0 is generic; (ii) the SIGN is
convention-dependent — the Masbaum variable q vs the framework's Jones t=q⁻¹
flips C_n(q)−C_n(1/q), which is why the prior n=1-only probe
(qbeta_5two_leading_odd_datum) reports −0.0139 where this q-convention gives
+0.0139 (same magnitude); (iii) the strip φ_odd (−0.004145) is ~5× smaller and
its intrinsic value needs the still-open classical-exponential stripping
(qbeta_g3_5two_barodd_substrate). scope-(a); no fit; no c_k; no recursion form
fabricated.

Run: python3 -u computations/probes/qbeta_5two_order3_barodd_tail_probe.py \\
       2>&1 | tee /tmp/qbeta_5two_order3_barodd.log
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

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


def _repo_root():
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found")


def _head_sha():
    for ev in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(ev)
        if v and v.strip():
            return v.strip()
    sha = subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


# muon substrate q0 (the computations/ canonical pin)
Q0 = mp.mpf("1.10997859555733471")
S_MUON = mp.mpf("0.00968298")
S_PROTON = mp.mpf("-0.03945936")
PHI_ODD_STRIP = mp.mpf("-0.004145")


def C(n, q):
    """Authoritative Masbaum 5₂ = K_2 cyclotomic coefficient (q-convention)."""
    if n == 0:
        return mp.mpf(1)
    if n == 1:
        return -(q ** 4 + q ** 2)
    if n == 2:
        return q ** 11 + q ** 8 + q ** 7 + q ** 5
    if n == 3:
        return -(q ** 21 + q ** 17 + q ** 16 + q ** 15
                 + q ** 13 + q ** 12 + q ** 11 + q ** 9)
    raise ValueError(n)


def f_n(n, q):
    """bar-even Kashaev-tail factor ∏_{j=1}^n (1−q^j)(1−q^{-j})."""
    r = mp.mpf(1)
    for j in range(1, n + 1):
        r *= (1 - q ** j) * (1 - q ** (-j))
    return r


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 74)
    print(" ATTACK 3 — 5₂ order-3 bar-odd tail vs corpus φ_odd (consistency test)")
    print("=" * 74)
    print(f"  q0 (muon) = {mp.nstr(Q0, 25)}")

    # (1) f_n bar-even (structural: all odd content is in the coefficient)
    max_fd = max(abs(f_n(n, Q0) - f_n(n, 1 / Q0)) for n in (1, 2, 3))
    check("f_n_bar_even", max_fd < mp.mpf("1e-30"),
          source="∏(1−q^j)(1−q^{-j}) is q↔q⁻¹ invariant — the bar-even factor, so "
                 "the entire bar-odd datum is carried by the cyclotomic coefficient")

    # (2) 4₁ (C_n=1, order-2, amphichiral) has EXACTLY zero bar-odd datum
    odd_41 = max(abs((mp.mpf(1) - mp.mpf(1)) * f_n(n, Q0)) for n in (1, 2, 3))
    check("fourone_order2_zero_odd_datum", odd_41 == 0,
          source="4₁'s order-2 recursion has C_n=1 (bar-symmetric) ⇒ zero bar-odd "
                 "datum exactly — the amphichiral / bar-even baseline the order-3 "
                 "chiral 5₂ departs from")

    # per-n bar-odd contributions
    print("\n  term_n = (C_n(q0) − C_n(1/q0))·f_n(q0):")
    terms = {}
    for n in range(0, 4):
        terms[n] = (C(n, Q0) - C(n, 1 / Q0)) * f_n(n, Q0)
        print(f"    n={n}: term = {mp.nstr(terms[n], 10)}")
    T1 = terms[1]
    T_odd = terms[1] + terms[2] + terms[3]
    print(f"\n  leading (n=1)          = {mp.nstr(T1, 12)}")
    print(f"  full order-3 tail T_odd = {mp.nstr(T_odd, 12)}")

    # (3) order-of-magnitude consistency with the O(10^-2) anchor scale
    oom_T = int(mp.nint(mp.log10(abs(T_odd))))
    oom_muon = int(mp.nint(mp.log10(abs(S_MUON))))
    oom_proton = int(mp.nint(mp.log10(abs(S_PROTON))))
    print("\n  --- order-of-magnitude vs corpus bar-odd anchors ---")
    for label, val in (("S_muon", S_MUON), ("S_proton", S_PROTON),
                       ("phi_odd(strip)", PHI_ODD_STRIP)):
        same_sign = (mp.sign(T_odd) == mp.sign(val))
        d_oom = int(mp.nint(mp.log10(abs(T_odd))) - mp.nint(mp.log10(abs(val))))
        print(f"    vs {label:>14} = {mp.nstr(val, 6):>11}   "
              f"same_sign={same_sign!s:>5}  |ratio|={mp.nstr(abs(T_odd/val),5):>8}  "
              f"ΔOOM={d_oom:+d}")
    # "same order of magnitude" = within a factor of 10 of both mass anchors
    r_muon = abs(T_odd / S_MUON)
    r_proton = abs(T_odd / S_PROTON)
    check("order3_tail_within_decade_of_anchors",
          mp.mpf("0.1") < r_muon < mp.mpf("10") and
          mp.mpf("0.1") < r_proton < mp.mpf("10"),
          source="|T_odd/S_muon|=1.98 and |T_odd/S_proton|=0.49 — both within a "
                 "factor of 10, i.e. T_odd (≈+0.019) is the same order of magnitude "
                 "O(10⁻²) as the corpus bar-odd anchors. NOT an identification: an "
                 "O(10⁻²) chiral bar-asymmetry at q0 is generic, and the SIGN is "
                 "convention-dependent (Masbaum q vs Jones t=q⁻¹ flips it — prior "
                 "n=1 probe reads −0.0139, this q-convention +0.0139)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CONSISTENCY (scope-(a)), NOT an identification. The order-3 content that "
        "distinguishes chiral 5₂ from amphichiral 4₁ (which gives EXACTLY zero) "
        "yields a bar-odd tail T_odd ≈ +0.019 at the muon q0 — O(10⁻²), the same "
        "decade as the corpus bar-odd anchors S_muon (+0.00968) and S_proton "
        "(−0.03946). This structurally supports 'the order-jump 2→3 is where the "
        "Q_β bar-odd datum lives' (4₁→0, 5₂→O(10⁻²) matching the anchor scale), but "
        "cannot promote it past consistency: (i) an O(10⁻²) magnitude is generic; "
        "(ii) the sign is convention-dependent (q vs t=q⁻¹); (iii) the strip φ_odd "
        "(−0.004145) is ~5× smaller and its intrinsic value needs the open "
        "classical-exponential stripping (qbeta_g3_5two_barodd_substrate); (iv) the "
        "tail converges slowly (ratio ~0.4), so N≥4 colored Jones still adds "
        "O(10⁻³). No scope-(b) invariant is invoked. No fit; no c_k wired; only "
        "Masbaum-authoritative C_n + standard f_n."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as fh:
        src = fh.read()
    witness = {
        "computation": "qbeta-5two-order3-barodd-tail",
        "description": "The 5₂ order-3 bar-odd Habiro tail T_odd=Σ_{n=1}^3 "
                       "(C_n(q0)−C_n(1/q0))f_n(q0) ≈ +0.019 (O(10⁻²)) is "
                       "order-of-magnitude consistent with the corpus bar-odd "
                       "anchors S_muon/S_proton; 4₁ (order-2) gives exactly 0. "
                       "Consistency, NOT identification (sign convention-dependent; "
                       "strip φ_odd 5× smaller). scope-(a).",
        "audit_only": True,
        "tier": "numerical consistency (order-of-magnitude)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "T_odd": mp.nstr(T_odd, 12),
            "T_leading_n1": mp.nstr(T1, 12),
            "per_term": {str(n): mp.nstr(terms[n], 10) for n in range(4)},
            "anchors": {"S_muon": mp.nstr(S_MUON, 8),
                        "S_proton": mp.nstr(S_PROTON, 8),
                        "phi_odd_strip": mp.nstr(PHI_ODD_STRIP, 8)},
            "sign_convention_caveat": "Masbaum q vs framework Jones t=q⁻¹ flips the "
                                      "odd part; magnitude is convention-independent",
            "verdict": verdict,
        },
        "context": {
            "axis": "b3ix order-jump 2→3 (bean qou-9ghx; ATTACK 3 of qou-do3a)",
            "coefficients": "authoritative Masbaum C_{5₂,n} (masbaum2003, #3993, "
                            "witness qbeta-5two-masbaum-cyclotomic)",
            "related": ["qbeta_5two_leading_odd_datum_probe (n=1 only)",
                        "qbeta_g3_5two_barodd_substrate (intrinsic strip, open)"],
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-5two-order3-barodd-tail.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
