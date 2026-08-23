#!/usr/bin/env python3
"""Keystone vector 2 — the FULL-Hecke λ-COLORED WRT(S³/2I) per-block weight vs the Hecke q-dimension.

THE FALSIFIABLE OPEN STEP (no fit, zero free parameters).
--------------------------------------------------------
Prior corpus (READ before this probe):
  * `keystone_habiro_wrt_s3_2i_probe.py` — the BARE closed-manifold WRT(Σ(2,3,5)) number Ψ(1/q₀)≈2.330;
    its verdict pinpointed "colored insertions" as the open step.
  * `keystone_colored_sigma235_wrt.py` — colored the ICOSAHEDRAL (order-5) fibre by ONE SU(2) colour α
    (shift 1/5→α/5). That is the SU(2) ≤2-row image; it is degenerate (α=1,4→{1,11,19,29};
    α=2,3→{7,13,17,23}: only TWO distinct Ψ values) and its naive value map [e]_q was REFUTED.
  * `2026-06-24-keystone-step1-gate-wrt-vs-wlambda.md` — (b)-EXCLUDED the SU(2) route: the GL₂/spinor-ℂ²
    Schur–Weyl image is exactly the ≤2-row partitions, so `d_q(λ)=[2j+1]_q` holds ONLY on the standard
    rep (n−1,1); the 3-row electron (3,1,1) and the muon (3,2) get no SU(2) weight.

Vector 2 therefore tests the FULL-HECKE colouring (all rows / all partitions λ⊢n), NOT the SU(2)
≤2-row image. The question, stated falsifiably at q₀ and as an exact all-q identity:

    Does the λ-colored WRT(S³/2I) per-block weight  W^{WRT}_λ  reproduce  d_q(λ)
    (the S_n-side q-hook-length dimension, the W_λ numerator)  for ALL blocks λ⊢n, n=3,4,5,
    INCLUDING the ≥3-row blocks (electron (3,1,1), etc.),  with ZERO free parameters?

The parameter-free colored weight (standard ribbon/modular-category fact).
-------------------------------------------------------------------------
In ANY ribbon/modular category, the WRT invariant of a framed 3-manifold carrying a Wilson line
colored by an irrep V_λ FACTORIZES its colour dependence as  [Reshetikhin–Turaev 1991; Lawrence–
Rozansky 1999 (Seifert spheres); Beasley–Witten 2005]:

    W^{WRT}_λ  =  (global, λ-independent factors) · S_{0λ} · θ_λ^{f},

  • S_{0λ}/S_{00} = d_q(λ)  — the vacuum S-matrix row = quantum dimension. On the FULL-Hecke
    (U_q(gl_∞) / stable-HOMFLY / principal-specialisation) side this is EXACTLY the q-hook-length
    dimension d_q(λ), for ALL rows (no ≤2-row truncation — that is the whole point of vector 2).
  • θ_λ = q^{κ_λ}, κ_λ = 2·c(λ),  c(λ)=Σ_{(i,j)∈λ}(j−i) = content sum — the RIBBON TWIST eigenvalue on
    V_λ (the a-independent / q-part of the framing anomaly of the colored Wilson line). This is exact
    representation theory, NOT a choice.
  • f ∈ ℚ\{0} — the fibre framing FORCED by the Σ(2,3,5) geometry (nonzero orbifold Euler number
    e = −1/(2·3·5) = −1/30; equivalently Σ(2,3,5) = −1 surgery on the left trefoil ⇒ a fibre/surgery
    Wilson line has framing ≠ 0). f is fixed by the manifold — it is NOT tunable.

So the colored weight is d_q(λ) DRESSED by the geometry-forced twist θ_λ^f. The falsifiable test:

    W^{WRT}_λ ∝ d_q(λ) for all λ   ⟺   θ_λ^{f} = const in λ   ⟺   f·c(λ) = const   ⟺   f = 0.

But f = 0 is the CONTENT-FREE reduction (bare modular-category S-matrix) — valid for S³ / the empty
manifold / ANY manifold — it carries ZERO Σ(2,3,5) geometry (and "∝ d_q up to a global constant" with a
free constant is exactly the tautology the discipline forbids). For the ACTUAL manifold f ≠ 0, and:

  (i)  d_q is conjugation-SYMMETRIC:  d_q(λ)=d_q(λ') EXACTLY at every q (hook multiset is
       conjugation-invariant; [n]_q! is symmetric). — proved invariant.
  (ii) the twist is conjugation-ANTISYMMETRIC:  c(λ')=−c(λ) ⇒ θ_{λ'}=θ_λ^{-1}. — proved invariant.
  ⇒  the framed colored weight has  W^{WRT}_λ / W^{WRT}_{λ'} = θ_λ^{2f} ≠ 1 for c(λ)≠0, whereas
     d_q(λ)/d_q(λ') = 1. The two objects have DIFFERENT SYMMETRY. This mismatch is NORMALIZATION-
     INDEPENDENT (any global constant cancels in the λ↔λ' ratio) and holds for EVERY nonzero framing —
     so no free parameter can rescue it.

VERDICT (expected, honest negative): PARTIAL/FAIL. The full-Hecke colored-WRT construction reproduces
d_q(λ) ONLY in its content-free (f=0, no-geometry) reduction — a tautology of the modular category, not
of Σ(2,3,5). The genuine Σ(2,3,5)-framed colored weight dresses d_q by the parameter-free, content-
dependent, conjugation-antisymmetric ribbon twist θ_λ^{f≠0}, which breaks proportionality and breaks the
conjugation symmetry d_q carries. Scope: (b)-exclusion of the NARROW hypothesis "fibre-colored
WRT(Σ(2,3,5)) weight = d_q as-is" (cites the two proved twist/hook invariants + the nonzero framing);
the BROAD geometric W_λ programme (an S¹-equivariant index on the corrected full-Hecke arena) stays
(a)-OPEN. This PRUNES the colored-WRT line and names exactly what is missing: any geometric carrier of
W_λ must CANCEL the fibre framing (produce a twist-free / conjugation-symmetric amplitude), which a
Wilson line on the nontrivially-framed Σ(2,3,5) fibre structurally does not.

No fit; nothing wired; q₀ enters only as the evaluation point.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(HERE))

import _path_bridge as _bridge  # noqa: E402, F401
from mpmath import mp, mpf  # noqa: E402

from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()  # ≥50 dps compute
Q0 = mpf("1.1099785955541805")

# Σ(2,3,5) Seifert data — the framing is FIXED by the geometry, not tuned.
SEIFERT = (2, 3, 5)
P = SEIFERT[0] * SEIFERT[1] * SEIFERT[2]  # 30 = h(E8)
ORBIFOLD_EULER = mpf(-1) / P               # e = -1/30 (Poincaré sphere)
# Σ(2,3,5) = -1 surgery on the left-handed trefoil ⇒ the natural INTEGER fibre/surgery framing is |f|=1.
# We use f = -1 (the surgery coefficient) for the numeric table, and PROVE below that the verdict is
# framing-value-independent (any f≠0 fails), so |f|=1 is not a tuned choice.
F_GEOM = -1

TOL = mpf(10) ** (-40)


# ---- q-integers, q-factorial, q-hook-length dimension d_q (full Hecke, ALL rows) ----------------
def qint(m):
    return (Q0 ** m - Q0 ** (-m)) / (Q0 - Q0 ** (-1))


def q_factorial(m):
    r = mpf(1)
    for k in range(1, m + 1):
        r *= qint(k)
    return r


def hooks(lam):
    conj = [sum(1 for r in lam if r > j) for j in range(lam[0])]
    return [(row - j - 1) + (conj[j] - i - 1) + 1
            for i, row in enumerate(lam) for j in range(row)]


def d_q(lam):
    den = mpf(1)
    for h in hooks(lam):
        den *= qint(h)
    return q_factorial(sum(lam)) / den


def content_sum(lam):
    """c(λ) = Σ_{(i,j)∈λ} (col − row), 0-indexed cells ⇒ (j − i)."""
    return sum(j - i for i, row in enumerate(lam) for j in range(row))


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > j) for j in range(lam[0]))


def num_rows(lam):
    return len(lam)


def partitions(n):
    """All partitions of n as weakly-decreasing tuples."""
    def gen(n, mx):
        if n == 0:
            yield ()
            return
        for first in range(min(n, mx), 0, -1):
            for rest in gen(n - first, first):
                yield (first,) + rest
    return list(gen(n, n))


# ---- the colored-WRT per-block weight -----------------------------------------------------------
def theta(lam):
    """Ribbon twist eigenvalue on V_λ, a-independent q-part: θ_λ = q^{2 c(λ)}. Exact rep theory."""
    return Q0 ** (2 * content_sum(lam))


def w_wrt(lam, f):
    """Full-Hecke colored WRT weight of Σ(2,3,5) with a λ-colored fibre Wilson line at framing f:
       W^{WRT}_λ = d_q(λ) · θ_λ^{f}   (global λ-independent factors dropped — they never affect a
       proportionality / conjugation-symmetry test)."""
    return d_q(lam) * theta(lam) ** f


def run():
    per_n = {}
    for n in (3, 4, 5):
        parts = partitions(n)
        rows = []
        # reference ratio k_λ = W/d_q = θ_λ^f ; "∝ d_q" ⟺ k_λ constant in λ.
        ratios = {}
        for lam in parts:
            dq = d_q(lam)
            c = content_sum(lam)
            th = theta(lam)
            w = w_wrt(lam, F_GEOM)
            k = w / dq  # = θ_λ^{F_GEOM}
            ratios[lam] = k
            rows.append({
                "lambda": list(lam),
                "rows": num_rows(lam),
                "d_q": float(dq),
                "content_sum": c,
                "theta_lambda": float(th),
                "W_wrt_f": float(w),
                "ratio_W_over_dq": float(k),
                "conj": list(conjugate(lam)),
            })
        ks = [ratios[p] for p in parts]
        kmin, kmax = min(ks), max(ks)
        spread = kmax / kmin  # multiplicative spread of the ratio; ==1 ⟺ ∝ d_q
        proportional = abs(spread - 1) < float(TOL)

        # conjugation-symmetry diagnostics
        dq_conj_sym = all(abs(d_q(p) - d_q(conjugate(p))) < TOL for p in parts)
        # framed colored weight breaks conjugation symmetry?  W_λ == W_{λ'} only if c(λ)=0.
        conj_pairs_broken = 0
        conj_pairs_total = 0
        seen = set()
        for p in parts:
            pc = conjugate(p)
            key = frozenset({p, pc})
            if key in seen:
                continue
            seen.add(key)
            conj_pairs_total += 1
            wl, wlc = w_wrt(p, F_GEOM), w_wrt(pc, F_GEOM)
            # compare the ratio W/d_q for λ vs λ' (normalization-independent)
            if abs((wl / d_q(p)) - (wlc / d_q(pc))) > TOL:
                conj_pairs_broken += 1

        # count "matching" blocks = blocks whose ratio equals the modal reference (only c==c_ref).
        # A single global constant ∝ d_q would need ALL k_λ equal; report how many share the max-mult class.
        ge3_blocks = [p for p in parts if num_rows(p) >= 3]
        per_n[n] = {
            "rows_table": rows,
            "ratio_spread_multiplicative": float(spread),
            "proportional_to_dq": proportional,
            "dq_conjugation_symmetric": dq_conj_sym,
            "conj_pairs_total": conj_pairs_total,
            "conj_pairs_symmetry_broken_by_twist": conj_pairs_broken,
            "n_blocks": len(parts),
            "n_ge3row_blocks": len(ge3_blocks),
            "ge3row_blocks": [list(p) for p in ge3_blocks],
        }

    # framing-value-INDEPENDENCE of the verdict: the ratio spread for f=0 (content-free) vs f=±1,±2.
    n5 = partitions(5)
    f_dichotomy = {}
    for f in (0, 1, -1, 2, -2):
        ks = [theta(p) ** f for p in n5]
        f_dichotomy[str(f)] = {
            "ratio_spread": float(max(ks) / min(ks)),
            "proportional_to_dq": abs(float(max(ks) / min(ks)) - 1) < float(TOL),
        }

    return {
        "q0": float(Q0),
        "seifert": list(SEIFERT),
        "P": P,
        "orbifold_euler": float(ORBIFOLD_EULER),
        "framing_f_geom": F_GEOM,
        "per_n": per_n,
        "framing_dichotomy_n5": f_dichotomy,
    }


def _fmt_lam(l):
    return "(" + ",".join(map(str, l)) + ")"


def report(res):
    print("# Keystone vector 2 — FULL-Hecke λ-colored WRT(S³/2I) per-block weight vs d_q(λ)\n")
    print(f"q₀ = {res['q0']:.13f}   Σ = {tuple(res['seifert'])}   P = {res['P']} = h(E₈)   "
          f"orbifold e = {res['orbifold_euler']:.6f} ≠ 0   fibre framing f = {res['framing_f_geom']}\n")
    print("Colored weight (parameter-free):  W^{WRT}_λ = d_q(λ) · θ_λ^{f},  θ_λ = q^{2c(λ)} "
          "(ribbon twist),  f fixed by the Σ(2,3,5) framing.\n")
    print("Test:  W^{WRT}_λ ∝ d_q(λ) for ALL λ  ⟺  ratio k_λ = θ_λ^{f} constant in λ.\n")

    for n in (3, 4, 5):
        d = res["per_n"][n]
        print(f"## n = {n}   ({d['n_blocks']} blocks, {d['n_ge3row_blocks']} with ≥3 rows: "
              f"{', '.join(_fmt_lam(b) for b in d['ge3row_blocks']) or '—'})\n")
        print("| λ | rows | d_q(λ) | c(λ) | θ_λ = q^{2c} | W^{WRT}_λ | k_λ = W/d_q |")
        print("|---|:--:|--:|--:|--:|--:|--:|")
        for r in d["rows_table"]:
            print(f"| {_fmt_lam(r['lambda'])} | {r['rows']} | {r['d_q']:.6f} | {r['content_sum']:+d} "
                  f"| {r['theta_lambda']:.5f} | {r['W_wrt_f']:.6f} | {r['ratio_W_over_dq']:.6f} |")
        print(f"\n- ratio k_λ multiplicative spread (max/min) = **{d['ratio_spread_multiplicative']:.4f}** "
              f"(=1 ⟺ ∝ d_q). Proportional to d_q: **{d['proportional_to_dq']}**.")
        print(f"- d_q conjugation-symmetric (d_q(λ)=d_q(λ′)): **{d['dq_conjugation_symmetric']}**.  "
              f"Twist BREAKS conjugation symmetry on **{d['conj_pairs_symmetry_broken_by_twist']}"
              f"/{d['conj_pairs_total']}** conjugate pairs (broken ⟺ c(λ)≠0).\n")

    print("## Framing-value independence of the verdict (n=5) — no free parameter\n")
    print("| framing f | ratio spread | ∝ d_q? |")
    print("|--:|--:|:--:|")
    for f, dd in res["framing_dichotomy_n5"].items():
        note = "  ← content-free tautology (valid for ANY manifold; carries no Σ(2,3,5) data)" if f == "0" else ""
        print(f"| {f} | {dd['ratio_spread']:.4f} | {dd['proportional_to_dq']}{note} |")
    print("\nOnly f=0 gives proportionality — and f=0 is the geometry-free reduction. Σ(2,3,5) forces "
          "f≠0 (orbifold e=−1/30); every nonzero framing FAILS. No tunable constant rescues it.\n")

    print("## Verdict\n")
    print("PARTIAL/FAIL — scope (b) for the narrow hypothesis, (a)-open for the programme.")
    print("- The full-Hecke colored-WRT weight reproduces d_q(λ) ONLY in its content-free (f=0) reduction,")
    print("  which is a tautology of the modular category (S³ / any manifold), not of Σ(2,3,5).")
    print("- The genuine Σ(2,3,5)-framed colored weight dresses d_q by the parameter-free, content-")
    print("  dependent ribbon twist θ_λ^{f≠0}. Two PROVED invariants exclude proportionality:")
    print("    (i)  d_q(λ)=d_q(λ′) exactly (hook multiset conjugation-invariant);")
    print("    (ii) θ_{λ′}=θ_λ^{−1} (content sum conjugation-antisymmetric) ⇒ W_λ/W_{λ′}=θ_λ^{2f}≠1.")
    print("  These break the conjugation symmetry d_q carries, normalization-independently.")
    print("- ≥3-row blocks (electron (3,1,1), etc.): d_q is defined for them on the FULL-Hecke side")
    print("  (unlike the SU(2)/≤2-row route that had NO weight there), but the twist still spoils")
    print("  proportionality — (3,1,1) is self-conjugate (c=0, θ=1, untouched) while (5),(4,1),(3,2)")
    print("  are dilated by q^{2f·c}. So even the coverage the SU(2) route lacked does not yield a match.")
    print("- PRUNES the colored-WRT line: a geometric carrier of W_λ must CANCEL the fibre framing")
    print("  (produce a twist-free, conjugation-symmetric amplitude); a Wilson line on the nontrivially-")
    print("  framed Σ(2,3,5) fibre structurally does not. The broad S¹-equivariant-index route stays open.")
    print("\nNo fit; nothing wired; q₀ is only the evaluation point.")


def main(argv=None):
    res = run()
    report(res)

    w = WitnessBuilder("keystone-colored-wrt-perblock-vs-dq", engine="mpmath")
    w.set_description(
        "Keystone vector 2 (colored WRT / Lawrence-Rozansky): does the FULL-Hecke lambda-colored "
        "WRT(S^3/2I)=Sigma(2,3,5) per-block weight W^{WRT}_lambda reproduce the Hecke q-hook-length "
        "dimension d_q(lambda) for ALL blocks lambda|-n, n=3,4,5, incl. >=3-row (electron (3,1,1), "
        "muon (3,2)), with ZERO free parameters? The parameter-free colored weight factorizes as "
        "W^{WRT}_lambda = d_q(lambda)*theta_lambda^f (RT/Lawrence-Rozansky/Beasley-Witten): S_{0lambda} "
        "= d_q(lambda) on the full-Hecke side, theta_lambda = q^{2c(lambda)} the ribbon twist "
        "(c=content sum), f the NONZERO fibre framing forced by Sigma(2,3,5) (orbifold e=-1/30; = -1 "
        "surgery on the left trefoil). VERDICT: PARTIAL/FAIL. Proportionality holds ONLY at f=0 (content-"
        "free tautology, valid for any manifold, no Sigma(2,3,5) data); for the actual nonzero framing "
        "the twist dressing is content-dependent and conjugation-ANTISYMMETRIC (theta_{lambda'}="
        "theta_lambda^{-1}) while d_q is conjugation-SYMMETRIC (d_q(lambda)=d_q(lambda') exactly), so "
        "W_lambda/W_{lambda'}=theta_lambda^{2f}!=1 breaks proportionality normalization-independently, "
        "for EVERY nonzero framing. (b)-excludes the narrow 'fibre-colored WRT weight = d_q as-is' "
        "hypothesis (cites the two proved twist/hook invariants + nonzero framing); the broad geometric "
        "W_lambda programme stays (a)-open. Prunes the colored-WRT line. No fit; nothing wired."
    )
    w.add_data("q0", res["q0"])
    w.add_data("seifert", res["seifert"])
    w.add_data("P_coxeter_E8", res["P"])
    w.add_data("orbifold_euler", res["orbifold_euler"])
    w.add_data("framing_f_geom", res["framing_f_geom"])
    w.add_data("per_n", res["per_n"])
    w.add_data("framing_dichotomy_n5", res["framing_dichotomy_n5"])
    w.add_data(
        "verdict",
        "PARTIAL/FAIL (scope-(b) narrow, (a)-open programme): the full-Hecke colored-WRT weight of "
        "Sigma(2,3,5) reproduces d_q(lambda) ONLY in the content-free f=0 reduction (a modular-category "
        "tautology, no Sigma(2,3,5) geometry). The geometry-forced nonzero framing dresses d_q by the "
        "content-dependent, conjugation-antisymmetric ribbon twist theta_lambda^f, breaking the "
        "conjugation symmetry d_q carries -- normalization-independently and for every nonzero framing. "
        "No free parameter rescues it. Prunes the colored-WRT line; the geometric carrier of W_lambda "
        "must cancel the fibre framing, which a fibre Wilson line does not.",
    )

    # Sanity assertions (the proved invariants underpinning the verdict) — these PASS.
    dq_sym_all = all(res["per_n"][n]["dq_conjugation_symmetric"] for n in (3, 4, 5))
    twist_breaks_all = all(res["per_n"][n]["conj_pairs_symmetry_broken_by_twist"] > 0 for n in (4, 5))
    f0_only = (res["framing_dichotomy_n5"]["0"]["proportional_to_dq"] and
               not res["framing_dichotomy_n5"]["-1"]["proportional_to_dq"] and
               not res["framing_dichotomy_n5"]["1"]["proportional_to_dq"])
    w.add_assertion(
        "dq_conjugation_symmetric", computed=1 if dq_sym_all else 0, expected=1, tolerance=0,
        source="d_q(lambda)=d_q(lambda') EXACTLY at every q: hook-length multiset is conjugation-"
               "invariant and [n]_q! is symmetric. Verified n=3,4,5 to 40 dps.",
    )
    w.add_assertion(
        "ribbon_twist_breaks_conjugation_symmetry", computed=1 if twist_breaks_all else 0,
        expected=1, tolerance=0,
        source="theta_{lambda'}=theta_lambda^{-1} (content sum c(lambda')=-c(lambda)), so the framed "
               "colored weight W_lambda=d_q*theta^f has W_lambda/W_{lambda'}=theta^{2f}!=1 for c!=0 -- "
               "it does NOT share d_q's conjugation symmetry. Verified on every non-self-conjugate pair.",
    )
    w.add_assertion(
        "proportional_to_dq_only_at_zero_framing", computed=1 if f0_only else 0, expected=1, tolerance=0,
        source="The colored weight is ∝ d_q ONLY at framing f=0 (the content-free modular-category "
               "reduction, valid for any manifold). Sigma(2,3,5) forces f!=0 (orbifold e=-1/30); every "
               "nonzero framing gives a content-dependent ratio theta_lambda^f that is NOT constant in "
               "lambda. Hence the geometric colored-WRT weight does NOT reproduce the d_q family -- a "
               "documented, parameter-free NEGATIVE that prunes the colored-WRT line.",
    )
    out = w.save()
    print(f"\nwitness → {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
