"""A2 (TAIL) first instance: closed form nu_n (epic qou-x631, attack qou-ogrk).

DERIVATION (verified exactly below, n <= 25):

1. Carrier lemma: a diagram of n cells has a hook of length n iff it is a
   hook shape lambda = (a, 1^{n-a}); the carrier cell is (0,0), multiplicity 1.
   (The (0,0)-hook is row 0 + column 0; length n forces them to exhaust lambda.)
2. f^{(a,1^{n-a})} = C(n-1, a-1); contents are {0..a-1} and {-1..-(n-a)}, so
   omega3 = Q(a-1) + Q(n-a) - C(n,2), Q(m) = m(m+1)(2m+1)/6.
3. E2[omega3] = 0, so nu_n = E2[N_n omega3]
     = (1/n!) Sigma_{k=0}^{m} C(m,k)^2 [Q(k) + Q(m-k) - C(n,2)],  m = n-1.
4. Binomial-square sums via k C(m,k) = m C(m-1,k-1):
     Sigma C(m,k)^2 = C(2m,m);  Sigma k C^2 = (m/2) C(2m,m);
     Sigma k^2 C^2 = m^2 C(2m-2,m-1);
     Sigma k^3 C^2 = m^2 (m+1)/2 C(2m-2,m-1).
   Algebra collapses the bracket to (m-2)(m-1)(m+1)/3 * C(2m-2, m-1):

     >>> nu_n = n (n-2)(n-3) C(2n-4, n-2) / (3 n!)  <<<

   Manifestly >= 0 for n >= 3, > 0 for n >= 4, and ZERO at n = 3 — matching
   the observed nu-pattern "-+0" at n=3 (the nu-sign-structure witness).

This is the first PROVED-shaped instance of (TAIL) [nu_v >= 0 for large v]:
the extreme value v = n, in closed form. Exact verification: carriers,
formula (Fraction equality), and nonnegativity, n <= 25.
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


def main():
    t0 = time.time()
    rows = []
    all_ok = True
    for n in range(3, N_MAX + 1):
        fact = math.factorial(n)
        C2 = n * (n - 1) // 2
        nu_n = Fraction(0)
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
            cells_n = [cell for cell, h in hc if h == n]
            if cells_n:
                is_hook = len(lam) == 1 or all(x == 1 for x in lam[1:])
                if not (is_hook and cells_n == [(0, 0)]):
                    carriers_ok = False
            nu_n += w * len(cells_n) * om
        closed = Fraction(n * (n - 2) * (n - 3) * math.comb(2 * n - 4, n - 2),
                          3 * fact)
        ok = carriers_ok and (nu_n == closed) and (nu_n >= 0)
        all_ok = all_ok and ok
        rows.append({"n": n, "carriers_ok": carriers_ok,
                     "closed_form_match": nu_n == closed,
                     "nu_n": str(nu_n), "nonneg": nu_n >= 0})
        print(f"n={n:3d} carriers_ok={carriers_ok} match={nu_n == closed} "
              f"nonneg={nu_n >= 0}", flush=True)
    verdict = {
        "all_checks_pass": all_ok,
        "closed_form": "nu_n = n (n-2)(n-3) C(2n-4, n-2) / (3 n!)",
        "sign": "== 0 at n = 3; > 0 for n >= 4 (manifest from the formula)",
        "status": ("First (TAIL) instance in closed form: derivation via the "
                   "carrier lemma + binomial-square sums, verified exactly "
                   f"n <= {N_MAX}. Lean formalization queued (carrier lemma is "
                   "list-level combinatorics on the existing cells/hookLen "
                   "machinery; the binomial identity is a finite sum)."),
    }
    out = {
        "description": "A2 (TAIL) first instance: exact closed form for nu_n "
                       "(hook-length-n covariance), derived and verified.",
        "epic": "qou-x631", "attack": "qou-ogrk (A2), TAIL sub-target",
        "verdict": verdict, "per_n": rows, "runtime_s": f"{time.time() - t0:.3f}",
    }
    path = (_HERE_W / "wlambda-covariance-epic-A2-tail-first-instance.witness.json")
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
    print(f"\nall_ok={all_ok}  witness -> {path} ({time.time()-t0:.1f}s)")
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
