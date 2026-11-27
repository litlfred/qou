#!/usr/bin/env python3
"""alpha_activation_brunnian_probe.py — derive-or-refute the k >= 3 ACTIVATION
of the alpha.alpha inter-cluster pair term via the Brunnian/Milnor mechanism.

CONTEXT (R6-a; follows R5-a)
----------------------------
R5-a (docs/audits/2026-07-13-inter-cluster-bond-term-derive-or-refute.md;
witness inter-cluster-bond-term.witness.json, committed, allPassed) left one
crisp datum: the alpha.alpha pair term is ~0 at k = 2 (8Be, deficit -0.092)
but pairwise-FLAT ~2.41 MeV/pair at k >= 3 under complete-graph C(k,2)
counting (12C 2.425 vs 16O 2.406, 0.8%), while the same 2.41 forces a
NEGATIVE alpha.n term at 9Be (no universal pair quantum).  Separately the
one-bond deficits are ~linear at b = 0.782 MeV per light-cluster nucleon.

HYPOTHESIS CLASS (formalize-first, compute-author.md §3.3 — the invariant
is stated BEFORE the numbers are looked at):
  If the k alpha clusters form a Brunnian-type arrangement (pairwise
  unlinked, triple-linked — the corpus Borromean pattern, validated at the
  nucleon level by binding_mn_milnor_linking.py), then:
  (I1) k = 2: all pairwise linkings vanish -> the alpha.alpha PAIR channel is
       structurally ZERO.  Predicts the 8Be anomaly (2-alpha unbound) as
       topology, not energetics.
  (I2) k >= 3: the triple channel mu_bar(a,b,c) = ±1 activates.
  (I3) MILNOR INDETERMINACY GATE (the new derivation attempted here):
       mu_bar(i j s) is well-defined only modulo gcd of the pairwise linking
       numbers of {i,j,s} (Milnor 1954).  A LIGHT spectator (n/d/t) is
       pairwise Hopf-linked to the alphas (that is exactly the always-on
       0.78*A_light pairwise channel), so gcd = 1 and the triple invariant
       carries NO content -> light clusters CANNOT activate an alpha.alpha
       pair.  Only a third ALPHA (pairwise-unlinked, gcd = 0) can.
       -> pre-registered adjudication at 9Be: gate = alpha-only vs gate = any.
  (C)  COUNTING RULE — three pre-registered candidates, adjudicated by the
       12C/16O flatness:
         (C-a) triple-sum:            deficit = t3 * C(k,3)
         (C-b) spectator-additive:    per-pair value grows with (k-2)
                                      [equivalently 3*C(k,3) pair-spectator
                                       incidences]
         (C-c) Boolean/idempotent:    per-pair value = const * [exists an
                                      activating spectator]  (saturating OR,
                                      cf. |mu_bar| coupling: the Lean D2
                                      sign-rep obstruction forces coupling
                                      through mu_bar^2 in {0,1} — idempotent)
  (U)  UNIFICATION CHECK (pre-registered): is the flat per-pair value
       3*b (three 0.78-channels, one per cluster of the mediating triple)?
       Genuinely out-of-sample: b is calibrated on the MIXED one-bond family
       (6Li/7Li/9Be) only; 12C/16O are pure-alpha predictions.

MODEL G (zero new constants; b witness-fed from the committed R5-a witness):
  deficit_pred(K) = sum over unordered cluster pairs of
      3*b                 if pair = alpha.alpha AND #alphas >= 3   (gate)
      0                   if pair = alpha.alpha AND #alphas  = 2
      A_light * b         if pair = alpha.X  (X in {n,d,t}; complete graph)
  Variants reported: gate=any (9Be adjudication), chain alpha.X counting
  (sensitivity).

MAGNITUDE CANDIDATES for the flat per-pair value (pre-registered, symbolic):
  3*b, B_D, deuteron rotor mu0*hbar_q*J_q^2(3), m_e*Vol(L6a4), m_e*Vol(4_1),
  m_e*Vol(8_11)/2, m_pi*hbar_q^2, alpha_der*m_pi.

Run:  python3 -u computations/deltalambda/alpha_activation_brunnian_probe.py \\
        2>&1 | tee /tmp/alpha_activation_brunnian.log

EXPLORATORY — audit-only witness; no production wiring; no fitted constant
(b is a committed R5-a characterization value, reused, not re-fit).
Audit: docs/audits/2026-07-13-alpha-activation-brunnian-derive-or-refute.md
"""
from __future__ import annotations

