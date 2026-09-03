#!/usr/bin/env python3
"""KSel-2-ID transport: the E-shift of the lattice class is EXACT algebra.

The u1-promotion audit (docs/audits/2026-08-01-ksel2id-u1-promotion.md)
left the balanced-vs-SW class transfer conditional on an unproved
PERTURBATION LEMMA (its §4 gap 1): "Jacobi matrices whose coefficients
converge geometrically to those of an indeterminate reference have
N-extremal supports with the same asymptotic lattice class."

This probe shows that lemma is NOT NEEDED for the class statement. The
transport can be run on the moment RATIOS (the tropical / Newton-polygon
roots) instead of on the Jacobi data, and there it is exact:

    m_k = G_k · E^k · (p;p)_k                      (the exact factorization,
                                                    Lean: SWJacksonMomentFactorization)
    ⇒ m_{k+1}/m_k = (G_{k+1}/G_k) · E · (1 − p^{k+1})     [T1, exact]
      G_{k+1}/G_k = q̃^k                                   [T2, exact]
    ⇒ log_q̃(m_{k+1}/m_k) = k + log_q̃ E + log_q̃(1 − p^{k+1})

so the SW core's tropical class is exactly 0 at EVERY k [T2], and the
balanced tropical class is φ₁ = frac(log_q̃ E) up to an error that is
bounded explicitly and decays geometrically at rate p [T3].

Net effect on the gap list: the two-step chain
  (SW class) --perturbation lemma--> (balanced class)
is replaced by
  (SW class = 0, exact) --exact algebra + geometric limit--> (balanced class = φ₁),
leaving ONE analytic residual — "extremal support class = tropical class"
— which is the SAME statement the pure SW core already needs (the A_w
zero asymptotics, audit §4 gap 2). No new analytic input is introduced.

[T4] records the pin behaviour HONESTLY. The tropical route is *not*
numerically cheaper at the pins: reaching 1e-12 still takes k ≈ 293
(comparable to the truncation route's N ≈ 375). The difference is not
depth but KIND — the tropical error has a closed-form bound
|log_q̃(1 − p^{k+1})|, so the limit is a theorem rather than an
extrapolation, and no computation at any depth is needed to establish
the class. The k-values below are illustrative, not evidence.

NO FIT. Audit-only; nothing wired. Every scored check is an exact
symbolic identity or a numeric check of a displayed bound.
"""

from __future__ import annotations

import hashlib
import json
import os
import platform
import subprocess
import time
from pathlib import Path

import sympy as sp
from mpmath import mp, mpf, log as mlog, floor as mfloor, nstr


def fmt(x) -> str:
    """mpf-safe short decimal string (mpf has no __format__)."""
    return nstr(mpf(x), 6)

HERE = Path(__file__).resolve().parent
WITNESS = HERE / "ksel2id-tropical-transport.witness.json"

mp.dps = 60

# Substrate pins (evaluation points only, no CODATA read). RESOLVED, not frozen:
# the literal here was the superseded muon pin A, which stopped being the muon
# anchor when PR #5500 re-derived it to CODATA-2022, so the probe went on
# evaluating at a retired anchor under the name Q_MUON. The pair evaluated is
# "the substrate pin and its inverse" -- the muon naming was incidental, not a
# proton-vs-muon comparison -- so it resolves the PROTON pin per the owner
# directive of 2026-08-15 (bean qou-1c4y).
import sys as _sys, pathlib as _pl  # noqa: E402
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: F401, E402

from substrate.q_parameter import Q_50_DIGIT_STR as _Q0_RESOLVED  # noqa: E402

Q_SUBSTRATE = _Q0_RESOLVED
Q_MUON = Q_SUBSTRATE          # kept as an alias: the key names below are load-bearing
PINS = {"muon_pin": Q_MUON, "inverse_muon_pin": None}  # inverse filled below

results: dict = {}
t0 = time.time()


def log(msg: str) -> None:
    print(f"[{time.time() - t0:7.1f}s] {msg}", flush=True)


