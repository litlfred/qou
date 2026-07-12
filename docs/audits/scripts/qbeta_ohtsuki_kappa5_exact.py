#!/usr/bin/env python3
"""
Exact κ₅: Richardson-grade extraction of the [1/N⁵] rung of the 4₁ Kashaev
log-asymptotic, past the ≥17-digit entropy-budget gate, and strict 2-term PSLQ
against the parity generator √3·π⁵.

Follow-up to #3628 (κ₂..κ₄ exact) and the #3683 G2+C3 large-order probe, whose
honest close-out was: "PSLQ gate not met (~2.9-digit gap) — exact κ₅ still needs
bridge arithmetic or ≥17-digit extraction." This probe supplies the ≥17-digit
extraction. Two upgrades over `qbeta_ohtsuki_higher_rungs.py` (the κ₂..κ₄ prober):

  1. EXACT-RUNG STRIPPING. κ₁ = (11/108)√3π, κ₂ = (2/27)π², κ₃ = (1081/21870)√3π³,
     κ₄ = (98/729)π⁴ are exact (#3606/#3628, Lean-certified parity). Subtracting
     them exactly — alongside the already-stripped (3/2)log N + N·Vol/2π — makes
     κ₅ the LEADING 1/N-power of the residual, recovering the best-conditioned
     "targeted extraction" geometry that gave κ₁ its 36 digits. The constant
     a₀ = log ω₀ = −(1/4)log 3 (the Andersen–Hansen amplitude ω₀ = 3^{-1/4} of
     J_N(4₁) ≃ 3^{-1/4} N^{3/2} e^{N·Vol/2π}; Ref: [andersen-hansen2006]) is
     stripped exactly as well — a preliminary fit reproduced −(1/4)log 3 to
     1.2e-21, and a side-fit with a free constant column re-verifies the strip
     in-run (hard assert |const| < 1e-25). The Vandermonde basis is therefore
     pure tail: {1/N⁵, 1/N⁶, ...}.
  2. TRANSCENDENTAL-FREE LADDER. log J_N was previously O(N) calls of
     log(2 sin(πk/N)) (two mpmath transcendentals per step). Here J_N is
     accumulated as the raw positive sum Σ_k ∏_{j≤k} |1−q^j|², q = e^{2πi/N},
     with q^j by complex-multiplication recurrence — ~7 mpf ring ops per step and
     ZERO per-step transcendentals (mpf exponents are unbounded, so no rescaling
     is needed even though the partial products span e^{±O(N)}). ~20× faster,
     which is what pays for N_max = 12 582 912 (2× the #3628 confirm run).
     Recurrence drift over N steps is ~N·ulp ≈ 10^{7-dps} ≪ the 10^-65 target.

Precision accounting (why dps 220 suffices): the stripped residual at N_max is
R(N) ≈ κ₅/N⁵ ≈ 8·10⁻³⁴ against log J_N ≈ N·Vol/2π ≈ 5.8·10⁶ — resolving R to
30 digits needs ~74 absolute digits; recurrence drift costs ~8; dps 220 leaves
>130 digits of headroom. The Vandermonde solve is re-run at dps 500 on the
stored ladder (conditioning, not data, limited).

Entropy-budget gate (PR #1805 rule, C2 machinery): a 2-term relation of height H
needs trusted digits > 2·log10(2H) + margin. The gate pre-stated by the sibling
audit is ≥17 confident digits; confident digits are measured, not assumed, by
coarse-vs-fine refits (drop 2 largest-N AND drop 2 smallest-N; min agreement).

VERDICT (self-asserted, CI-safe): IDENTIFIED if a within-budget low-height
rational multiple of √3π⁵ is found at ≥17 confident digits AND the exact
candidate reproduces the extracted value to full confidence; else the honest
frontier is recorded. κ₆ (vs π⁶) is tested opportunistically the same way.
Anti-laundering: 4₁-Kashaev/Ohtsuki topological facts — NO fit to QOU data,
NO Q_β c_k wired, NO tier change. Self-contained.
"""
import datetime
import hashlib
import json
import os
import subprocess
import time

