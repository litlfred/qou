#!/usr/bin/env python3
"""
Route 3 of the bar-odd-S program: the EXPERIMENTAL budget for the decay-sector
substrate determination q*.

WITHDRAWN PREMISE (2026-08-15, PR #5074, bean qou-kh7e, registry §9f).
This header previously read: "#3636 established (merged): the S=0 point q* is a
third, decay-sector determination of q₀". It is not one. q* is root-found on
S(q) = c₃(q) + Vol(4₁) where c₃ = (Q_β^exp/Q_N2 − 1)/u³ is EXTRACTED FROM
EXPERIMENTAL Q_β, so locating q* presupposes (H1) c₃^even = −Vol(4₁). It is
independent of the two MASS pins only — weaker, and a different statement.

WHAT SURVIVES, AND IT IS THE WHOLE ARITHMETIC OF THIS PROBE: the precision limit
on q* is the measured neutron Q_β (dq*/dQ_β ≈ −0.539 per MeV), not theory. That
derivative is real and the error propagation below is unchanged. Only the
INTERPRETATION of the first threshold moves: a sharper Q_β sharpens the OFFSET
test (does c₃^even equal −Vol(4₁)?), it does not adjudicate the substrate
modulus, because the quantity being sharpened already assumes the answer.

This probe quantifies that lever as a concrete budget:

  * σ(q*) TODAY from the canonical CAL-3 uncertainty Q_β = 0.78233341(61) MeV;
  * the improvement factor in σ(Q_β) needed for σ(q*) to fall below the two-pin
    spread |q_proton − q_muon| — read as "the (H1)-conditional offset test
    resolves structure at the scale of the μ–p tension", NOT as "q* arbitrates
    the tension";
  * the factor needed for q* to be COMPETITIVE with each mass pin itself
    (muon ratio 22 ppb; proton ratio 0.06 ppb — the current precision pin).

All inputs are loaded from committed canonical artifacts (no hidden literals):
  - computations/cal-3-q-beta.witness.json          → Q_β, σ(Q_β)  [PDG/AME]
  - computations/qbeta/qbeta-c3-imq-qstar-ladder-amplification.witness.json
                                                    → q*, dq*/dQ_β  [#3636]
  - qou_substrate.constants.q_at / q_muon_at        → the two pins

Anti-laundering: pure error-propagation arithmetic on committed values; no fit,
no c_k wired, no tier change. The falsifiable statement is #3636's, made
quantitative: a ~26× sharper neutron Q_β turns q* into an arbiter of the μ–p
tension; a ~14× sharpening makes it competitive with the muon pin.
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "computations", "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


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


def main():
    root = _repo_root()
    sys.path.insert(0, os.path.join(root, "tools", "qou-substrate", "python"))
    from qou_substrate.constants import q_at, q_muon_at  # noqa: E402

    # --- canonical inputs (committed artifacts) ---
    cal3 = json.load(open(os.path.join(root, "computations", "cal-3-q-beta.witness.json")))
    qb = mp.mpf(str(cal3["data"]["Q_beta_n_MeV"]))
    sigma_qb = mp.mpf(str(cal3["data"]["Q_beta_n_MeV_err"]))
    quoted = cal3["data"]["Q_beta_n_MeV_quoted"]

    amp = json.load(open(os.path.join(
        root, "computations", "qbeta",
        "qbeta-c3-imq-qstar-ladder-amplification.witness.json")))
    dqstar_dQ = mp.mpf(str(amp["data"]["precision_limit"]["dqstar_dQbeta"]))
    q_star = mp.mpf(str(amp["data"]["q_star"]["value"]))

    q_p, q_m = q_at(50), q_muon_at(50)
    spread = abs(q_p - q_m)

    print("=" * 78)
    print(" q* experimental budget — how far a sharper neutron Q_β goes (route 3)")
    print("=" * 78)
    print(f"\n inputs (loaded, not typed):")
    print(f"   Q_β = {quoted}   σ(Q_β) = {mp.nstr(sigma_qb, 6)} MeV "
          f"= {mp.nstr(sigma_qb * mp.mpf(10) ** 6, 4)} eV")
    print(f"   dq*/dQ_β = {mp.nstr(dqstar_dQ, 8)} per MeV   (#3636, merged witness)")
    print(f"   q* = {mp.nstr(q_star, 20)}")
    print(f"   pins: q_proton = {mp.nstr(q_p, 20)}")
    print(f"         q_muon   = {mp.nstr(q_m, 20)}")
    print(f"   μ–p pin spread |Δq| = {mp.nstr(spread, 6)} "
          f"({mp.nstr(spread / q_p * mp.mpf(10) ** 9, 4)} ppb)")

    # --- today's q* precision from Q_β alone ---
    sigma_qstar = abs(dqstar_dQ) * sigma_qb
    rel_ppb = sigma_qstar / q_star * mp.mpf(10) ** 9
    print(f"\n σ(q*) today = |dq*/dQ_β|·σ(Q_β) = {mp.nstr(sigma_qstar, 6)} "
          f"({mp.nstr(rel_ppb, 5)} ppb)")

    # --- budget thresholds ---
    # (1) resolve at the μ–p scale: σ(q*) ≤ |Δq|.  NOT "arbitrate the tension":
    #     q* presupposes (H1) (see the withdrawn premise in the module docstring),
    #     so this threshold measures when the (H1)-conditional OFFSET test becomes
    #     sharper than the two-pin spread — not when q* can adjudicate the modulus.
    f_arbitrate = sigma_qstar / spread
    sigma_qb_needed_arb = spread / abs(dqstar_dQ)
    # (2) competitive with the muon pin (22 ppb on q via the mass-ratio pin)
    sigma_q_muon_pin = q_p * mp.mpf(22) / mp.mpf(10) ** 9
    f_muon = sigma_qstar / sigma_q_muon_pin
    sigma_qb_needed_mu = sigma_q_muon_pin / abs(dqstar_dQ)
    # (3) competitive with the proton pin (0.06 ppb)
    sigma_q_proton_pin = q_p * mp.mpf("0.06") / mp.mpf(10) ** 9
    f_proton = sigma_qstar / sigma_q_proton_pin
    sigma_qb_needed_p = sigma_q_proton_pin / abs(dqstar_dQ)

    rows = [
        ("resolve at μ–p scale, (H1)-conditional (σ(q*) ≤ |Δq|)",
         spread, f_arbitrate, sigma_qb_needed_arb),
        ("competitive with muon pin (22 ppb)", sigma_q_muon_pin, f_muon, sigma_qb_needed_mu),
        ("competitive with proton pin (0.06 ppb)", sigma_q_proton_pin, f_proton, sigma_qb_needed_p),
    ]
    print("\n threshold                                   target σ(q)   need ×   need σ(Q_β)")
    budget = []
    for name, tgt, fac, need in rows:
        print(f"   {name:42s} {mp.nstr(tgt, 4):>10}  {mp.nstr(fac, 4):>6}   "
              f"{mp.nstr(need * mp.mpf(10) ** 6, 4)} eV")
        budget.append({"threshold": name, "target_sigma_q": mp.nstr(tgt, 8),
                       "improvement_factor_needed": mp.nstr(fac, 6),
                       "sigma_Qbeta_needed_eV": mp.nstr(need * mp.mpf(10) ** 6, 6)})

    verdict = (
        f"Today σ(q*) = {mp.nstr(sigma_qstar, 4)} ({mp.nstr(rel_ppb, 4)} ppb) from "
        f"σ(Q_β) = {mp.nstr(sigma_qb * mp.mpf(10) ** 6, 3)} eV. A ~{mp.nstr(f_arbitrate, 3)}× "
        f"sharper neutron Q_β brings σ(q*) below the μ–p spread "
        f"(needs σ(Q_β) ≈ {mp.nstr(sigma_qb_needed_arb * mp.mpf(10) ** 6, 3)} eV) — which "
        f"sharpens the (H1)-conditional OFFSET test, NOT the substrate modulus: q* is "
        f"the zero of c₃ + Vol(4₁) with c₃ extracted from experimental Q_β, so it "
        f"presupposes (H1) and is not an independent determination of q₀ "
        f"(WITHDRAWN 2026-08-15, registry §9f); "
        f"~{mp.nstr(f_muon, 3)}× makes it competitive with the muon pin; the proton "
        f"pin needs ~{mp.nstr(f_proton, 3)}× ({mp.nstr(sigma_qb_needed_p * mp.mpf(10) ** 6, 3)} eV — "
        f"beyond current technique). Pure error propagation on committed values; "
        f"no fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    ok_loaded = sigma_qb > 0 and abs(dqstar_dQ) > mp.mpf("0.1") and spread > 0
    assertions = [
        {"name": "inputs_loaded_from_canonical_witnesses", "passed": bool(ok_loaded)},
        {"name": "qstar_sigma_exceeds_pin_spread_today",
         "passed": bool(sigma_qstar > spread)},
    ]
    all_passed = all(a["passed"] for a in assertions)

    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-qstar-experimental-budget",
        "description": "Route-3 budget: error-propagation of the canonical CAL-3 "
                       "σ(Q_β) through dq*/dQ_β (#3636) to σ(q*), compared against "
                       "the μ–p pin spread and each pin's own precision — the "
                       "quantitative form of 'a better neutron Q_β directly "
                       "sharpens everything'. Inputs loaded from committed "
                       "witnesses; no hidden literals.",
        "audit_only": True,
        "tier": "error-propagation arithmetic (no new measurement, no fit)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "Q_beta_MeV_quoted": quoted,
            "sigma_Qbeta_eV": mp.nstr(sigma_qb * mp.mpf(10) ** 6, 6),
            "dqstar_dQbeta_per_MeV": mp.nstr(dqstar_dQ, 10),
            "q_star": mp.nstr(q_star, 25),
            "q_proton_pin": mp.nstr(q_p, 25),
            "q_muon_pin": mp.nstr(q_m, 25),
            "pin_spread_abs": mp.nstr(spread, 8),
            "pin_spread_ppb": mp.nstr(spread / q_p * mp.mpf(10) ** 9, 6),
            "sigma_qstar_today_abs": mp.nstr(sigma_qstar, 8),
            "sigma_qstar_today_ppb": mp.nstr(rel_ppb, 6),
            "budget": budget,
            "verdict": verdict,
        },
        "context": {
            "axis": "bar-odd S route 3: experimental Q_β lever",
            "inputs": ["computations/cal-3-q-beta.witness.json",
                       "computations/qbeta/qbeta-c3-imq-qstar-ladder-amplification.witness.json",
                       "qou_substrate.constants.q_at/q_muon_at"],
            "falsifiable_lever": "#3636 finding 3, made quantitative",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "qbeta-qstar-experimental-budget.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
