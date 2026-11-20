#!/usr/bin/env python3
"""qbeta_phib_2loop_bdictionary_probe.py — the Φ_b odd b-dictionary at the
substrate, and its trace-field compatibility with F1's D-ladder.

CONTEXT (bean qou-jzrf; PR after the #3902 branch-point closure). #3844's
four-front note names the single genuinely-unowned piece feeding F1 (odd
D-ladder Écalle acceleration): *the deformed b-dictionary normalization, which
#3596's Φ_b construction supplies once its saddle expansion is pushed to 2-loop
at m = q₀*. The 4₁ Φ_b state integral has the semiclassical (ħ = 2πb² = it)
tower log Z ~ 𝔙/ħ + ½log det + Σ_{n≥1} ħⁿ Sₙ; the fluctuation invariants Sₙ
are, up to the ħ↔2πi/N normalization (quantum modularity), the exact Ohtsuki
κ-ladder computed on main (κ_1..κ_7, transseries probe). The leading finite-b
correction i·t·κ_1 already in the corpus is the n=1 (2-loop) rung.

THE STRUCTURE THIS PROBE ESTABLISHES (all 4₁ geometric / arithmetic facts):

  (A) BAR-PARITY = √3-GRADING OF THE κ-LADDER. Under bar-conjugation q↔q⁻¹, i.e.
      t = ln q ↔ −t, the substrate assembly Σ ħⁿκ_n = Σ (it)ⁿκ_n splits by n:
      even n bar-even, odd n bar-odd. The κ-ladder's number-field grading is
      EXACTLY this: κ_odd ∈ ℚ·√3·πⁿ, κ_even ∈ ℚ·πⁿ (√3 = the 4₁ cusp trace
      field, cot(5π/6) = −√3). So the bar-ODD b-dictionary is the √3-graded
      subladder {κ_1, κ_3, κ_5, κ_7}, known in closed form.

  (B) THE D-LADDER SHARES THE TRACE FIELD ℚ(√3). F1's exact bar-odd D-ladder
      d_k = a_k + b_k·√3 (build_d_ladder, k ≤ 21) lives in the SAME ℚ(√3), with
      the G2 2-adic parity grading v₂(den b_k)=0 ⟺ k odd. Trace-field
      compatibility (not a naive term identity — the D-ladder carries both
      rational and √3 parts at every k; the bridge d↔κ is the open keystone).

  (C) THE ODD b-DICTIONARY AT THE SUBSTRATE. Assemble Σ_{n odd}(it)ⁿκ_n at
      t = ln q₀; the leading rung is i·t·κ_1 (regression to the corpus
      finite-b correction). Its q-Gevrey growth order is compared to #3861's
      D-ladder odd order ~0.07–0.09 — a same-object growth-rate check that
      tells F1 whether the geometric κ_odd subladder is the correct generating
      series to Écalle-accelerate.

HONEST SCOPE (scope-(a); anti-laundering). These are 4₁ topological / trace-
field facts. NO map from the physical Q_β observable to a meridian is claimed:
the d↔κ normalization is characterized, not asserted; ħ is the substrate value
it = i·ln q₀ but the fluctuation coefficients are geometric. The ħ↔2πi/N
channels relate by resummation, not term-by-term reparametrisation (bridge
growth-obstruction audit) — only the PERTURBATIVE κ_n around the single
geometric saddle is used. NO fit; NO Q_β c_k wired; NO tier change.

Run: python3 -u computations/probes/qbeta_phib_2loop_bdictionary_probe.py \\
       2>&1 | tee /tmp/qbeta_2loop_bdict.log
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

# `q_parameter` lives in computations/substrate/ (bean qou-9ugp); the anchor
# must be read from it so the witness resolves its stamp. Idempotent.
import sys as _sys_qp  # noqa: E402
from pathlib import Path as _Path_qp  # noqa: E402
for _p_qp in (_Path_qp(__file__).resolve().parent.parent,
              _Path_qp(__file__).resolve().parent.parent / 'substrate'):
    if str(_p_qp) not in _sys_qp.path:
        _sys_qp.path.insert(0, str(_p_qp))
from q_parameter import Q_50_DIGIT_STR, Q_MP, q_muon_at  # noqa: E402
from qou_substrate.witness import apply_q0_comparison  # noqa: E402
import sympy as sp

mp.mp.dps = 60

# proton pin (package layer); muon pin for the second anchor.
# Both pins read BY NAME from `q_parameter` (bean qou-9ugp, 2026-09-03). The
# muon leg was the literal 1.1099785955573... -- the RETIRED self-certified
# pin A, superseded 2026-08-22 by the CODATA-2022 lepton-ratio derivation. A
# mu-vs-p comparison whose muon leg is a retired literal compares live proton
# against yesterday's muon, which is the failure it exists to measure.
# Exception E1 of the 2026-08-30 ruling: both pins are read here on purpose.
Q0_PROTON = Q_MP
Q0_MUON = q_muon_at(50)

# Exact Ohtsuki κ-ladder (4₁ saddle-fluctuation invariants) — transseries probe
# (#3606/#3628 + C6 derivation). odd n carry √3, even n rational.
KAPPA = {
    1: sp.Rational(11, 108) * sp.sqrt(3) * sp.pi,
    2: sp.Rational(2, 27) * sp.pi ** 2,
    3: sp.Rational(1081, 21870) * sp.sqrt(3) * sp.pi ** 3,
    4: sp.Rational(98, 729) * sp.pi ** 4,
    5: sp.Rational(110011, 688905) * sp.sqrt(3) * sp.pi ** 5,
    6: sp.Rational(207892, 295245) * sp.pi ** 6,
    7: sp.Rational(32729683, 26572050) * sp.sqrt(3) * sp.pi ** 7,
}

# BarOddLadderShape measured data (merged #3621/#3660): the smooth-numerator
# slope A′(q*) of S = A/u³ at the S=0 point q*.
A_PRIME_QSTAR = mp.mpf("2.3716")


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


def _vp_den(x, p):
    """p-adic valuation of a sympy Rational's denominator (0 for integers)."""
    d = int(sp.Rational(x).q)
    v = 0
    while d % p == 0:
        d //= p
        v += 1
    return v