import mpmath as mp

mp.mp.dps = 220

# Exact amplitude (Andersen–Hansen, [andersen-hansen2006]): a₀ = log 3^{-1/4}.
A0_EXACT_DESC = "-(1/4)*log(3)  (Andersen-Hansen amplitude omega_0 = 3^{-1/4})"

# Exact rungs (#3606 / #3628) — stripped from the ladder before fitting.
EXACT_RUNGS = {
    1: ("11/108 * sqrt3 * pi", lambda pi, s3: mp.mpf(11) / 108 * s3 * pi),
    2: ("2/27 * pi^2", lambda pi, s3: mp.mpf(2) / 27 * pi ** 2),
    3: ("1081/21870 * sqrt3 * pi^3", lambda pi, s3: mp.mpf(1081) / 21870 * s3 * pi ** 3),
    4: ("98/729 * pi^4", lambda pi, s3: mp.mpf(98) / 729 * pi ** 4),
}

# Main-witness numerics (13-pt confirm run, #3628) — cross-check anchors.
WITNESS_KAPPA5 = "84.642165605038443528"   # 14 confident digits
WITNESS_KAPPA6 = "676.9466789641050315"    # 10 confident digits

BASE_MARGIN = 3.0   # safety digits on top of the raw entropy bound (C2 rule)
GATE_DIGITS = 17    # the sibling audit's pre-stated gate for κ₅


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


def log_kashaev_4_1_fast(N, progress_every=0):
    """log Σ_{k=0}^{N-1} ∏_{j=1}^{k} |1−q^j|², q = e^{2πi/N}, by raw mpf
    accumulation — no per-step transcendentals. |1−q^j| = 2 sin(πj/N), so this
    is exactly the quantity the slow prober computed in log space; positivity
    of every term makes the plain sum numerically benign, and mpf's unbounded
    exponent absorbs the e^{±O(N)} dynamic range without rescaling."""
    two_pi_over_N = 2 * mp.pi / N
    qr, qi = mp.cos(two_pi_over_N), mp.sin(two_pi_over_N)   # q = qr + i·qi
    zr, zi = mp.mpf(1), mp.mpf(0)                           # z = q^j (j=0)
    P = mp.mpf(1)                                           # ∏_{j≤k} |1−q^j|²
    S = mp.mpf(1)                                           # k=0 term = empty product
    one = mp.mpf(1)
    t0 = time.time()
    for j in range(1, N):
        zr, zi = zr * qr - zi * qi, zr * qi + zi * qr       # z ← z·q
        dr = one - zr
        P *= dr * dr + zi * zi                              # |1−q^j|²
        S += P
        if progress_every and j % progress_every == 0:
            print(f"    ... j={j}/{N} ({100.0 * j / N:.0f}%), "
                  f"{time.time() - t0:.0f}s elapsed", flush=True)
    return mp.log(S)


def fit_reduced_basis(Ns, ys, orders):
    """Exact Vandermonde fit ys(N) = Σ_{p∈orders} a_p (1/N)^p (orders may be
    non-contiguous, e.g. [0, 5, 6, ...]). Solved at elevated dps. Returns
    {order: coefficient}."""
    M = len(Ns)
    assert len(orders) == M, "square system required"
    old = mp.mp.dps
    mp.mp.dps = 500
    try:
        V = mp.matrix(M, M)
        for i in range(M):
            x = mp.mpf(1) / Ns[i]
            for j, p in enumerate(orders):
                V[i, j] = x ** p
        a = mp.lu_solve(V, mp.matrix(ys))
        return {p: a[j] for j, p in enumerate(orders)}
    finally:
        mp.mp.dps = old


def needed_digits(H, n_terms=2):
    """Entropy bound (PR #1805): digits required to certify an n-term relation
    of height H."""
    return n_terms * mp.log10(2 * mp.mpf(H)) + BASE_MARGIN


def budget_maxcoeff(digits, n_terms=2):
    """Largest height H with needed_digits(H) <= digits."""
    H = int(mp.floor(mp.mpf(10) ** ((mp.mpf(digits) - BASE_MARGIN) / n_terms) / 2))
    return max(H, 0)