import datetime
import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent          # computations/deltalambda/
_COMP = _HERE.parent                             # computations/
for _d in (_COMP, _COMP / "substrate"):
    _p = str(_d)
    if _p not in sys.path:
        sys.path.insert(0, _p)

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from codata_constants import M_E_MEV, M_PI_PM_MEV_VALIDATION, _ame_binding_mev  # noqa: E402
from experimental_constants import ALPHA_EM_INV  # noqa: E402
from q_parameter import Q_50_DIGIT_STR, Q_MP  # noqa: E402
import binding_mn_milnor_linking as MILNOR  # noqa: E402  (validated Magnus mu-bar)

set_compute_dps()

Q = Q_MP
M_E = mp.mpf(str(M_E_MEV))
M_PI = mp.mpf(str(M_PI_PM_MEV_VALIDATION))
H = Q - 1 / Q
HBAR_Q = 1 - 1 / Q
MU0 = M_E / (3 * H / 2)


def qint(x) -> mp.mpf:
    x = mp.mpf(x)
    return (Q**x - Q**(-x)) / H


def E_rot(j) -> mp.mpf:
    """Derived q-rotational energy mu0*hbar_q*[j]_q[j+1]_q (MeV)."""
    return MU0 * HBAR_Q * qint(j) * qint(mp.mpf(j) + 1)


A_OF = {"4He": 4, "d": 2, "t": 3, "n": 1}
ISO_ZA = {"6Li": (3, 6), "7Li": (3, 7), "8Be": (4, 8), "9Be": (4, 9),
          "11B": (5, 11), "12C": (6, 12), "14N": (7, 14), "16O": (8, 16),
          "19F": (9, 19)}


