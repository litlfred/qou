#!/usr/bin/env python3
"""helium_four_body_cluster_probe.py — Route-3: does the DERIVED Borromean-cluster
recipe (#4360 sign / #4364 magnitude lift) extend to A=4 (⁴He)?

The question
------------
For A=3 the derived Brunnian/Borromean cluster c₃ = E₀·(1 − τ_Borr) supplied the
POSITIVE 3-body residual moment μ₃ = +0.4708 (sign #4360; magnitude lifted ~49× to
0.63·μ₃ at the H₉ cabled level, #4364). For A=4 the natural analog is a
4-component Brunnian cluster c₄ = E₀·(1 − τ_L₄), realized the SAME way — a trace
DEFICIT against the unlink. Does the same 0-fit recipe reproduce the ⁴He 4-body
residual?

The DERIVED A=4 target (forward AME − model, 0 fit)
---------------------------------------------------
The exact 0-parameter simplex (Mayer) decomposition of the graded-subtracted
residual M(A) = ρ_strong(A) − ρ_grad(A) over the derived coordination counts
C(A,k), pinned by the three points A = 2,3,4 (AdditiveResidualSimplex #4320,
deltalambda_kappa_interface_residual_simplex_probe.py), gives

    μ₂ = 0,   μ₃ = +0.4708,   μ₄ = −4.591.

The genuinely-4-body coefficient μ₄ = −4.591 is NEGATIVE — the closed [1⁴] SU(4)
supermultiplet / α-cluster SATURATION signature (μ₄ = s₄ − g₄, the graded
reference's own 4-body simplex coefficient g₄ = +8.37 over-subtracts). This is a
FORWARD computation, never an inversion.

The sign obstruction (the finding)
----------------------------------
A trace deficit against the unlink is a BINDING object: whenever the link trace
lies at or below the unlink (τ ≤ 1) the cluster c = E₀·(1 − τ) ≥ 0. #4360 proved
this for the bare Borromean (1 − τ_Borr = h⁴(3+h²)/(h²+4) ≥ 0). So a Brunnian-
DEFICIT realization of the A=4 cluster is NON-NEGATIVE — sign-INCOMPATIBLE with the
derived μ₄ < 0. The recipe walls on SIGN at A=4. This mirrors #4354 (μ₃>0 excludes
the ≤0 multiplicative cluster); here μ₄<0 excludes the ≥0 Brunnian deficit — a sign
SWAP across the isotope step.

This probe measures the antecedent of the (scope-(b), conditional) Lean sign wall
`QOU.MassTheory.HeliumFourBodyCluster.mu4_ne_brunnian4Cluster`: is the 4-block
cabled Brunnian deficit ≥ 0 (τ ≤ 1) at the substrate q₀? It (i) forward-derives
μ₄; (ii) validates the machinery on the bare A=3 Borromean (deficit +, O(h⁴));
(iii) computes the width-3 cabled 4-block linking-word deficit at H₁₂, its sign,
leading h-order, and the delete-one-block sub-link profile (the operational
Brunnian test); (iv) reads the sign-compatibility with μ₄ < 0.

STRICT anti-fit: 0 free params; μ₄ is a forward AME−model datum, never inverted;
no level/cabling tuned to hit any target; nothing wired. The 4-component Brunnian
link is non-unique — the cabled block-word here is the direct analog of the A=3
(Δ_A·Δ_B⁻¹)³ construction, reported with its sub-link profile, NOT claimed to be
THE canonical 4-Brunnian link.
"""
from __future__ import annotations

import sys as _sys
from pathlib import Path as _Path
_COMP = _Path(__file__).resolve().parent.parent
for _d in ("hecke", "habiro", "substrate"):
    _p = str(_COMP / _d)
    if _p not in _sys.path:
        _sys.path.insert(0, _p)
_sys.path.insert(0, str(_COMP))
import _path_bridge  # noqa: E402, F401

import json  # noqa: E402
import time  # noqa: E402
import hashlib  # noqa: E402
import subprocess  # noqa: E402
from datetime import datetime, timezone  # noqa: E402

import mpmath as mp  # noqa: E402
import pyhecke_native  # noqa: E402

from wedderburn_jones_markov import y_lambda_at  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps(30)
HERE = _Path(__file__).resolve().parent
_T0 = time.time()


