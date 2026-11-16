#!/usr/bin/env python3
"""
Hecke trace engine — general-purpose computation for any N(p,n).

Computes the Gröbner--Shirshov-reduced Hecke representation of any nucleus:
  - Factored Markov trace (exact, O(A²))
  - Generator volumes V̂_i = z·a_i + b_i
  - Fractional ideal volume e(I)/e(R) at converting generator
  - Ground-state ordering (exact for A ≤ 14, heuristic for A > 14)
  - Parent/daughter comparison for beta decay
  - Full witness JSON

Usage:
    # As CLI
    python3 -m folio_assistant.computations.hecke_engine 6 8        # ¹⁴C
    python3 -m folio_assistant.computations.hecke_engine 83 127     # ²¹⁰Bi
    python3 -m folio_assistant.computations.hecke_engine --all       # all verification nuclei

    # As library
    from folio_assistant.computations.hecke_engine import HeckeEngine
    engine = HeckeEngine(q=1.110)
    result = engine.compute(p=6, n=8)
    print(result.trace, result.eIeR, result.Q_local)

Output:
    JSON to stdout (piped) or to witness file (--witness)
"""


# Path bridge (subdirectory refactor — Phase 4, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import json
import math
from mpmath import mp  # noqa: F401
import sys
import time

sys.set_int_max_str_digits(100000)
from dataclasses import dataclass, field, asdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Optional

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent


# ── Exact rational arithmetic ────────────────────────────────────

