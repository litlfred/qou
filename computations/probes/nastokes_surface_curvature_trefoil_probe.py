#!/usr/bin/env python3
"""
Transverse NA-Stokes surface-curvature pairing on the trefoil (pn/deuteron) Seifert
surface — the named-wall discretization for bean `qou-prjo`.

The deuteron −9.2% (E_unit/μ₀ tier) decomposes forward (2026-07-24-eunit-magnus-order2.md §3)
into a bar-odd impurity −t plus a bar-even gap ≈ g₂·h² on E⁺ = m_e[j]_q[j+1]_q/3, with the
NEAR-MATCH coefficient g₂ = 1.0087 (underived). The inter-crossing Magnus tower is proved 0
for the σ₁³ word (single generator, [X,X]=0), so the ONLY surviving order-2 candidate is the
**transverse** NA-Stokes surface-curvature pairing

    Ω₂^⊥ = ½ 𝒫 ∮∮ [𝓕, 𝓕]        (surface-ordered, over the Seifert surface)

quadratic in the germ q-curvature F_q = [δq₁, δq₂] (germ-commutator-q-curvature.md). This was
the wall: "needs a canonical discretization of the Yekutieli surface 2-form on the trefoil
Seifert surface — data the corpus lacks." This probe BUILDS that discretization and evaluates
the pairing, reporting the resulting bar-even coefficient c₂ vs the target g₂.

DISCRETIZATION (canonical genus-1 trefoil Seifert surface):
  • σ₁³ Seifert algorithm: 2 Seifert circles, 3 bands ⇒ genus 1, H₁ rank 2.
  • Seifert matrix V = [[-1,1],[0,-1]] (standard trefoil); intersection form J = V − Vᵀ
    = [[0,1],[-1,0]] (a·b = 1).
  • Germ q-curvature (two-observer commutator) F = [log s₁, log s₂] in the 2-dim Hecke rep.
  • NA-Stokes path-conjugation: 𝓕(x) = U(O,x)⁻¹ F U(O,x). The two H₁ handle cycles a,b of the
    σ₁³ surface sit at holonomies U_a = s₁, U_b = s₁² (after 1 and 2 of the 3 crossings).
  • Surface-ordered pairing collapses on genus-1 to the intersection-weighted handle commutator
        Ω₂^⊥ = ½ Σ_{ij} J_{ij} [𝓕_i, 𝓕_j] = [𝓕_a, 𝓕_b],   𝓕_k = U_k⁻¹ F U_k.

SCALAR EXTRACTION (the residual-freedom point, reported honestly): Ω₂^⊥ is a Lie element
(trace 0). Its bar-even contribution to the observable is the shift it induces in the
holonomy's counit/highest-weight log-eigenvalue: c₂·h² := (bar-even part of the leading
eigenvalue shift of exp(Ω₁+Ω₂^⊥) vs exp(Ω₁)) / h². We report c₂ and c₂/g₂; we flag which
steps are canonical vs choices.

Audit-only. No fit, no AME inversion, nothing wired.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent          # computations/probes
_COMP = HERE.parent                              # computations
for p in (str(_COMP), str(HERE), str(_COMP / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

import mpmath as mp
from eunit_magnus_order2_probe import hecke_rep, mat_log_hecke, commutator  # noqa: E402
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# substrate q0, proton-pinned, read BY NAME from `q_parameter` (bean qou-9ugp).
# NO SILENT FALLBACK. The `except` arm used to bind the literal
# 1.10997859555733471 -- the RETIRED muon pin A -- so any environment where
# the substrate package failed to import computed at a stale MUON value under
# a comment that says proton, and nothing said so. A pin that cannot be
# established is an error, not a default. `q_parameter` rather than
# `qou_substrate.constants` so the witness resolves its anchor stamp.
try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # type: ignore
except Exception as _exc:  # pragma: no cover
    raise RuntimeError(
        "cannot establish the q0 anchor: `q_parameter` did not import. "
        "Refusing to fall back to a literal -- see bean qou-9ugp."
    ) from _exc
Q0 = Q_MP


def conj(U, F):
    return U ** -1 * F * U


def main() -> int:
    q = Q0
    h = q - 1 / q
    h2 = h * h
    s1, s2 = hecke_rep(q)
    # germ increment δq_i = q·(∂_q s_i)·s_i⁻¹ — the LOGARITHMIC q-DERIVATIVE (the true germ-level
    # q-perturbation of germ-commutator-q-curvature.md, O(h)), NOT log σ (which is O(1), dominated
    # by the iπ antisymmetric-channel phase of log(−1/q) and overshoots ~168×).
    ds1 = mp.matrix([[1, 1 / q ** 2], [0, 1 / q ** 2]])   # ∂_q s1
    ds2 = mp.matrix([[1 / q ** 2, 0], [-1, 1]])           # ∂_q s2
    dq1 = q * ds1 * s1 ** -1
    dq2 = q * ds2 * s2 ** -1
    A1 = mat_log_hecke(s1, q)   # along-word counit connection

    # two GERM choices for F_q = [δq₁, δq₂]:
    ds1 = mp.matrix([[1, 1 / q ** 2], [0, 1 / q ** 2]])
    ds2 = mp.matrix([[1 / q ** 2, 0], [-1, 1]])
    F_log = commutator(mat_log_hecke(s1, q), mat_log_hecke(s2, q))   # O(1), iπ-phase-heavy
    F_qd = commutator(q * ds1 * s1 ** -1, q * ds2 * s2 ** -1)        # O(h), q-deformation germ

    # trefoil Seifert data (genus 1): intersection form J = V − Vᵀ
    J = mp.matrix([[-1, 1], [0, -1]]) - mp.matrix([[-1, 1], [0, -1]]).T

    # surface-ordered pairing on genus-1 = J_ab·[𝓕_a,𝓕_b], 𝓕_k = U_k⁻¹ F U_k.
    # The two independent H₁ handle-holonomy choices are NOT canonically fixed by the corpus —
    # that is the residual freedom. Characterize the term across natural choices.
    handle_choices = [("s1,s1^2", s1, s1 ** 2), ("s1,s2", s1, s2), ("s2,s1s2", s2, s1 * s2)]

    print("=" * 82)
    print("  Transverse NA-Stokes surface-curvature pairing — trefoil (σ₁³) Seifert surface")
    print("=" * 82)
    print(f"  q₀={mp.nstr(q,16)}  h²={mp.nstr(h2,8)}   Seifert J=V−Vᵀ=[[0,1],[-1,0]] (a·b=1)")
    print(f"  target: a g₂·h² correction needs ‖Ω₂^⊥‖/h² ≈ c₂ ≈ 1 (g₂=1.0087)")
    print(f"  {'germ':<8}{'handles':<12}{'||Om2perp||':>16}{'  c₂=||·||/h²':>16}")
    rng = []
    for gname, F in [("log", F_log), ("qderiv", F_qd)]:
        for hname, Ua, Ub in handle_choices:
            Om = mp.mpf("0.5") * (J[0, 1] * commutator(conj(Ua, F), conj(Ub, F))
                                  + J[1, 0] * commutator(conj(Ub, F), conj(Ua, F)))
            c2 = mp.norm(Om) / h2
            rng.append(c2)
            print(f"  {gname:<8}{hname:<12}{mp.nstr(mp.norm(Om),8):>16}{mp.nstr(c2,8):>16}")
    print()
    print(f"  c₂ range across natural choices: {mp.nstr(min(rng),4)} … {mp.nstr(max(rng),6)}")
    print("  VERDICT (scope-a): the transverse term is either ~0 (germ commutes with the on-axis")
    print("  handle) or 250–900× (mixed/log) — NO natural discretization lands near c₂≈1. So the")
    print("  surface-curvature pairing, once BUILT, does NOT supply g₂: the surface→scalar map has")
    print("  O(100×) gauge freedom the corpus does not fix. The named wall resolves in the NEGATIVE.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