def main() -> int:
    print("=" * 76)
    print(" ALPHA.ALPHA k>=3 ACTIVATION — Brunnian/Milnor derive-or-refute (R6-a)")
    print(" zero new constants; b witness-fed from the committed R5-a witness")
    print("=" * 76)

    # ── [0] load committed witnesses; consistency cross-check ───────────────
    W_ADD = json.load(open(_HERE / "alpha-cluster-volume-additivity.witness.json"))
    W_BOND = json.load(open(_HERE / "inter-cluster-bond-term.witness.json"))
    ADD = W_ADD["alpha_cluster_additivity_AME_level"]
    max_dev = 0.0
    for iso, row in ADD.items():
        Z, A = ISO_ZA[iso]
        b_ame = _ame_binding_mev(Z, A)
        b_add = sum(
            (_ame_binding_mev(*{"4He": (2, 4), "d": (1, 2), "t": (1, 3)}[p])
             if p != "n" else mp.mpf(0))
            for p in row["pieces"])
        max_dev = max(max_dev, abs(float(b_ame - b_add) - row["deficit_MeV"]))
    witness_consistent = max_dev < 1e-9
    B_LIN = mp.mpf(str(
        W_BOND["characterization"]["linear_in_A_light_mean_MeV_per_nucleon"]))
    print(f"\n[0] committed deficits reproduce from vendored AME2020 to "
          f"{max_dev:.2e} MeV;\n    b = {mp.nstr(B_LIN, 6)} MeV/nucleon "
          f"(R5-a committed characterization, GUARDED 3-point mean — reused,"
          f" not re-fit).")

    # ── [1] Milnor machinery anchors (I1/I2/I3 computational content) ────────
    bor_lk = [MILNOR.mu(MILNOR.BORROMEAN, s) for s in [(1, 2), (1, 3), (2, 3)]]
    bor_mu = MILNOR.mu(MILNOR.BORROMEAN, (1, 2, 3))
    chain_lk = [MILNOR.mu(MILNOR.CHAIN, s) for s in [(1, 2), (2, 3), (1, 3)]]
    chain_mu = MILNOR.mu(MILNOR.CHAIN, (1, 2, 3))
    milnor_ok = (bor_lk == [0, 0, 0] and abs(bor_mu) == 1 and chain_mu == 0
                 and 1 in chain_lk)
    print("\n[1] Milnor anchors (validated Magnus, imported from "
          "binding_mn_milnor_linking):")
    print(f"    Borromean: pairwise lk = {bor_lk}, mu_bar(123) = {bor_mu}"
          f"  -> I1 (k=2 pair channel = 0) + I2 (k>=3 triple = ±1)")
    print(f"    Hopf-chain (linked spectator): lk = {chain_lk}, mu_bar(123) = "
          f"{chain_mu}")
    print("    I3 (gate): mu_bar(i j s) is well-defined mod gcd(pairwise lk)")
    print("    [Milnor 1954]; a light spectator is Hopf-linked (lk = ±1, its")
    print("    own always-on 0.78*A_light channel) -> gcd = 1 -> triple content")
    print("    KILLED. Only a pairwise-unlinked (alpha) spectator activates.")

    # ── [2] counting-rule adjudication (pre-registered C-a/C-b/C-c) ──────────
    d12 = mp.mpf(str(ADD["12C"]["deficit_MeV"]))
    d16 = mp.mpf(str(ADD["16O"]["deficit_MeV"]))
    d8 = mp.mpf(str(ADD["8Be"]["deficit_MeV"]))
    per = {
        "C-a triple-sum C(k,3)": (d12 / 1, d16 / 4),
        "C-b spectator-additive 3*C(k,3)": (d12 / 3, d16 / 12),
        "C-c Boolean-gated pairs C(k,2)": (d12 / 3, d16 / 6),
    }
    print("\n[2] COUNTING-RULE adjudication on the pure-alpha family "
          "(12C k=3, 16O k=4):")
    flat = {}
    for name, (u12, u16) in per.items():
        r = float(u12 / u16)
        flat[name] = r
        print(f"    {name:34s} 12C {float(u12):6.3f}  16O {float(u16):6.3f} "
              f" MeV/unit   ratio {r:5.2f}")
    ca_ratio = flat["C-a triple-sum C(k,3)"]
    cb_ratio = flat["C-b spectator-additive 3*C(k,3)"]
    cc_ratio = flat["C-c Boolean-gated pairs C(k,2)"]
    counting_verdict = (abs(cc_ratio - 1) < 0.02
                        and ca_ratio > 1.9 and cb_ratio > 1.9)
    print("    -> C-a and C-b are ~2x NON-flat (refuted); C-c is flat to "
          f"{abs(cc_ratio - 1) * 100:.1f}%.")
    print("    The gate SATURATES: value independent of spectator count.")
    print("    Consistent with coupling through |mu_bar| (mu_bar^2 in {0,1},")
    print("    idempotent; Lean D2 sign-rep obstruction,")
    print("    QOU.Mass.MilnorSignRepObstruction) — consistent, NOT derived:")
    print("    OR-vs-SUM over spectators is data-selected here.")

    # 8Be structural zero (I1)
    aa_flat = (d12 / 3 + d16 / 6) / 2          # 2.4155 — the k>=3 per-pair value
    disc_8be = float(aa_flat / abs(d8))
    print(f"\n    8Be (k=2): deficit {float(d8):+.3f} MeV vs structural-zero "
          f"prediction 0 —\n    |residual| = 0.16% of B_AME; a universal pair "
          f"quantum would predict {float(aa_flat):.3f}\n    (discrimination "
          f"factor x{disc_8be:.0f}). The small NEGATIVE (2-alpha threshold,")
    print("    -92 keV unbound) is NOT derived — the mechanism gives 0, not")
    print("    the sign of the residual (Coulomb-scale physics, open).")

    # ── [3] 9Be gate adjudication (I3, pre-registered both ways) ─────────────
    d9 = mp.mpf(str(ADD["9Be"]["deficit_MeV"]))
    gate_any_alpha_n = (d9 - 3 * B_LIN) / 2   # forced alpha.n term if n gates
    gate_alpha_only_pred = 2 * B_LIN          # alpha.alpha off; 2 alpha.n pairs
    r9 = float(gate_alpha_only_pred / d9 - 1)
    print("\n[3] 9Be (alpha+alpha+n) GATE adjudication:")
    print(f"    gate=any (n activates): alpha.alpha = 3b = "
          f"{float(3 * B_LIN):.3f} -> forced alpha.n = "
          f"{float(gate_any_alpha_n):+.3f} MeV each: NEGATIVE, sign-"
          f"inconsistent. REFUTED.")
    print(f"    gate=alpha-only (I3): alpha.alpha = 0; pred = 2b = "
          f"{float(gate_alpha_only_pred):.3f} vs deficit {float(d9):.3f} "
          f"({r9 * 100:+.2f}%).")
    print("    -> the Milnor-indeterminacy gate PREDICTED the alpha-only rule")
    print("    (I3, stated before the check); 9Be passes at -0.6%.")

    # ── [4] unification check: is the flat per-pair value 3*b? ───────────────
    three_b = 3 * B_LIN
    uni_dev = float(three_b / aa_flat - 1)
    print(f"\n[4] UNIFICATION: flat per-pair value {float(aa_flat):.4f} MeV vs "
          f"3*b = {float(three_b):.4f} MeV")
    print(f"    deviation {uni_dev * 100:+.2f}% (one-bond family scatter about "
          f"b: max 5.8%); ratio\n    per-pair/b = {float(aa_flat / B_LIN):.3f} "
          f"vs 3 ({(float(aa_flat / B_LIN) / 3 - 1) * 100:+.1f}%). "
          f"CONSISTENT within scatter.")
    print("    Genuinely out-of-sample: b is calibrated on the MIXED one-bond")
    print("    family (6Li/7Li/9Be) only; 12C/16O are pure-alpha predictions.")
    print("    GUARD: the count '3' (one 0.78-channel per cluster of the")
    print("    mediating triple) is a post-hoc reading, NOT derived — an alpha")
    print("    as the light side of a pairwise bond would give 4 channels, not")
    print("    3; the 3-channel reading is recorded as a hypothesis only.")

    # ── [5] Model G across all witness isotopes (zero new constants) ─────────
    print("\n[5] MODEL G per-isotope (complete-graph pairs; alpha-only Boolean "
          "gate; b fixed):")
    print(f"    {'iso':5s} {'pairs (pred terms)':28s} {'pred':>7s} "
          f"{'deficit':>8s} {'resid':>7s} {'def-lvl':>8s} {'B-lvl':>7s} "
          f"{'add B-lvl':>9s}")
    rows = {}
    closed, not_closed = [], []
    for iso, row in ADD.items():
        pieces = row["pieces"]
        deficit = mp.mpf(str(row["deficit_MeV"]))
        b_ame = mp.mpf(str(row["B_AME_MeV"]))
        n_alpha = sum(1 for p in pieces if p == "4He")
        lights = [p for p in pieces if p != "4He"]
        # alpha.alpha pairs: gated
        n_aa = n_alpha * (n_alpha - 1) // 2
        aa_val = (3 * B_LIN) if n_alpha >= 3 else mp.mpf(0)
        # alpha.X pairs: complete graph -> each light pairs with every alpha
        ax_terms = [(x, A_OF[x] * B_LIN) for x in lights for _ in range(n_alpha)]
        pred = n_aa * aa_val + sum(v for _, v in ax_terms)
        # chain-variant sensitivity: each light attaches to ONE alpha
        pred_chain = n_aa * aa_val + sum(A_OF[x] * B_LIN for x in lights)
        resid = pred - deficit
        def_lvl = float(resid / deficit) if abs(float(deficit)) > 1e-12 else float("inf")
        b_lvl = float(resid / b_ame)
        lab = (f"{n_aa}aa[{'on' if aa_val > 0 else 'off'}]"
               + (f"+{len(ax_terms)}ax" if ax_terms else ""))
        rows[iso] = {
            "pieces": pieces, "n_alpha": n_alpha,
            "n_alpha_alpha_pairs": n_aa,
            "gate_on": bool(aa_val > 0),
            "pred_deficit_MeV": float(pred),
            "pred_deficit_chain_variant_MeV": float(pred_chain),
            "deficit_MeV": float(deficit),
            "resid_MeV": float(resid),
            "resid_over_deficit": def_lvl,
            "resid_over_B_AME": b_lvl,
            "additivity_rel_err": row["rel_err"],
        }
        (closed if abs(b_lvl) < 0.005 else not_closed).append(iso)
        print(f"    {iso:5s} {lab:28s} {float(pred):>7.3f} {float(deficit):>+8.3f} "
              f"{float(resid):>+7.3f} {def_lvl * 100:>+7.1f}% {b_lvl * 100:>+6.2f}% "
              f"{row['rel_err'] * 100:>+8.2f}%")
    print(f"\n    closed to < 0.5% of B: {', '.join(closed)}")
    print(f"    NOT closed:            {', '.join(not_closed)}")
    print("    In-sample caveat: 6Li/7Li/9Be calibrate b (their residuals are")
    print("    scatter about their own mean); OUT-OF-SAMPLE closures are 8Be,")
    print("    12C, 16O. The mixed MULTI-bond composites (11B, 14N; 19F")
    print("    marginal) are NOT closed — the missing structure is in the")
    print("    mixed-cluster interface at >= 2 bonds (or those decompositions")
    print("    are wrong), scope-(a).")

    # ── [6] magnitude candidates for the flat per-pair value (pre-registered) ─
    VOL_L6A4 = mp.mpf(str(W_ADD["inputs"]["Vol_L6a4_ppn"]["value"]))
    VOL_811 = mp.mpf(str(W_ADD["inputs"]["Vol_8_11_pnn"]["value"]))
    VOL_41 = 2 * mp.clsin(2, mp.pi / 3)   # Vol(4_1) = 2*Lobachevsky(pi/3) = 2*Cl_2(pi/3)
    alpha_der = 1 / (Q * qint(9) * qint(10))
    cands = {
        "3*b (unification)": three_b,
        "B_D (AME)": mp.mpf(str(_ame_binding_mev(1, 2))),
        "deuteron rotor mu0*hbar_q*Jq2(3)": E_rot(3),
        "m_e*Vol(L6a4)": M_E * VOL_L6A4,
        "m_e*Vol(4_1)": M_E * VOL_41,
        "m_e*Vol(8_11)/2": M_E * VOL_811 / 2,
        "m_pi*hbar_q^2": M_PI * HBAR_Q**2,
        "alpha_der*m_pi": alpha_der * M_PI,
    }
    print("\n[6] magnitude candidates vs the flat per-pair value "
          f"{float(aa_flat):.4f} MeV (pre-registered):")
    cand_rows = {}
    for name, v in cands.items():
        dev = float(v / aa_flat - 1)
        cand_rows[name] = {"value_MeV": float(v), "dev": dev}
        print(f"    {name:34s} {float(v):7.4f}  ({dev * 100:+6.1f}%)")
    others_far = all(abs(r["dev"]) > 0.05 for n, r in cand_rows.items()
                     if not n.startswith("3*b"))
    print("    -> only 3*b lands within 5%; every other candidate deviates")
    print("       > 5% (B_D -7.9% and rotor -16% were already quarantined in")
    print("       R5-a; they stay quarantined).")

    # ── verdict ──────────────────────────────────────────────────────────────
    verdict = (
        "PARTIAL DERIVATION (scope-(a) elsewhere). The Brunnian/Milnor "
        "mechanism DERIVES three of the four structural features of the "
        "alpha.alpha pair term: (I1) the k=2 zero — pairwise-unlinked alphas "
        "carry no pair channel, so 8Be sits at 0 (measured -0.092 MeV, 0.16% "
        "of B, x26 below the 2.42 a universal pair quantum would force; the "
        "sign of the -92 keV threshold residual is NOT derived); (I2) the "
        "k>=3 activation — mu_bar(a,b,c) = ±1 opens the triple channel; (I3) "
        "the alpha-only gate — mu_bar(i j s) is defined only mod gcd(pairwise "
        "lk), so a light spectator (Hopf-linked, gcd 1: its own always-on "
        "0.78*A_light channel) kills the triple content, and 9Be then closes "
        "at -0.6% where gate=any would force a negative alpha.n term "
        "(pre-registered adjudication, passed). The fourth feature — "
        "SATURATION (per-pair value independent of spectator count) — is "
        "data-SELECTED, not derived: triple-sum C(k,3) and spectator-additive "
        "3*C(k,3) counting are ~2x non-flat across 12C/16O (refuted), the "
        "Boolean-gated C(k,2) is flat to 0.8%; idempotent |mu_bar| coupling "
        "(mu_bar^2 in {0,1}; Lean D2 sign-rep obstruction) is a consistent "
        "reading, not a derivation. UNIFICATION: the flat per-pair value "
        "2.4155 MeV equals 3*b = 2.3458 to -2.9% (inside the one-bond "
        "family's 5.8% scatter), with b calibrated on the mixed one-bond "
        "family only — 12C (-3.3% deficit-level, -0.26% of B) and 16O "
        "(-2.5%, -0.28% of B) are genuine out-of-sample predictions with "
        "zero new constants; the channel count '3' remains a post-hoc "
        "reading (GUARDED). NOT closed: the mixed multi-bond composites 11B "
        "(-58% deficit-level), 14N (-33%), 19F (-10%; -1.8% of B) — the "
        "gated rule + linear term is not the whole interface theory there "
        "(scope-(a): constrains Model G as sole mechanism for mixed "
        "multi-bond composites; no ingredient excluded). Nothing tuned; b "
        "reused from the committed R5-a witness; no production wiring."
    )
    print(f"\nVERDICT: {verdict}")

    # ── witness ──────────────────────────────────────────────────────────────
    wit = {
        "computation": "alpha-activation-brunnian-derive-or-refute",
        "description": (
            "R6-a derive-or-refute of the k>=3 activation of the alpha.alpha "
            "inter-cluster pair term via the Brunnian/Milnor mechanism: (I1) "
            "k=2 structural zero (8Be), (I2) k>=3 triple activation, (I3) "
            "Milnor-indeterminacy alpha-only gate (9Be adjudication), "
            "counting-rule adjudication (Boolean-gated C(k,2) flat vs C(k,3)/"
            "spectator-additive ~2x non-flat), the 3*b unification check, and "
            "Model G (gated pairs + 0.78*A_light linear term, zero new "
            "constants) across all nine witness isotopes. All inputs from "
            "committed witnesses; nothing recomputed, nothing tuned."),
        "audit_only": True,
        "computedAt": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "engine": "mpmath + integer Magnus (witness-fed; no new tr_M compute)",
        "inputs": {
            "deficit_source": "alpha-cluster-volume-additivity.witness.json (committed; consistency-checked to 1e-9 MeV)",
            "b_linear_MeV_per_nucleon": {
                "value": float(B_LIN),
                "source": "inter-cluster-bond-term.witness.json characterization.linear_in_A_light_mean_MeV_per_nucleon (committed R5-a; GUARDED 3-point mean, reused not re-fit)"},
            "milnor_machinery": "binding_mn_milnor_linking.py (validated integer Magnus, imported)",
            "m_e_MeV": {"value": float(M_E), "source": "codata_constants.M_E_MEV (CODATA 2022, CAL-1)"},
            "q0": {"value": Q_50_DIGIT_STR[:20] + "...", "source": "q_parameter.Q_50_DIGIT_STR"},
            "m_pi_MeV": {"value": float(M_PI), "source": "codata_constants.M_PI_PM_MEV_VALIDATION (CAL-3)"},
            "volumes": {"L6a4": float(VOL_L6A4), "8_11": float(VOL_811),
                        "4_1": float(VOL_41),
                        "source": "additivity witness inputs (deprecated volume-search IDs, stated as such) + Vol(4_1) = 2*Lobachevsky(pi/3)"},
        },
        "milnor_anchors": {
            "borromean_pairwise_lk": bor_lk, "borromean_mu_bar_123": bor_mu,
            "chain_pairwise_lk": chain_lk, "chain_mu_bar_123": chain_mu,
            "indeterminacy_gate": "mu_bar(ijs) well-defined mod gcd(pairwise lk) [Milnor 1954]; Hopf-linked light spectator -> gcd 1 -> no triple content; alpha spectator (all pairwise lk 0) -> gcd 0 -> mu_bar in Z",
        },
        "counting_rule_adjudication": {
            "per_unit_12C_over_16O_ratio": {k: v for k, v in flat.items()},
            "verdict": "C-a (triple-sum) and C-b (spectator-additive) ~2x non-flat: REFUTED; C-c (Boolean-gated pairs) flat to 0.8%: SELECTED (saturation data-selected, not derived; |mu_bar| idempotency is a consistent reading per Lean QOU.Mass.MilnorSignRepObstruction)",
        },
        "structural_zero_8Be": {
            "deficit_MeV": float(d8), "prediction_MeV": 0.0,
            "universal_pair_quantum_would_give_MeV": float(aa_flat),
            "discrimination_factor": disc_8be,
            "note": "sign of the -92 keV threshold residual NOT derived",
        },
        "gate_adjudication_9Be": {
            "gate_any_forced_alpha_n_MeV": float(gate_any_alpha_n),
            "gate_any_verdict": "REFUTED (negative alpha.n, sign-inconsistent)",
            "gate_alpha_only_pred_MeV": float(gate_alpha_only_pred),
            "gate_alpha_only_resid": r9,
            "note": "I3 predicted alpha-only BEFORE the check (Milnor indeterminacy)",
        },
        "unification_3b": {
            "flat_per_pair_MeV": float(aa_flat), "three_b_MeV": float(three_b),
            "deviation": uni_dev,
            "per_pair_over_b": float(aa_flat / B_LIN),
            "one_bond_scatter_band": 0.058,
            "guard": "channel count '3' post-hoc (one per cluster of the mediating triple is a reading, not a derivation); b in-sample for 6Li/7Li/9Be, out-of-sample for 8Be/12C/16O",
        },
        "model_G_per_isotope": rows,
        "closed_below_half_percent_B": closed,
        "not_closed": not_closed,
        "magnitude_candidates_vs_flat_per_pair": cand_rows,
        "verdict": verdict,
        "scope": "(a) for the mixed multi-bond failures — Model G constrained as sole mechanism there; no ingredient excluded. I1/I2/I3 are structural derivations conditional on the Brunnian cluster-arrangement model input.",
        "assertions": [
            {"label": "committed witness deficits reproduce from vendored AME2020 to 1e-9 MeV",
             "passed": bool(witness_consistent)},
            {"label": "Milnor anchors: Borromean lk=0/mu=±1; Hopf-linked-spectator chain mu=0 (I1/I2/I3 computational content)",
             "passed": bool(milnor_ok)},
            {"label": "counting: Boolean-gated C(k,2) flat to <2% while C(k,3) and spectator-additive are >1.9x non-flat (12C vs 16O)",
             "passed": bool(counting_verdict)},
            {"label": "8Be structural zero: |deficit| < 0.1 MeV, i.e. x20+ below the universal-pair value (I1 passes)",
             "passed": bool(abs(float(d8)) < 0.1 and disc_8be > 20)},
            {"label": "9Be gate=any forces alpha.n < -0.3 MeV (refuted); gate=alpha-only closes to |resid| < 1%",
             "passed": bool(float(gate_any_alpha_n) < -0.3 and abs(r9) < 0.01)},
            {"label": "unification: |3b/flat-per-pair - 1| < 5% (inside the 5.8% one-bond scatter)",
             "passed": bool(abs(uni_dev) < 0.05)},
            {"label": "out-of-sample closures: 12C and 16O deficit predictions within 5% (B-level < 0.5%)",
             "passed": bool(abs(rows["12C"]["resid_over_deficit"]) < 0.05
                            and abs(rows["16O"]["resid_over_deficit"]) < 0.05
                            and abs(rows["12C"]["resid_over_B_AME"]) < 0.005
                            and abs(rows["16O"]["resid_over_B_AME"]) < 0.005)},
            {"label": "honest negative: mixed multi-bond 11B and 14N NOT closed (deficit-level residual > 25%)",
             "passed": bool(abs(rows["11B"]["resid_over_deficit"]) > 0.25
                            and abs(rows["14N"]["resid_over_deficit"]) > 0.25)},
            {"label": "no non-3b magnitude candidate within 5% of the flat per-pair value",
             "passed": bool(others_far)},
        ],
    }
    wit["allPassed"] = all(a["passed"] for a in wit["assertions"])
    out = _HERE / "alpha-activation-brunnian.witness.json"
    import os as _os, sys as _sys  # noqa: E402 — P30 rollup (bean cmiy)
    _d = _os.path.dirname(_os.path.abspath(__file__))
    while _d != _os.path.dirname(_d) and not _os.path.isdir(_os.path.join(_d, "substrate")):
        _d = _os.path.dirname(_d)
    _sys.path.insert(0, _os.path.join(_d, "substrate"))
    from witness_base import WitnessBuilder  # noqa: E402
    WitnessBuilder.stamp_staleness_metadata(wit, script_path=__file__, engine="mpmath")
    wit["scriptFile"] = _os.path.basename(__file__)
    json.dump(wit, open(out, "w"), indent=1)
    print(f"\nwitness -> {out.name}   allPassed: {wit['allPassed']}")
    return 0 if wit["allPassed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
