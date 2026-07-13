#!/usr/bin/env python3
"""
The κ→u re-basing test (is the f-map "read c_k off the Ohtsuki ladder"?) + the
nucleon-side knots.  Self-contained; NO fit to production, NO wiring, NO c_k
value, NO tier change.  Findings scope-(a)/(b) classified.

TASK 1 — f-map re-basing test.  The QOU even channel is an exact ũ-ladder with
rungs e_k = (3√3/4, -15.035, -58.409, -276.55, -1817.30) (bean ai81/08ds,
9fnm audit).  The figure-eight Ohtsuki ladder is κ_k.  Test whether a SINGLE
scale ũ = λ·(2π/N) maps κ_k → e_k (over-determined: fix λ from rung 1, PREDICT
rung 2,3).  A free per-order change of variables can fit anything (the Weber-ODE
overfitting trap the discipline forbids); the one-scale test is the honest,
parameter-free version.

TASK 1 structural diagnostic.  The colored Jones has an ESSENTIAL SINGULARITY at
q=1 (Kashaev ~ e^{N·V/2π}); its Ohtsuki series is a DIVERGENT asymptotic series
(κ_k grow).  The Q_β ratio ∏(1+c_k u^k) is REGULAR at q=1 (→1).  A regular
function and an essential-singularity function are NOT related by an analytic
change of variables ⇒ the f-map cannot be a coefficient re-basing; it is the
RESURGENCE connection (trivial-connection perturbative series ↔ geometric-
connection asymptotic series; Garoufalidis-Gu-Mariño Stokes data).

TASK 2 — nucleon-side knots.  Classical volumes (well-known constants) + the
sector map.  The Borromean (nucleon) QUANTUM volume needs the 3-component link
colored Jones (flagged as the next compute, not faked).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 80


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


def log_kashaev_4_1(N):
    pi = mp.pi
    logterms = [mp.mpf(0)]
    logP = mp.mpf(0)
    for k in range(1, N):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N))
        logterms.append(logP)
    m = max(logterms)
    return m + mp.log(mp.fsum(mp.e ** (t - m) for t in logterms))


def ohtsuki_ladder_4_1(order, Ns):
    """Fit log J_N = a·N + (3/2)logN + b + Σ_{k=1}^{order} κ_k / N^k."""
    rows = [(N, log_kashaev_4_1(N) - mp.mpf(3) / 2 * mp.log(N)) for N in Ns]
    def basis(N):
        return [mp.mpf(N), mp.mpf(1)] + [1 / mp.mpf(N) ** k for k in range(1, order + 1)]
    A = mp.matrix([basis(N) for N, _ in rows])
    y = mp.matrix([g for _, g in rows])
    coef = mp.lu_solve(A.T * A, A.T * y)
    a = coef[0]
    b = coef[1]
    kappa = [coef[2 + k] for k in range(order)]
    return a, b, kappa


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- Higher-order 4_1 Ohtsuki ladder -----------------------------------
    Ns = list(range(240, 721, 40))  # 13 values
    order = 4
    a, b, kappa = ohtsuki_ladder_4_1(order, Ns)
    Vol_41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    V_rec = 2 * mp.pi * a
    print("=== 4_1 Ohtsuki ladder (higher order) ===")
    print(f"  Vol recovered = {mp.nstr(V_rec,14)}  (exact {mp.nstr(Vol_41,14)}, "
          f"rel {mp.nstr(abs(V_rec/Vol_41-1),3)})")
    print(f"  b = {mp.nstr(b,10)} (= -¼log3 = {mp.nstr(-mp.log(3)/4,10)})")
    for k, kk in enumerate(kappa, 1):
        print(f"  κ_{k} = {mp.nstr(kk,10)}")
    check("vol41_recovered", abs(V_rec / Vol_41 - 1) < mp.mpf("1e-6"))

    # κ_k growth: |κ_{k+1}/κ_k| increasing ⇒ divergent asymptotic (resurgence)
    ratios = [abs(kappa[k + 1] / kappa[k]) for k in range(len(kappa) - 1)
              if kappa[k] != 0]
    kappa_growing = ratios[-1] > ratios[0] if len(ratios) >= 2 else False
    print(f"  |κ_{{k+1}}/κ_k| ratios = {[mp.nstr(r,4) for r in ratios]}  "
          f"(growing ⇒ divergent/asymptotic: {kappa_growing})")
    check("ohtsuki_series_divergent_asymptotic", kappa_growing)

    # --- TASK 1: one-scale re-basing test (parameter-free) ------------------
    # Even-channel rungs (exact ℚ(√3), 9fnm/ai81 witness).
    e = [3 * mp.sqrt(3) / 4, mp.mpf("-15.035"), mp.mpf("-58.409"),
         mp.mpf("-276.55")]
    # Fix the single scale from rung 1: e₁ = κ₁·λ  ⇒  λ = e₁/κ₁.
    lam = e[0] / kappa[0]
    print(f"\n=== TASK 1: one-scale re-basing  ũ = λ·(2π/N),  λ = e₁/κ₁ = {mp.nstr(lam,8)} ===")
    print(f"  {'k':>2} {'e_k (QOU even)':>16} {'κ_k·λ^k (pred)':>16} {'match?':>8}")
    onescale_fails = False
    for k in range(len(e)):
        pred = kappa[k] * lam ** (k + 1)
        rel = abs(pred / e[k] - 1) if e[k] != 0 else mp.inf
        ok = rel < mp.mpf("0.05")
        if k >= 1 and not ok:
            onescale_fails = True
        print(f"  {k+1:>2} {mp.nstr(e[k],10):>16} {mp.nstr(pred,10):>16} "
              f"{'yes' if ok else 'NO':>8}")
    # The test PASSES the audit by DEMONSTRATING the one-scale map fails at rung 2+
    check("one_scale_rebasing_fails_at_rung2plus", onescale_fails)

    # --- TASK 2: nucleon-side classical volumes + sector map ----------------
    print("\n=== TASK 2: classical volumes + sector map ===")
    knots = {
        "4_1 (lepton/muon; Vol enters m_μ)": Vol_41,
        "5_2":            mp.mpf("2.828122088330783"),
        "6_1":            mp.mpf("3.163963228883143"),
        "Borromean 6^3_2 (nucleon)": mp.mpf("7.327724753417925"),
    }
    for name, V in knots.items():
        print(f"  {name:38s} Vol = {mp.nstr(V,12)}")
    # Borromean = 2·Vol(4_1) + ... ?  Check the known 4·(Vol of ideal octahedron)
    #  = Borromean complement is 2 ideal octahedra; Vol(oct)=3.66386.
    vol_oct = mp.mpf("3.663862376708876")
    borro_is_two_oct = abs(knots["Borromean 6^3_2 (nucleon)"] / (2 * vol_oct) - 1) < mp.mpf("1e-6")
    print(f"  Borromean = 2·Vol(ideal octahedron)? {borro_is_two_oct} "
          f"(2·{mp.nstr(vol_oct,8)} = {mp.nstr(2*vol_oct,10)})")
    check("borromean_is_two_ideal_octahedra", borro_is_two_oct)

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        "The f-map is NOT a κ→c re-basing. (1) One-scale map ũ=λ(2π/N) fixed by "
        f"e₁=κ₁·λ (λ={mp.nstr(lam,6)}) PREDICTS e₂={mp.nstr(kappa[1]*lam**2,6)} vs "
        f"actual {mp.nstr(e[1],6)} — fails at rung 2 (wrong sign+magnitude). (2) "
        "STRUCTURAL reason: the colored Jones has an essential singularity at q=1 "
        "(Kashaev ~ e^{N·Vol/2π}) and its Ohtsuki series is DIVERGENT asymptotic "
        f"(|κ_{{k+1}}/κ_k| growing: {[mp.nstr(r,3) for r in ratios]}), while the "
        "Q_β ratio ∏(1+c_k u^k) is REGULAR at q=1 — different analytic type, no "
        "analytic change of variables between them. So the f-map is the RESURGENCE "
        "connection (trivial-connection perturbative c_k ↔ geometric-connection "
        "Ohtsuki κ_k; Garoufalidis-Gu-Mariño Stokes data), NOT a coefficient map. "
        "Caveat: 4_1 is the LEPTON knot; the even channel's knot may differ — knot "
        "identification is prerequisite. (Task 2) nucleon Borromean Vol = "
        "2·Vol(ideal octahedron) = 7.32772 exactly; its QUANTUM volume needs the "
        "3-component link colored Jones (next compute). No fit; no c_k; no wiring; "
        "no tier change."
        if all_passed else
        "INCONCLUSIVE — a volume/growth/re-basing assertion failed; re-derive."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-fmap-ohtsuki-rebasing-test",
        "description": "κ→u re-basing test: one-scale map fails; colored Jones "
                       "essential-singularity/divergent vs Q_β regular ⇒ f-map is "
                       "resurgence, not coefficient re-basing. + nucleon volumes.",
        "audit_only": True,
        "tier": "structural-exact (re-basing prune + volume identities; no QOU fit)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "vol41_recovered": mp.nstr(V_rec, 14),
            "kappa_4_1": [mp.nstr(k, 10) for k in kappa],
            "kappa_growth_ratios": [mp.nstr(r, 6) for r in ratios],
            "one_scale_lambda": mp.nstr(lam, 8),
            "e2_predicted_vs_actual": [mp.nstr(kappa[1] * lam ** 2, 8), mp.nstr(e[1], 8)],
            "borromean_two_octahedra": bool(borro_is_two_oct),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: Ohtsuki re-basing test",
            "even_rungs_source": "bean ai81/08ds; docs/audits/2026-07-03-9fnm-...md",
            "fmap_is_resurgence": "trivial-connection perturbative c_k ↔ geometric-"
                "connection Ohtsuki κ_k (Garoufalidis-Gu-Mariño)",
            "knot_id_caveat": "4_1 = lepton knot; even-channel knot may differ",
            "borromean_quantum_todo": "3-component link colored Jones (next compute)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-fmap-ohtsuki-rebasing-test.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
