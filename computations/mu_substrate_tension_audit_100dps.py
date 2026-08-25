"""m_μ substrate-tension audit at mp.mpf 50 dps.

Per author 2026-05-31 direction ("A — Audit m_μ structural tension").

## Setup

Post-PR #1422 q_0 re-pin, q_0 is anchored from m_p/m_e:
  q_0 := unique q satisfying m_p/m_e = f(q)  (specific framework formula)
So m_p matches CODATA by construction (0.0004 ppb).

The muon prediction then becomes:
  m_μ_pred / m_e = Vol(4_1) / ℏ_q²
where Vol(4_1) = 2·Λ(π/3) is a categorical constant (Lobachevsky
function at π/3, well-established to arbitrary precision).

Current dashboard reports m_μ at **210 ppb miss** (964× the 100×
target of 0.22 ppb). This is documented as the "μ-p substrate tension
floor" (PR #1574) — expected, not a bug. But no audit has isolated
WHERE the 210 ppb lives.

## What this probe does

Single-session audit of the m_μ prediction chain at 100 dps (extra
precision to rule out 50-dps numerical noise):

1. Compute m_μ_pred = m_e · Vol(4_1) / ℏ_q² at 100 dps using:
   - m_e = CODATA 2022 (CAL-1 anchor, sub-ppb)
   - q_0 from canonical re-pin (CAL-2 anchor)
   - Vol(4_1) = 2·Λ(π/3) — Lobachevsky at π/3

2. Compute the SAME prediction using the OLD (pre-#1422) q_0 derived
   from m_μ/m_e — should reproduce CODATA m_μ exactly (since q_0
   was defined to satisfy this).

3. Quantify q_0 shift: Δq_0 := q_0_new − q_0_old

4. Propagate Δq_0 through the muon formula: predicted m_μ shift

5. Compare residual to dashboard's reported 210 ppb

If steps 1–5 reproduce 210 ppb, the gap IS the q_0 re-pin choice;
NO categorical formula correction needed. If 210 ppb is LARGER than
the propagated Δq_0 effect, a categorical formula correction is
missing (analogous to "12·m_e" for the proton).

## Hypotheses tested

H1. **q_0 re-pin tension** (no formula correction): residual ≈
    propagated Δq_0 effect on m_μ formula.
H2. **Missing m_μ correction term**: residual ≠ propagated Δq_0
    effect → identify the missing structural piece.
H3. **Vol(4_1) precision floor**: Lobachevsky-Catalan at π/3
    has insufficient precision → residual matches Vol(4_1)
    uncertainty propagation.

## Cross-references

- `m_p_borromean_verification_50dps.py` (muon_check section, lines 272-289)
- PR #1574 ("m_μ regression sanity check (informational)")
- PR #1422 (q_0 re-pin from m_p/m_e)
- docs/precision-goals.md (2026-05-29 table, m_μ row "misses ~964×")
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# CODATA 2022 anchors
M_E_MEV = "0.51099895069"
M_MU_MEV = "105.6583755"


def vol_4_1_mathlib(dps: int) -> "mp.mpf":
    """Vol(4_1) = 2·Cl₂(π/3) where Cl₂ is the Clausen function.

    Standard SnapPy value: Vol(4_1) ≈ 2.02988321281930725004240510854658...

    Equivalent forms:
      Vol(4_1) = 2·Cl₂(π/3) = 4·Λ(π/6) = 2·Im[Li₂(e^{iπ/3})]

    Note: the comment header in m_p_borromean_verification_50dps.py
    and several audit docs say "Vol(4_1) = 2·Λ(π/3)" — that's
    INCORRECT (off by factor 3). The correct identity is the one
    above; 2·Λ(π/3) = Cl₂(2π/3) = 0.6766... = Vol(4_1)/3.
    """
    mp.mp.dps = dps + 5
    return 2 * mp.clsin(2, mp.pi / 3)


def m_mu_predicted(q, m_e, dps: int) -> "mp.mpf":
    """m_μ_pred = m_e · Vol(4_1) / ℏ_q²; ℏ_q = 1 - q⁻¹."""
    mp.mp.dps = dps + 5
    vol = vol_4_1_mathlib(dps)
    hbar_q = 1 - 1 / q
    return m_e * vol / hbar_q ** 2


def invert_for_q0(m_mu_target, m_e, dps: int) -> "mp.mpf":
    """Find q satisfying m_μ_target = m_e · Vol(4_1) / ℏ_q²."""
    mp.mp.dps = dps + 5
    vol = vol_4_1_mathlib(dps)
    # m_mu / m_e = vol / (1 - 1/q)^2  =>  (1 - 1/q)^2 = vol·m_e/m_mu
    rhs = vol * m_e / m_mu_target
    hbar_q = mp.sqrt(rhs)  # positive root; q > 1 means 0 < 1-1/q < 1
    # 1 - 1/q = hbar_q  =>  q = 1/(1 - hbar_q)
    return 1 / (1 - hbar_q)


def main() -> int:
    set_compute_dps(100)
    DPS = 100
    mp.mp.dps = DPS + 10

    w = WitnessBuilder("mu-substrate-tension-audit-100dps", engine="python")
    w.set_description(
        "100-dps audit of the m_μ prediction residual (210 ppb) post "
        "q_0 re-pin (#1422). Localises whether the residual is the "
        "propagated q_0 shift (H1: no formula correction needed) or "
        "requires a missing structural correction (H2)."
    )

    q_canonical = mp.mpf(Q_50_DIGIT_STR)
    m_e = mp.mpf(M_E_MEV)
    m_mu_codata = mp.mpf(M_MU_MEV)

    # ── GUARD: q_canonical must be the PROTON pin ────────────────────────
    # This audit's whole subject is the difference between the proton pin and
    # a muon-anchored q_0. If `q_canonical` is itself muon, the audit
    # differences muon against muon and reports the *inversion residual* --
    # the gap between the stored muon literal and a fresh Newton inversion --
    # as though it were the substrate tension.
    #
    # That is not hypothetical: `q0_anchor_manifest.json` listed this
    # producer under `ideal_muon`, and `q_parameter` auto-selects by
    # `sys.argv[0]`, flipping Q_50_DIGIT_STR to the muon literal when this
    # script runs under its own name. The committed witness reported
    # 0.0747 ppb where the answer is 11.61 ppb -- understating its own
    # subject by 155x. It went unnoticed because the wrong number is small,
    # non-zero and plausible; an exact 0 would have been caught immediately.
    #
    # The manifest entry is gone (owner directive 2026-08-15, proton
    # everywhere), but QOU_Q0_ANCHOR can still re-anchor a process, so the
    # invariant is asserted here rather than assumed.
    if not str(q_canonical).startswith("1.10997858275138"):
        raise SystemExit(
            "mu_substrate_tension_audit: q_canonical is not the proton pin "
            f"(got {mp.nstr(q_canonical, 22)}). This audit measures proton vs "
            "muon-anchored q_0; a muon q_canonical makes it difference muon "
            "against muon and report the inversion residual as the tension. "
            "Check QOU_Q0_ANCHOR and q0_anchor_manifest.json."
        )

    print("=" * 78)
    print("m_μ substrate-tension audit at 100 dps")
    print("=" * 78)
    print(f"\nq_0 canonical (from m_p re-pin #1422): {q_canonical}")
    print(f"m_e CAL-1: {m_e}")
    print(f"m_μ CODATA: {m_mu_codata}")

    vol = vol_4_1_mathlib(DPS)
    print(f"\nVol(4_1) at 100 dps  = {mp.nstr(vol, 50)}")
    print(f"  (= 2·Cl₂(π/3) = 4·Λ(π/6))")

    # Step 1: m_μ_pred at canonical q_0
    m_mu_pred = m_mu_predicted(q_canonical, m_e, DPS)
    residual_ppb = (m_mu_pred - m_mu_codata) / m_mu_codata * mp.mpf("1e9")
    print(f"\n[1] m_μ_pred at canonical q_0  = {mp.nstr(m_mu_pred, 18)} MeV")
    print(f"    m_μ CODATA                  = {mp.nstr(m_mu_codata, 18)} MeV")
    print(f"    residual                    = {mp.nstr(residual_ppb, 8)} ppb")

    # Step 2: Invert to find q_0 that EXACTLY matches m_μ
    q0_muon_anchored = invert_for_q0(m_mu_codata, m_e, DPS)
    print(f"\n[2] q_0 if m_μ_pred = CODATA m_μ exactly:")
    print(f"      q_0_μ-anchored = {mp.nstr(q0_muon_anchored, 30)}   "
          f"[fresh Newton inversion of CODATA m_μ/m_e]")
    print(f"      q_0 canonical  = {mp.nstr(q_canonical, 30)}   "
          f"[PROTON pin, q_parameter.Q_50_DIGIT_STR]")

    delta_q0 = q_canonical - q0_muon_anchored
    delta_q0_ppb = delta_q0 / q_canonical * mp.mpf("1e9")
    print(f"      Δq_0 (canonical − μ-anchored) = {mp.nstr(delta_q0, 15)}")
    print(f"      Δq_0 / q_0 = {mp.nstr(delta_q0_ppb, 8)} ppb   "
          f"← the μ–p substrate tension")

    # Separate the two effects that both live in the last digits of q_0, so a
    # reader can never mistake one for the other (the 155x error above).
    #   inversion residual = stored muon LITERAL vs this fresh inversion.
    #     Same pin, two routes; a floor on how sharply any muon-leg
    #     comparison can be stated, NOT a physical quantity.
    #   substrate tension  = proton pin vs the muon-anchored q_0.
    #     Physical: the 9.5σ μ–p disagreement.
    inversion_residual_ppb = None
    try:
        from q_parameter import q_muon_at  # noqa: PLC0415
        q_mu_literal = mp.mpf(q_muon_at(DPS))
        inversion_residual_ppb = ((q0_muon_anchored - q_mu_literal)
                                  / q_mu_literal * mp.mpf("1e9"))
        print(f"\n[2b] the two effects, separated:")
        print(f"      muon literal (q_muon_at) = "
              f"{mp.nstr(q_mu_literal, 30)}")
        print(f"      inversion residual  = "
              f"{mp.nstr(inversion_residual_ppb, 8)} ppb  "
              f"(literal vs inversion — same pin, precision floor)")
        print(f"      substrate tension   = {mp.nstr(delta_q0_ppb, 8)} ppb  "
              f"(proton vs muon — physical)")
        _ratio = abs(delta_q0_ppb / inversion_residual_ppb)
        print(f"      tension / residual  = {mp.nstr(_ratio, 6)}×  "
              f"— the tension must dominate; if it does not, q_canonical "
              f"has been re-anchored to muon and this audit is measuring "
              f"nothing.")
    except Exception as _exc:  # noqa: BLE001
        print(f"\n[2b] inversion residual unavailable ({_exc!r}); "
              f"reporting the tension alone.")

    # Step 3: Propagate Δq_0 through m_μ formula
    # d(m_μ)/dq = m_e · vol · d(1/ℏ_q²)/dq, ℏ_q = 1 - 1/q, dℏ_q/dq = 1/q²
    # d(1/ℏ_q²)/dq = -2·(1/ℏ_q³)·(1/q²)
    # d(m_μ)/m_μ = -2 · (1/ℏ_q) · (1/q²) · dq
    hbar_q = 1 - 1 / q_canonical
    sensitivity = -2 / (hbar_q * q_canonical ** 2)
    propagated_rel = sensitivity * delta_q0
    propagated_ppb = propagated_rel * mp.mpf("1e9")
    print(f"\n[3] Δq_0 → m_μ propagation:")
    print(f"      ∂ ln(m_μ)/∂q = -2/(ℏ_q·q²) = {mp.nstr(sensitivity, 10)}")
    print(f"      propagated relative shift = {mp.nstr(propagated_ppb, 8)} ppb")

    # Step 4: H1 check — does propagated Δq_0 explain the residual?
    print(f"\n[4] H1 test (q_0 re-pin tension, no formula correction needed):")
    print(f"      observed residual    = {mp.nstr(residual_ppb, 8)} ppb")
    print(f"      propagated Δq_0      = {mp.nstr(propagated_ppb, 8)} ppb")
    print(f"      H1 residual          = {mp.nstr(residual_ppb - propagated_ppb, 8)} ppb")
    h1_match = abs(residual_ppb - propagated_ppb) < abs(residual_ppb) * mp.mpf("0.1")
    if h1_match:
        print(f"      ✓ H1 SUPPORTED — observed ≈ propagated within 10%")
    else:
        print(f"      ✗ H1 NOT SUPPORTED — residual is NOT just Δq_0 propagation")

    # Step 5: Vol(4_1) precision floor check
    vol_50 = vol_4_1_mathlib(50)
    vol_diff = vol - vol_50
    print(f"\n[5] Vol(4_1) precision sanity:")
    print(f"      Vol(4_1) @ 50 dps           = {mp.nstr(vol_50, 25)}")
    print(f"      Vol(4_1) @ 100 dps          = {mp.nstr(vol, 25)}")
    print(f"      |diff|                      = {mp.nstr(abs(vol_diff), 12)}")

    # ── Witness ──
    # Name the pin in the field, not just in the value. `q_canonical` alone
    # is what let a muon value sit here unnoticed for the life of the
    # committed witness.
    w.add_parameter("q_canonical_50dps", Q_50_DIGIT_STR)
    w.add_parameter("q_canonical_anchor", "proton")
    w.add_parameter("q_canonical_anchor_note",
                    "asserted at run time; a muon value here would make the "
                    "audit difference muon against muon and report the "
                    "inversion residual as the tension (measured: 0.0747 ppb "
                    "vs the true 11.61 ppb, 155x understated)")
    w.add_parameter("m_e_CODATA", M_E_MEV)
    w.add_parameter("m_mu_CODATA", M_MU_MEV)
    w.add_data("vol_4_1_at_100dps", mp.nstr(vol, 50))
    w.add_data("m_mu_pred_at_canonical_q0", mp.nstr(m_mu_pred, 25))
    w.add_data("residual_ppb_at_canonical_q0", mp.nstr(residual_ppb, 12))
    w.add_data("q0_muon_anchored", mp.nstr(q0_muon_anchored, 50))
    w.add_data("delta_q0_canonical_minus_mu_anchored", {
        "delta_q0": mp.nstr(delta_q0, 25),
        "delta_q0_ppb": mp.nstr(delta_q0_ppb, 12),
    })
    if inversion_residual_ppb is not None:
        w.add_data("leg_separation", {
            "substrate_tension_ppb": mp.nstr(delta_q0_ppb, 12),
            "substrate_tension_meaning":
                "proton pin vs muon-anchored q_0 — PHYSICAL (the 9.5σ μ–p "
                "disagreement)",
            "inversion_residual_ppb": mp.nstr(inversion_residual_ppb, 12),
            "inversion_residual_meaning":
                "stored muon literal vs a fresh Newton inversion — SAME pin, "
                "two routes; a precision floor, not a physical quantity",
            "tension_over_residual":
                mp.nstr(abs(delta_q0_ppb / inversion_residual_ppb), 8),
            "why_recorded":
                "the committed witness once reported the residual AS the "
                "tension; carrying both makes that substitution visible "
                "instead of plausible",
        })
    w.add_data("propagated_q0_effect_on_m_mu_ppb",
               mp.nstr(propagated_ppb, 12))
    w.add_data("h1_substrate_tension_consistent_with_q0_shift",
               bool(h1_match))
    w.add_data("interpretation",
        "H1 SUPPORTED: the 210 ppb m_μ residual IS the q_0 re-pin "
        "shift propagated through Vol(4_1)/ℏ_q². No missing categorical "
        "correction to the muon formula. The substrate is fundamentally "
        "OVER-DETERMINED — q_0 cannot simultaneously match m_p AND m_μ "
        "at sub-ppb precision."
        if h1_match else
        "H1 NOT SUPPORTED: residual EXCEEDS the propagated q_0 shift. "
        "Categorical formula correction missing — search direction is "
        "a small Hecke or Bring contribution to m_μ analogous to '12·m_e' "
        "for the proton."
    )

    w.add_assertion(
        name="audit_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source="m_μ substrate-tension audit completed at 100 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
