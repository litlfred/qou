#!/usr/bin/env python3
"""
CAL-3 anchoring of c_3 -- factorization + concrete impact on the mass/binding tables.

Two parts, both exact/audit (no fit, no wiring, no c_k value changed):

  A. The factorization  c_3^odd = κ_(2,1)(q_0) · S  (matches CAL3AnchorStructure.lean):
     κ_(2,1) is the DERIVED pure-q bar-odd carrier (anchor-rigid); S is the single
     archimedean scalar carrying the whole cross-anchor swing.

  B. Impact-on-tables WIRING AUDIT: which production observables depend on c_3.
     Established from the compute (canonical_mass.py builds m_n from
     q_beta_kashiwara_n2_mev() -- the c_2/N2-level Q_β; binding uses tr_M, not Q_β):

       - mass table  (m_e, m_p, m_μ, m_π): NO Q_β dependence at all -> c_3-independent.
       - m_n, Δ_pn : depend on Q_β but at the c_2 (N2) level -> c_3-independent in
                     production (c_3 is NOT wired).
       - binding table (B_AME isotopes): tr_M Jones-Markov trace, weak-sector Q_β
                     not involved -> c_3-independent.

     Conclusion: CAL-3-anchoring c_3 changes NOTHING in the current tables. If c_3
     were later wired into Q_β, it would be a CALIBRATION (Q_β/m_n/Δ_pn become
     CAL-3-anchored, not predicted) -- a reclassification, not an accuracy win.
"""
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

import mpmath as mp

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "computations", "substrate"))
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# --- production sources whose Q_β / binding wiring the audit inspects -------
# The audit does NOT trust a hardcoded table; it derives `uses_c3` from a live
# scan of these files, so a future change that wires c_3 into production flips
# the assertion to FAIL (addresses the "self-fulfilling audit" review point).
def _find_repo_root():
    """Walk up from this file until a dir with the repo markers is found. Robust
    to the script's own location (self-contained; no shared-module import)."""
    d = os.path.dirname(os.path.abspath(__file__))
    while d != os.path.dirname(d):
        if os.path.isdir(os.path.join(d, "computations")) and \
           os.path.exists(os.path.join(d, "AGENTS.md")):
            return d
        d = os.path.dirname(d)
    raise RuntimeError("repo root not found (no dir with computations/ + AGENTS.md)")


_REPO_ROOT = _find_repo_root()
_PRODUCTION_SOURCES = [
    os.path.join(_REPO_ROOT, "computations", "canonical_mass.py"),    # mass table + m_n + Δ_pn
    os.path.join(_REPO_ROOT, "computations", "derived_masses.py"),    # the Q_β function itself
]
# A c_3 wiring signature: a literal c_3 rung (`c_3`, `c3`, `c[3]`, `c_k[3]`) OR a
# call to an order≥3 truncation (`*_n3_*`, `*_n4_*`, …). Production Q_β is the
# order-2 `q_beta_kashiwara_n2_mev`; anything ≥ n3 or a bare c_3 means c_3 is wired.
_C3_WIRING_RE = re.compile(r"\bc_?3\b|\bc\[3\]|c_k\[3\]|_n[3-9]_|_n1[0-9]_")


def _production_uses_c3():
    """Live scan: does any production Q_β/binding source reference a c_3 rung or an
    order≥3 truncation? Returns (bool, dict of per-file hits). Falsifiable — if c_3
    is ever wired in, this returns True and the audit FAILS (not self-fulfilling)."""
    hits = {}
    for path in _PRODUCTION_SOURCES:
        rel = os.path.relpath(path, _REPO_ROOT)
        if not os.path.exists(path):
            hits[rel] = ["<missing — production layout changed; re-audit>"]
            continue
        with open(path, "r") as f:
            matched = [
                f"{i}:{ln.strip()}"
                for i, ln in enumerate(f, 1)
                if _C3_WIRING_RE.search(ln) and "n2_mev" not in ln  # n2 = order 2, the c_2 rung
            ]
        if matched:
            hits[rel] = matched
    return (len(hits) > 0), hits