def _log(msg: str) -> None:
    print(f"[{time.time() - _T0:7.1f}s] {msg}", flush=True)


q0 = mp.mpf(str(Q0))
q0f = float(Q0)
H = q0 - 1 / q0
E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))     # SAME E₀ ρ_F / #4364 use


# =========================================================================
# (i) FORWARD-derive the A=4 residual target μ₄ (AME − model, 0 fit).
#     Byte-identical to deltalambda_kappa_interface_residual_simplex_probe.
# =========================================================================
def qint(n, q):
    return sum(q ** k for k in range(n))


def qfac_over_2(A, q):
    r = mp.mpf(1)
    for k in range(3, A + 1):
        r *= qint(k, q)
    return r


def derive_mu4():
    from math import comb
    rho_grad = {A: qfac_over_2(A, q0) for A in (2, 3, 4)}
    # ρ_strong: Coulomb/isospin-corrected AME comparison constants (TARGETS only);
    # ρ_strong(2)=1 is the deuteron self-reference (DERIVED, not an AME datum).
    rho_strong = {2: mp.mpf(1), 3: mp.mpf("3.8128"), 4: mp.mpf("13.0316")}
    M = {A: rho_strong[A] - rho_grad[A] for A in (2, 3, 4)}
    mu2 = M[2]
    mu3 = M[3] - 3 * mu2
    mu4 = M[4] - 6 * mu2 - 4 * mu3
    # self-check: exact reconstruction (it is a solve, 0 free params)
    for A in (2, 3, 4):
        recon = mu2 * comb(A, 2) + mu3 * comb(A, 3) + mu4 * comb(A, 4)
        assert abs(recon - M[A]) < mp.mpf("1e-25"), f"simplex must reproduce M({A})"
    return mu2, mu3, mu4, M


# =========================================================================
# Perblock joint trace at level n:  g(word) = Σ_{λ⊢n} y_λ·|χ_λ(word)|  (0-fit)
# =========================================================================
_YCACHE: dict[tuple, dict] = {}


def _yn(n, qv):
    key = (n, str(qv))
    if key not in _YCACHE:
        _YCACHE[key] = {tuple(k) if isinstance(k, (list, tuple)) else k: mp.mpf(str(v))
                        for k, v in y_lambda_at(n, qv).items()}
    return _YCACHE[key]


def _perblock(n, word, qv=None):
    """EXACT ρ_F perblock trace at level n (kernel gen index 1-based, as #4364)."""
    qv = q0 if qv is None else qv
    Y = _yn(n, qv)
    factors = [(float(c), float(d), int(g) + 1) for (c, d, g) in word]
    cp = pyhecke_native.chi_q_atomic_all_partitions(n, factors, float(qv))
    return sum(Y[tuple(s)] * abs(mp.mpf(repr(chi))) for s, chi in cp if tuple(s) in Y)


# =========================================================================
# Braid words: bare Borromean (A=3 validation) + cabled block transpositions
# =========================================================================
def borromean_bare(h=None):
    """(σ₁σ₂⁻¹)³ on 3 strands (0-based gens 0,1). Inverse = σ_g − h·I."""
    hh = H if h is None else h
    w = []
    for _ in range(3):
        w += [(1.0, 0.0, 0)]              # σ₁
        w += [(1.0, float(-hh), 1)]       # σ₂⁻¹
    return w


def _block_transposition(a: int, w: int = 3):
    """Positive block-transposition swapping cables [a..a+w-1] and [a+w..a+2w-1]
    (descending-run cabling word; identical to #4364)."""
    gens = []
    for r in range(w):
        for g in range(a + w - 1 + r, a - 1 + r, -1):
            gens.append(g)
    return gens


def _pos(g):
    return (1.0, 0.0, g)


def _neg(g, h):
    return (1.0, float(-h), g)


def cabled_word(pattern, h=None, w=3):
    """Build a width-w cabled inter-block word from a pattern of (block_pair, sign)
    tokens, each an adjacent block transposition. Blocks are 0..k-1; token
    ('AB',+1) => Δ between cables (0,1); ('BC',-1) => Δ⁻¹ between cables (1,2); etc.
    Δ_{block p↔p+1} uses generators starting at a = p*w."""
    hh = H if h is None else h
    base = {"AB": 0, "BC": 1 * w, "CD": 2 * w}   # starting cable index a for each pair
    word = []
    for tok, sgn in pattern:
        a = base[tok]
        gens = _block_transposition(a, w)
        if sgn > 0:
            word += [_pos(g) for g in gens]
        else:
            word += [_neg(g, hh) for g in reversed(gens)]
    return word


