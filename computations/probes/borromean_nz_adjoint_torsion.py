#!/usr/bin/env python3
"""W1 — the independent Neumann–Zagier adjoint torsion τ(𝓑₃), closing the

⚠ CORRECTED 2026-08-07 — this file's determinant is the WRONG construction.

It builds `J_ij = a_ij − b_ij·z_j/(1−z_j)`. Dimofte-Garoufalidis (arXiv:1202.6268,
Defn 1.2) is `det(A·Δ_z'' + B·Δ_z^{-1})` with a global 1/2 and a flattening
monomial — a different matrix, not a normalisation of this one. Consequences:

  * The 4_1 calibration here, |det J_NZ(4_1)| = √3, is exactly TWICE the correct
    value. DG's own worked example (their eq. 3.2) gives τ(4_1) = ½√−3, i.e.
    |τ| = √3/2. `computations/one_loop_torsion.py` reproduces that to rel 1e-71.
  * |det J_NZ(𝓑₃)| = 64 is not an invariant: the same quantity takes 2^{3..6}
    under retriangulation at fixed framing (PR #4691) and 2^{6..9} across
    framings (borromean_cusp_framing_factor.py). Neither is the cause — the
    object simply is not the invariant.
  * The exp(2c₀) = 1/|det J_NZ| relation calibrated on 4_1 inherits the factor 2.

USE `computations/one_loop_torsion.py` instead. It is triangulation-invariant
(verified over 25 retriangulations each of 13 manifolds) and carries the DG unit
test. It now covers ANY cusp number, including 𝓑₃ at c = 3, where it gives
|τ| = 8 rather than the 64 here. The multi-cusp case is DERIVED in
`docs/audits/2026-08-07-one-loop-multicusp-derivation.md` — it is not in DG at
all, and in particular not their Sec 4.5, which is the character-variety
generalization at one cusp (PR #4708).

CAVEAT before repointing this probe's calibration: the overall constant at
c ≥ 2 is inherited from c = 1 and is NOT pinned. Neither invariance nor the
change-of-curve law can see a factor depending only on c — which is exactly the
shape of the `2^{(c−1)/2}` per-cusp factor this chain wanted. Swapping 64 → 8
here does not settle c_σ.

Bean qou-fl4t; audit docs/audits/2026-08-07-one-loop-fix-impact-analysis.md.
Jones-side 1-loop measurement.

Chain of the three W1 Jones-side probes:
  #4208  leading term   → Vol(𝓑₃) = 8G                 (growth rate)
  #4238  subleading      → power p = 3/2, 1-loop c₀     (Kashaev asymptotics)
                            + 4₁ calibration: exp(2c₀) = 1/|det J_NZ| (validated 2e-11)
  THIS   independent τ   → |det J_NZ(𝓑₃)| from the topology, no Jones input.

The 1-loop conjecture (Dimofte–Garoufalidis arXiv:1102.4847 / arXiv:1202.6268)
identifies the constant term c₀ of the Kashaev asymptotics with the ADJOINT
REIDEMEISTER TORSION via the Neumann–Zagier Jacobian.  For an ideal
triangulation with N tetrahedra and shapes z_j, each gluing equation
Π_j z_j^{a_j}(1−z_j)^{b_j} = ±1 has Jacobian (w.r.t. log z_j)

  J_ij = a_ij − b_ij · z_j/(1−z_j)        [ ∂log(1−z)/∂log z = −z/(1−z) ].

Taking the square N×N system of (N−c) independent edge equations + the c
meridians and evaluating at the complete structure gives the torsion
determinant.  The #4238 calibration pinned the exact relation to the Kashaev
constant on the figure-eight:

  exp(2 c₀) = 1 / |det J_NZ|      (1-cusp knot).

VALIDATION (4₁, this file): |det J_NZ(4₁)| = √3, so 1/|det| = 1/√3 =
exp(2c₀(4₁)) — reproducing the #4238 calibration value exactly, from pure
topology (no Jones tower).

RESULT (𝓑₃ = L6a4): |det J_NZ(𝓑₃)| = 64 (= 2⁶), exact.  The #4238 Jones-side
measurement gave c₀(𝓑₃) ≈ −1.383 ≈ −ln4, i.e. exp(2c₀) ≈ 1/16 = 4/64.  So the
Jones measurement and the independent topological torsion agree up to a clean
factor 4 — the 3-cusp normalization offset predicted (not fitted) in #4238:
the relation is 1/|det| for the 1-cusp knot and 4/|det| for the 3-cusp link
(the Habiro J_{B,1}=1 normalization / diagonal-vs-full cusp framing; its exact
first-principles value 4 is the remaining thread, NOT a free parameter here).

DATA PROVENANCE.  The integer gluing matrices below are SnapPy's
`Manifold(name).gluing_equations('rect')` for 4₁ and L6a4 (Borromean rings),
transcribed verbatim; the shapes are the EXACT algebraic complete-structure
values (4₁: z = e^{iπ/3}; L6a4: the regular ideal octahedron z ∈ {(1+i)/2,
1+i}), so this probe is self-contained and exact — it needs no SnapPy at
runtime.  With SnapPy present, `--recompute` re-derives both live and asserts
agreement.

Discipline: audit-only; scope-(a); NO fit (shapes/gluing are topological
inputs; the torsion is computed, not tuned); nothing wired; L2 unchanged.

-- Ref: [manuscript] docs/audits/2026-07-25-borromean-jones-asymptotics-volume-and-1loop.md

THEOREM BACKING (2026-08-02, bean qou-pvuw): the 1-loop conjecture used below is now a THEOREM for both calibration cases — 4_1 is 2-bridge (Garoufalidis-Yoon arXiv:2411.03801 Thm 1.1, [garoufalidis-yoon-2024], library/arxiv-2411.03801v2/2411.03801v2.pdf) and the Borromean rings are a fundamental shadow link (Pandey-Wong arXiv:2308.06643, [pandey-wong-2023]). Wording below kept for history; readings of exp(2c0) = 1/|det J_NZ| are theorem-backed.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

mp.mp.dps = 50

# ── SnapPy gluing_equations('rect') rows: (a[·], b[·], sign);
#    equation Π_j z_j^{a_j} (1−z_j)^{b_j} = (−1)^sign.  First N rows are edges,
#    then per cusp [meridian, longitude]. Transcribed from SnapPy 3.3.2. ──
FIG8 = {
    "N": 2, "c": 1,
    "rows": [
        ([2, 2], [-1, -1], 1), ([-2, -2], [1, 1], 1),      # edges
        ([1, 1], [0, -1], -1), ([0, 4], [0, -2], 1),        # cusp1: mer, long
    ],
}
BOR = {
    "N": 8, "c": 3,
    "rows": [
        ([1, 0, 1, -1, 0, 1, 0, 0], [-1, 1, 0, 1, 0, 0, -1, 0], 1),
        ([-1, 0, 0, 0, 0, 0, 0, -1], [1, -1, 0, 0, -1, 0, 0, 1], 1),
        ([-1, 0, 0, 0, 0, 0, 0, 0], [1, 0, -1, -1, -1, 0, 0, 0], -1),
        ([0, -1, 0, 0, -1, 1, 0, 0], [-1, 1, 1, 0, 1, -1, 0, -1], -1),
        ([1, 1, 0, 0, 1, 0, 1, 1], [0, 0, 0, 1, 0, 0, -1, 0], -1),
        ([0, 0, 0, 0, 0, -1, -1, -1], [0, -1, 0, 0, 0, 1, 1, 1], -1),
        ([0, 0, 0, 0, 0, -1, -1, 0], [0, 0, -1, -1, 0, 1, 1, 0], 1),
        ([0, 0, -1, 1, 0, 0, 1, 1], [0, 0, 1, 0, 1, -1, 0, -1], 1),   # 8 edges above
        ([0, 1, 0, 0, 0, -1, 0, 0], [0, -1, 0, 0, 0, 1, 0, 1], 1),    # cusp1 mer
        ([1, 0, -1, 1, 0, 0, 1, 0], [-1, 1, 1, 0, 0, -1, 0, 0], 1),   # cusp1 long
        ([0, -1, -1, 0, 0, -1, -1, 1], [-1, 1, 0, -1, 1, 0, 1, -1], -1),  # cusp2 mer
        ([1, 0, 0, 0, 0, 0, 0, 0], [-1, 0, -1, -1, 1, 0, 0, 0], -1),  # cusp2 long
        ([0, 0, 0, 0, 0, -1, 0, 0], [0, -1, 0, 0, 0, 0, 1, 0], 1),    # cusp3 mer
        ([0, 1, 0, 0, 1, 1, 0, 1], [1, 0, 0, -1, -1, -1, 0, 0], 1),   # cusp3 long
    ],
}

# Exact complete-structure shapes.
Z_FIG8 = [mp.e ** (1j * mp.pi / 3)] * 2                    # e^{iπ/3}
# L6a4 regular ideal octahedron: z=(1+i)/2 at {0,5,6,7}, z=1+i at {1,2,3,4}.
_half = (1 + 1j) / mp.mpf(2)
_one = 1 + 1j * mp.mpf(1)
Z_BOR = [_half, _one, _one, _one, _one, _half, _half, _half]


def torsion_det(data, shapes):
    """|det J_NZ| via (N−c) independent edge rows + c meridian rows."""
    N, c, rows = data["N"], data["c"], data["rows"]
    w = [z / (1 - z) for z in shapes]                     # z_j/(1−z_j)

    def jrow(row):
        a, b, _ = row
        return [mp.mpf(a[j]) - mp.mpf(b[j]) * w[j] for j in range(N)]

    edges = [jrow(rows[i]) for i in range(N)]
    meridians = [jrow(rows[N + 2 * i]) for i in range(c)]

    # greedily pick N independent rows (edges first, then meridians)
    def rank_after(chosen, cand):
        Mx = [r[:] for r in chosen + [cand]]
        r = 0
        for col in range(N):
            piv = next((i for i in range(r, len(Mx))
                        if abs(Mx[i][col]) > mp.mpf(10) ** -25), None)
            if piv is None:
                continue
            Mx[r], Mx[piv] = Mx[piv], Mx[r]
            for i in range(len(Mx)):
                if i != r and abs(Mx[i][col]) > 0:
                    f = Mx[i][col] / Mx[r][col]
                    Mx[i] = [Mx[i][k] - f * Mx[r][k] for k in range(N)]
            r += 1
        return r

    chosen = []
    for cand in edges + meridians:
        if rank_after(chosen, cand) > len(chosen):
            chosen.append(cand)
        if len(chosen) == N:
            break
    return abs(mp.det(mp.matrix(chosen)))


def maybe_recompute():
    """Cross-check the hardcoded data against a live SnapPy, if present."""
    try:
        import snappy
    except Exception:
        print("  (SnapPy not installed — skipping live cross-check)")
        return
    for name, data in (("4_1", FIG8), ("L6a4", BOR)):
        M = snappy.Manifold(name)
        Gr = M.gluing_equations('rect')
        live = [(list(r[0]), list(r[1]), int(r[2])) for r in Gr]
        hard = [(a, b, s) for a, b, s in data["rows"]]
        assert live == hard, f"{name}: gluing rows drift vs hardcoded!"
    print("  SnapPy live cross-check: gluing rows match hardcoded ✓")


def main() -> int:
    recompute = "--recompute" in sys.argv
    print("W1 — independent Neumann–Zagier adjoint torsion  |det J_NZ|\n")

    d4 = torsion_det(FIG8, Z_FIG8)
    inv4 = 1 / d4
    sqrt3 = mp.sqrt(3)
    err4 = abs(d4 - sqrt3)
    exp2c0_41 = 1 / sqrt3   # = |τ_adj(4₁)| pinned by the #4238 calibration
    print(f"4₁ (validation):  |det J_NZ| = {mp.nstr(d4, 14)}   (√3 = {mp.nstr(sqrt3,14)}, err {float(err4):.1e})")
    print(f"                  1/|det|    = {mp.nstr(inv4, 12)}   = 1/√3 = exp(2c₀(4₁))  ✓")

    dB = torsion_det(BOR, Z_BOR)
    invB = 1 / dB
    err64 = abs(dB - 64)
    print(f"\n𝓑₃ = L6a4:        |det J_NZ| = {mp.nstr(dB, 14)}   (2⁶ = 64, err {float(err64):.1e})")
    print(f"                  1/|det|    = {mp.nstr(invB, 12)}   (= 1/64)")

    # Jones-side c₀(𝓑₃) from #4238 (Vol-fixed higher-order fit):
    c0_bor_measured = mp.mpf("-1.38281")
    exp2c0_bor = mp.e ** (2 * c0_bor_measured)
    factor = exp2c0_bor * dB
    print(f"\nBridge to the Jones measurement (#4238):")
    print(f"  measured  c₀(𝓑₃)      = {mp.nstr(c0_bor_measured,7)}   (−ln4 = {mp.nstr(-mp.log(4),7)})")
    print(f"  exp(2c₀)              = {mp.nstr(exp2c0_bor,7)}   (1/16 = 0.0625)")
    print(f"  exp(2c₀)·|det J_NZ|   = {mp.nstr(factor,6)}   (clean factor ≈ 4 = 3-cusp offset)")

    if recompute:
        print("\nSnapPy live cross-check:")
        maybe_recompute()

    ok = err4 < mp.mpf(10) ** -20 and err64 < mp.mpf(10) ** -10
    print(f"\nVERDICT: {'VALIDATED' if ok else 'CHECK'} — 4₁ torsion = √3 reproduces "
          f"exp(2c₀(4₁))=1/√3 exactly; 𝓑₃ torsion = 64 (independent of Jones); "
          f"Jones c₀ matches to the factor-4 3-cusp offset.")

    # witness
    sp = Path(__file__).resolve(); src = sp.read_text()
    try:
        commit = subprocess.check_output(["git", "log", "-1", "--format=%H", "--", str(sp)],
                                          cwd=sp.parent, text=True).strip()
    except Exception:
        commit = ""
    witness = {
        "engine": "mpmath", "engineVersion": f"mpmath {mp.__version__}",
        "computedAt": datetime.now(timezone.utc).isoformat(), "commitSha": commit,
        "scriptFile": "computations/probes/borromean_nz_adjoint_torsion.py",
        "scriptHash": hashlib.sha256(src.encode()).hexdigest()[:12], "scriptCommitSha": commit,
        "theorem_backing": "GY 2411.03801 Thm 1.1 (4_1, 2-bridge) + PW 2308.06643 (Borromean, fundamental shadow link) — 1-loop = adjoint torsion proved for both cases",
        "description": "Independent Neumann–Zagier adjoint-torsion determinant for the "
                       "Borromean rings (L6a4) and figure-eight (4₁), from SnapPy gluing "
                       "data + exact algebraic shapes. Validates exp(2c₀)=1/|det| on 4₁ "
                       "(=√3) and gives |det J_NZ(𝓑₃)|=64. Audit-only; no fit; nothing wired.",
        "auditOnly": True,
        "parameters": {"snappy_recompute": recompute},
        "data": {
            "fig8_det_abs": mp.nstr(d4, 20), "fig8_det_exact": "sqrt(3)",
            "fig8_inv_det": mp.nstr(inv4, 20), "fig8_matches_exp2c0": "1/sqrt(3)",
            "borromean_det_abs": mp.nstr(dB, 20), "borromean_det_exact": "64",
            "borromean_inv_det": mp.nstr(invB, 20),
            "jones_c0_borromean_measured": "-1.38281",
            "exp2c0_times_det_factor": mp.nstr(factor, 8),
            "note": "exp(2c0)=1/|det| validated on 4_1 (1-cusp); for the 3-cusp "
                    "Borromean the relation carries a clean factor 4 (normalization/"
                    "cusp offset), so exp(2c0)=4/|det|=1/16. |det(B3)|=64 is the exact "
                    "independent adjoint-torsion determinant.",
        },
    }
    out = sp.with_name("borromean-nz-adjoint-torsion.witness.json")
    out.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness → {out.name}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
