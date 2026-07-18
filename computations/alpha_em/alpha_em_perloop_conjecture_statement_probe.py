#!/usr/bin/env python3
"""alpha_em_perloop_conjecture_statement_probe.py

States the alpha_EM per-loop-measure wall as a PRECISE two-clause conjecture (the
"well-stated conjecture" ask) and machine-checks its exact arithmetic skeleton +
two literature anchors. Post-Gauss-Bonnet form (follows main's ba606720e /
2b562bc7d, which adjudicated the measure to |chi|/(4*Area), genus-independent).

THE CONJECTURE (per-loop measure; scope: the single load-bearing 1/pi wall):

  In the alpha_EM loop tower  1/alpha = q[9]_q[10]_q + b1/Area + alpha[2]_q/(8pi) - ...,
  the per-loop measure equals

      (1/2) * a0,     a0 := 1/(4pi) = |chi| / (2*Area)      (Gauss-Bonnet form),

  where
    Clause A (loop universality):  the per-mode weight is the universal 2d
      heat-kernel unit a0 = leading Seeley-DeWitt coefficient (1/4pi per mode),
      geometrized by GB: Area = 2pi|chi| => a0 = |chi|/(2*Area). [R2's content]
    Clause B (channel multiplicity): the multiplicity is EXACTLY 2 = the two
      Hecke eigenvalue channels of sigma_i ((sigma-q)(sigma+q^{-1})=0: the
      e+/e- braiding idempotents), NOT b1 and NOT a quantum dimension. [#3810's
      channel split; the one factor no route has derived]

  Clauses A+B => measure = 1/(8pi) on EVERY closed hyperbolic surface
  (genus-independent). The b1 form 1/(pi*b1) is a g=4 coincidence (main, GB).

WHAT IS PROVED vs CONJECTURAL (the honest split):
  * proved (main, sorry-free Lean): the GB identity |chi|/(4*Area) = 1/(8pi) and
    genus-independence.  * proved here (exact): the arithmetic skeleton + the
    McKean-Singer anchor.  * CONJECTURAL: Clause A (a0 is THE weight) and
    Clause B (multiplicity = 2 derived from the Hecke relation) — these two
    clauses ARE the wall. Owner ruling (dd55a5748): status stays R1
    (convention/mu-sector) until A+B are derived; R2/R3 are candidate routes.

IMPLICATION DIRECTION (the user's question): deriving this conjecture does NOT
prove conj:dilogarithm-archimedean-limit. R3 CONSUMES the dilog conjecture as
input (dilog + 2pi*g identity => 1/pi); the arrow points dilog -> wall, not
wall -> dilog. If both A+B and R3 were proven, their consistency would yield a
nontrivial identity linking the heat-kernel unit to the Bloch-Suslin archimedean
pi — a cross-check, not a proof of either.

Scope guard: no alpha_k wired; no fit; 1/(8pi) stays a phase-4 identification;
nothing here derives Clause A or B. Self-contained (sympy).
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

    g, pi = sp.symbols('g pi', positive=True)
    chi = 2 - 2 * g                      # Euler characteristic, g >= 2
    area = 2 * pi * (2 * g - 2)          # hyperbolic GB: Area = -2*pi*chi = 2*pi*|chi|
    b1 = 2 * g

    # 1. GB skeleton: |chi|/(4*Area) = 1/(8*pi) IDENTICALLY in g; b1-form only at g=4
    gb = sp.simplify(sp.Abs(chi).rewrite(sp.Piecewise).subs(sp.Abs(chi), 2 * g - 2) / (4 * area) - 1 / (8 * pi))
    gb_ident = sp.simplify((2 * g - 2) / (4 * area) - 1 / (8 * pi)) == 0
    b1_eq = sp.solve(sp.Eq(1 / (pi * b1), 1 / (8 * pi)), g)
    check("gb_identity_all_genus_b1_only_g4",
          gb_ident and b1_eq == [4],
          "|chi|/(4*Area) - 1/(8pi) == 0 identically in g (Area=2pi|chi|), while "
          f"1/(pi*b1)=1/(8pi) has unique solution g={b1_eq} — corroborates main's GB "
          "adjudication (ba606720e): the measure is a (chi,Area) invariant; b1 is a g=4 "
          "coincidence")

    # 2. McKean-Singer anchor: heat-trace constant term a1 = chi/6; Bring => EXACTLY -1
    #    Tr e^{tDelta} ~ Area/(4pi t) + chi/6 + O(t); a1 = Int K /(12 pi) = 2pi*chi/(12pi) = chi/6
    a1 = sp.simplify((2 * pi * chi) / (12 * pi))
    a1_bring = a1.subs(g, 4)
    check("mckean_singer_constant_term_bring_minus1",
          sp.simplify(a1 - chi / 6) == 0 and a1_bring == -1,
          "Seeley-DeWitt a1 = IntK/(12pi) = chi/6 (McKean-Singer 1967); Bring (g=4, "
          "chi=-6) gives heat-trace constant term EXACTLY -1 — the unique-S5 genus-4 "
          "curve sits at the integer anchor of the a1 coefficient")

    # 3. multiplicity discriminant: measure = 1/(m*4pi); m=2 -> 1/(8pi) (working term),
    #    m=b1=8 -> 1/(32pi) (excluded by the data-selected denominator D*~8.003, merged
    #    forcedness audit: 8 at 10.9 sigma, 32 out of the question). m=2 is DATA-selected;
    #    deriving m=2 from the Hecke relation is Clause B, still open.
    m = sp.symbols('m', positive=True)
    msel = sp.solve(sp.Eq(1 / (m * 4 * pi), 1 / (8 * pi)), m)
    check("multiplicity_discriminant_m2_not_b1",
          msel == [2],
          "measure = 1/(m*4pi) matches the working 1/(8pi) iff m=2 (m=b1=8 would give "
          "1/(32pi), ~4x off, excluded by the merged D*=8.003 forcedness). m=2 is "
          "DATA-selected; Clause B (m=2 == the two Hecke channels e+/e-) is the open "
          "derivation — this is a scope-(a) statement, not a derivation")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "PER-LOOP WALL STATED AS A PRECISE TWO-CLAUSE CONJECTURE (scope-(a); no fit, "
        "nothing wired, 1/(8pi) stays phase-4): measure = (1/2)*a0 with Clause A (per-mode "
        "weight = universal heat-kernel unit a0 = 1/(4pi) = |chi|/(2*Area), GB-geometrized) "
        "and Clause B (multiplicity EXACTLY 2 = the Hecke channels e+/e-). Machine-checked "
        "skeleton: the GB identity holds for ALL genus (b1 reading only at g=4, corroborating "
        "main's adjudication); the McKean-Singer heat-trace constant is chi/6 = -1 EXACTLY on "
        "Bring; the multiplicity discriminant selects m=2 (m=b1 excluded ~4x). Clauses A and "
        "B remain CONJECTURAL — they are the wall. IMPLICATION: proving them does NOT prove "
        "conj:dilogarithm-archimedean-limit (R3 consumes the dilog as input; arrow runs "
        "dilog->wall). NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "alpha-em-perloop-conjecture-statement",
        "description": "States the alpha_EM 1/pi wall as a precise two-clause conjecture (A: per-mode "
                       "weight = universal heat-kernel unit a0=|chi|/(2*Area); B: multiplicity = 2 = Hecke "
                       "channels) and machine-checks the exact skeleton: GB identity all-genus (b1 only at "
                       "g=4), McKean-Singer constant chi/6=-1 on Bring, multiplicity discriminant m=2. "
                       "Clauses A+B stay conjectural (the wall). Dilog implication runs dilog->wall, not "
                       "conversely. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-perloop-conjecture-statement.md",
        "tier": "symbolic-exact skeleton (sympy) + literature anchors (McKean-Singer 1967; "
                "D'Hoker-Phong 1986 / Sarnak 1987 in the audit); Clauses A/B conjectural",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "conjecture": "measure = (1/2)*a0; A: a0 = 1/(4pi) = |chi|/(2*Area) universal; "
                          "B: multiplicity = 2 = Hecke channels (e+, e-)",
            "gb_identity_all_genus": True, "b1_reading_unique_genus": 4,
            "mckean_singer_a1_bring": -1, "multiplicity_selected": 2,
            "dilog_implication": "wall does NOT imply conj:dilogarithm-archimedean-limit "
                                 "(R3 consumes dilog as input)",
            "verdict": verdict,
        },
        "context": {
            "follows": "main ba606720e/2b562bc7d (GB adjudication, sorry-free Lean) + dd55a5748 "
                       "(R1 canonical ruling) + #3810 (channel split, owns the 1/2)",
            "literature": "McKean-Singer 1967 (a1=chi/6); D'Hoker-Phong CMP 1986 + Sarnak CMP 1987 "
                          "(det'Delta on hyperbolic surfaces = exp(c*chi)*Z'(1): established spectral "
                          "normalizations are chi-objects, corroborating the GB adjudication); Wilms "
                          "arXiv:1605.00847 / Faltings delta / Bost (the polarized-Jacobian theta "
                          "determinant framework for the deferred genus-4 Epstein piece); Zagier/ "
                          "Bloch-Wigner (the dilog regulator side of R3)",
            "scope_guard": "states + checks the skeleton; does NOT derive Clause A or B; no fit; "
                           "nothing wired; 1/(8pi) stays phase-4 (R1 canonical)",
        },
    }
    out = os.path.join(_here, "alpha-em-perloop-conjecture-statement.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
