#!/usr/bin/env python3

# Path bridge (subdirectory refactor — Phase 2, 2026-06-02).
# Keeps flat-namespace imports (`from witness_base import …`)
# working from the cluster subdirectory. The bridge module
# also puts every other cluster subdir on sys.path so cross-
# cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps, fmt  # noqa: E402 — raise dps before any mpmath value
del _sys, _Path, _bridge

# polynomial_q_not_applicable: mpmath/numerical-only output; sympy use is intermediate or absent.
"""
Paper 6+1-term mass formula via SHADOW-PRICE DECOMPOSITION.

Replaces the per-generator-volume sum (Markov-non-invariant) of
`paper_six_term_isotope_sweep.py` with a Markov-invariant
shadow-price decomposition

    B(Z, N)  =  m_e · Σ_{λ ⊢ 3A}  C_λ(q) · S_λ(Z, N, A)

where:

  C_λ(q) = w_λ(q) · τ_λ(σ_g)
         = (dim_q(λ)² / [3A]_q!) · (tr σ_g^{(λ)} / dim λ)
  S_λ(Z, N, A) = scaling function determined by content sum c(λ).

For self-conjugate partitions, τ_λ = h/2 exactly (Wigner-2 result).
For non-self-conjugate λ, τ_λ is computed via the optimised
pyhecke kernel.

Markov invariance test: T (Z=1,N=2) and ³He (Z=2,N=1) should give
the same total binding (modulo the genuine Coulomb + n-p split
that lives in the per-content-class scaling) — because both
C_λ and S_λ depend only on partition data, not on braid-word
ordering.

Witness: paper-six-term-shadow-price-sweep.witness.json
"""
import json
import sys
import time
from pathlib import Path
from datetime import datetime, timezone

import mpmath as mp
import sympy as sp

REPO = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(REPO / "tools/pyhecke/python"))
sys.path.insert(0, str(Path(__file__).parent))

import pyhecke
from q_parameter import Q as Q0_FLOAT, Q_MP, Q_INV_MP
from partition_utils import hook_lengths  # noqa: E402


Q0 = Q_MP  # was f64 roundtrip


def q_int(n, q):
    """[n]_q = (q^n - q^{-n}) / (q - q^{-1})."""
    return (q ** n - q ** (-n)) / (q - 1 / q)


# This producer never raised working precision, so every mpmath value in
# it was built at mpmath's default 15 dps and the numbers it emits are
# HONESTLY float64 — no fake precision to detect, no constant built too
# early, so the padding / raw-float64 / import-time gates all pass it.
# Gate: never_raises_dps_audit.py (bean qou-j6gb). Idempotent.
set_compute_dps()

def q_factorial(n, q):
    p = mp.mpf(1)
    for k in range(1, n + 1):
        p *= q_int(k, q)
    return p


def is_self_conjugate(shape):
    """Check if partition is self-conjugate (λ = λ')."""
    if not shape:
        return True
    rows = len(shape)
    cols = max(shape)
    if rows != cols:
        return False
    transpose = []
    for j in range(cols):
        col = sum(1 for r in shape if r > j)
        transpose.append(col)
    return list(shape) == transpose


def dim_q_via_hooks(shape, q, n):
    """dim_q(λ) = [n]_q! / Π_cells [h_x]_q."""
    h_prod = mp.mpf(1)
    for h in hook_lengths(shape):
        h_prod *= q_int(h, q)
    return q_factorial(n, q) / h_prod


def w_lambda(shape, q, n):
    """w_λ = dim_q² / [n]_q!  (**symmetric Plancherel, not Jones-Markov**).

    .. warning::
        Symmetric Plancherel weight; coincides with Jones-Markov y_λ
        only at q = 1.  For Markov-trace contexts at q ≠ 1, use
        `markov_weights_symbolic.solve_y_lambda(n)`.  See
        `docs/audits/2026-05-08-p3-h-3a-divergence.md`.
    """
    d = dim_q_via_hooks(shape, q, n)
    return d ** 2 / q_factorial(n, q)


def content_sum(shape):
    """c(λ) = Σ_{(i,j) ∈ λ}(j - i)."""
    s = 0
    for i, r in enumerate(shape):
        for j in range(r):
            s += j - i
    return s


def height_of(shape):
    """height(λ) = number of rows."""
    return len(shape)


def partitions_of(n):
    """All integer partitions of n in weakly decreasing order."""
    if n == 0:
        yield ()
        return
    def _gen(rem, min_part):
        if rem == 0:
            yield ()
            return
        for p in range(min_part, 0, -1):
            if p > rem:
                continue
            for rest in _gen(rem - p, min(p, rem - p)):
                yield (p,) + rest
    yield from _gen(n, n)


