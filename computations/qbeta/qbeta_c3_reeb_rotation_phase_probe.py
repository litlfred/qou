#!/usr/bin/env python3
"""qbeta_c3_reeb_rotation_phase_probe.py

"Keep pushing on arg(u(q₀)) using reeb": test whether the open phase of the c₃
bar-odd `S` wall (`S = Im 𝔙(u(q₀))`, residue = arg(u(q₀)); see
qbeta_c3_wall_branch_structure_probe.py) is the DERIVED q-Reeb rotation angle
θ of the figure-eight operator, rather than an unconstrained fit.

THE REEB OBJECT (derived, parameter-free; content block
`content/quantum-observable-universe/braids-and-knots/figure-eight-reeb-rotation.md`):
the figure-eight knot operator `M_{4₁} = (σ₀ σ₁⁻¹)²` acting on the 2-dim lepton
channel `V_{(2,1)}` of `H₃(q)` has eigenvalues `λ_{4₁} = e^{±iθ}`, `|λ|=1`. The
phase θ is the accumulated q-Reeb rotation angle (rotates between the symmetric
`V_{(2)}` and antisymmetric `V_{(1,1)}` lepton channels).

We build the 2×2 Hoefsmit SEMINORMAL block of σ₀, σ₁ on `V_{(2,1)}` directly
(σ₀ diagonal `diag(q, −q⁻¹)`; σ₁ solved from braid + Hecke; only EIGENVALUES of
`M_{4₁}` are used, which are gauge-invariant), then read θ(q₀).

RESULTS (all derived/computed; scope-(a); C14; no c_k wired; no fit of S):

  1. **|λ_{4₁}| = 1 CONFIRMED** — `det M_{4₁} = 1` (from `det σ_i = −1` via Hecke)
     and `|tr M_{4₁}| < 2` at q₀, so the eigenvalues lie on the unit circle. This
     VERIFIES the content block's Reeb claim `λ = e^{±iθ}` from the actual rep.

  2. **θ(q₀) = 117.0867°** at BOTH anchors (they differ only ~1e-8 in q₀), with
     the clean CLASSICAL anchor **θ(q=1) = 120° = 2π/3 EXACT**: at q=1 the block
     is the `S₃` rep and `(σ₀σ₁)²` is a 3-cycle (eigenvalue `e^{2πi/3}`). The
     closed form is `tr M_{4₁} = q⁴ − 2q² + 1 − 2q⁻² + q⁻⁴`, `tr(1) = −1`.

  3. **θ is SMOOTH (`dθ/dq ≈ −51°` per unit q, O(1)).** So θ is NOT the source of
     the `dc₃/dq ≈ 4.66×10⁶` hypersensitivity / the `S(muon)>0>S(proton)`
     sign-flip. As in the geometry-side + Kashaev probes, the anchor-dependent
     sign-flip requires the near-singular substrate→deformation map `q₀→u`
     (`conj:algebraic-geometric-dilog-equivalence`, open) — the wall.

  4. **What Reeb DOES contribute (derived seed, not the fit):** at q=1 the knot is
     amphichiral (`θ=120°`, `CS=0`, `S=0`). The q-deformation breaks amphichirality
     by `Δθ = θ(q₀) − 120° = −2.9133°` — a parameter-free measure of the
     symmetry-breaking that SEEDS the bar-odd `S`. So the wall's carrier phase has
     a derived geometric scale (Reeb θ ≈ 117°, ~O(the required arg u)); only the
     hypersensitive q₀-correction near the π/2 quadrant boundary stays open.

HONEST VERDICT: `arg(u(q₀)) = θ(q₀)` is a scope-(a) NEGATIVE (θ is anchor-smooth;
cannot produce the sign-flip). But θ is a derived phase of the right magnitude
with a clean classical anchor — it pins the wall's carrier scale and the seed of
S to geometry, narrowing the open content to the hypersensitive substrate map.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 50
Q = {"muon": mp.mpf("1.10997859555733471"),
     "proton": mp.mpf("1.1099785827513808075916690956107688798744991218736")}
# required arg(u) from the non-fitting branch-structure inversion (this session):
ARG_U_REQ_DEG = {"muon": mp.mpf("82.6"), "proton": mp.mpf("135.0")}


def seminormal_sigma(q):
    """2×2 Hoefsmit seminormal block of (σ₀, σ₁) on V_{(2,1)} of H₃(q).

    σ₀ = diag(q, −q⁻¹) (entries 1,2 share a row / a column in the two SYT);
    σ₁ solved from braid (σ₀σ₁σ₀=σ₁σ₀σ₁) + Hecke ((σ−q)(σ+q⁻¹)=0), gauge b=1.
    Only eigenvalues of products are used downstream (gauge-invariant).
    """
    s0 = mp.matrix([[q, 0], [0, -1 / q]])
    a = -1 / (q * (q ** 2 + 1))
    b = mp.mpf(1)
    c = (q ** 2 - q + 1) * (q ** 2 + q + 1) / (q ** 2 + 1) ** 2
    d = q ** 3 / (q ** 2 + 1)
    s1 = mp.matrix([[a, b], [c, d]])
    return s0, s1


def fig8_operator(q):
    """M_{4₁} = (σ₀ σ₁⁻¹)² on V_{(2,1)}."""
    s0, s1 = seminormal_sigma(q)
    s1i = s1 ** -1
    g = s0 * s1i
    return g * g


def theta_of(q):
    """q-Reeb rotation angle: arg of the M_{4₁} eigenvalue (|λ|=1 at real q₀)."""
    M = fig8_operator(q)
    tr = M[0, 0] + M[1, 1]
    return mp.acos(tr / 2)          # 2 cos θ = tr, eigenvalues e^{±iθ}


def main() -> int:
    print("=" * 78)
    print(" c₃ bar-odd S — q-Reeb rotation angle θ of the figure-eight operator")
    print("=" * 78)

    # ---- 1. verify the rep: braid, Hecke eigenvalues, det M = 1, |tr|<2 ----
    q_chk = Q["muon"]
    s0, s1 = seminormal_sigma(q_chk)
    braid = s0 * s1 * s0 - s1 * s0 * s1
    braid_ok = max(abs(braid[i, j]) for i in range(2) for j in range(2)) < mp.mpf("1e-40")
    # Hecke eigenvalues of σ₁: {q, −1/q}
    trs1, dets1 = s1[0, 0] + s1[1, 1], s1[0, 0] * s1[1, 1] - s1[0, 1] * s1[1, 0]
    hecke_ok = abs(trs1 - (q_chk - 1 / q_chk)) < mp.mpf("1e-40") and abs(dets1 + 1) < mp.mpf("1e-40")
    M = fig8_operator(q_chk)
    detM = M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
    trM = M[0, 0] + M[1, 1]
    print("\n[1] rep verification (V_{(2,1)} seminormal block):")
    print(f"    braid σ₀σ₁σ₀=σ₁σ₀σ₁ : {'OK' if braid_ok else 'FAIL'}")
    print(f"    Hecke eig(σ₁)={{q,−1/q}}: {'OK' if hecke_ok else 'FAIL'}")
    print(f"    det M_{{4₁}} = {mp.nstr(mp.re(detM),12)}  (=1 ⇒ eigenvalues λ,1/λ)")
    print(f"    tr  M_{{4₁}} = {mp.nstr(mp.re(trM),12)}   (|tr|<2 ⇒ |λ|=1, a rotation)")
    unit_circle = abs(mp.re(detM) - 1) < mp.mpf("1e-40") and abs(mp.re(trM)) < 2

    # ---- 2. θ at anchors + classical q=1 anchor + closed form ----
    print("\n[2] q-Reeb rotation angle θ = arg λ_{4₁}:")
    th1 = theta_of(mp.mpf(1))
    print(f"    θ(q=1)   = {mp.nstr(mp.degrees(th1),10)}°  (= 120 = 2π/3 exact; S₃ 3-cycle)")
    thetas = {}
    for a in ("muon", "proton"):
        thetas[a] = theta_of(Q[a])
        print(f"    θ({a:6s}) = {mp.nstr(mp.degrees(thetas[a]),10)}°   "
              f"(required arg u ≈ {mp.nstr(ARG_U_REQ_DEG[a],4)}°)")

    # closed-form trace: q^4 - 2q^2 + 1 - 2/q^2 + 1/q^4
    def tr_cf(q):
        return q ** 4 - 2 * q ** 2 + 1 - 2 / q ** 2 + 1 / q ** 4
    cf_ok = abs(tr_cf(q_chk) - mp.re(trM)) < mp.mpf("1e-40") and abs(tr_cf(mp.mpf(1)) + 1) < mp.mpf("1e-40")
    print(f"    closed form tr = q⁴−2q²+1−2q⁻²+q⁻⁴ matches: {'OK' if cf_ok else 'FAIL'}  (tr(1)=−1)")

    # ---- 3. smoothness: dθ/dq is O(1) ⇒ not the hypersensitive source ----
    h = mp.mpf("1e-20")
    dth = (theta_of(q_chk + h) - theta_of(q_chk - h)) / (2 * h)
    print("\n[3] smoothness:")
    print(f"    dθ/dq = {mp.nstr(mp.degrees(dth),8)}° per unit q  (O(1) ⇒ NOT the dc₃/dq≈4.66e6 source)")
    print(f"    θ(muon)−θ(proton) = {mp.nstr(mp.degrees(thetas['muon']-thetas['proton']),6)}°  (anchor-smooth)")

    # ---- 4. derived seed: amphichirality breaking Δθ ----
    dtheta = thetas["muon"] - th1
    print("\n[4] derived seed (Reeb's real contribution):")
    print(f"    Δθ = θ(q₀) − 120° = {mp.nstr(mp.degrees(dtheta),8)}°  "
          "(q-deformation breaks 4₁ amphichirality ⇒ seeds S≠0)")

    # ---- 5. degeneration loci = figure-eight geometric special points ----
    print("\n[5] Reeb degeneration loci (tr M=±2, θ=0/π) = fig-8 special points:")
    phi = (1 + mp.sqrt(5)) / 2
    tr_phi = phi ** 4 - 2 * phi ** 2 + 1 - 2 / phi ** 2 + 1 / phi ** 4
    omega = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)          # cusp shape, root of Φ₆
    q_cusp = mp.sqrt(omega)
    tr_cusp = q_cusp ** 4 - 2 * q_cusp ** 2 + 1 - 2 / q_cusp ** 2 + 1 / q_cusp ** 4
    golden_ok = abs(tr_phi - 2) < mp.mpf("1e-30")
    cusp_ok = abs(tr_cusp + 2) < mp.mpf("1e-30")
    print(f"    θ=0 (tr=+2) at q=φ={mp.nstr(phi,8)} (golden ratio): tr(φ)={mp.nstr(tr_phi,8)}  {'OK' if golden_ok else 'FAIL'}")
    print(f"    θ=π (tr=−2) at q²=ω=e^(iπ/3) (cusp shape): tr(√ω)={mp.nstr(mp.re(tr_cusp),6)}  {'OK' if cusp_ok else 'FAIL'}")
    print("    exact identities: tr+2=(q²−1+q⁻²)² (⇒tr≥−2 real); tr−2=(q²−q−1)(q²+q−1)(q²−q+1)(q²+q+1)/q⁴")
    print("    ⇒ operator-θ shares degeneration loci with the A-poly/cusp geometry (#3573/#3579).")

    # honest gate: arg(u)=θ requires match at BOTH anchors AND sign-flip capacity
    match = all(abs(mp.degrees(thetas[a]) - ARG_U_REQ_DEG[a]) < 5 for a in ("muon", "proton"))
    print("\n VERDICT:", "arg(u)=θ CANDIDATE" if match else
          "arg(u)=θ scope-(a) NEGATIVE — θ derived & O(right magnitude) but anchor-smooth;")
    if not match:
        print("          the sign-flip needs the open substrate→u map. Reeb pins the carrier")
        print("          phase scale (θ≈117°) + the S seed (Δθ), not the hypersensitive residue.")

    wb = WitnessBuilder("qbeta-c3-reeb-rotation-phase", engine="mpmath")
    wb.set_description(
        "q-Reeb rotation angle θ of the figure-eight operator M_{4₁}=(σ₀σ₁⁻¹)² on "
        "V_{(2,1)} of H₃(q), built from the 2×2 Hoefsmit seminormal block "
        "(gauge-invariant eigenvalues). Verified: braid+Hecke hold, det M=1, "
        "|tr M|<2 ⇒ |λ_{4₁}|=1 (confirms the content block's Reeb claim). "
        "θ(q₀)=117.087° at both anchors; θ(1)=120°=2π/3 exact (S₃ 3-cycle); "
        "closed form tr=q⁴−2q²+1−2q⁻²+q⁻⁴. θ is SMOOTH (dθ/dq≈−51°/unit q) ⇒ NOT "
        "the dc₃/dq≈4.66e6 sign-flip source (the open q₀→u map is). Reeb's real "
        "contribution: Δθ=θ(q₀)−120°=−2.913° is the derived amphichirality-breaking "
        "seed of S. Scope-(a); C14; no c_k wired; no fit; arg(u)=θ negative."
    )
    wb.set_content_block("prop:phi-b-unitary-bar-odd")
    wb.add_data("rep_verification", {
        "braid_ok": bool(braid_ok), "hecke_ok": bool(hecke_ok),
        "det_M": mp.nstr(mp.re(detM), 12), "tr_M_q0": mp.nstr(mp.re(trM), 12),
        "unit_circle": bool(unit_circle), "closed_form_ok": bool(cf_ok)})
    wb.add_data("theta_deg", {
        "q_eq_1": mp.nstr(mp.degrees(th1), 12),
        "muon": mp.nstr(mp.degrees(thetas["muon"]), 12),
        "proton": mp.nstr(mp.degrees(thetas["proton"]), 12),
        "required_arg_u": {a: mp.nstr(ARG_U_REQ_DEG[a], 6) for a in Q}})
    wb.add_data("smoothness", {"dtheta_dq_deg": mp.nstr(mp.degrees(dth), 8),
                               "anchor_split_deg": mp.nstr(mp.degrees(thetas["muon"] - thetas["proton"]), 6)})
    wb.add_data("amphichirality_seed", {"delta_theta_deg": mp.nstr(mp.degrees(dtheta), 8),
                                        "classical_theta_deg": "120", "cs_at_q1": "0"})
    wb.add_data("verdict", "arg_u_eq_theta_candidate" if match else "arg_u_eq_theta_scope_a_negative")
    # assert the derived facts that ARE established (not the open map)
    wb.add_assertion("fig8_eigenvalue_unit_modulus",
                     computed=1.0 if unit_circle else 0.0, expected=1.0, tolerance=0.5,
                     source="det M_{4₁}=1 and |tr M_{4₁}|<2 at q₀ (seminormal V_{(2,1)} block)")
    wb.add_assertion("theta_classical_2pi_over_3",
                     computed=float(mp.degrees(th1)), expected=120.0, tolerance=1e-6,
                     source="θ(q=1)=120°: (σ₀σ₁)² is an S₃ 3-cycle, eigenvalue e^{2πi/3}")
    wb.add_data("degeneration_loci", {
        "theta_0_at_golden": {"q": mp.nstr(phi, 12), "tr": mp.nstr(tr_phi, 12), "ok": bool(golden_ok)},
        "theta_pi_at_cusp": {"q_sq": "e^{i pi/3} (Phi_6 root)", "tr": mp.nstr(mp.re(tr_cusp), 8), "ok": bool(cusp_ok)},
        "identities": ["tr+2=(q^2-1+q^-2)^2", "tr-2=(q^2-q-1)(q^2+q-1)(q^2-q+1)(q^2+q+1)/q^4"]})
    wb.add_assertion("reeb_degenerates_at_golden_ratio",
                     computed=1.0 if golden_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="tr M_{4_1}(phi)=2 (theta=0): the Reeb rotation degenerates at the golden ratio = A-poly branch point u=2 ln phi")
    wb.add_assertion("reeb_degenerates_at_cusp_shape",
                     computed=1.0 if cusp_ok else 0.0, expected=1.0, tolerance=0.5,
                     source="tr M_{4_1}(sqrt(omega))=-2 (theta=pi) at q^2=omega=e^{i pi/3}, the figure-8 cusp shape (Phi_6 root, barEven=1/barOdd^2=-3)")
    wb.save()

    print("\n  RESULT: Reeb θ derived (117.087°, θ(1)=120° exact); arg(u)=θ negative (smooth);")
    print("          θ pins the wall's carrier scale + the S seed Δθ, not the open residue.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