# =========================================================================
# Deficit + h-order diagnostics
# =========================================================================
def deficit(n, word, qv=None):
    """dimensionless 1 − g_link/g_unlink at level n."""
    g_link = _perblock(n, word, qv)
    g_unlink = _perblock(n, [], qv)
    return 1 - g_link / g_unlink, g_link, g_unlink


def leading_order(n, word_fn, grid=("1.02", "1.04", "1.08")):
    """log-log slope of |deficit(q)| across a q-grid => leading h-exponent."""
    pts = []
    for qv in grid:
        qm = mp.mpf(qv)
        hv = qm - 1 / qm
        w = word_fn(hv)
        d, _, _ = deficit(n, w, qm)
        pts.append((hv, d))
    (h1, d1), (h2, d2) = pts[0], pts[-1]
    n_ord = mp.log(abs(d2) / abs(d1)) / mp.log(h2 / h1) if d1 != 0 and d2 != 0 else mp.nan
    return n_ord, pts


def main() -> int:
    print("=" * 84)
    print("Route-3: A=4 (⁴He) 4-body cluster — does the Borromean-deficit recipe extend?")
    print(f"  q₀={float(q0):.8f}  h={float(H):.6f}  E₀={float(E0):.6f} MeV")
    print("=" * 84)

    # ── (i) forward-derived A=4 target ────────────────────────────────────────
    mu2, mu3, mu4, M = derive_mu4()
    _log("A=4 residual target (forward AME − model, 0 fit):")
    print(f"    μ₂(edge) = {mp.nstr(mu2,6)}   μ₃(triangle) = +{mp.nstr(mu3,6)}   "
          f"μ₄(tetra) = {mp.nstr(mu4,6)}")
    print(f"    ⇒ μ₄ = {mp.nstr(mu4,6)} MeV  sign = {'NEGATIVE' if mu4 < 0 else 'positive'}"
          f"  (closed [1⁴] SU(4) α-cluster SATURATION)")
    assert mu4 < 0, "derived μ₄ must be negative"

    # ── (ii) A=3 bare-Borromean machinery validation (deficit +, O(h⁴)) ───────
    _log("A=3 bare Borromean (σ₁σ₂⁻¹)³ — machinery validation")
    d3, gl3, gu3 = deficit(3, borromean_bare())
    n3, _ = leading_order(3, borromean_bare)
    c3_bare = E0 * gu3 * d3   # E₀·(g_unlink − g_link) = E₀·g_unlink·deficit
    print(f"    deficit 1−τ = {mp.nstr(d3,8)}  sign={'+' if d3 > 0 else '-'}  "
          f"leading order n≈{mp.nstr(n3,4)}  (expect + and 4)")
    print(f"    c₃(bare) = {mp.nstr(c3_bare,6)} MeV   (matches μ₃>0 sign — #4360)")
    # closed-form cross-check
    cf = H**4 * (3 + H**2) / (H**2 + 4)
    print(f"    closed-form 1−τ_Borr = h⁴(3+h²)/(h²+4) = {mp.nstr(cf,8)} (bare H₃ ref)")

    # ── (iii) A=4 width-3 cabled 4-block linking words at H₁₂ ─────────────────
    _log("A=4 width-3 cabled 4-block linking words at H₁₂ (77 partitions)")
    n = 12
    # Candidate patterns (each token = adjacent block transposition, ± sign).
    # P1: direct A=3-analog extended by a third pair — (AB·BC⁻¹·CD)³
    # P2: alternating commutator chain — (AB·BC⁻¹·CD·BC⁻¹)³ (block B shared)
    # P3: symmetric — (AB·BC⁻¹)³·(BC·CD⁻¹)³  (two Borromean sub-blocks, chain)
    candidates = {
        "P1_(AB·BC⁻¹·CD)³": [("AB", +1), ("BC", -1), ("CD", +1)] * 3,
        "P2_(AB·BC⁻¹·CD·BC⁻¹)³": [("AB", +1), ("BC", -1), ("CD", +1), ("BC", -1)] * 3,
        "P3_(AB·BC⁻¹)³(BC·CD⁻¹)³": [("AB", +1), ("BC", -1)] * 3 + [("BC", +1), ("CD", -1)] * 3,
    }
    results_a4 = {}
    for name, pat in candidates.items():
        _log(f"  candidate {name} ({len(pat)} block-tokens)")
        word = cabled_word(pat)
        d4, gl4, gu4 = deficit(n, word)
        c4 = E0 * gu4 * d4
        n4, _ = leading_order(n, lambda h, p=pat: cabled_word(p, h=h))
        # operational Brunnian test: delete each terminal block's crossings and
        # measure the residual sub-deficit (Brunnian ⇒ all proper sub-links trivial).
        sub = {}
        for drop in ("AB", "CD"):   # dropping a terminal pair ~ removing an end block
            wsub = cabled_word([(t, s) for (t, s) in pat if t != drop])
            dsub, _, _ = deficit(n, wsub)
            sub[f"drop_{drop}"] = mp.nstr(dsub, 6)
        results_a4[name] = {
            "n_tokens": len(pat), "n_crossings": len(word),
            "deficit_1_minus_tau": mp.nstr(d4, 8), "sign": "+" if d4 > 0 else "-",
            "tau_vs_unlink": ("below (τ<1, deficit +)" if d4 > 0
                              else "above (τ>1, deficit −)"),
            "c4_MeV": mp.nstr(c4, 6),
            "leading_h_order": mp.nstr(n4, 4),
            "sublink_deficits": sub,
            "sign_compatible_with_mu4_neg": bool(d4 < 0),
        }
        print(f"    deficit 1−τ = {mp.nstr(d4,8)}  sign={'+' if d4 > 0 else '-'}"
              f"  ({'τ>1 excess' if d4 < 0 else 'τ<1 deficit'})  "
              f"leading order n≈{mp.nstr(n4,4)}")
        print(f"    c₄ = {mp.nstr(c4,6)} MeV   sub-link(dropAB)={sub['drop_AB']} "
              f"sub-link(dropCD)={sub['drop_CD']}")
        print(f"    sign-compatible with μ₄<0 ? {'YES' if d4 < 0 else 'NO (deficit ≥0 ≠ μ₄<0)'}")

    # ── verdict ───────────────────────────────────────────────────────────────
    any_neg = any(r["sign"] == "-" for r in results_a4.values())
    all_pos = all(r["sign"] == "+" for r in results_a4.values())
    print("\n" + "=" * 84)
    if all_pos:
        verdict = ("SIGN WALL (scope-(a) confirmed): every deficit-realized 4-block "
                   "Brunnian cluster is POSITIVE (τ<1, c₄≥0), sign-INCOMPATIBLE with the "
                   "derived μ₄=−4.591<0. The Borromean-deficit BINDING recipe does NOT "
                   "extend to A=4 — the α-cluster residual is a SATURATION (negative) "
                   "object, structurally distinct. Mirror of #4354; a sign SWAP.")
    elif any_neg:
        verdict = ("MIXED: at least one 4-block linking word gives a NEGATIVE deficit "
                   "(τ>1 excess), sign-COMPATIBLE with μ₄<0 — the sign wall is construction-"
                   "dependent; the magnitude test becomes live for that word. Reported "
                   "honestly; nothing tuned.")
    else:
        verdict = "INDETERMINATE"
    print(f"VERDICT: {verdict}")
    print("=" * 84)

    witness = {
        "schema": "witness/v1",
        "producer": "computations/deltalambda/helium_four_body_cluster_probe.py",
        "computation": "helium-four-body-cluster",
        "description": (
            "Route-3: does the DERIVED Borromean-cluster recipe (#4360 sign / #4364 "
            "magnitude lift) extend to A=4 (⁴He)? The A=4 residual target is FORWARD-"
            "derived (AME − model, exact 0-parameter simplex solve): μ₂=0, μ₃=+0.4708, "
            "μ₄=−4.591 — the genuinely-4-body coefficient μ₄ is NEGATIVE (closed [1⁴] "
            "SU(4) α-cluster SATURATION, μ₄=s₄−g₄). A trace-deficit-against-the-unlink "
            "realization of the 4-component Brunnian cluster c₄=E₀·(1−τ_L4) is a BINDING "
            "object: whenever τ≤1 it is ≥0 (the #4360 shape). This probe validates the "
            "machinery on the bare A=3 Borromean (deficit +, O(h⁴)) and measures the "
            "width-3 cabled 4-block linking-word deficit sign + leading h-order + delete-"
            "one-block sub-link profile at H₁₂. Result feeds the (scope-(b), conditional-"
            "on-τ≤1) Lean sign wall QOU.MassTheory.HeliumFourBodyCluster.mu4_ne_"
            "brunnian4Cluster: a non-negative Brunnian deficit c₄≥0 ≠ the derived μ₄<0 — "
            "the recipe walls on SIGN at A=4 (mirror of #4354; a sign SWAP). STRICT "
            "anti-fit: 0 free params, μ₄ never inverted, no cabling tuned to a target, "
            "nothing wired; the 4-Brunnian link is non-unique and the block-word is the "
            "direct A=3-analog, reported with its sub-link profile, not claimed canonical."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "parameters": {
            "free_parameters": 0,
            "q0": str(q0), "h": str(H), "E0_MeV": str(E0),
            "level_a4": "H₁₂ perblock Σ_{λ⊢12} y_λ|χ_λ|, four width-3 nucleon cables",
            "note": "μ₄=−4.591 forward AME−model target only; SAME E₀+y_λ norm as #4364.",
        },
        "results": {
            "a4_residual_target": {
                "mu2_edge": mp.nstr(mu2, 8), "mu3_triangle": mp.nstr(mu3, 8),
                "mu4_tetra": mp.nstr(mu4, 8), "mu4_sign": "negative",
                "M": {str(A): mp.nstr(M[A], 8) for A in (2, 3, 4)},
                "derivation": "forward AME − graded model; exact 0-param simplex solve.",
            },
            "a3_borromean_validation": {
                "deficit_1_minus_tau": mp.nstr(d3, 8), "sign": "+" if d3 > 0 else "-",
                "leading_h_order": mp.nstr(n3, 4),
                "c3_bare_MeV": mp.nstr(c3_bare, 6),
                "closed_form_h4_ref": mp.nstr(cf, 8),
                "note": "reproduces #4360: positive deficit, O(h⁴), matches μ₃>0 sign.",
            },
            "a4_candidates": results_a4,
            "verdict": {
                "classification": verdict,
                "all_deficits_positive": bool(all_pos),
                "any_deficit_negative": bool(any_neg),
                "mu4_sign": "negative",
                "brunnian_deficit_sign_at_q0": ("positive (τ<1) for all candidates"
                                                if all_pos else "mixed"),
                "sign_wall": bool(all_pos),
                "is_fit": False, "wired": False, "free_param_count": 0,
                "scope": ("scope-(a) sign wall (if all deficits +): the derived Borromean-"
                          "deficit BINDING recipe gives c₄≥0, sign-incompatible with the "
                          "forward-derived μ₄<0. Elevated to scope-(b) by the Lean "
                          "mu4_ne_brunnian4Cluster CONDITIONAL on τ≤1 (measured here). The "
                          "A=4 α-cluster residual is a SATURATION object, not a binding "
                          "cluster — a sign SWAP vs A=3 (mirror of #4354's μ₃>0 wall)."),
                "anti_fit": "μ₄ forward AME−model, never inverted; no cabling/level tuned "
                            "to any target; 4-Brunnian link non-unique, block-word is the "
                            "direct A=3-analog with reported sub-link profile; nothing wired.",
            },
        },
        "scriptHash": hashlib.sha256(_Path(__file__).read_bytes()).hexdigest()[:16],
    }
    try:
        witness["scriptCommitSha"] = subprocess.check_output(
            ["git", "log", "-1", "--format=%H", "--", __file__],
            cwd=HERE, text=True).strip() or "uncommitted"
    except Exception:
        witness["scriptCommitSha"] = "uncommitted"
    out = HERE / "helium-four-body-cluster.witness.json"
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. resolve and stamp the q0 anchor.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=None)
    out.write_text(json.dumps(witness, indent=2) + "\n")
    _log(f"witness -> {out.relative_to(_COMP.parent)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
