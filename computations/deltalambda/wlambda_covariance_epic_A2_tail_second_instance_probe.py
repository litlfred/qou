"""A2 (TAIL) second instance: carrier reduction + sign ONSET for nu_{n-1}
(epic qou-x631, attack qou-ogrk).

DERIVED CARRIER CLASSIFICATION for hook length v = n-1 (n cells):
  - two-corner shapes lambda = (a, 2, 1^c), a >= 2, a + c = n - 2:
    carrier (0,0), multiplicity 1
    [f = n! / ((n-1) a (c+2) (a-2)! c!), omega3 = Q(a-1) + Q(c+1) - C(n,2)]
  - the row (n): carrier (0,1);  the column (1^n): carrier (1,0)
    [f = 1, omega3 = Q(n-1) - C(n,2), transpose-equal]
  No other carriers (any other cell's hook excludes >= 2 cells). Verified
  exhaustively n <= 25; the reduction formula matches full enumeration in
  exact Fractions.

SIGN ONSET (the honest refinement of (TAIL)):
  nu_{n-1} == 0 at n = 4; NEGATIVE for n = 5, 6, 7; positive for n >= 8
  (verified <= 25). So per-depth-j tail positivity nu_{n-j} > 0 holds only
  past an onset n_j (n_0 = 4 from the nu_n closed form, n_1 = 8 here) — the
  (TAIL) constant is genuinely > 2 and the conjecture must carry per-n
  thresholds, as the nu-sign-structure witness records (T(n)/n <= 0.72
  observed). Nothing here contradicts recorded data; it sharpens the
  statement a proof must target.
"""
import json
import math
import sys
import time
from fractions import Fraction

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent

N_MAX = 25


def partitions(n, maxp=None):
    if maxp is None:
        maxp = n
    if n == 0:
        yield []
        return
    for i in range(min(n, maxp), 0, -1):
        for r in partitions(n - i, i):
            yield [i] + r


def conj(l):
    return [sum(1 for x in l if x > j) for j in range(l[0])] if l else []


def hooks_cells(l):
    c = conj(l)
    out = []
    for i, li in enumerate(l):
        for j in range(li):
            out.append(((i, j), li + c[j] - j - i - 1))
    return out


def Q(m):
    return m * (m + 1) * (2 * m + 1) // 6


def main():
    t0 = time.time()
    rows = []
    all_ok = True
    for n in range(4, N_MAX + 1):
        fact = math.factorial(n)
        C2 = n * (n - 1) // 2
        nu_full = Fraction(0)
        carriers_ok = True
        for lam in partitions(n):
            hc = hooks_cells(lam)
            p = 1
            for _, h in hc:
                p *= h
            f = fact // p
            w = Fraction(f * f, fact)
            om = sum((j - i) ** 2 for i, li in enumerate(lam)
                     for j in range(li)) - C2
            cells_v = [cell for cell, h in hc if h == n - 1]
            if cells_v:
                is_2c = (len(lam) >= 2 and lam[1] == 2
                         and all(x == 1 for x in lam[2:]) and lam[0] >= 2)
                is_row = lam == [n]
                is_col = lam == [1] * n
                ok = ((is_2c and cells_v == [(0, 0)])
                      or (is_row and cells_v == [(0, 1)])
                      or (is_col and cells_v == [(1, 0)]))
                if not ok:
                    carriers_ok = False
            nu_full += w * len(cells_v) * om
        nu_red = Fraction(0)
        for a in range(2, n - 1):
            c = n - 2 - a
            f = fact // ((n - 1) * a * (c + 2)
                         * math.factorial(a - 2) * math.factorial(c))
            nu_red += Fraction(f * f, fact) * (Q(a - 1) + Q(c + 1) - C2)
        nu_red += Fraction(2, fact) * (Q(n - 1) - C2)
        ok = carriers_ok and (nu_full == nu_red)
        all_ok = all_ok and ok
        rows.append({"n": n, "carriers_ok": carriers_ok,
                     "reduction_match": nu_full == nu_red,
                     "nu_nm1": str(nu_full),
                     "sign": "0" if nu_full == 0 else ("+" if nu_full > 0 else "-")})
        print(f"n={n:3d} carriers_ok={carriers_ok} match={nu_full == nu_red} "
              f"sign={'0' if nu_full == 0 else ('+' if nu_full > 0 else '-')}",
              flush=True)
    signs = {r["n"]: r["sign"] for r in rows}
    onset_ok = (signs[4] == "0" and all(signs[n] == "-" for n in (5, 6, 7))
                and all(signs[n] == "+" for n in range(8, N_MAX + 1)))
    verdict = {
        "all_structural_checks_pass": all_ok,
        "sign_onset": {"zero_at": 4, "negative_at": [5, 6, 7],
                       "positive_from": 8, "onset_pattern_confirmed": onset_ok},
        "interpretation": (
            "Carrier reduction for nu_{n-1} DERIVED and exact-verified. Sign has "
            "an ONSET: negative n = 5..7, positive n >= 8 — refining (TAIL): "
            "per-depth-j positivity nu_{n-j} > 0 holds past an onset n_j "
            "(n_0 = 4, n_1 = 8); the (TAIL) constant is > 2 and per-n "
            "thresholds are required, as the sign-structure witness records."),
    }
    out = {
        "description": "A2 (TAIL) second instance: nu_{n-1} carrier reduction "
                       "(derived, exact) + sign onset n_1 = 8.",
        "epic": "qou-x631", "attack": "qou-ogrk (A2), TAIL sub-target",
        "verdict": verdict, "per_n": rows, "runtime_s": f"{time.time() - t0:.3f}",
    }
    path = (_HERE_W / "wlambda-covariance-epic-A2-tail-second-instance.witness.json")
    with open(path, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        import os as _os  # noqa: E402 -- provenance stamp
        from qou_substrate.witness import WitnessBuilder as _WB
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(out, fh, indent=1, default=str)
    print(f"\nall_ok={all_ok} onset_ok={onset_ok}  witness -> {path} "
          f"({time.time()-t0:.1f}s)")
    return 0 if (all_ok and onset_ok) else 1


if __name__ == "__main__":
    sys.exit(main())
