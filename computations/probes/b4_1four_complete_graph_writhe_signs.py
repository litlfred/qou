#!/usr/bin/env python3
"""Value leg — the [1⁴] complete-graph exchange matrix from READ-OFF writhe signs.

GAP-A-4 class-D. Scoping:
docs/design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md.

The ⁴He magnitude value is pinned to `b₄ = −ln det(I + G)` with `G` the
SIGN-CARRYING [1⁴] exchange matrix (Perron–Frobenius excluded positive-only
factors; uniform-sign naive exchanges failed —
b4_antisym_hecke_exchange_derivation.py). The [1⁴] closed shell is the
C(4,2)=6-pair COMPLETE GRAPH on the 4 nucleon blocks — NOT the committed
LINEAR-CHAIN word (atom_braid_word_3A gives only 3 adjacent inter-crossings;
§4a of the scoping doc). So `G` is a genuinely new link diagram and its per-pair
writhe signs must be READ OFF the framing, never chosen to hit 9.243.

WHAT IS DERIVED (read off the framework's OWN crossing convention in
mass_at_3A_proper.atom_braid_word_3A — NOT open, NOT fitted):
  • like PROTON pair  pp  →  σ    (positive crossing)  →  writhe sign  +1
  • like NEUTRON pair nn  →  σ⁻¹  (negative crossing)  →  writhe sign  −1
    (n is the bar-partner q↦q⁻¹ of p; its inter-block crossing is the mirror
    σ↦σ⁻¹ — this is where the p↔n bar-odd asymmetry enters, per I-par.)

WHAT IS THE ONE OPEN SIGN:
  • unlike pn pair  →  writhe sign  w_pn ∈ {−1, 0, +1}.
    The committed CHAIN convention AVERAGES the pn crossing → writhe 0, but that
    DECOUPLES the pn pairs (block-diagonal G) — physically impossible for the
    [1⁴] shell, whose binding is pn-dominated (the deuteron binds pn, not
    pp/nn). So the chain's pn=0 cannot be the [1⁴] value; the [1⁴] framing must
    set w_pn = ±1, and reading which requires the explicit [1⁴] link diagram
    (open — see #3407 Reeb `Lk_R^{(k)}`, still a stub).

METHOD (no fit): fix the pp/nn signs from the convention, fix the per-pair
magnitude to the pre-Archimedean bond factor z = 1/(q^{1/2}+q^{-1/2}) (the
canonical Markov-peel factor of one inter-block crossing — a DERIVED constant,
not a knob), and ENUMERATE the three discrete w_pn choices. Report −ln det(I+G)
in MeV for EACH and compare to b₄=9.243 as a verdict. Selecting the w_pn that
best matches would be a fit (Rule-14) and is REFUSED — the deliverable is the
discrete option→verdict map plus the honest statement that fixing w_pn needs the
[1⁴] framing.

`-- Ref:` b4_antisym_hecke_exchange_derivation.py;
b4_exchange_perron_frobenius_constraint.py; mass_at_3A_proper.atom_braid_word_3A.
"""
from __future__ import annotations

import os
import sys
import time
from pathlib import Path

import mpmath as mp

_HERE = Path(__file__).resolve().parent
_COMP = _HERE.parent
_p = str(_COMP)
if _p not in sys.path:
    sys.path.insert(0, _p)
from _li_2_q_util import load_q_50dps  # noqa: E402
from substrate._precision import set_compute_dps  # noqa: E402
from substrate.experimental_constants import M_E_MEV  # noqa: E402
from substrate.witness_base import WitnessBuilder  # noqa: E402

# Canonical compute-precision floor (compute_dps=70) — matches the
# WitnessBuilder precisionMetadata and preserves the 50-digit q from
# load_q_50dps() (Gemini + Copilot #3426 review).
set_compute_dps()

COMP = str(_COMP)

# ⁴He block ordering [p, p, n, n]; indices 0,1 = protons, 2,3 = neutrons.
PROTONS = (0, 1)
NEUTRONS = (2, 3)


def pair_sign(i: int, j: int, w_pn: int) -> int:
    """Read-off writhe sign of the block-pair (i, j) in the [1⁴] closure.

    pp → +1 (σ), nn → −1 (σ⁻¹) : DERIVED from the atom_braid_word_3A
    convention.  pn → w_pn : the one open discrete sign.
    """
    i_p, j_p = i in PROTONS, j in PROTONS
    if i_p and j_p:
        return +1          # pp : positive crossing σ
    if (not i_p) and (not j_p):
        return -1          # nn : negative crossing σ⁻¹
    return w_pn            # pn : open


def exchange_matrix(w_pn: int, z):
    """4×4 symmetric zero-diagonal G_{ij} = sign(i,j)·z for the [1⁴] shell."""
    G = mp.zeros(4, 4)
    for i in range(4):
        for j in range(i + 1, 4):
            g = pair_sign(i, j, w_pn) * z
            G[i, j] = g
            G[j, i] = g
    return G


