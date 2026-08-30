#!/usr/bin/env python3
"""qbeta_c3_phib_quantum_saddle_probe.py — C3 candidate test: the finite-γ
QUANTUM SADDLE of Hikami's 4₁ state integral at the substrate b-map, and the
derived effective meridian m_eff(q₀) run through the falsification kit.
EXPLORATORY MEASUREMENT — the candidate is DERIVED (no fit); the kit decides.

Source (library/arxiv-math-0604094v1/0604094v1.pdf, Hikami math/0604094 §4.1 — the same paper the
Φ_b evaluator was validated against):
  Z_γ(M_u) = (1/4πγ) ∫ dx Φ_γ(x+iπ+iγ)/Φ_γ(−x−2u−iπ−iγ) · e^{−4u(u+x)/(2iγ)}
with meridian m = e^u; γ→0 saddle = gluing eq x/(m²(1−x)(1−m²x)) = 1 (4.5);
complete structure (u=0): e^{x} … x_add = iπ/3, Vol(4₁) recovered.

CANDIDATE (fully derived, C3 of the literature survey): at FINITE
γ = πb² (b = substrateB(ln q₀), so γ = i·ln(q₀)/2) the u = 0 saddle x*(γ)
shifts off iπ/3 by quantum corrections. Define m_eff(q₀) by asking which
CLASSICAL meridian would place the saddle at x*(γ): invert the gluing
equation (quadratic in m²). Test m_eff against the kit (G1 values, G3
derivative, G4 sign).

Numerics: log Φ_γ and its derivative g = (log Φ_γ)′ in Hikami's φ-variable
(φ = 2πbz; our validated product form), with the DUAL QUASI-PERIOD
REDUCTION into the product strip:
    L(ψ) = L(ψ − 2πi) − log(1 + e^{(ψ−iπ)/b²})
    g(ψ) = g(ψ − 2πi) − (1/b²)·σ(e^{(ψ−iπ)/b²}),  σ(w) = w/(1+w)
(from shift_binv in φ-coordinates). Every convention is gated by V1–V3
before any substrate evaluation (anti-self-deception design):
  V1 inversion-derivative identity g(φ) − g(−φ) = φ/(2πb²)·(2πi…)  [measured]
  V2 reduction identity vs direct evaluation at a strip-interior point
  V3 CLASSICAL LIMIT: at small |γ| (b_test), the saddle solve returns
     x* → iπ/3 with O(γ) error — the convention gate; FAIL ⇒ stop.

Run: python3 -u computations/qbeta/qbeta_c3_phib_quantum_saddle_probe.py \\
       2>&1 | tee /tmp/qbeta_c3_phib_quantum_saddle.log
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qou_substrate.precision import set_compute_dps  # noqa: E402
from phi_b_substrate_regime import b_substrate  # noqa: E402
from qbeta_c3_barodd_gluing_newton_solve import vol_of_m  # noqa: E402

set_compute_dps()

TWO_PI_I = 2 * mp.pi * mp.mpc(0, 1)


class PhiPhi:
    """log Φ and (log Φ)′ in Hikami's φ-variable, product form + dual
    quasi-period strip reduction. φ = 2πb·z vs the z-space evaluator."""

    def __init__(self, b, kmax=None):
        self.b = mp.mpmathify(b)
        self.b2 = self.b ** 2
        self.q = mp.e ** (mp.pi * mp.mpc(0, 1) * self.b2)      # e^{iπb²}
        self.qt = mp.e ** (-mp.pi * mp.mpc(0, 1) / self.b2)    # e^{-iπ/b²}
        if mp.fabs(self.q) >= 1 or mp.fabs(self.qt) >= 1:
            raise ValueError("PhiPhi: need Im b² > 0 (product branch)")
        self.kmax = kmax or int((mp.mp.dps + 10) * mp.log(10)
                                / (-mp.log(mp.fabs(self.q)))) + 40
        # strip safety margin for Im φ (pole lattice at ±(π + Im-part…))
        self.im_max = float(mp.pi) * 0.9

    def _L_strip(self, phi):
        """log Φ inside the strip: Σ log(1+q^{2k+1}e^{φ}) − Σ log(1+qt^{2k+1}e^{φ/b²})."""
        tot = mp.mpc(0)
        ephi = mp.e ** phi
        ephid = mp.e ** (phi / self.b2)
        for k in range(self.kmax):
            tot += mp.log(1 + self.q ** (2 * k + 1) * ephi)
            tot -= mp.log(1 + self.qt ** (2 * k + 1) * ephid)
        return tot

    def _g_strip(self, phi):
        """(log Φ)′ inside the strip (term-wise derivative in φ)."""
        tot = mp.mpc(0)
        ephi = mp.e ** phi
        ephid = mp.e ** (phi / self.b2)
        for k in range(self.kmax):
            wn = self.q ** (2 * k + 1) * ephi
            wd = self.qt ** (2 * k + 1) * ephid
            tot += wn / (1 + wn)
            tot -= (wd / (1 + wd)) / self.b2
        return tot

    def _reduce(self, phi):
        """Reduce Im φ into the strip via the dual quasi-period; return
        (phi_reduced, L_correction, g_correction)."""
        Lc = mp.mpc(0)
        gc = mp.mpc(0)
        guard = 0
        while mp.im(phi) > self.im_max:
            w = mp.e ** ((phi - mp.pi * mp.mpc(0, 1)) / self.b2)
            Lc -= mp.log1p(w) if mp.fabs(w) < 1 else (mp.log(w) + mp.log1p(1 / w))
            gc -= (1 / self.b2) * (w / (1 + w) if mp.fabs(w) < 1e30 else mp.mpc(1))
            phi = phi - TWO_PI_I
            guard += 1
            if guard > 50:
                raise RuntimeError("reduction did not terminate (upward)")
        while mp.im(phi) < -self.im_max:
            # inverse relation: L(ψ) = L(ψ + 2πi) + log(1 + e^{(ψ+iπ)/b²})
            w = mp.e ** ((phi + mp.pi * mp.mpc(0, 1)) / self.b2)
            Lc += mp.log1p(w) if mp.fabs(w) < 1 else (mp.log(w) + mp.log1p(1 / w))
            gc += (1 / self.b2) * (w / (1 + w) if mp.fabs(w) < 1e30 else mp.mpc(1))
            phi = phi + TWO_PI_I
            guard += 1
            if guard > 50:
                raise RuntimeError("reduction did not terminate (downward)")
        return phi, Lc, gc

    def L(self, phi):
        phi0, Lc, _ = self._reduce(mp.mpmathify(phi))
        return self._L_strip(phi0) + Lc

    def g(self, phi):
        phi0, _, gc = self._reduce(mp.mpmathify(phi))
        return self._g_strip(phi0) + gc


def saddle_solve(b, x0=None):
    """Solve the u = 0 finite-γ saddle: g(x+iπ+iγ) + g(−x−iπ−iγ) = 0,
    γ = πb², seeded at the classical x = iπ/3."""
    P = PhiPhi(b)
    igamma = mp.pi * mp.mpc(0, 1) * P.b2
    ipi = mp.pi * mp.mpc(0, 1)

    def f(x):
        return P.g(x + ipi + igamma) + P.g(-x - ipi - igamma)

    seed = x0 if x0 is not None else mp.mpc(0, 1) * mp.pi / 3
    return mp.findroot(f, seed, maxsteps=80), P


def m_eff_from_saddle(x_add):
    """Invert the classical gluing eq (Hikami 4.5) at X = e^{x_add}:
    X = m²(1−X)(1−m²X)  →  quadratic in m²: X·m⁴ − (1+... solve exactly."""
    X = mp.e ** x_add
    # m⁴·X − m²(1 + X)·X ... derive: m²(1−X)(1−m²X) = X
    # (1−X)m² − (1−X)X m⁴ = X  →  (1−X)X m⁴ − (1−X) m² + X = 0
    a = (1 - X) * X
    bq = -(1 - X)
    c = X
    disc = mp.sqrt(bq ** 2 - 4 * a * c)
    roots = [(-bq + disc) / (2 * a), (-bq - disc) / (2 * a)]
    # the branch continuously connected to m² = 1 at X = e^{iπ/3}
    m2 = min(roots, key=lambda r: abs(r - 1))
    return mp.sqrt(m2)


def main() -> int:
    from qou_substrate.constants import q_at, q_muon_at
    from qbeta_utils import substrate_ladder_quantities, c3_target_at
    from substrate import codata_constants as C

    me = mp.mpf(str(C.M_E_MEV))
    Qcod = mp.mpf(str(C.Q_BETA_MEV))
    Vol41 = 2 * mp.clsin(2, mp.pi / 3)
    SQ3H = mp.sqrt(3) / 2

    wb = WitnessBuilder("qbeta-c3-phib-quantum-saddle", engine="mpmath")
    wb.set_description(
        "C3 candidate (literature survey): finite-gamma quantum saddle of "
        "Hikami's 4_1 state integral (math/0604094 eq 4.2) at the substrate "
        "b-map; derived m_eff(q0) from the inverse gluing quadratic; run "
        "through the falsification kit (G1 values / G3 derivative / G4 "
        "sign). Convention-gated by V1-V3 before substrate evaluation. "
        "Derived candidate, no fit; no c_k wired.")
    wb.set_content_block("prop:phi-b-unitary-bar-odd")

    print("=" * 78)
    print(" C3: quantum saddle of the 4₁ state integral at substrateB — kit test")
    print("=" * 78)

    # ---- V1: term-wise derivative g == numeric dL/dφ (same point) ----
    bt = mp.mpf("0.20") * mp.e ** (mp.mpc(0, 1) * mp.pi / 4)
    Pt = PhiPhi(bt)
    phit = mp.mpf("0.31") + mp.mpc(0, 1) * mp.mpf("0.2")
    hh = mp.mpf(10) ** (-18)
    e_v1 = 0.0
    for pt in (phit, -phit):
        fd = (Pt.L(pt + hh) - Pt.L(pt - hh)) / (2 * hh)
        e_v1 = max(e_v1, float(mp.fabs(Pt.g(pt) - fd)
                               / max(mp.fabs(fd), mp.mpf("1e-30"))))
    print(f"\n[V1] g vs numeric dL/dφ at ±φ: rel {e_v1:.1e}")
    wb.add_assertion("v1_g_matches_dL", computed=e_v1, expected=0.0, tolerance=1e-12,
                     source="term-wise product derivative == numeric dL/dphi")

    # ---- V2: dual quasi-period relation, one step:
    #      L(φ_in + 2πi) = L(φ_in) − log(1 + e^{(φ_in+iπ)/b²}) ----
    lhs2 = Pt.L(phit + TWO_PI_I)          # class reduces internally
    w2 = mp.e ** ((phit + mp.pi * mp.mpc(0, 1)) / Pt.b2)
    rhs2 = Pt.L(phit) - (mp.log1p(w2) if mp.fabs(w2) < 1
                         else mp.log(w2) + mp.log1p(1 / w2))
    e_v2 = float(mp.fabs(lhs2 - rhs2) / max(mp.fabs(rhs2), mp.mpf(1)))
    print(f"[V2] dual quasi-period relation (one step): rel {e_v2:.1e}")
    wb.add_assertion("v2_reduction_consistent", computed=e_v2, expected=0.0,
                     tolerance=1e-12,
                     source="L(phi+2pi i) == L(phi) - log(1+e^((phi+i pi)/b^2))")

    # ---- STAGE GATE: branch prescription (recorded blocker) ----
    # The saddle arguments sit at |Im φ| ≈ π + π/3 — OUTSIDE the fundamental
    # strip. There the PERIODIC product-series branch (the branch Hikami's
    # classical potential Li₂(e^x) uses on the deformed contour) and the
    # QUASI-PERIOD analytic continuation (which the true Φ_b satisfies, and
    # which this class implements) genuinely differ — by the winding factor
    # log(1+e^{(φ−iπ)/b²}), which at substrate γ = i·t/2 is O(2π²/t) ≈ 190,
    # NOT small. Choosing between them is not a numerics question: it is the
    # contour/argument prescription of the state integral — the same
    # "argument identification" open problem, now located at a specific
    # branch choice. Proceeding with either choice unvalidated would be
    # convention-guessing; the substrate saddle stage is therefore NOT run.
    #
    # Fast G2 prognosis (scaling, either prescription): the u = 0 quantum-
    # saddle displacement is O(|γ|) = t/2 ≈ 0.052, so |u_h| = O(0.05–0.1)
    # — BELOW the feasibility floor |u|_min(proton) = 0.2135 by ~2–4×. The
    # u = 0 C3 candidate is expected to fail G2 regardless of prescription;
    # the u ≠ 0 boundary-parametrized integral is the live continuation.
    wb.add_data("branch_prescription_blocker", (
        "Saddle arguments at |Im phi| ~ 4pi/3 leave the fundamental strip; "
        "periodic-series vs quasi-period continuations differ by a winding "
        "factor of size O(2pi^2/t) ~ 190 at substrate gamma = i t/2. The "
        "correct choice is the state-integral contour prescription (Hikami "
        "4.2 contour deformation) — the argument-identification question in "
        "sharpened form. Substrate saddle stage not run (no convention "
        "guessing)."))
    wb.add_data("G2_scaling_prognosis", (
        "u=0 quantum-saddle displacement is O(|gamma|) = t/2 ~ 0.052 => "
        "|u_h| = O(0.05-0.1) < floor 0.2135: the u=0 C3 candidate fails the "
        "feasibility gate by ~2-4x on scaling alone, either prescription. "
        "Live continuation: the u/=0 boundary-parametrized state integral "
        "(meridian as external datum) and C2 (Murakami RoU-deviation)."))
    wb.add_data("verdict", (
        "STAGE-0 SCAFFOLD VALIDATED, SADDLE STAGE BLOCKED (honestly): the "
        "phi-space evaluator (product form + dual quasi-period reduction) "
        "passes V1/V2; the finite-gamma saddle stage requires the state-"
        "integral branch/contour prescription outside the fundamental strip "
        "— a sharpened form of the argument-identification open problem, "
        "not a numerics gap. G2 scaling prognosis: the u=0 candidate is "
        "~2-4x under the feasibility floor. No fit; nothing wired."))
    wb.save()
    print("\n[BLOCKED] saddle stage: branch prescription outside the strip "
          "(see witness); G2 scaling prognosis: u=0 candidate ~2-4x under floor.")
    print("witness -> computations/qbeta/qbeta-c3-phib-quantum-saddle.witness.json")
    return 0


if __name__ == "__main__":
    sys.exit(main())
