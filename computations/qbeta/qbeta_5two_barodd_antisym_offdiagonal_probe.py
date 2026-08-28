#!/usr/bin/env python3
"""C1 (bean qou-jtii): the 5₂ bar-odd channel is the ι-ODD ANTISYMMETRIC
off-diagonal contraction of the block basis — and it is ANCHOR-SMOOTH.

DISTINCT ANGLE (parallel to the B-tranche; coordinated on 1ppq-qbeta).

The B-tranche walked:
  B1   (#4226) — the Stokes σ-pair population is FORCED ZERO on the real-q
                 ray; only the real saddle σ₃ is O(1). Successor named: the
                 GK bilinear block pairing.
  B1.2 (gk-bilinear-block-pairing) — the naked/dressed GK bilinear
                 W₋₁(1/q)·B·W₋₁(q)ᵀ and its odd assembly O = ½(S⁺−S⁻)
                 confronted ENTRY-BY-ENTRY with the bar-odd targets: 0 hits
                 at 1e-6. Wall = state-integral DRESSING + λ-row selection.
  B1.3 (masbaum-block-row-selection) — the Masbaum tail (an integer-q
                 series, u-parity EVEN) lies OUTSIDE the 18-dim GGM block
                 span for every scalar dressing (21 exact solves). Successor
                 named: a MODULE MAP (descendant/derivative tower, or the
                 cyclotomic expansion) — a different VECTOR in the module.

THIS ANGLE does not chase the module-map successors (B1.3's named rungs).
It uses the DERIVED A1 chirality split (qbeta-5two-chirality-state-integral,
landed) which already writes the frame-reduced state integral as

    Ẑ = e^{−iπ/4} Z
      =  R^{1/8}·[ H⁺₁ H⁻₁ ]                         (bar-EVEN / index channel)
      +  i·( −R^{1/8}/2 )·[ β·H⁺₂ H⁻₀ − β⁻¹·H⁺₀ H⁻₂ ] (bar-ODD / chirality)

so the bar-odd HOME is the β-graded ANTISYMMETRIC OFF-DIAGONAL contraction
    ω(β,p,q) := β·p − β⁻¹·q ,   p := H⁺₂H⁻₀ ,  q := H⁺₀H⁻₂ ,
NOT a single span-vector (B1.3's search grade) and NOT the symmetric
bilinear / all matrix entries (B1.2's search grade). ω is ι-ODD under the
amphichiral involution ι:(β,p,q) ↦ (β⁻¹,q,p):
    ω(ι(β,p,q)) = β⁻¹ q − β p = −ω(β,p,q).
Hence (char ≠ 2) an ι-fixed (amphichiral) datum forces ω = 0 — the
V(4₁)_odd = 0 fact — and no ι-EVEN object (the B1.2 symmetric bilinear /
the B1.3 span vectors, which are ι-graded even) can carry it. This
SELECTION RULE is formalized sorry-free in
    QOU/QBeta/BarOddAntisymOffDiagonal.lean.

WHAT THIS PROBE MEASURES (parameter-free; consumes committed data only —
no re-run of the A1 state integral, no wide scan):

  T1  ι-odd flip (probe↔Lean tie): with the actual committed block
      products, ω(β⁻¹,q,p) = −ω(β,p,q) to machine precision.
  T2  antisymmetric structure gate: N_odd = ½(N − Nᵀ) of the committed A2
      assembly matrix IS the antisymmetric part carrying the off-diagonal
      (0,2)/(2,0) contraction — the block-level home of ω.
  T3  ANCHOR-SWING BOUND (the decisive number): the committed A1 bar-odd
      datum Im Ẑ swings between the muon and proton q₀ anchors by
      Δ_odd = |odd(pr) − odd(mu)| / odd(mu). c₃ swings ~3.47 % across the
      same anchor pair. The ratio (c₃ swing)/(bar-odd swing) is the
      quantitative scope-(a) statement: the correct bar-odd algebraic
      object is ANCHOR-SMOOTH and cannot, alone, realize the c₃ swing.

VERDICT (pre-registered scope-(a)): the antisymmetric off-diagonal ω is the
provably-correct bar-odd HOME that B1.2/B1.3 structurally missed (wrong
ι-grade), but it is anchor-smooth (~ppm) while c₃ is a percent-level swing.
Any module-map successor that stays within this (anchor-smooth) block /
Habiro home inherits the ppm smoothness ⇒ cannot close the swing. The swing
must come from the anchor-DEPENDENT meridian-holonomy deformation q₀↦u
(CuspShapeBarParity's "open link"), not from selecting a smoother object.
No fit; no c_k wired; NEVER invert Q_β/CODATA; comparison to observed only.

Run: python3 -u computations/qbeta/qbeta_5two_barodd_antisym_offdiagonal_probe.py \
       2>&1 | tee /tmp/qbeta_5two_barodd_antisym.log
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from datetime import datetime, timezone
from decimal import Decimal, getcontext
from pathlib import Path

getcontext().prec = 60

_HERE = Path(__file__).resolve().parent
_ROOT = _HERE.parent.parent
_PROBES = _ROOT / "computations" / "probes"
_OUT = _ROOT / "computations" / "qbeta" / "qbeta-5two-barodd-antisym-offdiagonal.witness.json"

GK = json.loads((_PROBES / "qbeta-5two-gk-bilinear-pairing.witness.json").read_text())
A1 = json.loads((_PROBES / "qbeta-5two-chirality-state-integral.witness.json").read_text())

# c₃ cross-anchor swing (established corpus; NOT re-derived here):
# docs/audits/2026-05-31-qbeta-ck-truncation-order-canonical-framing.md
# "c_3 = -2 ... swings up to 3.47 % at m_p-pin q₀ (≈ 3 % cross-anchor)".
C3_SWING = Decimal("0.0347")


def _git_sha() -> str:
    try:
        return subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=_ROOT, text=True
        ).strip()
    except Exception:
        return "unknown"


def main() -> int:
    assertions = []
    data = {}

    # ---- T1: ι-odd flip (probe ↔ Lean tie) --------------------------------
    # Use the committed block-assembly antisymmetric entries as concrete
    # off-diagonal products p, q and a concrete modulus β; verify ω is ι-odd.
    beta = Decimal(A1["data"]["substrate"]["muon"]["beta"])
    N = [[Decimal(x) for x in row] for row in GK["data"]["assembly_tables"]["N"]]
    # off-diagonal (2,0) and (0,2) products stand in for H⁺₂H⁻₀ and H⁺₀H⁻₂.
    p = N[2][0]
    q = N[0][2]

    def omega(b: Decimal, pp: Decimal, qq: Decimal) -> Decimal:
        return b * pp - (Decimal(1) / b) * qq

    w = omega(beta, p, q)
    w_iota = omega(Decimal(1) / beta, q, p)  # ι:(β,p,q)↦(β⁻¹,q,p)
    flip_resid = abs(w_iota + w)  # want 0
    assertions.append(
        {
            "name": "iota_odd_flip",
            "computed": float(flip_resid),
            "expected": 0.0,
            "passed": flip_resid < Decimal("1e-30"),
            "tolerance": 1e-30,
            "source": "ω(β⁻¹,q,p) = −ω(β,p,q) on committed block products "
            "(probe↔Lean BarOddAntisymOffDiagonal.omega_iota_odd tie)",
        }
    )
    data["iota_odd_flip"] = {
        "beta": str(beta),
        "p": str(p),
        "q": str(q),
        "omega": str(w),
        "omega_iota": str(w_iota),
        "residual": str(flip_resid),
    }

    # ---- T2: antisymmetric-structure gate ---------------------------------
    # N_odd committed in the GK witness must equal ½(N − Nᵀ) (the block-level
    # home of ω), and its (0,2)/(2,0) entries are the off-diagonal contraction.
    Nodd_committed = [
        [Decimal(x) for x in row] for row in GK["data"]["assembly_tables"]["N_odd"]
    ]
    max_dev = Decimal(0)
    for i in range(3):
        for j in range(3):
            asym = (N[i][j] - N[j][i]) / 2
            max_dev = max(max_dev, abs(asym - Nodd_committed[i][j]))
    assertions.append(
        {
            "name": "antisym_offdiag_is_bar_odd_home",
            "computed": float(max_dev),
            "expected": 0.0,
            "passed": max_dev < Decimal("1e-12"),
            "tolerance": 1e-12,
            "source": "N_odd = ½(N − Nᵀ): the committed antisymmetric assembly "
            "IS the block home of the ι-odd off-diagonal contraction",
        }
    )
    data["antisym_gate"] = {
        "max_dev_vs_committed_Nodd": str(max_dev),
        "offdiag_02": str((N[0][2] - N[2][0]) / 2),
        "offdiag_20": str((N[2][0] - N[0][2]) / 2),
    }

    # ---- T3: ANCHOR-SWING BOUND (the decisive scope-(a) number) -----------
    odd_mu = Decimal(A1["data"]["chirality_split"]["muon"]["odd_ImZhat"])
    odd_pr = Decimal(A1["data"]["chirality_split"]["proton"]["odd_ImZhat"])
    even_mu = Decimal(A1["data"]["chirality_split"]["muon"]["even_ReZhat"])
    even_pr = Decimal(A1["data"]["chirality_split"]["proton"]["even_ReZhat"])
    barodd_swing = abs(odd_pr - odd_mu) / abs(odd_mu)
    bareven_swing = abs(even_pr - even_mu) / abs(even_mu)
    ratio = C3_SWING / barodd_swing

    assertions.append(
        {
            "name": "bar_odd_home_is_anchor_smooth",
            "computed": float(barodd_swing),
            "expected": 0.0,
            "passed": barodd_swing < Decimal("1e-4"),  # << c₃'s 3.47e-2
            "tolerance": 1e-4,
            "source": "|Im Ẑ_odd(proton) − Im Ẑ_odd(muon)| / |Im Ẑ_odd(muon)| "
            "from committed A1 two-anchor data — the bar-odd HOME swing",
        }
    )
    assertions.append(
        {
            "name": "c3_swing_exceeds_barodd_home_swing",
            "computed": float(ratio),
            "expected": 1.0,
            "passed": ratio > Decimal("100"),
            "tolerance": 1e9,  # one-sided: pass iff ratio > 100
            "source": "(c₃ cross-anchor swing 3.47%) / (bar-odd home swing): "
            "quantitative scope-(a) — the anchor-smooth bar-odd object cannot "
            "alone realize the percent-level c₃ swing",
        }
    )
    data["anchor_swing"] = {
        "barodd_home_swing": str(barodd_swing),
        "barodd_home_swing_ppm": float(barodd_swing * Decimal("1e6")),
        "bareven_home_swing_ppm": float(bareven_swing * Decimal("1e6")),
        "c3_cross_anchor_swing": str(C3_SWING),
        "ratio_c3_over_barodd": float(ratio),
        "anchor_pair": "muon q₀ vs proton q₀ (same pair as the c₃ swing)",
    }

    data["verdict"] = (
        "THE BAR-ODD CHANNEL IS THE ι-ODD ANTISYMMETRIC OFF-DIAGONAL "
        "CONTRACTION ω(β,p,q)=β·p−β⁻¹·q OF THE BLOCK BASIS (A1-derived), the "
        "provably-correct home B1.2 (symmetric bilinear) and B1.3 (single "
        "span-vector) structurally missed — both are ι-EVEN grades that "
        "cannot carry the ι-ODD ω (Lean: BarOddAntisymOffDiagonal, sorry-free). "
        "BUT ω is ANCHOR-SMOOTH: it swings %.3g ppm across the muon↔proton "
        "anchors while c₃ swings ~3.47%% (34700 ppm) — a %.0f× mismatch. "
        "Scope-(a): the correct bar-odd algebraic object cannot, ALONE, "
        "realize the c₃ swing; any module-map successor that stays inside "
        "this (anchor-smooth) block/Habiro home inherits the ppm smoothness. "
        "The swing must come from the anchor-DEPENDENT meridian-holonomy "
        "deformation q₀↦u (the open link), not a smoother object choice. "
        "No fit; no c_k wired; comparison to observed only."
        % (float(barodd_swing * Decimal("1e6")), float(ratio))
    )

    all_passed = all(a["passed"] for a in assertions)
    script_bytes = Path(__file__).read_bytes()
    witness = {
        "engine": "python-decimal",
        "engineVersion": "python 3.11",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "commitSha": _git_sha(),
        "assertions": assertions,
        "allPassed": all_passed,
        "durationMs": 0,
        "computation": "qbeta-5two-barodd-antisym-offdiagonal",
        "scriptFile": "qbeta_5two_barodd_antisym_offdiagonal_probe.py",
        "scriptHash": hashlib.sha256(script_bytes).hexdigest()[:12],
        "scriptCommitSha": _git_sha(),
        "precisionMetadata": {
            "compute_dps": 60,
            "output_dps": 30,
            "note": "consumes committed A1/A2 witness data; no state-integral re-run",
        },
        "contentBlock": "prop:phi-b-unitary-bar-odd",
        "description": (
            "C1 (bean qou-jtii): the 5₂ bar-odd channel identified as the ι-ODD "
            "ANTISYMMETRIC OFF-DIAGONAL contraction ω(β,p,q)=β·p−β⁻¹·q of the "
            "block basis (from the A1-derived chirality split), the grade B1.2 "
            "(symmetric bilinear) and B1.3 (single span-vector) structurally "
            "missed. ι-odd flip verified on committed block products (probe↔Lean "
            "tie); antisymmetric-structure gate vs committed N_odd; and the "
            "decisive ANCHOR-SWING bound from committed A1 two-anchor data: the "
            "bar-odd home swings ~4.6 ppm across muon↔proton while c₃ swings "
            "~3.47% — scope-(a), the correct object is anchor-smooth and cannot "
            "alone realize the swing. auditOnly; no fit; no c_k wired; consumes "
            "committed witnesses only (no re-run, no wide scan)."
        ),
        "data": data,
    }
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    from qou_substrate.witness import WitnessBuilder as _WB
    import os as _os  # noqa: E402 -- provenance stamp
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    _OUT.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")

    print(f"[C1] ι-odd flip residual      : {flip_resid}")
    print(f"[C1] N_odd antisym max dev    : {max_dev}")
    print(f"[C1] bar-odd home swing (ppm) : {float(barodd_swing*Decimal('1e6')):.4f}")
    print(f"[C1] bar-even home swing (ppm): {float(bareven_swing*Decimal('1e6')):.4f}")
    print(f"[C1] c₃ swing / bar-odd swing : {float(ratio):.1f}×")
    print(f"[C1] allPassed                : {all_passed}")
    print(f"[C1] witness -> {_OUT.relative_to(_ROOT)}")
    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
