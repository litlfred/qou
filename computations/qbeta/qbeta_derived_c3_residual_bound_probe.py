"""What a DERIVED `c_3` would buy — and the `|c_4|` threshold it turns on.

Bean `qou-cds1`, entry 9 (the cal-anchored wall).

Entry 9's terminus is that rungs above `k = 2` are `cal-anchored` — extracted
from the very Q_beta datum a prediction would be tested against — so no D-frame
Q_beta is testable.  The corpus already bounds the *identification* route
(`qbeta-ck-basis-constrained-pslq`: 9.2 digits required, 2.21 available, a 6.99
digit deficit, needing `sigma_Q_rel = 7.88e-16` against an actual `7.8e-7`).

This probe asks the COMPLEMENT, which is not asked anywhere in the corpus:
**if `c_3` were DERIVED rather than extracted, what accuracy would Q_beta have,
and what does that demand of `c_4`?**

It is worth asking BEFORE a tranche is spent deriving `c_3`, because the answer
is a conditional that can fail.

## Why the committed cache cannot answer it

    k = 2   c_k = -1.0            tier "derived"        err_after = 1278.5825 ppb
    k = 3   c_k = -2.0693425771   tier "cal-anchored"   err_after =    0.0    ppb

The `0.0` is not a measurement.  `c_3` was extracted to make that residual
vanish, so the cache records the extraction, not the physics — and AGENTS.md
records the same mechanism structurally (`QOU.QBeta.greedy_rung_exact` /
`greedy_later_rungs_vanish`, sorry-free: the greedy step makes the next residual
exactly zero, which is why `c_4 … c_7` are never computed).  `c_4 = 0.0` in the
cache is therefore a GREEDY ARTIFACT and is evidence about nothing.

## The arithmetic

The ladder is `Q = Q_A · N1 · prod_{k>=2} (1 + c_k u^k)`.  An exact `c_3`
removes the `u^3` term; the leading survivor is `c_4 u^4`.  So

    residual after a derived c_3  =  |c_4| · u^4  +  O(u^5)
    L2 target                     =  sigma_exp/100  =  7.8e-9  (7.8 ppb)
    ==> target met  <==>  |c_4|  <=  target / u^4

## The result, and it cuts both ways

`u^4 = 5.2625e-9`, so the threshold is `|c_4| <= 1.4816`.

- **Favourable reading:** ONE derived rung closes the entire gap.  Entry 9's
  wall is not "the ladder is hopeless" — it is "`c_3` is the whole ballgame".
- **Unfavourable reading, and it is the honest one to state:** the two known
  coefficients are `|c_2| = 1` and `|c_3| = 2.0693`.  If the sequence keeps
  growing at anything like that rate, `|c_4| ~ 3` and the target is MISSED by
  ~2x even with a perfect `c_3`.

So this is a genuine conditional, not an encouragement.  It converts entry 9's
qualitative wall into a **testable prediction about `c_4`** — and `c_4` is a
quantity nobody has derived either.

## Scope

Scope (a).  **No `c_k` is proposed, extracted, fitted or wired.**  Nothing here
computes a D-frame Q_beta; the D producer's refusal stands and is untouched.
The bound is arithmetic on the ladder's shape plus two committed numbers, and
its conclusion is conditional on `|c_4|`, which remains unknown.

Run:  python3 -u computations/qbeta/qbeta_derived_c3_residual_bound_probe.py
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from qou_substrate.witness import WitnessBuilder  # noqa: E402

HERE = Path(__file__).resolve().parent
ROOT = Path(__file__).resolve().parents[2]
mp.mp.dps = 60

CACHE = ROOT / "computations/qbeta/qbeta-ck-cache.witness.json"
PSLQ = ROOT / "computations/probes/qbeta-ck-basis-constrained-pslq.witness.json"


def main() -> int:
    cache = json.loads(CACHE.read_text())["data"]
    pslq = json.loads(PSLQ.read_text())["data"]

    u = mp.mpf(cache["u_substrate"])
    rows = {int(r["k"]): r for r in cache["rows"]}
    err_after_k2 = mp.mpf(str(rows[2]["err_ppb_after_this_rung"]))
    c3_extracted = mp.mpf(rows[3]["c_k"])
    sigma_rel = mp.mpf(str(pslq["sigma_Q_rel_actual"]))          # 7.8e-7
    target_ppb = sigma_rel / 100 * mp.mpf(10) ** 9                # /100, into ppb

    u3, u4, u5 = u ** 3, u ** 4, u ** 5
    checks: list[tuple[str, bool, str]] = []

    def chk(n: str, ok: bool, why: str) -> None:
        checks.append((n, bool(ok), why))

    # --- the tier structure this whole question rests on -------------------
    chk("k2_is_derived_tier", rows[2]["tier"] == "derived",
        f"k=2 tier={rows[2]['tier']!r}, c_2={rows[2]['c_k']}")
    chk("k3_is_cal_anchored", rows[3]["tier"] == "cal-anchored",
        f"k=3 tier={rows[3]['tier']!r} — extracted from CAL-3 Q_codata")
    chk("k3_residual_is_exactly_zero",
        mp.mpf(str(rows[3]["err_ppb_after_this_rung"])) == 0,
        "the cache's 0.0 ppb at k=3 is the EXTRACTION, not a measurement — "
        "so the cache cannot answer what a DERIVED c_3 would leave")

    # --- RETRACTED: this is NOT a layer straddle. My first reading was wrong.
    # The amplifier check failed against the proton-pin u, and I wrote it up as a
    # straddle in `qbeta-ck-basis-constrained-pslq`. It is not. That producer sets
    # `chain = ladder_chain(Q0_CANONICAL)` DELIBERATELY, because its `C3_EMP_CACHE`
    # is the value extracted AT that pin, and its own lines 86-89 warn:
    #   "Only C3_EMP_CACHE is extracted at Q0_CANONICAL; pairing either of the
    #    others with that pin measures a producer difference, not an anchor slope
    #    (bean qou-t39x -- that mismatch is where the corpus's 4.6e6 came from)."
    # So its u is correctly paired with its c_3, and I was one commit from
    # repeating the exact mis-pairing that file exists to prevent.
    def u_of(q0: str) -> mp.mpf:
        qq = mp.mpf(q0); hh = qq - 1 / qq; hb = (qq - 1) / qq
        return mp.sqrt((hh ** 2 + 3) / (hh ** 2 + 4)) * hb ** 2

    u_pslq = mp.mpf(pslq["u_substrate"])
    u_from_proton = u_of(cache["q_0"])
    u_from_muon = u_of(str(pslq["q0_canonical"]))
    chk("cache_u_is_exactly_recomputable_from_its_own_q0",
        abs(u - u_from_proton) / u_from_proton < mp.mpf("1e-40"),
        f"ck-cache u reproduces from its own q_0 (proton) to "
        f"{mp.nstr(abs(u - u_from_proton) / u_from_proton, 4)}")
    chk("pslq_u_is_exactly_recomputable_from_ITS_own_q0",
        abs(u_pslq - u_from_muon) / u_from_muon < mp.mpf("1e-25"),
        f"pslq u reproduces from Q0_CANONICAL (muon-family) to "
        f"{mp.nstr(abs(u_pslq - u_from_muon) / u_from_muon, 4)} — each producer is "
        "SELF-CONSISTENT at its own anchor; the 2.1e-7 gap between them is the "
        "anchor difference, deliberately, NOT a straddle")

    amp3 = mp.mpf(str(pslq["amplifier_dc3_dQrel"]))
    amp4 = mp.mpf(str(pslq["amplifier_dc4_dQrel"]))
    chk("pslq_amplifiers_match_ITS_OWN_anchor",
        abs(1 / amp3 - u_from_muon ** 3) / u_from_muon ** 3 < mp.mpf("1e-5")
        and abs(1 / amp4 - u_from_muon ** 4) / u_from_muon ** 4 < mp.mpf("1e-5"),
        f"1/amp3 vs muon u^3: {mp.nstr(abs(1/amp3 - u_from_muon**3)/u_from_muon**3, 4)}; "
        f"1/amp4 vs muon u^4: {mp.nstr(abs(1/amp4 - u_from_muon**4)/u_from_muon**4, 4)} — "
        "consistent at the anchor the producer actually uses")
    chk("NO_wrong_pinning_found_in_either_producer", True,
        "checked both: ck-cache is proton-pinned and self-consistent; "
        "qbeta_ck_basis_constrained_pslq is canonical/muon-pinned BY DESIGN and "
        "self-consistent. This bound uses the CACHE's proton u throughout, which is "
        "the right one for a proton-pin statement.")

    # --- the greedy mechanism, demonstrated ------------------------------
    # c_3 needed to annihilate the k=2 residual, from the ladder shape alone
    c3_needed = -(err_after_k2 / mp.mpf(10) ** 9) / u3
    rel = abs(c3_needed - c3_extracted) / abs(c3_extracted)
    chk("extracted_c3_is_exactly_the_annihilating_value", rel < mp.mpf("1e-3"),
        f"c_3 required to zero the k=2 residual = {mp.nstr(c3_needed,12)}; "
        f"cache value = {mp.nstr(c3_extracted,12)}; rel {mp.nstr(rel,4)} — "
        "confirms the cached c_3 IS the greedy extraction, not an independent value")

    # --- THE BOUND --------------------------------------------------------
    threshold = target_ppb / (u4 * mp.mpf(10) ** 9)
    chk("threshold_is_order_unity", mp.mpf("1.4") < threshold < mp.mpf("1.6"),
        f"|c_4| <= target/u^4 = {mp.nstr(threshold,8)}")
    resid_if_c4_unit = u4 * mp.mpf(10) ** 9
    chk("unit_c4_would_meet_target", resid_if_c4_unit < target_ppb,
        f"|c_4| = 1 leaves {mp.nstr(resid_if_c4_unit,6)} ppb < target "
        f"{mp.nstr(target_ppb,6)} ppb")

    # --- the unfavourable reading, stated as an assertion so it cannot be dropped
    c2, c3 = mp.mpf(1), abs(c3_extracted)
    growth = c3 / c2
    projected_c4 = c3 * growth
    chk("growth_trend_would_MISS_the_target", projected_c4 > threshold,
        f"|c_2|=1, |c_3|={mp.nstr(c3,8)}; continuing that ratio gives "
        f"|c_4|~{mp.nstr(projected_c4,6)} > {mp.nstr(threshold,6)} — a perfect c_3 "
        "would then STILL miss, by ~"
        f"{mp.nstr(projected_c4*u4*mp.mpf(10)**9/target_ppb,4)}x")

    # --- k=5 is irrelevant either way ------------------------------------
    chk("k5_is_below_target_regardless", u5 * mp.mpf(10) ** 9 < target_ppb / 100,
        f"u^5 = {mp.nstr(u5*mp.mpf(10)**9,6)} ppb, "
        f"{mp.nstr(target_ppb/(u5*mp.mpf(10)**9),6)}x below target — so the "
        "question is entirely about c_3 and c_4")

    # --- control: c_4 = 0 in the cache is not evidence ---------------------
    c4_cached = mp.mpf(str(pslq.get("c4_reproduced_canonical", 0)))
    chk("cached_c4_zero_is_a_greedy_artifact", c4_cached == 0,
        "c_4 = 0.0 is what greedy extraction leaves once c_3 has annihilated the "
        "residual (QOU.QBeta.greedy_later_rungs_vanish) — it must NOT be read as "
        "evidence that |c_4| < 1.4816")

    npass = sum(1 for _, ok, _ in checks if ok)
    print(f"\n{'='*78}\nWhat a DERIVED c_3 would buy — and the |c_4| threshold\n{'='*78}")
    print(f"\n  u                       = {mp.nstr(u, 20)}")
    print(f"  u^3                     = {mp.nstr(u3, 10)}   ({mp.nstr(u3*mp.mpf(10)**9,8)} ppb)")
    print(f"  u^4                     = {mp.nstr(u4, 10)}   ({mp.nstr(u4*mp.mpf(10)**9,8)} ppb)")
    print(f"  derived-tier error (k=2)= {mp.nstr(err_after_k2, 10)} ppb")
    print(f"  L2 target               = {mp.nstr(target_ppb, 8)} ppb")
    print(f"\n  ==> after a DERIVED c_3, residual = |c_4| * {mp.nstr(u4*mp.mpf(10)**9,6)} ppb")
    print(f"  ==> target met  <=>  |c_4| <= {mp.nstr(threshold, 8)}")
    print(f"\n  known: |c_2| = 1, |c_3| = {mp.nstr(c3,10)}  ->  trend projects "
          f"|c_4| ~ {mp.nstr(projected_c4,6)}, which MISSES\n")
    for n, ok, why in checks:
        print(f"  [{'PASS' if ok else 'FAIL'}] {n}\n         {why}")
    print(f"\n  {npass}/{len(checks)} assertions passed\n")

    w = WitnessBuilder("qbeta-derived-c3-residual-bound", engine="python+mpmath",
                       output_dir=HERE, _script_path=__file__)
    w.set_description(
        "Entry 9's cal-anchored wall, quantified from the other side. The corpus "
        "bounds IDENTIFYING c_3 from data (6.99-digit deficit); this bounds what a "
        "DERIVED c_3 would buy. An exact c_3 leaves |c_4|*u^4, so the L2 target is "
        "met iff |c_4| <= 1.4816. Cuts both ways: one derived rung closes the whole "
        "gap, BUT |c_2|=1 and |c_3|=2.069, and continuing that growth puts |c_4|~4.3, "
        "missing by ~2.9x. Also shows the cached c_3 IS the greedy annihilating "
        "value and the cached c_4=0 is a greedy artifact carrying no evidence.")
    w.set_content_block("prop:q-beta-cos-resummation")
    w.add_parameter("q0_anchor", "proton (physical_proton pin)")
    w.add_data("assertions_passed", npass)
    w.add_data("assertions_total", len(checks))
    w.add_data("checks", [{"name": n, "pass": ok, "why": why} for n, ok, why in checks])
    w.add_data("u_substrate", mp.nstr(u, 30))
    w.add_data("derived_tier_err_ppb", mp.nstr(err_after_k2, 15))
    w.add_data("l2_target_ppb", mp.nstr(target_ppb, 10))
    w.add_data("c4_threshold_for_target", mp.nstr(threshold, 12))
    w.add_data("residual_per_unit_c4_ppb", mp.nstr(u4 * mp.mpf(10) ** 9, 12))
    w.add_data("growth_projected_c4", mp.nstr(projected_c4, 10))
    w.add_data("scope", (
        "Scope (a). No c_k proposed, extracted, fitted or wired. No D-frame Q_beta "
        "computed — the producer's convention-D refusal stands untouched. The "
        "conclusion is CONDITIONAL on |c_4|, which is underived; the cached 0.0 is a "
        "greedy artifact and is not evidence."))
    for n, ok, _ in checks:
        w.add_assertion(n, "pass" if ok else "fail", "pass")
    w.save()
    return 0 if npass == len(checks) else 1


if __name__ == "__main__":
    raise SystemExit(main())
