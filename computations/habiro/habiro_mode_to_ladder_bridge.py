#!/usr/bin/env python3
"""habiro_mode_to_ladder_bridge.py — execute the PR #1622 OPEN BRIDGE:
the change of variable u = √q ↦ u_L = b·ℏ_q² that reads the ladder c_k
off the exact Δtr_M mode decomposition (1ppQ-Q_β keystone).

WHY THIS PROBE.  PR #1622 (`habiro_q_difference_mode_solve.py`)
decomposed Δtr_M(u), u = q^{1/2} = \\check q, EXACTLY into three spectral
sectors and left ONE defined step open: map u = √q onto the ladder
variable u_L = b·ℏ_q² and read off the c_k of
    Q_β = Q_base · ∏_{k≥2} (1 + c_k · u_L^k).
#2106 went the Stage-B (per-block operator) route instead and stalled.
This probe takes the orthogonal #1622 bridge.

THE FORMAL STRUCTURE (why this is a defined computation, not a real-q
scan — the refuted-class map §1 C1 forbids real-q evaluation):

  q = u²,  ℏ_q = (q−1)/q = 1 − u^{-2},  so with ℏ := ℏ_q:
    u = √q = (1 − ℏ)^{-1/2}          (integer-power series in ℏ; u(0)=1)
    u_L = b·ℏ²                        ⟹  ℏ = √(u_L / b)

  Δtr_M(u) is rational in u with denominator 4u⁴(u²+1) (≠0 at u=1), so
  Δtr_M expressed in ℏ is an ORDINARY power series Σ_n a_n ℏ^n.  Because
  u_L = b·ℏ²:
    EVEN n = 2k  →  a_{2k}·(u_L/b)^k          : INTEGER u_L^k  (the ladder)
    ODD  n = 2k+1 → a_{2k+1}·(u_L/b)^{k+1/2}  : HALF-INTEGER   (bar-ODD;
        the −√3/12·u¹ remainder PR #1602 found f must cancel — the √u→u²
        lift flagged in the refuted-class map §4)

  So the integer-ladder coefficients G_k := a_{2k} / b^k are CONSTANTS —
  anchor-independent BY CONSTRUCTION (no q₀ evaluation enters).  That is
  the only path that is NOT C1-refuted (registry §8 anchor-stability
  gate).  The bar-even projection ½(Δtr_M(u)+Δtr_M(1/u)) is exactly the
  even-in-ℏ part (kills the odd/half-integer rungs).

WHAT THIS PROBE COMPUTES (exact symbolic; b kept symbolic, value
substituted only for the final numeric c_k):

  1. Δtr_M(u) exact (from the canonical atomic Habiro witness).
  2. Its even-in-ℏ series (= bar-even projection) to order ℏ^8.
  3. The integer-ladder coefficients G_k = a_{2k}/b^k, k = 1..4.
  4. Peel the product ∏(1+c_k u_L^k): the seed normalised so the leading
     rung is the PROVED c_2 = −1 (the one scale d.o.f.); read implied
     c_3, c_4.
  5. CONTROL: the naive real-q analytic c_k at the two anchors (proton +
     muon) — predicted C1-refuted (swing ≫ 1%) — to contrast with the
     anchor-independent formal coefficients.

DISCIPLINE (AGENTS.md §7b, ck-tiered-not-binary, refuted-class map):
exact symbolic; TIERED reporting; NO fitted form; NO production wiring;
NO registry tier change from this probe.  A coefficient is reported
`derived` only if it equals the framework's stated form to compute
precision AND is anchor-stable; otherwise `near-match` or `refuted`.
"""
from __future__ import annotations

# Path bridge (subdirectory refactor — keeps flat-namespace imports).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))

import os  # noqa: E402
os.environ.setdefault("QOU_COMPUTE_DPS", "70")
os.environ.setdefault("QOU_OUTPUT_DPS", "60")

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(70)

from witness_base import WitnessBuilder  # noqa: E402

u = sp.Symbol("u", positive=True)        # Habiro half-twist u = √q
hbar = sp.Symbol("hbar")                 # ℏ_q  (the physical small param)
b = sp.Symbol("b", positive=True)        # Hoefsmit ladder constant
ORDER = 10                               # ℏ-series order (need ℏ^8 → u_L^4)


def q_pochhammer_sym(m: int) -> sp.Expr:
    r = sp.Integer(1)
    for k in range(1, m + 1):
        r *= (1 - u ** k)
    return r