def tau_lambda(shape, q, n):
    """τ_λ(σ_g) = tr(σ_g^{(λ)}) / dim(λ).

    Uses the Wigner-2 self-conjugate identity τ = h/2 when applicable;
    otherwise computes via Hoefsmit content-sum formula
    (the trace at content c is just the q-content):

      tr(σ_g^{(λ)})/dim(λ) = (1/dim) · Σ_T a_{ρ(T,g)}

    For partitions where Hoefsmit is expensive, we approximate via
    the AVERAGE content over cell pairs (a coarse but Markov-invariant
    estimate).  For exact non-self-conjugate τ, use pyhecke's character
    machinery.
    """
    if is_self_conjugate(shape):
        return (q - 1 / q) / 2
    # General case: τ_λ(σ_g) ≈ q^{c̄} − q^{−c̄} where c̄ is normalised
    # average content per cell-pair.  This is a coarse approximation;
    # exact value via Hoefsmit is in `hecke_characters.build_seminormal_matrices`.
    c_avg = content_sum(shape) / max(n - 1, 1)
    return q ** c_avg - q ** (-c_avg)


def scaling_function(shape, Z, N, A):
    """S_λ(Z, N, A) — content-class scaling.

    Per `prop:content-scaling-correspondence`:

      c = +1 (proton-NN):   Z(Z-1)/A^{1/3}
      c = -1 (neutron-NN):  N(N-1)/A^{1/3}
      c =  0 (balanced):    A^{2/3}
      c = ±2:               Z^{4/3}/A^{1/3}
      |c| ≥ 3:              T^p(T+1)^p/A^p

    For self-conjugate λ, c(λ) = 0; the scaling is the
    "balanced" branch.  Implementation here uses the dominant
    classical BW partition family for each content class.
    """
    c = content_sum(shape)
    A_mpf = mp.mpf(A)
    if c == 0:
        # balanced — A or A^{2/3}
        return A_mpf
    elif c == 1:
        return Z * (Z - 1) / A_mpf ** mp.mpf("1/3")
    elif c == -1:
        return N * (N - 1) / A_mpf ** mp.mpf("1/3")
    elif abs(c) <= 2:
        # next-nearest same-type: Z^{4/3}/A^{1/3}
        return mp.mpf(Z if c > 0 else N) ** mp.mpf("4/3") / A_mpf ** mp.mpf("1/3")
    else:
        # long-range: T(T+1)/A
        T = abs(N - Z) / 2
        return T * (T + 1) / A_mpf


def _exact(x):
    """Collapse an exactly-integral mpf to a Python int, leave the rest alone.

    S_lambda is A (a nucleon count) in the short-range branch and T(T+1)/A in
    the long-range one.  The first is exactly an integer; the old float64 cast
    wrote it as 2.0 / 4.0 and put a raw f64 into the witness for no gain.
    """
    if isinstance(x, int):
        return x
    n = mp.floor(x)
    return int(n) if x == n else x


def _serialize(o):
    """mpf -> output-precision string, recursively. Applied ONCE, at the
    witness boundary, so every in-script consumer still sees real mpf."""
    if isinstance(o, mp.mpf):
        return fmt(o)
    if isinstance(o, dict):
        return {k: _serialize(v) for k, v in o.items()}
    if isinstance(o, list):
        return [_serialize(v) for v in o]
    return o


def shadow_price_total(Z, N, q=Q0, partition_filter=None):
    """B = Σ_λ C_λ(q) · S_λ(Z, N, A)."""
    A = Z + N
    n = 3 * A
    total = mp.mpf(0)
    contributions = []
    for shape in partitions_of(n):
        if partition_filter is not None and not partition_filter(shape):
            continue
        w = w_lambda(shape, q, n)
        if abs(w) < mp.mpf('1e-30'):
            continue
        tau = tau_lambda(shape, q, n)
        S = scaling_function(shape, Z, N, A)
        c_lambda = w * tau
        contrib = c_lambda * S
        total += contrib
        if abs(contrib) > mp.mpf('1e-12'):
            # Sort on the mpf, serialize after — reading the serialized value
            # back for the sort key was what forced the float64 cast here.
            contributions.append((abs(contrib), {
                "shape": list(shape),
                "height": len(shape),
                "content_sum": content_sum(shape),
                "self_conjugate": is_self_conjugate(shape),
                "C_lambda": c_lambda,
                # S_lambda is a nucleon count or a T(T+1)/A ratio — exact when
                # integral, so it must not be flattened to float64.
                "S_lambda": _exact(S),
                "contribution": contrib,
            }))
    contributions.sort(key=lambda t: t[0], reverse=True)
    return total, [r for _, r in contributions]


def isospin_mirror_test(label_a, Z_a, N_a, label_b, Z_b, N_b):
    """Compare the shadow-price totals for two isospin partners
    (e.g. T = (Z=1, N=2) and ³He = (Z=2, N=1))."""
    print(f"\n── {label_a} vs {label_b} ──")
    t0 = time.time()
    tot_a, _ = shadow_price_total(Z_a, N_a)
    dt_a = time.time() - t0
    t0 = time.time()
    tot_b, _ = shadow_price_total(Z_b, N_b)
    dt_b = time.time() - t0
    diff = tot_a - tot_b
    rel = abs(diff) / max(abs(tot_a), abs(tot_b), 1e-30)
    print(f"  {label_a}: B_shadow = {mp.nstr(tot_a, 7)}  ({dt_a:.2f}s)")
    print(f"  {label_b}: B_shadow = {mp.nstr(tot_b, 7)}  ({dt_b:.2f}s)")
    print(f"  diff      = {mp.nstr(diff, 7)}  ({mp.nstr(100 * rel, 5)}% relative)")
    return tot_a, tot_b, diff, rel


