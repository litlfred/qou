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

`u^4 = 5.2625281e-9`, so the threshold is `|c_4| <= 1.4821774`.

- **Favourable reading:** ONE derived rung closes the entire gap.  Entry 9's
  wall is not "the ladder is hopeless" — it is "`c_3` is the whole ballgame".
- **Unfavourable reading, and it is the honest one to state:** the two known
  coefficients are `|c_2| = 1` and `|c_3| = 2.0693426`.  Continuing that ratio
  puts `|c_4| ~ 4.28218`, which MISSES the threshold by ~2.889x even with a
  perfect `c_3`.

So this is a genuine conditional, not an encouragement.  It converts entry 9's
qualitative wall into a **testable prediction about `c_4`**.

CORRECTED 2026-08-31.  This docstring read `1.4816`, `|c_4| ~ 3` and `~2x`
against the `1.4821774`, `4.28218` and `2.889x` this same file computes and
prints.  Every figure quoted in prose here is now the one the code derives; do
not re-introduce a literal.  The `1.4816` traced to a draft `u^4 = 5.2646e-9`
and was never the value any run produced.

## Does `c_4` have to be unknown?  (open, and NOT what this probe assumed)

The "growth trend" reading above is a *heuristic on two data points* and it is
the weakest thing in this file.  The corpus holds an **exact closed form** for
a `c_4`-family object — `qbeta-c4even-exact-sseries.witness.json`:

    c_2^even = -887/144 - 3*sqrt(3)/4              = -7.45876032789888...
    c_3^even = 733/72 + 15997*sqrt(3)/405          = 78.5944241201958...
    c_4^even = -425625605/290304 - 2864831*sqrt(3)/25920
                                                   = -1657.57403579524...

**ANSWERED, and the answer is NO — it constrains nothing.  Do not chase it.**
This section first proposed measuring the `c_k^even` <-> `c_k` normalisation and
suggested `|c_4^even| = 1657.6` might decide entry 9 outright.  The corpus had
already refuted that route and I had not read it.  Two independent reasons,
both on record before I looked:

1. **Structural.**  `u = b*hbar_q^2` is QUADRATIC in `t = q-1` near `q = 1`, so
   the `u`-reversion is singular and `R(q)` is **not analytic in `u`** — the
   `c_k` are not scalar-`q` Taylor coefficients at all.  The verdict of
   `docs/audits/2026-06-16-hoefsmit-stage-b-attempt-verdict.md` is that "exact
   operator-level `c_4..c_8` as constants do not exist".  That is why
   `qbeta_ck_sseries_operator_match_probe`'s `c2_gate` is red ON PURPOSE and
   its content block's `status` is pinned `"failed"`: the red assertion IS the
   finding, and relaxing it would delete a recorded refutation.

2. **Numerical, and measured rather than argued.**  The extraction obeys
   `sigma(c_k) = sigma_R / u^k`, so it AMPLIFIES input error: `1/u^2 ~ 1.4e4`
   at `k = 2` and `1/u^4 ~ 1.9e8` at `k = 4`.  Measured instance recorded in
   `content/.../mass-endomorphism/binding-qbeta-complex-volume.ts`: a **9.8e-8**
   relative change in `free-neutron-decay.witness.json` (regenerated in
   52c68267f2) moved `c_2^even` by **6.8 %** — ~7e5 amplification — with a
   BYTE-IDENTICAL producer.  Import-cone drift, invisible to a file-local diff.

So the exact ℚ(√3) form is not evidence of an identified constant.  The
previous value `c_2^even = -8.006410058709255` had its OWN exact form,
`-1049/144 - 5*sqrt(3)/12`, matching to **fifteen digits** — and that block
records it as the noise of a 7e5-amplifying extraction, caught one commit
before being written down as an identification.  A 15-digit coincidence is
exactly what this estimator's noise looks like.

**Therefore the growth heuristic above stands as the honest statement**: `|c_4|`
is unknown, the `1 -> 2.07 -> ?` extrapolation is two data points and is
labelled as such, and the `^even` sequence is NOT a sharper substitute for it.
Recorded so the next reader does not re-walk this — I found an exact-looking
closed form, assumed it was informative, and had to be corrected by a content
block written for exactly that purpose (bean qou-cds1, entry 16).

## Scope

Scope (a).  **No `c_k` is proposed, extracted, fitted or wired.**  Nothing here
computes a D-frame Q_beta; the D producer's refusal stands and is untouched.

**Convention scope — read this before quoting the threshold under D.**  The two
halves of this probe scope differently and must not be quoted together:

- `|c_4| <= target / u^4 = 1.4821774` is **convention-independent**.  `u =
  b*hbar_q^2` is a function of `q_0` alone and contains no Markov parameter, so
  neither `z_C` nor `z_D` enters it.  What it DOES assume is that the D-frame
  ladder, once re-derived, still has the graded product form
  `prod_{k>=2} (1 + c_k u^k)` in this same `u`.  qou-cds1 is explicit that the
  D ladder must be RE-DERIVED rather than re-evaluated, so that form is an
  assumption, not a given — if the re-derivation lands on a different expansion
  parameter, the threshold is about a different `c_4`.
- "One derived rung closes the entire gap" is **C-frame**.  It rests on the
  1278.5825 ppb k=2 residual, which comes from the committed C-frame cache
  (`c_2 = -1` folded against the N=1 cosine at `alpha_C`).  Under D the N=1
  factor is a bar-midpoint rather than a bar-invariant cosine (entry 10), so
  the k=2 residual is simply not known yet and this sentence does not transfer.

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
        f"evidence that |c_4| < {mp.nstr(threshold, 8)}")

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
        f"met iff |c_4| <= {mp.nstr(threshold, 8)}. Cuts both ways: one derived rung "
        f"closes the whole gap, BUT |c_2|=1 and |c_3|={mp.nstr(c3, 10)}, and continuing "
        f"that growth puts |c_4|~{mp.nstr(projected_c4, 6)}, missing by "
        f"~{mp.nstr(projected_c4/threshold, 4)}x. Also shows the cached c_3 IS the "
        "greedy annihilating value and the cached c_4=0 is a greedy artifact carrying "
        "no evidence. THRESHOLD IS CONVENTION-INDEPENDENT (u has no Markov parameter) "
        "but assumes the re-derived D ladder keeps the same u-graded product form; the "
        "'one rung closes it' reading is C-frame, resting on the C-cache k=2 residual. "
        "The c_k^even exact rungs do NOT sharpen the |c_4| question: the c_k are not "
        "scalar-q Taylor coefficients (u is quadratic in q-1, so the u-reversion is "
        "singular) and the extraction amplifies input error by sigma_R/u^k, measured "
        "at ~7e5 for k=2 -- a 15-digit 'exact' match there was noise.")
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
