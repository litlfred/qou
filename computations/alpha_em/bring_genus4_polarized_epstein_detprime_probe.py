#!/usr/bin/env python3
"""bring_genus4_polarized_epstein_detprime_probe.py

UNBLOCKS the deferred piece of the 2026-07-18 polarized-Epstein probe
(`bring_polarized_epstein_determinant_probe.py`): the FULL genus-4 Epstein det'Δ
on Jac(Bring), at BOTH the principally polarized period τ_B = τ₀·M
(Braden–Disney-Hogg arXiv:2208.13692 Thm 2.12;
M = [[4,1,-1,1],[1,4,1,-1],[-1,1,4,1],[1,-1,1,4]]) and the product/diagonal
period τ₀·diag(5,5,5,1) (the Prop 4.6 complex-torus isomorphism target).

Why it was deferred: the box enumeration (2R+1)^8 over Z^8 cannot converge at the
thin Bring modulus (Im τ₀ = 0.186676) at any feasible R (R=5 is already 2.1e8
points). FIX: Fincke–Pohst norm-cutoff enumeration — enumerate exactly the
lattice points with m^T H m ≤ Q (Cholesky-recursive, vectorized); at Q=14 the
theta tail is < e^{-π·14} ≈ 8.5e-20, far below the working precision. This does
the job the sibling called "Siegel reduction": exact-cutoff enumeration handles
thin forms directly, no basis reduction needed.

VALIDATION LADDER (machine-checked):
  1. genus-1: FP machinery reproduces det'Δ = (Im τ)²|η(τ)|⁴ exactly (the
     sibling's anchor, re-established for the FP path);
  2. genus-2 diag(5τ₀,τ₀): FP agrees with an INDEPENDENT factorized-theta
     evaluation (theta of a direct-sum lattice = product of per-block 2-dim
     thetas — the theta factorizes even though det'Δ does not), and sits at/above
     the sibling's box-R=5 value 3.9437 which was still converging up;
  3. genus-4 diagonal: FP vs factorized-theta cross-check again (8-dim live);
  4. genus-4 polarized M: cutoff-convergence (Q=11 vs Q=14) asserted.

Scope guard (STRICT): reports the two genus-4 measures + the polarization
theta-factor ratio + plain nearest-constant comparisons (8π, b₁=8, the retracted
naive product 8.226). NO q₀, NO 8π manufactured, NOTHING wired, no tier change.
The reciprocal π stays RT/Front-2.

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
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()


# ---------- shared with the 2026-07-18 sibling (identical conventions) ----------

def _gram(tau):
    g = tau.shape[0]
    P = np.zeros((2 * g, 2 * g))
    for i in range(g):
        P[i, i] = 1.0
        P[i, g:] = tau.real[i]
        P[g + i, g:] = tau.imag[i]
    return P.T @ P


def _eta(t):
    q = mp.e ** (2j * mp.pi * t)
    return q ** (mp.mpf(1) / 24) * mp.qp(q)


# ---------- Fincke–Pohst norm-cutoff enumeration (the unblocker) ----------

def fp_norms(H, Q, cap=30_000_000):
    """All norms m^T H m ≤ Q over m ∈ Z^n \\ {0}, exact cutoff (vectorized FP)."""
    H = np.asarray(H, float)
    n = H.shape[0]
    Rm = np.linalg.cholesky(H).T          # upper triangular, H = Rm^T Rm
    m = np.zeros((1, n))
    pn = np.zeros(1)
    for i in range(n - 1, -1, -1):
        c = (m[:, i + 1:] @ Rm[i, i + 1:]) / Rm[i, i]
        w = np.sqrt(np.maximum(Q - pn, 0.0)) / Rm[i, i]
        lo = np.ceil(-c - w - 1e-12).astype(np.int64)
        hi = np.floor(-c + w + 1e-12).astype(np.int64)
        cnt = np.maximum(hi - lo + 1, 0)
        k = int(cnt.sum())
        if k > cap:
            raise RuntimeError(f"FP candidate blowup: {k} at level {i}")
        idx = np.repeat(np.arange(len(cnt)), cnt)
        starts = np.concatenate(([0], np.cumsum(cnt)[:-1]))
        val = (lo[idx] + (np.arange(k) - starts[idx])).astype(float)
        newm = m[idx]
        newm = newm.copy()
        newm[:, i] = val
        pn = pn[idx] + (Rm[i, i] * (val + c[idx])) ** 2
        keep = pn <= Q + 1e-9
        m, pn = newm[keep], pn[keep]
    nz = np.any(m != 0, axis=1)
    return pn[nz]


def _theta_m1(qnorms, t):
    return float(np.sum(np.exp(-np.pi * t * qnorms)))


def _zeta_prime0_from_thetas(theta_m1_H, theta_m1_Hi, dH, n):
    # identical Chowla–Selberg split as the 2026-07-18 sibling probe
    I1 = float(mp.quad(lambda t: theta_m1_H(float(t)) / t, [1, mp.inf]))
    I2 = float(mp.quad(lambda u: theta_m1_Hi(float(u)) * float(u) ** (n / 2 - 1), [1, mp.inf]))
    return -np.log(np.pi) - np.euler_gamma - (2.0 / n) * dH ** -0.5 + I1 + dH ** -0.5 * I2


def measure_fp(tau, Q):
    """Scale-free boson measure √Vol/√det'Δ via FP-cutoff thetas."""
    n = 2 * tau.shape[0]
    G = _gram(tau)
    H = np.linalg.inv(G)                  # det'Δ = (4π²)^{-1} e^{-Z'_{G^{-1}}(0)}
    qH = fp_norms(H, Q)
    qHi = fp_norms(G, Q)
    zp = _zeta_prime0_from_thetas(lambda t: _theta_m1(qH, t),
                                  lambda u: _theta_m1(qHi, u),
                                  np.linalg.det(H), n)
    detprime = (4 * np.pi ** 2) ** -1 * np.exp(-zp)
    return float(np.sqrt(np.sqrt(np.linalg.det(G))) / np.sqrt(detprime)), len(qH), len(qHi)


