#!/usr/bin/env python3
# polynomial_q_not_applicable: structural/numeric cross-check harness.
"""Tier 1.B cross-check: the orbit-reduction API is correct and the
``|orbit|`` multiplier is absent.

Structural checks (fast, no trace) over A ≤ 8:
  S1. ``atom_braid_orbit_representative`` returns the canonical ``p…pn…n``.
  S2. ``orbit_size == Z!·N!`` and is metadata (never multiplied into a trace).
  S3. interface-minimality — canonical has exactly one ``pn`` crossing, and
      no other ordering of the same multiset has fewer.
  S4. the canonical word is byte-identical to the production
      ``atom_braid_word_3A`` (production path unchanged).

Numerical checks (two cheap traces):
  N1. ``|orbit|``-factor guard on ³He (Z=2,N=1, orbit_size=2!·1!=2):
      ``tr_M_via_orbit_representative(2,1) == tr_M_atomic_fast(2,1)``.
      A stray ``Z!·N!`` factor would make these differ by 2×.
  N2. value smoke on ⁴He: ``tr_M_via_orbit_representative(2,2)`` reproduces
      the post-re-pin canonical ``0.0553483351…`` @50dps.
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from itertools import permutations
from math import factorial
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from atom_orbit_reduction import (  # noqa: E402
    atom_braid_orbit_representative, atom_braid_word_ordered,
    interface_multiset, tr_M_via_orbit_representative,
)
from witness_base import WitnessBuilder  # noqa: E402
from lean_uniqueness_refs import lean_uniqueness_ref  # noqa: E402


def min_pn_over_orderings(Z: int, N: int) -> int:
    """Smallest pn-interface count over all orderings of the multiset."""
    best = None
    seen = set()
    for perm in permutations("p" * Z + "n" * N):
        if perm in seen:
            continue
        seen.add(perm)
        npn = interface_multiset(perm).get("pn", 0)
        best = npn if best is None else min(best, npn)
    return best if best is not None else 0


def main() -> int:
    w = WitnessBuilder("tier-1b-orbit-reduction-crosscheck",
                       engine="python+mpmath")
    w.set_description(
        "Tier 1.B cross-check: atom_braid_orbit_representative + "
        "tr_M_via_orbit_representative are correct and carry NO |orbit| "
        "(Z!·N!) trace multiplier. Structural (canonical ordering, orbit_size "
        "metadata, interface-minimality, byte-identical production word) over "
        "A≤8, plus the ³He |orbit|-factor guard and the ⁴He value smoke "
        "@50dps. Confirms the corrected identity tr_M(β)=tr_M(rep)."
    )
    w.set_audit_only("docs/audits/2026-05-30-tier-1b-orbit-reduction.md")

    cases = [(1, 1), (2, 1), (2, 2), (3, 2), (3, 3), (4, 3), (4, 4)]
    ok = True

    print("── structural (A≤8, no trace) ──")
    for Z, N in cases:
        rep = atom_braid_orbit_representative(Z, N)
        from mass_at_3A_proper import atom_braid_word_3A
        s1 = rep.ordering == "p" * Z + "n" * N
        s2 = rep.orbit_size == factorial(Z) * factorial(N)
        # interface-minimal: canonical pn-count equals the global minimum.
        s3 = rep.n_pn == min_pn_over_orderings(Z, N) == (1 if Z and N else 0)
        s4 = rep.word == atom_braid_word_3A(Z, N)
        row = s1 and s2 and s3 and s4
        ok = ok and row
        print(f"  ({Z},{N}) A={Z+N:>2}: ordering={rep.ordering:>8} "
              f"orbit_size={rep.orbit_size:>5} ifaces={rep.interfaces} "
              f"n_pn={rep.n_pn} byte_identical={s4} [{'✓' if row else '✗'}]")
        w.add_assertion(f"structural_{Z}_{N}", computed=float(row),
                        expected=1.0, tolerance=0.0,
                        source="canonical ordering + orbit_size meta + "
                               "interface-minimal + byte-identical word")

    print("\n── numerical ──")
    from hecke_laurent_fast import tr_M_atomic_fast
    from q_parameter import Q_50_DIGIT_STR
    from hecke_symbolic import q as qs
    qsp = sp.Float(Q_50_DIGIT_STR, 50)

    def evalq(expr):
        return expr.subs(qs, qsp).evalf(50)

    # N1: |orbit|-factor guard on ³He = (Z=2,N=1) (orbit_size = 2!·1! = 2).
    via = evalq(tr_M_via_orbit_representative(2, 1))
    direct = evalq(tr_M_atomic_fast(2, 1))
    delta = abs(via - direct)
    n1 = delta < sp.Float(10) ** -40
    ok = ok and n1
    print(f"  N1 ³He |orbit|-guard: via={str(via)[:18]} "
          f"direct={str(direct)[:18]} Δ={float(delta):.1e} "
          f"(orbit_size=2, must be 1×) [{'✓' if n1 else '✗ STRAY FACTOR'}]")
    w.add_assertion("N1_orbit_factor_guard_he3", computed=float(delta),
                    expected=0.0, tolerance=1e-40,
                    source="tr_M_via_orbit_representative(2,1) == "
                           "tr_M_atomic_fast(2,1); a Z!·N! factor would be 2×")

    # N2: ⁴He value smoke @50dps vs post-re-pin canonical.
    he4 = evalq(tr_M_via_orbit_representative(2, 2))
    ref = sp.Float("0.0553483351637685668", 50)
    d2 = abs(he4 - ref)
    n2 = d2 < sp.Float(10) ** -6
    ok = ok and n2
    print(f"  N2 ⁴He value smoke: tr_M={str(he4)[:20]} "
          f"(canonical {str(ref)[:12]}, Δ={float(d2):.1e}) [{'✓' if n2 else '✗'}]")
    w.add_assertion("N2_he4_value_smoke", computed=float(he4),
                    expected=float(ref), tolerance=1e-6,
                    source="tr_M_via_orbit_representative(2,2) @50dps")

    w.add_data("conclusion", {
        "api_correct": bool(ok),
        "orbit_multiplier_present": False,
        "identity": "tr_M(beta) = tr_M(rep)  [no |orbit| factor]",
        "canonical_interface_minimal": True,
    })
    w.add_data("lean_uniqueness_ref", lean_uniqueness_ref("proton"))
    w.save()

    print("\n" + "=" * 60)
    print("TIER 1.B ORBIT-REDUCTION CROSS-CHECK: " +
          ("PASS" if ok else "FAIL"))
    print("=" * 60)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
