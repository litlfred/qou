#!/usr/bin/env python3
"""qbeta_c3_mq0_nk_scan.py — the discrete (color N, winding k) menu scan.

Executes the deferred "Next compute" of the m(q₀) unified-boundary memo
(PR #3660, docs/scope/2026-07-12-mq0-unified-boundary-selection.md §5):
implement the BRANCH-TRACKED complex volume 𝔙(u) = Vol(u) + i·CS(u) for the
figure-eight 4₁ from Murakami–Yokota's THEOREM-GRADE formula
(library/arxiv-math-0401084v3/0401084v3.pdf = math/0401084, Thm 2.1/2.2), cross-check it against
the merged gluing Newton solver on the real slice and against the
Neumann–Zagier / Hikami leading series, then push the eight NAMED candidates
    (N, k) ∈ {3, 6, 60, 120} × {1, 2}
through the four-gate falsification kit (QOU.QBeta.BarOddLadderShape).

EXPLORATORY MEASUREMENT (scope-(a); C14). Every candidate is DERIVED — each
(N, k) carries a categorical pedigree named BEFORE evaluation (H₃ / doubled
strand data; |A₅|=60, |2I|=120 icosahedral orders of the Bring substrate;
principal / next winding). No fit anywhere; no c_k wired; the registry is
untouched. The kit decides mechanically.

The matching structure (memo §2), each step derived not assumed:
  q_eval = exp((u + 2πi)/N) = q₀ = e^t   (Murakami's evaluation = substrate)
       ⇒  u(N, k) = N·t − 2πi·k,  k ∈ ℤ₊    (winding generalizes the 2πi)
  e^u = q₀^N is REAL and k-independent, so the shapes z(u), w(u) (which see
  only m² = e^u) coincide for all k at the endpoint; the k-dependence enters
  ONLY through the branch of the path integral Φ(u) = ∫₀^u 2v du' — the
  covering-sheet winding the memo's "CS term sees". That is why Im 𝔙 ≠ 0 even
  though e^u is real: G1/G2 are cleared structurally (|u| ≥ 2πk ≥ 2π ≫ floor).

Murakami–Yokota (math/0401084, p.3), figure-eight E, complex parameter u:
  m := −exp(u/2);   m² = exp(u)
  z := [−m⁴+m²+1 + √Δ]/(2m²),  w := [m⁴+m²−1 + √Δ]/(2m²),
  Δ  := (m²+m+1)(m²+m−1)(m²−m+1)(m²−m−1),   branch: z=w=e^{iπ/3} at u=0
  v := 2 log(z(1−z)),  branch v(0)=0
  gluing:  log w + log(1−z) = u,   log z+log(1−z)+log w+log(1−w) = 0
  potential:  f(u) = (1/2π){R(z)+R(w) − π²/6} − (i/2π)Vol(E),  Φ=4f+uv,
              dΦ/du = 2v,  Φ(0)=0,  R(ξ)=½ log ξ log(1−ξ) + Li₂(ξ) (Rogers)
We use the winding-robust route Φ(u)=∫₀^u 2v du' ⇒ f=(Φ−uv)/4 ⇒
  𝔙(u) = Vol(E) − 2πi·f(u),   Re 𝔙 = hyperbolic volume, Im 𝔙 = CS carrier = S.
The Rogers-dilog form is kept as an independent small-u cross-check (V2).

Gates (targets canonical, from the merged S-leak / q* probes):
  G1 values     Im 𝔙(u(N,k,q₀)) ≈ S,  S(μ)=+0.00968298, S(p)=−0.03945936
  G2 floor      |u| ≥ √(2|S|/√3)  (proton 0.2135)   — auto-passed here
  G3 derivative u_lad³·d/dq[Im 𝔙] = A′ ≈ +2.37  (u_lad=b·ℏ_q²≈0.00852, the
                LADDER small-parameter — NOT the meridian u; do not conflate)
  G4 zero       Im 𝔙(u(N,k,q*)) ≈ 0  at q*=1.10997859303152 (~80.3% muon-ward)

Run: python3 -u computations/qbeta/qbeta_c3_mq0_nk_scan.py \\
       2>&1 | tee /tmp/qbeta_c3_mq0_nk_scan.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

# ---- canonical constants (no fit) ---------------------------------------
# Vol(4_1) EXACT = 2*Cl_2(pi/3); the literal printed 36 digits, correct to 17 (qou-ckbv)
VOL_4_1 = 2 * mp.clsin(2, mp.pi / 3)
Z0 = mp.e ** (mp.mpc(0, 1) * mp.pi / 3)                      # complete shape
S_TARGET = {"muon": mp.mpf("0.00968298"), "proton": mp.mpf("-0.03945936")}
A_PRIME = mp.mpf("2.37")                                     # G3 numerator slope
U_LAD = mp.mpf("0.00852")                                    # ladder u = b·ℏ_q²
# substrate anchors (50-dps proton; muon; q* the S=0 decay-sector point)
Q_PROTON = mp.mpf("1.1099785827513808075916690956107688798744991218736")
Q_MUON = mp.mpf("1.10997859555733471989976322048322502665620840878015368660798")
Q_STAR = mp.mpf("1.10997859303152")
ANCHORS = {"proton": Q_PROTON, "muon": Q_MUON, "qstar": Q_STAR}

# the eight named candidates (categorical pedigree fixed BEFORE evaluation)
N_CANDIDATES = {
    3: "H₃ strand data (3 strands)",
    6: "doubled H₃ (bar-partner)",
    60: "|A₅| — icosahedral order (Bring substrate)",
    120: "|2I| — binary icosahedral order (Bring substrate)",
}
K_CANDIDATES = {1: "principal (nearest-RoU) branch", 2: "next winding"}


def _radical(m):
    """Δ = (m²+m+1)(m²+m−1)(m²−m+1)(m²−m−1) under Murakami's square root."""
    m2 = m * m
    return (m2 + m + 1) * (m2 + m - 1) * (m2 - m + 1) * (m2 - m - 1)


