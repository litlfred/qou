#!/usr/bin/env python3
"""alpha_em_f_t1_cover_structure_probe.py

F-construction T1 (bean qou-bi1u, milestone qou-a46k): the COVER STRUCTURE
underlying the archimedean tau-functor — Bring -> Bring/<U> as a degree-4
cyclic cover, with the Chevalley-Weil eigenspace dimensions DERIVING the
(3,1) isotypic split that consistency-1 (#4019) could only match.

LITERATURE GROUNDING (answering the owner's standing "from the lit?" test):
this construction route is a known mathematical species — braid-group /
Hecke representations at roots of unity realized on the cohomology of
CYCLIC COVERS, with the Hodge-theoretic (anti-)unitary structure attached
to the deck character: Deligne-Mostow (Publ. IHES 63, 1986); McMullen,
"Braid groups and Hodge theory" (Math. Ann. 355, 2013); eigenspace
dimensions by Chevalley-Weil (1934). What is NOT from the lit — and stays
honestly open — is that the FRAMEWORK's tau restricts to this functor on
the relevant data (T5's residual identification).

GEOMETRIC INPUT (merged): the #3942 carrier — U is an order-4 automorphism
of Bring's curve fixing the vertex V with derivative dU|_V = i (multiplier
exactly i, Lean-locked), conj(V) = W the conjugate fixed vertex with
multiplier -i; the quotient Bring/<U> has genus 1 (= E_{5 tau0}, the x3
Jacobian factor). Hence pi: Bring -> E := Bring/<U> is a DEGREE-4 CYCLIC
cover, and H^1(Bring) carries the deck action U* with eigenvalues i^k.

VERIFICATION (V1-V4, exact integer/rational arithmetic):
  V1. RIEMANN-HURWITZ CLOSURE + SELECTION: 2g_B - 2 = 4(2g_E - 2) + sum
      (e_p - 1) with g_B = 4, g_E = 1 forces sum(e_p - 1) = 6. For a Z_4
      cover the solutions are (n2, n4) in {(6,0), (3,1), (0,2)} (e=2
      contributes 1, e=4 contributes 3). The carrier data — TWO genuine
      fixed points V, W with derivative multipliers i, -i (fixed point <=>
      total ramification e=4) — selects (n2, n4) = (0, 2) EXACTLY: the
      cover is branched at precisely the two carrier vertices, totally.
  V2. MONODROMY SUM RULE forces the local data: the two local monodromies
      (a_V, a_W) in (Z/4)^x with a_V + a_W = 0 mod 4 and both of order 4
      (total ramification) force {a_V, a_W} = {1, 3} — i.e. deck
      derivative i at V and i^3 = -i at W: EXACTLY the #3942 multiplier
      pair (i, -i), now derived from the cover axioms rather than read off.
  V3. CHEVALLEY-WEIL DERIVES THE ISOTYPIC DIMS: for k = 1, 2, 3 the
      chi^k-eigenspace of H^{1,0} has dim = g_E - 1 + <k a_V/4> + <k a_W/4>
      = 0 + 1 = 1 (each k), and the invariant part has dim g_E = 1. So
      H^{1,0} = (1+1+1) moving (+) 1 invariant: the (3,1) split is DERIVED
      with ZERO adjustable input (branch data forced by V1+V2). This
      upgrades consistency-1 from a low-entropy match to a structural
      derivation: (3,1) = (moving, invariant) under the order-4 deck
      action; moving <-> E_{5 tau0}^3, invariant <-> E_{tau0} (pullback of
      H^1(E)) — the spec(M) = {5,5,5,1} multiplicities.
  V4. THE chi = i EIGENLINE IS 1-DIMENSIONAL: dim H^{1,0}_{chi} = 1 for the
      faithful character — the vertex-local line of the B2 shadow. T2's
      Hecke module at q = i acts on this line + its conjugate: the shadow's
      forced 2-point structure (#3960) acquires its geometric home.

HONEST SCOPE: T1 establishes the COVER SIDE of the functor. It does not
construct F (T2-T5), does not derive the Markov weights from CW dims (T4 —
the (3,1) dim match is now derived, but the WEIGHT values (3/4,1/4) at q=1
still need the trace-transport leg), and does not identify F with the
framework's tau (T5). No fit; nothing wired; 1/(8 pi) stays phase-4.
Self-contained (sympy exact).
"""
import datetime
import hashlib
import json
import os
import subprocess
import sys

import sympy as sp


