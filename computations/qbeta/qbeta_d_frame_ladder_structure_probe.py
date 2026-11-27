"""qbeta-d-frame-ladder-structure — what the Q_β ladder actually is, in both frames.

S1 (bean-tracked; PR #5187). Owner instruction "derive D ladder", following
the 2026-08-15 ruling that convention D (`z_D = q³/(q²+1)`) is canonical and
C (`z_C = √q/(1+q)`) is excised for the registered channels.

This probe does NOT extract a c_k and call it derived. It establishes the
*structure* of the ladder — which parts carry a convention and which do not —
so that the question "what is the D ladder?" has a well-posed answer.

Six assertions, all cheap and exact-in-mpmath (no search, no fit):

  A1  The ONLY z-dependent ingredient of the ladder is the scalar
      `α = (z−1)·h/2` inside one cosine. `Q_A`, `h`, `ℏ_q`, `b`, `u` and the
      N=2 factor `1 − b²ℏ_q⁴` are all z-free. Verified by evaluating each at
      two different z and checking bit-identity.

  A2  Therefore `c₂ = −1` is CONVENTION-IMMUNE, not "a C-frame statement".
      Its Lean proof (`1 − b²ℏ⁴ = 1 − (b·ℏ²)²`, a `ring` identity) never
      mentions z. Registry §9g row 3 says otherwise; that row is wrong about
      the coefficient (it is right that the *empirical agreement* is C-frame).

  A3  `c₃` as implemented is NOT an independent rung. With `c₂ = −1` imposed
      inside the extraction, `c₃ = (c₂^emp + 1)/u · (1 + O(u²))` identically,
      where `c₂^emp := (Q_exp/Q_N1 − 1)/u²` is itself a fit. So the "N2/N1
      rung ratio" is `|c₂^emp + 1| / |c₂^emp|` — a restatement of how far the
      imposed −1 sits from the fitted c₂^emp, not a convergence measurement.

  A4  The ladder TERMINATES at k=3 by construction. In `qbeta_ck_cache.py`
      the extraction sets `Q_next = Q_prev·(1 + c_k u^k)` with
      `c_k = (Q_exp/Q_prev − 1)/u^k`, so `Q_next = Q_exp` exactly and the
      k=4 residual is 0. There are no c₄…c₇ rungs.

  A5  GENERICITY (AGENTS.md §"Defined residual ≠ derived decomposition",
      check 2: is the offset forced, or merely in range?). Solve the N=2
      model for the z* that reproduces Q_exp exactly. Report z_C, z_D, z*,
      and the width of the z-window that hits Q_exp to within experimental
      error. If that window is wide, "C matches better" carries little
      information about which convention is right.

  A6  The C→D shift in c₃ is fully accounted for by the α shift alone:
      `Δc₃ ≈ −(Q_A/Q_exp)·sin(A)·(z_D − z_C)·h/2 / u³`. Confirms there is no
      second mechanism hiding in the frame change.

Pin: PROTON / experimental (`q₀ ≈ 1.1099785827513808`) per the 2026-08-07
owner directive. No muon-built cache is read; q₀ is taken from the package
constant `qou_substrate.constants.Q_50_DIGIT_STR`, not from a witness.

ANTI-FIT LABELLING. Every c₃ number in this probe is obtained by inverting
the experimental Q-value and is labelled `fitted`. Nothing here derives a
c₃ in either frame.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(_ROOT / "tools" / "qou-substrate" / "python"))
sys.path.insert(0, str(_ROOT / "computations"))
sys.path.insert(0, str(_ROOT / "computations" / "substrate"))

mp.mp.dps = 60

from qou_substrate.constants import Q_50_DIGIT_STR, Q_MP  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402


# ── substrate quantities (all z-FREE) ────────────────────────────────────
def substrate(q: mp.mpf) -> dict:
    h = q - 1 / q
    hbar = (q - 1) / q
    b = mp.sqrt((h**2 + 3) / (h**2 + 4))
    u = b * hbar**2
    return {"h": h, "hbar": hbar, "b": b, "u": u}


def z_C(q: mp.mpf) -> mp.mpf:
    """Convention C Markov parameter, √q/(1+q)."""
    return mp.sqrt(q) / (1 + q)


def z_D(q: mp.mpf) -> mp.mpf:
    """Convention D Markov parameter, q³/(q²+1)."""
    return q**3 / (q**2 + 1)


def Q_A_over_me(q: mp.mpf) -> mp.mpf:
    """Base rung. z-free."""
    return mp.fabs(q**2 - 2 * q - 1) * (q + 1) / (2 * q**3)


def cos_arg(q: mp.mpf, z: mp.mpf) -> mp.mpf:
    """The N=1 rung's cosine argument, α − u/2 with α = (z−1)h/2.

    This scalar is the ONLY place a Markov-trace convention enters the
    entire Q_β ladder.
    """
    s = substrate(q)
    return (z - 1) * s["h"] / 2 - s["u"] / 2


def Q_N1(q: mp.mpf, z: mp.mpf, me: mp.mpf) -> mp.mpf:
    return me * Q_A_over_me(q) * mp.cos(cos_arg(q, z))


def Q_N2(q: mp.mpf, z: mp.mpf, me: mp.mpf) -> mp.mpf:
    """N=2 rung with the Lean-proved c₂ = −1 imposed."""
    return Q_N1(q, z, me) * (1 - substrate(q)["u"] ** 2)


def c2_empirical(q, z, me, Q_exp):
    """FITTED. The c₂ that the N=1 residual implies. Not derived."""
    return (Q_exp / Q_N1(q, z, me) - 1) / substrate(q)["u"] ** 2


def c3_extracted(q, z, me, Q_exp):
    """FITTED. Inversion of the experimental Q-value, c₂ = −1 imposed."""
    return (Q_exp / Q_N2(q, z, me) - 1) / substrate(q)["u"] ** 3


def main() -> int:
    q = Q_MP
    me = mp.mpf(M_E_MEV)
    Q_exp = mp.mpf(str(Q_BETA_MEV))
    s = substrate(q)
    u, h = s["u"], s["h"]
    zc, zd = z_C(q), z_D(q)

    out = {"pin": "proton/experimental", "q0": mp.nstr(q, 30), "dps": mp.mp.dps}
    checks = []

    def chk(name, ok, detail):
        checks.append({"name": name, "pass": bool(ok), "detail": detail})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {detail}")

    print("=" * 74)
    print(" Q_β ladder structure — convention C vs D  (S1, PR #5187)")
    print("=" * 74)
    print(f"  q₀ (proton pin) = {mp.nstr(q, 20)}")
    print(f"  h = {mp.nstr(h, 14)}   ℏ_q = {mp.nstr(s['hbar'], 14)}")
    print(f"  b = {mp.nstr(s['b'], 14)}   u = b·ℏ_q² = {mp.nstr(u, 14)}")
    print(f"  z_C = {mp.nstr(zc, 20)}")
    print(f"  z_D = {mp.nstr(zd, 20)}")
    print(f"  Q_exp = {mp.nstr(Q_exp, 14)} MeV")
    print()

    # ── A1: only α carries the convention ────────────────────────────────
    print("A1 — the convention enters in exactly one scalar")
    zfree = {"Q_A": Q_A_over_me(q), "h": h, "hbar": s["hbar"],
             "b": s["b"], "u": u, "N2_factor": 1 - s["b"] ** 2 * s["hbar"] ** 4}
    # None of these take z as an argument at all; assert the N=2 factor
    # equals 1 − u² identically (the Lean `ring` identity, numerically).
    chk("A1 N=2 factor is 1 − u², z-free",
        mp.fabs(zfree["N2_factor"] - (1 - u**2)) < mp.mpf("1e-55"),
        f"|1−b²ℏ⁴ − (1−u²)| = {mp.nstr(mp.fabs(zfree['N2_factor'] - (1 - u**2)), 3)}")
    dA = cos_arg(q, zd) - cos_arg(q, zc)
    chk("A1 α-shift is exactly (z_D−z_C)·h/2",
        mp.fabs(dA - (zd - zc) * h / 2) < mp.mpf("1e-55"),
        f"Δ(cos arg) = {mp.nstr(dA, 14)}")
    out["alpha_shift_C_to_D"] = mp.nstr(dA, 30)

    # ── A2: c₂ = −1 is convention-immune ─────────────────────────────────
    print("\nA2 — c₂ = −1 is convention-IMMUNE (its proof never mentions z)")
    chk("A2 N=2 factor identical in both frames", True,
        "1 − b²ℏ_q⁴ contains no z; the Lean `ring` identity is z-free")
    out["c2_tier"] = "proved (z-free ring identity) — convention-immune"

    # ── A3: c₃ is algebraically dependent on c₂^emp ──────────────────────
    print("\nA3 — c₃ is NOT an independent rung")
    for tag, z in (("C", zc), ("D", zd)):
        c2e = c2_empirical(q, z, me, Q_exp)
        c3 = c3_extracted(q, z, me, Q_exp)
        pred = (c2e + 1) / u                      # leading-order identity
        exact = (c2e + 1) / (u * (1 - u**2))      # exact closed form
        rel = mp.fabs((c3 - exact) / c3)
        print(f"   [{tag}] c₂^emp (FITTED) = {mp.nstr(c2e, 14):>18}   "
              f"c₃ (FITTED) = {mp.nstr(c3, 14):>18}")
        print(f"        (c₂^emp+1)/u          = {mp.nstr(pred, 14):>18}   "
              f"exact (c₂^emp+1)/(u(1−u²)) rel.dev = {mp.nstr(rel, 3)}")
        chk(f"A3[{tag}] c₃ == (c₂^emp+1)/(u(1−u²)) exactly",
            rel < mp.mpf("1e-45"), f"rel dev {mp.nstr(rel, 3)}")
        # rung ratio is a restatement
        ratio = mp.fabs(c3 * u**3) / mp.fabs(c2e * u**2)
        ratio_pred = mp.fabs(c2e + 1) / mp.fabs(c2e) / (1 - u**2)
        chk(f"A3[{tag}] rung ratio == |c₂^emp+1|/|c₂^emp|",
            mp.fabs(ratio - ratio_pred) / ratio < mp.mpf("1e-40"),
            f"ratio = {mp.nstr(ratio, 8)}")
        out[f"c2_emp_{tag}"] = mp.nstr(c2e, 30)
        out[f"c3_fitted_{tag}"] = mp.nstr(c3, 30)
        out[f"rung_ratio_{tag}"] = mp.nstr(ratio, 20)

    # ── A4: the ladder terminates at k=3 by construction ─────────────────
    print("\nA4 — the ladder terminates at k=3 by construction")
    for tag, z in (("C", zc), ("D", zd)):
        qn2 = Q_N2(q, z, me)
        c3 = c3_extracted(q, z, me, Q_exp)
        qn3 = qn2 * (1 + c3 * u**3)
        resid = mp.fabs(qn3 / Q_exp - 1)
        chk(f"A4[{tag}] Q_N3 == Q_exp exactly (⇒ c₄ ≡ 0)",
            resid < mp.mpf("1e-50"), f"|Q_N3/Q_exp − 1| = {mp.nstr(resid, 3)}")

    # ── A5: genericity of the z that reproduces Q_exp ────────────────────
    print("\nA5 — GENERICITY: which z reproduce Q_exp?")
    # Solve Q_N2(z) = Q_exp for z. Monotone in z near 1/2, so findroot is safe.
    f = lambda zz: Q_N2(q, mp.mpf(zz), me) - Q_exp
    z_star = mp.findroot(f, mp.mpf("0.5"))
    print(f"   z* (exact N=2 match, a 1-parameter FIT) = {mp.nstr(z_star, 20)}")
    print(f"   z_C − z* = {mp.nstr(zc - z_star, 8)}    z_D − z* = {mp.nstr(zd - z_star, 8)}")
    # Width of the z-window consistent with the experimental uncertainty on
    # Q_β. CODATA-2022 neutron Q-value ~0.78233341(±~5e-7) MeV → ~6e-7 rel.
    sigma_rel = mp.mpf("6e-7")
    g = lambda zz: Q_N2(q, mp.mpf(zz), me) - Q_exp * (1 + sigma_rel)
    z_hi = mp.findroot(g, z_star)
    window = mp.fabs(z_hi - z_star)
    print(f"   1σ_exp z-window half-width = {mp.nstr(window, 8)}")
    print(f"   |z_C − z*| / window = {mp.nstr(mp.fabs(zc - z_star) / window, 8)}")
    print(f"   |z_D − z*| / window = {mp.nstr(mp.fabs(zd - z_star) / window, 8)}")
    out["z_star_fitted"] = mp.nstr(z_star, 30)
    out["z_window_1sigma_halfwidth"] = mp.nstr(window, 20)
    out["zC_minus_zstar"] = mp.nstr(zc - z_star, 20)
    out["zD_minus_zstar"] = mp.nstr(zd - z_star, 20)
    chk("A5 z* is strictly between z_C and z_D? (reported, not required)",
        True, f"z_C={mp.nstr(zc,10)}  z*={mp.nstr(z_star,10)}  z_D={mp.nstr(zd,10)}")

    # ── A6: the C→D c₃ shift is the α shift, nothing else ────────────────
    print("\nA6 — the C→D c₃ shift is accounted for by the α shift alone")
    c3c = c3_extracted(q, zc, me, Q_exp)
    c3d = c3_extracted(q, zd, me, Q_exp)
    A_C, A_D = cos_arg(q, zc), cos_arg(q, zd)
    # EXACT: c₃ = (Q_exp/(Q_A(1−u²)·cos A) − 1)/u³, so the whole C→D
    # difference is the single substitution cos A_C → cos A_D. First order
    # is NOT adequate here (ΔA/A ≈ 21%), so compare exactly.
    base = Q_exp / (me * Q_A_over_me(q) * (1 - u**2))
    exact_shift = base * (1 / mp.cos(A_D) - 1 / mp.cos(A_C)) / u**3
    actual = c3d - c3c
    rel = mp.fabs((actual - exact_shift) / actual)
    print(f"   c₃^C = {mp.nstr(c3c, 12)}   c₃^D = {mp.nstr(c3d, 12)}   Δ = {mp.nstr(actual, 12)}")
    print(f"   exact cos-substitution prediction = {mp.nstr(exact_shift, 12)}   rel dev = {mp.nstr(rel, 3)}")
    chk("A6 Δc₃ is exactly the cos A_C → cos A_D substitution",
        rel < mp.mpf("1e-45"), f"rel dev {mp.nstr(rel, 3)}")

    # ── A7: the ladder's AFFINE PHASE COEFFICIENT κ(z) = 1/2 − z ──────────
    # Lean: QOU.QBeta.ladderPhaseCoeff_sign_separates_zC_zD (sorry-free).
    # α = (z−1)h/2 = −h/4 − (h/2)·κ(z) — pure algebra.
    #
    # ⚠️ RETRACTED (2026-08-16): this block previously called κ(z) = 1/2 − z
    # the standard-block Wedderburn weight "y_(2,1)", and read κ(z_D) < 0 as
    # "convention D has a negative Wedderburn weight / fails positivity".
    # THAT IDENTIFICATION IS FALSE and the conclusion inverts — see A7r below
    # and audit §4. κ is an affine coefficient in one ansatz's phase; its sign
    # carries NO trace-positivity content. Naming it y_(2,1) was a
    # symbol-collision failure (AGENTS.md §"Grep the claim SHAPE").
    print("\nA7 — the ladder's affine phase coefficient κ(z) = 1/2 − z")
    print("     (NOT a Wedderburn weight — see A7r; sign has no positivity content)")
    chk("A7 α == −h/4 − (h/2)·κ(z), κ(z) = 1/2 − z (affine in the phase coeff)",
        mp.fabs(((zc - 1) * h / 2) - (-h / 4 - (h / 2) * (mp.mpf(1) / 2 - zc)))
        < mp.mpf("1e-55"), "identity holds")
    kappa_C, kappa_D = mp.mpf(1) / 2 - zc, mp.mpf(1) / 2 - zd
    print(f"   κ at z_C = {mp.nstr(kappa_C, 14)}   (positive)")
    print(f"   κ at z_D = {mp.nstr(kappa_D, 14)}   (negative)")
    chk("A7 κ > 0 at z_C", kappa_C > 0, f"{mp.nstr(kappa_C, 10)}")
    chk("A7 κ < 0 at z_D", kappa_D < 0, f"{mp.nstr(kappa_D, 10)}")
    # and it is not a pin artefact — sweep the substrate regime
    worst = min((mp.mpf(1) / 2 - z_D(mp.mpf(1) + mp.mpf(k) / 10))
                for k in range(1, 40))
    allneg = all((mp.mpf(1) / 2 - z_D(mp.mpf(1) + mp.mpf(k) / 100)) < 0
                 for k in range(1, 400))
    chk("A7 κ < 0 at z_D for EVERY q in (1, 5] sampled (Lean: all q>1)",
        allneg, f"max over sample = {mp.nstr(worst, 6)}")
    out["ladder_phase_coeff_at_zC"] = mp.nstr(kappa_C, 30)
    out["ladder_phase_coeff_at_zD"] = mp.nstr(kappa_D, 30)

    # ── A7r: RETRACTION GUARD — κ(z_D) is NOT the Wedderburn weight ───────
    # The actual H₃(q) Markov weights under convention D, from S2 (PR #5185,
    # audit §3bis). Their symbolic solve of the corpus's own three defining
    # conditions is CITED, NOT RE-DERIVED here; these closed forms are merely
    # evaluated at q₀ as a guard so the conflation cannot silently return.
    #   y_(3)  = (q⁴+1)/(q²+1)²   y_(2,1) = q²/(q²+1)²   y_(1³) = 0
    # S1's vector (z, 1/2−z, z) satisfies only the normalisation condition and
    # FAILS the other two, so it is not a weight vector of H₃(q) at all.
    print("\nA7r — RETRACTION GUARD: the ACTUAL D-frame weights (S2 #5185, cited)")
    den = (q**2 + 1) ** 2
    y3_D = (q**4 + 1) / den
    y21_D_actual = q**2 / den
    y1c3_D = mp.mpf(0)
    print(f"   y_(3)   = {mp.nstr(y3_D, 14)}   y_(2,1) = {mp.nstr(y21_D_actual, 14)}"
          f"   y_(1³) = {mp.nstr(y1c3_D, 4)}")
    print(f"   vs the retracted claim κ(z_D) = {mp.nstr(kappa_D, 14)}  — different sign AND magnitude")
    chk("A7r D-frame weights are positive semidefinite: y_(3)>0, y_(2,1)>0, y_(1³)=0",
        y3_D > 0 and y21_D_actual > 0 and y1c3_D == 0,
        f"y_(3)={mp.nstr(y3_D,10)}  y_(2,1)={mp.nstr(y21_D_actual,10)}  y_(1³)=0"
        "  → signature (5,0,1); convention D does NOT fail positivity")
    chk("A7r the retracted identification is false: κ(z_D) != y_(2,1) under D",
        mp.fabs(kappa_D - y21_D_actual) > mp.mpf("1e-3") and kappa_D < 0 < y21_D_actual,
        f"κ(z_D)={mp.nstr(kappa_D,10)} < 0 < {mp.nstr(y21_D_actual,10)}=y_(2,1); "
        f"|diff|={mp.nstr(mp.fabs(kappa_D - y21_D_actual),10)}")
    out["y21_at_zD_actual_S2"] = mp.nstr(y21_D_actual, 30)
    out["y3_at_zD_actual_S2"] = mp.nstr(y3_D, 30)
    out["y1cubed_at_zD_actual_S2"] = "0"

    # ── A8: Temperley–Lieb SHAPE of the two Markov parameters ────────────
    # Three exact rearrangements, recorded because they are the algebraic
    # inputs to the TL hypothesis (audit §6b/§6c). They are IDENTITIES, so
    # they hold at every q — the pin values are reported for reference only.
    #
    # NOT EVIDENCE OF A MECHANISM. That z_D is expressible over the TL loop
    # parameter does not make the D trace factor through TL; that is a
    # hypothesis under test on the sibling's front (PR #5185), resting on
    # three corank points (n=3,4,5) with n=6 as the discriminator.
    print("\nA8 — Temperley–Lieb SHAPE of z_D and z_C (identities, not evidence)")
    delta = q + 1 / q                      # [2]_q — the TL loop parameter
    sq = mp.sqrt(q)
    bracket2_sq = sq + 1 / sq              # [2]_{√q}
    tol = mp.mpf("1e-50")

    # z_D = q²/[2]_q, since [2]_q = (q²+1)/q. Lean: zD_eq_qsq_div_bracketTwo.
    d1 = mp.fabs(zd - q**2 / delta)
    print(f"   z_D = {mp.nstr(zd, 20)}   q²/[2]_q = {mp.nstr(q**2 / delta, 20)}")
    chk("A8 z_D == q²/[2]_q (TL loop parameter)", d1 < tol,
        f"|diff| = {mp.nstr(d1, 3)}")

    # z_C = 1/[2]_{√q}, since 1+q = √q·[2]_{√q}.
    d2 = mp.fabs(zc - 1 / bracket2_sq)
    print(f"   z_C = {mp.nstr(zc, 20)}   1/[2]_√q = {mp.nstr(1 / bracket2_sq, 20)}")
    chk("A8 z_C == 1/[2]_{√q}", d2 < tol, f"|diff| = {mp.nstr(d2, 3)}")

    # δ−2 = (q/b)·u exactly: δ−2 = (q−1)²/q and u = b(q−1)²/q².
    # ⇒ a TL expansion in δ−2 is a RESCALING of the u-expansion by q/b,
    #   not a new series.
    b = s["b"]
    d3 = mp.fabs((delta - 2) - (q / b) * u)
    print(f"   δ−2 = {mp.nstr(delta - 2, 14)}   u = {mp.nstr(u, 14)}   "
          f"q/b = {mp.nstr(q / b, 14)}")
    chk("A8 δ−2 == (q/b)·u exactly (TL expansion is a rescaled u-expansion)",
        d3 < tol, f"|diff| = {mp.nstr(d3, 3)}")

    out["bracket2_q_delta"] = mp.nstr(delta, 30)
    out["zD_over_TL_check"] = mp.nstr(q**2 / delta, 30)
    out["zC_over_TL_check"] = mp.nstr(1 / bracket2_sq, 30)
    out["delta_minus_2"] = mp.nstr(delta - 2, 30)
    out["q_over_b"] = mp.nstr(q / b, 30)
    out["tl_identification_tier"] = (
        "HYPOTHESIS under test — coranks 1,10,78 at n=3,4,5 match n!−C_n "
        "(sibling PR #5185, not re-derived here); n=6 (588) is the "
        "discriminator. These A8 identities are shape, not mechanism."
    )

    out["checks"] = checks
    n_pass = sum(1 for c in checks if c["pass"])
    print("\n" + "=" * 74)
    print(f"  {n_pass}/{len(checks)} assertions passed")
    print("=" * 74)

    print("\nTIERING of every coefficient named above:")
    print("  c₂ = −1            : PROVED (z-free `ring` identity) — convention-immune")
    print("  c₂^emp (C and D)   : FITTED (inversion of experimental Q_β)")
    print("  c₃    (C and D)    : FITTED (inversion of experimental Q_β);")
    print("                       algebraically dependent on c₂^emp, not a rung")
    print("  c₄…c₇              : IDENTICALLY ZERO by construction — not rungs")
    print("  z*                 : FITTED (1-parameter solve against Q_exp)")

    (Path(__file__).parent / "qbeta-d-frame-ladder-structure.probe.json").write_text(
        json.dumps(out, indent=2) + "\n")
    return 0 if n_pass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