class HeckeRational:
    """Rational arithmetic with q = p_num/p_den."""
    def __init__(self, p_num=111, p_den=100):
        self.q = Fraction(p_num, p_den)
        self.q_inv = Fraction(p_den, p_num)
        self.ha = self.q - self.q_inv
        # Convention-D Markov parameter z = q^3/(q^2+1), exact in Q for
        # rational q (owner rulings 2026-08-15 and 2026-11-15: replace the
        # convention-C value with convention D).  Previously the rounded
        # convention-C z = 4993/10000 (~ sqrt(q)/(q+1)).
        self.z = self.q ** 3 / (self.q ** 2 + 1)

    def crossing(self, ti, tj):
        """Returns (c, d) where crossing = c σ + d."""
        if ti == 1 and tj == 1:
            return Fraction(1), Fraction(0)
        elif ti == 0 and tj == 0:
            return Fraction(1), -self.ha
        else:
            return Fraction(1), -self.ha / 2

    def traced_volume(self, gen_idx, ordering):
        """V̂_i = z·M₁₀ + M₁₁ via 2×2 transfer matrix product (exact rational).

        M = ∏ T(c,d) where T(c,d) = [[c·HA+d, c], [c, d]].
        Initial state [a,b] = [0,1], so [aₙ,bₙ] = [0,1]×M = (M₁₀, M₁₁).
        V̂ = z·aₙ + bₙ = z·M₁₀ + M₁₁.
        """
        M00 = Fraction(1); M01 = Fraction(0)
        M10 = Fraction(0); M11 = Fraction(1)
        A = len(ordering)
        for j in range(gen_idx + 1, A):
            c, d = self.crossing(ordering[gen_idx], ordering[j])
            t00 = c * self.ha + d; t01 = c
            t10 = c;               t11 = d
            n00 = M00*t00 + M01*t10; n01 = M00*t01 + M01*t11
            n10 = M10*t00 + M11*t10; n11 = M10*t01 + M11*t11
            M00, M01, M10, M11 = n00, n01, n10, n11
        return self.z * M10 + M11

    def traced_volumes_all(self, ordering):
        """All traced volumes [V̂_0, ..., V̂_{A-2}] in one right-to-left sweep.

        Same exact rationals as ``traced_volume(i, ordering)`` for every i,
        but O(A) matrix products instead of O(A^2). The transfer matrix
        T(c,d) depends only on the pair of strand types, so for each
        type t the suffix product R_t(i) = T(t,t_{i+1})...T(t,t_{A-1})
        obeys R_t(i-1) = T(t,t_i)·R_t(i). Row i uses R_{t_i}(i).
        """
        A = len(ordering)
        one, zero = Fraction(1), Fraction(0)
        # suffix products for each strand type: [M00, M01, M10, M11]
        R = {t: [one, zero, zero, one] for t in set(ordering)}
        out = [None] * max(A - 1, 0)
        for i in range(A - 2, -1, -1):
            tj = ordering[i + 1]
            for t, (M00, M01, M10, M11) in R.items():
                c, d = self.crossing(t, tj)
                t00 = c * self.ha + d; t01 = c
                t10 = c;               t11 = d
                # left-multiply: T · M
                R[t] = [t00*M00 + t01*M10, t00*M01 + t01*M11,
                        t10*M00 + t11*M10, t10*M01 + t11*M11]
            M = R[ordering[i]]
            out[i] = self.z * M[2] + M[3]
        return out

    def markov_trace(self, ordering):
        """Product of traced volumes (exact rational)."""
        A = len(ordering)
        product = Fraction(1)
        for i in range(A - 1):
            v = self.traced_volume(i, ordering)
            product *= v
        return product

    def eIeR(self, ordering_par, ordering_dau, conv_pos):
        """Fractional ideal volume at converting position."""
        Vp = self.traced_volume(conv_pos, ordering_par)
        Vd = self.traced_volume(conv_pos, ordering_dau)
        if Vp == 0:
            return Fraction(0)
        fiv = (Vp - Vd) / Vp
        return abs(fiv)

    # ── Wedderburn channels (CANONICAL per paper) ─────────────
    # Reference: wedderburn-mass-formula.md, tower-binding-energy.md
    #   V̂_i^full = w_sym·λ_i^sym + w_std·V_i^std + w_alt·λ_i^alt
    # where w_λ = dim_q(λ)² / ([2]² + 2), exactly summing to 1.
    #
    # ALL OBSERVABLES from H_3(q) MUST use V̂_i^full (not per-channel).

    def _channel_weights(self):
        """Wedderburn-Artin weights (w_sym, w_std, w_alt), sum=1 exactly."""
        # [2]² = (q + 1/q)² = q² + 2 + 1/q²
        n2_sq = self.q ** 2 + 2 + self.q_inv ** 2
        denom = n2_sq + 2  # ([2]² + 2) = sum dim²
        w_sym = Fraction(1) / denom
        w_std = n2_sq / denom
        w_alt = Fraction(1) / denom
        return w_sym, w_std, w_alt

    def lambda_sym(self, gen_idx, ordering):
        """Symmetric channel eigenvalue: λ_sym = ∏_{j>i} (c·q + d)."""
        prod = Fraction(1)
        A = len(ordering)
        for j in range(gen_idx + 1, A):
            c, d = self.crossing(ordering[gen_idx], ordering[j])
            prod *= c * self.q + d
        return prod

    def lambda_alt(self, gen_idx, ordering):
        """Alternating channel eigenvalue: λ_alt = ∏_{j>i} (-c/q + d)."""
        prod = Fraction(1)
        A = len(ordering)
        for j in range(gen_idx + 1, A):
            c, d = self.crossing(ordering[gen_idx], ordering[j])
            prod *= -c * self.q_inv + d
        return prod

    def V_full(self, gen_idx, ordering):
        """Wedderburn-weighted full traced volume per paper.

        V̂_i^full = w_sym·λ_sym + w_std·V_std + w_alt·λ_alt
        """
        w_sym, w_std, w_alt = self._channel_weights()
        lam_sym = self.lambda_sym(gen_idx, ordering)
        lam_alt = self.lambda_alt(gen_idx, ordering)
        v_std = self.traced_volume(gen_idx, ordering)
        return w_sym * lam_sym + w_std * v_std + w_alt * lam_alt

    def V_full_all(self, ordering):
        """All per-generator V̂_i^full for an ordering."""
        return [self.V_full(i, ordering) for i in range(len(ordering) - 1)]


# ── Result dataclass ─────────────────────────────────────────────

