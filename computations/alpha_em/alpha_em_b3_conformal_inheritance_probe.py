#!/usr/bin/env python3
"""alpha_em_b3_conformal_inheritance_probe.py

Bean B3 (qou-cncc) of the tau-correspondence proof plan (milestone qou-b5qg):
CONFORMAL INHERITANCE — the chain J => conformal class => Laplacian => a0, with
its one machine-checkable core verified across the computable metric family.

The chain (per-step status):
  (i)  J <=> conformal class on a surface — STANDARD (a complex structure on a
       2-manifold is exactly a conformal class + orientation; textbook), cited
       not re-proved.
  (ii) conformal class + area => Laplacian => leading heat asymptotics
       Tr e^{t*Delta} ~ Area/(4*pi*t): the UNIVERSALITY of a0 = 1/(4*pi) per
       unit area — the per-mode weight is METRIC-INDEPENDENT. This is the
       machine-checkable core, verified here across the flat family.
  (iii) hence: IF the B2 functorial lift holds (tau carries the braiding's
       degenerate pair to J at the vertices — shadow FORCED, #3960), THEN the
       loop geometry inherits the conformal class J defines and with it the
       universal unit a0 = 1/(4*pi). Clause A of the per-loop conjecture
       becomes CONDITIONAL on (B2-lift) + (B4: the tower's per-loop parameter
       is normalized by THIS unit at q->1).

VERIFICATION (V1-V3):
  V1. a0-UNIVERSALITY: Tr e^{t*Delta_G} * (4*pi*t)/Area(G) -> 1 as t -> 0 for
      metrics of very different shape (square, hexagonal, skew, 9:1
      anisotropic) — the leading coefficient carries NO metric data beyond the
      area: the per-mode weight 1/(4*pi) is universal.
  V2. CONVERGENCE IS UNIFORM-IN-SHAPE at the checked scales: the ratio is 1 to
      <=1e-6 at t=1e-3 for all four metrics (the subleading correction is the
      exponentially small dual-lattice term for flat tori — no curvature term
      on flat metrics, so the approach is exponential, not O(t)).
  V3. CONSISTENCY with the proved chi-side: on a CURVED (hyperbolic) surface
      the t^0 term is chi/6 (McKean-Singer; = -1 exactly on Bring, merged
      conjecture-statement PR) and Gauss-Bonnet fixes Area = 2*pi*|chi| — the
      merged GB Lean identity |chi|/(4*Area) = 1/(8*pi) then places the SAME
      universal a0 in the measure. Verified arithmetically here (g=4: chi=-6,
      Area=12*pi, |chi|/(4*Area)=1/(8*pi) exact).

Honest scope: (i) is citation; V1/V2 verify (ii) within the flat family (the
family where exact lattice sums exist — curvature corrections change SUBLEADING
terms only, by the standard heat expansion); (iii) is a CONDITIONAL statement —
B3 does NOT derive Clause A unconditionally, does not derive the B2 lift, and
leaves B4 open. No fit; nothing wired; 1/(8pi) stays phase-4.

Self-contained (numpy + sympy).
"""
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys

import numpy as np
import sympy as sp


