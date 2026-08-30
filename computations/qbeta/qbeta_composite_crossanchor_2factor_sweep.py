#!/usr/bin/env python3
"""qbeta_composite_crossanchor_2factor_sweep.py
===============================================

Systematic 2-factor COMPOSITE sweep for the Q_β c_3 f-map, discriminated
by **cross-anchor agreement** (proton AND muon).

## Motivation

The single-formula search for the c_3 residue-A categorical ID is
SATURATED (28 NEGATIVE candidates across four chains; see
`docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md` and
`docs/coordination/1ppq-qbeta.md`). The saturated-search outcome points
at COMPOSITE operators. An existing first-test
(`qbeta_composite_operator_first_test.py`) hand-picked 6 two-factor
products and checked them at the **proton anchor only**.

This probe strengthens that in two ways:

1. **Systematic, not hand-picked.** It sweeps *every* 2-factor
   combination `a ∘ b`, `∘ ∈ {×, ÷, +, −}`, over a curated set of ~20
   categorical atoms (quantum integers, Markov traces, Demazure / SYT /
   J_Hopf characters, Kashaev q-Pochhammers, Hoefsmit b, block
   eigenvalues, …). This SATURATES the natural 2-factor composite space,
   superseding the 6-product first-test.

2. **Cross-anchor discrimination (the rigorous criterion).** The
   CAL-anchored c_3 target is computed at BOTH the proton-pinned q₀ and
   the muon cross-check anchor via the ladder inversion
   `c_3(q) = (Q_codata / Q_N2(q) − 1) / u(q)³` (Q_codata is the
   anchor-independent experimental Q-value). The two targets differ by a
   clean swing:

       c_3_target(proton) ≈ −2.069343
       c_3_target(muon)   ≈ −2.020200
       swing              ≈  0.049142   (~2.4 %)

   A genuine f-map closure must reproduce the target at BOTH anchors —
   i.e. track the 0.049 swing. A candidate that matches the proton target
   but not the muon target is a single-anchor NEAR-MATCH (a coincidence),
   exactly the failure mode the 1ppQ ledger rejects. This makes the
   sweep a real structural test, not a one-anchor curve-fit.

## Verdict logic (per candidate)

    proton_miss = |f(q_p) − c3_target(q_p)| / |c3_target(q_p)|
    muon_miss   = |f(q_m) − c3_target(q_m)| / |c3_target(q_m)|

    CLOSURE     : proton_miss < TOL_CLOSURE  AND  muon_miss < TOL_CLOSURE
    NEAR-MATCH  : proton_miss < TOL_NEAR     AND  muon_miss ≥ TOL_CLOSURE
    NEGATIVE    : otherwise

`TOL_CLOSURE = 1e-6` (1 ppm at both anchors — a structural match), and
`TOL_NEAR = 1e-2` (1 % at the proton anchor — flags coincidences for the
record). No fitting, no tuning — every atom is a closed-form categorical
quantity; the sweep only combines them.

## Honest expectation

Per the saturated single-formula bracket, the LIKELY outcome is NEGATIVE
(no 2-factor composite lands within 1 ppm at both anchors). That is a
VALUABLE result: it saturates the 2-factor space too, narrowing the open
keystone to 3+-factor / infinite-product (Habiro-ring) / KLR-crystal
structures (Composites 1–4 of the KLR/crystal infra scope). A CLOSURE,
if found, identifies the residue-A f-map element and justifies the
upstream Lean infrastructure investment.

## CORRECTION 2026-08-24 (bean qou-y82a) — this probe ran with both legs
## on the muon anchor until today

Every run of this producer before 2026-08-24 was measured against the WRONG
target. The stem was listed under `ideal_muon` in
`computations/q0_anchor_manifest.json`, which makes `q_parameter` override
`q_at()` to the muon anchor. Both legs of a cross-anchor probe then sat on
the muon anchor:

    q_at()      1.1099785955573347   (muon, via the manifest override)
    q_muon_at() 1.1099785956427390   (muon)
    swing       0.00032782           vs the documented 0.04948227  — 151x low

The committed witness recorded this itself and was committed anyway:
`allPassed: false`, with `c3_target_proton_matches_canonical` computing
-2.0201881 against the canonical -2.0693426, and `cross_anchor_swing_resolvable`
= 0. AGENTS.md names this class verbatim — "A comparison producer needs BOTH
pins and the manifest cannot serve it ... belongs under `physical_proton`" —
with `mu_substrate_tension_audit_100dps` (155x) as the precedent.

Consequence for the recorded near-match set, and it is total rather than
partial. `single_anchor_near_matches` is exactly the swept candidates lying
within TOL_NEAR = 1% of the target, so it is a function of where the target
sits. Moving the target 2.4% — from the muon -2.0201881 to the proton
-2.0693426 — moves a window of half-width 1% clean off its old position:

    muon-pinned window   [-2.0403900, -1.9999862]
    proton-pinned window [-2.0900360, -2.0486491]

These are DISJOINT, so the two near-match sets share ZERO members: all 27
muon-pinned entries leave and 4 entirely new ones arrive. The candidates
themselves barely moved (q_at shifts by 1.2e-8 relative); what moved was the
window. So the 27 -> 4 change is NOT evidence about any candidate — it is a
corrected measurement, and the bean that recorded it as "21 of 25 did not
survive" understated it in both directions (the count was 27, not 25 — the
witness list was truncated at 25 — and the survivor count is 0, not 4).

What the 27 were, structurally: the "c_3 ~ -2" neighbourhood. Under the muon
target -2.0201881 the constant `-2` itself misses by 9.99e-3, i.e. it sits
JUST inside the 1% window, and so does everything clustered around it — hence
27 hits dominated by the atoms `-2`, `J_Hopf(q)` (~ -4.055, and J_Hopf(1) = -2)
and the near-`-2` q-Pochhammer differences. Under the correct proton target
`-2` misses by 3.351e-2, which is the c_3-normalised form of the 3.47% gap
AGENTS.md records for `c_3 = -2 = J_Hopf(q=1)`. The old set was therefore
re-reporting one already-known fact 27 times over, against a target mis-set
so that the fact fell inside the tolerance.

SCOPE (per AGENTS.md "Before declaring refuted/ruled out"): scope-(a),
scope-limited negative — "no 2-factor composite of these atoms reproduces the
c_3 target at both anchors within 1 ppm". NOT scope-(b): no proved invariant
excludes any of these ingredients from a closure, and in particular the 27
departures are a window artifact and say nothing at all about their
candidates. The overall NEGATIVE_2FACTOR_SATURATED verdict is unchanged and is
now, for the first time, actually tested — under the collapsed swing the
cross-anchor criterion had no power to separate a closure from a
single-anchor coincidence.

References:
    docs/coordination/1ppq-qbeta.md
    docs/audits/2026-06-03-qbeta-residue-a-cal-anchored-acceptance.md
    qbeta_ck_cache.py (c_3 ladder-inversion method)
    qbeta_composite_operator_first_test.py (the 6-product proton-only first-test)
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE.parent))

import _path_bridge as _bridge  # noqa: E402, F401

from mpmath import mp, mpf, sqrt, cos, fabs, isnan, isinf  # noqa: E402

from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import q_at, q_muon_at  # noqa: E402
from codata_constants import M_E_MEV, Q_BETA_MEV  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

from qbeta_utils import c3_target_at, substrate_ladder_quantities  # noqa: E402

# Precision must be raised BEFORE the module-scope constants below: at
# import time mp.dps is still mpmath's default 15 (~binary64), and a
# literal rounded there cannot be recovered by raising dps afterwards.
# Idempotent. Gate: mpf_import_time_dps_audit.py (bean qou-j6gb).
set_compute_dps()

TOL_CLOSURE = mpf("1e-6")   # 1 ppm at BOTH anchors → structural closure
TOL_NEAR = mpf("1e-2")      # 1 % at proton → flag as a near-match


# ── Categorical atoms (closed-form functions of the substrate q) ──

def quantum_int(n: int, q: mpf) -> mpf:
    """[n]_q = (qⁿ − q⁻ⁿ)/(q − q⁻¹)."""
    return (q ** n - q ** (-n)) / (q - q ** (-1))


def q_pochhammer(q: mpf, n: int) -> mpf:
    """(q; q)_n = Π_{k=1}^{n} (1 − qᵏ)."""
    out = mpf(1)
    for k in range(1, n + 1):
        out *= (1 - q ** k)
    return out


def j_hopf_kauffman(q: mpf) -> mpf:
    """J_Hopf(q) Kauffman: −(q^½+q^−½)(q^{3/2}+q^{−3/2})."""
    return -(q ** mpf("0.5") + q ** mpf("-0.5")) * (
        q ** mpf("1.5") + q ** mpf("-1.5")
    )


def build_atoms(q: mpf) -> dict[str, mpf]:
    """A curated set of categorical building blocks evaluated at `q`.

    Each is a closed-form quantity drawn from the candidate families that
    failed individually (the 28-candidate single-formula bracket) plus the
    structural objects named in the KLR/crystal composite scope.
    """
    sub = substrate_ladder_quantities(q, convention="C")
    h, hbar_q, b, u = sub["h"], sub["hbar_q"], sub["b"], sub["u"]
    atoms: dict[str, mpf] = {
        # quantum integers + Markov traces
        "[2]_q": quantum_int(2, q),
        "[3]_q": quantum_int(3, q),
        "[4]_q": quantum_int(4, q),
        "tr_M(p2)": mpf(-1) ** (2 - 1) / quantum_int(2, q),
        "tr_M(p3)": mpf(-1) ** (3 - 1) / quantum_int(3, q),
        # characters / crystal data
        "Demazure(2,1)": 2 * quantum_int(3, q),
        "SYT_maj(2,1)": q + q ** 2,
        "J_Hopf(q)": j_hopf_kauffman(q),
        # block eigenvalues (negative-exponent powers; key uses Unicode
        # superscript ⁻² / ⁻¹ to avoid being misread as subtraction)
        "q²+q⁻²": q ** 2 + q ** -2,
        "q+q⁻¹": q + q ** -1,
        # Kashaev q-Pochhammers
        "(q;q)_2": q_pochhammer(q, 2),
        "(q;q)_3": q_pochhammer(q, 3),
        "(q;q)_4": q_pochhammer(q, 4),
        # substrate scalars
        "b": b,
        "hbar_q^2": hbar_q ** 2,
        "h^2": h ** 2,
        "u": u,
        "cos_N1": cos(sub["alpha"] - b * hbar_q ** 2 / 2),
        # pure constants that recur in the candidate families
        "-2": mpf(-2),
        "1/2": mpf("0.5"),
        "3": mpf(3),
    }
    return atoms


def sweep_candidates(
    qp: mpf, qm: mpf
) -> dict[str, tuple[mpf, mpf]]:
    """Generate every 2-factor composite a∘b (and the singletons) as a
    name → (value_at_proton, value_at_muon) map.

    Operators: ×, ÷, +, −. Symmetric ops (×, +) include i == j (self-
    composites a × a = a², a + a = 2a) so the sweep is a TRUE saturation
    of the 2-factor space, not just ordered-pair coverage. Asymmetric
    ops (÷, −) skip i == j (a/a = 1, a − a = 0 are vacuous) and run in
    both directions. Singletons are included so the sweep supersets the
    single-formula bracket as well.
    """
    atoms_p = build_atoms(qp)
    atoms_m = build_atoms(qm)
    names = list(atoms_p.keys())

    out: dict[str, tuple[mpf, mpf]] = {}

    # singletons
    for n in names:
        out[n] = (atoms_p[n], atoms_m[n])

    def safe(fn_p, fn_m, label):
        try:
            vp = fn_p()
            vm = fn_m()
            if isnan(vp) or isinf(vp) or isnan(vm) or isinf(vm):
                return
            out[label] = (vp, vm)
        except (ZeroDivisionError, ValueError, ArithmeticError):
            return

    for i, a in enumerate(names):
        for j, bn in enumerate(names):
            ap, am = atoms_p[a], atoms_m[a]
            bp, bm = atoms_p[bn], atoms_m[bn]
            if j >= i:
                # symmetric ops once; j == i adds self-composites a×a, a+a
                safe(lambda: ap * bp, lambda: am * bm, f"{a} × {bn}")
                safe(lambda: ap + bp, lambda: am + bm, f"{a} + {bn}")
            if i != j:
                # asymmetric ops both directions (a/a, a-a are vacuous)
                safe(lambda: ap / bp, lambda: am / bm, f"{a} ÷ {bn}")
                safe(lambda: ap - bp, lambda: am - bm, f"{a} − {bn}")
    return out


def main() -> int:
    set_compute_dps()

    # Construct both anchors via str(...) so the cast is precision-safe
    # regardless of whether the source constant is mpf, str, or float.
    me = mpf(str(M_E_MEV))
    q_codata = mpf(str(Q_BETA_MEV))
    qp = q_at(mp.dps)
    qm = q_muon_at(mp.dps)

    cp = c3_target_at(qp, q_codata, me)
    cm = c3_target_at(qm, q_codata, me)
    swing = fabs(cp - cm)

    # ── Anchor-separation GUARD (bean qou-y82a) ──
    # This is a comparison producer: it needs BOTH pins, and it reads them by
    # name (`q_at` = proton, `q_muon_at` = muon). If the running stem is listed
    # under `ideal_muon` in computations/q0_anchor_manifest.json, q_parameter
    # OVERRIDES q_at() to the muon anchor — and then BOTH legs of this probe
    # sit on the muon anchor, the cross-anchor swing collapses ~151x
    # (0.0495 -> 0.00033), and the whole discriminating power of the test is
    # gone while the output still reads as a cross-anchor result.
    #
    # That is not hypothetical: it is how this producer ran from the day it was
    # written until 2026-08-24. The committed witness carried allPassed=false,
    # with `c3_target_proton_matches_canonical` computing -2.02019 against the
    # canonical -2.06934 — the file said it was wrong and was committed anyway.
    #
    # So REFUSE rather than record. A failing assertion inside a witness is too
    # quiet for a defect that silently rescales the probe's target; a refusal
    # that explains itself on stdout is the discipline AGENTS.md records for
    # `low_isotope_mass_table` and `qbeta_braid_nf_sdp_offset_probe`.
    anchor_sep = fabs(qp - qm) / fabs(qp)
    if anchor_sep < mpf("1e-9"):
        print()
        print("REFUSING TO RUN — the two anchors have collapsed onto one.")
        print(f"  q_at()      = {mp.nstr(qp, 22)}   (should be the PROTON pin)")
        print(f"  q_muon_at() = {mp.nstr(qm, 22)}   (the muon pin)")
        print(f"  relative separation = {mp.nstr(anchor_sep, 6)} < 1e-9")
        print()
        print("  This is a CROSS-ANCHOR probe: with both legs on the same")
        print("  anchor it has no discriminating power, and its 1%-wide")
        print("  near-match window sits around the WRONG c_3 target")
        print("  (muon -2.02019 instead of proton -2.06934, a 2.4% shift on a")
        print("  window of half-width 1% — the two windows are DISJOINT).")
        print()
        print("  Cause: this producer's stem is listed under `ideal_muon` in")
        print("  computations/q0_anchor_manifest.json, which overrides q_at()")
        print("  to the muon value, or QOU_Q0_ANCHOR is set to ideal/muon.")
        print("  Fix: the stem belongs under `physical_proton` (it reads both")
        print("  pins by name); unset QOU_Q0_ANCHOR. See bean qou-y82a.")
        print()
        print("  No witness written.")
        return 2

    print("=" * 78)
    print(" Q_β c_3 composite sweep — systematic 2-factor, cross-anchor discriminated")
    print("=" * 78)
    print(f"  q_proton           = {mp.nstr(qp, 16)}")
    print(f"  q_muon             = {mp.nstr(qm, 16)}")
    print(f"  c_3_target(proton) = {mp.nstr(cp, 18)}")
    print(f"  c_3_target(muon)   = {mp.nstr(cm, 18)}")
    print(f"  cross-anchor swing = {mp.nstr(swing, 12)}  (~{float(swing/fabs(cp)*100):.2f} %)")
    print(f"  TOL_closure = {mp.nstr(TOL_CLOSURE,2)} (both anchors), "
          f"TOL_near = {mp.nstr(TOL_NEAR,2)} (proton)")
    print()

    cands = sweep_candidates(qp, qm)
    print(f"  swept {len(cands)} candidates (singletons + 2-factor composites)")
    print()

    closures = []
    near_matches = []
    ranked = []  # (proton_miss, muon_miss, name, vp, vm)

    for name, (vp, vm) in cands.items():
        # mpf end to end. These misses are the probe's ARGUMENT, not a
        # display quantity: they decide near-match membership and they get read
        # back out of the witness. AGENTS.md's NO-FLOAT64 rule applies to probes
        # verbatim, so the float() casts that used to sit here — at the point of
        # measurement, before any ranking — are gone. float() now appears only
        # inside f-strings, which is the one permitted use.
        pm = fabs(vp - cp) / fabs(cp)
        mm = fabs(vm - cm) / fabs(cm)
        ranked.append((pm, mm, name, vp, vm))
        if pm < TOL_CLOSURE and mm < TOL_CLOSURE:
            closures.append((name, vp, vm, pm, mm))
        elif pm < TOL_NEAR and mm >= TOL_CLOSURE:
            near_matches.append((name, vp, vm, pm, mm))

    ranked.sort(key=lambda r: r[0])  # by proton miss

    print("  ── Top 12 by proton-anchor agreement ──")
    print(f"  {'candidate':<34}{'proton_miss':>14}{'muon_miss':>14}")
    for pm, mm, name, vp, vm in ranked[:12]:
        print(f"  {name:<34}{float(pm):>14.3e}{float(mm):>14.3e}")
    print()

    # Near-matches: hit proton (<1%) but NOT both-anchor closure
    near_matches.sort(key=lambda r: r[3])
    print(f"  ── Near-matches (proton < 1%, NOT both-anchor closure): "
          f"{len(near_matches)} ──")
    for name, vp, vm, pm, mm in near_matches[:10]:
        print(f"  {name:<34}  proton {float(pm):.3e}  muon {float(mm):.3e}  "
              f"(fails cross-anchor)")
    print()

    print("=" * 78)
    print(" VERDICT")
    print("=" * 78)
    if closures:
        print(f"  POSITIVE — {len(closures)} composite(s) match the c_3 target at BOTH")
        print("  anchors within 1 ppm. Residue-A f-map candidate(s):")
        for name, vp, vm, pm, mm in closures:
            print(f"    {name}:  c_3(p)={mp.nstr(vp,18)} c_3(m)={mp.nstr(vm,18)}")
        verdict = "POSITIVE_CLOSURE"
    else:
        best = ranked[0]
        print("  NEGATIVE — no 2-factor composite matches the c_3 target at BOTH")
        print(f"  anchors within 1 ppm. Best proton-anchor matcher: {best[2]}")
        print(f"    proton_miss = {float(best[0]):.3e},  muon_miss = {float(best[1]):.3e}")
        print(f"    → {len(near_matches)} single-anchor near-matches recorded "
              f"(all fail the cross-anchor test).")
        print()
        print("  Combined with the saturated 28-candidate single-formula bracket,")
        print("  the 2-factor composite space is now also saturated. The open")
        print("  residue-A keystone is therefore NOT a 1- or 2-factor product of")
        print("  natural categorical objects. Remaining productive directions:")
        print("    (a) infinite-product / Habiro-ring tower (Composite 4);")
        print("    (b) KLR / Type-B-folded-crystal operators (Composites 1, 3 —")
        print("        require Mathlib KLR/Demazure infra per the scope doc);")
        print("    (c) accept residue A as inherently CAL-3-anchored (PR #1770).")
        verdict = "NEGATIVE_2FACTOR_SATURATED"

    # ── Witness ──
    wb = WitnessBuilder(
        "qbeta-composite-crossanchor-2factor-sweep", engine="mpmath"
    )
    wb.set_description(
        "Systematic 2-factor composite sweep for the Q_β c_3 f-map, "
        "discriminated by cross-anchor agreement (proton AND muon). The "
        "CAL-anchored c_3 target is computed at both substrate anchors via "
        "the ladder inversion c_3(q)=(Q_codata/Q_N2(q)−1)/u(q)³; a genuine "
        "closure must match the target (and its ~0.049 cross-anchor swing) "
        "at BOTH anchors, not just at the proton anchor. Supersedes the "
        "6-product proton-only first-test. No fits."
    )
    wb.set_content_block("conj:qbeta-precision-ladder")
    wb.add_data("q_proton", mp.nstr(qp, 50))
    wb.add_data("q_muon", mp.nstr(qm, 50))
    wb.add_data("c3_target_proton", mp.nstr(cp, 50))
    wb.add_data("c3_target_muon", mp.nstr(cm, 50))
    wb.add_data("c3_cross_anchor_swing", mp.nstr(swing, 50))
    wb.add_data("n_candidates_swept", len(cands))
    # Which pin each leg actually ran at, and how far apart they are. Recorded
    # so a reader can tell the regime from the file alone rather than having to
    # re-derive it from q0_anchor_manifest.json (bean qou-y82a).
    wb.add_data("anchor_separation_relative", fmt(anchor_sep))
    wb.add_data("near_match_window", {
        "criterion": "proton_miss < TOL_near (1%) AND muon_miss >= TOL_closure",
        "centre_c3_target_proton": mp.nstr(cp, 30),
        "half_width_relative": mp.nstr(TOL_NEAR, 4),
        "lower": mp.nstr(cp * (1 + TOL_NEAR), 30),
        "upper": mp.nstr(cp * (1 - TOL_NEAR), 30),
        "note": (
            "The near-match set is exactly the swept candidates whose value "
            "falls in this window, so the set is a function of WHERE THE "
            "TARGET SITS. Moving the target by more than the window's "
            "half-width replaces the set wholesale rather than thinning it: "
            "the muon-pinned window (centred -2.0201881) and this "
            "proton-pinned one are DISJOINT, and their near-match sets share "
            "zero members. A candidate leaving this set on an anchor change "
            "is therefore evidence about the WINDOW, not about the candidate."
        ),
    })
    wb.add_data("verdict", verdict)
    wb.add_data("n_closures", len(closures))
    wb.add_data("n_single_anchor_near_matches", len(near_matches))
    wb.add_data("best_proton_matcher", {
        "name": ranked[0][2],
        "proton_miss": fmt(ranked[0][0]),
        "muon_miss": fmt(ranked[0][1]),
    })
    wb.add_data("top12_by_proton_agreement", [
        {"name": n, "proton_miss": fmt(pm), "muon_miss": fmt(mm)}
        for pm, mm, n, _, _ in ranked[:12]
    ])
    # NOT truncated. It used to be `near_matches[:25]`, which silently
    # disagreed with `n_single_anchor_near_matches` whenever the count exceeded
    # 25 — the muon-pinned run recorded a list of 25 beside a count of 27, and
    # the list length was then read downstream as the result (bean qou-y82a).
    wb.add_data("single_anchor_near_matches", [
        {"name": n, "proton_miss": fmt(pm), "muon_miss": fmt(mm)}
        for n, _, _, pm, mm in near_matches
    ])
    wb.add_data("interpretation", (
        "Cross-anchor swing of the c_3 target is large (~2.4%), so a "
        "single-anchor proton match is necessary but far from sufficient. "
        "Candidates listed under single_anchor_near_matches reproduce the "
        "proton target to <1% but FAIL at the muon anchor — they are "
        "coincidences, not the f-map. A both-anchor closure (n_closures>0) "
        "would identify the residue-A categorical element."
    ))
    # AGENTS.md "Before declaring refuted / ruled out / dead end" requires the
    # (a)/(b) split on every durable negative. Stated in the witness so a
    # consumer reading `verdict` alone cannot over-read it (bean qou-y82a).
    wb.add_data("scope_classification", {
        "scope": "a",
        "meaning": (
            "Scope-limited negative: no 2-factor composite of THESE atoms, "
            "alone, reproduces the c_3 target at both anchors within 1 ppm. "
            "It constrains magnitudes and combinations, not ingredients."
        ),
        "not_scope_b_because": (
            "No proved invariant excludes any of these atoms from a closure. "
            "In particular a candidate's departure from "
            "single_anchor_near_matches under an anchor change is a "
            "TOLERANCE-WINDOW artifact (see near_match_window) and is not "
            "evidence about that candidate at all."
        ),
    })
    # Real invariant: the inversion reproduces the canonical proton target.
    wb.add_assertion(
        "c3_target_proton_matches_canonical",
        computed=cp,
        expected=-2.06934257711516783787971951725,
        tolerance=1e-12,
    )
    # Real invariant: the cross-anchor swing is non-trivial (the test has
    # discriminating power).
    wb.add_assertion(
        "cross_anchor_swing_resolvable",
        computed=1.0 if swing > mpf("1e-3") else 0.0,
        expected=1.0,
    )
    wb.save()
    print()
    print("  Witness: qbeta-composite-crossanchor-2factor-sweep.witness.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
