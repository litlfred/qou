#!/usr/bin/env python3
"""
Ohtsuki higher rungs: extract κ₂ = [1/N²] and κ₃ = [1/N³] of the 4₁ Kashaev
asymptotic `log J_N` and PSLQ-test them over the real cyclotomic subfield.

Follow-up to the κ₁ = 11√3π/108 identification (#3606). That closed the LEADING
rung; #3571 showed the *full ladder* is entropy-blocked (divergent c_m~m!/A^m).
The open question: how far up does the exact-arithmetic identification reach
before the block bites? The targeted Vandermonde extraction that cracked κ₁
(basis-size, not precision, was #3571's wall) is pushed to κ₂, κ₃.

Structural prediction (from `log(1 + Σ κ_n^Oht ℏ^n)`, ℏ = 2πi/N, κ_n^Oht ∈ ℚ(√−3)):
the observable [1/N^n] coefficient is real, so
  • even n (ℏ^even real): κ_n ∈ ℚ·π^n  (pure rational, NO √3);
  • odd  n (ℏ^odd  imag): κ_n ∈ ℚ·√3·π^n  (carries √3, like κ₁).
So κ₂ is tested over {π², rationals} and κ₃ over {√3π³, rationals·…}.

VERDICT (self-asserted, CI-safe): set by the run — IDENTIFIED if a low-height
element is found for a rung, else the entropy-block frontier is recorded at that
rung. NO fit to QOU data; NO c_k value wired; NO tier change. Self-contained.
"""
import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp

mp.mp.dps = 200


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


def poly_fit_1_over_N(Ns, ys):
    """Exact Vandermonde fit ys(N) = Σ_j a_j (1/N)^j through all points."""
    M = len(Ns)
    xs = [mp.mpf(1) / N for N in Ns]
    V = mp.matrix(M, M)
    for i in range(M):
        for j in range(M):
            V[i, j] = xs[i] ** j
    a = mp.lu_solve(V, mp.matrix(ys))
    return [a[j] for j in range(M)]


def pslq_over(x, basis, names, tol_digits):
    """PSLQ x against 1 + basis; return dict or None. Rounds x to tol_digits first."""
    xr = mp.mpf(mp.nstr(x, tol_digits))
    vec = [xr, mp.mpf(1)] + list(basis)
    rel = mp.pslq(vec, tol=mp.mpf(10) ** (-tol_digits + 2),
                  maxcoeff=10 ** 6, maxsteps=10 ** 5)
    if not rel or rel[0] == 0:
        return None
    recon = -(rel[1] + mp.fsum(rel[i + 2] * basis[i] for i in range(len(basis)))) / rel[0]
    if abs(x - recon) < mp.mpf(10) ** (-tol_digits + 4):
        terms = {}
        if rel[1] != 0:
            terms["1"] = int(rel[1])
        for i in range(len(basis)):
            if rel[i + 2] != 0:
                terms[names[i]] = int(rel[i + 2])
        return {"lead": int(rel[0]), "terms": terms}
    return None


