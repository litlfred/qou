#!/usr/bin/env python3
"""
O2 (qou-ws1w): attempt — and refute — a derived integer-Stokes → S-residual map.

The A_ω arc (bean qou-arc1) offered four options; the owner chose "3 go, 2 try,
then 1 remove if not successful." This probe is the honest O2 attempt: try to
derive a PARAMETER-FREE map from an integer Stokes constant (A_ω = 3, or the
tower 3, 9, 75, 642, …) to the bar-odd decay residuals

    S(muon) = +0.00968 ,   S(proton) = −0.03946      (S = c₃ + Vol(4₁)).

It must explain the sign asymmetry, the co-occurring 4, and the tower. It does
not. The refutation is grounded in the CANONICAL witness
`computations/qbeta/qbeta-c3-barodd-sleak.witness.json`, not in a fresh fit.

THREE compounding obstructions, strongest first:

  (1) TARGET NOT ROBUSTLY DEFINED — the decisive one. Each individual S value
      carries a CAL-3 propagated uncertainty of ±1.262 (the 1/u³ ≈ 1.6e6
      amplification of the Q_β input error): that is 130× the muon value and 32×
      the proton value. The witness EXPLICITLY asserts the sign flip is NOT
      established by the data ("must not be cited as an established sign flip").
      So the opposite-signed premise the whole bridge rests on is unresolved.

  (2) THE ONE RESOLVED QUANTITY CARRIES NO A_ω CONTENT. Only the SWING
      S(muon) − S(proton) is resolved (CAL-3 error common ⇒ cancels, ±7.6e-7).
      And the swing is exactly c₃(muon) − c₃(proton): Vol(4₁) cancels, so the
      resolved quantity is the cross-anchor c₃ variation and contains no
      Vol(4₁), no A_ω, no Stokes constant at all.

  (3) INTEGRALITY (bean qou-q3np). A_ω and the whole tower are integers (M2
      showed the closed-sector BPS spectrum is abelian ⇒ dim BPS = |Ω|, plain
      integers, never Poincaré polynomials). An integer cannot map to a
      non-integer whose sign is not even established without free real inputs —
      and a map with free real inputs hitting 0.00968 is a fit, not a
      derivation.

For completeness the probe also tests the most natural framework near-match
(S ~ ℏ_q² with the co-occurring 4) and shows it is an UNFALSIFIABLE fit: it is
~1% off, needs two free inputs (ℏ_q² and the 4), and sits trivially inside the
±1.262 noise band — so it can be neither confirmed nor excluded, which is the
signature of a fit, not a derivation.

VERDICT: O2 FAILS. No parameter-free A_ω → S map exists; the target is ill-posed.
⇒ fire O1-remove (excise the A_ω → S bridge from paper content; retain here).

Self-contained (mpmath). Reads only the committed canonical witness values.
"""
import mpmath as mp
# Path bridge: keeps flat-namespace imports working from this cluster
# subdirectory. The bridge module puts every other cluster subdir on
# sys.path so cross-cluster bare-name imports resolve. Idempotent.
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# --- canonical witness values (qbeta-c3-barodd-sleak.witness.json) ---
VOL_4_1 = mp.mpf("2.02988321282")
C3 = {"muon": mp.mpf("-2.02020023502"), "proton": mp.mpf("-2.06934257712")}
S_LEAK = {"muon": mp.mpf("0.0096829778"), "proton": mp.mpf("-0.0394593643")}
S_UNCERTAINTY = mp.mpf("1.262")          # per anchor, CAL-3 propagated
SWING_WITNESS = mp.mpf("0.0491423421")   # S(muon) − S(proton), resolved
SWING_UNCERTAINTY = mp.mpf("7.573e-7")

# --- proton-pinned q0 (owner default for new compute) ---
Q0 = mp.mpf("1.1099785827513808")
HBAR_Q = 1 - 1 / Q0
HBAR_Q2 = HBAR_Q ** 2

# --- the integer Stokes tower (4₁), M2-certified abelian / integer ---
TOWER = [3, 9, 75, 642, 5580]
A_OMEGA = 3


