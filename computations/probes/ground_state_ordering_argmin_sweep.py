#!/usr/bin/env python3
"""Exhaustive Φ_q argmin sweep over nucleon arrangements — the truth-value
probe for ``prop:ground-state-ordering`` (bean ``qou-48is``).

The proposition asserts that the nuclear ground state is the arrangement
**minimising** ``Φ_q = Σ_i log|V̂_i|``, and that this minimiser is

  (A ≥ 4)  interleaved + tail-packed, and
  (A ≤ 3)  sorted (all protons first).

This probe decides both clauses by **exhaustive** enumeration of every
``C(A, Z)`` arrangement, at the experimental (proton) ``q₀`` pin, for
**both** readouts:

  Φ_nuc : the bare nucleon chain (no electrons)
  Φ₁    : the nucleon chain with the ``["e"] * Z`` tail appended — what
          ``hecke_core_symbolic.compute_phi1_full_sym`` actually calls.

Fast path
---------
``_phi1_from_ordering_sym`` is sympy-symbolic and costs ~seconds per
arrangement, which is unaffordable over ``C(14, 7) = 3432`` arrangements.
This probe therefore uses an **exactly equivalent** mpmath closed form,
derived from the corpus implementation and cross-checked against it:

The corpus transfer factor is ``T(d) = [[h+d, 1], [1, d]] = S + d·I`` with
``S = [[h, 1], [1, 0]]``.  All ``T(d)`` are polynomials in the single matrix
``S``, hence **commute** (cf. the sorry-free
``QOU.MassTheory.TransferFactorCommute``), so ``M_i = Π_{j>i} T(d_ij)``
depends on the crossing coefficients only as a **multiset**.  ``S`` has
``tr S = h = q − q⁻¹`` and ``det S = −1``, so its eigenvalues are exactly
the Hecke eigenvalues ``λ₊ = q``, ``λ₋ = −q⁻¹`` (whence ``λ₊λ₋ = −1``).
Reducing ``M_i = α I + β S`` via ``S² = hS + I`` gives ``M[1][0] = β``,
``M[1][1] = α``, so the corpus readout ``V̂_i = z·M[1][0] + M[1][1]``
becomes

    V̂_i = [ (z + q⁻¹)·μ₊ + (q − z)·μ₋ ] / (q + q⁻¹),
    μ± = Π_{j>i} (λ± + d_ij).

with ``z = √q/(q+1)``.  The per-``d`` eigenfactors are

    d = 0     (pp, ee)      :  μ₊ ·= q          μ₋ ·= −q⁻¹
    d = −h/2  (pn, np)      :  μ₊ ·= c          μ₋ ·= −c      , c = (q+q⁻¹)/2
    d = −h    (nn, pe, ep)  :  μ₊ ·= q⁻¹        μ₋ ·= −q
    d = None  (ne, en)      :  skipped (identity factor)

Usage
-----
    python3 -u ground_state_ordering_argmin_sweep.py --check     # xcheck only
    python3 -u ground_state_ordering_argmin_sweep.py --max-a 14

Anchor: experimental (proton) ``q₀`` via ``q_parameter.q_at`` — the default
``qou_substrate.constants`` re-export.  No AME/CODATA quantity enters the
arrangement comparison (``free_parameters = 0``): the only physical input is
``q₀`` itself, and the argmin is a pure ordering of ``Φ_q`` values.
"""

from __future__ import annotations

import argparse
import itertools
import json
import math
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))

import mpmath as mp  # noqa: E402

from q_parameter import q_at  # noqa: E402

DPS = 50


# ══════════════════════════════════════════════════════════════════
# Closed-form Φ_q (mpmath, exactly mirrors _phi1_from_ordering_sym)
# ══════════════════════════════════════════════════════════════════