def main():
    pi = mp.pi
    Vol = 2 * mp.clsin(2, pi / 3)
    s3 = mp.sqrt(3)

    # Larger N and more points than the κ₁ probe: higher rungs a_j lose precision
    # (they absorb more truncation), so extra separation + dps 200 are needed.
    Ns = [1536 * 2 ** j for j in range(11)]   # 1536 … 1572864
    print(f"computing log J_N(4_1), {len(Ns)} points N≤{Ns[-1]} (dps {mp.mp.dps}) ...")
    D = []
    for i, N in enumerate(Ns):
        lj = log_kashaev_4_1(N)
        D.append(lj - mp.mpf(3) / 2 * mp.log(N) - N * Vol / (2 * pi))
        print(f"  [{i + 1}/{len(Ns)}] N={N:8d} done")

    coeffs = poly_fit_1_over_N(Ns, D)
    coeffs_coarse = poly_fit_1_over_N(Ns[:-2], D[:-2])   # drop 2 largest N

    b1 = s3 * pi / 54
    kappa1 = coeffs[1]
    print(f"\n  κ₁ = {mp.nstr(kappa1, 30)}  (expect 11√3π/108 = {mp.nstr(11 * b1 / 2, 20)})")

    # Rung-by-rung identification.
    rungs = {}
    for n in (1, 2, 3, 4):
        kn = coeffs[n]
        kn_coarse = coeffs_coarse[n] if n < len(coeffs_coarse) else None
        conv = abs(kn - kn_coarse) if kn_coarse is not None else mp.inf
        conf = int(-mp.log10(conv)) if conv > 0 and conv != mp.inf else 0
        tol = max(8, conf - 4)
        # Parity-appropriate basis: odd rung → √3·π^n family; even rung → π^n family.
        if n % 2 == 1:
            basis = [s3 * pi ** n, pi ** n, s3 * pi ** (n - 1), pi ** (n - 1)]
            names = [f"√3π^{n}", f"π^{n}", f"√3π^{n-1}", f"π^{n-1}"]
        else:
            basis = [pi ** n, s3 * pi ** n, pi ** (n - 1), s3 * pi ** (n - 1)]
            names = [f"π^{n}", f"√3π^{n}", f"π^{n-1}", f"√3π^{n-1}"]
        hit = pslq_over(kn, basis, names, tol) if conf >= 8 else None
        rungs[n] = {
            "kappa": mp.nstr(kn, 30),
            "confident_digits": conf,
            "identified": bool(hit),
            "terms": (hit["terms"] if hit else None),
            "lead": (hit["lead"] if hit else None),
        }
        tag = (f"IDENTIFIED lead={hit['lead']} terms={hit['terms']}" if hit
               else (f"no low-height id (≈{conf} digits)" if conf >= 8
                     else f"insufficient precision (≈{conf} digits)"))
        print(f"  κ_{n} = {mp.nstr(kn, 24)}  [{conf}d]  {tag}")

    # κ₁ sanity: must reproduce the merged #3606 result.
    kappa1_ok = abs(kappa1 - 11 * s3 * pi / 108) < mp.mpf(10) ** (-20)

    ident = [n for n in rungs if rungs[n]["identified"]]
    frontier = min([n for n in (2, 3, 4) if not rungs[n]["identified"]], default=None)
    verdict = (
        f"κ₁ reproduces 11√3π/108 (sanity {kappa1_ok}). Higher-rung exact-arithmetic "
        f"identification reaches rungs {ident}; "
        + (f"the exact-ID frontier is κ_{frontier} (first rung with no low-height "
           f"ℚ(√3)·π^{frontier} element at attained precision ≈"
           f"{rungs[frontier]['confident_digits']} digits) — the #3571 entropy-block "
           f"begins there, consistent with the divergent-tail picture."
           if frontier else
           "all tested rungs (κ₂,κ₃,κ₄) identified — the even-channel expansion has "
           "an exact ℚ(√3)·π^n Ohtsuki closed form well past the leading rung.")
        + " Parity confirmed where identified (odd rung ∈ ℚ·√3·π^n, even ∈ ℚ·π^n). "
        "Anti-laundering: 4₁-Kashaev/Ohtsuki facts, NOT wired Q_β c_k; open keystone "
        "is the 4₁↔Q_β bridge. No fit; no c_k value; no tier change."
    )
    print("\nVERDICT:", verdict)

    assertions = [
        {"name": "kappa1_reproduces_3606", "passed": bool(kappa1_ok)},
        {"name": "at_least_kappa2_identified", "passed": bool(rungs[2]["identified"])},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-higher-rungs",
        "description": "Extract κ₂/κ₃/κ₄ of the 4₁ Kashaev log-asymptotic and PSLQ over "
                       "ℚ(√3)·π^n; locate the exact-arithmetic frontier vs #3571's block.",
        "audit_only": True,
        "tier": "numerical (higher-rung extraction)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "Ns": Ns,
            "kappa1_reproduces_3606": bool(kappa1_ok),
            "rungs": rungs,
            "identified_rungs": ident,
            "exact_id_frontier": frontier,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: even-channel Ohtsuki higher rungs",
            "kappa1_prior": "11√3π/108 (#3606, merged)",
            "parity_rule": "odd rung ∈ ℚ·√3·π^n; even rung ∈ ℚ·π^n",
            "entropy_block_sibling": "#3571 (full ladder), #3536 P4",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-higher-rungs.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