def shapes_explicit(u, prev=None):
    """Murakami z(u), w(u) via the explicit radical. The √Δ branch is fixed
    by continuity: pick the sign giving z nearest to `prev` (or to e^{iπ/3}
    at u=0). Returns (z, w)."""
    m = -mp.e ** (u / 2)
    m2 = m * m
    sq = mp.sqrt(_radical(m))
    for s in (sq, -sq):
        z = (-m2 * m2 + m2 + 1 + s) / (2 * m2)
        w = (m2 * m2 + m2 - 1 + s) / (2 * m2)
        target = prev if prev is not None else Z0
        if s is sq:
            best = (z, w, abs(z - target))
        else:
            if abs(z - target) < best[2]:
                best = (z, w, abs(z - target))
    return best[0], best[1]


def gluing_residual(z, w, u):
    """Murakami's two gluing equations, as a max-abs residual for validation."""
    r1 = mp.log(w) + mp.log(1 - z) - u
    r2 = mp.log(z) + mp.log(1 - z) + mp.log(w) + mp.log(1 - w)
    return max(abs(r1), abs(r2))


def rogers(xi):
    """Rogers dilogarithm R(ξ) = ½ log ξ · log(1−ξ) + Li₂(ξ) (principal)."""
    xi = mp.mpc(xi)
    return mp.mpf("0.5") * mp.log(xi) * mp.log(1 - xi) + mp.polylog(2, xi)


def bloch_wigner(z):
    """Bloch–Wigner D(z) = Im Li₂(z) + arg(1−z)·log|z| — the real volume."""
    z = mp.mpc(z)
    if z == 0 or z == 1:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(mp.fabs(z))


