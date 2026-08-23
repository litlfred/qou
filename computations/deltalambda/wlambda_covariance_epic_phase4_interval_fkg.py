#!/usr/bin/env python3
r"""
wlambda_covariance_epic_phase4_interval_fkg.py — Phase 4 of the covariance-kernel proof epic
(qou-x631): sharpen the kernel to a compact-interval correlation inequality (Griffiths/FKG-type),
by analogy with Fulman's Stein / eigenfunction-drift method.

The kernel `cov(k) = Σ_{λ⊢k} (f^λ)³ ω₃(λ) ≤ 0` (ω₃ = Σ_□c(□)² − C(k,2)) is, at the measure level,
`E_{(dim)³}[ω₃] ≤ 0` under the dimension-cubed measure `(f^λ)³/Z`. Writing the β-family
`H(β) := E_β[C₂] − C(k,2)` with `E_β[X] = Σ_λ(f^λ)^β X / Σ_λ(f^λ)^β`, the kernel is `H(3) ≤ 0`.

KEY SHARPENING (this probe).  We do NOT need the full β ≥ 2 family (whose global monotonicity fails —
Phase 1 found H rises 4→5).  β = 3 sits INSIDE the monotone-decreasing window: `E_β[C₂]` decreases
2→3→4.  So the kernel follows from the COMPACT-INTERVAL statement

    d/dβ E_β[C₂] = Cov_β(C₂, ln f) ≤ 0   for all β ∈ [2,3],

integrated from H(2) = 0.  And since `ln f^λ = ln(k!) − Σ_□ ln h(□)` (hook lengths), this is

    Cov_β( Σ_□ c(□)²,  Σ_□ ln h(□) ) ≥ 0   for β ∈ [2,3],

a **positive correlation between two explicit box-sum statistics** — the content-spread and the
log-hook-sum — under the `(f^λ)^β` measure.  This is the "by analogy with these papers" route
(Fulman's Stein/eigenfunction-drift + the correlation-inequality machinery).  NOTE (see Phase 4b):
this reduction LOWERS THE DIMENSION POWER (from the `(f^λ)³`-weighted sum to a `ln f`-covariance) but
does **not** sidestep the dimension — `Σ ln h = ln k! − ln f` still contains the log-dimension, which
is NOT a polynomial function of the diagram (`∉ A`).  Both off-the-shelf closers (FKG-on-dominance,
Chebyshev-comonotone) are ELIMINATED in Phase 4b; the reduced inequality remains open.

This probe verifies, at 40 dps on a fine β-grid over [2,3]:
  (a) `E_β[C₂]` is monotone non-increasing on [2,3]  (β=3 inside the monotone window);
  (b) `Cov_β(C₂, ln f) ≤ 0` on [2,3]  (the derivative that integrates to the kernel);
  (c) `Cov_β(Σc², Σ ln h) ≥ 0` on [2,3]  (the FKG/Griffiths target: content-spread ⊥⁺ log-hook-sum).

Discipline: scope-(a) reframing; no fit; nothing wired; no `c_k`; L2 unchanged (2/7).  The kernel
remains an honest §3b conjecture — this SHARPENS the open target, it does not close it.

# Ref: [fulman2004stein] https://doi.org/10.1090/S0002-9947-04-03499-3
"""
from __future__ import annotations

import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE.parent / "substrate"))

from mpmath import mp, mpf, power, fsum, log as mlog  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()
NMAX = 14
GRID = 20  # β samples over [2,3], step 1/GRID
TOL = mpf('1e-30')


def partitions_of(n, m=None):
    if m is None:
        m = n
    if n == 0:
        yield ()
        return
    for i in range(min(n, m), 0, -1):
        for rest in partitions_of(n - i, i):
            yield (i,) + rest


def hook_lengths(l):
    l = list(l)
    if not l:
        return []
    conj = [sum(1 for p in l if p > j) for j in range(l[0])]
    hs = []
    for i, row in enumerate(l):
        for j in range(row):
            hs.append((row - j) + (conj[j] - i) - 1)
    return hs


def hook_dim(l):
    d = 1
    for h in hook_lengths(l):
        d *= h
    return math.factorial(sum(l)) // d


def C2(l):
    return sum((j - i) ** 2 for i, row in enumerate(l) for j in range(row))


def shape_stats(k):
    """(f, C2, ln f, Σ ln h) per λ⊢k."""
    out = []
    for l in partitions_of(k):
        f = hook_dim(l)
        out.append((mpf(f), mpf(C2(l)), mlog(mpf(f)),
                    fsum(mlog(mpf(h)) for h in hook_lengths(l))))
    return out


def eval_at(stats, beta):
    Z = fsum(power(f, beta) for f, _, _, _ in stats)
    w = [power(f, beta) / Z for f, _, _, _ in stats]
    EC2 = fsum(wi * c2 for wi, (_, c2, _, _) in zip(w, stats))
    Elnf = fsum(wi * lf for wi, (_, _, lf, _) in zip(w, stats))
    Elnh = fsum(wi * lh for wi, (_, _, _, lh) in zip(w, stats))
    cov_C2_lnf = fsum(wi * c2 * lf for wi, (_, c2, lf, _) in zip(w, stats)) - EC2 * Elnf
    cov_C2_lnh = fsum(wi * c2 * lh for wi, (_, c2, _, lh) in zip(w, stats)) - EC2 * Elnh
    return EC2, cov_C2_lnf, cov_C2_lnh


