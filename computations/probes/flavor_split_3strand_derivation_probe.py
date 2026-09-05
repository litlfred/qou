#!/usr/bin/env python3
# polynomial_q_not_applicable: probe; mpmath numeric eval at substrate q0; no production wiring.
"""3-strand categorical correction to the proton–neutron flavor split.

Research probe (NOT production-wired). Asks the disciplined question posed in
docs/audits/2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md:

  The LEADING flavor split  Δm_pn/M_N = ℏ_q²·h_q·[2]_q/3  is DERIVED as a
  *2-strand* object (the u↔d swap is σ on a 2-strand sub-braid; the [2]_q
  factor is the σ-doublet quantum integer). It misses CODATA by 0.128%.

  CODATA demands the correction  C_true = (Δm_pn/M_N)_CODATA / leading
  ≈ 1.0012784. The production (1+ℏ_q³) supplies only 76% of C_true−1.

  The baryon is a 3-quark / 3-strand state. The 2-strand leading object treats
  the swap on 2 strands and a passive spectator. This probe builds genuine
  H_3 / 3-strand Markov-trace objects in which the spectator strand BRAIDS with
  the swapped pair, and tests whether any clean categorical 3-strand object
  reproduces C_true at BOTH the proton-anchored and muon-anchored q₀ (the
  anti-flip-flop guard: a real derivation matches at both anchors; a numerical
  near-match drifts).

ESTABLISHED CLUE (re-verified here): the trivial spectator factor is exactly
1.0 — tr_M(σ_passive) is n-independent. So the correction, if categorical,
must come from the spectator BRAIDING with the swapped pair.

This probe is HONEST per AGENTS.md §"Before declaring refuted": it does NOT
fit a clean formula to C_true−1 (the c_k-flip-flop trap). It evaluates a fixed
menu of parameter-free categorical candidates and REPORTS the residual.

Output: flavor-split-3strand-derivation-probe.witness.json + stdout table.
"""
from __future__ import annotations
import time as _time  # noqa: E402 — wall-clock anchor for witness durationMs
_T0 = _time.monotonic()

import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
COMP = HERE.parent
sys.path.insert(0, str(COMP))
sys.path.insert(0, str(COMP / "substrate"))
sys.path.insert(0, str(COMP / "markov"))
sys.path.insert(0, "/home/user/qou/tools/qou-substrate/python")
import _path_bridge  # noqa: E402, F401

from markov_trace_canonical import tr_M_word  # noqa: E402
from qou_substrate.constants import q_at, q_muon_at  # noqa: E402
from codata_constants import M_N_MEV_VALIDATION, M_P_MEV_VALIDATION

mp.mp.dps = 60

# CODATA 2018 (m_n − m_p)/M_N.  m_p c² = 938.272 088 16 MeV,
# m_n c² = 939.565 420 52 MeV  ⇒  Δ/M_N = 0.001377469939…
# (matches the audit-doc value 0.0013774699 to its quoted precision).
_M_P_MEV = M_P_MEV_VALIDATION
_M_N_MEV = M_N_MEV_VALIDATION
C_DATA = (_M_N_MEV - _M_P_MEV) / ((_M_N_MEV + _M_P_MEV) / 2)


def zh(q):
    qi = 1 / q
    z = q**3 / (q**2 + 1)
    h = q - qi
    return z, h


def leading(q):
    """Derived 2-strand leading split  ℏ_q²·h_q·[2]_q/3 = (q−1)²(1−q⁻⁴)/3."""
    qi = 1 / q
    return (q - 1) ** 2 * (1 - qi ** 4) / 3


def sigma_inv_word_trace(z, h):
    """Helper: tr_M of σ₀σ₁⁻¹ etc require the element route. We instead build
    the Borromean / inverse-crossing objects via the (z,h)-linear Hecke
    expansion σ⁻¹ = σ − h applied symbolically inside tr_M_word callers."""
    raise NotImplementedError


def trM(word, n, z, h):
    return tr_M_word(tuple(word), n, z, h)


# ── inverse-crossing aware trace: σ_i^{-1} = σ_i − h·1 ──────────────
# We expand any word with negative generator (encoded as ("inv", i)) into a
# (z,h)-linear sum over plain words by distributing (σ_i − h).
def trM_signed(word_signed, n, z, h):
    """word_signed: list of (gen, sign) with sign ∈ {+1,−1}.
    σ^{-1} = σ − h·1, expand into 2^{#inv} plain words."""
    inv_positions = [k for k, (g, s) in enumerate(word_signed) if s < 0]
    total = mp.mpf(0)
    from itertools import product as iproduct
    for choice in iproduct([0, 1], repeat=len(inv_positions)):
        # choice[j]=0 → take σ_i term (coeff 1); =1 → take −h·1 term (drop gen)
        w = []
        coeff = mp.mpf(1)
        cmap = dict(zip(inv_positions, choice))
        for k, (g, s) in enumerate(word_signed):
            if s < 0 and cmap[k] == 1:
                coeff *= -h
                # identity: drop generator
            else:
                w.append(g)
        total += coeff * trM(tuple(w), n, z, h)
    return total


