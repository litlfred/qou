#!/usr/bin/env python3
"""bring_polarized_epstein_determinant_probe.py

The genus-g Epstein det'Δ machinery for the α_EM polarized photon-determinant leg,
VALIDATED on genus 1, then used to CORRECT the naive per-factor product framing of
the earlier #3864 audit.

Background. #3864 reduced the α_EM 1/(8π) wall's magnitude leg to the boson 1-loop
measure on the Bring Jacobian, and (in its 2026-07-18 update) recorded a naive
"per-factor product" `m(5τ₀)³·m(τ₀) ≈ 8.226` over the Jac(Bring) ≅ E_{5τ₀}³×E_{τ₀}
decomposition (Braden–Disney-Hogg Prop 4.6). This probe shows that product is the
WRONG object: the genuine boson measure on the higher-dim torus T^{2g} is the genus-g
Epstein det'Δ, whose spectrum is {λ_i + μ_j} (sums), NOT a product of per-T² measures.

The machinery (Chowla–Selberg / heat-kernel analytic continuation):
  Z_H(s) = Σ'_{m∈Z^n}(m^T H m)^{-s},  det'Δ = (4π²)^{-1} exp(-Z'_{G^{-1}}(0)),  G = P^T P,
  Z'_H(0) = -ln π - γ - (2/n) det(H)^{-1/2}
            + ∫_1^∞ t^{-1}(θ_H(t)-1) dt + det(H)^{-1/2} ∫_1^∞ u^{n/2-1}(θ_{H^{-1}}(u)-1) du,
  θ_H(t) = Σ_{m∈Z^n} e^{-π t m^T H m},  scale-free measure = √Vol(J)/√det'Δ, Vol(J)=√det G.

VALIDATION (genus 1, EXACT): for T² = C/(Z+τZ) the machinery returns
det'Δ = (Im τ)²|η(τ)|⁴ and measure = 1/(√Im τ·|η(τ)|²) to machine precision — the
#3864 per-factor form. This anchors trust in the higher-genus output.

FINDING (genus 2): measure(E_{5τ₀} × E_{τ₀}) = 3.94 (Epstein) vs the naive product
m(5τ₀)·m(τ₀) = 2.92 — ratio ≈ 1.35 ≠ 1 (converging up in the truncation R). So the
per-factor product is NOT the torus boson measure; the polarized photon-determinant
magnitude of the α_EM wall is the full genus-4 Epstein det'Δ on Jac(Bring), and the
#3864 "8.226" is superseded as the wrong object.

Scope guard (STRICT): validates the machinery + corrects the product framing (scope-(a)
self-correction). Does NOT report a final genus-4 number — the full 8-dim Epstein at the
thin Bring modulus (Im τ₀ = 0.187) converges slowly and needs Siegel reduction (deferred).
No q₀, no 8π manufactured, nothing wired, no tier change. The reciprocal π stays RT/Front-2.

Self-contained (numpy + mpmath).
"""
import datetime
import hashlib
import itertools
import json
import os
import subprocess
import sys

import mpmath as mp
import numpy as np

mp.mp.dps = 20


def _pts(n, R):
    a = np.array(list(itertools.product(range(-R, R + 1), repeat=n)), float)
    return a[np.any(a != 0, axis=1)]


def _theta_m1(H, t, P):
    q = np.einsum('ij,jk,ik->i', P, H, P)
    return float(np.sum(np.exp(-np.pi * t * q)))


def _zeta_prime0(H, n, R):
    dH = np.linalg.det(H)
    Hi = np.linalg.inv(H)
    P = _pts(n, R)
    I1 = float(mp.quad(lambda t: _theta_m1(H, float(t), P) / t, [1, mp.inf]))
    I2 = float(mp.quad(lambda u: _theta_m1(Hi, float(u), P) * float(u) ** (n / 2 - 1), [1, mp.inf]))
    return -np.log(np.pi) - np.euler_gamma - (2.0 / n) * dH ** -0.5 + I1 + dH ** -0.5 * I2