class Kernel:
    """Per-``q₀`` cached eigenfactor table."""

    def __init__(self, dps: int = DPS) -> None:
        self.dps = dps
        with mp.workdps(dps + 10):
            q = q_at(dps + 10)
            self.q = +q
            self.qi = +(mp.mpf(1) / q)
            self.h = +(q - self.qi)
            self.c = +((q + self.qi) / 2)
            self.z = +(q ** 3 / (q ** 2 + 1))   # convention D (was C: sqrt(q)/(q+1))
            self.two_q = +(q + self.qi)
            # readout coefficients
            self.cp = +((self.z + self.qi) / self.two_q)   # weight on μ₊
            self.cm = +((q - self.z) / self.two_q)         # weight on μ₋

    def factors(self, ti: str, tj: str):
        """(λ₊-factor, λ₋-factor) for the crossing (ti, tj); None = skip.

        Mirrors ``hecke_core_symbolic._crossing_coeff_sym`` case-for-case,
        including the **absent** ``(n, e)`` case (returns ``None``, which the
        corpus silently skips).
        """
        if ti == "p" and tj == "p":
            return (self.q, -self.qi)                 # d = 0
        if ti == "n" and tj == "n":
            return (self.qi, -self.q)                 # d = -h
        if (ti, tj) in (("p", "n"), ("n", "p")):
            return (self.c, -self.c)                  # d = -h/2
        if (ti, tj) in (("p", "e"), ("e", "p")):
            return (self.qi, -self.q)                 # d = -h
        if ti == "e" and tj == "e":
            return (self.q, -self.qi)                 # d = 0
        return None                                    # (n, e) / (e, n)


def phi_from_ordering(ordering, K: Kernel) -> mp.mpf:
    """Φ_q of a strand ordering — closed form, exact mirror of the corpus."""
    n = len(ordering)
    if n <= 1:
        return mp.mpf(0)
    tol = mp.mpf(f"1e-{K.dps - 5}")
    phi = mp.mpf(0)
    with mp.workdps(K.dps + 10):
        for i in range(n - 1):
            mu_p = mp.mpf(1)
            mu_m = mp.mpf(1)
            ti = ordering[i]
            for j in range(i + 1, n):
                f = K.factors(ti, ordering[j])
                if f is None:
                    continue
                mu_p *= f[0]
                mu_m *= f[1]
            V = K.cp * mu_p + K.cm * mu_m
            if abs(V) > tol:
                phi += mp.log(abs(V))
    return +phi


# ══════════════════════════════════════════════════════════════════
# Reference orderings
# ══════════════════════════════════════════════════════════════════

def sorted_ordering(Z: int, N: int):
    return ["p"] * Z + ["n"] * N


def interleaved_tailpacked(Z: int, N: int):
    """The proposition's own rule (i) + (ii), literally.

    ``ordering[k] = 1 (proton) iff k odd and k < 2Z``; excess neutrons
    tail-packed at ``2Z .. A-1``.  NOTE: the .md prose says "neutrons at
    even, protons at odd" while the displayed formula says protons at odd
    — the same thing.  Only defined for ``Z ≤ N``.
    """
    A = Z + N
    return ["p" if (k % 2 == 1 and k < 2 * Z) else "n" for k in range(A)]


def corpus_ground_state(Z: int, N: int):
    """``hecke_core_symbolic._ground_state_ordering`` — protons at EVEN."""
    A = Z + N
    out, pc, nc = [], 0, 0
    for k in range(A):
        if (k % 2 == 0 and pc < Z) or nc >= N:
            out.append("p")
            pc += 1
        else:
            out.append("n")
            nc += 1
    return out


def corpus_alternating(Z: int, N: int):
    """``hecke_core_symbolic._alternating_ordering_sym``."""
    out, pi, ni = [], 0, 0
    for k in range(Z + N):
        if pi < Z and (ni >= N or k % 2 == 0):
            out.append("p")
            pi += 1
        else:
            out.append("n")
            ni += 1
    return out


def all_arrangements(Z: int, N: int):
    A = Z + N
    for pos in itertools.combinations(range(A), Z):
        s = set(pos)
        yield ["p" if k in s else "n" for k in range(A)]


# ══════════════════════════════════════════════════════════════════
# Cross-check against the corpus symbolic implementation
# ══════════════════════════════════════════════════════════════════

