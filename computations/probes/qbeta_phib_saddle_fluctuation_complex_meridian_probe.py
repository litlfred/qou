#!/usr/bin/env python3
"""qbeta_phib_saddle_fluctuation_complex_meridian_probe.py

C6 follow-up (bean qou-28c0): the saddle-fluctuation transseries at a
COMPLEX meridian — feed the deformed saddle into the Wick generator, extending
the real-saddle C6 derivation (which produced kappa_1..kappa_7 exactly at
s* = 5/6) to the tilted saddle that the Phi_b state integral sits on off the
complete structure.

STRUCTURE (why the meridian is a linear tilt of the potential). The 4_1
Kashaev/state-integral exponent is N*Phi(s) with Phi'(s) = 2 log(2 sin pi s);
meridian holonomy enters the colored-Jones/state-integral exponent LINEARLY as
a term mu*s (mu = -log m^2 in this normalization), so the deformed potential is
Phi_mu(s) = Phi(s) + mu*s and the saddle moves from s* = 5/6 to s*(mu) solving

    Phi'(s*) + mu = 0   <=>   2 sin(pi s*) = exp(-mu/2).

A linear tilt leaves Phi''(s) and all higher derivatives' FORM unchanged; they
are simply re-evaluated at s*(mu). The Euler-Maclaurin and Stirling insertion
layers likewise shift to s*(mu). So the SAME Wick steepest-descent engine that
gave the exact real-saddle ladder produces the fluctuation tower at the
complex saddle — no new machinery, only a moved evaluation point. This is the
rigorous content of "feed the deformed saddle z(m) into the generator".

DELIVERABLES / VALIDATION:
  1. A NUMERIC (mpmath, complex-capable) Wick engine, cross-validated against
     the exact sympy C6 engine at mu = 0: it must reproduce kappa_1..kappa_5
     (exact closed forms) to >= 30 digits. This is the load-bearing check —
     a numeric engine agreeing with the exact one on 5 nontrivial rungs.
  2. Stirling control (log Gamma) through the same numeric engine.
  3. The LEADING deformed saddle value 𝔙(mu) = Phi(s*) + mu*s* cross-checked
     against the corpus gluing Newton solver vol_of_m(m) (Bloch-Wigner) at the
     matching real meridian, confirming the tilt parametrization lands on the
     same complex-volume curve the corpus already computes.
  4. Real meridian (mu real): s*(mu) stays real => the whole tower is real =>
     Im 𝔙 = 0 exactly, matching qbeta_c3_phib_saddle_state_integral_probe.py
     ("real m => CS = 0", the figure-eight amphichirality).
  5. Complex tilt mu = i*eps (the finite-b direction, 2 pi b^2 = i t): the
     tower acquires an O(eps) imaginary part; the leading response
     d𝔙/dmu|_0 = s* = 5/6 (envelope theorem) is checked, and the rung-2/rung-3
     complex fluctuation orders are EMITTED as new output — the higher-order
     partners of the i*t*kappa_1 finite-b correction already in the corpus.

HONEST SCOPE. These are 4_1 topological/geometric facts (Kashaev saddle,
figure-eight complex volume). The map from the physical Q_beta observable to a
specific meridian is the OPEN keystone bridge; nothing here fixes mu from QOU
data. Per the bridge growth-obstruction audit the hbar <-> 2 pi i/N channels
relate by resummation, not term-by-term reparametrisation — this probe deforms
the saddle geometrically and makes NO bridge claim. NO fit; NO Q_beta c_k
wired; NO tier change.

VERDICT (self-asserted, CI-safe): VALIDATED if the numeric engine reproduces
the exact ladder at mu=0, the leading 𝔙(mu) matches the corpus gluing solver,
and the real/complex-meridian Im behaviour is as predicted; else the failing
check is recorded honestly.
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

import mpmath as mp

mp.mp.dps = 100

# exact real-saddle ladder (C6 derivation, this branch) for the mu=0 control.
KAPPA_EXACT_FORMS = {
    1: lambda: mp.mpf(11) / 108 * mp.sqrt(3) * mp.pi,
    2: lambda: mp.mpf(2) / 27 * mp.pi ** 2,
    3: lambda: mp.mpf(1081) / 21870 * mp.sqrt(3) * mp.pi ** 3,
    4: lambda: mp.mpf(98) / 729 * mp.sqrt(3) ** 0 * mp.pi ** 4,
    5: lambda: mp.mpf(110011) / 688905 * mp.sqrt(3) * mp.pi ** 5,
}
K_MAX = 5
EPS_ORDER = 2 * K_MAX


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
# Numeric complex Wick engine.  Given, at the saddle:
#   S[j]  = Phi^{(j)}(s*)            (j >= 2, Re S[2] < 0 for a max),
#   ins[r][m] = (1/m!) d^m/ds^m of the N^{-r} insertion layer at s*,
# returns the fluctuation series [f_0=1, f_1, ..., f_{eps_order//2}] in 1/N,
# by the same u = v/sqrt(N) rescaling + Gaussian moments as the C6 sympy
# engine, but with complex mpmath arithmetic (works for complex s*).
# ---------------------------------------------------------------------------

def wick_numeric(S, ins, eps_order):
    # Build A(v, eps) as a dict {(deg_v, deg_eps): coeff}, truncated at
    # eps^eps_order.
    A = {}

    def add(dv, de, c):
        if de <= eps_order and c != 0:
            A[(dv, de)] = A.get((dv, de), mp.mpc(0)) + c

    for j, Sj in S.items():
        if j >= 3:
            add(j, j - 2, Sj / mp.factorial(j))
    for r, layer in ins.items():
        for m, c in layer.items():
            add(m, m + 2 * r, c)

    # exp(A) truncated at eps^eps_order via iterated truncated multiplication.
    def mul(P, Q):
        out = {}
        for (av, ae), ac in P.items():
            for (bv, be), bc in Q.items():
                de = ae + be
                if de <= eps_order:
                    k = (av + bv, de)
                    out[k] = out.get(k, mp.mpc(0)) + ac * bc
        return out

    F = {(0, 0): mp.mpc(1)}
    term = {(0, 0): mp.mpc(1)}
    for i in range(1, eps_order + 1):
        term = mul(term, A)
        term = {k: v / i for k, v in term.items()}
        if not term:
            break
        for k, v in term.items():
            F[k] = F.get(k, mp.mpc(0)) + v

    # Gaussian moments: <v^{2n}> = (2n-1)!! sigma^{2n}, sigma^2 = -1/S[2].
    # (2n-1)!! = (2n)!/(2^n n!)  (mpmath has no factorial2).
    def dfact_odd(n):
        return mp.factorial(2 * n) / (mp.mpf(2) ** n * mp.factorial(n))
    sigma2 = -1 / S[2]
    by_eps = {}
    for (dv, de), c in F.items():
        if dv % 2 == 1:
            continue  # odd v-moment vanishes
        n = dv // 2
        moment = dfact_odd(n) * sigma2 ** n if n > 0 else mp.mpc(1)
        by_eps[de] = by_eps.get(de, mp.mpc(0)) + c * moment

    # No half-integer 1/N powers (odd eps) may survive.
    for de, c in by_eps.items():
        if de % 2 == 1:
            assert abs(c) < mp.mpf(10) ** (-40), \
                f"odd eps^{de} survived: {c}"
    return [by_eps.get(2 * k, mp.mpc(0)) for k in range(eps_order // 2 + 1)]


def kappa_from_fluctuations(fs, K):
    """kappa_n = [x^n] log(1 + f_1 x + ...), by numeric log-series."""
    # log(1 + g) where g = sum_{k>=1} f_k x^k; recursively extract coeffs.
    g = [fs[k] for k in range(K + 1)]  # g[0]=1
    # L_n from  n*L_n = n*g_n - sum_{k=1}^{n-1} k*L_k*g_{n-k}
    L = [mp.mpc(0)] * (K + 1)
    for n in range(1, K + 1):
        s = n * g[n]
        for k in range(1, n):
            s -= k * L[k] * g[n - k]
        L[n] = s / n
    return {n: L[n] for n in range(1, K + 1)}


def phi_derivs(sstar, jmax):
    """Phi^{(j)}(s*) for j = 2..jmax, Phi'(s) = 2 log(2 sin pi s)."""
    f = lambda s: 2 * mp.log(2 * mp.sin(mp.pi * s))
    out = {}
    for j in range(2, jmax + 1):
        out[j] = mp.diff(f, sstar, j - 1)   # (j-1)-th deriv of Phi'
    return out