def _detprime_delta(G, n, R):
    return (4 * np.pi ** 2) ** -1 * np.exp(-_zeta_prime0(np.linalg.inv(G), n, R))


def _gram(tau):
    g = tau.shape[0]
    P = np.zeros((2 * g, 2 * g))
    for i in range(g):
        P[i, i] = 1.0
        P[i, g:] = tau.real[i]
        P[g + i, g:] = tau.imag[i]
    return P.T @ P


def _measure(tau, R):
    n = 2 * tau.shape[0]
    G = _gram(tau)
    return float(np.sqrt(np.sqrt(np.linalg.det(G))) / np.sqrt(_detprime_delta(G, n, R)))


def _eta(t):
    q = mp.e ** (2j * mp.pi * t)
    return q ** (mp.mpf(1) / 24) * mp.qp(q)


def _m1(t):
    return float(1 / (mp.sqrt(mp.im(t)) * abs(_eta(t)) ** 2))


def main():
    t0 = complex(-0.5, 0.186676)
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 1. genus-1 validation: Epstein det'Δ reproduces (Im τ)²|η|⁴ and the #3864 measure
    tau1 = np.array([[complex(0.3, 1.4)]])
    G1 = _gram(tau1)
    dp1 = _detprime_delta(G1, 2, 6)
    exact1 = float(mp.im(mp.mpc(0.3, 1.4)) ** 2 * abs(_eta(mp.mpc(0.3, 1.4))) ** 4)
    meas1 = _measure(tau1, 6)
    meas1_exact = _m1(mp.mpc(0.3, 1.4))
    check("genus1_machinery_validated_exact",
          abs(dp1 / exact1 - 1) < 1e-6 and abs(meas1 / meas1_exact - 1) < 1e-6,
          f"det'Δ={dp1:.8f}=(Im τ)²|η|⁴={exact1:.8f}; measure={meas1:.8f}=1/(√Im τ|η|²)="
          f"{meas1_exact:.8f} — machinery reproduces #3864's per-factor form EXACTLY")

    # 2. genus-2: measure(E_{5τ₀}×E_{τ₀}) ≠ naive product m(5τ₀)·m(τ₀) (converging up)
    tau2 = np.array([[5 * t0, 0], [0, t0]])
    m_R = {R: _measure(tau2, R) for R in (3, 4, 5)}
    prod2 = _m1(5 * t0) * _m1(t0)
    ratio = m_R[5] / prod2
    converging = abs(m_R[5] - m_R[4]) < abs(m_R[4] - m_R[3])
    check("genus2_measure_not_the_naive_product",
          abs(ratio - 1) > 0.25 and converging,
          f"measure(E_5τ₀×E_τ₀)={m_R[5]:.5f} (R=3,4,5: {m_R[3]:.4f},{m_R[4]:.4f},{m_R[5]:.4f}, "
          f"converging up) vs naive product m(5τ₀)·m(τ₀)={prod2:.5f}: ratio={ratio:.4f}≠1 ⇒ the "
          "T⁴ boson measure is NOT the per-factor product (spectrum {λ+μ}, not a product)")

    # 3. consequence: the #3864 '8.226' per-factor product is the WRONG object
    naive_g4 = _m1(5 * t0) ** 3 * _m1(t0)
    check("product_framing_superseded_8p226_wrong_object",
          abs(ratio - 1) > 0.25,
          f"since even the genus-2 product framing fails by ×{ratio:.2f}, the #3864 genus-4 "
          f"naive product m(5τ₀)³·m(τ₀)={naive_g4:.4f} (≈8.226) is NOT the polarized photon-"
          "determinant measure; the genuine object is the full genus-4 Epstein det'Δ on "
          "Jac(Bring) (deferred: thin Bring modulus needs Siegel reduction). This RETRACTS "
          "the 8.226 as the magnitude value; only the machinery + structure stand")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "GENUS-g EPSTEIN det'Δ MACHINERY — VALIDATED + PRODUCT-FRAMING CORRECTED (scope-(a) "
        "self-correction; no q₀, no 8π, nothing wired): the Chowla–Selberg heat-kernel ζ'(0) "
        "reproduces the genus-1 det'Δ=(Im τ)²|η|⁴ and measure 1/(√Im τ|η|²) EXACTLY. Applied at "
        "genus 2, measure(E_5τ₀×E_τ₀)≈3.94 ≠ the naive product 2.92 (ratio≈1.35) — the torus "
        "boson measure is NOT a product of per-T² factors (spectrum {λ+μ}). CONSEQUENCE: the "
        "#3864 per-factor product 'm(5τ₀)³·m(τ₀)≈8.226' is the WRONG object for the polarized "
        "photon determinant and is RETRACTED as the magnitude value; the genuine magnitude leg "
        "is the full genus-4 Epstein det'Δ on Jac(Bring) (numerically deferred — the thin Bring "
        "modulus Im τ₀=0.187 needs Siegel reduction). The machinery + the Jac≅E_5τ₀³×E_τ₀ "
        "structure + genus-1 anchor stand; the naive product does not. π stays RT/Front-2. "
        "NO tier change."
        if all_passed else
        "INCONCLUSIVE — an assertion failed; re-derive before citing."
    )
    print("\nVERDICT:", verdict)

    _here = os.path.dirname(os.path.abspath(__file__))

    def _sha():
        s = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=_here, text=True).strip()
        if not s:
            raise RuntimeError("empty commitSha")
        return s

    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    with open(__file__, "rb") as _f:
        src = _f.read()
    witness = {
        "computation": "bring-polarized-epstein-determinant",
        "description": "Genus-g Epstein det'Δ machinery for the α_EM polarized photon-determinant leg. "
                       "VALIDATED on genus 1 (reproduces (Im τ)²|η|⁴ + measure 1/(√Im τ|η|²) exactly). "
                       "CORRECTS #3864: genus-2 measure(E_5τ₀×E_τ₀)≈3.94 ≠ naive product 2.92 (ratio 1.35) "
                       "⇒ the torus boson measure is NOT a per-factor product; the #3864 '8.226' is the "
                       "wrong object and is retracted as the magnitude value. Full genus-4 number deferred "
                       "(thin Bring modulus needs Siegel reduction). No q₀; no 8π; nothing wired.",
        "auditOnly": "docs/audits/2026-07-18-bring-polarized-epstein-determinant.md",
        "tier": "structural-exact machinery (genus-1 EXACT validation) + scope-(a) genus-2 finding",
        "computedAt": now, "commitSha": _sha(),
        "engine": "numpy+mpmath", "engineVersion": np.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {
            "genus1_detprime": dp1, "genus1_exact_ImTau2_eta4": exact1,
            "genus2_measure_R5": m_R[5], "genus2_naive_product": prod2,
            "genus2_ratio": ratio, "naive_g4_product_8p226_retracted": naive_g4,
            "verdict": verdict,
        },
        "context": {
            "validated": "genus-1 Epstein det'Δ = (Im τ)²|η|⁴ EXACTLY ⇒ machinery correct",
            "corrects": "#3864 2026-07-18 update — the per-factor product m(5τ₀)³·m(τ₀)≈8.226 is NOT "
                        "the T⁸ boson measure (genus-2 shows measure≠product by ×1.35); retracted",
            "structure_source": "Jac(Bring)≅E_5τ₀³×E_τ₀, period τ₀·M (Braden–Disney-Hogg Thm 2.12 + "
                                "Prop 4.6; PDF library/arxiv-2208.13692v1/2208.13692v1.pdf)",
            "deferred": "full genus-4 Epstein det'Δ at the thin Bring modulus (Im τ₀=0.187) — needs "
                        "Siegel reduction for numerical convergence",
            "scope_guard": "no q₀, no 8π manufactured, nothing wired, no tier change; scope-(a)",
        },
    }
    out = os.path.join(_here, "bring-polarized-epstein-determinant.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
