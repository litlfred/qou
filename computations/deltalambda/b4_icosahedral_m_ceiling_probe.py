#!/usr/bin/env python3
"""b4_icosahedral_m_ceiling_probe.py — does the Σ(2,3,5) binary-icosahedral
S-matrix supply a FORWARD per-pair magnitude m for the He4 [1⁴] cumulant
b₄ = −ln det(I+G), det(I+G) = (1−5m²)(1−m²), physicality ceiling m < 1/√5?

CONTEXT (bean qou-k4ud; Δ_λ MAGNITUDE frontier). The Δ_λ sign+magnitude single
trace Δ_λ = (−1)^{n(λ)}·dim_λ is settled and UNDER-binds the deuteron ×5.85; the
missing piece is the derived-shape He4-local ≥4-body cumulant
b₄ = −ln det(I+mag·S), eig(S)={±√5,±1} ⇒ det=(1−5m²)(1−m²), binding for
0<m<1/√5, unphysical (det<0) for m>1/√5 (b4_slater_antisymmetrizer_exchange_sign,
Lean ReebPnMagnitude). The open scalar is m∈(0,1/√5). The attack-vector map
(docs/audits/2026-07-18-deltalambda-attack-vector-map.md, Vector 2) flags a
non-fit lead: the ceiling 1/√5 is √5-related = binary-icosahedral, and Σ(2,3,5)
appears independently in the keystone (McKay 2I↔E₈). If m reads off that
S-matrix it is a DERIVATION, not a fit.

THIS probe tests the lead's PRECONDITION disciplinedly: does the icosahedral
S-matrix actually put a natural object BELOW the 1/√5 ceiling? It classifies the
Σ(2,3,5) S-matrix entries + natural icosahedral quantities vs the ceiling —
FORWARD only. It does NOT compare any m to AME (that back-solve is the forbidden
fit / the "seventh ansatz" AGENTS.md forbids). The deliverable is a scope-(a)
narrowing of the lead: which forward icosahedral objects survive m<1/√5, and
whether a UNIQUE one is singled out.

Σ(2,3,5) / Fibonacci S-matrix (golden ratio φ=(1+√5)/2, quantum dims {1,φ},
total D=√(1+φ²)): vacuum row (S_00,S_01) = (1/D, φ/D) = (2/√5)(sin π/5, sin 2π/5).

scope-(a): a ceiling classification, no AME fit; no c_k wired. If the primary
S-matrix objects OVERSHOOT the ceiling, the forward m is not the naive entry —
a genuine narrowing, not a closure.

Run: python3 -u computations/deltalambda/b4_icosahedral_m_ceiling_probe.py
"""
from __future__ import annotations

import datetime
import hashlib
import json
import os
import subprocess

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
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