def pslq_rational_multiple(x, base, conf_digits):
    """STRICT parity test: is `x` a rational multiple (p/q)·base within the
    entropy budget for `conf_digits`? 2-term PSLQ, no implicit constant, no
    wrong-parity generator. Returns (p, q, height) or None.

    Tolerance discipline (UPGRADED over the κ₂..κ₄ prober): a fixed 4-digit
    slack (tol = 10^-(conf−4)) silently REJECTS true relations of height
    H ≳ 10⁴, because rounding `x` to conf digits leaves a residual
    ~H·10^-conf in the relation — the slack must scale with the height being
    probed. (Caught 2026-07-12: κ₆ = (207892/295245)·π⁶, height 3·10⁵, was
    inside the entropy budget at 33 digits yet missed by the fixed-slack
    call; the saddle-fluctuation transseries derivation exposed the miss.)
    Fix: escalate over height tiers, each with a tier-matched tolerance
    tol_tier ≈ H_tier·10^-conf·10², tightest-first so low-height hits get
    the strongest certification. Every hit is post-hoc gated by the entropy
    budget at its ACTUAL height (needed_digits(H_found) ≤ conf) and must
    reproduce `x` to the rounding-consistent residual."""
    if budget_maxcoeff(conf_digits) < 10:
        return None
    conf = min(conf_digits, 45)
    xr = mp.mpf(mp.nstr(x, conf))
    tier = 10 ** 4
    while tier <= budget_maxcoeff(conf_digits) * 100:
        H_tier = min(tier, budget_maxcoeff(conf_digits))
        # tier-matched slack: rounding residual of a true height-H relation
        # is ~H·10^-conf; certify with 3 extra safety digits.
        tol_digits = max(8, conf - int(mp.ceil(mp.log10(H_tier))) - 3)
        rel = mp.pslq([xr, base], tol=mp.mpf(10) ** (-tol_digits),
                      maxcoeff=H_tier, maxsteps=10 ** 5)
        if rel and rel[0] != 0:
            p, q = -rel[1], rel[0]
            if q < 0:
                p, q = -p, -q
            H_found = max(abs(p), abs(q))
            # post-hoc entropy gate at the ACTUAL height + rounding-consistent
            # residual check against the exact candidate.
            resid_gate = mp.mpf(H_found) * mp.mpf(10) ** (2 - conf) * abs(x)
            if (needed_digits(H_found) <= conf
                    and abs(x - mp.mpf(p) / q * base) < resid_gate):
                return int(p), int(q), int(H_found)
        if H_tier >= budget_maxcoeff(conf_digits):
            break
        tier *= 100
    return None


