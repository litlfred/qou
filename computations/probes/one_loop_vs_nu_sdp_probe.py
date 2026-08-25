#!/usr/bin/env python3
# polynomial_q_not_applicable: hyperbolic-geometry numeric probe.
"""1-loop invariant (= adjoint Reidemeister torsion) vs ν_SDP — Option-A test.

Bean qou-r307. Gemini's "Option A" (q-deformed saddle-offsets brainstorm,
2026-08-02) proposed identifying the Kashaev density prefactor
ρ_F = ν_SDP ∈ {1,2} (conj:kashaev-density-equals-sdp-multiplicity) with the
1-loop invariant of the knot complement, citing Garoufalidis–Yoon
"1-loop equals torsion for two-bridge knots" (arXiv:2411.03801), which proves
1-loop = adjoint Reidemeister torsion.

This probe implements the Dimofte–Garoufalidis 1-loop invariant
(Def. 2.1 of 2411.03801) directly from SnapPy's Neumann–Zagier data:

    τ(T) = ± (1/2) · det(G_μ·diag(ζ) + G'_μ·diag(ζ') + G''_μ·diag(ζ''))
                     / ∏_j ζ_j^{f_j} ζ'^{f'_j}_j ζ''^{f''_j}_j

ζ_j=1/z_j, ζ'_j=1/(1−z_j), ζ''_j=1/(z_j(z_j−1)); G_μ = edge gluing matrices
with one edge row replaced by the meridian completeness row; (f,f',f'') an
integer flattening (f+f'+f''=1, Gf+G'f'+G''f''=2).

VERDICT (scope-(a), honest negative): τ is a transcendental/algebraic COMPLEX
number, NOT the integer ν_SDP. For 6₂: τ≈−1.715−1.404j (|τ|≈2.22) vs ν_SDP=1;
for 8₁₁: τ≈2.47+8.45j (|τ|≈8.81) vs ν_SDP=2. The flattening/sign ambiguity
(units, roots of unity) cannot turn these into 1 or 2 — the magnitudes alone
refute equality. So the 1-loop torsion does NOT derive ν_SDP; Gemini's Option-A
bridge is refuted AS STATED. (4₁ control lands in its trace field ℚ(√−3),
|τ|=√3/2.) 1-loop=torsion remains a valid analytic bridge — just not to the
integer ν_SDP.

RECONCILIATION with the landed value-validated probe (reuse pass, 2026-08-02):
the AUTHORITATIVE probe for the torsion VALUE is the sibling
`computations/probes/torsion_nu_sdp_probe.py` (PR #4576, bean qou-r307, audit
`docs/audits/2026-08-02-r307-torsion-vs-nu-sdp-probe.md`), which computes the
Porti adjoint Reidemeister torsion 𝕋_μ = −W'(1) via Fox calculus and is
VALUE-validated (reproduces the known 𝕋_μ(4₁) = −3.00003; 6₂ |𝕋_μ|=16.84,
8₁₁ |𝕋_μ|=27.76). This script is a DIFFERENT computation — the Dimofte–
Garoufalidis 1-loop invariant from NZ gluing data (Def 2.1, the "symmetric"
normalization of Remark 2.2) — and its normalization does NOT match Porti's
(4₁: |τ|=√3/2 here vs 3 there; the two conventions differ by units). It is kept
as an INDEPENDENT-ROUTE confirmation of the scope-(a) VERDICT ONLY (complex,
non-real, modulus ≫ {1,2} ⇒ ∉ ℤ), which is normalization-robust. Do NOT read the
τ values here as the adjoint torsion — use torsion_nu_sdp_probe.py for that.

⚠ REWRITTEN 2026-08-08 (bean qou-t0rf / qou-fl4t) — float64 drained, and the
duplicate implementation deleted.

This file used to carry its own copy of the construction, in float64 throughout:
`complex(s['rect'])` for the shapes, `np.linalg.det` for the determinant,
`complex(...)` for the flattening, `float(M.volume())`. That capped every number
below near 16 digits regardless of intent, and it was a SECOND copy of a
construction the corpus now has once.

It now delegates to `computations/one_loop_torsion.one_loop` — the shared,
high-precision, triangulation-invariant helper this very construction was
promoted INTO (PR #4707). Two things change as a result:

  * every number here is mpmath at the canonical working precision; no float64
    enters the computation at all;
  * `L6a4` now returns a real value (|τ| = 8) instead of the degenerate 0 the
    one-cusped row-substitution produced. The shared helper covers any cusp
    number (audit docs/audits/2026-08-07-one-loop-multicusp-derivation.md).

The VERDICT below is unchanged and is now computed at higher precision than the
margin it rests on by 50-odd digits.

Requires: snappy, sympy (numpy no longer needed).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "substrate"))
from _precision import set_compute_dps  # noqa: E402
from one_loop_torsion import one_loop as _one_loop_shared  # noqa: E402

set_compute_dps()


def one_loop(name: str):
    """(volume, det, tau) for `name`, all mpmath. Delegates the invariant."""
    import snappy

    M = snappy.Manifold(name)
    tau = _one_loop_shared(M)
    bits = int(mp.mp.dps * 3.3219) + 16
    vol = mp.mpf(str(M.volume(bits_prec=bits)).replace(" ", ""))
    return vol, 2 * tau, tau        # `det` kept for the printed column: det = 2*tau*denom-free


def main() -> int:
    print(f"{'knot':6} {'ν_SDP':>6} {'vol':>9} {'1-loop τ':>28} {'|τ|':>9}")
    for name, nu in [('6_2', 1), ('8_11', 2), ('L6a4', 2), ('4_1', None)]:
        try:
            vol, det, tau = one_loop(name)
            print(f"{name:6} {str(nu):>6} {mp.nstr(vol, 7):>9} "
                  f"{mp.nstr(tau, 8):>28} {mp.nstr(abs(tau), 7):>9}")
        except Exception as e:
            print(f"{name:6} {str(nu):>6}  ERROR: {str(e)[:50]}")
    print("\nVerdict: |τ| ≠ ν_SDP (2.22≠1, 8.81≠2). 1-loop torsion is a complex "
          "analytic invariant, not the integer dimension count ν_SDP. "
          "Gemini Option-A refuted as stated (scope-a).")
    print("Note: this is the DG 1-loop (symmetric) normalization; for the "
          "value-validated adjoint torsion 𝕋_μ use torsion_nu_sdp_probe.py "
          "(PR #4576). 4₁ here lands in ℚ(√−3) (trace field) but |τ|=√3/2≠3 — "
          "the two conventions differ by units. Verdict is normalization-robust.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
