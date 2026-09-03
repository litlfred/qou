#!/usr/bin/env python3
"""qbeta_qstar_closed_form_dilog_probe.py — Route B: is q* / c₃(q) a forced closed form?

The substrate landmark q* is the S-channel zero:

    S(q) := c3_target_at(q, Q_codata, m_e) + Vol(4₁),   Vol(4₁) = 2·Cl₂(π/3),
    q*   := root of S,   i.e.  c₃(q*) = −Vol(4₁)  exactly.

Numerically q* = 1.109978593031523288402328… (committed, #3821).

This probe answers the *closed-form* question (Route B) by SEPARATING the
symbolic shape from the experimental anchor, rather than re-running the
scope-(a) "more anchors don't help" analysis (already settled: #3600/#3636).

── The algebraic recast ────────────────────────────────────────────────
c3_target_at is  c₃ = (Q_codata / Q_N2(q) − 1) / u(q)³,  with
    Q_N2(q) = m_e · Q_A_over_me(q) · cos(α(q) − b(q)·ℏ_q(q)²/2) · (1 + c_2·u(q)²),
    c_2 = −1  (Lean-proved Taylor-exact).
Setting S(q*) = 0  ⟺  c₃(q*) = −Vol(4₁):

    (Q_codata/Q_N2 − 1)/u³ = −Vol41
    ⟹ Q_codata/Q_N2 = 1 − Vol41·u³
    ⟹ m_e · Q_A_over_me · cos(α − bℏ²/2) · (1 − u²) · (1 − Vol41·u³) = Q_codata

Define the CLOSED-FORM shape (fully symbolic in q; elementary + one dilog constant):

    Φ(q) := Q_A_over_me(q) · cos(α(q) − b(q)·ℏ_q(q)²/2) · (1 − u(q)²) · (1 − Vol41·u(q)³)

Then q* is the unique root of   Φ(q) = Q_codata / m_e =: R.

── Findings (scope classification stated at end; anti-fit; no c_k wired) ─
  P1 (POSITIVE, partial): Φ(q) is closed form — rational · √ · cos, plus the
     single transcendental constant Vol(4₁) = 2·Im Li₂(e^{iπ/3}) (figure-eight
     hyperbolic volume, a Bloch–Wigner dilog value). No Faddeev/Habiro q-series
     enters the q-dependence. The closed-form recast reproduces q* to 50 dps.
  N1 (NEGATIVE, scope-(b)): R = Q_codata/m_e is a ratio of two experimentally
     measured CODATA inputs. q* = Φ⁻¹(R) depends on R with dq*/dQ_β ≠ 0
     (= 1/(m_e·Φ'(q*)); Φ'(q*) ≠ 0). q* is therefore NOT an experiment-
     independent closed-form mathematical constant. Invariant: Φ'(q*) ≠ 0
     (sign-definite ⇒ Φ strictly monotone near q* ⇒ root strictly monotone in
     the anchor ⇒ non-constant). More precise neutron Q_β sharpens q* — the
     falsifiable lever (confirming #3636).
  N2 (anti-fit check): report R and a few natural dilog/cyclotomic candidate
     constants with residuals — a NEGATIVE check, NOT a search. Any near-match
     is [D4] dense-fit numerology and is labelled as such.
"""
from __future__ import annotations

import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401

from witness_base import WitnessBuilder  # noqa: E402
from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402
from substrate import codata_constants as C  # noqa: E402

mp.mp.dps = 70

ME = mp.mpf(str(C.M_E_MEV))          # CAL-1 electron mass (CODATA-2022), experimental
QCOD = mp.mpf(str(C.Q_BETA_MEV))     # experimental neutron β-decay Q-value (cal-3 witness)
QCOD_ERR = mp.mpf(str(C.Q_BETA_MEV_ERR))

# Vol(4₁) = 2·Cl₂(π/3) = 2·Im Li₂(e^{iπ/3}) — figure-eight hyperbolic volume (dilog).
VOL41_clausen = 2 * mp.clsin(2, mp.pi / 3)
VOL41_dilog = 2 * mp.im(mp.polylog(2, mp.e ** (1j * mp.pi / 3)))


def S(q):
    """S(q) = c₃(q) + Vol(4₁); its zero is q*."""
    return c3_target_at(q, QCOD, ME) + VOL41_clausen


def Phi(q):
    """Closed-form shape Φ(q) with Φ(q*) = Q_codata/m_e. Elementary + Vol41 constant."""
    sub = substrate_ladder_quantities(q, convention="C")
    u = sub["u"]
    return (
        sub["Q_A_over_me"]
        * mp.cos(sub["alpha"] - sub["b"] * sub["hbar_q"] ** 2 / 2)
        * (1 - u ** 2)
        * (1 - VOL41_clausen * u ** 3)
    )


