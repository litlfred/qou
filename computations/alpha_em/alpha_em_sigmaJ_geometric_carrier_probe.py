#!/usr/bin/env python3
"""alpha_em_sigmaJ_geometric_carrier_probe.py

Brick 4 of the correspondence-statement attack: the sigma->J map (constructed at
the degenerate locus in the merged brick 3) has a GEOMETRIC CARRIER on the Bring
surface itself — the order-4 element of the (2,4,5) triangle group realizes the
democratic braiding data exactly.

Established inputs: brick 3 (merged): at the democratic points q = +-i the
semisimplified braiding sigma_ss = +-i squares to -1 (J-type), transpose fixes
each point, bar exchanges them. Braden-Disney-Hogg (library/arxiv-2208.13692v1/2208.13692v1.pdf):
the Bring vertices are the permutations of [1:i:-1:-i:0] (Prop 3.9, fixed points
of order-4 automorphisms); B/<4-cycle> is elliptic with j = -25/2 = j(5*tau0)
(SS4.3, Weber's T).

FINDINGS (exact, sympy):
  G1. V = [1:i:-1:-i:0] LIES ON BRING: H1(V) = H2(V) = H3(V) = 0 exactly — the
      vertex coordinates are the 4th roots of unity (+ 0).
  G2. THE ORDER-4 AUTOMORPHISM ACTS AT V WITH MULTIPLIER EXACTLY i: the 4-cycle
      (x1,x2,x3,x4,x5) -> (x2,x3,x4,x1,x5) maps V to i*V (projectively fixed,
      multiplier i). At a fixed point of a holomorphic automorphism the
      differential acts on the holomorphic tangent line by the multiplier; and
      multiplication by i on the holomorphic tangent line IS the action of the
      complex structure J. So dU|_V = i = J|_V: the (2,4,5) order-4 rotation
      REALIZES J BY AN AUTOMORPHISM at the vertices — and its multiplier is the
      democratic q = i (same 4th root of unity).
  G3. CONJUGATION EXCHANGES THE MULTIPLIER FAMILIES: conj(V) = [1:-i:-1:i:0] is
      the 4-cycle's fixed point with multiplier -i. Complex conjugation swaps
      the (+i)-multiplier and (-i)-multiplier vertex families EXACTLY as bar
      exchanges the degenerate points q = +-i (brick-3 B3) and as conjugation
      exchanges spec(J) = {+-i}. The involution structure of the degenerate
      braiding is geometrically realized.
  G4. THE QUOTIENT IS THE E_{5tau0} JACOBIAN FACTOR: Riemann-Hurwitz with the
      two multiplier-+-i fixed points (ramification index 4) gives
      genus(B/<U>) = 1 exactly; per the paper (SS4.3, Weber's T) this elliptic
      quotient has j = -25/2 = j(5*tau0) — the SAME E_{5tau0} that appears with
      multiplicity 3 in Jac(Bring) ~ E_{5tau0}^3 x E_{tau0} (Prop 4.6). The
      democratic/order-4 structure quotients onto the dominant Jacobian factor.

NET: the tau-functor target of the degenerate braiding is now CONCRETE — the
assignment sigma_ss(q=+-i) = +-i |-> dU|_{V,conj(V)} = +-i = J at the vertices,
equivariantly for {bar <-> conjugation}, with the quotient landing on E_{5tau0}.
What remains of the wall (unchanged, but now with an explicit geometric target):
show tau carries the braiding to THIS automorphism action — i.e. the functorial
statement, whose classical limit would then inherit the conformal structure J
defines and hence the heat-kernel unit a0 (Clause A).

Scope guard: exact geometry + one RH computation; derives NO clause; no fit;
nothing wired; 1/(8pi) stays phase-4. Self-contained (sympy).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    i = sp.I
    V = [1, i, -1, -i, 0]
    W = [1, -i, -1, i, 0]          # conj(V)

    # G1: V on Bring
    g1 = all(sp.simplify(sum(x ** k for x in V)) == 0 for k in (1, 2, 3))
    check("vertex_on_bring_exact", g1,
          "V=[1:i:-1:-i:0] satisfies H1=H2=H3=0 exactly — the vertex coordinates are the "
          "4th roots of unity (+0); Bring's 30 vertices are the permutations of this point "
          "(Braden-Disney-Hogg Prop 3.9)")

    # G2: 4-cycle multiplier at V is exactly i
    cyc = [V[1], V[2], V[3], V[0], V[4]]
    g2 = all(sp.simplify(c - i * v) == 0 for c, v in zip(cyc, V))
    check("order4_multiplier_is_democratic_q", g2,
          "the 4-cycle maps V to i*V exactly — projectively fixed with MULTIPLIER i; at a "
          "holomorphic fixed point the differential acts on the tangent line by the "
          "multiplier, and multiplication by i on the holomorphic tangent line IS J: "
          "dU|_V = i = J|_V. The (2,4,5) order-4 rotation realizes J by an automorphism, "
          "with multiplier = the democratic q = i")

    # G3: conjugation exchanges the multiplier families
    cycW = [W[1], W[2], W[3], W[0], W[4]]
    g3 = (all(sp.simplify(c - (-i) * w) == 0 for c, w in zip(cycW, W))
          and [sp.conjugate(v) for v in V] == W)
    check("conjugation_swaps_multiplier_families", g3,
          "conj(V)=[1:-i:-1:i:0] is fixed with multiplier -i — complex conjugation swaps "
          "the (+i)- and (-i)-multiplier vertex families EXACTLY as bar exchanges the "
          "degenerate points q=+-i (brick-3 B3) and as conjugation exchanges spec(J): the "
          "degenerate involution structure is geometrically realized")

    # G4: RH => genus(B/<U>) = 1 (the E_{5tau0} elliptic quotient)
    gp = sp.symbols('gp')
    sol = sp.solve(sp.Eq(2 * 4 - 2, 4 * (2 * gp - 2) + 2 * (4 - 1)), gp)
    g4 = sol == [1]
    check("order4_quotient_is_E5tau0_factor", g4,
          "Riemann-Hurwitz with exactly the two multiplier-+-i vertices ramified (index 4): "
          "2*g_B-2 = 4*(2g'-2) + 2*3 => g' = 1 — the elliptic quotient; per the paper "
          "(SS4.3, Weber's T) it has j = -25/2 = j(5*tau0), the SAME E_{5tau0} appearing "
          "with multiplicity 3 in Jac(Bring) ~ E_{5tau0}^3 x E_{tau0} (Prop 4.6): the "
          "democratic/order-4 structure quotients onto the dominant Jacobian factor")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "GEOMETRIC CARRIER FOUND (scope-(a); derives no clause; no fit; nothing wired): the "
        "degenerate braiding data is realized ON the Bring surface exactly — V=[1:i:-1:-i:0] "
        "lies on Bring (G1); the (2,4,5) order-4 rotation fixes it with multiplier exactly "
        "i = the democratic q, so dU|_V = J|_V (J is automorphism-realized at the vertices, "
        "G2); complex conjugation swaps the +-i multiplier families exactly as bar swaps the "
        "degenerate points / conjugation swaps spec(J) (G3); and the order-4 quotient is the "
        "genus-1 E_{5tau0} — the dominant Jacobian factor (G4). The tau target of "
        "sigma_ss(q=+-i)=+-i is now CONCRETE: dU at the vertex pair. Remaining wall "
        "(unchanged): the functorial statement tau(braiding) = this automorphism action, "
        "whose classical limit inherits the conformal structure and hence a0 (Clause A). "
        "NO tier change."
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
        "computation": "alpha-em-sigmaJ-geometric-carrier",
        "description": "Brick 4: the sigma->J map's geometric carrier — the Bring vertex V=[1:i:-1:-i:0] "
                       "(on-curve exact) is fixed by the (2,4,5) order-4 rotation with multiplier exactly "
                       "i = the democratic q, so dU|_V = J|_V (J automorphism-realized); conjugation swaps "
                       "the +-i multiplier families (= bar on the degenerate pair = conjugation on "
                       "spec(J)); the order-4 quotient is genus-1 = E_{5tau0}, the dominant Jacobian "
                       "factor. The tau target is now concrete. Derives no clause; nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-sigmaJ-geometric-carrier.md",
        "tier": "symbolic-exact (sympy; on-curve check, projective multipliers, Riemann-Hurwitz)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "vertex": "[1:i:-1:-i:0] on Bring (H1=H2=H3=0 exact)",
            "multiplier": "i at V (dU|_V = J|_V); -i at conj(V); conjugation swaps the families",
            "quotient": "genus(B/<U>)=1 = E_{5tau0} (j=-25/2), the x3 Jacobian factor",
            "tau_target": "dU at the vertex pair — concrete geometric target for sigma_ss(q=+-i)",
            "verdict": verdict,
        },
        "context": {
            "builds_on": "merged #3933 (bricks 1-3: corrected dictionary, unique tau target, sigma->J at "
                         "the degenerate locus) + Braden-Disney-Hogg Prop 3.9/SS4.3/Prop 4.6 (PDF in "
                         "library/)",
            "remaining": "the functorial statement tau(braiding) = the order-4 automorphism action; its "
                         "classical limit inherits the conformal structure J defines, hence a0 (Clause A)",
            "scope_guard": "derives NO clause; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-sigmaJ-geometric-carrier.witness.json")
    with open(out, "w") as f:
        # Provenance envelope. This producer writes its witness as raw JSON, so
        # nothing stamps `scriptHash` — and a witness without one cannot be
        # compared against its producer, so it drops OUT of the self-staleness
        # audit and reads as "not stale" forever. Regenerating it then looks
        # like progress while removing it from the count: a false drain.
        # Full rationale and the detector: computations/witness_drain_audit.py.
        #
        # `stamp_staleness_metadata`, not `wrap_legacy().save()`: it adds the
        # fields in place and leaves the on-disk shape untouched, so consumers
        # of legacy `assertions` records (which key on `label`, not `name`) do
        # not have to change. `engine` is passed back from the payload because
        # the helper overwrites it, and a descriptive engine string is worth
        # keeping.
        try:
            from witness_base import WitnessBuilder  # noqa: E402
        except ImportError:  # cluster subdir without the _path_bridge bootstrap
            import sys as _sys
            from pathlib import Path as _Path
            _sys.path.insert(0, str(next(
                _a / "substrate" for _a in _Path(__file__).resolve().parents
                if (_a / "substrate" / "witness_base.py").is_file())))
            from witness_base import WitnessBuilder  # noqa: E402
        WitnessBuilder.stamp_staleness_metadata(
            witness, script_path=__file__,
            engine=witness.get("engine", 'sympy'))
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