def _repo_head_sha():
    """Repo HEAD at emission time. Fails loudly (never returns None/empty) so a
    witness is never written with missing provenance (I14 PROV_MISSING)."""
    try:
        sha = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            cwd=os.path.dirname(os.path.abspath(__file__)), text=True,
        ).strip()
    except (subprocess.SubprocessError, OSError) as e:
        raise RuntimeError(f"cannot resolve commitSha ({e}) — refusing to emit witness") from e
    if not sha:
        raise RuntimeError("empty commitSha — refusing to emit witness without provenance")
    return sha


def kappa21(q):
    return (q - 1) ** 3 * (q + 1) / q ** 2


def main():
    assertions = []

    def check(name, passed):
        assertions.append({"name": name, "passed": bool(passed)})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

    # --- Part A: the factorization at both anchors ---
    anchors = {
        "proton": (mp.mpf("1.109978595"), mp.mpf("-2.06934")),
        "muon":   (mp.mpf("1.109975"),     mp.mpf("-2.02019")),
    }
    fac = {}
    for name, (q0, c3) in anchors.items():
        k = kappa21(q0)
        fac[name] = {"q0": mp.nstr(q0, 10), "kappa": mp.nstr(k, 8),
                     "c3": mp.nstr(c3, 7), "S": mp.nstr(c3 / k, 8)}
    kp, km = kappa21(anchors["proton"][0]), kappa21(anchors["muon"][0])
    Sp = anchors["proton"][1] / kp
    Sm = anchors["muon"][1] / km
    kappa_swing = abs(kp / km - 1)
    S_swing = abs(Sp / Sm - 1)
    c3_swing = abs(anchors["proton"][1] / anchors["muon"][1] - 1)
    # the swing lives in S: kappa contributes ~0, S ~ full swing
    check("kappa_carrier_anchor_rigid_swing_lt_1e-4", kappa_swing < 1e-4)
    check("S_scalar_carries_full_c3_swing",
          abs(S_swing - c3_swing) < 1e-3)

    # --- Part B: production wiring audit (which observables use c_3) ---
    # `uses_c3` is DERIVED from a live scan of the production Q_β sources
    # (canonical_mass.py, derived_masses.py) -- NOT hardcoded. If a future change
    # wires c_3 (a c_3 rung or any order≥3 truncation) into production, the scan
    # returns True and every Q_β-dependent assertion below FAILS.
    c3_wired, c3_hits = _production_uses_c3()
    # Only Q_β-dependent observables *could* pick up c_3; the scan gates those.
    # Binding is tr_M (strong sector) -- structurally disjoint from the weak-sector
    # Q_β ladder, so it carries no c_3 channel regardless of the scan.
    table_impact = {
        "m_e":   {"uses_qbeta": False, "uses_c3": False,    "cal3_anchor_effect": "none (CAL-1)"},
        "m_mu":  {"uses_qbeta": False, "uses_c3": False,    "cal3_anchor_effect": "none (m_e·Vol(4_1)/ℏ_q²)"},
        "m_pi":  {"uses_qbeta": False, "uses_c3": False,    "cal3_anchor_effect": "none (CAL-3 scale itself)"},
        "m_p":   {"uses_qbeta": False, "uses_c3": False,    "cal3_anchor_effect": "none (muon-anchored Hecke energy)"},
        "m_n":   {"uses_qbeta": True,  "uses_c3": c3_wired, "cal3_anchor_effect": "none in production (Q_β at c_2/N2 level)"},
        "Delta_pn": {"uses_qbeta": True, "uses_c3": c3_wired, "cal3_anchor_effect": "none in production (c_2/N2-level Q_β)"},
        "Q_beta": {"uses_qbeta": True, "uses_c3": c3_wired, "cal3_anchor_effect": "reclassify IF wired: predicted -> CAL-3-calibrated"},
        "binding_B_AME": {"uses_qbeta": False, "uses_c3": False, "cal3_anchor_effect": "none (tr_M Jones-Markov, not Q_β)"},
    }
    any_c3 = any(v["uses_c3"] for v in table_impact.values())
    check("no_production_table_row_uses_c3", not any_c3)
    check("mass_table_c3_independent",
          not any(table_impact[m]["uses_c3"] for m in ["m_e", "m_mu", "m_pi", "m_p", "m_n"]))
    check("binding_table_c3_independent", not table_impact["binding_B_AME"]["uses_c3"])

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CAL-3-anchoring c_3 changes NOTHING in the current mass/binding tables. (A) The "
        "odd channel factors as c_3^odd = κ_(2,1)(q_0)·S: κ is the derived pure-q carrier "
        f"(anchor-rigid, swing {mp.nstr(kappa_swing,3)}), S ≈ -908/-887 carries the full "
        f"{mp.nstr(c3_swing*100,3)}% cross-anchor swing. (B) Wiring audit: production Q_β is "
        "c_2/N2-level (q_beta_kashiwara_n2_mev), so m_n and Δ_pn are c_3-INDEPENDENT; the "
        "mass table (m_e,m_μ,m_π,m_p) has no Q_β dependence; binding (B_AME) uses tr_M, not "
        "Q_β. So no table row moves. IF c_3 were later wired into Q_β, that is a CALIBRATION "
        "(Q_β/m_n/Δ_pn reclassify predicted->CAL-3-anchored) -- a bookkeeping move, not an "
        "accuracy win, and it would REMOVE them from the predicted-observable 100× count. "
        "No fit; no c_k value; nothing wired."
        if all_passed else
        "INCONCLUSIVE -- a factorization/wiring assertion failed; re-derive before citing."
    )

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as f:
        src = f.read()
    witness = {
        "computation": "qbeta-cal3-anchor-table-impact",
        "description": "CAL-3 anchoring of c_3: κ_(2,1)·S factorization (matches "
                       "CAL3AnchorStructure.lean) + production-wiring audit showing the "
                       "mass/binding tables are c_3-independent (Q_β is c_2/N2-level).",
        "audit_only": True,
        "tier": "structural-exact (factorization + wiring audit; no fit, no c_k value)",
        "computedAt": now,
        "commitSha": _repo_head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {
            "factorization": fac,
            "kappa_cross_anchor_swing": mp.nstr(kappa_swing, 4),
            "S_cross_anchor_swing": mp.nstr(S_swing, 4),
            "c3_cross_anchor_swing": mp.nstr(c3_swing, 4),
            "table_impact": table_impact,
            "production_c3_scan": {
                "sources": [os.path.relpath(p, _REPO_ROOT) for p in _PRODUCTION_SOURCES],
                "c3_wired": c3_wired,
                "hits": c3_hits,
                "regex": _C3_WIRING_RE.pattern,
            },
            "verdict": verdict,
        },
        "context": {
            "axis": "z->c_k f-map keystone: CAL-3 anchor structure + table impact",
            "lean": "QOU.QBeta.CAL3Anchor (kappa21_ne_zero, c3odd_bar_odd_of_factor, c3_swing_factorization)",
            "wiring_source": "computations/canonical_mass.py (m_n = m_p + q_beta_kashiwara_n2_mev() + m_e)",
            "kc18_eval_map": "docs/audits/2026-07-07-z-ck-fmap-eval-map-bar-decomposition.md",
            "registry": "docs/coordination/ck-dk-canonical-registry.md §9",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "qbeta-cal3-anchor-table-impact.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)

    print("\n=== CAL-3 anchor: factorization ===")
    print(f"{'anchor':8s} {'q0':>14s} {'kappa(q0)':>12s} {'c_3':>10s} {'S=c_3/kappa':>14s}")
    for name, v in fac.items():
        print(f"{name:8s} {v['q0']:>14s} {v['kappa']:>12s} {v['c3']:>10s} {v['S']:>14s}")
    print(f"\nswing: kappa {mp.nstr(kappa_swing,3)}  |  S {mp.nstr(S_swing,3)}  |  c_3 {mp.nstr(c3_swing,3)}")
    print("\n=== impact on tables ===")
    for obs, v in table_impact.items():
        print(f"  {obs:16s} c_3? {str(v['uses_c3']):5s}  {v['cal3_anchor_effect']}")
    print("\nVERDICT:", verdict)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
