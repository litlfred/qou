#!/usr/bin/env python3
"""
Hecke trace engine — general-purpose computation for any N(p,n).

Computes the Gröbner-reduced Hecke representation of any nucleus:
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

import json
import math
import sys
import time

sys.set_int_max_str_digits(100000)
from dataclasses import dataclass, field, asdict
from fractions import Fraction
from itertools import combinations
from pathlib import Path
from typing import Optional


# ── Exact rational arithmetic ────────────────────────────────────

class QRat:
    """Rational arithmetic with q = p_num/p_den."""
    def __init__(self, p_num=111, p_den=100):
        self.q = Fraction(p_num, p_den)
        self.q_inv = Fraction(p_den, p_num)
        self.ha = self.q - self.q_inv
        # z = 1/(q^{1/2} + q^{-1/2}) — approximate as rational
        # For exact: z = 4993/10000 at q=111/100
        # Better: use the exact value from q^{1/2} ≈ 1053/1000
        self.z = Fraction(4993, 10000)

    def crossing(self, ti, tj):
        """Returns (c, d) where crossing = c σ + d."""
        if ti == 1 and tj == 1:
            return Fraction(1), Fraction(0)
        elif ti == 0 and tj == 0:
            return Fraction(1), -self.ha
        else:
            return Fraction(1), -self.ha / 2

    def chain_reduce(self, gen_idx, ordering):
        """Reduce the chain at generator gen_idx to (a, b)."""
        a = Fraction(0)
        b = Fraction(1)
        A = len(ordering)
        for j in range(gen_idx + 1, A):
            c, d = self.crossing(ordering[gen_idx], ordering[j])
            new_a = a * c * self.ha + a * d + b * c
            new_b = a * c + b * d
            a, b = new_a, new_b
        return a, b

    def traced_volume(self, gen_idx, ordering):
        """V̂_i = z·a_i + b_i (exact rational)."""
        a, b = self.chain_reduce(gen_idx, ordering)
        return self.z * a + b

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
        self.qr = QRat(q_num, q_den)

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
            log_par = sum(math.log(abs(float(self.qr.traced_volume(i, ord_par))))
                         for i in range(A - 1))
            log_dau = sum(math.log(abs(float(self.qr.traced_volume(i, ord_dau))))
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
            "z": "4993/10000",
            "results": [asdict(r) for r in results],
        }
        out = Path("folio-assistant/computations/hecke-engine.witness.json")
        with open(out, "w") as f:
            json.dump(witness, f, indent=2)
        print(f"\nWitness: {out}")


if __name__ == "__main__":
    main()
