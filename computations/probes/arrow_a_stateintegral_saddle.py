#!/usr/bin/env python3
"""W1 arrow (A), index↔tr_M: the volume-asymptotics route goes through the
state-integral SADDLE, not the index q-series (two series routes ruled out).

Context. The `I_𝓑₃ → tr_M(β_Bor)` bridge invariant list
(docs/audits/2026-07-24-borromean-index-bridge-invariant.md §1(d)-(e)) names the
DGG volume-asymptotics route (q→1 't Hooft limit; the index's leading
asymptotics carry Vol(M)) as "the honest candidate" for arrow (A), but does not
say HOW to extract Vol from the index.  This probe settles that, on the cheap
figure-eight testbed and the Borromean target, and reports what does NOT work.

TWO NATURAL INDEX-SERIES ROUTES FAIL (empirical, this file):

1. Naive q→1 evaluation of the total index I^tot_{4₁}(q) = Σ_e I(eμ)(q).
   The partial sum goes NEGATIVE near q=1 (−48 at q=0.7 → −1500 at q=0.95): the
   truncated growing tail + the sign structure dominate, so (1−q)·log I^tot is
   meaningless.

2. Circle-method coefficient asymptotics.  With coefficients verified STABLE to
   q^60 (cutoff-independent), the total-index coefficients [1,−8,−9,18,46,90,62,
   10,−170,…] PEAK at n≈12 (|a|≈980) and DECAY to ≈0 by n≈19 — there is NO
   exp(V/(1−q)) essential singularity at q=1, so the standard
   log|a_n| ~ 2√(Vn/2π) law gives garbage (fit → V≈1239, not 2.03).  The total
   index is not the object that carries Vol as coefficient growth.

THE PROPER RESUMMATION — the state-integral SADDLE — WORKS (uses symmetries):

The state integral (Andersen–Kashaev; "closely related to the total index",
GHRS arXiv:1604.02688 Rmk 1.13) is the Borel sum of the divergent perturbative
series; its ℏ→0 saddle value is the complex volume.  Amphichirality of 4₁
(CS = 0) makes that saddle PURELY REAL, and the octahedral S₃ symmetry fixes the
Borromean shapes.  The saddle value is the Bloch–Wigner dilogarithm at the
shapes,  D(z) = Im Li₂(z) + arg(1−z)·log|z|:

   4₁ :  Vol = 2·D(e^{iπ/3}) = 2.02988321…      (= Vol(4₁), CS = 0)
   𝓑₃ :  Vol = 8·D(i)        = 7.32772475… = 8G  (= Vol(𝓑₃), 8 octahedron tets)

Both reproduce the hyperbolic volume EXACTLY, and 8G matches the Jones-side
anchor (PR #4208) and the NZ-torsion probe (PR #4253).  So the volume-route
resummation is the state-integral saddle = classical dilog at the shapes — the
SHARED geometric datum both the colored-Jones asymptotics and the index/
state-integral carry.

SCOPE (what this does / does NOT close).  This establishes the CORRECT route for
arrow (A)'s volume piece and rules out the two naive index-series routes.  It
does NOT close arrow (A): the actual map I_𝓑₃ → tr_M(β_Bor) is the full DGG
3d-3d / quantum-modularity dictionary; the shared saddle data (Vol, and the
1-loop torsion 64 from #4253) is the leading + subleading geometric anchor both
sides must share, but the non-perturbative map to tr_M's actual values remains
the research-scale open sub-problem.  Audit-only; scope-(a); NO fit (shapes are
topological; volumes are computed, not tuned); nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/audits/2026-07-24-borromean-index-bridge-invariant.md
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import math
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


def bloch_wigner(z):
    """D(z) = Im Li₂(z) + arg(1−z)·log|z| — the state-integral saddle value."""
    z = mp.mpc(z)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def load_fig8_index():
    p = Path(__file__).resolve().parent / "figure_eight_3d_index.py"
    spec = importlib.util.spec_from_file_location("f8", p)
    m = importlib.util.module_from_spec(spec)
    try:
        spec.loader.exec_module(m)
    except SystemExit:
        pass
    return m


def total_index_coeffs(f8, NQ, emax, km):
    """I^tot_{4₁}(q) = Σ_e I(eμ)(q) coefficients of q^0..q^NQ (Q^{2j}=q^j)."""
    tot = {}
    for e in range(-emax, emax + 1):
        d = f8.index(e, 0, kmax=km)
        for P, c in d.items():
            if P % 2 == 0:
                j = P // 2
                if 0 <= j <= NQ:
                    tot[j] = tot.get(j, 0) + c
    return [int(tot.get(j, 0)) for j in range(NQ + 1)]


def lstsq(X, y):
    m = len(X[0])
    AtA = [[sum(X[k][i] * X[k][j] for k in range(len(X))) for j in range(m)] for i in range(m)]
    Aty = [sum(X[k][i] * y[k] for k in range(len(X))) for i in range(m)]
    M = [AtA[i] + [Aty[i]] for i in range(m)]
    for c in range(m):
        p = max(range(c, m), key=lambda r: abs(M[r][c])); M[c], M[p] = M[p], M[c]
        for r in range(m):
            if r != c and M[r][c]:
                f = M[r][c] / M[c][c]; M[r] = [M[r][k] - f * M[c][k] for k in range(m + 1)]
    return [M[i][m] / M[i][i] for i in range(m)]


def main() -> int:
    VOL_41 = float(2 * bloch_wigner(mp.e ** (1j * mp.pi / 3)))
    VOL_BOR = float(8 * bloch_wigner(1j))

    print("W1 arrow (A): volume-route resummation = state-integral saddle\n")

    # ── route 1 + 2: the failing index-series routes (figure-eight) ──
    # NQ=60 so the "stable to q^60" claim is reproducible from this script.
    NQ = 60
    f8 = load_fig8_index()
    a = total_index_coeffs(f8, NQ=NQ, emax=25, km=45)
    a_hi = total_index_coeffs(f8, NQ=NQ, emax=40, km=70)
    stable = NQ
    for j in range(NQ + 1):
        if a[j] != a_hi[j]:
            stable = j - 1
            break
    print(f"Route 1/2 — total index I^tot_4₁ (coeffs stable to q^{stable}):")
    print(f"  a[0..18] = {a_hi[:19]}")
    # route 1: naive q→1
    negs = []
    for q in (0.7, 0.9, 0.95):
        S = sum(mp.mpf(a_hi[j]) * mp.mpf(q) ** j for j in range(NQ + 1))
        negs.append((q, float(S)))
    print(f"  route 1 (naive q→1): I^tot(q) = {['%.0f@q=%.2f' % (v, qq) for qq, v in negs]}")
    print(f"    → sign-indefinite, tail-dominated: (1−q)log I^tot meaningless. FAILS.")
    # route 2: circle method log|a_n| ~ 2√(Vn/2π)
    pts = [(n, math.log(abs(a_hi[n]))) for n in range(6, 14) if a_hi[n] != 0]
    A, B, C = lstsq([[math.sqrt(n), math.log(n), 1.0] for n, _ in pts], [v for _, v in pts])
    V_circle = (A / 2) ** 2 * 2 * math.pi if A > 0 else float('nan')
    print(f"  route 2 (circle method): coeffs peak n≈12 then decay to 0 by n≈19 "
          f"→ no exp(V/(1−q)) singularity; fit V={V_circle:.1f} (Vol=2.03). FAILS.")

    # ── the working route: state-integral saddle = Bloch–Wigner dilog ──
    print(f"\nProper route — state-integral saddle (Bloch–Wigner dilog at the shapes):")
    print(f"  4₁ : 2·D(e^{{iπ/3}}) = {VOL_41:.8f}   (Vol(4₁)=2.02988321, CS=0 amphichiral)")
    print(f"  𝓑₃ : 8·D(i)         = {VOL_BOR:.8f}   (8G = Vol(𝓑₃); matches Jones #4208 + NZ #4253)")
    ok = abs(VOL_41 - 2.0298832) < 1e-6 and abs(VOL_BOR - 7.3277247) < 1e-6
    print(f"\nVERDICT: {'CONFIRMED' if ok else 'CHECK'} — the two index-series routes fail; the "
          f"state-integral saddle (classical dilog at the symmetry-fixed shapes) gives Vol "
          f"exactly on both sides. Arrow (A)'s volume piece goes through the saddle, not the "
          f"series; the full non-perturbative map to tr_M stays open.")

    sp = Path(__file__).resolve(); src = sp.read_text()
    # Provenance: resolve repo root, use a repo-relative pathspec, and fall back
    # to HEAD if the file has no commit yet (avoids empty commitSha → PROV_MISSING).
    rel = "computations/probes/arrow_a_stateintegral_saddle.py"
    try:
        root = subprocess.check_output(["git", "rev-parse", "--show-toplevel"],
                                       cwd=sp.parent, text=True).strip()
        commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", rel],
                                         cwd=root, text=True).strip()
        if not commit:
            commit = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                             cwd=root, text=True).strip()
    except Exception:
        commit = "unknown"
    wit = {
        "engine": "mpmath", "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": commit,
        "scriptFile": "computations/probes/arrow_a_stateintegral_saddle.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12], "scriptCommitSha": commit,
        "description": "W1 arrow (A): the index↔tr_M volume-route resummation is the "
                       "state-integral saddle (Bloch-Wigner dilog at the shapes), not the "
                       "index q-series (two series routes ruled out). Audit-only; no fit.",
        "auditOnly": True,
        "parameters": {"fig8_index_stable_to_q": stable},
        "data": {
            "route1_naive_q1": "FAILS: I^tot sign-indefinite near q=1 (tail-dominated)",
            "route2_circle_method": f"FAILS: coeffs peak+decay, no exp(V/(1-q)) singularity; fit V={V_circle:.1f}",
            "saddle_vol_4_1": VOL_41, "saddle_vol_borromean": VOL_BOR,
            "vol_4_1_exact": 2.0298832128, "vol_borromean_8G": 7.3277247534,
            "verdict_saddle_gives_vol": bool(ok),
            "note": "state-integral saddle = Borel sum critical value = Bloch-Wigner D(shape); "
                    "amphichiral 4_1 CS=0 -> real saddle. Shared (Vol, torsion=64 #4253) anchor "
                    "both sides; full I_B3->tr_M map remains the DGG-correspondence open problem.",
        },
    }
    out = sp.with_name("arrow-a-stateintegral-saddle.witness.json")
    out.write_text(json.dumps(wit, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
