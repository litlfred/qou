#!/usr/bin/env python3
"""
Pin the f-map resurgence action A (real, amphichiral 4_1) with a higher-order
ladder + Aitken acceleration, and rigorously prune the complex-q ≈29° "hexagonal"
thread. Self-contained, high precision; NO fit to QOU data, NO wiring, NO c_k
value, NO tier change. Scope-(a); follow-up to #3482/#3487.

Part A — action A. Extend the 4_1 Ohtsuki ladder κ_1..κ_K (dps 260), form the
large-order ratios A_k = k·κ_{k-1}/κ_k → A, and Aitken-Δ² accelerate the reliable
middle window. Compare A to framework candidates (Vol/2π, Vol/4=Λ(π/3), 2/e, …).

Part B — complex-q hexagonal prune. The Hopf cubic's complex root maps (via
y=q²+q⁻²) to a complex substrate q with arg≈29.1°. Test whether arg = π/6 (30°,
hexagonal ζ₃) EXACTLY. It does not — the odd channel's arithmetic is the prime-19
cubic field, distinct from the even channel's ℚ(√3)/ζ₃. Prunes the near-miss as
numerology (scope-(a)).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 260


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
    for env_var in ("GITHUB_SHA", "GIT_COMMIT_SHA"):
        v = os.environ.get(env_var)
        if v and v.strip():
            return v.strip()
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


def aitken(seq):
    """Aitken Δ² acceleration; returns the accelerated sequence."""
    out = []
    for i in range(len(seq) - 2):
        d1 = seq[i + 1] - seq[i]
        d2 = seq[i + 2] - 2 * seq[i + 1] + seq[i]
        if d2 == 0:
            out.append(seq[i + 2])
        else:
            out.append(seq[i] - d1 * d1 / d2)
    return out


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    Vol41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))

    # --- Part A: higher-order ladder + Aitken ------------------------------
    K = 13
    Ns = list(range(400, 1601, 40))  # 31 values
    print(f"computing log J_N for {len(Ns)} values (dps {mp.mp.dps}) ...")
    rows = [(N, log_kashaev_4_1(N) - mp.mpf(3) / 2 * mp.log(N)) for N in Ns]

    def basis(N):
        return [mp.mpf(N), mp.mpf(1)] + [1 / mp.mpf(N) ** k for k in range(1, K + 1)]
    A_mat = mp.matrix([basis(N) for N, _ in rows])
    y = mp.matrix([g for _, g in rows])
    coef = mp.lu_solve(A_mat.T * A_mat, A_mat.T * y)
    a = coef[0]
    kappa = [coef[2 + k] for k in range(K)]
    V_rec = 2 * mp.pi * a
    print(f"  Vol recovered rel err = {mp.nstr(abs(V_rec/Vol41-1),3)}")
    check("vol41_recovered", abs(V_rec / Vol41 - 1) < mp.mpf("1e-8"))

    A_k = [(k, k * kappa[k - 2] / kappa[k - 1]) for k in range(2, K + 1)]
    print("  large-order ratios A_k = k·κ_{k-1}/κ_k:")
    for k, ak in A_k:
        print(f"    A_{k:2d} = {mp.nstr(ak,10)}")
    # Aitken on the reliable middle window (drop k≤4 low-order, and the last 2
    # highest-order where κ_K fit error dominates).
    win = [ak for k, ak in A_k if 5 <= k <= K - 2]
    acc = win
    for _ in range(3):
        if len(acc) >= 3:
            acc = aitken(acc)
    A_pin = acc[-1] if acc else win[-1]
    print(f"  Aitken-accelerated A ≈ {mp.nstr(A_pin,8)}")

    candidates = {
        "Vol/2π":       Vol41 / (2 * mp.pi),
        "Vol/4=Λ(π/3)": Vol41 / 4,
        "Vol/π":        Vol41 / mp.pi,
        "2/e":          2 / mp.e,
        "Vol/e":        Vol41 / mp.e,
        "2Vol/2π":      Vol41 / mp.pi,
    }
    print("  A vs candidates:")
    best = None
    for name, val in candidates.items():
        rel = abs(A_pin / val - 1)
        print(f"    {name:14s} = {mp.nstr(val,10)}   rel {mp.nstr(rel,4)}")
        if best is None or rel < best[1]:
            best = (name, rel, val)
    print(f"  closest: {best[0]} (rel {mp.nstr(best[1],3)})")
    # Honest assertions: A is real-positive O(0.7); NOT cleanly identified (no
    # candidate within 1%). We assert the bound + the non-identification, not a match.
    check("action_real_positive_0p6_to_0p8", mp.mpf("0.6") < A_pin < mp.mpf("0.8"))
    check("action_not_cleanly_identified_within_1pct", best[1] > mp.mpf("0.01"))

    # --- Part B: complex-q hexagonal prune ---------------------------------
    # Hopf cubic complex root y_c → q via y=q²+q⁻² (w=q², w²−y w+1=0).
    roots = mp.polyroots([1, -6, 10, -6])
    yc = [r for r in roots if abs(mp.im(r)) > mp.mpf("1e-20")][0]
    w = (yc + mp.sqrt(yc ** 2 - 4)) / 2
    q = mp.sqrt(w)
    arg_q = mp.arg(q)
    arg_deg = abs(arg_q) * 180 / mp.pi  # magnitude (branch sign is immaterial)
    hexagonal = mp.pi / 6  # 30°, the ζ₃ / hexagonal angle
    rel_to_hex = abs(abs(arg_q) / hexagonal - 1)
    print(f"\n=== Part B: complex-q hexagonal prune ===")
    print(f"  Hopf complex root y_c = {mp.nstr(yc,8)} → q = {mp.nstr(q,8)}")
    print(f"  |arg(q)| = {mp.nstr(arg_deg,7)}°   vs hexagonal π/6 = 30°   rel {mp.nstr(rel_to_hex,3)}")
    print(f"  ⇒ |arg(q)| ≠ 30° (3% off — a generic algebraic angle of the prime-19 "
          f"cubic, NOT ℚ(√3)/ζ₃ hexagonal)")
    # Prune: the near-miss is NOT an exact hexagonal angle (>1% off).
    check("complex_q_arg_not_exactly_hexagonal", rel_to_hex > mp.mpf("0.01"))

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        f"(A) f-map resurgence action of 4_1 (real, amphichiral): order-{K} ladder "
        f"(dps 260, Vol rec rel {mp.nstr(abs(V_rec/Vol41-1),3)}), large-order ratios "
        f"A_k=k·κ_{{k-1}}/κ_k Aitken-accelerate to A≈{mp.nstr(A_pin,6)}. Real-positive, "
        f"O(0.7); closest candidate {best[0]} (rel {mp.nstr(best[1],3)}) — NOT cleanly "
        "identified (no framework constant within 1%). The action is a genuine "
        "categorical invariant of the even/amphichiral sector but does not reduce to "
        "a simple Vol-ratio at this order; an exact saddle expansion (rationals over "
        "ℚ(√-3)) is the route to a closed form. (B) The Hopf-cubic complex root maps "
        f"to a complex substrate q with |arg|={mp.nstr(arg_deg,4)}°, ~3% off the "
        f"hexagonal π/6=30° (rel {mp.nstr(rel_to_hex,2)}) and NOT equal to it — pruned "
        "as numerology: |arg| is a generic algebraic angle of the prime-19 cubic "
        "field (disc -76), distinct from the even channel's ℚ(√3)/ζ₃. No fit; no c_k "
        "value; no wiring; no tier change."
        if all_passed else
        "INCONCLUSIVE — a recovery/bound/prune assertion failed; re-derive."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-action-pin-refine",
        "description": "Refined f-map action A (Aitken on order-13 4_1 ladder; real, "
                       "not cleanly identified) + complex-q hexagonal-angle prune.",
        "audit_only": True,
        "tier": "structural-exact (Vol recovery, prune) + numerical (action, order-limited)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "vol41_recovered_rel": mp.nstr(abs(V_rec / Vol41 - 1), 3),
            "kappa": [mp.nstr(k, 10) for k in kappa],
            "action_A_aitken": mp.nstr(A_pin, 10),
            "closest_candidate": best[0],
            "closest_rel": mp.nstr(best[1], 6),
            "complex_q_arg_deg": mp.nstr(arg_deg, 8),
            "arg_vs_hexagonal_rel": mp.nstr(rel_to_hex, 6),
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: action pin + hexagonal prune",
            "prior": "#3482 (action real, amphichiral), #3487 (Hopf cubic complex roots)",
            "action_open": "exact saddle expansion (ℚ(√-3)) for a closed-form A",
            "odd_field": "prime-19 cubic (disc -76), NOT ℚ(√3)/ζ₃",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-action-pin-refine.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