# ---------------------------------------------------------------- T1, T2
def block_t1_t2_exact() -> dict:
    """Exact symbolic identities for the moment ratio and the SW ratio."""
    log("T1/T2: exact symbolic ratio identities ...")
    v, k = sp.symbols("v k", positive=True)  # v = q̃, so q = v**2, p = v**-2

    def G(n):  # SW core moments q̃^{n(n-1)/2}
        return v ** sp.Rational(n * (n - 1), 2)

    def qint_fact(n, q):  # [n]_q!
        out = sp.Integer(1)
        for j in range(1, n + 1):
            out *= sum(q ** i for i in range(j))
        return out

    def m(n):  # balanced normalizer N^bal(n+1) = q̃^{-C(n,2)}·[n]_q!  (q = v²)
        q = v ** 2
        return v ** sp.Rational(-n * (n - 1), 2) * qint_fact(n, q)

    q = v ** 2
    p = 1 / q
    E = 1 / (1 - p)

    t1_ok, t2_ok, fact_ok = [], [], []
    for n in range(0, 13):
        # T1: m_{n+1}/m_n = (G_{n+1}/G_n)·E·(1 − p^{n+1})
        lhs = sp.simplify(m(n + 1) / m(n))
        rhs = sp.simplify((G(n + 1) / G(n)) * E * (1 - p ** (n + 1)))
        t1_ok.append(sp.simplify(lhs - rhs) == 0)
        # T2: G_{n+1}/G_n = q̃^n  (exact, so tropical class of the core ≡ 0)
        t2_ok.append(sp.simplify(G(n + 1) / G(n) - v ** n) == 0)
        # the factorization itself (Lean-proved; re-checked here)
        poch = sp.prod([1 - p ** j for j in range(1, n + 1)])
        fact_ok.append(sp.simplify(m(n) - G(n) * E ** n * poch) == 0)

    assert all(t1_ok), "T1 exact ratio identity failed"
    assert all(t2_ok), "T2 exact SW ratio failed"
    assert all(fact_ok), "factorization re-check failed"
    log("T1/T2:   -> exact for n <= 12 (ratio identity, SW ratio, factorization)")
    return {
        "t1_ratio_identity_exact_upto_n": 12,
        "t2_sw_ratio_is_qtilde_pow_exact_upto_n": 12,
        "t2_sw_tropical_class_exact": "0 at every k (no asymptotics)",
        "factorization_recheck_exact_upto_n": 12,
        "identity": "m_{k+1}/m_k = q̃^k · E · (1 − p^{k+1});  E = 1/(1−p), p = 1/q",
    }


# -------------------------------------------------------------------- T3
def tropical_class_dev(qstr: str, kmax: int) -> list[tuple[int, mpf, mpf]]:
    """|frac(log_q̃(m_{k+1}/m_k)) − φ₁| and the displayed geometric bound."""
    q = mpf(qstr)
    v = sp.sqrt(q) if False else q ** mpf("0.5")
    p = 1 / q
    E = 1 / (1 - p)
    lv = mlog(v)
    phi1 = mlog(E) / lv
    phi1 = phi1 - mfloor(phi1)
    out = []
    for k in range(0, kmax + 1):
        # exact ratio, no truncation: log_q̃(m_{k+1}/m_k) = k + log_q̃E + log_q̃(1−p^{k+1})
        lr = k + mlog(E) / lv + mlog(1 - p ** (k + 1)) / lv
        cls = lr - mfloor(lr)
        dev = abs(cls - phi1)
        if dev > mpf("0.5"):  # wrap-around near the class boundary
            dev = 1 - dev
        bound = abs(mlog(1 - p ** (k + 1)) / lv)
        out.append((k, dev, bound))
    return out


def block_t3_geometric() -> dict:
    """The deviation is bounded by the displayed term and decays at rate p."""
    log("T3: explicit geometric error bound across a q-ladder ...")
    rows = []
    ladder = ["2.0736", "1.8", "1.5", "1.3", "1.2", "1.15", Q_MUON,
              str(1 / mpf(Q_MUON))]
    for qstr in ladder:
        q = mpf(qstr)
        p = 1 / q if q > 1 else q  # inverse pin: use the >1 representative
        data = tropical_class_dev(qstr if q > 1 else str(1 / q), 60)
        # bound must dominate the deviation at every k
        dominates = all(d <= b * (1 + mpf("1e-30")) for _, d, b in data)
        # measured decay rate of the bound: bound_{k+1}/bound_k → p
        pk = min(1 / q, q) if q != 1 else mpf(1)
        r_meas = data[40][2] / data[39][2]
        rate_err = abs(r_meas - pk) / pk
        # PREDICTED tolerance, not a fitted one: expanding
        # bound_k = −log(1−p^{k+1})/ln q̃ = (p^{k+1} + p^{2k+2}/2 + …)/ln q̃
        # gives bound_{k+1}/bound_k = p·(1 + O(p^{k+1})), so the relative
        # rate error at k = 39 is O(p^{40}); allow one order of slack.
        rate_tol = 10 * pk ** 40
        rows.append({
            "q": qstr,
            "dev_k10": fmt(data[10][1]),
            "dev_k30": fmt(data[30][1]),
            "bound_k30": fmt(data[30][2]),
            "bound_dominates_dev": bool(dominates),
            "measured_rate": nstr(mpf(r_meas), 15),
            "predicted_rate_p": nstr(mpf(pk), 15),
            "rate_rel_err": fmt(rate_err),
            "rate_rel_err_predicted_tol": fmt(rate_tol),
        })
        assert dominates, f"bound failed to dominate at q={qstr}"
        assert rate_err < rate_tol, (
            f"rate mismatch at q={qstr}: {nstr(mpf(rate_err), 6)} "
            f"exceeds predicted {nstr(mpf(rate_tol), 6)}")
        log(f"T3:   -> q = {qstr}: dev(k=30) = {fmt(data[30][1])}, "
            f"rate = p to {fmt(rate_err)}")
    return {"ladder": rows,
            "bound": "|class(k) − φ₁| ≤ |log_q̃(1 − p^{k+1})| ≤ p^{k+1}/((1−p)·ln q̃)",
            "decay_rate": ("p = 1/q; the measured ratio matches p within the "
                           "PREDICTED O(p^{k+1}) correction at every rung")}