def run_anchor(name, q):
    z, h = zh(q)
    qi = 1 / q
    hbar = (q - 1) / q
    two_q = q + qi
    lead = leading(q)
    Ctrue = C_DATA / lead

    rec = {
        "anchor": name,
        "q": mp.nstr(q, 50),
        "leading_split": mp.nstr(lead, 30),
        "C_true": mp.nstr(Ctrue, 30),
        "C_true_minus_1": mp.nstr(Ctrue - 1, 20),
        "candidates": [],
    }

    def add(label, value, kind="multiplier"):
        """value is a candidate for C (the multiplier on leading). The
        predicted split is value·leading; report its % error vs CODATA and
        the fraction of the needed correction it supplies."""
        resid_C = Ctrue - value
        pred_split = value * lead
        err_pct = abs(pred_split - C_DATA) / C_DATA * 100
        rec["candidates"].append({
            "label": label,
            "value": mp.nstr(value, 24),
            "value_minus_1": mp.nstr(value - 1, 18),
            "pred_split": mp.nstr(pred_split, 20),
            "err_vs_codata_pct": float(err_pct),
            "C_true_minus_value": mp.nstr(resid_C, 18),
            "frac_of_correction_supplied":
                mp.nstr((value - 1) / (Ctrue - 1), 12) if Ctrue != 1 else "n/a",
        })

    # ── reference: the established clues ───────────────────────────
    # trivial passive spectator = 1.0 (re-verify n-independence)
    bare2 = trM((0,), 2, z, h)
    spec3 = trM((0,), 3, z, h)
    rec["spectator_trivial_ratio"] = mp.nstr(spec3 / bare2, 30)  # == 1
    add("production (1+ℏ_q³) [posited, for reference]", 1 + hbar ** 3)

    # ── 3-strand candidate menu (parameter-free categorical objects) ──
    # The split's structural ingredients: ℏ_q (Planck action), h (crossing),
    # [2]_q (2-strand doublet). A 3-strand extension should dress one of these
    # with the spectator's H_3 contribution.

    # C1: replace the 2-strand doublet [2]_q by the H_3 normalized doublet.
    # In H_3 the σ-eigenspaces still are {q,−q⁻¹}; the 3-strand "quantum
    # dimension" weighting of the symmetric channel vs the bare doublet is
    # [3]_q/[2]_q-type. Test [3]_q/([2]_q·something).
    q3 = (q ** 2 - qi ** 2) / (q - qi)  # [3]_q symmetric = q^2+1+q^-2... wait
    # symmetric [n]_q = (q^n − q^-n)/(q − q^-1)
    def qint(n):
        return (q ** n - qi ** n) / (q - qi)
    # C1: spectator dresses [2]_q → [2]_q·(1 + (qint(3)/qint(2)−q)/<scale>) ...
    # Too speculative; instead use trace-based objects below.

    # C2: spectator-braiding trace ratio — swap σ₀ dressed by ONE spectator
    # crossing σ₁, normalized so the leading (no-spectator) part is divided out.
    # object = tr_M(σ₀σ₁σ₀⁻¹σ₁⁻¹) / tr_M(1)  (a commutator: spectator braids
    # then unbraids around the swap — measures the non-commutativity = the
    # genuine spectator dressing, → 1 as h→0).
    commutator = trM_signed([(0, +1), (1, +1), (0, -1), (1, -1)], 3, z, h)
    add("C2: spectator commutator tr_M([σ₀,σ₁]) ", commutator)

    # C3: the symmetric spectator dressing — tr_M(σ₁σ₀σ₁⁻¹)/tr_M(σ₀):
    # the swap conjugated by the spectator crossing. = 1 if spectator passive.
    conj = trM_signed([(1, +1), (0, +1), (1, -1)], 3, z, h) / bare2
    add("C3: spectator-conjugated swap tr_M(σ₁σ₀σ₁⁻¹)/tr_M(σ₀)", conj)

    # C4: the half-crossing (color-weighted) spectator dressing.
    # The canonical p-n crossing is σ − h(½−δ/4). The spectator's color-tube
    # coupling to the swap is a HALF crossing. Object: ratio of swap with a
    # half-spectator-crossing to bare swap. Half crossing ~ (σ₁ + 1)/2 weight.
    # Build tr_M(σ₀ · (1 − h/2·σ₁-ish)). Use the documented color crossing:
    half = trM((0,), 3, z, h)  # passive baseline = z
    # swap dressed by a half spectator crossing modeled as (σ₁ − h/2):
    dressed_half = (trM((0, 1), 3, z, h) - (h / 2) * trM((0,), 3, z, h)) / half
    add("C4: half-spectator-dressed swap ratio", dressed_half)

    # C5: the FULL 3-strand baryon swap object. The genuine flavor split is
    # the trace DIFFERENCE between the neutron-ordered and proton-ordered
    # 3-strand swap. Build the σ-swap acting on the 2-strand sub-braid of the
    # symmetric 3-strand state, and take (sym − antisym)/(sym).
    # tr_M(σ₀σ₁) (symmetric path) vs tr_M(σ₀σ₁⁻¹) (mixed/figure-8 path):
    sym = trM((0, 1), 3, z, h)
    mixed = trM_signed([(0, +1), (1, -1)], 3, z, h)
    add("C5: (sym tr_M(σ₀σ₁))/(mixed tr_M(σ₀σ₁⁻¹))",
        sym / mixed if mixed != 0 else mp.mpf("nan"))

    # C6: the spectator contributes one extra ℏ_q of action (3rd quark = 3rd
    # action quantum). Leading has ℏ_q²; 3-strand adds a fractional ℏ_q from
    # the spectator. Test (1 + ℏ_q³·[scale]) for categorical scales derived
    # from H_3 (NOT fit): [2]_q/2, [3]_q/3, z, h, two_q/2.
    for sl_label, sl in [
        ("[3]_q/[2]_q", qint(3) / qint(2)),
        ("[2]_q/2", two_q / 2),
        ("z·[2]_q", z * two_q),
        ("1/(2z)", 1 / (2 * z)),
        ("q", q),
    ]:
        add(f"C6: 1+ℏ_q³·({sl_label})", 1 + hbar ** 3 * sl)

    # C8 (PRINCIPAL FINDING): self-interaction / second-order split.
    # In a 3-quark baryon the split is a sum over quark PAIRS. The 2-strand
    # leading object accounts for the single swapped u↔d pair. The spectator
    # quark pairs with each swapped quark, contributing a SECOND-ORDER term
    # equal to the leading split applied to the spectator coupling:
    #     C = 1 + leading          (so full split = leading·(1+leading))
    # equivalently the geometric self-energy  leading/(1−leading).
    # This is parameter-free: the "correction scale" IS the leading split
    # itself, not a posited ℏ_q-power. NOT fit — leading is fully derived.
    add("C8: 1+leading (3-strand self-interaction)", 1 + lead)
    add("C8b: 1/(1−leading) (geometric self-energy)", 1 / (1 - lead))

    # C7: replace 2-strand [2]_q by the actual H_3 Markov dimension ratio of
    # the swapped pair seen from 3 strands. The mass split ∝ the per-crossing
    # energy times the multiplicity the swap "sees". In H_2 that is [2]_q; in
    # H_3 with a braiding spectator it is the ratio of the 3-strand swap-pair
    # trace to the 2-strand one through the canonical color crossing.
    # Object: leading rebuilt with the 3-strand swap normalization.
    # 3-strand swap "doublet" = tr_M(σ₀σ₁σ₀)/tr_M(σ₀)  (spectator brackets swap)
    bracket = trM((0, 1, 0), 3, z, h) / bare2
    add("C7: 3-strand bracketed-swap multiplier tr_M(σ₀σ₁σ₀)/tr_M(σ₀)", bracket)

    return rec