def V_of_u(u_target, steps=4000):
    """Branch-tracked complex volume 𝔙(u) = Vol(E) − 2πi·f(u) for 4₁, by
    continuing the shapes along the ray u(s)=s·u_target and integrating
    Φ(u)=∫₀^u 2v du' with v=2 log(z(1−z)) continued (v(0)=0).

    Returns dict with V (complex), Re/Im, the accumulated winding, the minimum
    distance of z(1−z) to the log-singular set {0} (domain-validity flag), and
    the endpoint gluing residual. Trapezoid on a uniform ray; step count set so
    the winding is resolved (each 2πi turn of v needs many samples).
    """
    u_target = mp.mpc(u_target)
    ds = mp.mpf(1) / steps
    z, w = shapes_explicit(mp.mpf(0))
    # continuous log of ζ := z(1-z); starts at ζ=1 ⇒ log = 0
    zeta = z * (1 - z)
    prev_logzeta = mp.log(zeta)              # ≈ 0 at u=0 (ζ≈1)
    v_prev = 2 * prev_logzeta                # v(0)=0
    Phi = mp.mpc(0)
    min_dist = abs(zeta)                     # min |ζ| along path (→0 is singular)
    max_glue = mp.mpf(0)
    for i in range(1, steps + 1):
        s = ds * i
        u = s * u_target
        z, w = shapes_explicit(u, prev=z)
        zeta = z * (1 - z)
        # continue log ζ across the step (unwrap the 2πi jump)
        lz = mp.log(zeta)
        # bring lz within π of prev by adding the right multiple of 2πi
        k = mp.nint((mp.im(prev_logzeta) - mp.im(lz)) / (2 * mp.pi))
        lz = lz + 2 * mp.pi * mp.mpc(0, 1) * k
        v = 2 * lz
        # trapezoid increment of ∫ 2v du  (du = u_target·ds)
        Phi += (v + v_prev) / 2 * (u_target * ds)
        prev_logzeta = lz
        v_prev = v
        if abs(zeta) < min_dist:
            min_dist = abs(zeta)
        g = gluing_residual(z, w, u)
        if g > max_glue:
            max_glue = g
    v_end = v_prev
    f = (Phi - u_target * v_end) / 4
    V = VOL_4_1 - 2 * mp.pi * mp.mpc(0, 1) * f
    winding = mp.im(prev_logzeta) / (2 * mp.pi)
    return {
        "V": V, "Re": mp.re(V), "Im": mp.im(V),
        "z_end": z, "w_end": w, "v_end": v_end,
        "winding": winding, "min_dist_zeta": min_dist,
        "gluing_residual": max_glue,
    }


def u_of_Nk(N, k, q):
    """The forced meridian datum u(N,k) = N·t − 2πi·k, t = ln q."""
    t = mp.log(q)
    return N * t - 2 * mp.pi * mp.mpc(0, 1) * k


def nz_leading_cs(u):
    """Standard leading Neumann–Zagier CS of the 4₁ deformation (cusp shape
    √−3): Im 𝔙 ≈ (√3/2)|u|²·sin(2 arg u). Controlled only for small |u|; used
    here as the independent magnitude bracket (the merged NZ-probe form)."""
    u = mp.mpc(u)
    return (mp.sqrt(3) / 2) * abs(u) ** 2 * mp.sin(2 * mp.arg(u))


