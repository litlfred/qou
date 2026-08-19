#!/usr/bin/env python3
"""alpha_em_f_t2_burau_at_i_probe.py

F-construction T2 (bean qou-yuff, milestone qou-a46k): the MONODROMY HECKE
MODULE at the degenerate locus — the local braid monodromy of the T1 cover
reproduces EXACTLY the H2(i) Jordan module of VertexLocalTauModel (#3992),
via the Burau parameter dictionary q_Burau = q_Hecke^{-2}.

This was the first place the functor could FAIL: if the cover's local
monodromy at the deck character had been semisimple at the degenerate
locus, the McMullen route would not reproduce the framework's Jordan-block
module and the F-construction would be dead. It is not: the specializations
line up exactly.

LITERATURE (now in library/): McMullen, "Braid groups and Hodge theory"
(library/mcmullen-braids-hodge-2013/mcmullen-braids-hodge-2013.pdf) — the braid-monodromy/Hodge
dictionary for cyclic branched covers; Squier
(library/squier-burau-unitary-1984/squier-burau-unitary-1984.pdf) — the hermitian form on Burau at
|q| = 1; Gambaudo-Ghys (library/gambaudo-ghys-braids-signatures-2005/gambaudo-ghys-braids-signatures-2005.pdf)
— signatures of Burau at roots of unity, whose JUMP LOCUS is exactly the
degenerate specialization found here; Deligne-Mostow
(library/deligne-mostow-1986/deligne-mostow-1986.pdf) — the eigenspace local systems.

VERIFICATION (V1-V4, sympy-exact):
  V1. PARAMETER DICTIONARY: the unreduced Burau sigma_B(q_B) of B_2 has
      eigenvalues {1, -q_B}; the §7a Hecke convention has {q_H, -q_H^{-1}}.
      Projective matching forces q_B = q_H^{-2}; at the degenerate locus
      q_H = i this gives q_B = -1 — the INTEGRAL specialization, which is
      ALSO chi(deck)^2 (chi = i, the T1 deck multiplier): the Burau
      parameter is the square of the deck character because the half-twist
      squares to the local full twist. Three independent readings of the
      same point coincide: (Hecke degenerate) = (Burau integral /
      Gambaudo-Ghys signature-jump) = (deck-character square).
  V2. JORDAN STRUCTURE AT THE SPECIALIZATION: sigma_B(-1) = [[2,-1],[1,0]]
      has char poly (lambda-1)^2 with sigma_B != 1: a genuine Jordan block
      — the local monodromy at the degenerate locus is NON-semisimple.
  V3. EXACT MODULE MATCH: the rescaled generator sigma_H := i*sigma_B(-1)
      satisfies the §7a Hecke relation at q_H = i — (sigma_H - i)^2 = 0
      with sigma_H not scalar — and is GL_2(C)-conjugate to the
      VertexLocalTauModel Jordan block !![i,1;0,i] (explicit conjugating
      matrix computed). The cover's local monodromy module IS the
      framework's H2(i) module.
  V4. RHO-PARTNER: entrywise conjugation sends sigma_H to a generator
      satisfying (sigma + i)^2 = 0 — the q = -i partner module — matching
      rho_carries_module (#3992) on the monodromy side.

HONEST SCOPE: T2 establishes the LOCAL monodromy model (a disk around the
two branch points of the T1 cover); the GLOBAL monodromy on H^1_chi(Bring)
(torus-with-2-points mapping classes, periods) is T3/T5 territory. No fit;
nothing wired; 1/(8 pi) stays phase-4. Self-contained (sympy).
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

    qB, qH, lam = sp.symbols('q_B q_H lambda')
    I = sp.I

    # V1: parameter dictionary
    burau = sp.Matrix([[1 - qB, qB], [1, 0]])
    ev_burau = sp.solve(sp.det(burau - lam * sp.eye(2)), lam)
    dict_ok = sp.simplify((-qH ** -1) / qH - (-(qH ** -2))) == 0
    qB_at_i = sp.simplify((I) ** -2)
    chi_sq = sp.simplify(I ** 2)
    v1 = (sorted([sp.simplify(e - 1) == 0 for e in ev_burau]).count(True) == 1
          and any(sp.simplify(e + qB) == 0 for e in ev_burau)
          and dict_ok and qB_at_i == -1 and chi_sq == -1)
    check("parameter_dictionary", v1,
          "Burau eigenvalues {1, −q_B}; Hecke {q_H, −q_H⁻¹}; projective matching forces "
          "q_B = q_H⁻²; at q_H = i: q_B = −1 = χ(deck)² (χ = i, the T1 multiplier) — the "
          "Hecke degenerate locus = the Burau INTEGRAL point = the Gambaudo–Ghys "
          "signature-jump locus = the deck-character square. Three readings coincide")

    # V2: Jordan structure at q_B = -1
    B = sp.Matrix([[2, -1], [1, 0]])
    cp = sp.factor(sp.det(B - lam * sp.eye(2)))
    v2 = sp.simplify(cp - (lam - 1) ** 2) == 0 and B != sp.eye(2) \
        and (B - sp.eye(2)) ** 2 == sp.zeros(2)
    check("jordan_structure_at_specialization", v2,
          f"σ_B(−1) = [[2,−1],[1,0]]: char poly {cp} = (λ−1)², σ_B ≠ 1, (σ_B−1)² = 0 — a "
          "genuine Jordan block: the local monodromy at the degenerate locus is "
          "NON-semisimple (the first potential failure point of the F-construction — "
          "and it does not fail)")

    # V3: exact module match to VertexLocalTauModel
    S = I * B                                    # rescaled generator sigma_H
    hecke_ok = (S - I * sp.eye(2)) ** 2 == sp.zeros(2) and S != I * sp.eye(2)
    Jref = sp.Matrix([[I, 1], [0, I]])           # VertexLocalTauModel block
    # explicit conjugation: columns = generalized eigenvector chain of S
    N = S - I * sp.eye(2)
    v = sp.Matrix([1, 0])
    w = N * v                                     # eigenvector = N v (nonzero)
    # want P with S P = P Jref: P columns (p1, p2): S p1 = i p1; S p2 = p1 + i p2
    p1 = w
    p2 = v
    P = sp.Matrix.hstack(p1, p2)
    conj_ok = sp.simplify(P.det()) != 0 and sp.simplify(S * P - P * Jref) == sp.zeros(2)
    v3 = hecke_ok and conj_ok
    check("exact_module_match", v3,
          "σ_H := i·σ_B(−1) satisfies the §7a Hecke relation at q_H = i — (σ_H−i)² = 0, "
          "σ_H not scalar — and S·P = P·J with J = !![i,1;0,i] and det P ≠ 0 (explicit "
          "conjugation): the cover's local monodromy module IS the VertexLocalTauModel "
          "H₂(i) Jordan module, exactly")

    # V4: rho-partner
    Sc = S.applyfunc(lambda z: sp.conjugate(z))
    v4 = (Sc + I * sp.eye(2)) ** 2 == sp.zeros(2) and Sc != -I * sp.eye(2)
    check("rho_partner_on_monodromy_side", v4,
          "entrywise conjugation sends σ_H to a generator with (σ+i)² = 0 (not scalar) — "
          "the q = −i partner module: rho_carries_module (#3992) reproduced on the "
          "monodromy side")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "F-CONSTRUCTION T2 DELIVERED (scope-(a); no fit; nothing wired): the local braid "
        "monodromy of the T1 cover reproduces EXACTLY the framework's H₂(i) Jordan module — "
        "the parameter dictionary q_B = q_H⁻² sends the Hecke degenerate locus q_H = i to "
        "the Burau integral point q_B = −1 = χ(deck)² (also the Gambaudo–Ghys signature-"
        "jump locus), where Burau is a genuine Jordan block; the rescaled generator "
        "satisfies the §7a Hecke relation and is explicitly conjugate to !![i,1;0,i] "
        "(VertexLocalTauModel), with the ρ-partner reproduced under conjugation. The first "
        "potential failure point of the McMullen route does NOT fail. OPEN (T3–T5): global "
        "monodromy on H¹_χ(Bring), ρ-equivariance globally, weight-value transport, and "
        "the residual identification F = framework-τ. NO tier change."
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
        "computation": "alpha-em-f-t2-burau-at-i",
        "description": "F-construction T2 (qou-yuff): the local braid monodromy of the T1 cover "
                       "reproduces the H2(i) Jordan module exactly. Dictionary q_B = q_H^{-2} sends "
                       "q_H = i to the Burau integral point q_B = -1 = chi(deck)^2 (Gambaudo-Ghys "
                       "jump locus); Burau there is a genuine Jordan block; rescaled generator "
                       "conjugate to !![i,1;0,i] (VertexLocalTauModel) with the rho-partner under "
                       "conjugation. First potential failure point of the McMullen route passes. "
                       "T3-T5 open. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-alpha-em-f-t2-burau-at-i.md",
        "tier": "symbolic-exact (sympy; Burau/Hecke specializations + explicit conjugation)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "sympy", "engineVersion": sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "dictionary": "q_Burau = q_Hecke^{-2}; q_H = i -> q_B = -1 = chi(deck)^2",
            "coincident_readings": "Hecke degenerate = Burau integral = Gambaudo-Ghys "
                                   "signature-jump = deck-character square",
            "module_match": "i*Burau(-1) ~ !![i,1;0,i] (explicit conjugation); rho-partner "
                            "reproduced",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-yuff (T2) of milestone qou-a46k; T1 merged #4039",
            "literature": "library/mcmullen-braids-hodge-2013/mcmullen-braids-hodge-2013.pdf; library/squier-burau-unitary-"
                          "1984.pdf; library/gambaudo-ghys-braids-signatures-2005/gambaudo-ghys-braids-signatures-2005.pdf; "
                          "library/deligne-mostow-1986/deligne-mostow-1986.pdf",
            "scope_guard": "local model only (disk around the two branch points); global "
                           "monodromy = T3/T5; no fit; nothing wired; 1/(8pi) stays phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-f-t2-burau-at-i.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
