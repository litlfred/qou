#!/usr/bin/env python3
"""(binding, Q_β) Askey–Wilson three-term recurrence probe — ONE bar-even multiplier?

Numerical counterpart of the Lean theorem `recurrence_invol_descent`
(`qou:QOU.MassEndomorphism` in
content/quantum-observable-universe/mass-endomorphism/binding-qbeta-complex-volume.lean):
IF the complex ladder 𝔙_A satisfies ONE three-term recurrence
𝔙_{A+1} = c·𝔙_A − 𝔙_{A−1} with a BAR-EVEN multiplier c (σc = c), THEN the
bar-even (binding) and bar-odd (𝔔_β) ladders each satisfy the SAME recurrence.
This probe tests the numerical converse-signature: solve the multiplier from
each channel separately along neutron-addition isotope chains and ask whether
the three answers agree (and whether the complex multiplier is real).

    B(q)   = E₀ · ln( tr_M(W_free; q) / tr_M(W_atom; q) )        (predecessor form)
    B_even = ½[B(q₀)+B(q₀⁻¹)]   (bar-even / cosh / binding channel)
    B_odd  = ½[B(q₀)−B(q₀⁻¹)]   (bar-odd  / sinh / 𝔔_β channel)
    𝔙_A    = B_even(A) + i·B_odd(A)                              (complex ladder)
    L(A)   = ln[tr_atom(q₀⁻¹)/tr_atom(q₀)] / ln q₀               (log-trace ladder)

For each consecutive triple (A−1, A, A+1) the recurrence X_{A+1} = c·X_A − X_{A−1}
gives c = (X_{A+1} + X_{A−1}) / X_A, solved separately on the even, odd, and
complex ladders. DECIDABLE OUTPUTS (no fit — solve-and-compare):
  (a) relative gap |c_even − c_odd| (shared multiplier ⇒ should vanish);
  (b) |Im c_complex| / |c_complex|  (bar-even multiplier ⇒ should vanish);
  (c) raw multipliers vs the reference 2·cosh(10·η₀) (η₀ = ln q₀; the b-ladder
      multiplier of docs/audits/2026-06-29-delta-lambda-imme-askey.md §"The
      Askey connection") and vs 2·cosh(6.68·η₀) (the ≈6.68-per-neutron
      log-trace increment of the predecessor probe), plus the implied
      k = arccosh(c/2)/η₀ per channel.

Data: canonical binding transfer path (`binding_canonical` fast path =
`tr_m_atom_zn`) at q₀ AND q₀⁻¹; on the known main regression
(`chi_monotone_transfer.word_to_mpfr: unrecognised crossing`) falls back to the
committed predecessor witness `computations/binding-bar-even-odd-probe.witness.json`.

Discipline: mpmath 65-dps compute / 50-dps serialization; NO FIT (measure-and-
compare); verdict TIERED with (a)/(b) scope per AGENTS.md. Audit-only.
Predecessor: docs/audits/2026-06-30-complex-volume-bar-parity-binding-probe.md.
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))  # computations/ — flat-namespace bridge
import _path_bridge  # noqa: F401, E402

import json  # noqa: E402
import mpmath as mp  # noqa: E402

from q_parameter import Q as Q0  # noqa: E402 — canonical q₀ source (same as predecessor)
from codata_constants import M_E_MEV as _ME  # noqa: E402
from experimental_constants import Q_NEUTRON_MEV  # noqa: E402

COMPUTE_DPS = 65   # compute precision (compute-author discipline)
OUT_DPS = 50       # serialization precision (significant digits, as strings)

# Base tower (always) + extension (feasibility-gated, ~10 min budget)
ISOTOPES_BASE = [("2H", 1, 1), ("3H", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
ISOTOPES_EXT = [("6Li", 3, 3), ("7Li", 3, 4)]
TIME_BUDGET_SEC = 480.0  # leave headroom under ~10 min

# Neutron-addition chains (consecutive triples A−1 → A → A+1)
CHAINS = {
    "chain1_2H-3H-4He": ["2H", "3H", "4He"],
    "chain2_2H-3He-4He": ["2H", "3He", "4He"],
}

FALLBACK_WITNESS = _HERE.parent / "binding-bar-even-odd-probe.witness.json"


def s(x) -> str:
    """Serialize an mpf/mpc to OUT_DPS significant digits as a string."""
    return mp.nstr(x, OUT_DPS)


def acquire(q0: mp.mpf, qi: mp.mpf, E0: mp.mpf):
    """Return (rows, data_source, traces_available, errors).

    rows: {iso: {"B_q0", "B_qinv", and optionally "tr_atom_q0", "tr_atom_qinv"}}
    Tries the canonical binding path first; falls back to the committed
    predecessor witness on the known main regression.
    """
    errors: list[str] = []
    t_start = time.time()
    try:
        # Smoke-test the canonical binding path itself (the known regression
        # `chi_monotone_transfer.word_to_mpfr: unrecognised crossing` fires here).
        from binding_canonical import binding_canonical
        smoke = binding_canonical(1, 1)
        print(f"  binding_canonical smoke test (2H): status={smoke['status']} "
              f"B={smoke['B_MeV']:.6f} MeV — canonical path OK")

        from tr_m_atom_via_transfer import tr_m_atom_zn

        rows: dict[str, dict] = {}
        for name, Z, N in ISOTOPES_BASE:
            t0 = time.time()
            ta0, tf0, _, _ = tr_m_atom_zn(Z, N, q=q0, dps=COMPUTE_DPS)
            tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=COMPUTE_DPS)
            ta0, tf0, tai, tfi = (mp.mpf(str(x)) for x in (ta0, tf0, tai, tfi))
            rows[name] = {
                "B_q0": E0 * mp.log(tf0 / ta0),
                "B_qinv": E0 * mp.log(tfi / tai),
                "tr_atom_q0": ta0, "tr_atom_qinv": tai,
                "tr_free_q0": tf0, "tr_free_qinv": tfi,
            }
            print(f"  [{name}] recomputed both anchors in {time.time()-t0:.2f}s "
                  f"(elapsed {time.time()-t_start:.1f}s)")

        # Extension isotopes under the time budget (supplementary ladder values;
        # no consecutive-A triple is formable from {4He, 6Li, 7Li} alone).
        for name, Z, N in ISOTOPES_EXT:
            if time.time() - t_start > TIME_BUDGET_SEC:
                errors.append(f"skipped {name}: time budget "
                              f"({TIME_BUDGET_SEC:.0f}s) exhausted")
                print(f"  [{name}] SKIPPED — time budget exhausted")
                continue
            try:
                t0 = time.time()
                ta0, tf0, _, _ = tr_m_atom_zn(Z, N, q=q0, dps=COMPUTE_DPS)
                tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi, dps=COMPUTE_DPS)
                ta0, tf0, tai, tfi = (mp.mpf(str(x)) for x in (ta0, tf0, tai, tfi))
                rows[name] = {
                    "B_q0": E0 * mp.log(tf0 / ta0),
                    "B_qinv": E0 * mp.log(tfi / tai),
                    "tr_atom_q0": ta0, "tr_atom_qinv": tai,
                    "tr_free_q0": tf0, "tr_free_qinv": tfi,
                }
                print(f"  [{name}] recomputed both anchors in "
                      f"{time.time()-t0:.2f}s (elapsed {time.time()-t_start:.1f}s)")
            except Exception as e:  # extension is best-effort
                errors.append(f"{name} extension failed: {type(e).__name__}: {e}")
                print(f"  [{name}] extension FAILED: {e}")
        return rows, ("recomputed via canonical binding path "
                      "(binding_canonical fast path = tr_m_atom_zn) at q0 and "
                      "q0^-1"), True, errors
    except Exception as e:
        errors.append(f"canonical binding path raised: {type(e).__name__}: {e}")
        print(f"  canonical binding path RAISED ({type(e).__name__}: {e}) — "
              f"falling back to committed witness")
        with open(FALLBACK_WITNESS, "r", encoding="utf-8") as f:
            w = json.load(f)
        rows = {}
        for name, _, _ in ISOTOPES_BASE:
            iso = w["isotopes"][name]
            rows[name] = {
                "B_q0": mp.mpf(iso["B_q0_MeV"]),
                "B_qinv": mp.mpf(iso["B_qinv_MeV"]),
                # no raw trace values in the committed witness → no L ladder
            }
        return rows, "committed witness (binding_canonical regression)", False, errors


def main() -> int:
    mp.mp.dps = COMPUTE_DPS
    q0 = mp.mpf(str(Q0))
    qi = mp.mpf(1) / q0
    eta0 = mp.log(q0)
    E0 = mp.mpf(str(_ME)) / (q0 * (q0 - 1))

    print("\n  (binding, Q_β) ASKEY–WILSON THREE-TERM RECURRENCE PROBE")
    print(f"  Lean counterpart: recurrence_invol_descent "
          f"(binding-qbeta-complex-volume.lean)")
    print(f"  q0 = {mp.nstr(q0, 12)}  eta0 = ln q0 = {mp.nstr(eta0, 12)}  "
          f"E0 = {mp.nstr(E0, 8)} MeV  (dps={mp.mp.dps})\n")

    rows, data_source, traces_available, errors = acquire(q0, qi, E0)
    print(f"\n  data_source: {data_source}\n")

    # ── Ladders ──────────────────────────────────────────────────────────
    ladders: dict[str, dict] = {}
    print("| iso | B(q0) | B(q0^-1) | B_even | B_odd | L(A) |")
    print("|---|--:|--:|--:|--:|--:|")
    for name, r in rows.items():
        B0, Bi = r["B_q0"], r["B_qinv"]
        Be = (B0 + Bi) / 2
        Bo = (B0 - Bi) / 2
        entry = {"B_q0_MeV": B0, "B_qinv_MeV": Bi,
                 "B_even_MeV": Be, "B_odd_MeV": Bo,
                 "V_complex": mp.mpc(Be, Bo)}
        L_str = "n/a"
        if traces_available:
            L = mp.log(r["tr_atom_qinv"] / r["tr_atom_q0"]) / eta0
            entry["L_logtrace"] = L
            L_str = mp.nstr(L, 8)
        ladders[name] = entry
        print(f"| {name} | {mp.nstr(B0, 8)} | {mp.nstr(Bi, 8)} | "
              f"{mp.nstr(Be, 8)} | {mp.nstr(Bo, 8)} | {L_str} |")

    # ── Reference multipliers ────────────────────────────────────────────
    ref_10 = 2 * mp.cosh(10 * eta0)       # b-ladder reference (imme-askey audit)
    ref_668 = 2 * mp.cosh(mp.mpf("6.68") * eta0)  # per-neutron log-trace slope
    print(f"\n  references: 2·cosh(10·eta0) = {mp.nstr(ref_10, 10)}   "
          f"2·cosh(6.68·eta0) = {mp.nstr(ref_668, 10)}\n")

    def implied_k(c):
        """k such that c = 2·cosh(k·eta0); complex when |c| < 2."""
        return mp.acosh(mp.mpc(c) / 2) / eta0

    # ── Per-chain multipliers ────────────────────────────────────────────
    chains_out: dict[str, dict] = {}
    gaps_a, gaps_b = [], []
    for cname, (m, k, p) in ((cn, tuple(members)) for cn, members in CHAINS.items()):
        Lm, Lk, Lp = ladders[m], ladders[k], ladders[p]
        c_even = (Lp["B_even_MeV"] + Lm["B_even_MeV"]) / Lk["B_even_MeV"]
        c_odd = (Lp["B_odd_MeV"] + Lm["B_odd_MeV"]) / Lk["B_odd_MeV"]
        c_cx = (Lp["V_complex"] + Lm["V_complex"]) / Lk["V_complex"]
        rel_gap = abs(c_even - c_odd) / ((abs(c_even) + abs(c_odd)) / 2)
        im_frac = abs(mp.im(c_cx)) / abs(c_cx)
        gaps_a.append(rel_gap)
        gaps_b.append(im_frac)
        out = {
            "members": [m, k, p],
            "c_even": s(c_even),
            "c_odd": s(c_odd),
            "c_complex_re": s(mp.re(c_cx)),
            "c_complex_im": s(mp.im(c_cx)),
            "decidable_a_rel_gap_even_vs_odd": s(rel_gap),
            "decidable_b_im_frac_c_complex": s(im_frac),
            "vs_reference": {
                "c_even_over_2cosh10eta0": s(c_even / ref_10),
                "c_odd_over_2cosh10eta0": s(c_odd / ref_10),
                "c_even_over_2cosh668eta0": s(c_even / ref_668),
                "c_odd_over_2cosh668eta0": s(c_odd / ref_668),
                "implied_k_even": s(implied_k(c_even)),
                "implied_k_odd": s(implied_k(c_odd)),
            },
        }
        if traces_available and all("L_logtrace" in x for x in (Lm, Lk, Lp)):
            c_L = (Lp["L_logtrace"] + Lm["L_logtrace"]) / Lk["L_logtrace"]
            out["c_logtrace"] = s(c_L)
            out["vs_reference"]["implied_k_logtrace"] = s(implied_k(c_L))
        chains_out[cname] = out
        print(f"  [{cname}] {m} → {k} → {p}")
        print(f"    c_even    = {mp.nstr(c_even, 12)}")
        print(f"    c_odd     = {mp.nstr(c_odd, 12)}")
        print(f"    c_complex = {mp.nstr(c_cx, 12)}")
        print(f"    (a) |c_even−c_odd| rel gap = {mp.nstr(rel_gap, 8)}")
        print(f"    (b) |Im c_complex|/|c_complex| = {mp.nstr(im_frac, 8)}")
        if "c_logtrace" in out:
            print(f"    c_logtrace = {out['c_logtrace'][:16]}…")
        print()

    # Supplementary: per-neutron log-trace increments (the ≈6.68 tell), if fresh
    L_increments = {}
    if traces_available:
        for (a, b) in (("2H", "3H"), ("3He", "4He"), ("6Li", "7Li")):
            if a in ladders and b in ladders and "L_logtrace" in ladders[a] \
                    and "L_logtrace" in ladders[b]:
                dL = ladders[b]["L_logtrace"] - ladders[a]["L_logtrace"]
                L_increments[f"{a}->{b}"] = s(dL)
                print(f"  ΔL({a}→{b}) = {mp.nstr(dL, 8)} (one neutron added)")

    # ── Tiered verdict (thresholds; no fit) ──────────────────────────────
    max_a = max(gaps_a)
    max_b = max(gaps_b)
    TOL_MATCH = mp.mpf("1e-6")   # shared-multiplier claim would need this
    TOL_NEAR = mp.mpf("0.03")    # near-match band (cf. c_3 cross-anchor 3%)
    if max_a < TOL_MATCH and max_b < TOL_MATCH:
        tier = "near-match (numerically shared bar-even multiplier at these isotopes; not proved)"
        verdict = (
            "NEAR-MATCH: the even and odd channel ladders yield the same "
            "three-term multiplier and the complex multiplier is real to "
            f"{s(max(max_a, max_b))} — numerically consistent with ONE "
            "bar-even Askey–Wilson multiplier per recurrence_invol_descent. "
            "Not proved; not wired."
        )
    elif max_a < TOL_NEAR and max_b < TOL_NEAR:
        tier = "near-match (percent-level)"
        verdict = (
            f"NEAR-MATCH at percent level: max even/odd multiplier gap {s(max_a)}, "
            f"max |Im c|/|c| {s(max_b)} — suggestive of a shared bar-even "
            "multiplier with sub-percent corrections. Not proved; not wired."
        )
    else:
        tier = "refuted, scope (a) — scope-limited negative"
        verdict = (
            "REFUTED, SCOPE (a) (scope-limited negative per AGENTS.md): at the "
            "isotope triples (2H,3H,4He) and (2H,3He,4He), with the log-trace "
            "binding proxy B(q) = E0·ln(tr_free/tr_atom) and the ½[B(q0)±B(q0^-1)] "
            "parity split, the (binding, Q_beta) channel ladders do NOT share one "
            f"Askey–Wilson three-term multiplier: max relative even/odd gap = "
            f"{s(max_a)} and max |Im c_complex|/|c_complex| = {s(max_b)}, both far "
            "from zero. This ladder, ALONE, at these isotopes and in this proxy "
            "form, does not realize the recurrence_invol_descent hypothesis "
            "(one recurrence, bar-even multiplier). NOT a structural exclusion: "
            "the Lean theorem is conditional (IF one bar-even-multiplier "
            "recurrence THEN both channels inherit it) and remains valid; the "
            "negative constrains this particular ladder construction (parity "
            "split of the log-trace proxy along A), not the ingredient — a "
            "different normalization, ladder variable (e.g. the c_k Habiro "
            "ladder), or corrected binding proxy is not excluded."
        )
    print(f"\n  TIER: {tier}")
    print(f"  VERDICT: {verdict}\n")

    # ── Witness ──────────────────────────────────────────────────────────
    ladders_ser = {}
    for name, e in ladders.items():
        d = {
            "B_q0_MeV": s(e["B_q0_MeV"]), "B_qinv_MeV": s(e["B_qinv_MeV"]),
            "B_even_MeV": s(e["B_even_MeV"]), "B_odd_MeV": s(e["B_odd_MeV"]),
            "V_complex_re_MeV": s(mp.re(e["V_complex"])),
            "V_complex_im_MeV": s(mp.im(e["V_complex"])),
        }
        if "L_logtrace" in e:
            d["L_logtrace"] = s(e["L_logtrace"])
        ladders_ser[name] = d

    witness = {
        "description": (
            "Askey–Wilson three-term recurrence probe on the (binding, Q_beta) "
            "channel ladders: solve the multiplier c = (X(A+1)+X(A-1))/X(A) "
            "separately on the bar-even, bar-odd, and complex ladders along "
            "neutron-addition chains and test for ONE shared bar-even multiplier "
            "— the numerical counterpart of the Lean recurrence_invol_descent."
        ),
        "discipline": (
            "no fit — solve-and-compare; mpmath 65-dps compute / 50-dps "
            "serialization (strings); tiered verdict with (a)/(b) scope per "
            "AGENTS.md"
        ),
        "audit_only": True,
        "lean_counterpart": (
            "qou:QOU.MassEndomorphism.recurrence_invol_descent + "
            "AWDeformationPath.channel_ladders "
            "(content/quantum-observable-universe/mass-endomorphism/"
            "binding-qbeta-complex-volume.lean)"
        ),
        "predecessor": "docs/audits/2026-06-30-complex-volume-bar-parity-binding-probe.md",
        "data_source": data_source,
        "traces_available": traces_available,
        "acquisition_errors": errors,
        "precision": {"compute_dps": COMPUTE_DPS, "output_sig_digits": OUT_DPS},
        "constants": {
            "q_0": s(q0), "q_inv": s(qi), "eta_0": s(eta0), "E0_MeV": s(E0),
            "Q_beta_codata_MeV": str(float(Q_NEUTRON_MEV)),
            "ref_2cosh_10eta0": s(2 * mp.cosh(10 * eta0)),
            "ref_2cosh_668eta0": s(2 * mp.cosh(mp.mpf("6.68") * eta0)),
        },
        "results": {
            "ladders": ladders_ser,
            "chains": chains_out,
            "log_trace_per_neutron_increments": L_increments,
            "decidable_outputs": {
                "a_max_rel_gap_even_vs_odd": s(max_a),
                "b_max_im_frac_c_complex": s(max_b),
                "c_reference_comparison": "per-chain vs_reference blocks",
            },
        },
        "tier": tier,
        "verdict": verdict,
    }
    from witness_base import WitnessBuilder  # noqa: E402
    out = WitnessBuilder.wrap_legacy(
        "binding-qbeta-aw-recurrence-probe", witness,
        script_path=__file__, engine="mpmath",
    ).save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
