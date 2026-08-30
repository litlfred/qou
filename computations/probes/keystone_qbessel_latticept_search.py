#!/usr/bin/env python3
"""keystone_qbessel_latticept_search.py — s013 geometric W_λ vector 1.

Falsifiable, ZERO-fit test of the OPEN `latticePt` field of the keystone
obligation class `QBesselRadialPartRealization`
(`QOU/BraidKnot/KeystoneQBesselRadialTarget.lean`).

## What is open, and what this probe tests

The keystone residual-(i) reduced to the single open field
`bwS0(λ) = d_q(λ)/D` (the Verlinde vacuum row).  The Lean obligation class
supplies, for a *realization*:

  * `latticePt : Part → ℕ`         — the OPEN partition→lattice-index map
  * `weight    : ℕ → R`            — a radial weight solving the Jackson
        SECOND-KIND q-Bessel contiguity recurrence (`qbesselSecondKindRatio`,
        `QBesselContiguityRecurrence.lean`):
            w(k+1)·(1−q^{k+1})(1−a q^{k+1}) = −(a q^{2k+1})·w(k)
        ⟹  w(k) = w(0)·∏_{j<k} r_j,   r_j = −(a q^{2k+1})/[(1−q^{k+1})(1−a q^{k+1})]
  * `realizes : w(latticePt λ) = bwS0(λ) = d_q(λ)/D`
  * `latticePt_conj`               — TRANSPOSE-INVARIANCE (W_λ = W_{λ′})

Because `weight` is fixed by the recurrence up to the global scale `w(0)`, and
`D` is a global constant, the realization condition is normalization-free:

        P_{k_λ}/P_{k_μ}  =  d_q(λ)/d_q(μ)     for ALL blocks λ,μ           (†)

where `P_k = ∏_{j<k} r_j` is the second-kind contiguity ORBIT.  A realization
therefore demands the whole vacuum row lie on ONE q-Bessel orbit at the
structurally-chosen indices `k_λ` (`realization_on_orbit`).  (†) eliminates
both `w(0)` and `D`; the discriminating block is the self-conjugate `(3,1,1)`
whose `d_q = [4][3]/[2]` is the sole genuine product.

## Distinct from prior s013 probes (anti-duplication)

  * `keystone_valuemap_screen_s013.py` (#3197): screened COMPACT closed forms
    ([e]_q, sin-kernel, sinh) against d_q via E₈-exponent labels — all refuted.
  * `keystone_qhankel_eq2_vacuum_row.py`: tested the ROOTS μ_j of the
    Hahn–Exton q-Bessel (Plancherel nodes) as the values — refuted (scope a).

Neither tested a STRUCTURAL `latticePt` INDEX map feeding the second-kind
contiguity WEIGHT orbit.  That is the open field this probe attacks.

## The falsifiability discipline (no fit, no free constant)

A candidate `latticePt` is admissible ONLY if it is a fixed structural formula
with ZERO tunable parameters.  We compute a battery of transpose-invariant,
parameter-free integer indices directly from each Young diagram:

    (A) |content sum|     |Σ(j−i)|            (candidate: content-sum index)
    (B) content² sum       Σ(j−i)²            (quadratic-Casimir / |κ| index)
    (C) Durfee size        d(λ)               (self-conjugate diagonal length)
    (D) n(λ)+n(λ')         Σ(i−1)λ_i + transp (transpose-symmetric coarea)
    (E) max hook           max hook length    (principal-hook / column index)
    (F) hook sum           Σ hooks

The recurrence parameter `a = q^ν` is likewise NOT fitted: `ν` ranges over the
small DISCRETE structural order-set {0, 1/2, 1, 2} (each a fixed q-Bessel order,
not a continuous constant).  `q` is the substrate q₀ (and its image 1/q₀; the
balanced d_q is q↔1/q invariant, the orbit is not, so both are reported).

A map is admissible for (†) ONLY IF it is INJECTIVE on the classes with
distinct d_q — a map that assigns the SAME index to two classes with different
d_q forces one weight value to equal two numbers, an immediate structural
exclusion (reported as such, no numeric run needed).

Nothing is wired to production; nothing is committed by this probe.
Honest negative is the expected, acceptable outcome (no-negative-result
discipline, AGENTS.md).

-- Ref: [koelink1994] https://doi.org/10.1215/S0012-7094-94-07617-0
-- Ref: [koelink-swarttouw-1994] https://doi.org/10.1006/jmaa.1994.1330
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
COMPUTATIONS_DIR = HERE.parent
sys.path.insert(0, str(COMPUTATIONS_DIR))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from q_parameter import Q_MP  # noqa: E402
import mpmath as mp  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402

COMPUTE_DPS = 60
mp.mp.dps = COMPUTE_DPS

# Substrate modulus (muon-q0 canonical computations/ value, matching the
# value-map screen #3197 exactly).
# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches
# neither current pin, so nothing could compare it against
# anything. Owner ruling 2026-08-24, bean `qou/ftuv`.
Q0 = Q_MP

TOL = mp.mpf("1e-9")   # relative match tolerance for (†)


# ── q-integer (screen convention: unbalanced-symmetric (q^n−q^-n)/(q−q^-1)) ──
def qi(m, q):
    # Guard the q→1 removable singularity (Copilot/Gemini #3652): the closed
    # form suffers catastrophic cancellation / division-by-zero as q→1, where
    # [m]_q → m. Tolerance tied to the active precision (mp.eps), not hardcoded.
    if abs(q - 1) < mp.eps:
        return mp.mpf(m)
    return (q ** m - q ** (-m)) / (q - q ** (-1))


# ── Young-diagram combinatorics (parameter-free structural indices) ──────────
def cells(part):
    return [(i, j) for i, r in enumerate(part) for j in range(r)]  # 0-indexed


def conjugate(part):
    if not part:
        return []
    m = part[0]
    return [sum(1 for r in part if r > c) for c in range(m)]


def content_sum(part):
    return sum(j - i for (i, j) in cells(part))


def content_sq_sum(part):
    return sum((j - i) ** 2 for (i, j) in cells(part))


def durfee(part):
    d = 0
    while d < len(part) and part[d] > d:
        d += 1
    return d


def n_stat(part):
    return sum(i * r for i, r in enumerate(part))  # Σ (i-1)λ_i with 0-index i


def hooks(part):
    conj = conjugate(part)
    hs = []
    for (i, j) in cells(part):
        arm = part[i] - j - 1
        leg = conj[j] - i - 1
        hs.append(arm + leg + 1)
    return hs


def dq_partition(part, q):
    """d_q(λ) = [n]_q! / ∏ hook_q  (q-hook-length)."""
    n = sum(part)
    num = mp.mpf(1)
    for m in range(1, n + 1):
        num *= qi(m, q)
    den = mp.mpf(1)
    for h in hooks(part):
        den *= qi(h, q)
    return num / den


# ── second-kind q-Bessel contiguity orbit ────────────────────────────────────
def second_kind_ratio(q, a, k):
    return -(a * q ** (2 * k + 1)) / ((1 - q ** (k + 1)) * (1 - a * q ** (k + 1)))


def orbit_P(q, a, kmax):
    """P_k = ∏_{j<k} r_j for k = 0..kmax."""
    P = [mp.mpf(1)]
    acc = mp.mpf(1)
    for j in range(kmax):
        acc *= second_kind_ratio(q, a, j)
        P.append(acc)
    return P


# ── the four n=5 conjugation classes (seven blocks under transpose) ──────────
# class_key: representative partition ; blocks: the transpose orbit
CLASS_PARTS = {
    "(5)~(1^5)": (5,),
    "(4,1)~(2,1^3)": (4, 1),
    "(3,2)~(2,2,1)": (3, 2),
    "(3,1,1) self-conj": (3, 1, 1),
}
SEVEN_BLOCKS = [
    ("(5)", (5,)), ("(1^5)", (1, 1, 1, 1, 1)),
    ("(4,1)", (4, 1)), ("(2,1,1,1)", (2, 1, 1, 1)),
    ("(3,2)", (3, 2)), ("(2,2,1)", (2, 2, 1)),
    ("(3,1,1)", (3, 1, 1)),
]

INDEX_MAPS = {
    "A_abs_content_sum": lambda p: abs(content_sum(p)),
    "B_content_sq_sum": lambda p: content_sq_sum(p),
    "C_durfee": lambda p: durfee(p),
    "D_n_plus_nconj": lambda p: n_stat(p) + n_stat(conjugate(p)),
    "E_max_hook": lambda p: max(hooks(p)),
    "F_hook_sum": lambda p: sum(hooks(p)),
}
MAP_WHY = {
    "A_abs_content_sum": "|Σ(j−i)|; transpose-invariant (content negates → abs fixed); no free param",
    "B_content_sq_sum": "Σ(j−i)² = quadratic-Casimir magnitude; transpose-invariant; no free param",
    "C_durfee": "Durfee-square side (main-diagonal length); transpose-invariant; no free param",
    "D_n_plus_nconj": "n(λ)+n(λ′), transpose-symmetric coarea; no free param",
    "E_max_hook": "max hook length (principal hook = arm+leg+1 of corner); transpose-invariant; no free param",
    "F_hook_sum": "Σ hook lengths; transpose-invariant (hook multiset invariant); no free param",
}


def transpose_invariant(mapfn):
    for _, p in SEVEN_BLOCKS:
        if mapfn(list(p)) != mapfn(conjugate(list(p))):
            return False
    return True


def run():
    res = {"q0": mp.nstr(Q0, 20), "compute_dps": COMPUTE_DPS, "maps": {}, "runs": []}

    # target d_q per class (q0 convention)
    q = Q0
    dq_class = {k: dq_partition(list(p), q) for k, p in CLASS_PARTS.items()}
    res["target_d_q"] = {k: mp.nstr(v, 12) for k, v in dq_class.items()}

    # class-index per map, injectivity + transpose-invariance triage
    class_of_part = {
        (5,): "(5)~(1^5)", (1, 1, 1, 1, 1): "(5)~(1^5)",
        (4, 1): "(4,1)~(2,1^3)", (2, 1, 1, 1): "(4,1)~(2,1^3)",
        (3, 2): "(3,2)~(2,2,1)", (2, 2, 1): "(3,2)~(2,2,1)",
        (3, 1, 1): "(3,1,1) self-conj",
    }
    for mname, mapfn in INDEX_MAPS.items():
        idx_class = {k: mapfn(list(p)) for k, p in CLASS_PARTS.items()}
        tinv = transpose_invariant(mapfn)
        # injective on classes whose d_q differ?
        collisions = []
        keys = list(CLASS_PARTS)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                ki, kj = keys[i], keys[j]
                if idx_class[ki] == idx_class[kj] and \
                   abs(dq_class[ki] - dq_class[kj]) > TOL:
                    collisions.append((ki, kj, idx_class[ki]))
        res["maps"][mname] = {
            "why_structural": MAP_WHY[mname],
            "transpose_invariant": tinv,
            "index_per_class": idx_class,
            "injective_on_distinct_dq": len(collisions) == 0,
            "collisions": [
                {"classes": [a, b], "shared_index": idx} for (a, b, idx) in collisions
            ],
        }

    # numeric (†) test for the admissible (injective) maps, over q-choices and orders
    q_choices = [("q0", Q0), ("1/q0", 1 / Q0)]
    orders = [("0", mp.mpf(0)), ("1/2", mp.mpf(1) / 2), ("1", mp.mpf(1)), ("2", mp.mpf(2))]

    any_match = False
    for mname, minfo in res["maps"].items():
        if not (minfo["transpose_invariant"] and minfo["injective_on_distinct_dq"]):
            continue
        mapfn = INDEX_MAPS[mname]
        for qn, q in q_choices:
            dq_c = {k: dq_partition(list(p), q) for k, p in CLASS_PARTS.items()}
            idx_c = {k: mapfn(list(p)) for k, p in CLASS_PARTS.items()}
            kmax = max(idx_c.values()) + 1
            for on, nu in orders:
                a = q ** nu
                P = orbit_P(q, a, kmax)
                # reference class = the one with the SMALLEST index (anchor)
                ref = min(idx_c, key=lambda kk: idx_c[kk])
                Pref = P[idx_c[ref]]
                blocks = []
                max_rel = mp.mpf(0)
                sign_ok = True
                for bname, p in SEVEN_BLOCKS:
                    cl = class_of_part[p]
                    k = idx_c[cl]
                    pred = P[k] / Pref * dq_c[ref]   # w(k)/w(ref)·d_q(ref) target-normalized
                    tgt = dq_c[cl]
                    rel = abs(pred - tgt) / abs(tgt) if tgt != 0 else abs(pred)
                    if rel > max_rel:
                        max_rel = rel
                    if (pred < 0) != (tgt < 0):
                        sign_ok = False
                    blocks.append({
                        "block": bname, "class": cl, "lattice_k": k,
                        "P_k": mp.nstr(P[k], 8),
                        "predicted_weight_normed": mp.nstr(pred, 10),
                        "target_d_q": mp.nstr(tgt, 10),
                        "rel_err": mp.nstr(rel, 6),
                    })
                matched = bool(max_rel < TOL and sign_ok)
                any_match = any_match or matched
                res["runs"].append({
                    "map": mname, "q_choice": qn, "order_nu": on,
                    "a_eq_q_pow_nu": mp.nstr(a, 10),
                    "anchor_class": ref,
                    "sign_consistent": sign_ok,
                    "max_rel_err": mp.nstr(max_rel, 6),
                    "matched_no_fit": matched,
                    "blocks": blocks,
                })
    res["any_candidate_matched"] = any_match
    return res


def report(res):
    print("# s013 — geometric W_λ vector 1: q-Bessel radial latticePt search (NO FIT)\n")
    print(f"q0 = {res['q0']}   dps = {res['compute_dps']}\n")
    print("Target vacuum-row d_q per n=5 conjugation class:")
    for k, v in res["target_d_q"].items():
        print(f"  d_q[{k:22s}] = {v}")
    print()

    print("## Structural latticePt maps — transpose-invariance + injectivity triage\n")
    print("| map | transpose-inv | injective on distinct d_q | indices (5)/(4,1)/(3,2)/(3,1,1) |")
    print("|---|:--:|:--:|---|")
    order = ["(5)~(1^5)", "(4,1)~(2,1^3)", "(3,2)~(2,2,1)", "(3,1,1) self-conj"]
    for mname, mi in res["maps"].items():
        idxs = "/".join(str(mi["index_per_class"][k]) for k in order)
        print(f"| {mname} | {mi['transpose_invariant']} | "
              f"{mi['injective_on_distinct_dq']} | {idxs} |")
    print()
    for mname, mi in res["maps"].items():
        if mi["collisions"]:
            for c in mi["collisions"]:
                a, b = c["classes"]
                print(f"  - {mname}: STRUCTURALLY EXCLUDED — classes {a} and {b} share "
                      f"index {c['shared_index']} but have different d_q "
                      f"(one weight cannot equal two values).")
    print("\n  → Only INJECTIVE transpose-invariant maps can possibly satisfy (†); "
          "the rest are excluded a priori (no numeric run needed).\n")

    print("## Numeric (†) test on admissible maps  P_{k_λ}/P_{k_ref} = d_q(λ)/d_q(ref)\n")
    print("| map | q | ν (a=q^ν) | sign-consistent | max rel err | MATCH (no fit) |")
    print("|---|---|---|:--:|--:|:--:|")
    for r in res["runs"]:
        print(f"| {r['map']} | {r['q_choice']} | {r['order_nu']} | "
              f"{r['sign_consistent']} | {r['max_rel_err']} | {r['matched_no_fit']} |")
    print()
    # show the worst discriminating block detail for one representative failing run
    if res["runs"]:
        r0 = res["runs"][0]
        print(f"Representative per-block detail ({r0['map']}, q={r0['q_choice']}, ν={r0['order_nu']}):")
        print("| block | class | k | P_k | predicted (normed) | target d_q | rel err |")
        print("|---|---|--:|--:|--:|--:|--:|")
        for b in r0["blocks"]:
            print(f"| {b['block']} | {b['class']} | {b['lattice_k']} | {b['P_k']} | "
                  f"{b['predicted_weight_normed']} | {b['target_d_q']} | {b['rel_err']} |")
    print()

    print("## Verdict\n")
    if res["any_candidate_matched"]:
        print("- **A STRUCTURAL latticePt MATCHED all seven blocks with NO fit.** This is a "
              "genuine candidate construction of the open `latticePt` field — see the matching "
              "row; a follow-up may formalize it as a `QBesselRadialPartRealization` instance "
              "(pending owner review + (a)/(b) adjudication).")
    else:
        print("- **ALL structural latticePt candidates FAIL (scope-(a)).** No transpose-invariant, "
              "zero-parameter index map — among |content sum|, content² sum, Durfee, n(λ)+n(λ′), "
              "max hook, hook sum — feeds the second-kind q-Bessel contiguity orbit so that "
              "P_{k_λ}/P_{k_ref} reproduces the vacuum row d_q at the seven n=5 blocks.")
        print("- Two structural obstructions, reported separately:")
        print("  1. **Collision exclusion (a priori):** most transpose-invariant integer indices "
              "(Durfee, n+n′, max hook, hook sum) assign the SAME index to classes with DIFFERENT "
              "d_q — one weight cannot be two values. Only |content sum| and content² sum are "
              "injective enough to even be testable.")
        print("  2. **Orbit-shape mismatch (numeric):** for the injective maps, the second-kind "
              "contiguity orbit P_k (whose consecutive ratios alternate sign and scale like "
              "q^{2k}) does not track the near-linear d_q growth (1, 4.11, 5.22, 6.22); the "
              "self-conjugate (3,1,1) product [4][3]/[2] is missed as sharply as the single "
              "q-integers.")
        print("- **Scope classification (AGENTS.md): (a) scope-limited negative.** These specific "
              "structural lattice maps, ALONE, do not realize the vacuum row on the second-kind "
              "q-Bessel orbit. This is NOT a structural exclusion (b): no proved invariant forbids "
              "a q-Bessel radial realization in general — a *non-integer-index* / *different-order* "
              "/ *first- or third-kind* / genuinely geometric (owner-gated DG, #2503) latticePt is "
              "untouched here. What a (b) would need: a proved parity/degree/orbit invariant "
              "showing NO reindexing of the contiguity orbit can hit the d_q vector.")
        print("- Consistent with the two prior s013 negatives (compact value-map screen #3197; "
              "Hahn–Exton Plancherel-root probe): the compact Markov/Verlinde identity "
              "S_0λ/S_00 = d_q remains the non-geometric 'why', not a q-Bessel radial weight.")


def main():
    res = run()
    report(res)
    w = WitnessBuilder("keystone-qbessel-latticept-search", engine="mpmath", output_dir=HERE)
    w.set_description(
        "s013 geometric W_lambda vector 1: falsifiable NO-FIT test of the open latticePt field of "
        "QBesselRadialPartRealization. Feeds six transpose-invariant zero-parameter structural index "
        "maps (|content sum|, content^2 sum, Durfee, n(l)+n(l'), max hook, hook sum) into the "
        "second-kind Jackson q-Bessel contiguity WEIGHT orbit P_k=prod r_j (qbesselSecondKindRatio), "
        "over q in {q0,1/q0} and orders nu in {0,1/2,1,2} (a=q^nu). Tests the normalization-free "
        "realization condition P_{k_lambda}/P_{k_ref}=d_q(lambda)/d_q(ref) at all seven n=5 blocks "
        "incl. the self-conjugate (3,1,1)=[4][3]/[2]. Distinct from prior probes which tested "
        "q-Bessel ROOTS (keystone_qhankel_eq2_vacuum_row) or COMPACT closed forms "
        "(keystone_valuemap_screen_s013), not a structural latticePt INDEX into the weight orbit. "
        "Structural triage: most transpose-invariant indices collide (same index, different d_q) => "
        "excluded a priori; only |content sum| and content^2 sum are injective+testable. VERDICT: "
        "all candidates FAIL (scope a) -- these structural lattice maps alone do not realize the "
        "vacuum row on the second-kind q-Bessel orbit; NOT a structural exclusion (b). No fit, "
        "nothing wired."
    )
    w.add_data("q0", res["q0"])
    w.add_data("compute_dps", res["compute_dps"])
    w.add_data("target_d_q", res["target_d_q"])
    w.add_data("maps", res["maps"])
    w.add_data("runs", res["runs"])
    w.add_data("any_candidate_matched", res["any_candidate_matched"])
    verdict = (
        "MATCH (no fit) — a structural latticePt reproduces the seven-block vacuum row on the "
        "second-kind q-Bessel orbit; candidate construction of the open field (pending review)."
        if res["any_candidate_matched"] else
        "REFUTED-as-is (scope a): NO transpose-invariant zero-parameter structural index map "
        "(|content sum| / content^2 sum / Durfee / n+n' / max hook / hook sum) feeds the "
        "second-kind Jackson q-Bessel contiguity orbit P_k so that P_{k_lambda}/P_{k_ref} = "
        "d_q(lambda)/d_q(ref) at the seven n=5 blocks. Two obstructions: (1) collision exclusion "
        "-- Durfee/n+n'/max-hook/hook-sum assign one index to classes with different d_q (a "
        "priori excluded); (2) orbit-shape mismatch -- for the injective |content sum| and "
        "content^2 sum maps, the alternating q^{2k}-scaled orbit misses the near-linear d_q "
        "(1,4.11,5.22,6.22), the self-conjugate [4][3]/[2] missed as sharply as the single "
        "q-integers. Scope (a) not (b): no proved invariant forbids a q-Bessel radial "
        "realization in general; non-integer-index / other-order / other-kind / geometric-DG "
        "(#2503) latticePt untouched. A (b) would need a proved parity/degree/orbit invariant. "
        "Consistent with the two prior s013 negatives. No fit; nothing wired."
    )
    w.add_data("verdict", verdict)
    w.add_assertion(
        "no_structural_latticept_realizes_vacuum_row",
        computed=(0 if res["any_candidate_matched"] else 1),
        expected=1, tolerance=0,
        source="Falsification gate: the disciplined claim is a coherent no-fit realization of the "
               "seven-block vacuum row on the second-kind q-Bessel contiguity orbit via a "
               "transpose-invariant zero-parameter structural latticePt. A future map that "
               "reproduces d_q(lambda)/d_q(ref) at all seven blocks must FAIL this assertion so it "
               "is re-adjudicated (a)/(b) under owner review before any wiring.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
