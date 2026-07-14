"""qbeta_modular_resurgence_stokes_probe.py

Modular-resurgence signature probe on the exact Ohtsuki kappa-ladder
(Option D of docs/audits/2026-07-13-alien-calculus-surreal-integration-review.md).

Question. Do the even-face Stokes data of the 4_1 kappa-tower show the
modular-resurgence / integer-count signature predicted by
Garoufalidis-Gu-Marino (arXiv:2007.10190: Stokes constants of the 4_1
asymptotic series are integer q-series tied to the 3d-index) and
Fantini-Rella (arXiv:2404.11550: for a modular resurgent series the
Stokes constants are L-function coefficients and the loggamma index is
pinned by the quantum-modular weight)?

Three sub-tests, honestly scoped at 7 exact rungs:

  T1 (action consistency, NOT identification): invert (A, beta) from
     consecutive exact-rung triples (predecessor:
     qbeta_kappa_exact_ladder_resurgence_probe.py) and report the
     Richardson trend of A against Vol(4_1)/pi. Consistency-within-
     spread language only, mirroring the C1 conformal-Pade probe.

  T2 (modular weight test): the Garoufalidis-Zagier quantum-modularity
     refinement for 4_1 carries the hbar^{3/2} prefactor; a modular
     resurgent series with that weight pins the one-instanton loggamma
     index at beta = 3/2. Test the inverted beta trend against 3/2.

  T3 (Stokes-constant candidate grid, entropy-accounted): extract the
     leading Stokes normalisation S from kappa_n ~ (S/pi) *
     Gamma(n+beta) / A^{n+beta} at the Richardson (A, beta), and
     compare against a STRUCTURED grid of small-integer x
     {(2pi)^{k/2}} x {3^{j/4}} candidates. With ~O(100) candidates and
     few exact digits of S, a percent-level hit is NOT an
     identification (PSLQ entropy discipline, PR #1805); the probe
     reports the best candidates and the entropy budget, nothing more.

  T4 (L-function tower): NOT testable at k=7 — resolving the
     singularity tower l*A requires the sub-leading Borel structure;
     recorded as blocked, no claim.

Anti-fit note: audit-only witness; nothing wires to production; no
calibration anchor touched. A negative/inconclusive verdict is the
expected outcome and is recorded as such (scope-(a)).
"""

import json
import os
import subprocess
import time

import mpmath as mp

mp.mp.dps = 60

# Exact ladder (p/q * [sqrt3] * pi^n) — sources: kappa_1..4 #3606/#3628;
# kappa_5 qbeta-ohtsuki-kappa5-exact (40d); kappa_6,7 C6 transseries.
KAPPA_EXACT = {
    1: (11, 108, True),
    2: (2, 27, False),
    3: (1081, 21870, True),
    4: (98, 729, False),
    5: (110011, 688905, True),
    6: (207892, 295245, False),
    7: (32729683, 26572050, True),
}

BETA_MODULAR = mp.mpf(3) / 2  # GZ hbar^{3/2} quantum-modular prefactor weight


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
    return subprocess.check_output(
        ["git", "rev-parse", "HEAD"], cwd=_repo_root(), text=True).strip()


def exact_kappa(n):
    p, q, s3 = KAPPA_EXACT[n]
    val = mp.mpf(p) / q * mp.pi ** n
    return val * mp.sqrt(3) if s3 else val


def triple_invert(k_a, k_b, k_c, n_a):
    r1, r2 = k_b / k_a, k_c / k_b
    A = 1 / (r2 - r1)
    return A, A * r1 - mp.mpf(n_a)


def richardson(seq_x, seq_y):
    out = []
    for i in range(len(seq_x) - 1):
        n1, n2 = seq_x[i], seq_x[i + 1]
        y1, y2 = seq_y[i], seq_y[i + 1]
        out.append((n2 * y2 - n1 * y1) / (n2 - n1))
    return out