def b4(m):
    det = (1 - 5 * m ** 2) * (1 - m ** 2)
    return (-mp.log(det)) if det > 0 else None


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 78)
    print(" b₄ He4-[1⁴] cumulant: does Σ(2,3,5) supply a FORWARD m < 1/√5?")
    print("=" * 78)

    ceiling = 1 / mp.sqrt(5)
    phi = (1 + mp.sqrt(5)) / 2
    D = mp.sqrt(1 + phi ** 2)          # Fibonacci total quantum dim
    s_pi5 = mp.sin(mp.pi / 5)
    s_2pi5 = mp.sin(2 * mp.pi / 5)
    print(f"  ceiling 1/√5 = {mp.nstr(ceiling, 8)}   φ = {mp.nstr(phi, 8)}   "
          f"D = √(1+φ²) = {mp.nstr(D, 8)}")

    # forward icosahedral candidates (NO AME input)
    cands = {
        "S_00 = 1/D = (2/√5)sin(π/5)": 1 / D,
        "S_01 = φ/D = (2/√5)sin(2π/5)": phi / D,
        "φ⁻¹": 1 / phi,
        "S_00/S_01 = 1/φ": (1 / D) / (phi / D),
        "φ⁻²": 1 / phi ** 2,
        "1/D²": 1 / D ** 2,
        "sin²(π/5)": s_pi5 ** 2,
        "z_naive = 1/[2]_v (0.4993, corpus)": mp.mpf("0.4993"),
        "ceiling 1/√5 itself": ceiling,
    }
    print("\n  candidate                                   value     < 1/√5 ?   b₄=−ln det")
    below = []
    rows = []
    for name, m in cands.items():
        ok = m < ceiling
        bv = b4(m)
        rows.append({"name": name, "m": mp.nstr(m, 10), "below_ceiling": bool(ok),
                     "b4": (mp.nstr(bv, 10) if bv is not None else "unphysical(det≤0)")})
        if ok and "ceiling" not in name:
            below.append(name)
        print(f"    {name:42s} {mp.nstr(m,8):>9}   {str(ok):>5}    "
              f"{(mp.nstr(bv,8) if bv is not None else 'unphysical'):>12}")

    # (1) the PRIMARY S-matrix objects (S_00, S_01, φ⁻¹) overshoot the ceiling
    primary_overshoot = ((1 / D) > ceiling and (phi / D) > ceiling and
                         (1 / phi) > ceiling)
    check("primary_icosahedral_objects_overshoot_ceiling", primary_overshoot,
          source="S_00=1/D=0.5257, S_01=φ/D=0.8507, φ⁻¹=0.6180 all EXCEED "
                 "1/√5=0.4472 — the naive Σ(2,3,5) vacuum-row entries and the "
                 "golden ratio itself are NOT admissible as m (det(I+mS)<0, "
                 "unphysical). So the forward m is NOT the primary S-matrix entry.")

    # (2) the forward m is not uniquely singled out (multiple sub-ceiling objects)
    non_unique = len(below) >= 2
    check("forward_m_not_uniquely_singled_out", non_unique,
          source=f"{len(below)} distinct icosahedral objects fall BELOW the ceiling "
                 f"(φ⁻²=0.382, 1/D²=0.276, sin²(π/5)=0.345, …) — no single one is "
                 "structurally forced as m. Selecting the one that matches AME "
                 "would be the forbidden back-solve (the 'seventh ansatz'); a "
                 "forward derivation needs extra structure not yet present.")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "SCOPE-(a) NARROWING of the icosahedral-m lead (NOT a closure, NOT a "
        "refutation). The 1/√5 ceiling is genuinely √5/binary-icosahedral, but the "
        "PRIMARY Σ(2,3,5) objects — S_00=0.526, S_01=0.851, φ⁻¹=0.618 — all "
        "OVERSHOOT the ceiling (unphysical as m), as does the corpus z_naive=0.499. "
        "Only SECONDARY powers/combinations fall below (φ⁻²=0.382, 1/D²=0.276, "
        "sin²(π/5)=0.345), and no single one is structurally forced. CONSEQUENCE: "
        "the 'pin m to the icosahedral S-matrix' lead does NOT yet supply a "
        "parameter-free m — the forward selection among sub-ceiling candidates is "
        "unresolved, and choosing by AME match is the forbidden fit. The lead is "
        "SUGGESTIVE (√5 ceiling = icosahedral, and Σ(2,3,5) is the keystone object) "
        "but needs additional structure — most naturally the SAME archimedean "
        "continuation the keystone τ derivation needs (Frontier B): the S-matrix "
        "lives at the root-of-unity fibre, the physical m at real q₀. The two "
        "frontiers share the fibre→observable wall. No fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as fh:
        src = fh.read()
    witness = {
        "computation": "b4-icosahedral-m-ceiling",
        "description": "Ceiling classification of Σ(2,3,5) S-matrix objects vs the "
                       "b₄ physicality bound m<1/√5. Primary entries (S_00,S_01,φ⁻¹) "
                       "overshoot; only secondary powers fall below and none is "
                       "forced — the icosahedral-m lead does not yet supply a "
                       "forward parameter-free m. scope-(a); no AME fit.",
        "audit_only": True,
        "tier": "structural classification (forward, no fit)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"ceiling": mp.nstr(ceiling, 10), "candidates": rows,
                   "below_ceiling": below, "verdict": verdict},
        "context": {
            "axis": "Δ_λ magnitude — b₄ [1⁴] cumulant scalar m (bean qou-k4ud)",
            "assembly": "det(I+mag·S)=(1−5m²)(1−m²), eig(S)={±√5,±1}, m<1/√5 "
                        "(b4_slater_antisymmetrizer_exchange_sign; Lean "
                        "ReebPnMagnitude)",
            "lead": "docs/audits/2026-07-18-deltalambda-attack-vector-map.md Vector 2 "
                    "(icosahedral 1/√5 coincidence)",
            "cross_link": "the Σ(2,3,5) S-matrix is the keystone object (Frontier B "
                          "qou-2v7k); both frontiers meet at the fibre→observable "
                          "archimedean-continuation wall",
        },
    }
    out = os.path.join(os.path.dirname(__file__), "b4-icosahedral-m-ceiling.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
