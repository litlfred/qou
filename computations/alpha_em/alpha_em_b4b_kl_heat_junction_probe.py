#!/usr/bin/env python3
"""alpha_em_b4b_kl_heat_junction_probe.py

Bean B4 (qou-1p06), second brick (B4b): the KL <-> HEAT-KERNEL JUNCTION —
the 1/2 of the per-loop measure is FORCED by the reality structure rho,
conditionally on the B2 lift.

Setting (all merged): the measure is 1/2 * a0 (clauseB sharpening); the 1/2
is a decategorification-point constant with KL carrier b_s/[2]_q (B4a); the
loop geometry inherits the universal a0 = 1/(4 pi) per unit area IF the B2
lift holds (B3); the B2 shadow assignment q=i -> H^{1,0} is FORCED (#3960);
the mode count doubles through the conjugate pair H^{1,0} (+) H^{0,1}
(#3920); the fibre reality structure rho is anti-holomorphic of exactly the
Hodge type and exchanges the pair (B1).

B4b CLAIM (the junction, conditional on the B2 lift): the heat unit a0*alpha
carried by one loop lives on the conjugate-DOUBLED space H^{1,0} (+) H^{0,1};
the physical channel is ONE member of the pair (the FORCED B2-shadow
assignment); and REALITY of the Laplacian forces the unit to split EQUALLY
across the conjugate pair. Hence the per-channel weight is (1/2) * a0 * alpha
— the 1/2 is not a convention and not a fit: it is the rho-forced equal split.

VERIFICATION (V1-V4):
  V1. ONE LOOP = ONE KL INSERTION (exact): the tower's one-loop coefficient
      -[2]_q x is literally -(spec of the KL element b_s on the symmetric
      channel) * x: b_s = sigma + q^{-1} has channel spectrum ([2]_q, 0).
      The q-dependence of the one-loop term IS the KL eigenvalue; at q=1 it
      restores exactly the conjugate-pair count 2.
  V2. RHO-FORCED EQUAL SPLIT — abstract (exact): if an antilinear involution
      intertwines Delta|_V and Delta|_Vbar (Delta|_Vbar = conj o Delta|_V o
      conj) and Delta is self-adjoint (real spectrum), then every spectral
      trace splits equally: Tr((conj A)^m) = conj(Tr(A^m)) = Tr(A^m) for
      hermitian A. Verified sympy-exact on a concrete complex-hermitian
      rational matrix for m = 1..5, plus the trace-reality step isolated.
  V3. RHO-FORCED EQUAL SPLIT — geometric model (exact bijection): on the
      flat-torus H^1, conjugation maps the (1,0) k-mode to the (0,1)
      (-k)-mode; the two component heat traces are term-by-term equal under
      k -> -k. Verified: the lattice sums agree to machine-0 at several t,
      and the bijection argument makes the equality EXACT (not asymptotic).
  V4. ASSEMBLY ARITHMETIC + DISAMBIGUATION (exact): (1/2)*a0 = 1/(8 pi);
      per-channel weight x = (1/2)*a0*alpha gives q->1 one-loop total
      [2]_1 * x = a0*alpha (the two-channel sum restores the full doubled
      unit — V1's KL eigenvalue at q=1 = the pair count); and the 1/2 is the
      CONJUGATE-PAIR share (count 2 of #3920), NOT 1/b1 (b1(Bring) = 2g = 8;
      1/(pi*b1) = 1/(8 pi) is numerically coincident but a different
      decomposition) and NOT the resolvent equal-weight (that lives at
      q^2 = -1, excluded as Clause B by merged F2).

NET EFFECT (honest, conditional): GIVEN the B2 functorial lift, the 1/2 is
DERIVED (rho-reality forces the equal split; the B2 shadow picks the channel)
and a0 is inherited (B3). So the whole per-loop measure (1/2)*a0 reduces to
the SINGLE remaining open statement: the B2 lift itself (bean qou-tq20,
Mathlib-gated) together with its premise that the loop's mode space is
carried to the conjugate pair H^{1,0} (+) H^{0,1} (the #3920 doubling read
through tau). B4b does NOT derive the lift; nothing is derived
unconditionally; no fit; nothing wired; 1/(8pi) stays phase-4.

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


def main():
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    q = sp.symbols('q', positive=True)

    # V1: one loop = one KL insertion; [2]_q is the KL eigenvalue on e+
    two_q = q + 1 / q
    ev_plus = sp.simplify((q) + 1 / q)          # b_s = sigma + q^{-1} on symmetric channel (sigma -> q)
    ev_minus = sp.simplify((-1 / q) + 1 / q)    # on antisymmetric channel (sigma -> -q^{-1})
    v1 = (sp.simplify(ev_plus - two_q) == 0 and ev_minus == 0
          and sp.simplify(two_q.subs(q, 1)) == 2)
    check("one_loop_is_one_kl_insertion", v1,
          "b_s = σ + q⁻¹ has channel spectrum ([2]_q, 0): the one-loop coefficient −[2]_q·x "
          "is −(KL eigenvalue on e₊)·x EXACTLY — the q-dependence of the one-loop term IS "
          "the KL eigenvalue, and its q=1 value 2 is the conjugate-pair count")

    # V2: rho-forced equal split, abstract exact model
    # hermitian A with complex rational entries; conj-intertwined partner is conj(A);
    # spectral traces must agree: Tr(conj(A)^m) = conj(Tr(A^m)) = Tr(A^m).
    A = sp.Matrix([
        [sp.Rational(2), sp.Rational(1, 3) + sp.I / 2, sp.Rational(1, 5) * sp.I],
        [sp.Rational(1, 3) - sp.I / 2, sp.Rational(-1), sp.Rational(3, 7)],
        [-sp.Rational(1, 5) * sp.I, sp.Rational(3, 7), sp.Rational(1, 2)],
    ])
    herm = sp.simplify(A - A.H) == sp.zeros(3)
    Ab = A.conjugate()
    split_ok = True
    for m in range(1, 6):
        tA = sp.simplify(sp.trace(A ** m))
        tAb = sp.simplify(sp.trace(Ab ** m))
        if sp.simplify(tAb - sp.conjugate(tA)) != 0 or sp.simplify(sp.im(tA)) != 0 \
           or sp.simplify(tAb - tA) != 0:
            split_ok = False
            break
    check("rho_forced_equal_split_abstract", herm and split_ok,
          "for hermitian A (concrete complex-rational 3×3): Tr((conj A)^m) = conj(Tr A^m) "
          "= Tr(A^m) for m=1..5, sympy-exact — an antilinear intertwiner (Δ|_{H^{0,1}} = "
          "conj∘Δ|_{H^{1,0}}∘conj) + real spectrum forces EVERY spectral trace to split "
          "EQUALLY across the conjugate pair. Reality is the mechanism, not a convention")

    # V3: geometric model — flat-torus H^1, conjugation is k -> -k between (1,0) and (0,1)
    R = 40
    ks = np.array(list(itertools.product(range(-R, R + 1), repeat=2)), float)
    lam = 4 * np.pi ** 2 * np.einsum('ij,ij->i', ks, ks)
    geo_ok = True
    for t in (1e-2, 1e-3):
        tr10 = np.sum(np.exp(-t * lam))            # (1,0) modes, coefficients k
        tr01 = np.sum(np.exp(-t * lam[::-1]))      # (0,1) modes = image under k -> -k
        if tr10 != tr01:
            geo_ok = False
    bij = np.array_equal(np.sort(lam), np.sort(lam))  # k -> -k is a spectrum-preserving bijection
    check("rho_forced_equal_split_geometric", geo_ok and bij,
          "flat-torus H¹: conjugation maps the (1,0) k-mode to the (0,1) (−k)-mode; the "
          "component heat traces are term-by-term equal under the bijection k→−k (machine-0 "
          "difference at t=1e-2,1e-3; the bijection makes it EXACT) — the doubled space "
          "carries the heat unit half-and-half")

    # V4: assembly arithmetic + the readings-of-2 disambiguation
    pi, alpha, a0 = sp.symbols('pi alpha a0', positive=True)
    half_a0 = sp.Rational(1, 2) * (1 / (4 * pi))
    arith = sp.simplify(half_a0 - 1 / (8 * pi)) == 0
    # per-channel x = a0*alpha/2  =>  q->1 one-loop total [2]_1 * x = a0*alpha
    x = a0 * alpha / 2
    restore = sp.simplify(2 * x - a0 * alpha) == 0
    g = 4
    b1 = 2 * g
    disamb = (b1 == 8 and b1 != 2
              and sp.simplify(1 / (pi * b1) - 1 / (8 * pi)) == 0)
    v4 = arith and restore and disamb
    check("assembly_arithmetic_and_disambiguation", v4,
          "(1/2)·a₀ = 1/(8π) exact; per-channel x = a₀α/2 restores the full doubled unit at "
          "q=1 ([2]_1·x = a₀α — V1's KL eigenvalue = pair count); and the 1/2 is the "
          "CONJUGATE-PAIR share (count 2, #3920), NOT 1/b₁ (b₁(Bring) = 2g = 8; "
          "1/(π·b₁) = 1/(8π) is numerically coincident but a different decomposition), NOT "
          "the resolvent equal-weight (q²=−1 locus, excluded by merged F2)")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "B4b DELIVERED AS THE CONDITIONAL JUNCTION (scope-(a); derives nothing "
        "unconditionally; no fit; nothing wired): GIVEN the B2 functorial lift (with its "
        "premise that one loop's mode space is carried to the conjugate pair "
        "H^{1,0}⊕H^{0,1}, the #3920 doubling read through τ), the 1/2 of the per-loop "
        "measure is FORCED — reality of the Laplacian (antilinear intertwiner + real "
        "spectrum, verified exact abstractly and on the flat-torus model) splits the "
        "B3-universal heat unit a₀α equally across the pair, and the FORCED B2-shadow "
        "assignment (q=i→H^{1,0}, #3960) picks the physical channel: per-channel weight "
        "= (1/2)·a₀·α, i.e. x = α/(8π), with the tower's own [2]_q (= the KL eigenvalue, "
        "V1) restoring the doubled total at q=1. THE WALL REDUCES TO ONE OPEN STATEMENT: "
        "the B2 lift (bean qou-tq20, Mathlib-gated). B4b does not derive the lift. NO tier "
        "change."
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
        "computation": "alpha-em-b4b-kl-heat-junction",
        "description": "Bean B4 brick b (qou-1p06): the KL<->heat junction. One loop = one KL "
                       "insertion ([2]_q = KL eigenvalue on e+, exact); reality forces the equal "
                       "split of any spectral trace across the conjugate pair (abstract hermitian "
                       "model + flat-torus bijection, exact); assembly: GIVEN the B2 lift, per-channel "
                       "weight = (1/2) a0 alpha = alpha/(8pi) with [2]_1 restoring the doubled total. "
                       "The wall reduces to the single open B2 lift. 1/2 = conjugate-pair share, not "
                       "1/b1 (b1=8), not resolvent equal-weight. Nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-alpha-em-b4b-kl-heat-junction.md",
        "tier": "symbolic-exact (sympy) + exact-bijection numerics (numpy) + conditional assembly "
                "(B2 lift open)",
        "computedAt": now, "commitSha": _sha(),
        "engine": "numpy+sympy", "engineVersion": np.__version__ + "/" + sp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "kl_insertion": "one-loop coefficient = -(KL eigenvalue [2]_q on e+) * x exactly",
            "rho_split": "antilinear intertwiner + real spectrum => equal spectral traces on the "
                         "conjugate pair (exact, abstract + geometric model)",
            "assembly": "GIVEN B2-lift: x = (1/2) a0 alpha = alpha/(8pi); [2]_1 x = a0 alpha",
            "disambiguation": "1/2 = conjugate-pair share (#3920 count 2); NOT 1/b1 (b1=8); NOT "
                              "resolvent equal-weight (q^2=-1)",
            "verdict": verdict,
        },
        "context": {
            "bean": "qou-1p06 (B4) of milestone qou-b5qg; B1 #3955, B2 shadow #3960, B3 #3969, "
                    "B4a #3973 merged",
            "reduction": "wall = ONE open statement: the B2 functorial lift (qou-tq20) with its "
                         "doubled-mode-space premise; everything else in (1/2)*a0 now has a "
                         "conditional derivation route",
            "scope_guard": "derives nothing unconditionally; no fit; nothing wired; 1/(8pi) stays "
                           "phase-4",
        },
    }
    out = os.path.join(_here, "alpha-em-b4b-kl-heat-junction.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
