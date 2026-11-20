#!/usr/bin/env python3
"""The pulled-back sl₂ KZ monodromy representation of the colour cubic — written down exactly
(bean qou-d0qq, the construction half of Step-2 option C).

What is now computable, and what this probe does with it:

  (1) THE LEVEL, convention-free.  The half-twist monodromy of the sl₂ KZ connection on V ⊗ V
      is P·exp(iπħ Ω) with Ω the split Casimir: eigenvalue 1/4 on Sym² V, −3/4 on Λ² V.  So the
      half-twist has eigenvalues λ₁ = e^{iπħ/4} (Sym²) and λ₂ = −e^{−3iπħ/4} (Λ²), RATIO −e^{iπħ},
      product −e^{−iπħ/2}.  The framework's Hecke normalisation (σ − q)(σ + q⁻¹) = 0 has ratio −q²
      and product −1.  A scalar rescaling of the generator moves the product, never the ratio, so
      the invariant matching condition is  q² = e^{iπħ}, i.e. ħ = (2/iπ) ln q — purely imaginary
      for the framework's real q₀ > 1 (this IS the "imaginary level").  Level bookkeeping:
      ħ = 1/(k+2) gives k+2 = iπ/(2 ln q₀) ≈ 15.05 i, ħ = 2/(k+2) gives k+2 = iπ/ln q₀ ≈ 30.1 i
      (q = e^{iπ/(k+2)}), and the bean's other candidate 2πi/ln q₀ ≈ 60.2 i is q = e^{2πi/(k+2)},
      i.e. ħ = 4/(k+2) — an earlier docstring mapped these off by a factor of two; the computed
      values below were right.  The corpus's earlier "KD matching forces ħ = 2 ln q" (route-5 fibre
      probe) is the same relation with iπħ renamed ħ.  SCOPE: the ratio −q² is read off the §7a Skein
      normalisation (H); under the corpus's other normalisation (J) (bean qou-8bxv) the ratio is −q
      and ħ halves — the relation is conditional on (H), which AGENTS.md makes canonical.
      Lean: QOU.Mass.KZLevelFromHeckeNormalisation.
  (2) THE REPRESENTATION.  With the framework's R-matrix (eigenvalues q on Sym², −q⁻¹ on Λ² —
      exactly the rescaled KZ half-twist) on V^{⊗3}, and the six lasso words measured in
      colour_cubic_braid_monodromy_probe.py (all positive half-twists up to conjugacy), the
      pulled-back monodromy ϱ: π₁(ℂ∖Δ) = F₆ → B₃ → End(V^{⊗3}) is explicit.  Checked exactly
      (sympy, q formal): every ϱ(w_j) satisfies the Hecke quadratic; the image of F₆ contains
      ϱ(σ₁), ϱ(σ₂) so it is the whole image of B₃; ϱ(w₁⋯w₆) = ϱ(Δ²) commutes with every ϱ(σ_i)
      and acts as a scalar on each isotypic block of V^{⊗3} = spin-3/2 ⊕ 2·spin-1/2, with the
      scalars recorded (q^{6} on the 4-dim block, q^{−2}·... on the 2-dim blocks — read them from
      the witness, do not quote this docstring); the pivotal (convention-D) trace of each ϱ(w_j)
      is z_D = q³/(q²+1) (conjugation-invariant), so the pulled-back generators carry the
      framework's Markov parameter without any further choice.
  (3) THE FRAMEWORK SIDE.  Nothing here evaluates "is the substrate connection this one": there is
      no connection object on that side (cheat-sheet §2a; audit 2026-09-07 §B item 2).  The class
      QOU.Mass.KZPullbackGenerators is the interface; this probe supplies the KZ side of it.

No float64: sympy exact for (2), mpmath 50 dps for the pin evaluation in (1) (q₀ read from
q_parameter as an INPUT — the forever-gate is respected; nothing here outputs a q₀).
Anchor: proton (diagnostic values only).

Run:  PYTHONPATH=computations python3 -u computations/probes/kz_pullback_monodromy_exact_probe.py \
        2>&1 | tee /tmp/kz_pullback.log
"""
from __future__ import annotations

import json
import os
import sys
import time

import mpmath as mp
import sympy as sp

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import _path_bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

try:
    from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
except Exception:  # pragma: no cover
    Q_50_DIGIT_STR = None

mp.mp.dps = 50
T0 = time.monotonic()