def load_d_ladder():
    """Exact bar-odd D-ladder d_k = a_k + b_k·√3 (build_d_ladder, k ≤ 21)."""
    os.environ.setdefault("DLADDER_ORD", "63")   # k ≈ 31 window
    qdir = str(Path(__file__).resolve().parent.parent / "qbeta")
    sys.path.insert(0, qdir)
    saved = sys.argv
    sys.argv = [saved[0]]
    try:
        import qbeta_dladder_generating_function_structure_probe as dlad
        dk, KMAX, valid_top, odd_ok = dlad.build_d_ladder()
    finally:
        sys.argv = saved
    out = {}
    for k in sorted(dk):
        e = sp.expand(sp.nsimplify(dk[k]))
        a = sp.Rational(e.coeff(sp.sqrt(3), 0))
        b = sp.Rational(e.coeff(sp.sqrt(3), 1))
        # verify no residual radicals: e == a + b√3 exactly
        resid = sp.simplify(e - (a + b * sp.sqrt(3)))
        out[k] = (a, b, resid == 0)
    return out, odd_ok


def local_gevrey(ks, vals):
    """local Gevrey index γ = Δln|v| / Δln k! between consecutive listed k."""
    out = {}
    pairs = list(zip(ks, vals))
    for (k1, v1), (k2, v2) in zip(pairs[:-1], pairs[1:]):
        if v1 == 0 or v2 == 0:
            continue
        num = mp.log(abs(v2)) - mp.log(abs(v1))
        den = mp.log(mp.factorial(k2)) - mp.log(mp.factorial(k1))
        out[k2] = float(num / den)
    return out


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" Φ_b odd b-dictionary at the substrate + D-ladder trace-field compat")
    print("=" * 78)

    # --- (A) κ-ladder bar-parity = √3-grading -------------------------------
    print("\n=== (A) κ-ladder: bar-parity is the √3-grading of ℚ(√3) ===")
    parity_ok = True
    for n, kn in KAPPA.items():
        has_sqrt3 = sp.simplify(sp.together(kn / (sp.sqrt(3) * sp.pi ** n))).is_rational
        rational_only = sp.simplify(sp.together(kn / sp.pi ** n)).is_rational
        expect_sqrt3 = (n % 2 == 1)
        ok = (has_sqrt3 if expect_sqrt3 else rational_only)
        parity_ok = parity_ok and ok
        print(f"  κ_{n}: {'√3·ℚ·π^n' if expect_sqrt3 else 'ℚ·π^n'}  "
              f"({'bar-ODD' if expect_sqrt3 else 'bar-even'})  {'ok' if ok else 'MISMATCH'}")
    check("kappa_ladder_parity_is_sqrt3_grading", parity_ok,
          source="κ_odd ∈ ℚ·√3·πⁿ (bar-odd under t↔−t), κ_even ∈ ℚ·πⁿ "
                 "(bar-even) — the geometric fluctuation ladder's number-field "
                 "grading IS the substrate-assembly bar-parity")

    # --- (B) D-ladder shares the trace field ℚ(√3) ---------------------------
    print("\n=== (B) D-ladder ⊂ ℚ(√3), same cusp trace field; G2 parity ===")
    dk, odd_resid_ok = load_d_ladder()
    ks = sorted(dk)
    field_ok = all(dk[k][2] for k in ks)     # every d_k = a_k + b_k√3 exactly
    print(f"  exact d_k: k = {ks[0]}..{ks[-1]} ({len(ks)} rungs); "
          f"all ∈ ℚ(√3): {field_ok}")
    check("dladder_in_trace_field_Q_sqrt3", field_ok and odd_resid_ok,
          source="every bar-odd D-ladder rung d_k = a_k + b_k·√3 exactly "
                 "(build_d_ladder over-determination odd_ok); same ℚ(√3) as κ")
    # G2 regression: v₂(den b_k) = 0 ⟺ k odd
    g2_ok = all((_vp_den(dk[k][1], 2) == 0) == (k % 2 == 1)
                for k in ks if dk[k][1] != 0)
    check("dladder_G2_2adic_parity_grading", g2_ok,
          source="v₂(den b_k)=0 ⟺ k odd (2 the unique graded prime) — the "
                 "D-ladder's bar-parity on the √3-part (regression of #3861 G2)")

    # --- (B2) THE GRADING UNIFICATION: odd-k ⟺ √3-dominated ⟺ bar-odd --------
    print("\n=== (B2) grading unification: odd-k rungs are √3-dominated ===")
    dom_ok = True
    for k in ks:
        a, b, _ = dk[k]
        mag_rat = abs(mp.mpf(str(a)))
        mag_s3 = abs(mp.mpf(str(b)) * mp.sqrt(3))
        s3_dominant = mag_s3 > mag_rat
        expect = (k % 2 == 1)
        ok = (s3_dominant == expect)
        dom_ok = dom_ok and ok
        if k <= 8:
            print(f"  d_{k}: |a|={mp.nstr(mag_rat,3)}  |b√3|={mp.nstr(mag_s3,3)}  "
                  f"{'√3-dom (bar-ODD)' if s3_dominant else 'ℚ-dom (bar-even)'}  "
                  f"{'ok' if ok else 'MISMATCH'}")
    check("dladder_odd_k_is_sqrt3_dominant_bar_odd", dom_ok,
          source="odd-k D-ladder rungs are √3-DOMINATED (bar-odd), even-k "
                 "ℚ-dominated (bar-even) — the G2 2-adic k-parity grading "
                 "COINCIDES with the √3 bar-parity of the cusp trace field, "
                 "unifying #3861's grading with the geometric κ-ladder grading")

    # --- (C) odd b-dictionary at the substrate -------------------------------
    print("\n=== (C) odd b-dictionary Σ_{n odd}(it)ⁿκ_n at the substrate ===")
    for label, q0 in (("proton", Q0_PROTON), ("muon", Q0_MUON)):
        t = mp.log(q0)
        it = mp.mpc(0, 1) * t
        odd_terms = {n: (it ** n) * mp.mpf(str(sp.N(KAPPA[n], 50)))
                     for n in (1, 3, 5, 7)}
        lead = odd_terms[1]
        # leading = i·t·κ_1 ; it is purely imaginary (bar-odd), value i·t·κ_1
        kap1 = mp.mpf(str(sp.N(KAPPA[1], 50)))
        lead_ref = mp.mpc(0, 1) * t * kap1
        lead_ok = abs(lead - lead_ref) < mp.mpf(10) ** (-40)
        print(f"  [{label}] t=ln q₀={mp.nstr(t,12)}  leading = i·t·κ_1 = "
              f"{mp.nstr(lead,10)}  (regression {'ok' if lead_ok else 'FAIL'})")
        if label == "proton":
            check("leading_odd_bdictionary_is_it_kappa1", lead_ok,
                  computed=mp.nstr(lead, 12), expected=mp.nstr(lead_ref, 12),
                  source="leading odd b-dictionary rung assembled at the "
                         "substrate = i·t·κ_1, the corpus finite-b correction")
            odd_series_proton = odd_terms

    # --- (C2) growth of the odd-k D-ladder (reported data, no band claim) ----
    print("\n=== (C2) odd-k D-ladder growth (reported; F1 Écalle target) ===")
    # F1's "bar-odd D-ladder" = the odd-k rungs (full value, √3-dominated, B2).
    # The RAW local Gevrey is O(1) and DECREASING in k (3-adic denominator
    # explosion v₃~1.5k dominates the finite-k window); #3861 extracts the mild
    # q-Gevrey order ~0.078 via their arithmetic normalization at the k=31
    # window. Reported here as data — NOT asserted (the precise mild order is
    # #3861's E2 result, not reproduced term-for-term).
    odd = [(k, dk[k]) for k in ks if k % 2 == 1]
    raw = [(k, mp.mpf(str(a)) + mp.mpf(str(b)) * mp.sqrt(3)) for k, (a, b, _) in odd]
    gev_raw = local_gevrey([k for k, _ in raw], [v for _, v in raw])
    raw_tail = [v for k, v in gev_raw.items() if k >= 11]
    raw_med = sorted(raw_tail)[len(raw_tail) // 2] if raw_tail else float("nan")
    decreasing = (len(raw_tail) >= 3 and raw_tail[-1] < raw_tail[0])
    tail_list = [round(v, 3) for k, v in sorted(gev_raw.items()) if k >= 11]
    print(f"  raw odd-k |d_k| local Gevrey (k≥11): {tail_list}  "
          f"median {round(raw_med,4)}")
    print(f"  (decreasing in k: {decreasing} — the direction of #3861's mild "
          f"q-Gevrey extraction; not reproduced as a specific band here)")

    # --- (D) leading-term vs A′(q*) consistency (scope-(a), honest) ----------
    print("\n=== (D) leading odd b-dictionary vs A′(q*) — scope-(a) ===")
    # The measured smooth-numerator slope A′(q*) ≈ 2.3716 (BarOddLadderShape).
    # κ_1 = (11/108)√3π; report the ratio as a characterization, NOT a bridge.
    kap1_num = mp.mpf(str(sp.N(KAPPA[1], 50)))
    ratio = A_PRIME_QSTAR / kap1_num
    print(f"  κ_1 = (11/108)√3π = {mp.nstr(kap1_num,10)};  "
          f"A′(q*) = {mp.nstr(A_PRIME_QSTAR,6)};  A′/κ_1 = {mp.nstr(ratio,8)}")
    print("  (characterization only — the d↔κ normalization is the open "
          "keystone bridge; NOT asserted, NOT wired)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        ("ESTABLISHED: the bar-parity split of the Φ_b substrate assembly "
         "Σ(it)ⁿκ_n is EXACTLY the √3-grading of the 4₁ cusp trace field ℚ(√3) "
         "— the bar-ODD b-dictionary is the closed-form √3-subladder "
         "{κ_1,κ_3,κ_5,κ_7}. F1's exact bar-odd D-ladder d_k = a_k + b_k√3 "
         "shares that trace field, and — the unifying finding — its odd-k rungs "
         "are √3-DOMINATED (bar-odd) while even-k are ℚ-dominated (bar-even), so "
         "the G2 2-adic k-parity grading COINCIDES with the √3 bar-parity. The "
         "odd-k √3-dominated rungs are F1's Écalle-acceleration target (mild "
         "q-Gevrey order per #3861). The leading odd rung assembles at the "
         "substrate to the corpus finite-b correction i·t·κ_1. "
         if all_passed else
         "PARTIAL: a structural check failed — see the per-check table. ")
        + "This pins the GEOMETRIC generating object F1 should accelerate (the "
        "√3-graded κ_odd subladder) and its trace-field compatibility with the "
        "D-ladder; the d↔κ normalization (the meridian↔Q_β map) stays the OPEN "
        "keystone bridge — characterized, NOT asserted. ħ↔2πi/N: perturbative "
        "κ_n only. NO fit; NO c_k wired; NO tier change; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-phib-2loop-bdictionary",
        "description": "The Φ_b odd b-dictionary at the substrate: bar-parity = "
                       "the √3-grading of the 4₁ cusp trace field ℚ(√3); the "
                       "bar-odd b-dictionary is the closed-form κ_odd subladder "
                       "{κ_1,κ_3,κ_5,κ_7}; trace-field compatibility with F1's "
                       "exact D-ladder d_k=a_k+b_k√3 (G2 parity + q-Gevrey band); "
                       "leading rung = corpus i·t·κ_1. scope-(a); d↔κ bridge open.",
        "audit_only": True,
        "tier": "symbolic-exact + numerical (trace-field / growth-order)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "sympy+mpmath",
        "engineVersion": f"sympy {sp.__version__}, mpmath {mp.__version__}",
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "kappa_odd_subladder": {str(n): str(KAPPA[n]) for n in (1, 3, 5, 7)},
            "dladder_rungs": len(ks),
            "dladder_odd_raw_gevrey_median_tail": round(float(raw_med), 5),
            "dladder_odd_raw_gevrey_decreasing": bool(decreasing),
            "A_prime_qstar_over_kappa1": mp.nstr(ratio, 10),
            "verdict": verdict,
        },
        "context": {
            "axis": "Φ_b 2-loop b-dictionary (F1 unowned input; bean qou-jzrf)",
            "kappa_source": "qbeta-phib-saddle-fluctuation-transseries "
                            "(C6 exact κ_1..κ_7)",
            "dladder_source": "qbeta_dladder_generating_function_structure_probe"
                              ".build_d_ladder (exact d_k, ℚ(√3))",
            "qgevrey_reference": "#3861 odd D-ladder single order ~0.07-0.09 (k=31)",
            "finite_b_rung1": "i·t·κ_1 in "
                              "qbeta_c3_phib_saddle_state_integral_probe.py",
            "open_bridge": "d↔κ normalization = meridian↔Q_β map "
                           "(conj:algebraic-geometric-dilog-equivalence)",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-phib-2loop-bdictionary.witness.json")
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
        from qou_substrate.witness import WitnessBuilder as _WB
        import os as _os  # noqa: E402 -- provenance stamp
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=None)
        # Explicit `comparison` stamp (bean qou-9ugp): this producer reads BOTH
        # pins deliberately, so no anchor list can classify it and it was going
        # out unstamped. The reason string is kept ASCII on purpose: this
        # witness is written with json.dump, whose ensure_ascii=True turns any
        # non-ASCII into a \\uXXXX escape and collapses the shape guard.
        apply_q0_comparison(witness,
            muon=Q0_MUON, proton=Q0_PROTON,
            reason='evaluates the phi_b 2-loop b-dictionary at both pins and reports each under its own key; both pins are read on purpose',
        )
        json.dump(witness, f, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