# -------------------------------------------------------------------- T4
def block_t4_pins() -> dict:
    """Pin behaviour, reported honestly: depth is comparable to the
    truncation route; the advantage is the closed-form bound, not speed."""
    log("T4: pin certification depth for the tropical route ...")
    out = {}
    for name, qstr in (("muon_pin", Q_MUON),
                       ("inverse_muon_pin", str(1 / mpf(Q_MUON)))):
        qq = mpf(qstr)
        rep = qstr if qq > 1 else str(1 / qq)
        data = tropical_class_dev(rep, 2000)
        k_1em12 = next(k for k, d, _ in data if d < mpf("1e-12"))
        k_1em30 = next(k for k, d, _ in data if d < mpf("1e-30"))
        out[name] = {"k_for_1e-12": k_1em12, "k_for_1e-30": k_1em30,
                     "dev_at_k1000": fmt(data[1000][1])}
        log(f"T4:   -> {name}: 1e-12 at k = {k_1em12}, 1e-30 at k = {k_1em30}")
        assert k_1em12 < 2000
    out["contrast"] = (
        "HONEST: the tropical route is NOT numerically cheaper at the pins "
        "(k ≈ 293 for 1e-12 vs the truncation route's N ≈ 375). Its advantage "
        "is of kind, not speed: the error carries the closed-form bound "
        "|log_q̃(1−p^{k+1})|, so the class limit is proved rather than "
        "extrapolated, and no depth is required to establish it. The k values "
        "here are illustrative only.")
    out["inverse_pin_note"] = (
        "the inverse pin is evaluated through its >1 representative, so its "
        "row duplicates the muon pin by construction (the balanced convention "
        "is bar-invariant); it is not an independent datum")
    return out


def git_sha(path: Path) -> str:
    try:
        return subprocess.run(["git", "log", "-1", "--format=%H", "--", str(path)],
                              capture_output=True, text=True, cwd=HERE,
                              check=False).stdout.strip() or "unknown"
    except Exception:
        return "unknown"


def main() -> None:
    results["t1_t2_exact"] = block_t1_t2_exact()
    results["t3_geometric"] = block_t3_geometric()
    results["t4_pins"] = block_t4_pins()
    results["verdict"] = {
        "claim": ("the balanced tropical (moment-ratio) lattice class equals the "
                  "SW-core class shifted by log_q̃ E, exactly, with an explicit "
                  "geometrically-decaying error — no perturbation lemma"),
        "sw_core_tropical_class": "0, exact at every k (T2)",
        "balanced_tropical_class": "φ₁ = frac(log_q̃ E), limit with rate p (T1+T3)",
        "residual": ("ONE analytic statement — extremal support class = tropical "
                     "class — which is the same input the pure SW core already "
                     "requires (A_w zero asymptotics); the u1-promotion audit's "
                     "§4 gap 1 (perturbation lemma) is thereby dissolved, not "
                     "proved"),
        "scope": ("scope-(a) throughout; nothing wired; the target conjecture is "
                  "unchanged in kind"),
    }
    src = Path(__file__)
    # Provenance fields required by computations/audits/witness_provenance_audit.py
    # (REQUIRED_FIELDS = engine/scriptFile/commitSha); shape matches the sibling
    # ksel2id_* probes. Addresses Copilot review on PR #4446.
    head_sha = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True,
                              text=True, cwd=HERE, check=False).stdout.strip() or "unknown"
    script_hash = hashlib.sha256(src.read_bytes()).hexdigest()[:12]
    witness = {
        "schema": "witness/v1",
        "engine": "sympy+mpmath",
        "engineVersion": f"python {platform.python_version()}",
        "commitSha": head_sha,
        "scriptFile": src.name,
        "scriptHash": script_hash,
        "scriptCommitSha": git_sha(src),
        "computation": "ksel2id-tropical-transport",
        "description": ("KSel-2-ID tropical transport: the E-shift of the lattice "
                        "class is exact algebra on moment ratios, dissolving the "
                        "perturbation lemma"),
        "auditOnly": "docs/audits/2026-08-01-ksel2id-tropical-transport.md",
        "allPassed": True,
        "precisionMetadata": {"compute_dps": mp.dps, "symbolic": "sympy exact"},
        "data": results,
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. This producer DOES read q0, so the anchor
    # is resolved and stamped rather than suppressed (qou-1c4y).
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    # q0_anchor was `False`, i.e. "this witness carries no q0-dependent field".
    # Untrue: this producer reads q0 and records it, so the false declaration
    # DELETED the anchor stamp on every run, converting a visible Q0_FLIP into a
    # silent Q0_ANCHOR_MISSING (bean qou-1c4y). Resolving is the default.
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None)
    WITNESS.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\n✓ Witness: {WITNESS.name}  (3 assertion blocks, all passed)")
    print("witness saved; all assertions passed.")


if __name__ == "__main__":
    main()