def cross_check(K: Kernel, verbose: bool = True) -> dict:
    """Assert the closed form reproduces ``_phi1_from_ordering_sym`` exactly."""
    from hecke_core_symbolic import _phi1_from_ordering_sym  # noqa: E402

    cases = [
        ["p", "n"],
        ["p", "p", "n"],
        ["p", "n", "p"],
        ["n", "p", "n"],
        ["p", "n", "p", "n"],
        ["p", "p", "n", "n"],
        ["n", "n", "p", "p"],
        ["p", "n", "n", "p", "n"],
        # with the electron tail (exercises the (n,e) skip)
        ["p", "n", "e"],
        ["p", "n", "p", "n", "e", "e"],
        ["n", "p", "n", "p", "n", "e", "e"],
    ]
    rows = []
    worst = mp.mpf(0)
    for c in cases:
        a = phi_from_ordering(c, K)
        b = _phi1_from_ordering_sym(c, dps=K.dps)
        d = abs(a - b)
        rel = d / max(abs(b), mp.mpf(1))
        worst = max(worst, rel)
        rows.append({"ordering": "".join(c), "closed_form": mp.nstr(a, 20),
                     "corpus": mp.nstr(b, 20), "rel_diff": mp.nstr(rel, 6)})
        if verbose:
            print(f"  {''.join(c):<10} closed={mp.nstr(a, 18):<24} "
                  f"corpus={mp.nstr(b, 18):<24} rel={mp.nstr(rel, 4)}")
    ok = worst < mp.mpf("1e-40")
    if verbose:
        print(f"  worst relative difference: {mp.nstr(worst, 6)}  "
              f"[{'PASS' if ok else 'FAIL'}]")
    return {"passed": bool(ok), "worst_rel_diff": mp.nstr(worst, 6), "cases": rows}


# ══════════════════════════════════════════════════════════════════
# Sweep
# ══════════════════════════════════════════════════════════════════

def describe(ordering) -> str:
    return "".join(ordering)