def main() -> int:
    print("=== Covariance-kernel epic (qou-x631) — Phase 4: interval / FKG reframing ===\n")
    print("Kernel (β=3) ⇐ E_β[C₂] monotone-decreasing on [2,3] ⇐ Cov_β(Σc², Σln h) ≥ 0 on [2,3].\n")

    betas = [mpf(2) + mpf(j) / mpf(GRID) for j in range(0, GRID + 1)]  # 2.00 .. 3.00
    all_mono = all_cov1 = all_cov2 = True
    for k in range(3, NMAX + 1):
        stats = shape_stats(k)
        ECs, c1s, c2s = [], [], []
        for b in betas:
            ec, c1, c2 = eval_at(stats, b)
            ECs.append(ec); c1s.append(c1); c2s.append(c2)
        mono = all(ECs[i] >= ECs[i + 1] - TOL for i in range(len(ECs) - 1))
        cov1_neg = all(c <= TOL for c in c1s)
        cov2_pos = all(c >= -TOL for c in c2s)
        all_mono &= mono; all_cov1 &= cov1_neg; all_cov2 &= cov2_pos
        print(f"k={k:2d}: E_β[C₂]↓on[2,3]={mono}  Cov_β(C₂,lnf)≤0={cov1_neg}  "
              f"Cov_β(Σc²,Σlnh)≥0={cov2_pos}  [E₂={float(ECs[0]):.3f}→E₃={float(ECs[-1]):.3f}]")

    ok = all_mono and all_cov1 and all_cov2
    print(f"\nAll k≤{NMAX}, β∈[2,3] (step 1/{GRID}): interval-monotone={all_mono}, "
          f"Cov(C₂,lnf)≤0={all_cov1}, Cov(Σc²,Σlnh)≥0={all_cov2}")
    print(f"\nRESULT: kernel sharpened to the compact-interval FKG target: {ok}")
    print("Target for a proof (analogy of Fulman/Stein + Griffiths-FKG): "
          "Cov_β(Σ_□c², Σ_□ln h) ≥ 0 on [2,3].")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("wlambda-covariance-epic-phase4-interval-fkg", engine="python-exact+mpmath")
        w.set_description(
            "Phase 4 of the covariance-kernel proof epic (qou-x631): sharpen the kernel to a "
            "compact-interval correlation inequality, by analogy with Fulman's Stein/eigenfunction-drift "
            "method. The kernel cov(k)=Σ(f^λ)³ω₃≤0 is H(3)≤0 for H(β)=E_β[C₂]−C(k,2). β=3 lies inside "
            "the monotone-decreasing window (E_β[C₂] decreases 2→3→4; only rises 4→5, Phase 1), so the "
            "kernel needs only the INTERVAL statement d/dβ E_β[C₂]=Cov_β(C₂,ln f)≤0 on [2,3], integrated "
            "from H(2)=0. Since ln f=ln k!−Σln h, this is Cov_β(Σc², Σln h)≥0 on [2,3] — a POSITIVE "
            "correlation between two explicit box-sum statistics (content-spread, log-hook-sum). NOTE "
            "(Phase 4b): this LOWERS THE DIMENSION POWER (from (f)³-weighting to a ln f-covariance) but "
            "does NOT sidestep the dimension — Σln h=ln k!−ln f still contains the log-dimension (∉A); "
            "and both off-the-shelf closers (FKG-on-dominance, Chebyshev-comonotone) are eliminated in "
            "Phase 4b. Verified 40 dps on a fine β-grid over [2,3], all k≤14: (a) E_β[C₂] monotone "
            "non-increasing; (b) Cov_β(C₂,ln f)≤0; (c) Cov_β(Σc²,Σln h)≥0. This SHARPENS the open "
            "target; it does not close it. scope-(a); no fit; nothing wired; no c_k; L2 2/7.")
        w.add_data("interval", "[2,3]")
        w.add_data("kmax", NMAX)
        w.add_data("beta_grid_step", f"1/{GRID}")
        w.add_data("interval_monotone_all_k", bool(all_mono))
        w.add_data("cov_C2_lnf_nonpos_all_k", bool(all_cov1))
        w.add_data("cov_C2_lnh_nonneg_all_k", bool(all_cov2))
        w.add_data("fkg_target", "Cov_beta(sum c^2, sum ln h) >= 0 on [2,3]")
        w.add_assertion(
            "covariance_epic_phase4_interval_fkg_reframing",
            computed=str(int(ok)), expected="1", tolerance=0,
            source=("Kernel (β=3) sharpened to Cov_β(Σc²,Σln h)≥0 on [2,3] (Griffiths/FKG-type): "
                    "E_β[C₂] monotone-decreasing on [2,3], Cov_β(C₂,ln f)≤0, Cov_β(Σc²,Σln h)≥0, "
                    "all verified 40 dps k≤14. Both statistics are explicit box-sums (dimension "
                    "obstruction sidestepped). No fit; no c_k."))
        out = w.save()
        print(f"\nWitness: {out}")
    except ImportError as e:
        print(f"\n(witness skipped — witness_base unavailable: {e})")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