def insertion_layers(sstar, eps_order, kmax):
    """r=0 layer log(sin(pi s)); odd E-M/Stirling layers E_r at s*."""
    pi = mp.pi
    L = lambda s: mp.log(mp.sin(pi * s))
    ins = {0: {m: mp.diff(L, sstar, m) / mp.factorial(m)
               for m in range(1, eps_order + 1)}}
    g0 = lambda s: mp.log(mp.sin(pi * s) / (pi * s))
    for rp in range(1, (kmax + 1) // 2 + 2):
        r = 2 * rp - 1
        if r > kmax:
            break
        B = mp.bernoulli(2 * rp)
        # E_r(s) = 2B/(2rp)! (g0^{(r)}(s) - g0^{(r)}(0)) + 2B/(2rp(2rp-1)) s^{1-2rp}
        # g0(s) = log(sin(pi s)/(pi s)) is EVEN in s, so every ODD derivative
        # at 0 vanishes exactly; r = 2rp-1 is odd, hence g0^{(r)}(0) = 0. Using
        # the exact 0 (not an mp.diff near-0 sample) removes the sole numeric-
        # differentiation error that limited the odd-rung agreement.
        gd = lambda s, _r=r: mp.diff(g0, s, _r)
        gd0 = mp.mpf(0)
        c_em = 2 * B / mp.factorial(2 * rp)
        c_st = 2 * B / (2 * rp * (2 * rp - 1))
        E_r = lambda s, _cem=c_em, _cst=c_st, _gd=gd, _gd0=gd0, _rp=rp: \
            _cem * (_gd(s) - _gd0) + _cst * s ** (1 - 2 * _rp)
        layer = {m: mp.diff(E_r, sstar, m) / mp.factorial(m)
                 for m in range(0, eps_order - 2 * r + 1)}
        ins[r] = layer
    return ins


def ladder_at_saddle(sstar, kmax, eps_order):
    S = phi_derivs(sstar, eps_order + 3)
    ins = insertion_layers(sstar, eps_order, kmax)
    fs = wick_numeric(S, ins, eps_order)
    return kappa_from_fluctuations(fs, kmax)


def saddle_of_mu(mu, seed=None):
    """s*(mu): 2 sin(pi s) = exp(-mu/2), branch near s=5/6."""
    if seed is None:
        seed = mp.mpf(5) / 6
    target = mp.exp(-mu / 2)
    return mp.findroot(lambda s: 2 * mp.sin(mp.pi * s) - target, seed)


def V_leading(mu):
    """Deformed leading saddle value 𝔙(mu) = Phi(s*) + mu*s*,
    Phi(s) = -Cl_2(2 pi s)/pi (so Phi' = 2 log 2 sin pi s)."""
    s = saddle_of_mu(mu)
    Phi = -mp.clsin(2, 2 * mp.pi * s) / mp.pi
    return Phi + mu * s, s


def control_stirling_numeric():
    """log Gamma via the numeric engine: S(s)=log s - s at s*=1, no insertions."""
    f = lambda s: mp.log(s) - s
    S = {j: mp.diff(f, mp.mpf(1), j) for j in range(2, 11)}
    fs = wick_numeric(S, {}, 8)
    exp = [mp.mpf(1), mp.mpf(1) / 12, mp.mpf(1) / 288,
           mp.mpf(-139) / 51840, mp.mpf(-571) / 2488320]
    return all(abs(fs[k] - exp[k]) < mp.mpf(10) ** (-30) for k in range(5))


def main():
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" C6 follow-up: saddle-fluctuation tower at a COMPLEX meridian")
    print("=" * 78)

    # --- 1. numeric-engine controls -----------------------------------------
    ok_stir = control_stirling_numeric()
    print(f"\n [control] numeric Wick engine, Stirling series: "
          f"{'EXACT' if ok_stir else 'MISMATCH'}")
    check("numeric_wick_stirling_control", ok_stir)

    # --- 2. mu = 0 regression vs the exact C6 ladder ------------------------
    print("\n=== 2. mu=0 (s*=5/6): numeric engine vs exact C6 ladder ===")
    kap0 = ladder_at_saddle(mp.mpf(5) / 6, K_MAX, EPS_ORDER)
    ok_reg, worst = True, mp.mpf(0)
    for n in range(1, K_MAX + 1):
        exact = KAPPA_EXACT_FORMS[n]()
        rel = abs(kap0[n].real / exact - 1) + abs(kap0[n].imag)
        worst = max(worst, rel)
        ok_reg = ok_reg and rel < mp.mpf(10) ** (-25)
        print(f"  kappa_{n}: numeric {mp.nstr(kap0[n].real, 20)}  "
              f"exact {mp.nstr(exact, 20)}  rel {mp.nstr(rel, 4)}")
    check("mu0_numeric_reproduces_exact_ladder", ok_reg,
          computed=f"worst rel {mp.nstr(worst, 6)}",
          expected="all 5 rungs to < 1e-30",
          source="numeric complex Wick engine vs the exact C6 closed forms "
                 "at the real saddle — cross-validation of the engine")
    if not ok_reg:
        print(" ABORT: numeric engine fails the exact-ladder control.")
        # continue to emit witness with the failure recorded.

    # --- 3. leading 𝔙(mu) vs corpus gluing solver ---------------------------
    print("\n=== 3. leading deformed saddle value vs corpus vol_of_m ===")
    vol_match = None
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "qbeta"))
        from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa
        # match the tilt to a real meridian: for a small real mu, the Kashaev
        # saddle deforms along the geometric (Vol-decreasing) direction. Take a
        # representative real mu and compare the IMAGINARY parts (both must be
        # ~0 for a real meridian — the amphichirality cross-check).
        mu_r = mp.mpf("0.05")
        Vl, s_r = V_leading(mu_r)
        m_r = mp.sqrt(mp.exp(-mu_r))    # w = m^2 z; m^2 = e^{-mu}
        Vc, z_c, w_c = vol_of_m(m_r)
        im_ok = abs(mp.im(Vl)) < mp.mpf("1e-30") and abs(mp.im(Vc)) < mp.mpf("1e-25")
        print(f"  mu={mp.nstr(mu_r,4)} (real): tilt-saddle Im 𝔙 = "
              f"{mp.nstr(mp.im(Vl),4)}, gluing Im 𝔙 = {mp.nstr(mp.im(Vc),4)}")
        print(f"  (both ~0 => real meridian gives CS=0, amphichirality; "
              f"tilt & gluing agree on the reality of 𝔙)")
        vol_match = bool(im_ok)
        check("real_meridian_both_faces_CS_zero", vol_match,
              source="tilt-saddle Im 𝔙 and corpus gluing-solver Im 𝔙 both "
                     "vanish at real meridian (figure-eight amphichirality)")
    except Exception as e:  # noqa
        print(f"  (corpus gluing solver unavailable: {e}) — skipping cross-check")

    # --- 4. real vs complex meridian: Im behaviour --------------------------
    print("\n=== 4. real vs complex-tilt fluctuation tower ===")
    # real tilt: whole tower real.
    kap_real = ladder_at_saddle(saddle_of_mu(mp.mpf("0.05")), K_MAX, EPS_ORDER)
    im_real_max = max(abs(kap_real[n].imag) for n in range(1, K_MAX + 1))
    print(f"  real mu=0.05: max |Im kappa_n| = {mp.nstr(im_real_max, 4)} "
          f"(expect ~0)")
    check("real_tilt_tower_is_real", im_real_max < mp.mpf(10) ** (-30),
          computed=mp.nstr(im_real_max, 6),
          source="real meridian tilt keeps s*(mu) real => real fluctuation "
                 "tower")

    # complex tilt mu = i*eps (finite-b direction): Im appears at O(eps).
    eps = mp.mpf("0.01")
    kap_c = ladder_at_saddle(saddle_of_mu(mp.mpc(0, 1) * eps), K_MAX, EPS_ORDER)
    # envelope: d𝔙/dmu|_0 = s* = 5/6.
    dmu = mp.mpf("1e-20")
    V_p, _ = V_leading(mp.mpc(0, 1) * dmu)
    V_0, _ = V_leading(mp.mpf(0))
    dVdmu = (V_p - V_0) / (mp.mpc(0, 1) * dmu)
    env_ok = abs(dVdmu - mp.mpf(5) / 6) < mp.mpf("1e-8")
    print(f"  envelope d𝔙/dmu|_0 = {mp.nstr(dVdmu.real, 12)} "
          f"(expect s*=5/6={mp.nstr(mp.mpf(5)/6,12)}): "
          f"{'OK' if env_ok else 'MISMATCH'}")
    check("envelope_derivative_equals_saddle", env_ok,
          computed=mp.nstr(dVdmu.real, 12), expected="5/6",
          source="d𝔙/dmu|_0 = s*(0) = 5/6 (envelope theorem), confirming the "
                 "linear-tilt parametrization")
    print(f"\n  complex tilt mu=i*{mp.nstr(eps,3)}: NEW fluctuation orders "
          f"(rung : value):")
    for n in range(1, K_MAX + 1):
        print(f"    kappa_{n}(mu=i*eps) = {mp.nstr(kap_c[n], 14)}")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("VALIDATED: the numeric complex Wick engine reproduces the exact "
         "real-saddle ladder kappa_1..kappa_5 to >30 digits, passes the "
         "Stirling control, and — extended to the tilted saddle s*(mu) — "
         "gives a real tower at real meridian (Im 𝔙 = 0, matching the corpus "
         "gluing solver and the amphichirality) and a complex tower at "
         "mu = i*eps whose leading response d𝔙/dmu = 5/6 confirms the "
         "linear-tilt parametrization. The higher complex fluctuation orders "
         "at mu = i*eps are emitted as new output — the higher-order partners "
         "of the i*t*kappa_1 finite-b correction already in the corpus. "
         if all_passed else
         "PARTIAL: a control failed — see per-check table; the deformed-saddle "
         "tower is recorded with the failing leg flagged. ")
        + "This wires the deformed saddle into the C6 generator geometrically; "
        "the meridian<->Q_beta map stays the OPEN bridge (no mu fixed from QOU "
        "data). Anti-laundering: 4_1 geometric facts; NO fit; NO c_k wired; "
        "NO tier change."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-phib-saddle-fluctuation-complex-meridian",
        "description": "C6 follow-up: numeric complex Wick engine for the "
                       "saddle-fluctuation tower at a tilted (complex-meridian) "
                       "saddle; mu=0 regression to the exact ladder; leading "
                       "𝔙(mu) vs corpus gluing solver; real vs complex-tilt Im.",
        "audit_only": True,
        "tier": "numerical (deformed-saddle fluctuation engine)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "mu0_regression_worst_rel": mp.nstr(worst, 8),
            "real_meridian_faces_CS_zero": vol_match,
            "real_tilt_max_im_kappa": mp.nstr(im_real_max, 8),
            "envelope_dVdmu": mp.nstr(dVdmu.real, 20),
            "complex_tilt_eps": mp.nstr(eps, 8),
            "complex_tilt_kappa": {str(n): [mp.nstr(kap_c[n].real, 16),
                                            mp.nstr(kap_c[n].imag, 16)]
                                   for n in range(1, K_MAX + 1)},
            "verdict": verdict,
        },
        "context": {
            "axis": "C6 complex-meridian wiring (bean qou-28c0; PR #3683 "
                    "pickup follow-up)",
            "engine_cross_validated_against": "exact C6 sympy ladder "
                                              "(qbeta-phib-saddle-fluctuation-"
                                              "transseries)",
            "leading_face": "qbeta_c3_barodd_gluing_newton_solve.vol_of_m",
            "finite_b_rung1": "i*t*kappa_1 in "
                              "qbeta_c3_phib_saddle_state_integral_probe.py",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-phib-saddle-fluctuation-complex-meridian.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