if __name__ == "__main__":
    print("BW SHADOW-PRICE DECOMPOSITION SWEEP")
    print("=" * 80)
    print(f"q_0 = {float(Q0):.6f}")
    print()
    print("Each isotope's binding decomposed as:")
    print("    B = m_e · Σ_λ C_λ(q) · S_λ(Z, N, A)")
    print("where C_λ = w_λ · τ_λ is partition-only (Markov-invariant)")
    print("and S_λ depends only on (Z, N, A) and content-class.")
    print()

    cases = [
        ("p   (Z=1, N=0)", 1, 0),
        ("n   (Z=0, N=1)", 0, 1),
        ("D   (Z=1, N=1)", 1, 1),
        ("T   (Z=1, N=2)", 1, 2),
        ("³He (Z=2, N=1)", 2, 1),
        ("⁴He (Z=2, N=2)", 2, 2),
    ]

    results = {}
    for label, Z, N in cases:
        t0 = time.time()
        try:
            tot, contribs = shadow_price_total(Z, N)
            dt = time.time() - t0
            print(f"  {label}: B_shadow = {mp.nstr(tot, 7)}  "
                  f"(top contrib partition = {contribs[0]['shape']} → "
                  f"{contribs[0]['contribution']}, "
                  f"{len(contribs)} non-trivial λ, {dt:.2f}s)")
            results[label] = {
                "Z": Z, "N": N,
                "B_shadow": tot,
                "n_partitions_nonzero": len(contribs),
                "top_5_contributions": contribs[:5],
                "walltime_sec": dt,
            }
        except Exception as exc:
            print(f"  {label}: ERROR {type(exc).__name__}: {exc}")
            results[label] = {"error": str(exc)}

    # ── Markov-invariance test: T vs ³He ───
    print("\n══ MARKOV-INVARIANCE TEST: T vs ³He ══")
    T = results.get("T   (Z=1, N=2)")
    He3 = results.get("³He (Z=2, N=1)")
    if T and He3 and "error" not in T and "error" not in He3:
        tot_T = T["B_shadow"]
        tot_3He = He3["B_shadow"]
        diff = tot_T - tot_3He
        rel = abs(diff) / max(abs(tot_T), abs(tot_3He), 1e-30) * 100
        print(f"  T:   B_shadow = {mp.nstr(tot_T, 7)}")
        print(f"  ³He: B_shadow = {mp.nstr(tot_3He, 7)}")
        print(f"  diff = {mp.nstr(diff, 7)}  ({mp.nstr(rel, 5)}% relative)")
        print()
        # Decompose the difference per content class
        c_diff = {c: mp.mpf(0) for c in (0, 1, -1, 2, -2)}
        for r in T["top_5_contributions"]:
            c = r["content_sum"]
            if c in c_diff: c_diff[c] += r["contribution"]
        for r in He3["top_5_contributions"]:
            c = r["content_sum"]
            if c in c_diff: c_diff[c] -= r["contribution"]
        print(f"  Per-content-class T − ³He breakdown:")
        for c in sorted(c_diff):
            if abs(c_diff[c]) > mp.mpf('1e-12'):
                print(f"    c = {c:+d}: {mp.nstr(c_diff[c], 5)}")
        print()
        print(f"  CODATA T − ³He    = +0.019 MeV")
        print(f"  Shadow-price diff = {mp.nstr(diff, 5)} (Hecke units, "
              f"unscaled by m_e and E_0 calibration)")

    witness = {
        "computation": "paper-six-term-shadow-price-sweep",
        "description": (
            "BW shadow-price decomposition B = Σ_λ C_λ · S_λ for each "
            "isotope.  Markov-invariant by construction: C_λ depends "
            "only on partition (no braid-word ordering); S_λ depends "
            "only on (Z, N, A, content_sum).  Replaces the "
            "non-Markov-invariant per-generator V̂_i sum of "
            "paper_six_term_isotope_sweep.py."
        ),
        "reference_blocks": [
            "thm:knot-mass-formula-unified",
            "prop:mass-coefficient-shadow-price",
            "prop:wigner-2-coefficient",
            "prop:content-scaling-correspondence",
            "conj:shell-correction-term-seven",
        ],
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "q_0": fmt(Q_MP),  # was float(Q0_FLOAT): a 16-digit record of a 70-digit pin
            "tau_lambda_implementation": (
                "Wigner-2 closed form (h/2) for self-conjugate λ; "
                "approximate q^{c̄} − q^{−c̄} for non-self-conjugate "
                "(coarse — exact via Hoefsmit available in pyhecke)."
            ),
        },
        "results": _serialize(results),
    }
    out = Path(__file__).parent / "paper-six-term-shadow-price-sweep.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2, default=str))
    print(f"\nWitness: {out}")
