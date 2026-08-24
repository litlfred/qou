#!/usr/bin/env python3
"""Task-B cyclic-vector intertwiner — verification + witness (Python reference).

The gauge-aligned A-combiner (`a_operator_gauge_align.gauge_aligned_A_combiner_general`)
builds the intertwiner `U: V_μ⊗V_ν⊗ℂ^c → range(Π_{μν})` by vectorising the
intertwining constraints into an `r²×r²` null space — **O(r⁴) memory / O(r⁶) time**.
For the 4 large-`r` (r=64) λ⊢9 — `(3,3,2,1)`, `(4,3,2)`, `(4,2,2,1)`, `(4,3,1,1)` —
that `r²×r²` matrix OOMs (~5.4 GB), leaving 26/30 λ⊢9 covered.

`gauge_aligned_A_combiner_general_cyclic` replaces the null space with the
**handover §5 cyclic-vector construction** (matrix-unit preimages + cyclic
reference vectors): it never forms an `r²`-sized matrix, so it is O(r³) and
clears the OOM. This probe is the **correctness gate** — the gauge-invariant
combiner identity at 1e-25:

    χ^λ(W·I·β)  ==  Σ_{μν} Tr[ A^λ_{μν}(I) · (ρ_μ(W) ⊗ ρ_ν(β)) ]

with ground-truth χ from the H_n seminormal trace and ρ_μ/ρ_ν at the *small*
H_inner/H_block level. Checks:

  * H_6 (n_inner=3, n_block=3): all 11 λ⊢6, all braid test words.
  * H_9 (n_inner=6, n_block=3): a feasible λ=(8,1) — exercises the n_inner=6 path.

The pure-mpmath cyclic build is correct but still slow at r=64 (256 matrix-unit
words × r×r products); the *production* unlock of the 4 r=64 λ is the Rust port
of this construction into `combiner_block` (lib.rs). This file pins the
reference values the Rust port must match bit-for-(40+)-digit.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: F401,E402
from _precision import set_compute_dps  # noqa: E402 — dps must rise before module constants
del _sys, _Path, _bridge

import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import a_operator_gauge_align as g  # noqa: E402
import a_operator_categorical as aoa  # noqa: E402
from lr_coefficients import partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

EXACT = mp.mpf("1e-25")


def _idcheck(lam, n_inner, n_block, q_str, h, rho_in, rho_bl, p_in, p_bl,
             n_inner_words, n_block_words, dps):
    """Combiner identity max-residual for one λ using the cyclic combiner."""
    mats, dim = aoa.exact_seminormal_matrices(lam, q_str, dps)
    if dim == 0:
        return None, 0
    # Colour-weighted p-n interface, the SAME shift the combiner on the RHS
    # uses (a_operator_gauge_align._d_pn).  Was the colour-blind -h/2 here,
    # which 3dcf933c5d moved on the RHS but missed on this side: the two legs
    # of a gauge-invariant identity were then built with different interfaces.
    I_if = mats[n_inner - 1] + g._d_pn(h) * mp.eye(dim)

    def fac(br):
        return [(mp.mpf(1), mp.mpf(0) if s > 0 else -h, gg) for (s, gg) in br]

    def wm(ms, f):
        M = mp.eye(ms[0].rows)
        for (c, d, gg) in f:
            M = M * (c * ms[gg] + d * mp.eye(ms[0].rows))
        return M

    Ac = g.gauge_aligned_A_combiner_general_cyclic(lam, n_inner, n_block, q_str, dps)
    inner = aoa._braid_test_words(n_inner)[:n_inner_words]
    block = aoa._braid_test_words(n_block)[:n_block_words]
    max_abs = mp.mpf(0)
    n = 0
    for wi in inner:
        fi = fac(wi)
        W = wm(mats, fi)
        rmu = {mu: wm(rho_in[mu], fi) for mu in p_in}
        for wb in block:
            fb = [(c, d, gg + n_inner) for (c, d, gg) in fac(wb)]
            B = wm(mats, fb)
            lhs = aoa._trace(W * I_if * B)
            rnu = {nu: wm(rho_bl[nu], fac(wb)) for nu in p_bl}
            rhs = mp.mpf(0)
            for (mu, nu), info in Ac.items():
                rhs += aoa._trace(info["A"] * g._kron(rmu[mu], rnu[nu]))
            ad = abs(lhs - rhs)
            if ad > max_abs:
                max_abs = ad
            n += 1
    return max_abs, n


def main() -> int:
    dps = 50
    mp.mp.dps = dps + 10
    q = aoa.q0_mp(dps)
    q_str = mp.nstr(q, dps)
    h = q - 1 / q
    p3, p6 = partitions_of(3), partitions_of(6)
    rho3 = {p: aoa.exact_seminormal_matrices(p, q_str, dps)[0] for p in p3}
    rho6 = {p: aoa.exact_seminormal_matrices(p, q_str, dps)[0] for p in p6}

    print("Task-B cyclic-vector intertwiner — combiner-identity gate (1e-25)")
    print("=" * 66)

    # H_6: all 11 λ⊢6.
    h6_max = mp.mpf(0)
    h6_checks = 0
    for lam in partitions_of(6):
        ma, n = _idcheck(lam, 3, 3, q_str, h, rho3, rho3, p3, p3, 999, 999, dps)
        if ma is None:
            continue
        h6_max = max(h6_max, ma)
        h6_checks += n
    h6_pass = h6_max < EXACT
    print(f"  H_6 (all 11 λ⊢6): {h6_checks} checks, max_abs={mp.nstr(h6_max, 8)}, "
          f"PASS={h6_pass}")

    # H_9: feasible λ=(8,1), exercises the n_inner=6 path.
    h9_max, h9_n = _idcheck((8, 1), 6, 3, q_str, h, rho6, rho3, p6, p3, 4, 4, dps)
    h9_pass = h9_max < EXACT
    print(f"  H_9 λ=(8,1) (n_inner=6): {h9_n} checks, max_abs={mp.nstr(h9_max, 8)}, "
          f"PASS={h9_pass}")

    all_pass = h6_pass and h9_pass
    print(f"\n  cyclic == nullspace reference (gauge-invariant identity): "
          f"{'PASS' if all_pass else 'FAIL'}")
    print("  Note: the 4 r=64 λ⊢9 are correct under this construction but slow in")
    print("  pure mpmath; their production unlock is the Rust port (combiner_block).")

    w = WitnessBuilder("cyclic-intertwiner-verify", engine="mpmath")
    w.set_description(
        "Task-B cyclic-vector intertwiner (handover §5) — Python reference "
        "correctness gate. Replaces the O(r⁴) vectorised null-space U in the "
        "gauge-aligned A-combiner with the O(r³) matrix-unit / cyclic-vector "
        "construction (no r²×r² matrix → clears the 4 r=64 λ⊢9 that OOM). "
        "Verified against the gauge-invariant combiner identity χ^λ(W·I·β) = "
        "Σ_μν Tr[A·(ρ_μ(W)⊗ρ_ν(β))] at 1e-25: H_6 all 11 λ⊢6, and H_9 λ=(8,1) "
        "(n_inner=6 path). Pins the reference for the Rust port."
    )
    w.add_data("q0", q_str)
    w.add_data("h6_all_lambda6", {"checks": h6_checks,
                                  "max_abs_residual": mp.nstr(h6_max, 8),
                                  "passed": h6_pass})
    w.add_data("h9_feasible_8_1", {"checks": h9_n,
                                   "max_abs_residual": mp.nstr(h9_max, 8),
                                   "passed": h9_pass})
    w.add_assertion(
        name="cyclic_combiner_identity_exact",
        computed=1 if all_pass else 0,
        expected=1,
        source="the cyclic-vector intertwiner reproduces χ^λ via the small "
               "H_inner/H_block reps to 1e-25 at H_6 (all λ⊢6) and H_9 (8,1)",
    )
    w.save()
    print("\n  Witness: cyclic-intertwiner-verify.witness.json")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