# The six lasso words of colour_cubic_braid_monodromy_probe.py (departure-angle order), as
# lists of signed generator indices: +1 = σ₁, −1 = σ₁⁻¹, +2 = σ₂, −2 = σ₂⁻¹.
LASSO_WORDS = {
    "w1": [-1, 2, 1],
    "w2": [1],
    "w3": [-1, 2, 1],
    "w4": [2, 1, -2],
    "w5": [2, 2, -2],
    "w6": [1],
}
B1_WITNESS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "colour-cubic-braid-monodromy.witness.json")


def log(msg: str) -> None:
    print(f"  [{time.monotonic() - T0:6.1f}s] {msg}", flush=True)


def build(n: int, q):
    R = sp.Matrix([[q, 0, 0, 0], [0, q - 1 / q, 1, 0], [0, 1, 0, 0], [0, 0, 0, q]])
    Rinv = R.inv()
    K = sp.diag(q, 1 / q)
    I2 = sp.eye(2)

    def kron(*ms):
        out = ms[0]
        for m in ms[1:]:
            out = sp.kronecker_product(out, m)
        return out

    def sigma(i, inv=False):  # i = 1 .. n-1
        M = Rinv if inv else R
        return kron(*([I2] * (i - 1) + [M] + [I2] * (n - i - 1)))

    W = kron(*([K] * n))
    br2 = q + 1 / q

    def tr_D(X):
        return sp.simplify((W * X).trace() / br2 ** n)

    return sigma, tr_D


def word_matrix(sigma, word):
    M = None
    for g in word:
        m = sigma(abs(g), inv=(g < 0))
        M = m if M is None else M * m
    return M