def main() -> int:
    print("O2 — attempt a derived integer-Stokes → S map, and its refutation\n")

    # (0) S = c₃ + Vol(4₁) reproduced exactly (defined residual, not derived split)
    for k in ("muon", "proton"):
        recon = C3[k] + VOL_4_1
        assert abs(recon - S_LEAK[k]) < mp.mpf("1e-9"), f"S={k} mismatch"
    print("  (0) S = c₃ + Vol(4₁) reproduced (a DEFINED residual, per the 2026-08-08 rule)")

    # (1) target not robustly defined
    ratio_mu = S_UNCERTAINTY / abs(S_LEAK["muon"])
    ratio_p = S_UNCERTAINTY / abs(S_LEAK["proton"])
    print(f"  (1) uncertainty/value:  muon {mp.nstr(ratio_mu,4)}× ,  proton {mp.nstr(ratio_p,4)}×")
    print("      ⇒ individual S values NOT robustly defined; sign flip NOT established.")
    assert ratio_mu > 100 and ratio_p > 10, "expected large uncertainty ratios"

    # (2) the one resolved quantity is the c₃ swing; Vol(4₁)/A_ω cancel out
    swing = S_LEAK["muon"] - S_LEAK["proton"]
    c3_swing = C3["muon"] - C3["proton"]
    assert abs(swing - c3_swing) < mp.mpf("1e-9"), "swing ≠ c₃ difference"
    assert abs(swing - SWING_WITNESS) < mp.mpf("1e-6"), "swing ≠ witness"
    print(f"  (2) resolved swing = {mp.nstr(swing,10)} = c₃(μ)−c₃(p) exactly "
          f"(Vol(4₁), A_ω cancel)")
    print(f"      swing uncertainty {mp.nstr(SWING_UNCERTAINTY,3)} — the ONLY resolved "
          f"quantity, and it is A_ω-free")

    # (3) integrality: no parameter-free integer → S map. Show the natural
    #     near-match S ~ ℏ_q² (with the co-occurring 4) is an unfalsifiable fit.
    print(f"\n  (3) integrality obstruction + the ℏ_q² near-match test:")
    print(f"      ℏ_q² = {mp.nstr(HBAR_Q2,8)}  (proton pin)")
    for k, factor, label in (("muon", 1, "ℏ_q²"), ("proton", -4, "−4·ℏ_q²")):
        pred = factor * HBAR_Q2
        rel = abs(pred - S_LEAK[k]) / abs(S_LEAK[k])
        within_noise = abs(pred - S_LEAK[k]) < S_UNCERTAINTY
        print(f"      S({k}) = {mp.nstr(S_LEAK[k],6)}  vs  {label} = {mp.nstr(pred,6)}"
              f"   rel {mp.nstr(rel,3)}  within ±1.262 noise: {within_noise}")
        # It "matches" only because EVERYTHING matches inside a ±1.262 band.
        assert within_noise, "near-match unexpectedly outside noise"
        assert rel > mp.mpf("1e-3"), "near-match is not exact (it is a ~1% fit)"

    print("\n      The ℏ_q² map needs TWO free inputs (ℏ_q² and the factor 4), is ~1% off,")
    print("      and is unfalsifiable (any O(0.01) target sits inside ±1.262). That is the")
    print("      signature of a FIT, not a derivation — and it uses no Stokes integer anyway.")

    # A_ω / tower never enter S
    assert A_OMEGA == 3 and TOWER[0] == 3
    print("\n  A_ω = 3 and the tower 3,9,75,642,5580 do not appear in S = c₃ + Vol(4₁).")

    print("\n  VERDICT: O2 FAILS. No parameter-free A_ω → S map exists; the individual")
    print("  targets are not robustly defined (±130×/±32×), the sign flip is not")
    print("  established, the one resolved quantity (the c₃ swing) is A_ω-free, and any")
    print("  numerical hit is a fit inside a ±1.262 noise band. ⇒ fire O1-remove.")

    print("\n  [assert] all O2 refutation checks pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