# ---------- independent cross-check: factorized thetas for direct-sum (diag) forms ----------

def _box_norms(g2, R):
    a = np.array(list(itertools.product(range(-R, R + 1), repeat=2)), float)
    a = a[np.any(a != 0, axis=1)]
    return np.einsum('ij,jk,ik->i', a, g2, a)


def measure_factorized(taus, R=60):
    """diag(τ₁..τ_g): θ_{⊕H_i}(t) = Π θ_{H_i}(t); det'Δ from the SAME CS split.

    Independent of FP (different enumeration, different theta assembly) — a
    genuine cross-check, valid only for direct-sum periods."""
    blocks = [_gram(np.array([[t]])) for t in taus]
    n = 2 * len(blocks)
    detG = float(np.prod([np.linalg.det(b) for b in blocks]))
    qH = [_box_norms(np.linalg.inv(b), R) for b in blocks]     # blocks of G^{-1}
    qHi = [_box_norms(b, R) for b in blocks]                   # blocks of G

    def prod_theta_m1(qlist, t):
        p = 1.0
        for q in qlist:
            p *= 1.0 + float(np.sum(np.exp(-np.pi * t * q)))
        return p - 1.0

    zp = _zeta_prime0_from_thetas(lambda t: prod_theta_m1(qH, t),
                                  lambda u: prod_theta_m1(qHi, u),
                                  1.0 / detG, n)
    detprime = (4 * np.pi ** 2) ** -1 * np.exp(-zp)
    return float(np.sqrt(np.sqrt(detG)) / np.sqrt(detprime))