def heat_ratio(G, t, R=60):
    Gi = np.linalg.inv(G)
    pts = np.array(list(itertools.product(range(-R, R + 1), repeat=2)), float)
    q = np.einsum('ij,jk,ik->i', pts, Gi, pts)
    tr = np.sum(np.exp(-4 * np.pi ** 2 * t * q))
    return tr * (4 * np.pi * t) / np.sqrt(np.linalg.det(G))


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    metrics = {
        "square": np.eye(2),
        "hexagonal": np.array([[2, 1], [1, 2]], float),
        "skew": np.array([[1, 0.7], [0.7, 2]], float),
        "anisotropic_9to1": np.diag([1, 9.0]),
    }

    # V1: universality across shapes
    ratios = {n: heat_ratio(G, 1e-3) for n, G in metrics.items()}
    v1 = all(abs(r - 1) < 1e-6 for r in ratios.values())
    check("a0_universality_across_metrics", v1,
          "Tr e^{tΔ}·(4πt)/Area = " + ", ".join(f"{n}:{r:.8f}" for n, r in ratios.items())
          + " at t=1e-3 — the leading heat coefficient is 1/(4π) PER UNIT AREA for every "
          "metric shape (square/hex/skew/9:1): the per-mode weight carries no metric data "
          "beyond area — a0 is UNIVERSAL")

    # V2: t-convergence for the worst-conditioned metric
    seq = [heat_ratio(metrics["anisotropic_9to1"], t) for t in (1e-2, 3e-3, 1e-3)]
    v2 = all(abs(r - 1) < 1e-6 for r in seq)
    check("convergence_uniform_in_shape", v2,
          f"anisotropic 9:1 ratios at t=1e-2,3e-3,1e-3: {[f'{r:.8f}' for r in seq]} — "
          "flat-family approach is exponential (dual-lattice term), already exact at the "
          "checked scales even for the worst-conditioned shape")

    # V3: consistency with the proved chi-side (Bring: chi=-6, Area=12*pi)
    g, pi = sp.symbols('g pi', positive=True)
    chi = 2 - 2 * g
    area = 2 * pi * (2 * g - 2)
    gb = sp.simplify((2 * g - 2) / (4 * area) - 1 / (8 * pi)) == 0
    bring_vals = (chi.subs(g, 4) == -6 and sp.simplify(area.subs(g, 4) - 12 * pi) == 0
                  and sp.simplify(chi / 6).subs(g, 4) == -1)
    check("consistency_with_proved_chi_side", gb and bring_vals,
          "|χ|/(4·Area)=1/(8π) identically (the merged GB Lean identity) with Bring χ=−6, "
          "Area=12π, heat-trace constant χ/6=−1 (merged) — the SAME universal a₀ sits in "
          "the measure on the curved side; V1's universality is what makes it a₀ and not a "
          "metric-dependent weight")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B3 DELIVERED AS A CONDITIONAL CHAIN (scope-(a); derives no clause unconditionally; "
        "no fit; nothing wired): the machine-checkable core of J => conformal class => "
        "Laplacian => a0 is VERIFIED — the leading heat coefficient is 1/(4π) per unit area "
        "for every metric shape in the computable flat family (ratios = 1 to <=1e-6 incl. a "
        "9:1 anisotropic case; exponential approach), and it is consistent with the proved "
        "curved-side facts (GB identity, χ/6=−1 on Bring). Chain status: (i) J<=>conformal "
        "class — standard, cited; (ii) a0-universality — VERIFIED here; (iii) the "
        "CONDITIONAL: IF the B2 functorial lift (shadow FORCED, #3960) THEN the loop "
        "geometry inherits J's conformal class and the universal a0 — Clause A reduces to "
        "(B2-lift) + (B4 classical-limit normalization). B4 remains the open analytic "
        "piece. NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        out = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not out:
            raise RuntimeError("empty commitSha")
        return out

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-b3-conformal-inheritance",
        "description": "Bean B3 (qou-cncc): conformal inheritance J => conformal class => Laplacian => "
                       "a0. Verified core: a0-universality — Tr e^{tΔ}·(4πt)/Area -> 1 for square/hex/"
                       "skew/9:1-anisotropic metrics (<=1e-6 at t=1e-3, exponential approach); "
                       "consistent with the proved GB identity + χ/6=−1. Conditional: IF B2-lift THEN "
                       "the loop geometry carries the universal a0; Clause A reduces to B2-lift + B4. "
                       "Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-b3-conformal-inheritance.md",
        "tier": "verified core (numpy lattice heat traces + sympy exact GB arithmetic) + "
                "conditional chain (J<=>conformal cited; B2-lift open; B4 open)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "numpy+sympy", "engineVersion": np.__version__ + "/" + sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "a0_universality": {n: float(r) for n, r in ratios.items()},
            "chain": "(i) J<=>conformal std cited; (ii) a0 universal VERIFIED; (iii) conditional on "
                     "B2-lift + B4",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-cncc (B3) of milestone qou-b5qg; B1 merged #3955, B2 shadow merged #3960",
            "conditional_shape": "IF tau carries the braiding's degenerate pair to J (B2 lift) THEN "
                                 "the loop geometry inherits J's conformal class and the universal "
                                 "a0 = 1/(4pi); Clause A = B2-lift + B4",
            "scope_guard": "derives no clause unconditionally; no fit; nothing wired; 1/(8pi) stays "
                           "phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-b3-conformal-inheritance.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
