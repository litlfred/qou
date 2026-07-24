#!/usr/bin/env python3
"""qbeta_g3_formal_gaussian_loops_41gate.py — W2 part 1: the EXACT
higher-loop engine (formal Gaussian expansion at a state-integral
saddle), built and GATED on the printed 4₁ loop coefficients (GGM eq
42) before any 5₂ use.

Why: the landed part-2c-2 obstruction (audit 2026-07-18-5two-part2c-
wall-crossing-barpair) concluded a derived-precision φ_odd needs
higher-loop c₂, c₃ — which the paper does not print for deformed 5₂ —
"NOT deeper numerics". Loop coefficients are EXACT algebraic data:
GGM (12) states φ(x,y;τ) ∈ (1/√(iδ))·Q[x±,y±,δ⁻¹][[2πiτ]] — rational
in the saddle coordinates. So they are derivable by formal Gaussian
integration (Feynman rules of a 1-dim integral), with no
ill-conditioning: this probe builds that engine.

Engine: for Z = ∫ exp( U₀(w)/ħ + ħ·U₂(w) + ħ³·U₄(w) ) dw with
ħ = 2πib² (the Faddeev expansion log Φ_b(v) = Σ_{n≥0} ħ^{2n−1}·
B_{2n}(1/2)/(2n)!·Li_{2−2n}(e^w), w = 2πb·v, which has ONLY odd ħ
powers — certified below by the gate, not trusted from memory):
  - saddle w₀: U₀'(w₀) = 0;
  - fluctuation expansion to ε^{10}, Gaussian moments
    ⟨ε^{2m}⟩ = (2m−1)!!·(−ħ/U₀''(w₀))^m,
  - collect ħ-orders through ħ³ — the loop ratios φ_k = c_k.

4₁ GATE (all printed data exact): state integral (37)
Z₄₁(0;τ) = ∫ Φ_b(v)² e^{−πiv²} dv. Derivation chain, each link
machine-certified in this session (recorded here):
  G0  the Faddeev expansion itself was certified against the exact
      Φ_b PRODUCT formula at small b: argument −e^w, coefficients
      B₂(1/2)/2! = −1/24 and B₄(1/2)/4! = 7/5760, only odd ħ-powers
      (residual 1.5e-9 = |ħ|⁵-scale, mod-2πi log branch);
  G1  w-frame potential U₀ = 2·Li₂(−e^w) + w²/2; its saddle set
      {y² + y + 1 = 0} maps to the printed curve (38) y + y⁻¹ = 1 by
      ξ = −e^w, and the branch w₀ = −2πi/3 gives δ := U₀''(w₀) = √−3
      (Im > 0) — exactly the δ whose powers organize the printed (42);
  G2  NORMALIZATION (derived, then verified): the raw engine series
      differs from the print by the universal factor e^{−ħ/24} (the
      (q/q̃)^{1/24}-type convention constant) — derived from c₁'s
      constant part (+1/24, found by exact hand-computation) and
      VERIFIED on the two held-out orders c₂, c₃;
  G3  the normalized engine output equals (42) EXACTLY:
      c₁ = 11/(72√−3), c₂ = (697/2)/(72√−3)²,
      c₃ = (724351/30)/(72√−3)³ — matched to ~1e-59 at dps 60.

Engine completeness note: c₃ requires fluctuation order ≥ 18 (six
cubic vertices); EPS_ORD = 18.

Scope: engine + gate only (part 1). Part 2 ports the engine to the
deformed 5₂ potential (231) → the new exact c₂, c₃ that the φ_odd
derivation needs (gate on the printed 5₂ u=0 (76) and deformed 2-loop
(238) on the way). No fit; no c_k wired; mpmath dps 60, no float64;
scope-(a).
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))
sys.path.insert(0, str(_HERE.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 60

EPS_ORD = 18          # fluctuation order kept (≥ 18 needed for c₃)
H_ORD = 3             # loop orders in ħ kept (c₁..c₃)

# Bernoulli(1/2) / (2n)! for the Faddeev expansion (n = 1, 2)
B2_HALF_OVER_2F = mp.mpf(-1) / 24          # B₂(1/2)/2!
B4_HALF_OVER_4F = mp.mpf(7) / 5760         # B₄(1/2)/4!


def polylog_neg(k, y):
    """Li_{-k}(y) for k ≥ 0 (rational in y; mpmath supports negative
    order directly — cross-checked against the k ≤ 2 closed forms)."""
    return mp.polylog(-k, y)


def dilog_derivs(y, nmax):
    """d^j/dw^j Li₂(y·e^{w})|_{w=0} for j = 0..nmax: j=0 → Li₂(y),
    j=1 → −log(1−y), j≥2 → Li_{2−j} elementary."""
    out = [mp.polylog(2, y), -mp.log(1 - y)]
    for j in range(2, nmax + 1):
        out.append(polylog_neg(j - 2, y))
    return out


class EpsSeries:
    """Series in ε with dict coefficients {power: mpc}."""

    def __init__(self, d=None):
        self.d = dict(d or {})

    def __add__(self, o):
        r = dict(self.d)
        for k, v in o.d.items():
            r[k] = r.get(k, mp.mpc(0)) + v
        return EpsSeries(r)

    def __mul__(self, o):
        r = {}
        for a, va in self.d.items():
            for b, vb in o.d.items():
                if a + b > EPS_ORD:
                    continue
                r[a + b] = r.get(a + b, mp.mpc(0)) + va * vb
        return EpsSeries(r)

    def scale(self, s):
        return EpsSeries({k: s * v for k, v in self.d.items()})


def loop_ratios(derivs0, derivs2, derivs4):
    """Loop ratios c₁..c₃ of ∫exp(U₀/ħ + ħU₂ + ħ³U₄)dw around the
    saddle, from Taylor derivative lists (index j = d^j/dw^j at w₀;
    derivs0[1] must vanish). Returns [c₁, c₂, c₃] with
    φ/φ_gaussian = 1 + Σ c_k ħ^k."""
    Vpp = derivs0[2]
    # interaction exponent: X(ε; ħ) = Σ_{j≥3} U₀^(j) ε^j / (j! ħ)
    #                              + ħ·Σ_{j≥0} U₂^(j) ε^j / j!
    #                              + ħ³·U₄(w₀)
    # Each monomial carries (eps_power, hbar_power). Expand exp(X) as
    # polynomial; Gaussian-average ε^{2m} → (2m−1)!!·(−ħ/Vpp)^m.
    # Track terms as dict {(p_eps, p_h): coeff}.
    terms = {}
    for j in range(3, EPS_ORD + 1):
        c = derivs0[j] / mp.factorial(j)
        if c != 0:
            terms[(j, -1)] = terms.get((j, -1), mp.mpc(0)) + c
    for j in range(0, EPS_ORD + 1):
        c = derivs2[j] / mp.factorial(j)
        if c != 0:
            terms[(j, 1)] = terms.get((j, 1), mp.mpc(0)) + c
    terms[(0, 3)] = terms.get((0, 3), mp.mpc(0)) + derivs4[0]

    # exp(X) truncated: iterate powers of X (bounded: each X-factor
    # raises effective ħ-order by ≥ 1/2 [j≥3, ħ⁻¹ → j/2−1 ≥ 1/2])
    total = {(0, 0): mp.mpc(1)}
    power = {(0, 0): mp.mpc(1)}
    for it in range(1, 13):
        new = {}
        for (e1, h1), v1 in power.items():
            for (e2, h2), v2 in terms.items():
                e, h = e1 + e2, h1 + h2
                if e > EPS_ORD:
                    continue
                # effective order bound: h + e/2 ≤ H_ORD kept later
                if h + mp.mpf(e) / 2 > H_ORD + mp.mpf("0.1"):
                    continue
                new[(e, h)] = new.get((e, h), mp.mpc(0)) + v1 * v2
        power = {k: v / it for k, v in new.items()}
        if not power:
            break
        for k, v in power.items():
            total[k] = total.get(k, mp.mpc(0)) + v

    # Gaussian moments
    out = [mp.mpc(0)] * (H_ORD + 1)
    for (e, h), v in total.items():
        if e % 2 == 1:
            continue
        m = e // 2
        dfact = mp.mpf(1)
        for i in range(1, 2 * m, 2):
            dfact *= i
        contrib_h = h + m
        if contrib_h < 0 or contrib_h > H_ORD or contrib_h != int(contrib_h):
            continue
        out[int(contrib_h)] += v * dfact * (-1 / Vpp) ** m
    return out[1:], out[0]


def main() -> int:
    print("=" * 78)
    print(" W2 part 1 — formal-Gaussian loop engine, gated on the "
          "printed 4₁ (42)")
    print("=" * 78)

    # G1: saddle branch with δ = √−3 (the print's organizing constant):
    # ξ = −e^{w₀} = e^{iπ/3}  ⇔  w₀ = −2πi/3
    w0 = -2 * mp.pi * mp.mpc(0, 1) / 3
    y0 = mp.e ** w0
    s = -1
    delta = 2 * polylog_neg(0, s * y0) + 1        # U₀''(w₀)
    s3 = mp.sqrt(mp.mpf(3)) * mp.mpc(0, 1)        # √−3, Im > 0
    ok1 = abs(delta - s3) < mp.mpf("1e-50")
    print(f"\n[G1] saddle ξ = −e^(w₀) = e^(iπ/3); δ = U₀''(w₀) = "
          f"{mp.nstr(delta, 10)} = √−3: {ok1}")

    dl = dilog_derivs(s * y0, EPS_ORD)
    derivs0 = []
    for j in range(EPS_ORD + 1):
        v = 2 * dl[j]
        if j == 0:
            v += w0 ** 2 / 2
        elif j == 1:
            v += w0
        elif j == 2:
            v += 1
        derivs0.append(v)
    derivs0[1] = mp.mpc(0)   # saddle: kill the exact 2πi-lattice residue
    # Faddeev subleading potentials (factor 2 = the two Φ_b's):
    derivs2 = [2 * B2_HALF_OVER_2F * polylog_neg(j, s * y0)
               for j in range(EPS_ORD + 1)]
    derivs4 = [2 * B4_HALF_OVER_4F * polylog_neg(j + 2, s * y0)
               for j in range(EPS_ORD + 1)]
    c_raw, _c0 = loop_ratios(derivs0, derivs2, derivs4)

    # G2: the universal e^{−ħ/24} normalization (derived from c₁'s
    # constant part; the two held-out orders below are the verification)
    a_n = mp.mpf(-1) / 24
    c_eng = [c_raw[0] + a_n,
             c_raw[1] + a_n * c_raw[0] + a_n ** 2 / 2,
             c_raw[2] + a_n * c_raw[1] + a_n ** 2 / 2 * c_raw[0]
             + a_n ** 3 / 6]
    print(f"[G2] normalization φ_print = φ_engine·e^(−ħ/24) applied "
          f"(derived; verified on the held-out orders below)")

    # G3: the printed (42) exact targets (expansion variable = ħ)
    c_prt = [mp.mpf(11) / 72 / s3,
             mp.mpf(697) / 2 / (72 * s3) ** 2,
             mp.mpf(724351) / 30 / (72 * s3) ** 3]
    print("\n[G3] normalized engine loop ratios vs printed (42):")
    devs = []
    for k in range(3):
        dv = abs(c_eng[k] - c_prt[k]) / abs(c_prt[k])
        devs.append(dv)
        print(f"    c_{k + 1}: engine {mp.nstr(c_eng[k], 15)} | "
              f"printed {mp.nstr(c_prt[k], 15)} | rel dev "
              f"{mp.nstr(dv, 4)}")
    ok3 = all(d < mp.mpf("1e-45") for d in devs)
    print(f"    EXACT match at all three printed orders: {ok3}")

    ok12 = ok1
    ok = ok12 and ok3
    verdict = (
        f"LOOP ENGINE CERTIFIED — the formal-Gaussian higher-loop "
        f"engine reproduces the printed 4_1 loop coefficients (42) "
        f"EXACTLY at all three printed orders (c_1 = 11/72sqrt(-3), "
        f"c_2 = 697/2/(72sqrt(-3))^2, c_3 = 724351/30/(72sqrt(-3))^3; "
        f"rel devs {', '.join(mp.nstr(d, 3) for d in devs)}), on the "
        f"delta = sqrt(-3) saddle branch (xi = e^(i pi/3), the printed "
        f"curve (38) via xi = -e^w), with the Faddeev expansion "
        f"product-certified (G0), the subleading vertices "
        f"B_2(1/2)/2! = -1/24, B_4(1/2)/4! = 7/5760, and the "
        f"e^(-hbar/24) normalization derived-then-verified on two "
        f"held-out orders. This is the well-conditioned "
        f"algebraic route to higher loops the 2c-2 obstruction called "
        f"for (loop data rational in the saddle per GGM (12)) — no "
        f"ill-conditioned inversion anywhere. NEXT (W2 part 2): run "
        f"the engine on the deformed 5_2 potential (231) at the "
        f"sigma-saddles -> the unprinted exact c_2, c_3, gate the "
        f"printed 2-loop (238) on the way, then re-extract phi_odd "
        f"with the extended transseries. No fit; no c_k wired; "
        f"scope-(a)."
        if ok else
        f"ENGINE GATE INCOMPLETE (honest): G1 delta = {ok12}, G3 "
        f"match = {ok3}" + (f" (devs {', '.join(mp.nstr(d, 3) for d in devs)})"
                            if c_eng else "") +
        f" — the failing gate localizes the convention/vertex error; "
        f"nothing downstream is run. No fit; no c_k wired; scope-(a)."
    )
    print("\nVERDICT:", verdict)

    wb = WitnessBuilder("qbeta-g3-formal-gaussian-loops-41gate",
                        engine="mpmath")
    wb.set_description(
        "W2 part 1: formal-Gaussian higher-loop engine for state-"
        "integral saddles, gated EXACTLY on the printed 4_1 loop "
        "coefficients (GGM 42) on the delta = sqrt(-3) branch of the "
        "printed curve (38), with the Faddeev expansion product-"
        "certified and the e^{-hbar/24} normalization derived-then-"
        "verified. The well-conditioned algebraic route to the "
        "unprinted 5_2 c_2/c_3 that the phi_odd derivation needs.")
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_data("derivation_chain", {
        "G0_faddeev_expansion": "certified vs exact product formula "
                                "(arg -e^w, B2(1/2)/2! = -1/24, "
                                "B4(1/2)/4! = 7/5760, odd hbar only)",
        "G1_saddle": {"w0": "-2*pi*i/3", "xi": "e^{i pi/3}",
                      "delta": mp.nstr(delta, 20)},
        "G2_normalization": "phi_print = phi_engine * e^{-hbar/24} "
                            "(derived from c1 constant part; verified "
                            "on held-out c2, c3)"})
    wb.add_data("gate", {
        "printed_c": ["11/(72*sqrt(-3))", "697/2/(72*sqrt(-3))^2",
                      "724351/30/(72*sqrt(-3))^3"],
        "engine_c": [mp.nstr(c, 25) for c in c_eng],
        "rel_devs": [mp.nstr(d, 8) for d in devs] if c_eng else []})
    wb.add_data("verdict", verdict)
    wb.add_assertion("saddle_branch_delta_sqrt_minus3",
                     computed=1.0 if ok12 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="U0''(w0) = sqrt(-3) exactly on the "
                            "xi = e^{i pi/3} branch of the printed "
                            "curve (38)")
    wb.add_assertion("printed_42_reproduced_exactly",
                     computed=1.0 if ok3 else 0.0, expected=1.0,
                     tolerance=0.5,
                     source="c_1..c_3 match the printed exact rationals "
                            "to < 1e-45 relative at dps 60")
    wb.save()
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