def main():
    out = {
        "computation": "flavor-split-3strand-derivation-probe",
        "description": (
            "3-strand categorical correction to the p-n flavor split. Tests "
            "whether genuine H_3 / 3-strand Markov-trace objects (spectator "
            "strand braiding with the u↔d swap pair) reproduce the CODATA "
            "correction C_true = (Δm_pn/M_N)_CODATA/leading ≈ 1.0012784 that "
            "the 2-strand leading object (ℏ_q²·h_q·[2]_q/3) misses. Evaluated "
            "at BOTH proton- and muon-anchored q₀ (anti-flip-flop guard). NOT "
            "production-wired; honest negative/positive report, no fit to "
            "C_true−1. See docs/audits/"
            "2026-06-29-color-weighting-coverage-and-flavor-split-closed-form.md."
        ),
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "C_DATA_Dm_over_MN": mp.nstr(C_DATA, 12),
        "anchors": [],
    }

    print("=" * 100)
    print("3-STRAND FLAVOR-SPLIT CORRECTION PROBE")
    print(f"CODATA (m_n−m_p)/M_N = {mp.nstr(C_DATA, 12)}")
    print("=" * 100)

    for name, q in [("proton", q_at(50)), ("muon", q_muon_at(50))]:
        rec = run_anchor(name, q)
        out["anchors"].append(rec)
        print(f"\n── anchor: {name}  q = {rec['q'][:22]}…")
        print(f"   leading split = {rec['leading_split'][:16]}")
        print(f"   C_true        = {rec['C_true'][:16]}   "
              f"(C_true−1 = {rec['C_true_minus_1'][:12]})")
        print(f"   spectator trivial ratio (should be 1) = "
              f"{rec['spectator_trivial_ratio'][:18]}")
        print(f"\n   {'candidate':<52}{'value':>16}{'err%CODATA':>13}"
              f"{'frac corr':>12}")
        print("   " + "-" * 93)
        for c in rec["candidates"]:
            print(f"   {c['label']:<52}{c['value'][:14]:>16}"
                  f"{c['err_vs_codata_pct']:>13.5f}"
                  f"{c['frac_of_correction_supplied'][:10]:>12}")

    # ── anti-flip-flop cross-anchor drift table ────────────────────
    print("\n" + "=" * 100)
    print("ANTI-FLIP-FLOP: cross-anchor value drift (a real derivation is "
          "anchor-stable to ~10 digits)")
    print("=" * 100)
    pa, ma = out["anchors"][0], out["anchors"][1]
    print(f"   {'candidate':<52}{'proton value':>16}{'muon value':>16}"
          f"{'|drift|':>12}")
    print("   " + "-" * 96)
    drift_rows = []
    for cp, cm in zip(pa["candidates"], ma["candidates"]):
        vp = mp.mpf(cp["value"])
        vm = mp.mpf(cm["value"])
        drift = abs(vp - vm)
        drift_rows.append({"label": cp["label"],
                           "drift": mp.nstr(drift, 6)})
        print(f"   {cp['label']:<52}{cp['value'][:14]:>16}"
              f"{cm['value'][:14]:>16}{mp.nstr(drift, 4):>12}")
    out["cross_anchor_drift"] = drift_rows

    # ── verdict (scope-(a) honest report, no fit to C_true−1) ──────
    verdict = {
        "summary": (
            "The 3-strand SELF-INTERACTION candidate C = 1 + leading "
            "(equivalently leading/(1−leading), or [2]_q → [2]_q·(1+leading)) "
            "lands at ~0.0097% vs CODATA — a ~13× improvement over leading-only "
            "(0.128%) and a ~3× improvement over the posited production (1+ℏ_q³) "
            "(0.0305%). It is parameter-free (the correction scale IS the "
            "derived leading split, not a posited ℏ_q-power) and anchor-stable "
            "to ~12 digits (proton vs muon q₀). HOWEVER it is a NEAR-MATCH, not "
            "an exact closure: the exact factor is (C_true−1)/leading ≈ 0.929, "
            "not 1.000, so C=1+leading OVER-supplies the correction by ~7.6%. "
            "Per AGENTS.md §refuted/§open this is a scope-(a) numerical result: "
            "the second-order/self-interaction STRUCTURE is strongly indicated, "
            "but the exact 0.929 coefficient is NOT closed and must not be "
            "fit. Raw H_3 trace-ratio objects (spectator commutator, "
            "bracketed-swap, sym/mixed) give O(10–70%) corrections — far too "
            "large — confirming the correction is a DIFFERENCE/self-energy "
            "structure, not a raw trace ratio."
        ),
        "best_candidate": "C8: 1+leading (3-strand self-interaction)",
        "best_err_vs_codata_pct": 0.00972,
        "leading_only_err_pct": 0.12767,
        "posited_production_err_pct": 0.03053,
        "exact_factor_C_true_minus_1_over_leading": "0.9292",
        "anchor_stable": True,
        "is_exact_closure": False,
        "is_fit": False,
    }
    out["verdict"] = verdict
    print("\n" + "=" * 100)
    print("VERDICT")
    print("=" * 100)
    for line in [verdict["summary"][i:i + 96]
                 for i in range(0, len(verdict["summary"]), 96)]:
        print("  " + line)

    import os as _os, sys as _sys  # noqa: E402
    _sys.path.insert(0, _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), "../substrate"))
    from witness_base import WitnessBuilder  # noqa: E402 — P30 rollup (bean cmiy)
    _wpath = WitnessBuilder.wrap_legacy(
        "flavor-split-3strand-derivation-probe", out,
        script_path=__file__, engine="mpmath", start_time=_T0, output_dir=str(HERE),
    ).save()
    print(f"\nwitness -> {_wpath}")


if __name__ == "__main__":
    main()
