#!/usr/bin/env python3
"""
qou-6y1p: does retargeting the S-channel at the RESOLVED swing rescue it? NO.

After O2 refuted the individual S values (±1.26, sign flip not established), the
one resolved quantity was the swing S(muon) − S(proton) = c₃(muon) − c₃(proton).
I flagged "retarget at the swing" as a foreseeable direction. Corpus-grep (the
discipline) corrects that guess: the swing has NO first-principles derivation.

Two settled corpus facts:
  * c₃ has NO first-principles value — the fixed theory ladder through N=2 gives
    Q_theory/Q_base − 1 = c₂·u² exactly, so its [u³] coefficient is IDENTICALLY 0;
    the ~−2 number is only the circular cal-anchored extraction Q_codata/Q_base(q).
    (docs/audits/2026-07-06-c3-not-exact-cross-anchor-verdict.md; registry §3 tier
    = empirical / cal-anchored / circular / not-anchor-stable.)
  * the swing is the 1/u³ ladder artifact, dc₃/dq ≈ 3.84e6
    (computations/qbeta/qbeta-c3-swing-selfdual-pole-vs-ladder.witness.json).

This probe confirms the ONE arithmetic link those two imply: the swing is exactly
the μ-p substrate tension amplified by dc₃/dq. So deriving the swing reduces to
(a) a first-principles c₃ — whose theory coefficient is identically 0 — AND (b)
the μ-p substrate tension, an open ~9.5σ residual. Same wall, not a new front.

VERDICT: qou-6y1p is NOT foreseeably tractable. The swing reframe does not rescue
the S-channel; per "excise if no progress foreseeable," it joins the A_ω→S bridge
at the wall. (The S = c₃ + Vol(4₁) DEFINITION still stands — it is a definition.)

Self-contained (mpmath). Reads committed corpus anchor values only. No fit.
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

# Anchors and c₃ values — 2026-07-06 cross-anchor verdict (post-bug-fix compute).
Q_PROTON = mp.mpf("1.10997858275138")
Q_MUON = mp.mpf("1.10997859555733")
C3_PROTON = mp.mpf("-2.06934257711516784")
C3_MUON = mp.mpf("-2.02018812814143946")

# The swing witness records dc₃/dq ≈ 3.84e6 (the 1/u³ ladder slope at q*).
DC3_DQ_WITNESS = mp.mpf("3.84e6")


def main() -> int:
    swing = C3_MUON - C3_PROTON
    dq = Q_PROTON - Q_MUON
    implied_slope = swing / dq
    mu_p_tension_ppb = abs(dq) / Q_PROTON * mp.mpf("1e9")

    print("qou-6y1p — is the swing reframe tractable? Corpus-grounded verdict: NO\n")
    print(f"  swing = c₃(μ) − c₃(p)        = {mp.nstr(swing, 8)}")
    print(f"  Δq (proton − muon)           = {mp.nstr(dq, 6)}")
    print(f"  μ-p substrate tension        = {mp.nstr(mu_p_tension_ppb, 4)} ppb")
    print(f"  implied dc₃/dq = swing/Δq    = {mp.nstr(implied_slope, 6)}"
          f"   (swing witness: 3.84e6)")
    print()
    print("  ⇒ swing = (μ-p tension) × dc₃/dq exactly. It is the known 11.5 ppb")
    print("    μ-p substrate tension amplified by the circular 1/u³ extraction —")
    print("    NOT an independent quantity. Deriving it needs BOTH a first-")
    print("    principles c₃ (theory [u³] coeff ≡ 0) AND the μ-p tension (open ~9.5σ).")
    print("\n  VERDICT: qou-6y1p NOT foreseeably tractable — same wall. The S=c₃+Vol(4₁)")
    print("  DEFINITION stands (it is a definition); the reframe does not rescue a")
    print("  derivation.")

    # Assertions: the swing IS the amplified μ-p tension, matching the witness slope.
    # Compare magnitudes: the witness records |S'(q*)| ≈ 3.84e6; sign depends on
    # the Δq direction convention (c₃ decreases as q increases).
    assert abs(abs(implied_slope) - DC3_DQ_WITNESS) / DC3_DQ_WITNESS < mp.mpf("0.02"), \
        "implied |slope| disagrees with the swing witness |dc₃/dq|"
    assert 11 < mu_p_tension_ppb < 12, "μ-p tension not the known ~11.5 ppb"
    assert abs(swing - mp.mpf("0.049154449")) < mp.mpf("1e-6"), "swing value drift"
    print("\n  [assert] swing = μ-p tension × dc₃/dq (matches witness); μ-p = 11.5 ppb — PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
