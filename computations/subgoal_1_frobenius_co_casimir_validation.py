"""subgoal_1_frobenius_co_casimir_validation.py — Subgoal-1 Phase D.

Independent reproduction of the Frobenius co-Casimir term
(T4 of the unified knot mass formula, thm:knot-mass-formula-unified):

    Frob(n) = m_e · Σ_{λ ⊢ n} 1/dim_q(λ)      [n = 3A for isotope]

This is the third additive piece of the multi-term mass formula

    m(K) = |tr_M(T_w)| + brane-tower(n) + m_e · Σ_{λ⊢n} 1/dim_q(λ)

documented in knot-mass-formula-unified.md §168-198.  The
single-term SDP flagship (B = m_e·ρ·tr_M(T_w)) used in
joint_tower_sdp_solver_v2.py omits this term — which is why the
deuteron 6_2 fails single-term PSD-feasibility (audit
2026-06-02-subgoal-1-sdp-canonical-knot-run.md).

Cross-checks the Frobenius sum against the documented values:

  | atom | n=3A | m_e·Σ_{λ⊢n} 1/dim_q(λ) (documented) |
  | D    | 6    | 1.636 MeV                          |
  | T    | 9    | 1.300 MeV                          |
  | 4He  | 12   | 1.151 MeV                          |
  | p    | 3    | 1.276 MeV (= m_e·(2 + 1/[2]_q))    |

Ref: content/.../mass-theory/knot-mass-formula-unified.md §150-198
Ref: docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
_sys.path.insert(0, str(_Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from q_parameter import Q_MP as Q_CANONICAL  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from murnaghan_nakayama import dim_q_lambda  # noqa: E402

set_compute_dps()

q = mp.mpf(str(Q_CANONICAL))
m_e = M_E_MEV

# Documented target values (knot-mass-formula-unified.md §194-198 + §156)
DOCUMENTED = {
    3: mp.mpf("1.276"),   # proton: m_e·(2 + 1/[2]_q)
    6: mp.mpf("1.636"),   # D
    9: mp.mpf("1.300"),   # T, 3He
    12: mp.mpf("1.151"),  # 4He
}


def partitions(n: int):
    """All integer partitions of n as descending tuples."""
    if n == 0:
        yield ()
        return

    def helper(m: int, maxp: int):
        for first in range(min(m, maxp), 0, -1):
            if first == m:
                yield (first,)
            else:
                for rest in helper(m - first, first):
                    yield (first,) + rest

    yield from helper(n, n)


def frobenius_co_casimir(n: int) -> mp.mpf:
    """Σ_{λ ⊢ n} 1/dim_q(λ) — Frobenius co-Casimir at H_n(q_0).

    Uses the shared `murnaghan_nakayama.dim_q_lambda` (the canonical
    q-dimension). The documented target values came from a different
    code path (`probe_term4_conventions.py`), so this remains an
    independent cross-check while reusing the centralized utility.
    """
    return sum((1 / dim_q_lambda(lam, q) for lam in partitions(n)), mp.mpf(0))


def main() -> int:
    print(f"Frobenius co-Casimir validation @ q_0 = {mp.nstr(q, 12)}")
    print(f"  m_e = {m_e} MeV")
    print()
    print(f"  {'atom':4s} {'n=3A':>5s} {'Σ 1/dim_q':>14s} "
          f"{'m_e·Σ (MeV)':>14s} {'documented':>11s} {'match':>8s}")
    print("  " + "-" * 62)

    w = WitnessBuilder("subgoal-1-frobenius-co-casimir-validation",
                       engine="mpmath")
    w.set_description(
        "Independent reproduction of the Frobenius co-Casimir term "
        "(T4) of the unified knot mass formula: m_e·Σ_{λ⊢3A} 1/dim_q(λ). "
        "Validates against documented values (D=1.636, T=1.300, "
        "4He=1.151, proton=1.276 MeV per knot-mass-formula-unified.md). "
        "This term is omitted by the single-term SDP flagship, which is "
        "why deuteron 6_2 fails single-term PSD-feasibility."
    )

    atom_for_n = {3: "p", 6: "D", 9: "T", 12: "4He"}
    all_match = True
    for n in [3, 6, 9, 12]:
        A = n // 3
        sig = frobenius_co_casimir(n)
        frob = m_e * sig
        doc = DOCUMENTED[n]
        # Match to 3-decimal documented precision (rounding tolerance)
        match = abs(frob - doc) < mp.mpf("0.001")
        all_match = all_match and match
        atom = atom_for_n[n]
        print(f"  {atom:4s} {n:>5d} {mp.nstr(sig, 11):>14s} "
              f"{mp.nstr(frob, 9):>14s} {mp.nstr(doc, 5):>11s} "
              f"{'✓' if match else '✗':>8s}")
        w.add_data(f"frobenius_sum_n{n}", mp.nstr(sig, 30))
        w.add_data(f"m_e_times_sum_n{n}_MeV", mp.nstr(frob, 30))
        w.add_assertion(
            name=f"frobenius_co_casimir_n{n}_matches_documented",
            computed=float(frob),
            expected=float(doc),
            tolerance=1e-3,
            source=f"knot-mass-formula-unified.md (n={n}, A={A})",
        )

    print()
    print(f"  All match documented: {'YES ✓' if all_match else 'NO ✗'}")
    print()
    print("  This is the third additive term of the multi-term mass")
    print("  formula. The single-term SDP flagship omits it, which is")
    print("  why deuteron 6_2 fails single-term PSD-feasibility (see")
    print("  docs/audits/2026-06-02-subgoal-1-sdp-canonical-knot-run.md).")

    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
