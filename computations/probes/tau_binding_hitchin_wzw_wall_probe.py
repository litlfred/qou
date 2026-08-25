#!/usr/bin/env python3
"""tau_binding_hitchin_wzw_wall_probe.py — the Hitchin/WZW monodromy trace
(Laszlo–Pauly–Sorger) is the RIGHT TYPE for τ = tr B but hits the known
archimedean-continuation wall: root-of-unity WZW monodromy is unitary (elliptic,
|tr|≤2), while τ_binding = 2.6424 > 2 is hyperbolic.

CONTEXT (bean qou-oduj / qou-1gdc; ATTACK 2 of the fresh-look qou-do3a). The
binding kernel R(q,x)=x²−τx+1 is derived; τ has a Lean-proved closed form
(BindingTauAnchorClosure.lean: τ = 3(3q⁴+8q²+3)/(4q(q+1)²) = 3(3[2]²+2)/(4([2]+2)),
bar-even in [2]_q; τ(q₀)=2.6424, proved >2 ⇒ B hyperbolic). Its GEOMETRIC
derivation is the owner-gated s5-so3 keystone (the archimedean continuation of the
RT/WRT amplitude from a fibre root-of-unity to real q₀>1). The uploaded
Laszlo–Pauly–Sorger "On the monodromy of the Hitchin connection" computes the
SL(2) WZW/Hitchin monodromy = the framework's Hecke braiding — a candidate handle.

FINDINGS (this probe):
 (1) LPS Prop 5.1: tr ρ(σ₁⁻¹σ₂) = 2 − q − q⁻¹ + q² + q⁻² = [2]_q² − [2]_q (det 1,
     bar-even) — exactly the right OBJECT TYPE (SL₂ det-1 bar-even WZW/Hecke
     monodromy trace, same (q+1)²-shape as τ_binding's denominator). But at real
     q₀ this specific element = 2.033 ≠ τ_binding 2.6424 (scope-(a): distinct
     [2]_q-rationals).
 (2) LPS q = exp(2πi/(l+2)) is a ROOT OF UNITY; the WZW/WRT monodromy is UNITARY
     (positive-definite Gilmer–Masbaum form) ⇒ a det-1 unitary element has
     eigenvalues on the unit circle ⇒ trace ∈ [−2,2] (ELLIPTIC) at EVERY level,
     including the keystone level l=8 (A₅ image, trace ≈ 1.0). It never reaches
     and structurally cannot reach the hyperbolic τ=2.6424>2. scope-(b) exclusion,
     cited invariant: WRT unitarity.
 (3) STRUCTURAL CONFIRMATION (not new, but clarifying): LPS Prop 5.3 gives
     l=8 → A₅ (icosahedral) as the finite WZW monodromy image — the keystone's
     A₅ ⊂ SO(3). So the keystone symmetry IS the level-8 WZW monodromy; binding τ
     is its HYPERBOLIC archimedean continuation to real q₀. Same WZW/Hecke
     braiding, two evaluations (fibre root-of-unity unitary vs observable real-q
     hyperbolic — the AGENTS.md Im(q) wall).

VERDICT: classification (ii) structural analogy needing a bridge — the Hitchin
paper confirms the correct object class and the A₅=level-8 symmetry origin, but
does NOT supply a new route to 2.6424: its root-of-unity monodromy is elliptic by
unitarity, and the only route to the hyperbolic value is the standing owner-gated
keystone archimedean continuation. NOT a derivation; not passed off as a closure.
scope-(a) for the element mismatch; scope-(b) for the unitarity exclusion (cited
invariant: WRT/Gilmer–Masbaum unitarity). No fit; no c_k wired.

Run: python3 -u computations/probes/tau_binding_hitchin_wzw_wall_probe.py
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


Q0 = mp.mpf("1.10997859555733471")


def tau_binding(q):
    return 3 * (3 * q ** 4 + 8 * q ** 2 + 3) / (4 * q * (q + 1) ** 2)


def tau_hitchin_real(q):
    # LPS Prop 5.1: tr rho(sigma1^-1 sigma2), det 1
    return 2 - q - 1 / q + q ** 2 + 1 / q ** 2


def main() -> int:
    assertions = []

    def check(name, passed, **kw):
        e = {"name": name, "passed": bool(passed)}
        e.update({k: v for k, v in kw.items() if v is not None})
        assertions.append(e)
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}", flush=True)

    print("=" * 76)
    print(" τ = tr B vs the Hitchin/WZW monodromy trace (Laszlo–Pauly–Sorger)")
    print("=" * 76)

    tb = tau_binding(Q0)
    th = tau_hitchin_real(Q0)
    b = Q0 + 1 / Q0
    print(f"  τ_binding(q0)            = {mp.nstr(tb, 10)}  (Lean closed form)")
    print(f"  LPS σ₁⁻¹σ₂ at real q0    = {mp.nstr(th, 10)}  = [2]²−[2]")
    print(f"  [2]_q0                   = {mp.nstr(b, 10)}")

    # (1) the specific LPS element ≠ τ_binding (scope-(a))
    check("lps_element_neq_tau_binding", abs(th - tb) > mp.mpf("0.5"),
          source=f"LPS σ₁⁻¹σ₂ real-q0 trace = [2]²−[2] = {mp.nstr(th,6)} ≠ "
                 f"τ_binding = {mp.nstr(tb,6)} — the right object TYPE (SL₂ det-1 "
                 "bar-even WZW/Hecke trace) but a distinct [2]_q-rational function. "
                 "scope-(a).")
    # τ_binding matches its [2]_q form (self-consistency)
    check("tau_binding_bareven_form_consistent",
          abs(tb - 3 * (3 * b * b + 2) / (4 * (b + 2))) < mp.mpf("1e-30"),
          source="τ_binding = 3(3[2]²+2)/(4([2]+2)) reproduces the closed form — "
                 "bar-even in [2]_q (Lean BindingTauAnchorClosure)")

    # (2) WZW root-of-unity monodromy is ELLIPTIC at every level (scope-(b))
    print("\n  LPS at root-of-unity levels q=exp(2πi/(l+2)) (unitary ⇒ elliptic):")
    all_elliptic = True
    l8_trace = None
    for l in (3, 5, 6, 7, 8, 10, 20, 100):
        ang = 2 * mp.pi / (l + 2)
        tr = 2 - 2 * mp.cos(ang) + 2 * mp.cos(2 * ang)
        if abs(tr) > 2 + mp.mpf("1e-30"):
            all_elliptic = False
        if l == 8:
            l8_trace = tr
        tag = "A₅ keystone" if l == 8 else ""
        print(f"    l={l:3d}: tr={mp.nstr(tr,8):>11}  |tr|≤2? {abs(tr) <= 2}  {tag}")
    check("wzw_root_of_unity_always_elliptic", all_elliptic,
          source="at every level l the WZW/WRT monodromy trace ∈ [−2,2] (elliptic) "
                 "— it is UNITARY (positive-definite Gilmer–Masbaum form; det-1 "
                 "unitary ⇒ eigenvalues on the unit circle ⇒ tr=2Re(λ)∈[−2,2]). "
                 "including l=8 (A₅ keystone, tr≈1.0). It CANNOT carry the "
                 "hyperbolic τ_binding=2.6424>2. scope-(b) exclusion, cited "
                 "invariant WRT unitarity — the fibre(root-of-unity)/observable"
                 "(real-q) archimedean-continuation wall.")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "CLASSIFICATION (ii) structural analogy needing a bridge — NOT a derivation. "
        "The Hitchin/WZW monodromy (Laszlo–Pauly–Sorger) supplies exactly the right "
        "OBJECT TYPE for τ=tr B (SL₂ det-1 bar-even WZW/Hecke trace, Prop 5.1 = "
        "[2]²−[2]) and confirms the keystone's A₅ as the finite level-8 SU(2) "
        "monodromy image (Prop 5.3). But it does NOT bridge to τ_binding=2.6424: "
        "(a) the specific element σ₁⁻¹σ₂ at real q0 = 2.033 ≠ 2.6424 (distinct "
        f"[2]_q-rationals); (b) at every root of unity the monodromy is UNITARY ⇒ "
        f"elliptic |tr|≤2 (l=8 A₅ gives {mp.nstr(l8_trace,4) if l8_trace else 'n/a'}), "
        "so no literal WZW element carries the hyperbolic τ>2 (cited invariant: WRT "
        "unitarity). This is the SAME archimedean-continuation wall the corpus "
        "already names (fibre root-of-unity unitary vs observable real-q hyperbolic; "
        "keystone §Frontier bwS0_eq_hecke). The Hitchin paper makes the wall vivid "
        "(A₅ = level-8 finite monodromy; binding τ = its hyperbolic continuation) "
        "but leaves the owner-gated keystone continuation as the sole route. Not "
        "passed off as a closure. No fit; no c_k wired."
    )
    print("\nVERDICT:", verdict)

    with open(__file__, "rb") as fh:
        src = fh.read()
    witness = {
        "computation": "tau-binding-hitchin-wzw-wall",
        "description": "The Hitchin/WZW monodromy (Laszlo–Pauly–Sorger) is the right "
                       "object type for τ=tr B and confirms A₅=level-8, but its "
                       "root-of-unity monodromy is unitary/elliptic (|tr|≤2) while "
                       "τ=2.6424>2 is hyperbolic — the archimedean-continuation "
                       "wall. Structural analogy (ii), not a derivation. scope-(a)+"
                       "(b).",
        "audit_only": True,
        "tier": "structural assessment (scope-(a) mismatch + scope-(b) exclusion)",
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "commitSha": _head_sha(),
        "engine": "mpmath",
        "engineVersion": mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions,
        "allPassed": all_passed,
        "result": {"tau_binding_q0": mp.nstr(tb, 10),
                   "lps_sigma_real_q0": mp.nstr(th, 10),
                   "l8_A5_trace": mp.nstr(l8_trace, 8) if l8_trace else None,
                   "verdict": verdict},
        "context": {
            "axis": "τ=tr B geometric derivation — Hitchin route (ATTACK 2 of "
                    "qou-do3a; beans qou-oduj/qou-1gdc/z2bn)",
            "paper": "Laszlo–Pauly–Sorger, On the monodromy of the Hitchin "
                     "connection (library/monodromyhitchiny/MonodromyHitchinY.pdf)",
            "corpus": "BindingTauAnchorClosure.lean (τ closed form); s5-so3 keystone "
                      "(bwS0_eq_hecke, archimedean continuation, owner-gated)",
            "correction": "τ is NOT an open number — it has a Lean-proved closed "
                          "form; only its GEOMETRIC derivation is open",
        },
    }
    out = os.path.join(os.path.dirname(__file__),
                       "tau-binding-hitchin-wzw-wall.witness.json")
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
    print("\nwitness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
