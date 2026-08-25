#!/usr/bin/env python3
"""[1^A] value leg — Slater antisymmetrizer rank + exchange-spectrum sign/ceiling.

Executes the two named-but-unbuilt pieces of the construction spec
(docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md §5)
and the "NEXT UNIT" of b4_slater_dictionary_functional_form.py, WITHOUT fitting
any AME magnitude.

TARGET (the many-body real wall).  Single-trace Delta_lambda = (-1)^{n(lambda)}
* dim(lambda) undershoots AME connected binding; the missing piece is a >=4-body,
He4-LOCAL term.  The candidate closed form is the connected [1^4] cumulant
b4 = -ln det(I+G) with a sign-carrying (bar-odd) exchange matrix G, gated by the
SU(4) fully-antisymmetric [1^A] channel whose dimension C(4,A) vanishes for A>4.

PART 1 (parameter-free, EXACT integers) -- He4-LOCALITY of the 4-body term.
  The nucleon-flavor projector P_{[1^A]} = Lambda^A(C^4) is the S_A antisymmetrizer
  over the 4 SU(4) single-particle states (p up, p dn, n up, n dn).  Its rank is
  the antisymmetrizer TRACE on (C^4)^{otimes A}:
      rank = (1/A!) * sum_{sigma in S_A} sgn(sigma) * 4^{c(sigma)}
           = falling_factorial(4, A) / A!  =  C(4, A)         (a Lean-provable
  cycle-sum identity; here VERIFIED by exact enumeration of S_A, not asserted from
  the binomial).  Consequences, all exact and q-independent (no fit possible):
    * rank(A) = {1,4,6,4,1,0,0,...} for A = 0,1,2,3,4,5,6,7;
    * A = 5 is the FIRST vanishing  =>  b4(A>4) = 0  (He4-locality is structural);
    * A = 4 is the UNIQUE A whose fully-antisymmetric channel is the rank-1
      SINGLET -- the Wigner supermultiplet closed shell (all four states filled),
      i.e. He4 is the unique doubly-magic [1^4] closure.

PART 2 (derived pair factors, NO magnitude fit) -- the EXCHANGE SPECTRUM.
  Build the He4 [1^4] complete-graph (6 crossings) exchange matrix G = mag * S,
  S the writhe-sign pattern (pp = +1, nn = -1, pn = +-1; det-class value is
  pn-sign-invariant by the diag(1,1,-1,-1) conjugation, corpus-proved in
  QOU/MassTheory/ReebPnMagnitude.lean).  Its spectrum is EXACTLY
      eig(S) = { +sqrt5, -sqrt5, +1, -1 }  =>  det(I + mag*S) = (1 - 5*mag^2)(1 - mag^2),
  a closed form.  Structural readings, all parameter-free:
    * a NEGATIVE eigenvalue (-sqrt5*mag) is ALWAYS present  => the net-attractive
      channel the dictionary probe's sign branch (s = -1) requires exists for any
      magnitude (confirms the sign half of the NEXT UNIT, no fit);
    * det(I+G) < 1 for all 0 < mag < 1  =>  -ln det(I+G) > 0  (binding / attractive);
    * PHYSICALITY  det(I+G) > 0  requires  mag < 1/sqrt5 = 0.44721  -- this is
      EXACTLY the derived per-pair writhe cap g < 1/sqrt5.  The naive Markov bond
      factor z = 1/[2]_v = 0.4993 EXCEEDS the ceiling (det < 0, unphysical); the
      derived reeb magnitude g = 1/sqrt(5 + (q0-1)^2/q0) = 0.4467 sits just below
      it (marginal), reproducing the corpus finding that "z anywhere is unphysical
      at A=4" (2026-07-06 reeb audit, section 3h).

HONEST RESIDUAL (the open scalar).  The b4 MeV magnitude needs (i) the per-pair
magnitude selection inside (0, 1/sqrt5) and (ii) the E0 -> MeV dressing.  That
selection IS the Delta_lambda / E_unit gate (the 2026-07-06 reeb audit sec 2j
shows the A-flattened normalization = the Delta_lambda closure), on which six
parameter-free ansatze have failed and for which AGENTS.md forbids a seventh
fit-based ansatz.  So this probe DERIVES locality (exact), the attractive sign,
and the physicality-ceiling = writhe-cap (exact closed form), and leaves the
magnitude scalar CONSTRAINED-BUT-OPEN -- it is not closed here and is NOT wired.

  -- Ref: spec docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md
     (Step A' Lambda^A(4), section 5 su4_slater_antisymmetrizer.py);
     b4_slater_dictionary_functional_form.py (the NEXT UNIT executed here);
     QOU/MassTheory/SU4SupermultipletGate.lean (C(4,A)=0 iff A>4);
     QOU/MassTheory/ReebPnMagnitude.lean (pn-sign det invariance; g<1/sqrt5 ceiling).
EXPLORATORY -- audit + witness only; no production wiring, no fit.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import mpmath as mp
from sympy import binomial, factorial, ff
from sympy.combinatorics import SymmetricGroup

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
for _p in (str(_COMP), str(_COMP / "substrate")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
from substrate.witness_base import WitnessBuilder  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

COMP = str(_COMP)

# muon-canonical q0 (the computations/ layer convention; AGENTS.md q0-convention)
Q0_STR = "1.10997859555733471"


def antisymmetrizer_rank(n: int, A: int) -> int:
    """Exact rank of Lambda^A(C^n) via the antisymmetrizer trace on (C^n)^{oxA}:
        rank = (1/A!) sum_{sigma in S_A} sgn(sigma) n^{c(sigma)}.
    Verified by explicit S_A enumeration (not read off the binomial)."""
    if A == 0:
        return 1
    tot = 0
    for p in SymmetricGroup(A).generate():
        # cycles including fixed points = (# non-trivial cycles) + (# fixed points)
        n_cycles = len(p.cyclic_form) + (A - sum(len(c) for c in p.cyclic_form))
        tot += (1 if p.is_even else -1) * n ** n_cycles
    assert tot % factorial(A) == 0
    return tot // int(factorial(A))


def main() -> int:
    # ---- PART 1: Lambda^A(4) rank = C(4,A), exact ----------------------------
    ranks = {}
    for A in range(0, 8):
        r = antisymmetrizer_rank(4, A)
        cb = int(binomial(4, A))
        ff_over = int(ff(4, A) // factorial(A)) if A <= 4 else 0
        assert r == cb == ff_over, (A, r, cb, ff_over)
        ranks[A] = r
    rank_seq = [ranks[A] for A in range(0, 8)]
    first_vanishing_A = next(A for A in range(1, 8) if ranks[A] == 0)
    unique_singlet_A = [A for A in range(1, 8) if ranks[A] == 1]  # A with a rank-1 shell

    # ---- PART 2: exchange spectrum, derived magnitudes, NO fit ---------------
    set_compute_dps()
    q0 = mp.mpf(Q0_STR)
    v = mp.sqrt(q0)
    two_v = v + 1 / v
    z_naive = 1 / two_v                                   # Markov bond factor 1/[2]_v
    g_reeb = 1 / mp.sqrt(5 + (q0 - 1) ** 2 / q0)          # derived reeb magnitude
    ceiling = 1 / mp.sqrt(mp.mpf(5))                      # writhe cap g < 1/sqrt5

    # He4 [1^4] complete-graph exchange matrix G = mag*S ; S has spectrum {+-sqrt5,+-1}
    sign = {("p", "p"): 1, ("n", "n"): -1, ("p", "n"): 1, ("n", "p"): 1}
    typ = ["p", "p", "n", "n"]

    def spectrum(mag):
        M = mp.matrix(4, 4)
        for i in range(4):
            for j in range(4):
                if i != j:
                    M[i, j] = sign[(typ[i], typ[j])] * mag
        ev = sorted((mp.re(e) for e in mp.eig(M, left=False, right=False)))
        detIG = mp.det(mp.eye(4) + M)
        return ev, detIG

    rows = {}
    for name, mag in (("z_naive", z_naive), ("g_reeb", g_reeb)):
        ev, detIG = spectrum(mag)
        closed = (1 - 5 * mag ** 2) * (1 - mag ** 2)      # closed form for det(I+G)
        rows[name] = {
            "magnitude": mp.nstr(mag, 18),
            "eigs": [mp.nstr(e, 12) for e in ev],
            "det_I_plus_G": mp.nstr(detIG, 18),
            "det_closed_form_(1-5m2)(1-m2)": mp.nstr(closed, 18),
            "det_matches_closed_form": bool(abs(detIG - closed) < mp.mpf(10) ** -30),
            "physical_det_gt_0": bool(detIG > 0),
            "has_negative_eigenvalue": bool(ev[0] < 0),
            "binding_det_lt_1": bool(detIG < 1),
            "minus_ln_det_dimensionless": (mp.nstr(-mp.log(detIG), 12) if detIG > 0 else "undefined(det<=0)"),
        }

    z_excluded = rows["z_naive"]["det_I_plus_G"].startswith("-") or (not rows["z_naive"]["physical_det_gt_0"])
    g_physical = rows["g_reeb"]["physical_det_gt_0"]
    ceiling_matches = bool(abs(g_reeb - ceiling) < mp.mpf("2e-3")) and (z_naive > ceiling) and (g_reeb < ceiling)

    result = {
        "part1_locality": {
            "antisymmetrizer_rank_identity": "rank Lambda^A(C^4) = (1/A!) sum_sigma sgn(sigma) 4^{c(sigma)} = C(4,A)",
            "rank_sequence_A_0_to_7": rank_seq,
            "matches_binomial_C(4,A)": True,
            "first_vanishing_A": first_vanishing_A,       # 5
            "he4_local_b4_vanishes_for_A_gt_4": True,
            "A_with_rank1_singlet_shell": unique_singlet_A,  # [0, 4]
            "he4_A4_is_unique_doubly_magic_singlet": (4 in unique_singlet_A and 5 not in unique_singlet_A),
            "parameter_free": True,
            "verdict": "DERIVED (exact, q-independent): the 4-body [1^4] channel is He4-LOCAL "
                       "(C(4,A)=0 for A>4; A=5 first vanishing) and He4 (A=4) is the unique "
                       "rank-1 fully-antisymmetric singlet -- the Wigner-supermultiplet closed shell.",
        },
        "part2_exchange_sign_and_ceiling": {
            "S_spectrum_exact": "{+sqrt5, -sqrt5, +1, -1}",
            "det_closed_form": "det(I + mag*S) = (1 - 5*mag^2)(1 - mag^2)",
            "physicality_ceiling": mp.nstr(ceiling, 12),
            "ceiling_equals_writhe_cap_1_over_sqrt5": True,
            "z_naive_excluded_above_ceiling": bool(z_excluded),
            "g_reeb_physical_below_ceiling": bool(g_physical),
            "negative_eigenvalue_always_present": all(r["has_negative_eigenvalue"] for r in rows.values()),
            # Was the literal `True` — a vacuous check flagged by
            # circ-vacuous-check. The genuine computation is the line above
            # (and is asserted at the bottom of this file), so bind to it
            # rather than assert the conclusion.
            "attractive_channel_confirmed":
                all(r["has_negative_eigenvalue"] for r in rows.values()),
            "rows": rows,
            "verdict": "DERIVED (parameter-free, no fit): a negative eigenvalue (-sqrt5*mag) is always "
                       "present so the dictionary's net-attractive branch (s=-1, B=-ln det(I+G)) is "
                       "realized for any magnitude; det<1 => binding; and PHYSICALITY det>0 requires "
                       "mag<1/sqrt5, EXACTLY the derived writhe cap. Naive z=0.4993 is excluded "
                       "(det<0); reeb g=0.4467 sits just below the ceiling.",
        },
        "residual_open_scalar": {
            "what_is_derived": ["He4-locality (exact C(4,A))",
                                "attractive sign / -ln det branch (negative eigenvalue always present)",
                                "physicality ceiling = writhe cap 1/sqrt5 (closed form)"],
            "what_is_NOT_derived": "the per-pair magnitude selection inside (0, 1/sqrt5) and the E0->MeV "
                                   "dressing -- i.e. the b4 MeV VALUE.",
            "identification": "that magnitude selection IS the Delta_lambda / E_unit gate (reeb audit "
                              "2026-07-06 sec 2j: the A-flattened normalization = the Delta_lambda closure); "
                              "six parameter-free ansatze have failed and a seventh fit-based ansatz is "
                              "forbidden (AGENTS.md).",
            "classification": "CONSTRAINED-NOT-CLOSED. The b4 form's locality + sign + ceiling are derived "
                              "parameter-free; the remaining scalar (the bond magnitude, hence the MeV "
                              "magnitude) is the standing Delta_lambda gate and is NOT wired.",
        },
    }

    payload = {
        "computation": "b4-slater-antisymmetrizer-exchange-sign",
        "description": ("[1^4] value leg: exact Lambda^A(C^4) antisymmetrizer rank = C(4,A) "
                        "(He4-locality, A=4 unique rank-1 singlet) + exchange spectrum {+-sqrt5,+-1} "
                        "closed-form det=(1-5m^2)(1-m^2) with attractive negative eigenvalue and "
                        "physicality ceiling = writhe cap 1/sqrt5. Derives locality/sign/ceiling; "
                        "the magnitude scalar (the Delta_lambda gate) stays open. No fit, audit-only."),
        "tier": "structural (exact combinatorics + closed-form spectrum; no fit, no AME inversion)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D -- [1^4] connected b4 value leg (locality + exchange sign)",
            "spec": "docs/design/2026-07-06-gap-a4-b4-branching-projector-construction-spec.md",
            "q0_convention": "muon-canonical (computations/ layer)",
            "no_fit": True,
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-slater-antisymmetrizer-exchange-sign", payload,
        script_path=__file__, engine="python", output_dir=os.path.join(COMP, "deltalambda"),
    )
    wb.add_assertion("rank_sequence_equals_C4A", computed=str(rank_seq), expected="[1, 4, 6, 4, 1, 0, 0, 0]")
    wb.add_assertion("first_vanishing_A_is_5", computed=str(first_vanishing_A), expected="5")
    wb.add_assertion("A4_is_unique_rank1_singlet", computed=str(4 in unique_singlet_A and 5 not in unique_singlet_A), expected="True")
    wb.add_assertion("det_closed_form_holds_both_magnitudes",
                     computed=str(all(r["det_matches_closed_form"] for r in rows.values())), expected="True")
    wb.add_assertion("negative_eigenvalue_always_present",
                     computed=str(all(r["has_negative_eigenvalue"] for r in rows.values())), expected="True")
    wb.add_assertion("physicality_ceiling_equals_writhe_cap",
                     computed=str(ceiling_matches), expected="True")
    wb.add_assertion("z_naive_excluded_g_reeb_physical",
                     computed=str(z_excluded and g_physical), expected="True")
    out = wb.save(extra={"auditOnly": True})

    print("=== [1^4] Slater antisymmetrizer rank + exchange spectrum sign/ceiling ===")
    print(f"PART 1  rank Lambda^A(C^4) = C(4,A), A=0..7 : {rank_seq}   (first vanishing A={first_vanishing_A})")
    print(f"        He4 (A=4) is the unique rank-1 fully-antisymmetric SINGLET (doubly-magic closed shell).")
    print(f"        => 4-body [1^4] term is He4-LOCAL, exact and q-independent (no fit possible).")
    print(f"PART 2  eig(S) = {{+-sqrt5, +-1}} ; det(I+mag*S) = (1-5 mag^2)(1-mag^2)")
    for name, r in rows.items():
        print(f"   {name:8}: mag={r['magnitude'][:8]}  det(I+G)={r['det_I_plus_G'][:10]}  "
              f"physical={r['physical_det_gt_0']}  neg_eig={r['has_negative_eigenvalue']}  "
              f"-lndet={r['minus_ln_det_dimensionless']}")
    print(f"        physicality ceiling = 1/sqrt5 = {mp.nstr(ceiling, 8)}  == derived writhe cap.")
    print(f"        naive z EXCLUDED (det<0); reeb g physical, just below ceiling.")
    print("RESIDUAL open scalar: the per-bond magnitude (the Delta_lambda / E_unit gate) -- NOT closed, NOT wired.")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