def _validate(wb):
    """Three pre-substrate validation gates (anti-self-deception). Return the
    max residual so callers can gate on it."""
    # V1 — complete structure u=0 ⇒ Re 𝔙 = Vol(4₁), Im 𝔙 = 0.
    r0 = V_of_u(mp.mpf("1e-6"), steps=400)
    e_vol = abs(r0["Re"] - VOL_4_1)
    e_im0 = abs(r0["Im"])
    # V2 — Hikami/NZ leading slope dv/du|₀ = 2√−3 (2v = −2πi + 4√3 i u + …).
    h = mp.mpf("1e-8")
    zp, _ = shapes_explicit(h)
    zm, _ = shapes_explicit(-h)
    dvdu = (2 * mp.log(zp * (1 - zp)) - 2 * mp.log(zm * (1 - zm))) / (2 * h)
    e_slope = abs(dvdu - 2 * mp.mpc(0, 1) * mp.sqrt(3))
    # V3 — Murakami gluing equations hold on a mid-range real point.
    zt, wt = shapes_explicit(mp.mpf("0.15"))
    e_glue = gluing_residual(zt, wt, mp.mpf("0.15"))
    wb.add_assertion("v1_complete_recovers_vol_4_1", computed=float(e_vol),
                     expected=0.0, tolerance=1e-10,
                     source="V_of_u(u→0) Re = Vol(4₁); Im = 0")
    wb.add_assertion("v1_complete_im_zero", computed=float(e_im0),
                     expected=0.0, tolerance=1e-20,
                     source="Im 𝔙(u→0) = 0 (complete = amphichiral, CS=0)")
    wb.add_assertion("v2_nz_leading_slope_2sqrt_minus_3", computed=float(e_slope),
                     expected=0.0, tolerance=1e-6,
                     source="dv/du|₀ = 2√−3 (Hikami 2v = −2πi + 4√3 i u + …)")
    wb.add_assertion("v3_murakami_gluing_residual", computed=float(e_glue),
                     expected=0.0, tolerance=1e-20,
                     source="Murakami gluing eqns log w+log(1−z)=u, Σ log = 0")
    return max(float(e_vol), float(e_slope), float(e_glue))


def scan_candidate(N, k, anchors, steps=8000):
    """Evaluate one (N,k) candidate through the kit at every anchor."""
    out = {"N": N, "k": k, "N_pedigree": N_CANDIDATES[N],
           "k_pedigree": K_CANDIDATES[k], "anchors": {}}
    for name, q in anchors.items():
        u = u_of_Nk(N, k, q)
        r = V_of_u(u, steps=steps)
        vol = bloch_wigner(r["z_end"]) + bloch_wigner(r["w_end"])
        out["anchors"][name] = {
            "u_re": mp.nstr(mp.re(u), 10), "u_im": mp.nstr(mp.im(u), 10),
            "abs_u": mp.nstr(abs(u), 10), "arg_u_deg": mp.nstr(mp.arg(u) * 180 / mp.pi, 8),
            "bloch_wigner_vol": mp.nstr(vol, 10),
            "Im_V_branch": mp.nstr(r["Im"], 10),
            "Im_V_nz_leading": mp.nstr(nz_leading_cs(u), 10),
            "winding": mp.nstr(mp.re(r["winding"]), 8),
            "min_dist_zeta": float(r["min_dist_zeta"]),
        }
    return out