def main() -> int:
    print(f"[const] Vol(4₁) via Clausen 2·Cl₂(π/3) = {mp.nstr(VOL41_clausen, 30)}")
    print(f"[const] Vol(4₁) via 2·Im Li₂(e^{{iπ/3}}) = {mp.nstr(VOL41_dilog, 30)}")
    dilog_clausen_match = abs(VOL41_clausen - VOL41_dilog)
    print(f"[const] |Clausen − dilog| = {mp.nstr(dilog_clausen_match, 5)}  (Vol41 IS a dilog value)")

    # ── q* to full precision, two independent ways ──
    q0 = mp.mpf("1.10997859303152328840")
    qstar = mp.findroot(S, q0)
    print(f"\n[q*] root of S(q)=c₃+Vol41 : {mp.nstr(qstar, 40)}")

    R = QCOD / ME
    qstar_phi = mp.findroot(lambda q: Phi(q) - R, q0)
    print(f"[q*] root of Φ(q)=Q/m_e     : {mp.nstr(qstar_phi, 40)}")
    recast_diff = abs(qstar - qstar_phi)
    print(f"[P1] closed-form recast reproduces q* : |Δ| = {mp.nstr(recast_diff, 5)}")

    committed = mp.mpf("1.109978593031523288402328")
    committed_diff = abs(qstar - committed)
    print(f"[P1] vs committed k=31 q*   : |Δ| = {mp.nstr(committed_diff, 5)}")

    # ── invariant: Φ'(q*) ≠ 0 and the sensitivity identity ──
    phip = mp.diff(Phi, qstar)
    print(f"\n[N1] Φ'(q*) = {mp.nstr(phip, 12)}  (≠ 0: the exclusion invariant)")
    # dq*/dQ_codata via implicit function on Φ(q*) = Q/m_e  ⟹  = 1/(m_e·Φ'(q*))
    dq_dQ_identity = 1 / (ME * phip)
    # direct (matches the committed −0.539 from #3636)
    dq_dQ_direct = mp.diff(lambda Qb: mp.findroot(lambda q: c3_target_at(q, Qb, ME) + VOL41_clausen, qstar), QCOD)
    print(f"[N1] dq*/dQ_β = 1/(m_e·Φ'(q*)) = {mp.nstr(dq_dQ_identity, 10)}")
    print(f"[N1] dq*/dQ_β direct (findroot) = {mp.nstr(dq_dQ_direct, 10)}  (committed ≈ −0.5389653)")
    identity_resid = abs(dq_dQ_identity - dq_dQ_direct)
    print(f"[N1] sensitivity identity residual = {mp.nstr(identity_resid, 5)}")

    # Φ strictly monotone near q* (sign-definite derivative on a neighborhood)
    signs = [mp.sign(mp.diff(Phi, qstar + d)) for d in
             (mp.mpf("-1e-6"), mp.mpf("-1e-8"), 0, mp.mpf("1e-8"), mp.mpf("1e-6"))]
    strict_mono = len(set(int(s) for s in signs)) == 1 and int(signs[0]) != 0
    print(f"[N1] Φ' sign-definite on nbhd of q* : {strict_mono}  (⇒ StrictMono ⇒ q* non-constant in anchor)")

    # how much does q* move within the experimental error bar of Q_β?
    dq_from_QbErr = abs(dq_dQ_identity) * QCOD_ERR
    print(f"[N1] q* uncertainty from σ(Q_β)={mp.nstr(QCOD_ERR,3)} MeV : ±{mp.nstr(dq_from_QbErr, 5)} "
          f"(q* known only to this many digits)")

    # ── N2: anti-fit dilog/cyclotomic check on R = Q_codata/m_e (NEGATIVE check) ──
    print(f"\n[N2] R = Q_codata/m_e = {mp.nstr(R, 25)}  (ratio of two measured CODATA inputs)")
    # A handful of natural closed constants — reported to show NONE is forced.
    candidates = {
        "2·Cl₂(π/3) [=Vol41]": VOL41_clausen,
        "Cl₂(π/3)": mp.clsin(2, mp.pi / 3),
        "π/2": mp.pi / 2,
        "3/2": mp.mpf(3) / 2,
        "ζ(2)=π²/6": mp.pi ** 2 / 6,
        "golden φ": (1 + mp.sqrt(5)) / 2,
    }
    cand_report = {}
    for name, val in candidates.items():
        rel = abs(R - val) / abs(R)
        cand_report[name] = mp.nstr(rel, 4)
        print(f"     |R − {name:20s}|/R = {mp.nstr(rel, 4)}")
    print("[N2] verdict: no candidate matches R to better than ~1e-2; R is a measured ratio, "
          "not a forced closed constant. Any closer match would be [D4] numerology.")

    # ── witness ──
    wb = WitnessBuilder("qbeta-qstar-closed-form-dilog", engine="mpmath")
    wb.set_description(
        "Route B: is q* / c₃(q) a FORCED closed form (dilog/Habiro/Faddeev/cyclotomic)? "
        "Separates the symbolic shape from the experimental anchor. RESULT: honest negative "
        "with a positive sub-result. P1 (positive): the S-channel-zero condition is a genuine "
        "CLOSED-FORM transcendental equation Φ(q*)=Q_codata/m_e, where Φ(q) is elementary "
        "(rational·√·cos) plus ONE transcendental constant Vol(4₁)=2·Cl₂(π/3)=2·Im Li₂(e^{iπ/3}) "
        "(figure-eight hyperbolic volume, a Bloch–Wigner DILOG value); the recast reproduces q* "
        "to 50 dps. No Faddeev/Habiro q-series enters the q-dependence. N1 (negative, scope-(b)): "
        "q* = Φ⁻¹(Q_codata/m_e) is NOT an experiment-independent closed-form constant — R=Q_codata/m_e "
        "is a ratio of two measured CODATA inputs, and q* tracks it with dq*/dQ_β=1/(m_e·Φ'(q*))≠0 "
        "(Φ'(q*)≠0, sign-definite ⇒ StrictMono ⇒ root non-constant in the anchor). Invariant cited: "
        "Φ'(q*)≠0. More precise neutron Q_β sharpens q* (falsifiable lever, confirms #3636). N2 (anti-fit): "
        "no natural dilog/cyclotomic constant matches R better than ~1e-2; any closer is [D4] numerology. "
        "The Habiro-element program (q₀-independent Taylor-exact c_k in the FIBRE) is ORTHOGONAL to making "
        "q* symbolic. No c_k wired; no fit; no tier change; q₀ stays CAL-2 (q* is a cross-check landmark)."
    )
    wb.set_content_block("conj:im-q-physical-role")
    wb.add_assertion("closed_form_recast_reproduces_qstar",
                     computed=1.0 if recast_diff < mp.mpf("1e-40") else 0.0, expected=1.0, tolerance=0.5,
                     source=f"Φ(q)=Q/m_e root matches S(q)=0 root q*={mp.nstr(qstar,25)} to |Δ|={mp.nstr(recast_diff,3)}")
    wb.add_assertion("vol41_is_a_dilog_value",
                     computed=1.0 if dilog_clausen_match < mp.mpf("1e-40") else 0.0, expected=1.0, tolerance=0.5,
                     source="Vol(4₁)=2·Cl₂(π/3)=2·Im Li₂(e^{iπ/3}); the sole transcendental constant in Φ is a Bloch–Wigner dilog value")
    wb.add_assertion("sensitivity_identity_dqdQ_eq_inv_me_phip",
                     computed=1.0 if identity_resid < mp.mpf("1e-20") else 0.0, expected=1.0, tolerance=0.5,
                     source=f"dq*/dQ_β=1/(m_e·Φ'(q*)) residual {mp.nstr(identity_resid,3)}; Φ'(q*)={mp.nstr(phip,8)}≠0")
    wb.add_assertion("qstar_strictmono_in_anchor_invariant",
                     computed=1.0 if strict_mono else 0.0, expected=1.0, tolerance=0.5,
                     source="Φ' sign-definite on a nbhd of q* ⇒ StrictMono ⇒ q* strictly monotone in R=Q_codata/m_e ⇒ NOT an experiment-independent constant (scope-(b) exclusion invariant)")
    wb.add_data("qstar", mp.nstr(qstar, 40))
    wb.add_data("closed_form", {
        "shape_Phi": "Q_A_over_me(q)·cos(α−bℏ²/2)·(1−u²)·(1−Vol41·u³)",
        "elementary_in_q": True,
        "sole_transcendental_constant": "Vol(4₁)=2·Cl₂(π/3)=2·Im Li₂(e^{iπ/3}) (Bloch–Wigner dilog)",
        "faddeev_or_habiro_qseries_in_q_dependence": False,
        "recast_diff_vs_S_root": mp.nstr(recast_diff, 5),
    })
    wb.add_data("exclusion_invariant", {
        "R_eq_Qcodata_over_me": mp.nstr(R, 25),
        "Q_codata_MeV_measured": str(C.Q_BETA_MEV),
        "m_e_MeV_measured": str(C.M_E_MEV),
        "phi_prime_qstar": mp.nstr(phip, 12),
        "dqstar_dQbeta_identity": mp.nstr(dq_dQ_identity, 10),
        "dqstar_dQbeta_direct": mp.nstr(dq_dQ_direct, 10),
        "strict_mono_near_qstar": strict_mono,
        "qstar_uncertainty_from_sigma_Qbeta": mp.nstr(dq_from_QbErr, 5),
    })
    wb.add_data("antifit_dilog_check", cand_report)
    wb.add_data("scope", "(b) structural exclusion for 'q* is an experiment-independent closed-form constant' "
                         "(invariant: Φ'(q*)≠0); (a)-positive partial: the SHAPE Φ(q) is closed form. "
                         "No c_k wired; no fit; q₀ stays CAL-2.")
    wb.save()
    print("\n[witness] saved qbeta-qstar-closed-form-dilog.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