@dataclass
class HeckeResult:
    nucleus: str
    p: int
    n: int
    A: int
    ordering_par: list
    ordering_dau: list
    ordering_method: str  # "exact" or "heuristic"
    conv_pos: int
    k_crossings: int  # crossings at converting generator
    trace_par: str  # exact rational as string
    trace_par_float: float
    trace_dau: str
    trace_dau_float: float
    eIeR: str  # exact rational
    eIeR_float: float
    Q_exp: Optional[float] = None
    generator_volumes_par: list = field(default_factory=list)
    generator_volumes_dau: list = field(default_factory=list)
    elapsed_s: float = 0.0


# ── Engine ───────────────────────────────────────────────────────

class HeckeEngine:
    def __init__(self, q_num=111, q_den=100):
        self.qr = HeckeRational(q_num, q_den)

    def ground_state_ordering(self, p, n, max_orderings=5000):
        """Find minimum-energy ordering."""
        A = p + n
        total = math.comb(A, p)

        if total <= max_orderings:
            best_energy = None
            best_ordering = None
            for positions in combinations(range(A), p):
                ordering = [0] * A
                for pos in positions:
                    ordering[pos] = 1
                energy = sum(
                    float(self.qr.traced_volume(i, ordering))
                    for i in range(A - 1)
                )
                if best_energy is None or energy < best_energy:
                    best_energy = energy
                    best_ordering = ordering
            return best_ordering, "exact"
        else:
            # Heuristic: alternating, extra neutrons at end
            ordering = []
            pi, ni = 0, 0
            for k in range(A):
                if pi < p and (ni >= n or k % 2 == 0):
                    ordering.append(1)
                    pi += 1
                else:
                    ordering.append(0)
                    ni += 1
            return ordering, "heuristic"

    def find_converting_position(self, ordering_par, ordering_dau):
        """First position where parent=neutron, daughter=proton."""
        for k in range(len(ordering_par)):
            if ordering_par[k] == 0 and ordering_dau[k] == 1:
                return k
        return -1

    def compute(self, p, n, Q_exp=None):
        """Full computation for N(p,n)."""
        t0 = time.time()
        A = p + n

        # Ground state orderings
        ord_par, method = self.ground_state_ordering(p, n)
        ord_dau, _ = self.ground_state_ordering(p + 1, n - 1)

        # Converting position
        conv = self.find_converting_position(ord_par, ord_dau)
        k = A - conv - 1 if conv >= 0 else 0

        # Markov traces — use log for heavy nuclei to avoid overflow
        if A <= 20:
            tr_par = self.qr.markov_trace(ord_par)
            tr_dau = self.qr.markov_trace(ord_dau)
            tr_par_str = str(tr_par)
            tr_dau_str = str(tr_dau)
            tr_par_f = float(tr_par)
            tr_dau_f = float(tr_dau)
        else:
            # Log trace (sum of log|V̂_i|) to avoid overflow
            tr_par_str = "overflow:use_log"
            tr_dau_str = "overflow:use_log"
            log_par = sum(mp.log(abs(float(self.qr.traced_volume(i, ord_par))))
                         for i in range(A - 1))
            log_dau = sum(mp.log(abs(float(self.qr.traced_volume(i, ord_dau))))
                         for i in range(A - 1))
            tr_par_f = log_par  # store log instead of value
            tr_dau_f = log_dau

        # e(I)/e(R) at converting generator (always exact rational)
        eIeR = self.qr.eIeR(ord_par, ord_dau, conv) if conv >= 0 else Fraction(0)

        # Generator volumes (first 20 + last 5, skip middle for large A)
        if A <= 30:
            gen_vols_par = [str(self.qr.traced_volume(i, ord_par)) for i in range(A - 1)]
            gen_vols_dau = [str(self.qr.traced_volume(i, ord_dau)) for i in range(A - 1)]
        else:
            gen_vols_par = ["truncated"]
            gen_vols_dau = ["truncated"]

        elapsed = time.time() - t0

        # Element symbol
        symbols = {
            (1,0): "H", (1,1): "²H", (1,2): "³H", (2,1): "³He", (2,2): "⁴He",
            (3,3): "⁶Li", (6,6): "¹²C", (6,8): "¹⁴C", (7,7): "¹⁴N",
            (27,33): "⁶⁰Co", (38,52): "⁹⁰Sr", (55,82): "¹³⁷Cs", (83,127): "²¹⁰Bi",
        }
        name = symbols.get((p, n), f"N({p},{n})")

        return HeckeResult(
            nucleus=name, p=p, n=n, A=A,
            ordering_par=ord_par, ordering_dau=ord_dau,
            ordering_method=method,
            conv_pos=conv + 1,  # 1-indexed for Singular compatibility
            k_crossings=k,
            trace_par=tr_par_str, trace_par_float=tr_par_f,
            trace_dau=tr_dau_str, trace_dau_float=tr_dau_f,
            eIeR=str(eIeR), eIeR_float=float(eIeR),
            Q_exp=Q_exp,
            generator_volumes_par=gen_vols_par,
            generator_volumes_dau=gen_vols_dau,
            elapsed_s=elapsed,
        )


