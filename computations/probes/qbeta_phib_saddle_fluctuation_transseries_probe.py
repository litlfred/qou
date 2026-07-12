#!/usr/bin/env python3
"""qbeta_phib_saddle_fluctuation_transseries_probe.py

C6 of the Borel/alien-calculus utilization audit — "the wall": the
saddle-fluctuation TRANSSERIES of the 4_1 Kashaev/state-integral saddle,
computed order by order as EXACT arithmetic, not extracted numerically.

WHAT IS BUILT (the audit's "no script computes it — pure opportunity"):

  A generator that produces the fluctuation orders of the saddle expansion
  of J_N(4_1) = Sum_k Prod_{j<=k} (2 sin(pi j/N))^2 arithmetically, from three
  exactly-known layers at the saddle s* = 5/6:

    1. the DILOG POTENTIAL Phi(s) = -Cl_2(2 pi s)/pi with Phi'(s) =
       2 log(2 sin(pi s)) — its full derivative tower at s* lies in
       Q(sqrt3)*pi^k because cot(5 pi/6) = -sqrt3 (the Q(sqrt(-3)) trace
       field made concrete);
    2. the EULER-MACLAURIN layer of the inner sum Sum_{j<=k} log(2 sin(pi j/N))
       after splitting off the exactly-summable singular part
       Sum 2 log(2 pi j/N) = 2k log(2 pi/N) + 2 log k!  (so E-M applies to the
       smooth g0(s) = log(sin(pi s)/(pi s)), g0(0) = 0);
    3. the STIRLING layer of the 2 log k! piece.

  The assembled exponent  log T_k = N*Phi(s) + log(2 pi N) + log s + g0(s)
  + Sum_{r odd} E_r(s)/N^r  is saddle-expanded by formal steepest descent
  (Wick / Gaussian moments in v = u*sqrt(N)), and the log of the fluctuation
  series gives the Ohtsuki rungs kappa_n EXACTLY.

GROUND TRUTH (why this is checkable at every rung): kappa_1..kappa_4 are
exact on main (#3606/#3628); kappa_5 = (110011/688905)*sqrt3*pi^5 was
identified today at 40 confident digits (2026-07-12 kappa5-exact audit, this
branch). The generator must REPRODUCE all five — turning the PSLQ
identifications into computed theorems — and then EMITS exact kappa_6,
kappa_7 as new output. Today's kappa_6 puzzle (33 confident digits, NO
Q*pi^6 element of height <= 5e14) is adjudicated by the exact kappa_6.

Relation to Phi_b (the C6 naming): the root-of-unity Kashaev saddle is the
checkable face of the same figure-eight saddle whose Phi_b state-integral
value 𝔙(m) the corpus computes via the gluing Newton solver
(qbeta_c3_phib_saddle_state_integral_probe.py); the finite-b correction
i*t*kappa_1 already in use there is literally rung 1 of this transseries.
Producing the higher fluctuation orders at complex meridian m is the same
generator fed the deformed-saddle derivative tower — follow-up wiring, kept
out of scope here (anti-laundering: the ħ <-> 2 pi i/N channels relate by
resummation, not term-by-term reparametrisation — the bridge
growth-obstruction audit's correction).

Controls: (a) the generator is validated on the Stirling series of log Gamma
via the SAME Wick engine (independent known answer); (b) the assembled
prefactor must reproduce a_0 = -(1/4) log 3 and the N^(3/2) power exactly;
(c) every exact kappa_n is ALSO compared to the corpus 40/33-digit numerics.

VERDICT (self-asserted, CI-safe): DERIVED if kappa_1..kappa_5 are reproduced
exactly and kappa_6 matches the 33-digit extraction; else the mismatch layer
is recorded honestly. NO fit to QOU data; NO Q_beta c_k wired; NO tier change.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import math
import os
import subprocess
import sys
import time

import mpmath as mp
import sympy as sp

K_MAX = 7          # produce kappa_1..kappa_7 (eps^14)
EPS_ORDER = 2 * K_MAX

# Exact rungs: #3606/#3628 (1-4) + today's 40-digit identification (5).
KAPPA_EXACT_PRIOR = {
    1: sp.Rational(11, 108) * sp.sqrt(3) * sp.pi,
    2: sp.Rational(2, 27) * sp.pi ** 2,
    3: sp.Rational(1081, 21870) * sp.sqrt(3) * sp.pi ** 3,
    4: sp.Rational(98, 729) * sp.pi ** 4,
    5: sp.Rational(110011, 688905) * sp.sqrt(3) * sp.pi ** 5,
}
# Today's kappa5-exact extraction numerics (40 / 33 confident digits).
KAPPA5_NUMERIC = "84.6421656050384435275283130292"
KAPPA6_NUMERIC = "676.946678964105031492781861098"


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


# ---------------------------------------------------------------------------
# The Wick engine: fluctuation series of  ∫ exp(N*S(u) + W(u; 1/N)) du
# around a nondegenerate maximum, as a formal series in 1/N.
#
# Input: taylor coefficients S_j (j >= 2, S_2 < 0) of S at the saddle and a
# dict insertions[r][m] = m-th taylor coefficient (derivative/m!) of the
# N^{-r} insertion layer (r >= 0; r = 0 is the N-independent layer, e.g.
# log-weight terms). Scaling u = v/sqrt(N) (eps := 1/sqrt(N)):
#   N S_j u^j        -> S_j v^j eps^{j-2}
#   insertions r, m  -> c v^m eps^{m+2r}
# exp of the non-Gaussian part is expanded to eps^EPS_ORDER; odd v-moments
# vanish; <v^{2n}> = (2n-1)!! sigma^{2n}, sigma^2 = -1/S_2.  Output: series
# 1 + f_1/N + f_2/N^2 + ...  (assert: no half-integer powers survive).
# ---------------------------------------------------------------------------

def wick_fluctuation_series(S, insertions, eps_order):
    """S: dict {j: coeff} for j >= 2 (S[2] < 0); insertions: dict
    {r: {m: coeff}}. Returns list [f_0 = 1, f_1, ..., f_{eps_order//2}]."""
    v, eps = sp.symbols("v eps")
    A = sp.S.Zero
    for j, Sj in S.items():
        if j >= 3 and Sj != 0:
            A += Sj * v ** j * eps ** (j - 2) / sp.factorial(j)
    for r, layer in insertions.items():
        for m, c in layer.items():
            if c != 0:
                deg = m + 2 * r
                if deg <= eps_order:
                    A += c * v ** m * eps ** deg
    A = sp.expand(A)

    # exp(A) truncated at eps^eps_order by iterated truncated multiplication.
    def trunc(e):
        e = sp.expand(e)
        out = sp.S.Zero
        for term in sp.Add.make_args(e):
            if sp.degree(term, eps) <= eps_order:
                out += term
        return out

    F = sp.S.One
    term = sp.S.One
    kmax = eps_order  # A has min eps-degree 1
    for i in range(1, kmax + 1):
        term = trunc(term * A) / i
        if term == 0:
            break
        F = F + term
    F = sp.expand(F)

    # Gaussian moments: v^{2n} -> (2n-1)!! sigma^{2n}; odd -> 0.
    sigma2 = -1 / S[2]
    out = sp.S.Zero
    for term in sp.Add.make_args(F):
        dv = sp.degree(term, v)
        if dv % 2 == 1:
            continue
        n = dv // 2
        moment = sp.factorial2(2 * n - 1) * sigma2 ** n if n > 0 else 1
        out += term.subs(v, 1) * moment  # term/v^dv * moment: v->1 after split
    # NOTE: term.subs(v, 1) is safe because each Add-arg is a monomial in
    # (v, eps) with a scalar coefficient; substituting v = 1 strips v^dv.
    out = sp.expand(out)

    fs = []
    for k in range(0, eps_order // 2 + 1):
        fs.append(sp.simplify(out.coeff(eps, 2 * k)))
    # No half-integer 1/N powers may survive (odd eps orders).
    for k in range(1, eps_order + 1, 2):
        c = sp.simplify(out.coeff(eps, k))
        assert c == 0, f"odd eps^{k} coefficient survived: {c}"
    return fs


def kappa_from_fluctuations(fs, K):
    """kappa_n = [x^n] log(1 + f_1 x + f_2 x^2 + ...)."""
    x = sp.symbols("x")
    series = sum(fs[k] * x ** k for k in range(min(len(fs), K + 1)))
    logser = sp.series(sp.log(series), x, 0, K + 1).removeO()
    return {n: sp.simplify(sp.expand(logser).coeff(x, n)) for n in range(1, K + 1)}


# ---------------------------------------------------------------------------
# Control: Stirling's series from the same engine.
#   Gamma(N+1) = ∫_0^oo e^{-t} t^N dt = N^{N+1} ∫ e^{N(log s - s)} ds,
#   S(s) = log s - s, saddle s* = 1, no insertions.  The engine must return
#   the Stirling fluctuation series 1 + 1/(12N) + 1/(288N^2) - 139/(51840N^3).
# ---------------------------------------------------------------------------

def control_stirling():
    s = sp.symbols("s")
    S_expr = sp.log(s) - s
    S = {j: sp.diff(S_expr, s, j).subs(s, 1) for j in range(2, EPS_ORDER + 3)}
    fs = wick_fluctuation_series(S, {}, 8)
    expected = [sp.S.One, sp.Rational(1, 12), sp.Rational(1, 288),
                sp.Rational(-139, 51840), sp.Rational(-571, 2488320)]
    ok = all(sp.simplify(fs[k] - expected[k]) == 0 for k in range(5))
    return ok, [str(f) for f in fs[:5]]


# ---------------------------------------------------------------------------
# The 4_1 assembly.
# ---------------------------------------------------------------------------

def build_41_layers():
    """Exact taylor data at s* = 5/6 for the three layers."""
    s = sp.symbols("s")
    sstar = sp.Rational(5, 6)

    # Potential: Phi'(s) = 2 log(2 sin(pi s));  Phi_j = d^{j-1} Phi' (j >= 2).
    phip = 2 * sp.log(2 * sp.sin(sp.pi * s))
    S = {}
    d = phip
    for j in range(2, EPS_ORDER + 4):
        d = sp.diff(d, s)
        S[j] = sp.simplify(d.subs(s, sstar)) if j == 2 else d.subs(s, sstar)
    # S[2] = 2 pi cot(5 pi/6) = -2 sqrt3 pi < 0.
    assert sp.simplify(S[2] + 2 * sp.sqrt(3) * sp.pi) == 0

    # r = 0 layer: log(sin(pi s))  (the e^{log s + g0} = sin(pi s)/pi weight,
    # with the constant 1/pi and value at s* pulled into the prefactor).
    L = sp.log(sp.sin(sp.pi * s))
    L_taylor = {}
    d = L
    for m in range(1, EPS_ORDER + 1):
        d = sp.diff(L, s, m)
        L_taylor[m] = d.subs(s, sstar) / sp.factorial(m)

    # g0 and its odd E-M / Stirling layers E_r, r = 2r'-1:
    #   E_{2r'-1}(s) = 2 B_{2r'}/(2r')! * (g0^{(2r'-1)}(s) - g0^{(2r'-1)}(0))
    #                + 2 B_{2r'}/(2r'(2r'-1)) * s^{1-2r'}          (Stirling)
    g0 = sp.log(sp.sin(sp.pi * s) / (sp.pi * s))
    # g0 is smooth at 0 (g0(0) = 0); take boundary derivatives from the
    # series expansion (robust + fast, vs high-order sp.limit).
    g0_ser = sp.series(g0, s, 0, EPS_ORDER + 6).removeO()
    insertions = {0: L_taylor}
    for rp in range(1, (K_MAX + 1) // 2 + 2):
        r = 2 * rp - 1
        if r > K_MAX:
            break
        B = sp.bernoulli(2 * rp)
        gd = sp.diff(g0, s, 2 * rp - 1)
        gd0 = sp.diff(g0_ser, s, 2 * rp - 1).subs(s, 0)
        E_r = (2 * B / sp.factorial(2 * rp)) * (gd - gd0) \
            + (2 * B / (2 * rp * (2 * rp - 1))) * s ** (1 - 2 * rp)
        layer = {}
        for m in range(0, EPS_ORDER - 2 * r + 1):
            layer[m] = sp.diff(E_r, s, m).subs(s, sstar) / sp.factorial(m)
        insertions[r] = layer

    # Prefactor check data.
    L_star = L.subs(s, sstar)              # log sin(5 pi/6) = log(1/2)
    return S, insertions, L_star


def main() -> int:
    mp.mp.dps = 60
    t0 = time.time()
    print("=" * 78)
    print(" C6: 4_1 saddle-fluctuation transseries — exact fluctuation orders")
    print("=" * 78)

    # --- 1. Control: Stirling from the same Wick engine --------------------
    ok_stirling, stirling_fs = control_stirling()
    print(f"\n [control] Stirling series from the Wick engine: "
          f"{'EXACT MATCH' if ok_stirling else 'MISMATCH'} {stirling_fs}")
    assert ok_stirling, "Wick engine fails the Stirling control"

    # --- 2. Assemble the 4_1 layers -----------------------------------------
    print("\n [4_1] building exact taylor data at s* = 5/6 "
          "(potential + E-M + Stirling layers) ...", flush=True)
    S, insertions, L_star = build_41_layers()

    # Prefactor: J_N = 2 N^2 * e^{L*} * sqrt(2 pi/(-S2 N)) * (fluct) * e^{N Phi*}
    #  = 3^{-1/4} N^{3/2} e^{N V/2pi} * (fluct); a0 must equal -(1/4) log 3.
    amp = 2 * sp.exp(L_star) * sp.sqrt(2 * sp.pi / (-S[2]))
    a0 = sp.simplify(sp.log(amp))
    a0_ok = sp.simplify(a0 + sp.Rational(1, 4) * sp.log(3)) == 0
    print(f" [4_1] prefactor amplitude: a0 = {a0}  "
          f"({'= -(1/4) log 3 EXACT' if a0_ok else 'MISMATCH'})")
    assert a0_ok, "prefactor amplitude does not reproduce Andersen-Hansen 3^(-1/4)"

    # --- 3. Fluctuation orders + kappa ladder --------------------------------
    print(f" [4_1] Wick expansion to eps^{EPS_ORDER} (kappa_1..kappa_{K_MAX}) "
          "...", flush=True)
    fs = wick_fluctuation_series(S, insertions, EPS_ORDER)
    kappa = kappa_from_fluctuations(fs, K_MAX)
    print(f"       done in {time.time() - t0:.0f}s")

    s3, pi = sp.sqrt(3), sp.pi
    results, all_prior_ok = {}, True
    print("\n rung | derived exact value | vs prior")
    for n in range(1, K_MAX + 1):
        kn = sp.simplify(kappa[n])
        gen = (s3 * pi ** n) if n % 2 == 1 else pi ** n
        ratio = sp.simplify(kn / gen)
        ratio = sp.nsimplify(ratio, rational=True) if ratio.is_number else ratio
        is_rat = isinstance(ratio, sp.Rational)
        prior = KAPPA_EXACT_PRIOR.get(n)
        prior_ok = (sp.simplify(kn - prior) == 0) if prior is not None else None
        if prior is not None:
            all_prior_ok = all_prior_ok and bool(prior_ok)
        results[n] = {
            "exact": str(kn),
            "rational_over_parity_generator": str(ratio),
            "parity_form_ok": bool(is_rat),
            "matches_prior_exact": prior_ok,
            "numeric_50d": mp.nstr(mp.mpf(sp.N(kn, 60).__str__()), 40)
            if kn.is_number else None,
        }
        tag = ("MATCHES exact prior" if prior_ok
               else ("NEW (no prior exact)" if prior is None else "MISMATCH"))
        print(f"  k_{n} = ({ratio})*{'sqrt3*' if n % 2 == 1 else ''}pi^{n}   [{tag}]")

    # --- 4. kappa_6 adjudication vs today's 33-digit extraction -------------
    k6 = sp.simplify(kappa[6])
    k6_num = sp.N(k6, 45)
    obs6 = mp.mpf(KAPPA6_NUMERIC)
    k6_match = abs(mp.mpf(str(k6_num)) / obs6 - 1) < mp.mpf(10) ** (-30)
    r6 = sp.nsimplify(sp.simplify(k6 / sp.pi ** 6), rational=True)
    h6 = max(abs(sp.numer(r6)), abs(sp.denom(r6))) if isinstance(r6, sp.Rational) else None
    print(f"\n kappa_6 derived = {k6}")
    print(f"   numeric: {k6_num}")
    print(f"   vs 33-digit extraction: {'MATCH (<=1e-30 rel)' if k6_match else 'MISMATCH'}")
    if h6 is not None:
        print(f"   height(kappa_6/pi^6) = {h6}  (today's PSLQ budget was 5e14: "
              f"{'explains the miss — height above budget' if h6 > 5 * 10**14 else 'was WITHIN budget — puzzle deepens'})")
    k5_num_ok = abs(mp.mpf(str(sp.N(kappa[5], 45))) / mp.mpf(KAPPA5_NUMERIC) - 1) \
        < mp.mpf(10) ** (-38)

    assertions = [
        {"name": "wick_engine_stirling_control_exact", "passed": bool(ok_stirling)},
        {"name": "prefactor_amplitude_is_3_pow_minus_quarter", "passed": bool(a0_ok)},
        {"name": "kappa_1_to_5_reproduced_exactly", "passed": bool(all_prior_ok)},
        {"name": "kappa_5_matches_40digit_extraction", "passed": bool(k5_num_ok)},
        {"name": "kappa_6_matches_33digit_extraction", "passed": bool(k6_match)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    verdict = (
        ("DERIVED: the saddle-fluctuation transseries generator (potential + "
         "Euler-Maclaurin + Stirling layers, Wick-expanded) reproduces "
         "kappa_1..kappa_5 EXACTLY (the PSLQ identifications are now computed "
         "theorems) and emits exact kappa_6, kappa_7. "
         if (all_prior_ok and k6_match) else
         "PARTIAL: mismatch layer recorded — see per-rung table. ")
        + (f"kappa_6 = ({r6})*pi^6, height {h6} "
           + ("> the 5e14 budget — today's PSLQ miss is a height explosion, "
              "parity rule INTACT. " if (h6 and h6 > 5 * 10**14) else
              "(within today's budget — investigate). ") if h6 is not None else
           "kappa_6 not a pure rational multiple of pi^6 — parity analysis "
           "needs the derived form. ")
        + "This is C6 of the Borel/alien-calculus audit built at the "
        "root-of-unity face (the checkable face of the Phi_b saddle; rung 1 "
        "is the i*t*kappa_1 finite-b correction already in use). Complex-"
        "meridian wiring is follow-up. NO fit; NO c_k wired; NO tier change."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-phib-saddle-fluctuation-transseries",
        "description": "C6: exact saddle-fluctuation transseries of the 4_1 "
                       "Kashaev saddle (potential + Euler-Maclaurin + Stirling "
                       "layers, Wick engine); derives kappa_1..kappa_7 "
                       "arithmetically; Stirling control; kappa_6 adjudication.",
        "audit_only": True,
        "tier": "symbolic-exact (derivation, sympy)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy+mpmath",
        "engineVersion": f"sympy {sp.__version__}, mpmath {mp.__version__}",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "stirling_control": stirling_fs,
            "a0": str(a0),
            "rungs": results,
            "kappa6_height_over_pi6": (int(h6) if h6 is not None else None),
            "kappa6_explains_pslq_miss": (bool(h6 > 5 * 10**14) if h6 is not None else None),
            "verdict": verdict,
        },
        "context": {
            "axis": "C6 state-integral saddle-fluctuation transseries "
                    "(PR #3683 pickup item 3; audit 2026-07-12 Borel/alien)",
            "ground_truth": "kappa_1..4 #3606/#3628; kappa_5 today "
                            "(qbeta-ohtsuki-kappa5-exact, 40 digits)",
            "phib_face": "leading finite-b correction i*t*kappa_1 in "
                         "qbeta_c3_phib_saddle_state_integral_probe.py",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-phib-saddle-fluctuation-transseries.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