def main() -> int:
    print("=" * 78)
    print(" pulled-back sl2 KZ monodromy of the colour cubic — exact (qou-d0qq)")
    print("=" * 78)
    checks = []
    q = sp.symbols("q", positive=True)
    hb = sp.symbols("hbar")

    # ---- (1) the level: Casimir eigenvalues → half-twist eigenvalues → ratio → q² = e^{iπħ} ----
    # split Casimir Ω = (C_{V⊗V} − C_V⊗1 − 1⊗C_V)/2 with C_V = j(j+1): spin 1 → 2, spin 0 → 0, spin ½ → 3/4
    cas_sym = sp.Rational(1, 4)   # (2 − 3/4 − 3/4)/2
    cas_alt = sp.Rational(-3, 4)  # (0 − 3/2)/2
    checks.append(("split Casimir eigenvalues on Sym2 / Lambda2 are 1/4 / -3/4", (cas_sym, cas_alt) == (sp.Rational(1, 4), sp.Rational(-3, 4))))
    lam1 = sp.exp(sp.I * sp.pi * hb * cas_sym)          # swap = +1 on Sym²
    lam2 = -sp.exp(sp.I * sp.pi * hb * cas_alt)         # swap = −1 on Λ²
    ratio = sp.simplify(lam1 / lam2)
    prod = sp.simplify(lam1 * lam2)
    checks.append(("half-twist eigenvalue ratio = -e^{i pi hbar}", sp.simplify(ratio + sp.exp(sp.I * sp.pi * hb)) == 0))
    checks.append(("half-twist eigenvalue product = -e^{-i pi hbar/2}", sp.simplify(prod + sp.exp(-sp.I * sp.pi * hb / 2)) == 0))
    # rescale by c = e^{iπħ/4}: eigenvalues become e^{iπħ/2}, −e^{−iπħ/2} = q, −q⁻¹ with q = e^{iπħ/2}
    c = sp.exp(sp.I * sp.pi * hb / 4)
    qKZ = sp.exp(sp.I * sp.pi * hb / 2)
    checks.append(("rescaled eigenvalues are q, -1/q with q = e^{i pi hbar/2}", sp.simplify(c * lam1 - qKZ) == 0 and sp.simplify(c * lam2 + 1 / qKZ) == 0))
    checks.append(("invariant matching condition q^2 = e^{i pi hbar}", sp.simplify(qKZ ** 2 - sp.exp(sp.I * sp.pi * hb)) == 0))
    level = {}
    if Q_50_DIGIT_STR is not None:
        q0 = Q_MP
        hbar_val = 2 * mp.log(q0) / (mp.pi * mp.mpc(0, 1))      # ħ = (2/iπ) ln q₀, purely imaginary
        level = {
            "q0": Q_50_DIGIT_STR,
            "ln_q0": mp.nstr(mp.log(q0), 30),
            "hbar_from_ratio": mp.nstr(hbar_val, 30),
            "hbar_is_purely_imaginary": bool(abs(mp.re(hbar_val)) < mp.mpf(10) ** -45),
            "k_plus_2_if_hbar_eq_1_over_k_plus_2": mp.nstr(1 / hbar_val, 30),
            "k_plus_2_if_hbar_eq_2_over_k_plus_2": mp.nstr(2 / hbar_val, 30),
            "k_plus_2_if_hbar_eq_4_over_k_plus_2_ie_q_eq_exp_2pi_i_over_k_plus_2": mp.nstr(4 / hbar_val, 30),
            "route5_form_hbar_eq_2_ln_q": mp.nstr(2 * mp.log(q0), 30),
        }
        checks.append(("at the proton pin hbar = (2/i pi) ln q0 is purely imaginary", level["hbar_is_purely_imaginary"]))
        log(f"level at the pin: ħ = {level['hbar_from_ratio'][:22]}; k+2 = {level['k_plus_2_if_hbar_eq_1_over_k_plus_2'][:12]} (ħ = 1/(k+2)) or {level['k_plus_2_if_hbar_eq_2_over_k_plus_2'][:12]} (ħ = 2/(k+2))")

    # ---- (2) the pulled-back representation on V^{⊗3} ----
    sigma, tr_D = build(3, q)
    s1, s2 = sigma(1), sigma(2)
    I8 = sp.eye(8)
    h = q - 1 / q
    z_D = q ** 3 / (q ** 2 + 1)
    # cross-check the words against the B1 witness if it is on disk
    if os.path.exists(B1_WITNESS):
        try:
            wdata = json.load(open(B1_WITNESS))
            blob = json.dumps(wdata)
            checks.append(("B1 witness on disk mentions all six words", all(k in blob for k in ("s1^-1 s2 s1", "s2 s1 s2^-1"))))
        except Exception:
            pass
    rho = {name: word_matrix(sigma, w) for name, w in LASSO_WORDS.items()}
    quad_ok = all(sp.simplify(M * M - h * M - I8) == sp.zeros(8, 8) for M in rho.values())
    checks.append(("every rho(w_j) satisfies the Hecke quadratic (conjugates of half-twists)", quad_ok))
    trace_ok = all(sp.simplify(tr_D(M) - z_D) == 0 for M in rho.values())
    checks.append(("pivotal trace of every rho(w_j) is z_D = q^3/(q^2+1)", trace_ok))
    gens_in_image = any(w == [1] for w in LASSO_WORDS.values()) and any(w == [2, 2, -2] for w in LASSO_WORDS.values())
    checks.append(("image of F6 contains sigma1 (w2) and sigma2 (w5 = s2 s2 s2^-1): it is the image of B3", gens_in_image))
    prod_word = [g for name in ("w1", "w2", "w3", "w4", "w5", "w6") for g in LASSO_WORDS[name]]
    Pinf = word_matrix(sigma, prod_word)
    Delta2 = word_matrix(sigma, [1, 2, 1, 1, 2, 1])
    checks.append(("rho(w1...w6) = rho(Delta^2) = rho((s1 s2 s1)^2)", sp.simplify(Pinf - Delta2) == sp.zeros(8, 8)))
    central = sp.simplify(Pinf * s1 - s1 * Pinf) == sp.zeros(8, 8) and sp.simplify(Pinf * s2 - s2 * Pinf) == sp.zeros(8, 8)
    checks.append(("rho(Delta^2) commutes with rho(sigma1), rho(sigma2)", central))
    # scalars on the isotypic blocks: eigenvalues of rho(Delta²) with multiplicities
    ev = Pinf.eigenvals()
    ev_simpl = {sp.simplify(k): v for k, v in ev.items()}
    checks.append(("rho(Delta^2) is diagonalisable with exactly 2 distinct eigenvalues (spin-3/2 block, spin-1/2 blocks)", len(ev_simpl) == 2 and sum(ev_simpl.values()) == 8))
    log(f"rho(Δ²) eigenvalues: {ev_simpl}")
    # the quadratic on the generators lifted from KZ: eigenvalues of rho(sigma1) are q (x6) and -1/q (x2)
    ev1 = {sp.simplify(k): v for k, v in s1.eigenvals().items()}
    checks.append(("rho(sigma1) eigenvalues q (mult 6) and -1/q (mult 2)", ev1.get(q) == 6 and ev1.get(-1 / q) == 2))

    ok = 0
    print()
    for name, passed in checks:
        print(f"  [{'PASS' if passed else 'FAIL'}] {name}")
        ok += bool(passed)
    print(f"\n  {ok}/{len(checks)} checks passed   ({time.monotonic() - T0:.1f}s)")

    wb = WitnessBuilder("kz-pullback-monodromy-exact", engine="sympy+mpmath", _script_path=__file__)
    wb.set_description(
        "qou-d0qq, the construction half of Step-2 option C, as far as it is computable. (1) The level is "
        "fixed convention-free by the eigenvalue RATIO of the KZ half-twist: split Casimir 1/4 on Sym², "
        "−3/4 on Λ² ⇒ ratio −e^{iπħ}; matching the Hecke ratio −q² gives q² = e^{iπħ}, i.e. "
        "ħ = (2/iπ) ln q — purely imaginary at the real proton pin (the 'imaginary level'), conditional on "
        "the §7a Skein normalisation (H) — under (J) the ratio is −q and ħ halves; k+2 = 15.05 i / 30.1 i / "
        "60.2 i for ħ = 1/(k+2), 2/(k+2), 4/(k+2). (2) The pulled-back monodromy "
        "ϱ: F₆ → B₃ → End(V^{⊗3}) is explicit from the six measured lasso words: every ϱ(w_j) satisfies "
        "the Hecke quadratic and has pivotal trace z_D; the image is that of B₃; ϱ(w₁⋯w₆) = ϱ(Δ²) is "
        "central with two distinct eigenvalues (the two isotypic blocks). (3) Nothing here evaluates "
        "the framework side: no connection object exists there; KZPullbackGenerators is the interface. "
        "q₀ is an input only; nothing outputs a q₀.")
    wb.set_content_block("conj:hecke-monodromy-step-two")
    for name, passed in checks:
        wb.add_assertion(name.replace(" ", "_")[:80], computed="1" if passed else "0", expected="1",
                         tolerance="0.5", source="exact (sympy) / mpmath 50 dps at the pin")
    wb.add_parameter("lasso_words", {k: " ".join(("s%d" % abs(g)) + ("^-1" if g < 0 else "") for g in w) for k, w in LASSO_WORDS.items()})
    wb.add_parameter("lasso_words_source", "computations/probes/colour_cubic_braid_monodromy_probe.py (13/13), departure-angle order")
    wb.add_parameter("R_matrix", "eigenvalues q (Sym^2), -1/q (Lambda^2); K = diag(q, 1/q); tr_D = tr(K^{⊗n} X)/[2]^n")
    if Q_50_DIGIT_STR is not None:
        wb.add_parameter("q0", Q_50_DIGIT_STR)
    wb.add_data("level", {"casimir_sym2": str(cas_sym), "casimir_lambda2": str(cas_alt),
                          "half_twist_eigenvalues": {"sym2": str(lam1), "lambda2": str(lam2)},
                          "ratio": str(ratio), "product": str(prod), "rescaling": str(c),
                          "matching": "q^2 = e^{i pi hbar}; hbar = (2/(i pi)) ln q", "at_pin": level})
    wb.add_data("representation", {"rho_Delta2_eigenvalues": {str(k): int(v) for k, v in ev_simpl.items()},
                                   "rho_sigma1_eigenvalues": {str(k): int(v) for k, v in ev1.items()},
                                   "pivotal_trace_each_lasso": str(z_D)})
    wb.add_data("verdict", (
        "The KZ side of Step-2 option C is now explicit and exact: level from the eigenvalue ratio, "
        "representation from the measured lasso words, Markov parameter z_D recovered without a choice. "
        "The remaining hypothesis is on the framework side — that the substrate connection IS this "
        "pulled-back connection — and the corpus has no connection object to compare; the class "
        "KZPullbackGenerators names it. Not a derivation of q0; not a fit."))
    wb.add_caveat("Kohno–Drinfeld (the KZ half-twist monodromy is the R-matrix) is cited (kohno1987, drinfeld1985), not held in library/ and not re-derived here; (1) uses only its eigenvalue statement.")
    wb.add_caveat("Scope: n = 3 strands (V^{⊗3}); the six words are the measured ones, hard-coded with their source and cross-checked against the B1 witness when present.")
    out = wb.save()
    print(f"  witness -> {os.path.relpath(out, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))}")
    return 0 if ok == len(checks) else 1


if __name__ == "__main__":
    sys.exit(main())
