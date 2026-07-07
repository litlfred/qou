#!/usr/bin/env python3
"""
Ohtsuki series of the figure-eight knot 4_1 — recover Vol(4_1) from the Kashaev
invariant asymptotics (volume conjecture) and extract the quantum-correction
ladder κ_k.  Self-contained, exact-to-precision; NO fit to QOU data, NO wiring,
NO c_k value, NO tier change.

Why 4_1: it is THE canonical hyperbolic knot, and Vol(4_1) = 2Λ(π/3) already
enters the muon anchor (m_μ = m_e·Vol(4_1)/ℏ_q²).  This computes the QUANTUM side
(𝔙_q via the Kashaev sum), whose N→∞ exponential rate is the CLASSICAL 𝔙(4_1) —
making the 𝔙_q vs 𝔙 distinction concrete.

Kashaev invariant (real form):
    J_N(4_1) = Σ_{k=0}^{N-1} ∏_{j=1}^{k} (2 sin(π j / N))²
Asymptotics (Kashaev/Murakami–Murakami volume conjecture; Ohtsuki expansion):
    log J_N = (V/2π)·N + (3/2)·log N + b + κ₁/N + κ₂/N² + κ₃/N³ + …
with V = Vol(4_1).  We fit this and CHECK 2π·(leading slope) ≈ Vol(4_1) — the
volume-conjecture recovery is the validating assertion.  The κ_k are the
fixed-knot (anchor-INVARIANT) Ohtsuki data — they pin the c_k ladder STRUCTURE
(the derived even channel), NOT S's anchor swing (an extraction artifact).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

mp.mp.dps = 60


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
    """log J_N(4_1) = log Σ_k ∏_{j≤k}(2 sin(πj/N))², computed in log-space."""
    pi = mp.pi
    logterms = []
    logP = mp.mpf(0)  # k=0 empty product -> P_0 = 1 -> log 0
    logterms.append(logP)
    for k in range(1, N):
        s = 2 * mp.sin(pi * k / N)
        logP += 2 * mp.log(s)   # multiply P_{k-1} by (2 sin(πk/N))²
        logterms.append(logP)
    # logsumexp
    m = max(logterms)
    return m + mp.log(mp.fsum(mp.e ** (t - m) for t in logterms))


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # Exact Vol(4_1) = 2·Λ(π/3) = 2·Im Li₂(e^{iπ/3}).
    Vol_41 = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
    print(f"Vol(4_1) = 2Λ(π/3) = {mp.nstr(Vol_41, 20)}")

    # Compute log J_N for a window of large N and fit the ansatz
    #   log J_N = a·N + (3/2) log N + b + c1/N + c2/N² + c3/N³
    Ns = [300, 360, 420, 480, 540, 600, 660]
    print("\n=== Kashaev invariant log J_N(4_1) ===")
    rows = []
    for N in Ns:
        lJ = log_kashaev_4_1(N)
        g = lJ - mp.mpf(3) / 2 * mp.log(N)   # subtract known N^{3/2}
        rows.append((N, g))
        print(f"  N={N:4d}  log J_N={mp.nstr(lJ,16)}")

    # Linear solve: g_N = a·N + b + c1/N + c2/N² + c3/N³  (5 unknowns, 7 eqns → LSQ)
    # Build normal equations with mpmath.
    basis = lambda N: [mp.mpf(N), mp.mpf(1), 1/mp.mpf(N), 1/mp.mpf(N)**2, 1/mp.mpf(N)**3]
    A = mp.matrix([basis(N) for N, _ in rows])
    y = mp.matrix([g for _, g in rows])
    # least squares via normal equations AᵀA x = Aᵀy
    AtA = A.T * A
    Aty = A.T * y
    coef = mp.lu_solve(AtA, Aty)
    a, b, c1, c2, c3 = [coef[i] for i in range(5)]
    V_recovered = 2 * mp.pi * a
    rel_err = abs(V_recovered / Vol_41 - 1)
    print(f"\n=== fit  log J_N = a·N + (3/2)logN + b + c1/N + c2/N² + c3/N³ ===")
    print(f"  a (slope)            = {mp.nstr(a,16)}")
    print(f"  2π·a  (recovered Vol)= {mp.nstr(V_recovered,16)}")
    print(f"  Vol(4_1) exact       = {mp.nstr(Vol_41,16)}")
    print(f"  rel err              = {mp.nstr(rel_err,4)}")
    print(f"  b                    = {mp.nstr(b,12)}   (= -¼ log 3 ⇒ 3^{{-1/4}} prefactor)")
    print(f"  κ-ladder: c1={mp.nstr(c1,10)}  c2={mp.nstr(c2,10)}  c3={mp.nstr(c3,10)}")

    # VALIDATING assertion: volume conjecture recovered to <1e-3
    check("volume_conjecture_recovered_lt_1e-3", rel_err < mp.mpf("1e-3"))
    # sanity: J_N grows (positive slope) and κ-ladder is finite
    check("positive_exponential_growth", a > 0)
    check("kappa_ladder_finite", all(abs(c) < mp.mpf("1e6") for c in [c1, c2, c3]))

    # Structural note: b is the log of the leading constant. For THIS Kashaev
    # normalization J_N = Σ∏(2 sin)², the known 4_1 prefactor is exactly N^{3/2}·
    # 3^{-1/4}·e^{NV/2π}, i.e. b = -¼ log 3.  (Same √3/hexagonal ζ₃ constant that
    # appears in the c_3^even ℚ(√3) rungs — a structural consistency, not a fit.)
    b_expected = -mp.log(3) / 4
    b_close = abs(b - b_expected) < mp.mpf("1e-3")
    print(f"  b expected (3^{{-1/4}} ⇒ -¼log3) = {mp.nstr(b_expected,12)}  match={b_close}")
    check("leading_constant_is_3^-1/4_hexagonal", b_close)

    all_passed = all(x["passed"] for x in assertions)
    verdict = (
        f"Kashaev asymptotics of 4_1 recover Vol(4_1)={mp.nstr(Vol_41,10)} to rel "
        f"{mp.nstr(rel_err,3)} (volume conjecture, VALIDATED), with the known "
        f"3^(-1/4) leading constant (b=-¼log3, the same √3/hexagonal ζ₃ that "
        f"appears in the c_3^even ℚ(√3) rungs). The quantum object J_N (=𝔙_q side) "
        f"has exponential rate = the CLASSICAL 𝔙(4_1) — the 𝔙_q vs 𝔙 bridge made "
        f"concrete. The extracted κ-ladder (c1={mp.nstr(c1,6)}, c2={mp.nstr(c2,6)}, "
        f"c3={mp.nstr(c3,6)}) are FIXED-KNOT (anchor-invariant) Ohtsuki data: they "
        f"pin the c_k ladder STRUCTURE (the derived even channel), NOT S's anchor "
        f"swing (a circular-extraction artifact, not reproduced here — as it must "
        f"not be). Bridging these κ_k to the u=b·ℏ_q² ladder normalization IS the "
        f"open f-map. No fit to QOU data; no c_k value; no wiring; no tier change."
        if all_passed else
        "INCONCLUSIVE — volume recovery or a sanity assertion failed."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-ohtsuki-figure-eight-ladder",
        "description": "Ohtsuki series of 4_1: recover Vol(4_1) from Kashaev "
                       "invariant asymptotics (volume conjecture) + extract the "
                       "quantum-correction κ-ladder. Makes 𝔙_q vs 𝔙 concrete.",
        "audit_only": True,
        "tier": "structural-exact (volume-conjecture recovery; κ-ladder measured, "
                "not fitted to QOU)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "Vol_41_exact": mp.nstr(Vol_41, 20),
            "Vol_recovered_2pi_a": mp.nstr(V_recovered, 16),
            "vol_rel_err": mp.nstr(rel_err, 4),
            "leading_constant_b": mp.nstr(b, 12),
            "kappa_ladder": {"c1": mp.nstr(c1, 12), "c2": mp.nstr(c2, 12),
                             "c3": mp.nstr(c3, 12)},
            "N_window": Ns,
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: Ohtsuki route (quantum 𝔙_q of 4_1)",
            "knot": "4_1 figure-eight (Vol enters muon anchor m_μ=m_e·Vol(4_1)/ℏ_q²)",
            "classical_vs_quantum": "N→∞ exp rate = classical 𝔙(4_1); J_N itself = 𝔙_q side",
            "kappa_are_anchor_invariant": "Ohtsuki κ_k pin ladder STRUCTURE (even "
                "channel ℚ(√3)), not S's swing (extraction artifact)",
            "open_fmap": "bridging κ_k (2π/N basis) to the u=b·ℏ_q² ladder normalization",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-ohtsuki-figure-eight-ladder.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
