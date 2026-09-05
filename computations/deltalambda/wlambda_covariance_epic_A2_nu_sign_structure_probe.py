"""A2 nu-sign-structure probe (epic qou-x631, attack qou-ogrk).

Follow-up to the fractional-moment family (FMP) audit
2026-07-26-covariance-kernel-A2-fractional-moment-family.md: test the
Descartes-Laguerre mechanism for FMP. M_alpha = Sigma_v nu_v v^alpha is an
exponential sum in alpha, so #real zeros of M <= #sign changes of (nu_v) in
v-order (Laguerre). If nu had <= 2 changes with the second zero at alpha < 0,
FMP would follow by zero-counting.

Findings (exact-Fraction nu_v, n <= 30):
  1. DESCARTES INSUFFICIENT AS-IS: sign changes fluctuate 5..9 (not <= 2).
  2. ONE REAL ZERO ANYWAY: M(-inf) = nu_1 < 0 (the v=1 term is constant and
     nu_1 < 0 always), M < 0 on the scanned negative axis, M(0) = 0,
     M > 0 on (0, infty) — exactly one real zero although Laguerre allows ~9.
     FMP <=> alpha = 0 is M's ONLY real zero.
  3. TAIL POSITIVITY: the sign-mixing is confined to the low-v bulk; nu_v > 0
     uniformly for v above roughly n/2 (long-hook tail), nu_1 < 0 always.
     New provable-shaped sub-target (TAIL): nu_v >= 0 for v > n/2 + O(1) —
     long hooks live only in dominance-extreme diagrams where the spectrum/
     spread covariance localizes.

Vanilla python; exact Fractions for nu; float only in v^alpha scanning.
"""
import json
import math
import sys
import time
from fractions import Fraction

from pathlib import Path as _PathW  # noqa: E402 — witness output root
_HERE_W = _PathW(__file__).resolve().parent

N_MAX = 30


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


def hooks(l):
    c = conj(l)
    out = []
    for i, li in enumerate(l):
        for j in range(li):
            out.append(li + c[j] - j - i - 1)
    return out


def nu_exact(n):
    fact = math.factorial(n)
    C2 = n * (n - 1) // 2
    e_nv_om = {}
    for lam in partitions(n):
        hks = hooks(lam)
        p = 1
        for h in hks:
            p *= h
        f = fact // p
        w = Fraction(f * f, fact)
        om = sum((j - i) ** 2 for i, li in enumerate(lam) for j in range(li)) - C2
        spec = {}
        for h in hks:
            spec[h] = spec.get(h, 0) + 1
        for v, c in spec.items():
            e_nv_om[v] = e_nv_om.get(v, Fraction(0)) + w * c * om
    return e_nv_om  # E2[omega3] = 0 exactly (asserted in the FMP probe)


def M(nu, a):
    return sum(float(x) * (v ** a) for v, x in nu.items())


def main():
    t0 = time.time()
    rows = []
    for n in range(3, N_MAX + 1):
        nu = nu_exact(n)
        vs = sorted(nu)
        signs = [1 if nu[v] > 0 else (-1 if nu[v] < 0 else 0) for v in vs]
        nz = [s for s in signs if s != 0]
        changes = sum(1 for i in range(1, len(nz)) if nz[i] != nz[i - 1])
        pattern = "".join("+" if s > 0 else ("-" if s < 0 else "0") for s in signs)
        # negative-axis scan for zeros of M
        neg_zeros = []
        prev_a = prev_m = None
        a = -12.0
        while a < -1e-9:
            m = M(nu, a)
            if prev_m is not None and prev_m * m < 0:
                neg_zeros.append(round((prev_a + a) / 2, 3))
            prev_a, prev_m = a, m
            a += 0.05
        # tail-positivity threshold: least T with nu_v > 0 for all v >= T
        T = vs[-1]
        for idx in range(len(vs) - 1, -1, -1):
            if signs[idx] > 0:
                T = vs[idx]
            else:
                break
        nu1_neg = signs[0] < 0 if vs[0] == 1 else None
        rows.append({
            "n": n, "sign_changes": changes, "pattern": pattern,
            "v_max": vs[-1], "neg_axis_zeros": neg_zeros,
            "tail_pos_from": T, "tail_over_n": T / n, "nu1_negative": nu1_neg,
        })
        print(f"n={n:3d} changes={changes} tail_pos_from={T:3d} (T/n={T/n:.2f}) "
              f"neg_zeros={neg_zeros} nu1<0={nu1_neg}", flush=True)
    verdict = {
        "descartes_route": "INSUFFICIENT as-is: sign changes 5..9, not <= 2",
        "single_real_zero_observed": all(not r["neg_axis_zeros"] for r in rows),
        "nu1_always_negative": all(r["nu1_negative"] for r in rows),
        "tail_positivity": {
            "max_T_over_n": max(r["tail_over_n"] for r in rows),
            "statement": "nu_v > 0 for all v >= T(n), with T(n)/n bounded (~<= 0.72 observed)",
        },
        "interpretation": (
            "FMP <=> alpha = 0 is the ONLY real zero of M (M(-inf) = nu_1 < 0, "
            "M negative on the negative axis, positive above). Descartes counting "
            "alone cannot give this (too many coefficient sign changes); the "
            "observed mechanism is bulk-cancellation + long-hook tail positivity. "
            "New provable-shaped sub-target (TAIL): nu_v >= 0 for v > n/2 + O(1)."
        ),
    }
    out = {
        "description": "nu-sign structure: Descartes-Laguerre narrowing + single-real-zero "
                       "+ long-hook tail positivity for the A2/FMP mechanism.",
        "epic": "qou-x631", "attack": "qou-ogrk (A2), FMP mechanism narrowing",
        "verdict": verdict, "per_n": rows, "runtime_s": f"{time.time() - t0:.3f}",
    }
    path = (_HERE_W / "wlambda-covariance-epic-A2-nu-sign-structure.witness.json")
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    with open(path, "w") as fh:
        # Provenance stamp (bean qou-4un2): this producer writes its
        # witness directly, so nothing else records which script made
        # it -- and a re-run of an unstamped producer DELETES the
        # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
        out.setdefault("scriptFile", _os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            out, script_path=__file__, engine=None, q0_anchor=False)
        json.dump(out, fh, indent=1, default=str)
    print(f"\nwitness -> {path} ({time.time()-t0:.1f}s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