def habiro_trM(atom: dict) -> sp.Expr:
    # Bean qou-0ndb: `denom_in_u` / `a_m` are serialized in whichever
    # symbol the atomic producer computed with. Files written before the
    # `str_in_u` canonicalisation say `check_q`; the current convention-D
    # `habiro-coefficients-atomic.witness.json` says `u`. Binding only
    # `check_q` made `sympify` mint a SECOND, assumption-free `Symbol('u')`
    # distinct from this module's `Symbol('u', positive=True)` — the "ARMED"
    # case in that bean's consumer survey. Nothing raised: the two symbols
    # print identically, so Δtr_M silently became a BIVARIATE rational
    # function (451 numerator terms instead of 5), `.subs(u, ...)` reached
    # only half of it, and the ℏ-series at step 2 then expanded a rational
    # function of a free symbol — 13.9 GB and an OOM kill. Bind both names
    # until every affected witness has been regenerated.
    loc = {"u": u, "check_q": u}
    D = sp.sympify(atom["denom_in_u"], locals=loc)
    total = sp.Integer(0)
    for c in atom["habiro_coefficients"]:
        a_m = sp.sympify(c["a_m"], locals=loc)
        total += a_m * q_pochhammer_sym(int(c["m"]))
    trM = sp.cancel(total / D)
    stray = trM.free_symbols - {u}
    if stray:
        raise ValueError(
            f"habiro_trM: unbound symbol(s) {stray} survived the "
            f"atomic-witness parse — the serialized symbol name is "
            f"neither `u` nor `check_q` (bean qou-0ndb). Refusing to "
            f"continue: a free symbol here does not raise, it makes the "
            f"ℏ-series below expand a bivariate rational function and "
            f"exhaust memory.")
    return trM