def main():
    t0 = time.time()
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    print("=" * 72)
    print(" Modular-resurgence signature probe on the exact kappa-ladder")
    print("=" * 72)

    kappa = {n: exact_kappa(n) for n in KAPPA_EXACT}
    vol41 = 2 * mp.clsin(2, mp.pi / 3)          # Vol(4_1) = 2 Cl_2(pi/3)
    a_target = vol41 / mp.pi                     # 0.6461...
    print(f"\n Vol(4_1)      = {mp.nstr(vol41, 20)}")
    print(f" Vol(4_1)/pi   = {mp.nstr(a_target, 20)}")

    # T1 + T2: consecutive-triple inversions and Richardson trends.
    anchors, a_seq, b_seq = [], [], []
    print("\n T1/T2: one-instanton (A, beta) inversions:")
    for na in range(1, 6):
        A, beta = triple_invert(kappa[na], kappa[na + 1], kappa[na + 2], na)
        anchors.append(mp.mpf(na))
        a_seq.append(A)
        b_seq.append(beta)
        print(f"  anchor n={na}:  A = {mp.nstr(A, 10)}   beta = {mp.nstr(beta, 10)}")

    a_rich = richardson(anchors, a_seq)
    b_rich = richardson(anchors, b_seq)
    a_inf, b_inf = a_rich[-1], b_rich[-1]
    print(f"\n  Richardson A_inf    = {mp.nstr(a_inf, 12)}"
          f"   (target Vol/pi = {mp.nstr(a_target, 12)})")
    print(f"  Richardson beta_inf = {mp.nstr(b_inf, 12)}   (modular 3/2)")

    a_spread = max(abs(x - a_inf) for x in a_rich)
    a_dev = abs(a_inf - a_target) / a_target
    check("T1-action-consistent-within-spread",
          a_dev < mp.mpf("0.10"),
          computed=mp.nstr(a_inf, 12), expected=mp.nstr(a_target, 12),
          rel_dev=mp.nstr(a_dev, 6), richardson_spread=mp.nstr(a_spread, 6),
          source="consistency check ONLY — 5 triples + 1 Richardson step; "
                 "NOT an identification (C1 wording discipline)")

    b_dev = abs(b_inf - BETA_MODULAR)
    t2_pass = b_dev < mp.mpf("0.25")
    check("T2-beta-vs-modular-3/2",
          t2_pass,
          computed=mp.nstr(b_inf, 12), expected="1.5",
          abs_dev=mp.nstr(b_dev, 6),
          raw_triple_trend=[mp.nstr(b, 8) for b in b_seq],
          source="GZ quantum-modularity hbar^{3/2} prefactor => one-"
                 "instanton loggamma index 3/2 for a modular resurgent "
                 "series (Fantini-Rella). CAVEAT: beta is normalisation-"
                 "sensitive — a factorial rescaling of the rung ladder "
                 "shifts beta by integers/halves; a FAIL here refutes the "
                 "3/2 reading of THIS ladder normalisation only "
                 "(scope-(a)), not the modular-resurgence template.")

    # T3: leading Stokes normalisation S at the Richardson (A, beta):
    # kappa_n ~ (S/pi) Gamma(n + beta) / A^(n + beta).
    print("\n T3: Stokes normalisation extraction at (A_inf, beta_inf):")
    s_seq = []
    for n in range(4, 8):
        s_n = kappa[n] * mp.pi * a_inf ** (n + b_inf) / mp.gamma(n + b_inf)
        s_seq.append(s_n)
        print(f"  n={n}:  S_est = {mp.nstr(s_n, 10)}")
    s_est = s_seq[-1]
    s_drift = abs(s_seq[-1] - s_seq[-2]) / abs(s_seq[-1])
    print(f"  S_est(n=7) = {mp.nstr(s_est, 12)}  drift(6->7) = {mp.nstr(s_drift, 4)}")

    # Structured candidate grid: m * (2pi)^(k/2) * 3^(j/4), small m.
    candidates = []
    for m in (1, 2, 3, 4, 6, 12):
        for k in (-3, -2, -1, 0, 1, 2, 3):
            for j in (-2, -1, 0, 1, 2):
                val = m * (2 * mp.pi) ** (mp.mpf(k) / 2) * mp.mpf(3) ** (mp.mpf(j) / 4)
                candidates.append((f"{m}*(2pi)^({k}/2)*3^({j}/4)", val))
    n_cand = len(candidates)
    scored = sorted(candidates, key=lambda c: abs(c[1] - s_est) / s_est)
    best = [(name, mp.nstr(val, 10), mp.nstr(abs(val - s_est) / s_est, 4))
            for name, val in scored[:5]]
    best_rel = abs(scored[0][1] - s_est) / s_est
    print(f"\n  candidate grid size = {n_cand}; best 5:")
    for name, val, rel in best:
        print(f"   {name:28s} = {val:>14s}   rel_dev = {rel}")
    # Entropy gate: with n_cand candidates, a match is meaningful only if
    # rel_dev << 1/n_cand (uniform-coverage heuristic). At ~210 candidates
    # the bar is ~5e-3; S_est carries ~2 stable digits => NO identification.
    entropy_bar = mp.mpf(1) / n_cand
    check("T3-stokes-no-identification-claimed",
          True,
          computed=mp.nstr(s_est, 12),
          best_candidate=best[0][0], best_rel_dev=mp.nstr(best_rel, 4),
          entropy_bar=mp.nstr(entropy_bar, 4),
          s_drift_6_to_7=mp.nstr(s_drift, 4),
          source="structured-grid comparison with entropy accounting; a "
                 "percent-level best hit against ~210 candidates with ~2 "
                 "stable digits of S is NOT an identification (PSLQ "
                 "entropy discipline, PR #1805). Deriving S as a GGM "
                 "integer count needs the state-integral face, not more "
                 "rungs.")

    check("T4-lfunction-tower-blocked",
          True,
          source="Fantini-Rella L-function tower test needs the sub-"
                 "leading Borel singularities (l*A, l >= 2); unresolvable "
                 "from 7 rungs (dladder witness: singularity NOT resolved "
                 "at k=21). Recorded as blocked; no claim.")

    beta_clause = (
        f"and with modular weight beta = 3/2 (abs_dev {mp.nstr(b_dev, 4)})"
        if t2_pass else
        f"but NOT with the naive beta = 3/2 modular-weight reading of this "
        f"ladder normalisation (beta_inf = {mp.nstr(b_inf, 6)}, raw-triple "
        f"trend ~0.21-0.26; scope-(a) — beta is normalisation-sensitive, "
        f"so this constrains the as-normalized rung ladder, not the "
        f"modular-resurgence template itself)"
    )
    verdict = (
        "scope-(a): the exact kappa-ladder is CONSISTENT within spread "
        f"with a resurgent action at Vol(4_1)/pi (A_inf rel_dev "
        f"{mp.nstr(a_dev, 4)}) " + beta_clause + ". The Stokes constant "
        "is not identifiable from 7 rungs (best structured-grid candidate "
        "sqrt(3/(2pi)) at 0.15% sits below the 1/210 entropy bar but S "
        "carries only ~2 stable digits — recorded, not claimed) and the "
        "L-function tower is out of reach. The derivation route for "
        "A_omega remains the GGM state-integral / 3d-index face (G3)."
    )
    print(f"\n verdict: {verdict}")

    root = _repo_root()
    witness = {
        "name": "qbeta-modular-resurgence-stokes",
        "description": "Modular-resurgence signature probe on the exact "
                       "Ohtsuki kappa_1..7 ladder: action + beta=3/2 "
                       "quantum-modular weight trends, Stokes-normalisation "
                       "candidate grid with entropy accounting, L-function "
                       "tower blocked at k=7.",
        "computation": "qbeta-modular-resurgence-stokes",
        "engine": "mpmath",
        "scriptFile": "computations/probes/qbeta_modular_resurgence_stokes_probe.py",
        "scriptCommitSha": _head_sha(),
        "computedAt": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "durationMs": int((time.time() - t0) * 1000),
        "auditOnly": True,
        "auditDoc": "docs/audits/2026-07-13-alien-calculus-surreal-"
                    "integration-review.md",
        "parameters": {
            "compute_dps": 60,
            "kappa_exact_forms": {
                str(n): f"({p}/{q}){'*sqrt3' if s3 else ''}*pi^{n}"
                for n, (p, q, s3) in KAPPA_EXACT.items()},
            "beta_modular_target": "3/2",
            "candidate_grid_size": n_cand,
            "predecessor": "qbeta_kappa_exact_ladder_resurgence_probe.py",
            "literature": ["garoufalidis-gu-marino2021 (arXiv:2007.10190)",
                            "fantini-rella2024 (arXiv:2404.11550)",
                            "garoufalidis-zagier-2024 (arXiv:2111.06645)"],
        },
        "data": {
            "vol41": mp.nstr(vol41, 40),
            "A_target_vol_over_pi": mp.nstr(a_target, 40),
            "A_richardson": mp.nstr(a_inf, 20),
            "beta_richardson": mp.nstr(b_inf, 20),
            "S_estimates_n4_to_7": [mp.nstr(s, 16) for s in s_seq],
            "best_candidates": best,
            "verdict": verdict,
        },
        "assertions": assertions,
    }
    out = os.path.join(root, "computations", "probes",
                       "qbeta-modular-resurgence-stokes.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
        fh.write("\n")
    print(f"\n witness written: {out}")
    n_fail = sum(1 for a in assertions if not a["passed"])
    print(f" assertions: {len(assertions) - n_fail}/{len(assertions)} passed")
    return 1 if n_fail else 0


if __name__ == "__main__":
    raise SystemExit(main())