def sweep_one(Z: int, N: int, K: Kernel, readout: str) -> dict:
    """Exhaustive argmin over all C(A,Z) arrangements for one (Z, N)."""
    A = Z + N
    tail = ["e"] * Z if readout == "phi1" else []
    best_val = None
    best = []
    worst_val = None
    worst = []
    vals = {}
    for arr in all_arrangements(Z, N):
        v = phi_from_ordering(list(arr) + tail, K)
        vals[describe(arr)] = v
        if best_val is None or v < best_val - mp.mpf("1e-40"):
            best_val, best = v, [describe(arr)]
        elif abs(v - best_val) <= mp.mpf("1e-40"):
            best.append(describe(arr))
        if worst_val is None or v > worst_val + mp.mpf("1e-40"):
            worst_val, worst = v, [describe(arr)]
        elif abs(v - worst_val) <= mp.mpf("1e-40"):
            worst.append(describe(arr))

    refs = {
        "sorted": sorted_ordering(Z, N),
        "prop_interleaved_tailpacked": interleaved_tailpacked(Z, N),
        "corpus_ground_state": corpus_ground_state(Z, N),
        "corpus_alternating": corpus_alternating(Z, N),
    }
    ranked = sorted(vals.items(), key=lambda kv: kv[1])
    rank_of = {k: i for i, (k, _) in enumerate(ranked)}
    n_arr = len(vals)

    ref_rows = {}
    for name, o in refs.items():
        key = describe(o)
        ref_rows[name] = {
            "ordering": key,
            "phi": mp.nstr(vals[key], 20),
            "rank": rank_of[key] + 1,
            "n_arrangements": n_arr,
            "is_argmin": key in best,
            "is_argmax": key in worst,
        }

    return {
        "Z": Z, "N": N, "A": A, "readout": readout,
        "n_arrangements": n_arr,
        "argmin": best,
        "argmin_phi": mp.nstr(best_val, 20),
        "argmax": worst,
        "argmax_phi": mp.nstr(worst_val, 20),
        "references": ref_rows,
        "top3": [{"ordering": k, "phi": mp.nstr(v, 20)} for k, v in ranked[:3]],
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-a", type=int, default=14)
    ap.add_argument("--check", action="store_true", help="cross-check only")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    mp.mp.dps = DPS + 10
    K = Kernel(DPS)
    print(f"q₀ (experimental/proton pin) = {mp.nstr(K.q, 25)}")
    print("Cross-checking the closed form against "
          "hecke_core_symbolic._phi1_from_ordering_sym …")
    xc = cross_check(K)
    if not xc["passed"]:
        print("CROSS-CHECK FAILED — aborting.", file=sys.stderr)
        return 1
    if args.check:
        return 0

    cases = []
    for A in range(2, args.max_a + 1):
        for Z in range(1, A // 2 + 1):      # Z ≤ N per the proposition
            N = A - Z
            cases.append((Z, N))

    t0 = time.time()
    results = []
    total = len(cases) * 2
    done = 0
    for readout in ("phi_nuc", "phi1"):
        for (Z, N) in cases:
            r = sweep_one(Z, N, K, readout)
            results.append(r)
            done += 1
            el = time.time() - t0
            eta = el / done * (total - done)
            print(f"[{done}/{total}] {readout:<8} Z={Z} N={N} A={Z+N} "
                  f"({r['n_arrangements']} arr)  argmin={r['argmin'][0]}  "
                  f"prop_rank={r['references']['prop_interleaved_tailpacked']['rank']}"
                  f"/{r['n_arrangements']}  sorted_rank="
                  f"{r['references']['sorted']['rank']}"
                  f"  [{el:.0f}s elapsed, ETA {eta:.0f}s]", flush=True)

    # ── verdict tallies ────────────────────────────────────────────
    def tally(readout, pred):
        rows = [r for r in results if r["readout"] == readout and pred(r)]
        out = {}
        for name in ("sorted", "prop_interleaved_tailpacked",
                     "corpus_ground_state", "corpus_alternating"):
            hit = sum(1 for r in rows if r["references"][name]["is_argmin"])
            mx = sum(1 for r in rows if r["references"][name]["is_argmax"])
            out[name] = {"argmin_hits": hit, "argmax_hits": mx, "cases": len(rows)}
        return out

    verdict = {
        "A_le_3": {ro: tally(ro, lambda r: r["A"] <= 3) for ro in ("phi_nuc", "phi1")},
        "A_ge_4": {ro: tally(ro, lambda r: r["A"] >= 4) for ro in ("phi_nuc", "phi1")},
    }

    print("\n" + "=" * 70)
    print("VERDICT TALLY (argmin hits / cases)")
    print("=" * 70)
    for clause in ("A_le_3", "A_ge_4"):
        for ro in ("phi_nuc", "phi1"):
            print(f"\n{clause}  readout={ro}")
            for name, v in verdict[clause][ro].items():
                print(f"   {name:<32} argmin {v['argmin_hits']}/{v['cases']}"
                      f"   argmax {v['argmax_hits']}/{v['cases']}")

    out = {
        "probe": "ground_state_ordering_argmin_sweep",
        "bean": "qou-48is",
        "block": "prop:ground-state-ordering",
        "q0_anchor": "experimental (proton) — q_parameter.q_at",
        "q0": mp.nstr(K.q, 25),
        "dps": DPS,
        "readouts": ["phi_nuc (bare nucleon chain)",
                     "phi1 (nucleon chain + ['e']*Z tail)"],
        "cross_check_vs_corpus": xc,
        "max_A": args.max_a,
        "verdict_tally": verdict,
        "results": results,
        # wall clock, not a measurement — string so it is not raw float64
        "wall_seconds": f"{time.time() - t0:.1f}",
    }
    path = args.out or str(Path(__file__).resolve().parent.parent /
                           "ground-state-ordering-argmin-sweep.witness.json")

    # PRESERVE blocks this probe does not produce. The committed witness carries
    # a `lean_bridge` block that NO producer writes — it was added by 7c60b2f38
    # and is cited by
    # docs/audits/2026-08-09-ground-state-ordering-truth-value.md. A plain
    # overwrite DELETED it, which is why this witness could not be regenerated
    # (and so kept its one raw-float64 field on the ratchet indefinitely).
    #
    # Merge rather than clobber: anything already on disk that this run does not
    # compute is carried forward. A producer that silently drops published data
    # is worse than a stale field.
    existing = {}
    try:
        existing = json.loads(Path(path).read_text())
    except (OSError, ValueError):
        pass
    carried = [k for k in existing if k not in out]
    for k in carried:
        out[k] = existing[k]
    if carried:
        print(f"  carried forward {len(carried)} block(s) this probe does not "
              f"produce: {', '.join(sorted(carried))}")

    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    out.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        out, script_path=__file__, engine=None, q0_anchor=None)
    Path(path).write_text(json.dumps(out, indent=2) + "\n")
    print(f"\nwrote {path}  ({out['wall_seconds']}s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