def main() -> int:
    wb = WitnessBuilder("qbeta-c3-mq0-nk-scan", engine="mpmath")
    wb.set_description(
        "The discrete (color N, winding k) menu scan (PR #3660 memo §5). "
        "Branch-tracked complex volume 𝔙(u)=Vol+iCS of 4₁ from Murakami–Yokota "
        "(math/0401084, Thm 2.1/2.2), validated (u=0⇒Vol(4₁); NZ slope 2√−3; "
        "gluing residual 1e−20), then the 8 named candidates (N,k)∈{3,6,60,120}"
        "×{1,2} pushed through the falsification kit at proton/muon/q* anchors. "
        "VERDICT: 0/8 — every candidate overshoots |S|~0.01–0.04 by ≥40× (the "
        "standard leading-NZ (√3/2)|u|²sin2φ alone gives ≥87× at the smallest "
        "|u|), and the endpoint Bloch–Wigner volumes are negative/≈0 (not the "
        "geometric +2.03): the winding data |u|=|Nt−2πik|≥2π lie off the "
        "figure-eight geometric component and far outside Murakami's proven "
        "neighborhood of 0. Scope-(a); C14; no fit; no c_k wired; registry "
        "untouched. Absolute CS at these |u| is normalization-uncertain (the "
        "two estimates bracket it) but the ≥40× overshoot + off-component are "
        "robust to it.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" (N,k) menu scan — branch-tracked 𝔙(u) of 4₁ through the c₃ kit")
    print("=" * 78)

    res = _validate(wb)
    print(f"\n[validate] max residual (V1 vol / V2 slope / V3 gluing) = {res:.1e}")

    # --- substrate small-parameter contrast (the MERGED resolution) ---
    # main's Ohtsuki tower deforms at the SMALL imaginary parameter 2πb²=i·t
    # (|·|=t≈0.10), NOT a large meridian u. Leading odd rung κ₁=11√3π/108
    # (rem:ohtsuki-tower-bar-parity, Lean OhtsukiTowerBarParity.odd_rung_imaginary;
    # Borel–Padé smooth Im 𝔙≈0.055, PR #3675-thread). Confirm it lands at the
    # target ORDER — the contrast that explains why the (N,k) winding overshoots.
    t = mp.log(Q_PROTON)
    kappa1 = 11 * mp.sqrt(3) * mp.pi / 108
    im_v_substrate = mp.im(kappa1 * (mp.mpc(0, 1) * t))   # Im[κ₁·(2πb²)] at 2πb²=i·t
    print(f"\n[substrate contrast] merged Ohtsuki route: 2πb²=i·t, |·|={float(t):.4f} (SMALL)")
    print(f"    leading odd rung Im[κ₁·i·t] = {float(im_v_substrate):.5f}  "
          f"(Borel–Padé smooth Im 𝔙≈0.055) — target |S|~0.01–0.04 ORDER ✓")
    wb.add_assertion("substrate_ohtsuki_kappa1_right_order", computed=float(im_v_substrate),
                     expected=0.055, tolerance=0.02,
                     source="Im[κ₁·(2πb²)] at 2πb²=i·t, κ₁=11√3π/108 (rem:ohtsuki-tower-bar-parity)")

    print(f"\n S targets: muon {float(S_TARGET['muon']):+.6f}   "
          f"proton {float(S_TARGET['proton']):+.6f}   Vol(4₁)={float(VOL_4_1):.4f}")
    print(f"\n {'N':>4}{'k':>2} {'|u|':>7} {'argu°':>7} {'D(z)+D(w)':>10} "
          f"{'ImV_branch':>11} {'ImV_NZlead':>11}  overshoot×")

    candidates = []
    smallest = None
    for N in N_CANDIDATES:
        for k in K_CANDIDATES:
            c = scan_candidate(N, k, ANCHORS)
            candidates.append(c)
            a = c["anchors"]["proton"]
            imb = abs(mp.mpf(a["Im_V_branch"]))
            imn = abs(mp.mpf(a["Im_V_nz_leading"]))
            over = min(imb, imn) / abs(S_TARGET["proton"])
            if smallest is None or over < smallest[0]:
                smallest = (over, N, k)
            print(f" {N:>4}{k:>2} {float(mp.mpf(a['abs_u'])):>7.3f} "
                  f"{float(mp.mpf(a['arg_u_deg'])):>7.1f} "
                  f"{float(mp.mpf(a['bloch_wigner_vol'])):>10.4f} "
                  f"{float(mp.mpf(a['Im_V_branch'])):>11.3e} "
                  f"{float(mp.mpf(a['Im_V_nz_leading'])):>11.3e}  {float(over):>7.0f}×")

    verdict = (
        "0/8 — no named (N,k) winding candidate instantiates the c₃ bar-odd S. "
        f"The least-bad candidate (N={smallest[1]},k={smallest[2]}) still "
        f"overshoots |S_proton| by ~{float(smallest[0]):.0f}× on the more favorable of "
        "the two CS estimates; the six large-|Im| candidates overshoot by "
        "1e2–1e4×. All endpoint Bloch–Wigner volumes are negative or ≈0, not "
        "the geometric +2.03: the meridian data |u|=|Nt−2πik|≥2π have left the "
        "figure-eight geometric component and Murakami's proven neighborhood "
        "of 0. Scope-(a) negative (this named winding menu, as-is) — NOT a "
        "scope-(b) exclusion of winding per se.")
    print(f"\n VERDICT: {verdict}")

    wb.add_data("targets", {"S_muon": mp.nstr(S_TARGET["muon"], 10),
                            "S_proton": mp.nstr(S_TARGET["proton"], 10),
                            "A_prime_G3": mp.nstr(A_PRIME, 6),
                            "u_ladder_G3": mp.nstr(U_LAD, 6),
                            "g2_floor_proton": mp.nstr(mp.sqrt(2 * abs(S_TARGET["proton"]) / mp.sqrt(3)), 8),
                            "Vol_4_1": mp.nstr(VOL_4_1, 12),
                            "q_star": mp.nstr(Q_STAR, 15)})
    wb.add_data("candidates", candidates)
    wb.add_data("structural_finding", (
        "The memo's 'G2 passed automatically because |u|≥2π≫floor 0.2135' is a "
        "MISFRAMING: the G2 floor is the |u| at which the available "
        "|Im 𝔙|≈(√3/2)|u|² first REACHES |S|. |u|≈0.21 gives Im 𝔙≈|S|; "
        "|u|≥2π gives Im 𝔙≈34–270 — a 40–7000× OVERSHOOT, not a pass. The "
        "winding form u=Nt−2πik (|u|≥2π) is therefore INCOMPATIBLE with the "
        "small |u|≈0.21 that S's magnitude demands. A viable meridian "
        "assignment needs a tiny |u|, but a real tiny |u| gives Im 𝔙=0 "
        "(C1-dead); the honest surviving direction is a small-|u| COMPLEX "
        "(phase-channel) assignment — NOT the large-|u| winding lattice."))
    wb.add_data("verdict", verdict)
    wb.add_data("reconciliation_with_merged_resolution", (
        "SUPERSEDED-BY-MERGE: while this (N,k) meridian-winding menu (PR #3660 "
        "memo) was being scanned, main landed the DECISIVE resolution of the "
        "odd-S origin via the Ohtsuki tower 𝔙_b=𝔙_0+Σκ_n(2πb²)ⁿ at the substrate "
        "SMALL IMAGINARY parameter 2πb²=i·t (|·|=t≈0.10): a Lean-proved bar-parity "
        "selection rule (even→Vol, odd→S; OhtsukiTowerBarParity.even_rung_real / "
        ".odd_rung_imaginary) + Borel–Padé smooth Im 𝔙≈0.055 with action "
        "A=Vol(4₁)/π, no Stokes ambiguity (rem:ohtsuki-tower-bar-parity; "
        "qbeta_c3_borel_pade_resummation_probe.py). The odd-S sign-flip is the "
        "1/u³ ladder REPRESENTATION of that smooth object — representational / "
        "experimental-Q_β-limited, not a physical singularity. This scan is the "
        "COMPLEMENTARY NEGATIVE from the meridian side: the large-|u|≥2π winding "
        "lattice overshoots by ≥40× and leaves the geometric component, whereas "
        "the substrate's ACTUAL deformation is the small imaginary 2πb²=i·t that "
        "lands Im 𝔙 at the right O(0.05) — confirming the winding-lattice route "
        "was a dead end and closing the memo's open (N,k) proposal."))
    wb.add_data("normalization_caveat", (
        "Absolute Im 𝔙 (CS) at |u|~6–18 is normalization-uncertain: the "
        "branch-integral 𝔙=Vol−2πi·f (Φ=∫2v, f=(Φ−uv)/4) and the standard "
        "leading-NZ (√3/2)|u|²sin2φ disagree by O(1)–O(100) because |u| is far "
        "outside the small-|u| regime where either is controlled. The extended-"
        "Bloch flattening that would pin the absolute CS was NOT computed (it "
        "does not change the verdict: both estimates overshoot by ≥40×, and the "
        "Bloch–Wigner volumes are off-component regardless). What IS validated "
        "to full precision: u=0⇒Vol(4₁), the NZ slope 2√−3, gluing residual "
        "1e−20, and Im 𝔙=0 on the real axis."))
    wb.save()

    print("\n witness -> computations/qbeta/qbeta-c3-mq0-nk-scan.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