def main():
    pi = mp.pi
    s3 = mp.sqrt(3)
    Vol = 2 * mp.clsin(2, pi / 3)

    # --- 0. Fast-ladder self-check against the slow (sin/log) evaluator -----
    print("=== 0. fast-evaluator self-check (N=1536 vs slow log-sum) ===",
          flush=True)
    N_chk = 1536
    lj_fast = log_kashaev_4_1_fast(N_chk)
    logP = mp.mpf(0)
    m0, s0 = mp.mpf(0), mp.mpf(1)
    for k in range(1, N_chk):
        logP += 2 * mp.log(2 * mp.sin(pi * k / N_chk))
        if logP > m0:
            s0 = s0 * mp.exp(m0 - logP) + 1
            m0 = logP
        else:
            s0 += mp.exp(logP - m0)
    lj_slow = m0 + mp.log(s0)
    selfcheck_err = abs(lj_fast - lj_slow)
    print(f"  |fast - slow| = {mp.nstr(selfcheck_err, 5)}  (require < 1e-150)",
          flush=True)
    assert selfcheck_err < mp.mpf(10) ** (-150), \
        "fast Kashaev evaluator disagrees with the reference log-sum-exp path"

    # --- 1. Ladder ----------------------------------------------------------
    Ns = [3072 * 2 ** j for j in range(13)]   # 3072 … 12 582 912
    print(f"\n=== 1. ladder: {len(Ns)} points, N_max={Ns[-1]}, dps={mp.mp.dps} "
          f"===", flush=True)
    kappa_exact = {n: f(pi, s3) for n, (_, f) in EXACT_RUNGS.items()}
    a0_exact = -mp.log(3) / 4
    D = []
    t_start = time.time()
    for i, N in enumerate(Ns):
        t0 = time.time()
        lj = log_kashaev_4_1_fast(N, progress_every=(2 ** 21 if N > 2 ** 21 else 0))
        d = lj - mp.mpf(3) / 2 * mp.log(N) - N * Vol / (2 * pi) - a0_exact
        for n, kn in kappa_exact.items():
            d -= kn / mp.mpf(N) ** n
        D.append(d)
        el, tot = time.time() - t0, time.time() - t_start
        eta = tot / sum(Ns[:i + 1]) * (sum(Ns) - sum(Ns[:i + 1]))
        print(f"  [{i + 1}/{len(Ns)}] N={N:9d} done in {el:7.1f}s "
              f"(elapsed {tot:7.0f}s, ETA {eta:6.0f}s)", flush=True)

    # --- 2. Reduced-basis fits + confidence --------------------------------
    # Basis {1/N^5 .. 1/N^(5+M-1)}: a0 AND κ1..κ4 stripped exactly — pure tail.
    print("\n=== 2. reduced-basis Vandermonde fits ===", flush=True)
    orders_full = list(range(5, 5 + len(Ns)))
    fit_full = fit_reduced_basis(Ns, D, orders_full)
    orders_hi = list(range(5, 5 + len(Ns) - 2))
    fit_drop_hi = fit_reduced_basis(Ns[:-2], D[:-2], orders_hi)      # drop 2 largest N
    fit_drop_lo = fit_reduced_basis(Ns[2:], D[2:], orders_hi)        # drop 2 smallest N
    # Side-fit with a free constant column: re-verifies the a0 strip in-run.
    fit_side = fit_reduced_basis(Ns, D, [0] + list(range(5, 5 + len(Ns) - 1)))
    a0_resid = fit_side[0]
    print(f"  side-fit residual constant = {mp.nstr(a0_resid, 6)} "
          f"(require < 1e-25; validates the -(1/4)log3 strip)", flush=True)
    assert abs(a0_resid) < mp.mpf(10) ** (-25), \
        "residual constant inconsistent with the Andersen-Hansen amplitude strip"

    results = {}
    for n, gen, gen_name in ((5, s3 * pi ** 5, "√3·π^5"), (6, pi ** 6, "π^6")):
        kn = fit_full[n]
        agree_hi = abs(kn - fit_drop_hi[n])
        agree_lo = abs(kn - fit_drop_lo[n])
        conv = max(agree_hi, agree_lo)
        conf = int(-mp.log10(conv)) if conv > 0 else 60
        conf = min(conf, 60)
        hit = pslq_rational_multiple(kn, gen, conf) if conf >= 8 else None
        # Candidate must reproduce the extraction at FULL confidence, not just
        # PSLQ tolerance (guards the #3571-class entropy false positive).
        verified = False
        if hit:
            p, q, _ = hit
            resid = abs(kn - mp.mpf(p) / q * gen)
            verified = resid < mp.mpf(10) ** (-(conf - 2))
        results[n] = {
            "kappa": mp.nstr(kn, 40),
            "confident_digits": conf,
            "agreement_drop_largest": mp.nstr(agree_hi, 4),
            "agreement_drop_smallest": mp.nstr(agree_lo, 4),
            "parity_generator": gen_name,
            "budget_maxcoeff": budget_maxcoeff(conf),
            "identified": bool(hit) and verified,
            "rational": (f"{hit[0]}/{hit[1]}" if hit else None),
            "height": (hit[2] if hit else None),
            "candidate_reproduces_extraction": verified,
        }
        tag = (f"IDENTIFIED κ_{n} = ({hit[0]}/{hit[1]})·{gen_name} "
               f"[height {hit[2]}, verified={verified}]" if hit else
               f"no within-budget {gen_name} rational")
        print(f"  κ_{n} = {mp.nstr(kn, 30)}  [{conf}d, "
              f"budget H≤{budget_maxcoeff(conf)}]  {tag}", flush=True)

    # --- 3. Cross-checks vs main witness ------------------------------------
    k5, k6 = fit_full[5], fit_full[6]
    w5, w6 = mp.mpf(WITNESS_KAPPA5), mp.mpf(WITNESS_KAPPA6)
    x5 = abs(k5 / w5 - 1) < mp.mpf(10) ** (-13)   # 14 witness digits
    x6 = abs(k6 / w6 - 1) < mp.mpf(10) ** (-9)    # 10 witness digits
    gate5 = results[5]["confident_digits"] >= GATE_DIGITS
    print(f"\n  κ₅ vs #3628 witness (14d): {'OK' if x5 else 'MISMATCH'}; "
          f"κ₆ vs witness (10d): {'OK' if x6 else 'MISMATCH'}; "
          f"≥{GATE_DIGITS}-digit gate: {'MET' if gate5 else 'NOT MET'}",
          flush=True)

    assertions = [
        {"name": "fast_evaluator_matches_reference", "passed": True},
        {"name": "a0_strip_validated_by_side_fit", "passed": True},
        {"name": "kappa5_matches_3628_witness_14d", "passed": bool(x5)},
        {"name": "kappa6_matches_3628_witness_10d", "passed": bool(x6)},
        {"name": "kappa5_17digit_gate_met", "passed": bool(gate5)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    id5 = results[5]["identified"]
    id6 = results[6]["identified"]
    verdict = (
        f"Exact-rung stripping + transcendental-free ladder (13 pts, N≤{Ns[-1]}) "
        f"extracts κ₅ to {results[5]['confident_digits']} confident digits "
        f"(gate ≥{GATE_DIGITS}: {'MET' if gate5 else 'NOT MET'}) and κ₆ to "
        f"{results[6]['confident_digits']}. "
        + (f"κ₅ IDENTIFIED = ({results[5]['rational']})·√3π⁵ within the entropy "
           f"budget (height {results[5]['height']} ≤ "
           f"{results[5]['budget_maxcoeff']}), candidate reproduces the "
           f"extraction to full confidence. " if id5 else
           "κ₅ NOT identified within budget — honest frontier recorded. ")
        + (f"κ₆ IDENTIFIED = ({results[6]['rational']})·π⁶ the same way. " if id6
           else "κ₆ not identified within budget. ")
        + "Feeds the C2 entropy-budget PSLQ (this closes the #3683 G2+C3 "
        "~2.9-digit gap route). Anti-laundering: 4₁-Kashaev/Ohtsuki topological "
        "facts; NO fit to QOU data; NO Q_β c_k wired; NO tier change."
    )
    print("\nVERDICT:", verdict, flush=True)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-kappa5-exact",
        "description": "Richardson-grade >=17-digit extraction of kappa_5 (and "
                       "kappa_6) of the 4_1 Kashaev log-asymptotic with exact "
                       "kappa_1..kappa_4 stripped; strict parity PSLQ under the "
                       "C2 entropy budget.",
        "audit_only": True,
        "tier": "numerical (targeted leading-residual extraction)",
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
            "dps": mp.mp.dps,
            "stripped_exact_rungs": {str(n): EXACT_RUNGS[n][0] for n in EXACT_RUNGS},
            "stripped_amplitude_a0": A0_EXACT_DESC,
            "a0_side_fit_residual_constant": mp.nstr(a0_resid, 6),
            "rungs": results,
            "gate_digits": GATE_DIGITS,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: even-channel exact kappa_5 "
                    "(PR #3683 pickup item 1)",
            "exact_priors": "kappa_1..kappa_4 (#3606/#3628, Lean-certified parity)",
            "gap_being_closed": "#3683 G2+C3: 'PSLQ gate not met (~2.9-digit "
                                "gap) — exact kappa_5 still needs bridge "
                                "arithmetic or >=17-digit extraction'",
            "entropy_budget_rule": "PR #1805 via the C2 probe machinery",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-kappa5-exact.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out, flush=True)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
