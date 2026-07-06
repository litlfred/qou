#!/usr/bin/env python3
"""D14 modular-S-transform: theta-convergence (bar-side) + nome-conflation probe.

Formalize-first probe for the Jacobi-triple-product / theta avenue on the
modular S-transform conjecture
(`conj:modular-s-transform-q-q-tilde`, duality D14).

Two structural facts the probe establishes (both q0-robust):

  (A) BAR-SIDE CONVERGENCE.  The Jacobi theta series
          theta(v | tau) = sum_{n in Z} z^n q_nome^{n^2},   q_nome = exp(2 pi i tau)
      converges iff |q_nome| < 1 iff Im(tau) > 0 (tau in the upper half-plane H).
      Writing the Hecke substrate as q0 = exp(2 pi i tau), the value q0 ~ 1.11 > 1
      gives tau with Im(tau) < 0 (LOWER half-plane) -> theta DIVERGES.  Only the
      bar image q0^{-1} < 1 gives tau in H -> theta CONVERGES.  Hence a QOU theta
      object is intrinsically a bar-symmetric / binding (Li_2^q) object, and the
      D14 conjecture's stated premise "tau in H" forces the q0^{-1} branch, not q0.

  (B) NOME-CONFLATION TRAP.  The framework's *named* elliptic curves (the
      Descartes/color curve E_q : y^2 = x^3 + a x + b, j ~ 129.9) are NOT the
      Hecke modular torus.  E_q's period nome lies in [exp(-2pi), exp(-pi*sqrt3)]
      ~ [0.0019, 0.0043] for any 0 < j < 1728, whereas the Hecke modular nome is
      q0^{-1} ~ 0.90.  Mismatch ~ 200-480x.  Do NOT identify the modular tau of
      D14 with the period tau of E_q / E_z.

No fit, no free parameter.  Pure consequence of theta convergence + Klein-j.
"""
import json
import os
import mpmath as mp

mp.mp.dps = 40


def tau_from_nome(q):
    """Solve q = exp(2 pi i tau) for tau (principal branch)."""
    return mp.log(q) / (2 * mp.pi * mp.j)


def descartes_nome():
    """Period nome |exp(2 pi i tau_E)| of the color curve E_q (j ~ 129.9),
    via Klein-j inversion on the fundamental-domain boundary arc |tau| = 1."""
    a, b = mp.mpf("0.7087"), mp.mpf("0.8056")
    j = 1728 * 4 * a**3 / (4 * a**3 + 27 * b**2)
    # On the arc tau = exp(i phi), phi in (pi/3, pi/2], Klein-j is real and
    # monotone 0 -> 1728.  Bisect for kleinj = j.  NB mpmath.kleinj uses the
    # j(i)=1 normalization (returns j/1728), so scale by 1728 to compare.
    # Keep lo/hi/phi as mpf throughout (mp.pi and mp.mpf are full precision)
    # and use mp.exp(mp.j*phi) for high-precision complex exponentiation, so
    # tau_E / nome are accurate to mp.mp.dps rather than 53-bit double.
    f = lambda phi: 1728 * mp.kleinj(mp.exp(mp.j * phi)).real - j
    lo, hi = mp.pi / 3 + mp.mpf("1e-9"), mp.pi / 2
    tol = mp.mpf(10) ** -mp.mp.dps  # tolerance tied to the working precision
    for _ in range(200):
        if hi - lo < tol:
            break
        mid = (lo + hi) / 2
        (lo, hi) = (mid, hi) if f(mid) < 0 else (lo, mid)
    phi = (lo + hi) / 2
    tau_E = mp.exp(mp.j * phi)
    return j, tau_E, mp.exp(-2 * mp.pi * mp.im(tau_E))


def run(q0=mp.mpf("1.10998")):  # substrate value (cheat-sheet); verdict is q0-robust
    out = {"q0": mp.nstr(q0, 12), "branches": {}}
    for name, q in [("q0", q0), ("q0_inv", 1 / q0)]:
        tau = tau_from_nome(q)
        out["branches"][name] = {
            "nome": mp.nstr(q, 12),
            "tau": mp.nstr(tau, 12),
            "im_tau": mp.nstr(mp.im(tau), 8),
            "in_upper_half_plane": bool(mp.im(tau) > 0),
            "theta_converges": bool(abs(q) < 1),
        }
    j, tau_E, nome_E = descartes_nome()
    out["descartes_curve_E_q"] = {
        "equation": "y^2 = x^3 + 0.7087 x + 0.8056",
        "j_invariant": mp.nstr(j, 8),
        "period_tau": mp.nstr(tau_E, 10),
        "period_nome": mp.nstr(nome_E, 8),
    }
    out["nome_conflation"] = {
        "hecke_modular_nome_bar_side": mp.nstr(1 / q0, 8),
        "descartes_period_nome": mp.nstr(nome_E, 8),
        "ratio": mp.nstr((1 / q0) / nome_E, 6),
        "same_curve": bool(abs((1 / q0) / nome_E - 1) < mp.mpf("1e-3")),
    }
    return out


if __name__ == "__main__":
    result = run()
    witness = {
        "computation": "d14-theta-bar-side",
        "description": (
            "D14 modular-S-transform: theta converges only on the bar image q0^{-1} "
            "(Im tau > 0); the Descartes/color elliptic curve E_q is NOT the Hecke "
            "modular torus (period-nome mismatch ~200-480x). Formalize-first probe "
            "for the Jacobi-triple-product/theta avenue (conj:modular-s-transform-q-q-tilde)."
        ),
        "findings": {
            "A_bar_side_convergence": (
                "q0 > 1 -> Im(tau) < 0 -> theta diverges; q0^{-1} < 1 -> Im(tau) > 0 "
                "-> theta converges. The D14 premise 'tau in H' forces the q0^{-1} branch."
            ),
            "B_nome_conflation_trap": (
                "E_q period nome ~ 0.002-0.004 (deep in fundamental domain, tau ~ i) vs "
                "Hecke modular nome q0^{-1} ~ 0.90 (near cusp, tau ~ 0.0166 i). Distinct "
                "elliptic structures; do not identify."
            ),
        },
        "objects": result,
        "no_fit": True,
        "precision_dps": mp.mp.dps,
    }
    path = os.path.join(os.path.dirname(__file__), "d14-theta-bar-side.witness.json")
    with open(path, "w") as fh:
        json.dump(witness, fh, indent=2)
    print(json.dumps(result, indent=2))
    print(f"\nwitness -> {path}")
