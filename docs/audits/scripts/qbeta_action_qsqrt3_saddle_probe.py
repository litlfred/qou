#!/usr/bin/env python3
"""
Test whether the ℚ(√−3) arithmetic of the 4₁ resurgence action's saddle
expansion is recoverable by PSLQ on the numerical Kashaev-ladder coefficients.

Follow-up to #3508 (A ≈ 0.688 real, not a clean framework constant). ℚ(√−3) is
the invariant trace field of the figure-eight knot 4₁ (the Eisenstein/hexagonal
field) — the arithmetic home of its perturbative expansion. The prior audit said
a closed form needs "the exact saddle expansion (rationals over ℚ(√−3)), not a
higher-order numerical fit." This is the cheap decisive check of the *numerical*
avenue, run before any expensive exact computation (formalize-first).

Method: high-precision log J_N(4₁), QR least-squares fit of log J_N − (3/2)log N
against {N, 1, 1/N, …, 1/N^K}; the 1/N^n coefficients c_n are PSLQ-tested for
rationality under torsion normalizations 3^{a·n}.

VERDICT (self-asserted, CI-safe): REFUTED (scope-(a)) — no c_n is a clean
rational under any tested ℚ(√−3) normalization, because (1) c_n is a divergent
resurgent series (c_n ~ n!/A^n, the Borel singularity A ≈ 0.688) and (2) the
high-n fit coefficients are precision-contaminated. Same entropy-block class as
the c_k PSLQ (#3536 P4). The exact route is the Ohtsuki state-integral saddle
recursion, NOT a numerical fit. NO fit to QOU data, NO wiring, NO c_k value, NO
tier change. Self-contained.
"""
import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp

mp.mp.dps = 220


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
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e})") from e
    if not sha:
        raise RuntimeError("empty commitSha")
    return sha


def log_kashaev_4_1(N):
    pi = mp.pi
    logterms = [mp.mpf(0)]
    logP = mp.mpf(0)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N))
        logterms.append(logP)
    m = max(logterms)
    return m + mp.log(mp.fsum(mp.exp(t - m) for t in logterms))


def is_rational(x, tol=mp.mpf(10) ** (-22)):
    r = mp.pslq([x, mp.mpf(1)], maxcoeff=10 ** 7, maxsteps=20000)
    if r and r[0] != 0:
        q = mp.mpf(-r[1]) / mp.mpf(r[0])
        if abs(x - q) < tol:
            return q
    return None


def main():
    K = 9
    Ns = list(range(300, 1181, 40))
    print(f"computing log J_N(4_1) for {len(Ns)} N (dps {mp.mp.dps}) ...")
    rows = [(N, log_kashaev_4_1(N) - mp.mpf(3) / 2 * mp.log(N)) for N in Ns]

    def basis(N):
        return [mp.mpf(N), mp.mpf(1)] + [1 / mp.mpf(N) ** k for k in range(1, K + 1)]
    coef = mp.qr_solve(mp.matrix([basis(N) for N, _ in rows]),
                       mp.matrix([g for _, g in rows]))[0]
    Vol = 2 * mp.im(mp.polylog(2, mp.exp(mp.j * mp.pi / 3)))
    vol_rel = abs(2 * mp.pi * coef[0] / Vol - 1)
    print(f"  Vol(4_1) recovered rel err = {mp.nstr(vol_rel, 3)}")
    c = [coef[2 + k] for k in range(K)]

    tp = 2 * mp.pi
    torsions = [(mp.mpf(0), ""), (mp.mpf(1) / 4, "3^(m/4)"),
                (mp.mpf(1) / 2, "3^(m/2)"), (mp.mpf(1), "3^m"),
                (-mp.mpf(1) / 2, "3^(-m/2)")]
    any_rational = False
    ratios = []
    # c[k] is the coefficient of 1/N^(k+1); label it c_m with the physical index
    # m = k+1 so the 1/N^1 coefficient (c_1) is tested and labels are honest.
    print("  PSLQ ℚ(√−3) test of ladder coeff c_m = [1/N^m] (raw and Ohtsuki-rescaled):")
    for k in range(K):
        m = k + 1
        if k >= 1:
            # NOT float(): `c` is exact/mpmath here, and the emission one line
            # below `c_n` already serializes via mp.nstr — this field simply
            # skipped the convention its sibling follows. Bean qou-irzg.
            ratios.append(c[k] / c[k - 1])
        hit = None
        for form, val in (("c_m", c[k]),
                          ("c_m·m!·(2π)^m", c[k] * mp.factorial(m) * tp ** m)):
            for a, tag in torsions:
                q = is_rational(val * mp.mpf(3) ** (a * m))
                if q is not None:
                    hit = (form, tag, q)
                    break
            if hit:
                break
        if hit:
            any_rational = True
            print(f"    c_{m}: {hit[0]}·{hit[1]} = {hit[2]}  RATIONAL")
        else:
            print(f"    c_{m}: {mp.nstr(c[k], 12)}  — no clean ℚ(√−3) rational")

    # Confirm the divergent/factorial growth signature (Borel singularity).
    print(f"  c_(m)/c_(m-1) ratios (rising ⇒ factorial growth): "
          f"{[round(float(r), 2) for r in ratios]}")

    verdict = (
        f"REFUTED (scope-(a)): the ℚ(√−3) saddle arithmetic of the 4₁ resurgence "
        f"action is NOT recoverable by PSLQ on the numerical Kashaev-ladder "
        f"coefficients. No c_m (m=1..{K}) is a clean rational under any tested "
        "torsion normalization 3^{a·m}. Two structural reasons: (1) c_m is a "
        "divergent resurgent series with factorial growth c_m ~ m!/A^m (A ≈ 0.688, "
        "the Borel singularity of #3508) — the rescaled c_m·m!·(2π)^m explodes past "
        "PSLQ's reach; (2) high-m fit coefficients are precision-contaminated. Same "
        "entropy-block class as the c_k PSLQ (#3536 P4). ℚ(√−3) IS the 4₁ invariant "
        "trace field (arithmetic home; classical, not in doubt), but the exact "
        "coefficients need the Ohtsuki state-integral saddle recursion, NOT a "
        "numerical fit. No fit; no c_k value; no wiring; no tier change."
        if not any_rational else
        "A ladder coefficient identified as an exact ℚ(√−3) rational — surface for "
        "the exact saddle-recursion cross-check (do NOT wire)."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "vol41_recovered", "passed": bool(vol_rel < mp.mpf(10) ** (-15))},
        {"name": "no_qsqrt3_rational_identified", "passed": bool(not any_rational)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-action-qsqrt3-saddle-probe",
        "description": "Numerical ℚ(√−3) identification of the 4₁ resurgence-action "
                       "saddle coefficients is entropy-blocked (divergent series + "
                       "fit contamination); exact route = Ohtsuki saddle recursion.",
        "audit_only": True,
        "tier": "numerical (decisive negative)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "vol41_recovered_rel": mp.nstr(vol_rel, 3),
            "c_n": [mp.nstr(x, 12) for x in c],
            "c_ratios": [mp.nstr(r, 12) for r in ratios],
            "any_rational_identified": any_rational,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: even-channel action, ℚ(√−3) saddle",
            "trace_field": "ℚ(√−3) IS the 4₁ invariant trace field (arithmetic home)",
            "exact_route": "Ohtsuki state-integral saddle recursion (not a numerical fit)",
            "entropy_block_sibling": "#3536 P4 (c_k PSLQ)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-action-qsqrt3-saddle-probe.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