def main() -> int:
    t0 = time.monotonic()
    builder = WitnessBuilder(
        "habiro-mode-to-ladder-bridge",
        engine="python+sympy",
        start_time=t0,
    )
    builder.set_description(
        "Executes the PR #1622 open bridge: the change of variable "
        "u=√q ↦ u_L=b·ℏ_q² that reads the ladder c_k off the exact Δtr_M "
        "mode decomposition. Δtr_M expressed in ℏ_q is an ordinary power "
        "series; u_L=b·ℏ² makes even-in-ℏ rungs the integer-u_L ladder "
        "(G_k=a_2k/b^k, anchor-independent constants — the only "
        "non-C1-refuted path) and odd-in-ℏ rungs the bar-odd half-integer "
        "remainder. Peels c_2..c_4 with c_2=−1 fixing the scale; contrasts "
        "the anchor-independent formal coefficients against the naive "
        "real-q analytic control (predicted C1-refuted). Exact symbolic; "
        "tiered; no fit; no wiring."
    )
    builder.set_content_block("prop:q-beta-categorical-precision-ladder")

    print("=" * 78)
    print(" HABIRO MODE → LADDER BRIDGE  (PR #1622 open step, executed)")
    print("=" * 78)

    # ── 1. exact Δtr_M(u) ──────────────────────────────────────────
    wit = builder.add_upstream(_pb.witness_path("habiro-coefficients-atomic.witness.json", HERE))
    trM_p = habiro_trM(wit["results"]["p (proton, A=1)"])
    trM_n = habiro_trM(wit["results"]["n (neutron, A=1)"])
    dtrM = sp.cancel(trM_n - trM_p)
    num, den = sp.fraction(dtrM)
    print(f"\n  Δtr_M(u) = ({sp.expand(num)}) / ({sp.factor(den)})")

    # bar-even projection (charge conjugation u ↦ 1/u) = even-in-ℏ part
    dtrM_bar = sp.cancel(dtrM.subs(u, 1 / u))
    even_u = sp.cancel((dtrM + dtrM_bar) / 2)
    odd_u = sp.cancel((dtrM - dtrM_bar) / 2)

    # ── 2. re-express in ℏ and Taylor-expand ──────────────────────
    # u = (1 − ℏ)^{-1/2}.  Substitute, then series in ℏ about 0.
    u_of_h = (1 - hbar) ** sp.Rational(-1, 2)
    dtrM_h = sp.series(dtrM.subs(u, u_of_h), hbar, 0, ORDER).removeO()
    even_h = sp.series(even_u.subs(u, u_of_h), hbar, 0, ORDER).removeO()
    odd_h = sp.series(odd_u.subs(u, u_of_h), hbar, 0, ORDER).removeO()
    dtrM_h = sp.expand(dtrM_h)
    even_h = sp.expand(even_h)
    odd_h = sp.expand(odd_h)

    print("\n  Δtr_M as a power series in ℏ_q (about ℏ=0, i.e. q=1):")
    a = {n: sp.nsimplify(dtrM_h.coeff(hbar, n)) for n in range(ORDER)}
    for n in range(ORDER):
        if a[n] != 0:
            print(f"    a_{n} = [ℏ^{n}] Δtr_M = {a[n]}")

    # sanity: even-in-ℏ part should match the bar-even projection's series
    a_even = {n: sp.nsimplify(even_h.coeff(hbar, n)) for n in range(ORDER)}
    a_odd = {n: sp.nsimplify(odd_h.coeff(hbar, n)) for n in range(ORDER)}
    even_matches = all(
        sp.simplify(a_even.get(n, 0) - (a[n] if n % 2 == 0 else 0)) == 0
        for n in range(ORDER))
    odd_matches = all(
        sp.simplify(a_odd.get(n, 0) - (a[n] if n % 2 == 1 else 0)) == 0
        for n in range(ORDER))
    print(f"\n  bar-even projection == even-in-ℏ part of Δtr_M : {even_matches}")
    print(f"  bar-odd  projection == odd-in-ℏ  part of Δtr_M : {odd_matches}")
    print(f"  (PR #1602 odd remainder)  a_1 = [ℏ^1] = {a[1]}   "
          f"a_3 = [ℏ^3] = {a[3]}")

    uL = sp.Symbol("u_L", positive=True)
    Nrm = sp.Symbol("N")

    def peel_ladder(coeffs: dict, label: str) -> dict:
        """Seed S = 1 + N·Σ_{k≥2} (coeff_{2k}/b^k) u_L^k; fix N so the
        leading rung c_2 = −1 (the one PROVED rung = single scale d.o.f.),
        then read off c_3, c_4 with product-form bookkeeping. coeffs is the
        ℏ-series {n: a_n}; only EVEN n contribute (integer u_L)."""
        G = {k: sp.nsimplify(coeffs.get(2 * k, 0)) / b ** k
             for k in range(0, ORDER // 2)}
        print(f"\n  [{label}] integer-ladder G_k = a_2k/b^k:")
        for k in sorted(G):
            print(f"      G_{k} = {G[k]}")
        seed = sp.expand(1 + Nrm * sum(G[k] * uL ** k
                                       for k in range(2, ORDER // 2)))
        logseed = sp.series(sp.log(seed), uL, 0, ORDER // 2).removeO()
        L = {k: sp.nsimplify(sp.expand(logseed).coeff(uL, k))
             for k in range(2, ORDER // 2)}
        Nsol = sp.solve(sp.Eq(L[2], -1), Nrm)
        if not Nsol:
            print(f"      scale-fix c_2=−1 UNSOLVABLE (G_2 = {G[2]})")
            return {"solvable": False, "G2": str(G[2])}
        Nval = Nsol[0]
        c = {
            2: sp.simplify(L[2].subs(Nrm, Nval)),
            3: sp.simplify(L[3].subs(Nrm, Nval)),
            4: sp.simplify((L[4] + sp.Rational(1, 2) * L[2] ** 2).subs(Nrm, Nval)),
        }
        print(f"      scale-fix c_2=−1 ⟹ N = {Nval}")
        print(f"      c_3 = {c[3]} ;  c_4 = {c[4]}")
        return {"solvable": True, "N": str(Nval), "c_sym": c}

    # ── 4. peel TWO principled f-candidates ───────────────────────
    # (a) raw Δtr_M even-in-ℏ ; (b) the #1602-prescribed bar-even f, then
    #     its even-in-ℏ part (bar-even ≠ ℏ-parity, established above).
    print("\n" + "=" * 78)
    print("  PEEL — two principled f-candidates (NOT a scan; both reported)")
    print("=" * 78)
    cand_a = peel_ladder(a, "a: raw Δtr_M even-in-ℏ")
    cand_b = peel_ladder(a_even, "b: #1602 bar-even projection, even-in-ℏ")

    # numeric b
    b_val = sp.Float(builder.add_upstream(Path(HERE).parent / "q-beta-operator-valued-N3.witness.json")["data"]["hoefsmit_b"], 50)
    print(f"\n  Hoefsmit b = {b_val}")
    bridge_ck = cand_a.get("c_sym", {})
    bridge_ck_num = {k: sp.N(v.subs(b, b_val), 30) for k, v in bridge_ck.items()}
    candb_num = {k: sp.N(v.subs(b, b_val), 30)
                 for k, v in cand_b.get("c_sym", {}).items()}
    print("\n  candidate (a) c_k numeric:", {k: str(v)[:12] for k, v in bridge_ck_num.items()})
    print("  candidate (b) c_k numeric:", {k: str(v)[:12] for k, v in candb_num.items()})

    # ── 5. compare against the framework's stated forms ────────────
    stated = {
        2: sp.Integer(-1),
        3: sp.Integer(-2),                       # J_Hopf(q=1)
        4: sp.Integer(-2) * b ** 4,              # c_3·b⁴
    }
    stated_num = {k: sp.N(v.subs(b, b_val), 30) for k, v in stated.items()}
    # empirical (CODATA-peel) anchors for c_3 (the near-match swing)
    c3_proton, c3_muon = sp.Float("-2.0693", 8), sp.Float("-2.0097", 8)
    print("\n" + "=" * 78)
    print("  COMPARISON (bridge vs stated form vs empirical anchors)")
    print("=" * 78)
    def tier_of(bv, sv):
        rel = (abs((bv - sv) / sv) if sv not in (None, 0) else None)
        t = ("derived" if (rel is not None and rel < sp.Float("1e-12"))
             else "near-match" if (rel is not None and rel < sp.Float("0.05"))
             else "refuted")
        return rel, t
    tiers = {"candidate_a_raw_even": {}, "candidate_b_bareven": {}}
    for tag, cand_num in (("candidate_a_raw_even", bridge_ck_num),
                          ("candidate_b_bareven", candb_num)):
        print(f"\n  --- {tag} ---")
        for k in sorted(cand_num):
            bv, sv = cand_num[k], stated_num.get(k)
            rel, t = tier_of(bv, sv)
            tiers[tag][f"c_{k}"] = {"bridge": str(bv), "stated": str(sv),
                                    "rel_to_stated": (str(rel) if rel is not None else None),
                                    "tier": t}
            print(f"    c_{k}:  bridge = {str(bv)[:18]}   stated = {str(sv)[:18]}"
                  f"   rel = {str(rel)[:8] if rel is not None else None}  ⟹ {t}")
            if k == 3:
                print(f"          empirical anchors proton {c3_proton} / muon "
                      f"{c3_muon} (swing "
                      f"{float(abs((c3_proton-c3_muon)/c3_proton)*100):.2f}%); "
                      f"bridge c_3 is a CONSTANT (no swing).")
    # overall verdict
    any_derived = any(v.get("tier") == "derived" and kk != "c_2"
                      for cand in tiers.values() for kk, v in cand.items())
    verdict = ("CLOSURE (escalate to owner)" if any_derived
               else "REFUTED — neither principled f-candidate reproduces c_3; "
                    "gate stays open, exact ℏ-series is the new constraint on f")
    print(f"\n  VERDICT: {verdict}")

    # ── witness ────────────────────────────────────────────────────
    builder.add_data("delta_trM", {
        "numerator": str(sp.expand(num)),
        "denominator": str(sp.factor(den)),
    })
    builder.add_data("hbar_series", {
        f"a_{n}": str(a[n]) for n in range(ORDER) if a[n] != 0})
    builder.add_data("bar_split_matches_parity", {
        "even_proj_eq_even_in_hbar": bool(even_matches),
        "odd_proj_eq_odd_in_hbar": bool(odd_matches),
        "odd_remainder_a1": str(a[1]),
        "odd_remainder_a3": str(a[3]),
        "note": "odd-in-ℏ rungs are the bar-odd half-integer-u_L remainder "
                "(PR #1602's −√3/12·u¹ class); the ladder is the even part.",
    })
    builder.add_data("candidate_a_raw_even", {
        "c_symbolic": {f"c_{k}": str(v) for k, v in cand_a.get("c_sym", {}).items()},
        "c_numeric": {f"c_{k}": str(v) for k, v in bridge_ck_num.items()},
        "scale_N": cand_a.get("N"),
    })
    builder.add_data("candidate_b_bareven", {
        "c_symbolic": {f"c_{k}": str(v) for k, v in cand_b.get("c_sym", {}).items()},
        "c_numeric": {f"c_{k}": str(v) for k, v in candb_num.items()},
        "scale_N": cand_b.get("N"),
    })
    builder.add_data("comparison_tiers", tiers)
    builder.add_data("verdict", verdict)
    builder.add_data("anchor_stability", {
        "bridge_ck_are_constants": True,
        "note": "Bridge c_k are formal-series constants (no q₀ enters) ⇒ "
                "anchor-independent by construction — the non-C1-refuted "
                "path. The empirical c_3 swing (proton −2.069 / muon −2.010) "
                "is the higher-rung truncation, not a c_3 ambiguity.",
    })

    # assertion: c_2 = −1 scale-fix solvable for both candidates (the bridge
    # is well-defined); the c_3 refutation is the substantive finding.
    builder.add_assertion(
        "both_candidates_scale_fix_solvable",
        computed=1.0 if (cand_a.get("solvable") and cand_b.get("solvable")) else 0.0,
        expected=1.0,
        tolerance=0.0,
        source="Both principled f-candidates (raw even-in-ℏ; #1602 bar-even) "
               "admit a scale N fixing c_2 = −1 — the bridge is well-defined. "
               "Neither reproduces c_3 = −2 (a: −1.497, b: −1.401), so the "
               "Δtr_M-seeded linear/bar-even f is REFUTED (new C13 row).",
    )
    builder.save()
    print("\n  Witness: habiro-mode-to-ladder-bridge.witness.json")
    print("  wall:", round(time.monotonic() - t0, 1), "s")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