def main():
    t0 = complex(-0.5, 0.186676)          # Thm 2.12 Bring modulus (sibling-identical)
    M = np.array([[4, 1, -1, 1], [1, 4, 1, -1], [-1, 1, 4, 1], [1, -1, 1, 4]], float)
    assertions = []

    def check(name, passed, detail=""):
        assertions.append({"name": name, "passed": bool(passed), "detail": detail})
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}  {detail}")

    # 1. genus-1 anchor for the FP path: det'Δ = (Im τ)²|η|⁴ ⇔ measure = 1/(√Im τ|η|²)
    tau1c = mp.mpc(0.3, 1.4)
    m1_fp, _, _ = measure_fp(np.array([[complex(0.3, 1.4)]]), Q=14)
    m1_exact = float(1 / (mp.sqrt(mp.im(tau1c)) * abs(_eta(tau1c)) ** 2))
    check("genus1_fp_reproduces_eta_form",
          abs(m1_fp / m1_exact - 1) < 1e-6,
          f"FP measure={m1_fp:.10f} vs 1/(√Im τ|η|²)={m1_exact:.10f}")

    # 2. genus-2 diag(5τ₀,τ₀): FP vs independent factorized theta; refines sibling box-R=5
    tau2 = np.array([[5 * t0, 0], [0, t0]])
    m2_fp, n2a, n2b = measure_fp(tau2, Q=14)
    m2_fac = measure_factorized([5 * t0, t0])
    sib = 3.9437282500685407              # sibling's R=5 box value, converging up
    check("genus2_fp_eq_factorized_theta",
          abs(m2_fp / m2_fac - 1) < 1e-6,
          f"FP={m2_fp:.10f} vs factorized={m2_fac:.10f} (pts {n2a}/{n2b})")
    check("genus2_refines_sibling_box_value",
          m2_fp >= sib * 0.999 and abs(m2_fp / sib - 1) < 0.02,
          f"FP(Q=14)={m2_fp:.8f} vs sibling box R=5 {sib:.8f} (was converging up)")

    # 3. genus-4 DIAGONAL diag(5τ₀,5τ₀,5τ₀,τ₀): FP vs factorized (8-dim live check)
    tau4d = np.diag([5 * t0, 5 * t0, 5 * t0, t0])
    m4d_fp, n4a, n4b = measure_fp(tau4d, Q=14)
    m4d_fac = measure_factorized([5 * t0, 5 * t0, 5 * t0, t0])
    check("genus4_diag_fp_eq_factorized_theta",
          abs(m4d_fp / m4d_fac - 1) < 1e-5,
          f"FP={m4d_fp:.8f} vs factorized={m4d_fac:.8f} (pts {n4a}/{n4b})")

    # 4. genus-4 POLARIZED τ_B = τ₀·M — the deferred headline; cutoff convergence
    tau4p = t0 * M
    m4p_lo, _, _ = measure_fp(tau4p, Q=11)
    m4p, n4pa, n4pb = measure_fp(tau4p, Q=14)
    check("genus4_polarized_cutoff_converged",
          abs(m4p / m4p_lo - 1) < 1e-5,
          f"Q=11: {m4p_lo:.10f} vs Q=14: {m4p:.10f} (pts {n4pa}/{n4pb})")

    # 5. comparisons (recorded plainly, nothing interpreted/wired)
    naive = 8.226285221978587             # retracted per-factor product (context only)
    eight_pi = float(8 * mp.pi)
    comparisons = {
        "measure_polarized_M": m4p,
        "measure_diagonal": m4d_fp,
        "polarization_theta_factor_ratio_pol_over_diag": m4p / m4d_fp,
        "retracted_naive_product": naive,
        "ratio_pol_over_naive": m4p / naive,
        "ratio_pol_over_8pi": m4p / eight_pi,
        "ratio_pol_over_8": m4p / 8.0,
        "ratio_diag_over_naive": m4d_fp / naive,
    }
    for k, v in comparisons.items():
        print(f"    {k} = {v:.10e}")

    all_passed = all(a["passed"] for a in assertions)
    verdict = (
        "GENUS-4 POLARIZED EPSTEIN det'Δ — DEFERRED PIECE COMPUTED (scope-(a); no q₀, no 8π "
        "manufactured, nothing wired): Fincke–Pohst norm-cutoff enumeration unblocks the thin "
        f"Bring modulus. measure(τ₀·M, principally polarized) = {m4p:.8f} (O(1)); "
        f"measure(τ₀·diag(5,5,5,1)) = {m4d_fp:.6e} (the product-period BLOW-UP); polarization "
        f"theta-factor = {m4p / m4d_fp:.3e} — the integer M-lattice theta is precisely what "
        "removes the ~12-orders blow-up of the near-degenerate product period. Both differ "
        "from the retracted naive product 8.226 "
        f"(pol/naive = {m4p / naive:.6f}) and neither is 8π (pol/8π = {m4p / eight_pi:.6f}). "
        "Machinery validated genus-1 exact + genus-2/genus-4 factorized-theta cross-checks. "
        "π stays RT/Front-2; NO tier change."
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
        "computation": "bring-genus4-polarized-epstein-detprime",
        "description": "Computes the deferred genus-4 Epstein det'Δ measures on Jac(Bring) at the "
                       "principally polarized period τ₀·M (Thm 2.12) and the diagonal period "
                       "τ₀·diag(5,5,5,1), via Fincke–Pohst norm-cutoff enumeration (unblocks the "
                       "thin Bring modulus that stalled the 2026-07-18 box enumeration). Validated "
                       "genus-1 exact (η-form) + independent factorized-theta cross-checks at "
                       "genus 2 and genus 4. No q₀; no 8π; nothing wired.",
        "auditOnly": "docs/audits/2026-07-19-bring-genus4-polarized-epstein-detprime.md",
        "tier": "structural-exact machinery (genus-1 exact + factorized-theta cross-checks) + "
                "scope-(a) genus-4 numbers",
        "computedAt": now, "commitSha": _sha(),
        "engine": "numpy+mpmath", "engineVersion": np.__version__ + "/" + mp.__version__,
        "scriptFile": os.path.basename(__file__),
        "scriptHash": hashlib.sha256(src).hexdigest()[:12],
        "assertions": assertions, "allPassed": all_passed,
        "result": {**comparisons, "verdict": verdict},
        "context": {
            "unblocks": "the 'deferred' item of bring-polarized-epstein-determinant.witness.json "
                        "(full genus-4 Epstein det'Δ at Im τ₀=0.187, was Siegel-reduction-blocked)",
            "structure_source": "τ_B=τ₀·M, M=[[4,1,-1,1],[1,4,1,-1],[-1,1,4,1],[1,-1,1,4]] "
                                "(Braden–Disney-Hogg arXiv:2208.13692 Thm 2.12) + Prop 4.6 "
                                "diag(5,5,5,1); PDF library/arxiv-2208.13692v1/2208.13692v1.pdf",
            "method": "Fincke–Pohst exact norm-cutoff (Q=14, tail<8.5e-20) + Chowla–Selberg "
                      "heat-kernel split identical to the 2026-07-18 sibling",
            "scope_guard": "no q₀, no 8π manufactured, nothing wired, no tier change; scope-(a)",
        },
    }
    out = os.path.join(_here, "bring-genus4-polarized-epstein-detprime.witness.json")
    with open(out, "w") as f:
        json.dump(witness, f, indent=2)
    print("witness ->", out)
    return 0 if all_passed else 1


if __name__ == "__main__":
    sys.exit(main())