def neg_log_det_I_plus_G(w_pn: int, z):
    G = exchange_matrix(w_pn, z)
    I = mp.eye(4)
    d = mp.det(I + G)
    return d, (None if d <= 0 else -mp.log(d))


def main() -> int:
    t0 = time.monotonic()
    q, qi, z = load_q_50dps()
    # E₀ = m_e / (q(q−1)) — the same substrate energy unit used across the
    # value-leg probes.  m_e from the single-source CODATA anchor (Copilot #3426).
    m_e = mp.mpf(str(M_E_MEV))
    import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590)
    E0 = _qbeta_e0.order_zero_scaled(m_e, q)  # order-zero E_0, routed (owner ruling 2026-11-20, #8590)
    b4_target = mp.mpf("9.243")

    rows = []
    for w_pn in (-1, 0, +1):
        d, nld = neg_log_det_I_plus_G(w_pn, z)
        if nld is None:
            mev = None
            ratio = None
            status = "UNPHYSICAL (det ≤ 0 ⇒ −ln det complex)"
        else:
            mev = E0 * nld
            ratio = mev / b4_target
            status = f"{float(ratio):.3f}× of b₄ (={float(mev):.3f} MeV)"
        rows.append({
            "w_pn": w_pn,
            "det_I_plus_G": mp.nstr(d, 8),
            "neg_log_det": (None if nld is None else mp.nstr(nld, 8)),
            "MeV": (None if mev is None else mp.nstr(mev, 8)),
            "ratio_to_b4": (None if ratio is None else mp.nstr(ratio, 6)),
            "status": status,
        })

    # Sensitivity disclosure (NOT a selection): the pn=0 chain case is
    # block-diagonal (1−z²)² by construction; record it explicitly.
    z2 = z * z
    block_diag_det = (1 - z2) ** 2

    # Physicality ceiling for the mixed-sign (pn=±1) case: det(I+g·S) = ∏(1+g·μ_k)
    # over the eigenvalues μ_k of the sign matrix S.  det ≤ 0 iff g ≥ 1/|μ_min|
    # (μ_min the most-negative eigenvalue).  This is a STRUCTURAL BOUND (an
    # eigenvalue of the read-off sign pattern), NOT a fit: it says the [1⁴]
    # framing must supply a per-pair magnitude BELOW this ceiling for physicality
    # — and the naive bond factor z EXCEEDS it, which is why pn=±1 fail at z.
    S_pn1 = exchange_matrix(+1, mp.mpf(1))          # sign matrix (magnitude 1)
    try:
        eigs, _ = mp.eig(S_pn1)                      # (eigenvalues, eigenvectors)
        mu = sorted(float(mp.re(e)) for e in eigs)
        mu_min = mu[0]
        g_ceiling = 1.0 / abs(mu_min) if mu_min < 0 else None
    except Exception:  # pragma: no cover - eig fallback
        mu = None
        mu_min = None
        g_ceiling = None

    result = {
        "shell": "⁴He [1⁴] complete graph, 6 pairs (1 pp, 1 nn, 4 pn)",
        "constants": {
            "q0": mp.nstr(q, 12),
            "z_bond_factor": mp.nstr(z, 10),
            "E0_MeV": mp.nstr(E0, 8),
            "b4_target_MeV": "9.243",
        },
        "derived_signs": {
            "pp": "+1 (σ, positive crossing) — from atom_braid_word_3A",
            "nn": "−1 (σ⁻¹, negative crossing = bar-mirror of pp) — from atom_braid_word_3A",
        },
        "open_sign": "w_pn ∈ {−1, 0, +1} — set by the [1⁴] framing (chain word averages to 0, "
                     "which decouples pn and is physically excluded for the pn-dominated shell)",
        "enumeration": rows,
        "pn0_block_diagonal_check": {
            "det_closed_form_(1-z^2)^2": mp.nstr(block_diag_det, 8),
            "note": "pn=0 ⇒ G block-diagonal (pp block ⊕ nn block); pn pairs contribute nothing.",
        },
        "mixed_sign_physicality_ceiling": {
            "sign_matrix_eigs_pn+1": (None if mu is None else [f"{m:.5f}" for m in mu]),
            "mu_min": (None if mu_min is None else f"{mu_min:.6f}"),
            "g_ceiling_for_det_gt_0": (None if g_ceiling is None else f"{g_ceiling:.6f}"),
            "z_bond_factor": mp.nstr(z, 8),
            "z_exceeds_ceiling": (None if g_ceiling is None else bool(float(z) > g_ceiling)),
            "note": ("STRUCTURAL BOUND (not a fit): for pn=±1 the sign pattern's most-negative "
                     "eigenvalue forces det(I+g·S) ≤ 0 once per-pair magnitude g ≥ 1/|μ_min|. "
                     "The naive bond factor z EXCEEDS this ceiling ⇒ pn=±1 unphysical at z. The "
                     "[1⁴] framing must supply a REDUCED (or non-uniform) per-pair magnitude "
                     "below the ceiling — a sharper open than the sign alone."),
        },
        "verdict": (
            "The pp/nn signs are DERIVED (+1/−1) from the framework's own crossing convention; "
            "only the pn sign is open. Enumerating w_pn∈{−1,0,+1} at the derived magnitude z: "
            "pn=±1 give det<0 (UNPHYSICAL — the mixed-sign pattern over-rotates at magnitude z), "
            "pn=0 (the chain convention) gives 2.40 MeV (0.26×) AND decouples the pn pairs "
            "(block-diagonal — physically excluded for the pn-dominated shell). So NO discrete pn "
            "sign closes at magnitude z. The sharper finding: the sign pattern's most-negative "
            "eigenvalue caps the physical per-pair magnitude at g_ceiling < z, so the [1⁴] framing "
            "must supply a mixed sign (pn=±1) AND a reduced/non-uniform per-pair magnitude below "
            "the ceiling — NOT the naive bond factor z. No magnitude is solved-for to hit 9.243 "
            "(that would be a fit, Rule-14, refused); only the structural ceiling (an eigenvalue of "
            "the read-off sign pattern) is reported. Fixing sign+magnitude needs the explicit [1⁴] "
            "link diagram (open; candidate source #3407 Reeb Lk_R^{(k)}, still a stub)."),
    }

    payload = {
        "computation": "b4-1four-complete-graph-writhe-signs",
        "description": ("[1⁴] complete-graph exchange matrix from read-off writhe signs: pp=+1, "
                        "nn=−1 (derived from atom_braid_word_3A); pn sign open, enumerated over "
                        "{−1,0,+1} at bond-factor magnitude z. −ln det(I+G) in MeV vs b₄=9.243. No "
                        "fit; the pn sign needs the [1⁴] framing (open). audit-only."),
        "tier": "structural (enumeration of 3 discrete pn signs; derived pp/nn signs; no tuning)",
        "result": result,
        "context": {
            "axis": "GAP-A-4 class-D — [1⁴] value leg, complete-graph writhe signs",
            "spec": "docs/design/2026-07-06-gap-a4-writhe-derivation-lit-review-and-framework.md",
            "status": "pp/nn signs derived; pn sign open (needs [1⁴] framing / #3407 Lk_R^{(k)})",
        },
    }
    wb = WitnessBuilder.wrap_legacy(
        "b4-1four-complete-graph-writhe-signs", payload,
        script_path=__file__, engine="python+mpmath", output_dir=os.path.join(COMP, "probes"),
        start_time=t0,
    )
    # Derived-sign assertions (not fits): pp positive, nn negative.
    wb.add_assertion("pp_sign_positive_from_convention",
                     computed=str(pair_sign(0, 1, 0)), expected="1")
    wb.add_assertion("nn_sign_negative_from_convention",
                     computed=str(pair_sign(2, 3, 0)), expected="-1")
    # pn=0 decouples the shell (block-diagonal): the physical exclusion of the
    # chain convention for the [1⁴] value.
    d0, _ = neg_log_det_I_plus_G(0, z)
    wb.add_assertion("pn0_is_block_diagonal_(1-z2)^2",
                     computed=mp.nstr(d0, 6), expected=mp.nstr((1 - z * z) ** 2, 6))
    out = wb.save(extra={"auditOnly": True})

    print("=== [1⁴] complete-graph exchange matrix — read-off writhe signs ===")
    print(f"  q₀={float(q):.6f}  z={float(z):.6f}  E₀={float(E0):.4f} MeV  b₄_target=9.243 MeV")
    print("  DERIVED signs (from atom_braid_word_3A): pp=+1 (σ), nn=−1 (σ⁻¹)")
    print("  OPEN sign: w_pn (set by the [1⁴] framing; chain word averages to 0 → decouples pn)")
    print("  " + "-" * 66)
    for r in rows:
        print(f"  w_pn={r['w_pn']:+d}  det(I+G)={r['det_I_plus_G']:>12}  {r['status']}")
    print("  " + "-" * 66)
    if g_ceiling is not None:
        print(f"  sign-pattern μ_min={mu_min:+.4f} ⇒ physical magnitude ceiling g<{g_ceiling:.4f}"
              f"  (z={float(z):.4f} EXCEEDS it ⇒ pn=±1 unphysical at z)")
    print("  VERDICT: pp/nn derived; pn sign OPEN. Mixed sign needs magnitude < ceiling < z —")
    print("           the framing must supply BOTH (needs [1⁴] diagram / #3407 Lk_R^{(k)}).")
    print("           No sign/magnitude solved-for to hit 9.243 (fit refused).")
    print("witness ->", out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