def frac(x):
    return x - sp.floor(x)


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    gB, gE, N = 4, 1, 4

    # V1: RH closure + selection of (n2, n4) = (0, 2)
    lhs = 2 * gB - 2                       # 6
    base = N * (2 * gE - 2)                # 0
    need = lhs - base                      # 6
    sols = [(n2, n4) for n2 in range(0, 7) for n4 in range(0, 3)
            if n2 * 1 + n4 * 3 == need]
    v1 = need == 6 and sorted(sols) == [(0, 2), (3, 1), (6, 0)]
    check("riemann_hurwitz_closure_and_selection", v1,
          f"2g_B−2 = {lhs} = 4·(2g_E−2) + Σ(e_p−1) ⟹ Σ(e_p−1) = {need}; ℤ₄ solutions "
          f"(n₂,n₄) ∈ {sorted(sols)}; the #3942 carrier (TWO fixed points V,W with "
          "derivative multipliers i,−i ⟺ total ramification e=4) SELECTS (0,2): branched "
          "at exactly the two carrier vertices, totally")

    # V2: monodromy sum rule forces {a_V, a_W} = {1, 3} — the (i, -i) pair
    pairs = [(a, b) for a in range(1, 4) for b in range(1, 4)
             if (a + b) % 4 == 0 and sp.gcd(a, 4) == 1 and sp.gcd(b, 4) == 1]
    v2 = sorted(set(tuple(sorted(p)) for p in pairs)) == [(1, 3)]
    check("monodromy_sum_rule_forces_multipliers", v2,
          "a_V + a_W ≡ 0 (mod 4) with both of order 4 forces {a_V,a_W} = {1,3} — deck "
          "derivatives (i, i³=−i): the #3942 multiplier pair (i,−i) DERIVED from the cover "
          "axioms (branch-cycle sum rule), not read off")

    # V3: Chevalley-Weil derives the (3,1) split with zero adjustable input
    aV, aW = 1, 3
    dims = {}
    for k in range(1, N):
        dims[k] = gE - 1 + frac(sp.Rational(k * aV, N)) + frac(sp.Rational(k * aW, N))
    moving = sum(dims.values())
    invariant = gE
    total = moving + invariant
    v3 = (all(d == 1 for d in dims.values()) and moving == 3 and invariant == 1
          and total == gB)
    check("chevalley_weil_derives_31", v3,
          f"dim H^{{1,0}}_{{χ^k}} = g_E−1+⟨k·a_V/4⟩+⟨k·a_W/4⟩ = {dict(dims)} (k=1,2,3), "
          f"invariant part = g_E = {invariant}; total {total} = g_B ✓. The (3,1) isotypic "
          "split is DERIVED (moving ↔ E_{5τ₀}³, invariant ↔ E_{τ₀} = pullback H¹(E); the "
          "spec(M)={5,5,5,1} multiplicities) with ZERO adjustable input — consistency-1 "
          "upgraded from low-entropy match to structural derivation")

    # V4: the chi = i eigenline is 1-dim — the vertex-local shadow home
    v4 = dims[1] == 1 and dims[3] == 1
    check("chi_i_eigenline_one_dimensional", v4,
          "dim H^{1,0}_χ = 1 for the faithful character (and 1 for its inverse) — the "
          "vertex-local line of the B2 shadow: T2's Hecke module at q = i acts on this "
          "line and its conjugate; the FORCED 2-point shadow (#3960) acquires its "
          "geometric home")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "F-CONSTRUCTION T1 DELIVERED (scope-(a); no fit; nothing wired): the cover side of "
        "the archimedean τ-functor is established — Bring → Bring/⟨U⟩ ≅ E is a degree-4 "
        "cyclic cover branched TOTALLY at exactly the two #3942 carrier vertices (RH "
        "closure selects it; the branch-cycle sum rule DERIVES the multiplier pair (i,−i)); "
        "Chevalley–Weil then DERIVES the (3,1) isotypic split with zero adjustable input "
        "(moving {k=1,2,3} ↔ E_{5τ₀}³, invariant ↔ E_{τ₀}) — consistency-1 upgraded to a "
        "structural derivation — and the χ=i eigenline is 1-dim, the geometric home of the "
        "forced B2 shadow. Route literature-grounded (Deligne–Mostow; McMullen 2013; "
        "Chevalley–Weil). OPEN (T2–T5): the Hecke module via braid monodromy at q=i, the "
        "ρ-equivariance theorem, the WEIGHT transport (dims derived; weight VALUES not "
        "yet), and the residual identification F = framework-τ. NO tier change."
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
        "computation": "alpha-em-f-t1-cover-structure",
        "description": "F-construction T1 (qou-bi1u): Bring -> Bring/<U> = E as a degree-4 cyclic "
                       "cover. RH closure selects total branching at exactly the two #3942 carrier "
                       "vertices; the branch-cycle sum rule derives the multiplier pair (i,-i); "
                       "Chevalley-Weil derives the (3,1) isotypic split with zero adjustable input "
                       "(consistency-1 upgraded to a structural derivation); the chi=i eigenline is "
                       "1-dim (geometric home of the forced B2 shadow). Lit-grounded route "
                       "(Deligne-Mostow; McMullen 2013; Chevalley-Weil). T2-T5 open. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-alpha-em-f-t1-cover-structure.md",
        "tier": "exact integer/rational arithmetic (RH + branch-cycle + Chevalley-Weil); "
                "structural derivation",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "cover": "Bring -> E = Bring/<U>, degree 4 cyclic, branched totally at V, W",
            "multipliers": "(i, -i) derived from the branch-cycle sum rule",
            "cw_dims": "H^{1,0}: chi^k dims (1,1,1) for k=1,2,3 + invariant 1 — the (3,1) "
                       "split DERIVED",
            "chi_i_line": "1-dimensional — the B2 shadow's geometric home",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-bi1u (T1) of milestone qou-a46k (F-construction)",
            "literature": "Deligne-Mostow 1986; McMullen, Braid groups and Hodge theory, 2013; "
                          "Chevalley-Weil 1934",
            "scope_guard": "cover side only; F not constructed; weight VALUES not derived (T4); "
                           "F = framework-tau not identified (T5); no fit; nothing wired; "
                           "1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-f-t1-cover-structure.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    with open(out, "w") as f:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        witness.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