# ── CLI ──────────────────────────────────────────────────────────

VERIFICATION_NUCLEI = [
    (1, 2, 0.01861),
    (6, 8, 0.156),
    (27, 33, 0.318),
    (38, 52, 0.546),
    (55, 82, 0.514),
    (83, 127, 1.163),
]


def main():
    engine = HeckeEngine()

    if len(sys.argv) > 1 and sys.argv[1] == "--all":
        nuclei = VERIFICATION_NUCLEI
    elif len(sys.argv) >= 3:
        p, n = int(sys.argv[1]), int(sys.argv[2])
        Q_exp = float(sys.argv[3]) if len(sys.argv) > 3 else None
        nuclei = [(p, n, Q_exp)]
    else:
        print("Usage: python3 -m folio_assistant.computations.hecke_engine P N [Q_exp]")
        print("       python3 -m folio_assistant.computations.hecke_engine --all")
        sys.exit(1)

    results = []
    for p, n, *rest in nuclei:
        Q_exp = rest[0] if rest else None
        r = engine.compute(p, n, Q_exp)
        results.append(r)

        print(f"{r.nucleus}: N({r.p},{r.n}), A={r.A}, conv={r.conv_pos}, k={r.k_crossings}")
        print(f"  tr(par) = {r.trace_par_float:+.8e}")
        print(f"  tr(dau) = {r.trace_dau_float:+.8e}")
        print(f"  e(I)/e(R) = {r.eIeR_float:.10f} [{r.eIeR}]")
        if r.Q_exp:
            print(f"  Q_exp = {r.Q_exp:.5f}")
        print(f"  ordering: {''.join('●' if x else '○' for x in r.ordering_par)}")
        print(f"  method: {r.ordering_method}, time: {r.elapsed_s:.2f}s")
        print()

    # Summary table
    if len(results) > 1:
        print("=" * 70)
        print(f"{'Nuc':>8} | {'e(I)/e(R)':>12} | {'Q_exp':>8} | {'k':>3} | {'conv':>4} | {'time':>6}")
        print("-" * 70)
        for r in results:
            Q_str = f"{r.Q_exp:.5f}" if r.Q_exp else "—"
            print(f"{r.nucleus:>8} | {r.eIeR_float:12.6f} | {Q_str:>8} | {r.k_crossings:3d} | {r.conv_pos:4d} | {r.elapsed_s:5.2f}s")

    # Write witness if --witness flag
    if "--witness" in sys.argv:
        witness = {
            "computation": "hecke-engine",
            "q": "111/100",
            "z": str(HeckeRational().z),
            "results": [asdict(r) for r in results],
        }
        out = Path(_HERE_W.parent / "hecke-engine.witness.json")
        with open(out, "w") as f:
            # Provenance stamp (bean qou-4un2): this producer writes its
            # witness directly, so nothing else records which script made
            # it -- and a re-run of an unstamped producer DELETES the
            # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
            import os as _os  # noqa: E402 -- provenance stamp
            from qou_substrate.witness import WitnessBuilder as _WB
            witness.setdefault("scriptFile", _os.path.basename(__file__))
            _WB.stamp_staleness_metadata(
                witness, script_path=__file__, engine=None, q0_anchor=False)
            json.dump(witness, f, indent=2)
        print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()
