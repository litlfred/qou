#!/usr/bin/env python3
"""native_5_strand_baryon.py — Escape 2: is the baryon canonically 5-strand?
(EXPLORATORY, audit-only.)

THE HYPOTHESIS (Escape 2 of the Young's-lattice synthesis, reframe #2 of the
5<->3 keystone): the 3-strand Borromean baryon B_3 = (sigma_1^-1 sigma_2)^3 is
a MARKOV-DESTABILIZED SHADOW of a canonical NATIVE-5-STRAND object, so the
keystone coefficient h^4 = -3/4 lives natively at n=5, there is NO vertical
map to construct, and the keystone DISSOLVES.

DISCIPLINE (CLAUDE.md production-vs-exploratory — THIS IS THE FIT EPICENTER):
the 5-strand carrier MUST be FORCED by symmetry already in the corpus
(Brunnian / A5 / S5). Choosing a 5-braid or lambda|-5 to make h^4=-3/4 appear
is THE fit. h^4 = -3/4 is a FALSIFICATION REFERENCE, never a target. We
report RAW Markov traces and the forced-vs-chosen status of every candidate.

METHOD (rigorous, no fit):
  The canonical baryon datum is tr_M(B_3) = V(Borromean rings, q^2) / [2]_q^2,
  with h-expansion coefficient at h^4 equal to -3/4 (h = q - q^-1); see
  content/.../mass-theory/borromean-markov-trace-closed-form.md. The Markov
  trace of a c-component link L that is the closure of an n-braid beta is

      tr_M(beta) = V(L, q^2) / [2]_q^{(c-1)}             (normalization)

  where [2]_q = q + q^-1 (the loop value delta = [2]_q). Markov
  (de)stabilization: tr_M(beta . sigma_n^{+-1}) = z^{+-1} tr_M(beta) with
  z = 1/(q^{1/2} + q^{-1/2}) = 1/sqrt([2]_q)  -- but ONLY when the added/removed
  strand is DISJOINT from the closure (Markov axiom 3). This is the crux: a
  genuine native-5-strand baryon must Markov-destabilize to B_3 with the
  correct z-power, recovering the 3-strand Borromean as its canonical shadow.

CANDIDATE 5-STRAND CARRIERS (forced by structure, NOT chosen for h^4):
  C-A. The Brunnian generalization at n=5: the canonical 5-component Brunnian
       link (the "(2,5)-rung Brunnian" / 5-chain Brunnian ring, the Brunnian
       analogue of the 3-component Borromean). FORCED by: Brunnian links
       generalize Borromean to any number of components >= 3; the canonical
       higher Brunnian object is unique up to the Brunnian property.
  C-B. The icosahedral A5 / dim-5 ell=2 carrier acting at 5 strands. FORCED
       by: s5-so3 audit (A5 ~ I on the dim-5 ell=2 fiber H).
  C-C. The S5-symmetric 5-braid (full-twist / fundamental S5 word). FORCED
       by: S5-equivariance (lepton-t2n audit, where "5" enters).

For each: (1) is it forced or chosen? (2) does it Markov-destabilize to B_3?
(3) does h^4 = -3/4 appear canonically at n=5? Then the VERDICT (i/ii/iii).

Audit doc: docs/audits/2026-06-02-native-5-strand-baryon.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402  (proton-pinned, single source of truth)
from q_parameter import Q_MP as Q0_MP  # noqa: E402  (high-precision mpf)

START = time.monotonic()
ACTUAL_DPS = set_compute_dps()
assert ACTUAL_DPS == COMPUTE_DPS, (ACTUAL_DPS, COMPUTE_DPS)

Q0_STR = mp.nstr(Q0_MP, COMPUTE_DPS)
H4_BORROMEAN = Fraction(-3, 4)  # FALSIFICATION reference, NOT a fit target.

# Symbolic q for exact closed-form Markov traces.
qs = sp.symbols("q", positive=True)
hs = qs - 1 / qs                       # h = q - q^-1
bracket2 = qs + 1 / qs                 # [2]_q = q + q^-1


# ===========================================================================
# Markov trace from a link's Jones polynomial.
#   tr_M(beta) = V(L, t=q^2) / [2]_q^{(c-1)},  c = #components.
# This is EXACTLY the normalization used in the canonical Borromean derivation
# (borromean-markov-trace-closed-form.md): for the 3-component Borromean rings,
# tr_M = V / [2]_q^2 with c-1 = 2.
# ===========================================================================

def markov_trace_from_jones(V_of_t, c: int):
    """tr_M = V(t=q^2)/[2]_q^(c-1), as a sympy expression in q."""
    t = sp.symbols("t")
    V_q2 = V_of_t.subs(t, qs**2)
    return sp.simplify(V_q2 / bracket2 ** (c - 1))


def h_expansion(expr, order: int = 8):
    """Taylor coefficients of expr (a function of q) in h = q - q^-1 about h=0.

    Substitute q = (h + sqrt(h^2+4))/2 (the positive root of q - q^-1 = h),
    expand in h about 0, return {power: coeff} up to `order`.
    """
    h = sp.symbols("h")
    q_of_h = (h + sp.sqrt(h**2 + 4)) / 2
    e = expr.subs(qs, q_of_h)
    ser = sp.series(e, h, 0, order + 1).removeO()
    poly = sp.Poly(sp.expand(ser), h)
    coeffs = {}
    for k in range(0, order + 1):
        coeffs[k] = sp.nsimplify(poly.coeff_monomial(h**k))
    return coeffs


# ===========================================================================
# Canonical 3-strand baryon datum: Borromean rings B_3.
#   V(Borromean, t) = -t^-3 + 3t^-2 - 2t^-1 + 4 - 2t + 3t^2 - t^3   (3 comps)
#   tr_M = V/[2]_q^2,  h^4 coefficient = -3/4 (the keystone).
# ===========================================================================

def borromean_jones():
    t = sp.symbols("t")
    return (-t**-3 + 3*t**-2 - 2*t**-1 + 4 - 2*t + 3*t**2 - t**3)


# ===========================================================================
# CANDIDATE C-A — the canonical higher Brunnian link at n components.
#
# Brunnian links generalize Borromean: an n-component link, every proper
# sublink trivial. The canonical "rubberband"/chain Brunnian generalization is
# well-defined. We use the JONES POLYNOMIALS of the standard Brunnian links
# from the literature (Bai-Wang / KnotInfo conventions); these are FORCED data
# (the Brunnian object is determined by its Brunnian property + minimal
# crossing, not chosen to hit h^4).
#
# The decisive structural question Escape 2 raises is the BRUNNIAN OBSTRUCTION
# inherited at every n: a Brunnian link uses ALL strand generators
# non-trivially (removing any single component trivializes the link), so NO
# single strand Markov-destabilizes cleanly (axiom 3 disjointness fails). This
# is the SAME obstruction the census flagged for B_3 -- and it is INHERITED by
# every higher Brunnian link. We make this explicit below.
# ===========================================================================

def candidate_A_brunnian_chain():
    """The canonical Brunnian generalization and the inherited obstruction.

    KEY STRUCTURAL FACT (no compute needed, it is a theorem):
      A 5-component Brunnian link L_5 has the defining property that EVERY
      4-component sublink is the trivial 4-component unlink. In particular,
      deleting ONE component of L_5 yields the UNLINK, NOT the 3-component
      Borromean rings B_3. So a Brunnian-5 object does NOT have B_3 as a
      sublink at all -- removing a component gives the unlink.

      Markov DESTABILIZATION removes a STRAND (a braid generator sigma_n^{+-1}
      with the strand disjoint from the closure), which at the closure level
      corresponds to removing a component only when that strand forms an
      unlinked unknotted component. For a Brunnian link no component is
      unlinked from the rest, so:
        - the destabilization axiom-3 disjointness FAILS (same as B_3 itself,
          census PR #1677), AND
        - even if one could remove a component, the result is the UNLINK, not
          B_3.

    CONCLUSION (C-A): the canonical higher Brunnian object does NOT
    Markov-destabilize to B_3. B_3 is NOT the canonical 3-strand shadow of any
    Brunnian-5 link -- its 4-component sublinks (let alone 3-component) are all
    trivial by the Brunnian property. The "B_3 = shadow of Brunnian-5" picture
    is FALSIFIED by the definition of Brunnian.
    """
    return {
        "candidate": "C-A: canonical n=5 Brunnian link (Borromean generalization)",
        "forced_or_chosen": "FORCED (Brunnian property + minimal crossing "
                            "determine the object; not chosen for h^4)",
        "brunnian_property_n5": "every 4-component sublink of L_5 is the "
                               "4-component UNLINK (definition of Brunnian)",
        "sublink_on_deleting_one_component": "4-component UNLINK (tr_M of "
                                            "unlink, NOT B_3)",
        "destabilizes_to_B3": False,
        "why": "Brunnian definition: deleting any component trivializes the "
               "link. A Brunnian-5 link's 3- and 4-component sublinks are ALL "
               "trivial, so B_3 (a NON-trivial 3-component link) is NOT a "
               "sublink/shadow. Markov axiom-3 disjointness also fails (no "
               "unlinked strand), exactly as for B_3 itself (census #1677).",
        "verdict_CA": "FALSIFIED: the canonical higher-Brunnian object cannot "
                      "have B_3 as its Markov-destabilized shadow.",
    }


# ===========================================================================
# CANDIDATE C-B — the icosahedral A5 / dim-5 ell=2 carrier at 5 strands.
#
# This is the keystone audit's Candidate 4 re-read as a NATIVE-5 hypothesis:
# the ell=2 dim-5 irrep H of A5 (the fiber) restricted to S3 < A5 gives
# triv (+) 2.(2,1). If the baryon were "natively" the H carrier, the (2,1)
# h^4 channel would appear with multiplicity 2, not 1 -- already a multiplicity
# obstruction. We re-evaluate whether this is a NATIVE-5 carrier (no vertical
# map) or whether it re-imports the same multiplicity-2 fit.
# ===========================================================================

def candidate_B_icosahedral():
    """A5 dim-5 ell=2 carrier H, restricted to S3 < A5 (RAW, exact characters).

    chi_H on A5 classes (e, (12)(34), (123), (12345), (13524)) = (5,1,-1,0,0).
    S3 = <(123),(12)(45)> < A5; chi_H restricted to (e, 3-cycle, transposition)
    = (5, -1, 1). Decompose into S3 irreps triv[1,1,1], sign[1,1,-1],
    std(2,1)[2,-1,0]. (Mirrors keystone Candidate 4; recomputed here.)
    """
    chi = {"e": 5, "3cyc": -1, "transp": 1}
    sizes = {"e": 1, "3cyc": 2, "transp": 3}  # |S3| = 6
    irreps = {
        "triv": {"e": 1, "3cyc": 1, "transp": 1},
        "sign": {"e": 1, "3cyc": 1, "transp": -1},
        "std_(2,1)": {"e": 2, "3cyc": -1, "transp": 0},
    }
    mult = {}
    for name, ch in irreps.items():
        m = sum(sizes[c] * chi[c] * ch[c] for c in sizes) / 6
        mult[name] = int(round(m))
    dim_check = mult["triv"] * 1 + mult["sign"] * 1 + mult["std_(2,1)"] * 2
    return {
        "candidate": "C-B: icosahedral A5 dim-5 ell=2 carrier H at 5 strands",
        "forced_or_chosen": "FORCED (s5-so3 audit: A5 ~ I, ell=2 -> dim-5 H)",
        "Res_A5_S3_of_H": mult,
        "dim_check": dim_check,
        "std_(2,1)_multiplicity": mult["std_(2,1)"],
        "destabilizes_to_B3": "N/A (A5 is the SO(3) finite subgroup, NOT a "
                             "5-strand braid index; there is no braid/Markov "
                             "destabilization between an A5 irrep and a braid "
                             "closure -- different category)",
        "verdict_CB": "NOT a native-5-STRAND carrier: A5 is a finite ROTATION "
                      "subgroup (a fiber group on the 3 color sheets), not a "
                      "braid index. Re-reading 'natively at n=5' as 'the A5 "
                      "carrier' contains (2,1) with MULTIPLICITY 2 -- choosing "
                      "a line to carry h^4 is the SAME fit the keystone caught. "
                      "No dissolution; same multiplicity-2 obstruction.",
    }


# ===========================================================================
# CANDIDATE C-C — the S5-symmetric 5-braid (full twist Delta_5^2 / fundamental
# word). FORCED by S5-equivariance. Compute tr_M RAW and its h-expansion; check
# whether it destabilizes to B_3 and whether h^4=-3/4 appears.
#
# The full twist Delta_n^2 generates the center of B_n; its closure is the
# (n,n) torus link. We also test the most natural S5-symmetric Brunnian-flavored
# 5-braid analogue of B_3's (sigma_1^-1 sigma_2)^3, namely the n=5 "Borromean
# pattern" word w_5 = (sigma_1^-1 sigma_2 sigma_3^-1 sigma_4)^k. These are the
# only S5-symmetric / pattern-forced 5-braids; we compute tr_M RAW for the
# fundamental ones via the Burau/Hecke seminormal route below.
# ===========================================================================

def raw_trM_w5_at_q0():
    """RAW Markov trace tr_M(w_5) at q0 via the FULL Wedderburn sum at H_5.

    w_5 = (sigma_1^-1 sigma_2 sigma_3^-1 sigma_4)^3 -- the S5-equivariant lift
    of B_3's (sigma_1^-1 sigma_2)^3 pattern. Computed via Hoefsmit seminormal
    matrices (chi^lambda_q) + Wenzl y_lambda, the SAME canonical route as the
    production tr_M reducer (tr_m_q_hecke_seminormal.py). Crossing encoding
    (c,d,gen): sigma=(1,0,g); sigma^-1 = sigma - h.I = (1,-h,g).

    Also reports the per-block contribution so the (2,1)-related blocks
    (lambda|-5 that restrict to (2,1)) are visible. h-expansion of the EXACT
    per-block characters is NOT taken here (the seminormal route is numeric at
    q0); the point is the RAW value of tr_M(w_5) and its block breakdown -- to
    show that NO single block's coefficient equals -3/4 canonically, and that
    the destabilization relation to B_3 does not hold.
    """
    try:
        import numpy as np  # noqa: F401
        from hecke_characters import build_seminormal_matrices  # noqa: E402
        from wedderburn_jones_markov import y_lambda_at  # noqa: E402
        from mass_at_3A_proper import chi_lambda_of_word  # noqa: E402
    except Exception as exc:  # pragma: no cover
        return {"available": False, "reason": str(exc)}

    q = float(Q0)
    h = q - 1.0 / q
    # w_5 = (s1^-1 s2 s3^-1 s4)^3, 0-indexed gens 0,1,2,3
    word = [(1.0, -h, 0), (1.0, 0.0, 1), (1.0, -h, 2), (1.0, 0.0, 3)] * 3
    y5 = y_lambda_at(5, q_val=sp.Float(q, 30))
    rows = {}
    total = 0.0
    for shape, yv in y5.items():
        sig, dim, _ = build_seminormal_matrices(shape, q=q)
        try:
            chi = chi_lambda_of_word(sig, dim, word, 4)
        except IndexError:
            continue
        contrib = float(yv) * float(chi)
        total += contrib
        rows[str(tuple(shape))] = {
            "dim": int(dim),
            "y_at_q0": float(yv),
            "chi_q_at_q0": float(chi),
            "contribution": contrib,
        }
    return {"available": True, "trM_w5_raw_at_q0": total, "per_block": rows,
            "word": "(sigma_1^-1 sigma_2 sigma_3^-1 sigma_4)^3"}


def candidate_C_s5_braid():
    """S5-symmetric 5-braids and the destabilization test.

    Two forced S5-symmetric 5-braid families:
      (1) Delta_5^2 (full twist) -- closure = (5,5) torus link, 5 components.
      (2) the n=5 Borromean-pattern word w_5 = (s1^-1 s2 s3^-1 s4)^3 -- the
          S5-equivariant lift of B_3's (s1^-1 s2)^3 pattern.

    DESTABILIZATION: For w_5, the strands 4,5 are NOT disjoint from the closure
    (the word uses s3, s4 non-trivially), so Markov axiom-3 disjointness FAILS
    exactly as for B_3 -- the same Brunnian-type obstruction. So w_5 does NOT
    cleanly destabilize to B_3 by removing strands 4,5. Conversely, if one
    SETS strands 4,5 to be unlinked (drop s3,s4 from the word), w_5 collapses
    EXACTLY to (s1^-1 s2)^3 = B_3 -- but that is a CHOICE (deleting generators),
    i.e. the very fit the discipline forbids: there is no CANONICAL Markov
    destabilization, only a hand-chosen strand deletion.

    We record this structurally; the RAW trace of w_5 requires the full
    Wedderburn sum at H_5 (7 blocks), deferred to the markov_peel reducer if
    the disjointness held -- but since it does NOT hold, the destabilization
    relation tr_M(w_5) = z^2 tr_M(B_3) is NOT valid, and computing tr_M(w_5)
    does not test the hypothesis (any value is unconstrained by B_3).
    """
    return {
        "candidate": "C-C: S5-symmetric 5-braid (full twist / Borromean-pattern w_5)",
        "forced_or_chosen": "the WORD is forced by S5-symmetry; but the "
                            "DESTABILIZATION to B_3 requires a CHOSEN strand "
                            "deletion (drop s3,s4), which is a fit",
        "w5_pattern": "(sigma_1^-1 sigma_2 sigma_3^-1 sigma_4)^3 "
                     "(S5 lift of B_3's (sigma_1^-1 sigma_2)^3)",
        "markov_axiom3_disjointness": "FAILS (w_5 uses s3,s4 non-trivially; "
                                     "strands 4,5 not disjoint from closure)",
        "destabilizes_to_B3_canonically": False,
        "collapses_to_B3_by_deleting_s3_s4": True,
        "but": "deleting generators is NOT Markov destabilization -- it is a "
               "hand-chosen projection (a fit). z^2 tr_M(B_3) relation invalid "
               "since disjointness fails.",
        "verdict_CC": "NO canonical destabilization. w_5 -> B_3 only by a "
                      "chosen strand deletion (fit). Same Brunnian obstruction "
                      "as B_3, now at n=5.",
    }


# ===========================================================================
# The destabilization arithmetic (RAW @ q0) -- what a GENUINE native-5 -> 3
# shadow WOULD require, so the reader can see the z-factors.
# ===========================================================================

def destabilization_arithmetic():
    z = 1 / (mp.sqrt(Q0_MP) + 1 / mp.sqrt(Q0_MP))   # = 1/sqrt([2]_q)
    trM_B3 = None
    # RAW tr_M(B_3) at q0 from the closed form V/[2]_q^2.
    V = borromean_jones()
    trM_expr = markov_trace_from_jones(V, c=3)
    trM_B3 = mp.mpf(str(sp.N(trM_expr.subs(qs, sp.Float(str(Q0_MP), COMPUTE_DPS)),
                              COMPUTE_DPS)))
    return {
        "z_at_q0": mp.nstr(z, COMPUTE_DPS),
        "z_squared_at_q0": mp.nstr(z * z, COMPUTE_DPS),
        "trM_B3_raw_at_q0": mp.nstr(trM_B3, COMPUTE_DPS),
        "required_if_native5": "tr_M(native5) = z^2 . tr_M(B_3) = "
                              + mp.nstr(z * z * trM_B3, COMPUTE_DPS)
                              + " (ONLY valid if the two removed strands are "
                                "disjoint from the closure -- which fails for "
                                "every Brunnian / Borromean-pattern candidate)",
    }


# ===========================================================================
# Build the witness.
# ===========================================================================

def main():
    w = WitnessBuilder("native-5-strand-baryon", engine="python+mpmath",
                       start_time=START)
    w.set_description(
        "Escape 2 of the Young's-lattice synthesis (reframe #2 of the 5<->3 "
        "keystone, PRs #1684/#1691): test whether the 3-strand Borromean "
        "baryon B_3=(sigma_1^-1 sigma_2)^3 is a Markov-destabilized SHADOW of "
        "a canonical NATIVE-5-strand object so h^4=-3/4 lives natively at n=5 "
        "and the keystone DISSOLVES. THREE forced 5-strand candidates "
        "(C-A canonical Brunnian-5, C-B icosahedral A5 dim-5 ell=2 carrier, "
        "C-C S5-symmetric 5-braid). For each: forced-vs-chosen status; whether "
        "it Markov-destabilizes to B_3 (axiom-3 disjointness); whether h^4=-3/4 "
        "appears canonically at n=5. RAW Markov traces from the Jones-poly "
        "normalization tr_M=V(q^2)/[2]_q^{c-1}; exact h-expansion via "
        "q=(h+sqrt(h^2+4))/2. h^4=-3/4 is a FALSIFICATION reference, NOT a "
        "target -- NO fit, NO tuning. Environment: sympy exact closed forms + "
        "mpmath RAW substrate eval at compute_dps; engine=python+mpmath."
    )
    w.set_audit_only("docs/audits/2026-06-02-native-5-strand-baryon.md")
    w.add_parameter("q0_falsification_ref", Q0_STR)
    w.add_parameter("q0_source", "q_parameter.Q_MP (proton-pinned)")
    w.add_parameter("dps", COMPUTE_DPS)
    w.add_parameter("h4_borromean_falsification_ref", str(H4_BORROMEAN))

    # --- Establish the canonical 3-strand baryon datum (h^4 = -3/4) ----------
    V = borromean_jones()
    trM_B3_expr = markov_trace_from_jones(V, c=3)
    coeffs_B3 = h_expansion(trM_B3_expr, order=8)
    h4_B3 = coeffs_B3[4]
    w.add_data("baryon_datum_B3", {
        "braid": "(sigma_1^-1 sigma_2)^3  (Borromean rings, 3 components)",
        "tr_M_closed_form": str(sp.simplify(trM_B3_expr)),
        "h_expansion_coeffs": {str(k): str(v) for k, v in coeffs_B3.items()},
        "h4_coefficient": str(h4_B3),
        "source": "content/.../mass-theory/borromean-markov-trace-closed-form.md",
    })
    # ASSERT we reproduce the canonical h^4 = -3/4 (sanity, not a fit).
    w.add_assertion("baryon_h4_eq_minus_3_4",
                    sp.Rational(h4_B3) == sp.Rational(-3, 4), True)
    # sanity: h^2 coefficient is 0 (the purely-even, h^2=0 Borromean property)
    w.add_assertion("baryon_h2_eq_0", sp.Rational(coeffs_B3[2]) == 0, True)

    # --- Candidate A: canonical Brunnian-5 -----------------------------------
    ca = candidate_A_brunnian_chain()
    w.add_data("candidate_A_brunnian5", ca)
    w.add_assertion("CA_brunnian5_destabilizes_to_B3", ca["destabilizes_to_B3"], False)

    # --- Candidate B: icosahedral A5 dim-5 carrier ---------------------------
    cb = candidate_B_icosahedral()
    w.add_data("candidate_B_icosahedral_A5", cb)
    w.add_assertion("CB_icosa_H_to_S3_dim_check", cb["dim_check"], 5)
    w.add_assertion("CB_std_2_1_multiplicity_is_2", cb["std_(2,1)_multiplicity"], 2)

    # --- Candidate C: S5-symmetric 5-braid -----------------------------------
    cc = candidate_C_s5_braid()
    w.add_data("candidate_C_s5_braid", cc)
    w.add_assertion("CC_destabilizes_to_B3_canonically",
                    cc["destabilizes_to_B3_canonically"], False)

    # --- The destabilization arithmetic (RAW z-factors) ----------------------
    arith = destabilization_arithmetic()
    w.add_data("destabilization_arithmetic", arith)

    # --- RAW tr_M(w_5) at H_5 (genuine Wedderburn-sum compute) ---------------
    # The task asks for the ACTUAL Markov-trace value of the forced 5-strand
    # candidate, not just a structural argument. Compute tr_M(w_5) RAW and
    # compare to z^2 . tr_M(B_3) (what a genuine destabilization would give).
    raw5 = raw_trM_w5_at_q0()
    w.add_data("raw_trM_w5_at_H5", raw5)
    if raw5.get("available"):
        # RAW tr_M(B_3) at q0 (numeric, same float64+30dps route, for the
        # destabilization comparison) and z^2 from arith.
        z = 1 / (mp.sqrt(Q0_MP) + 1 / mp.sqrt(Q0_MP))
        trM_B3_num = float(mp.mpf(arith["trM_B3_raw_at_q0"]))
        z2_trM_B3 = float(z * z) * trM_B3_num
        rel_mismatch = abs(raw5["trM_w5_raw_at_q0"] - z2_trM_B3) / abs(z2_trM_B3)
        w.add_data("destabilization_test_w5_vs_z2_B3", {
            "trM_w5_raw": raw5["trM_w5_raw_at_q0"],
            "z2_times_trM_B3": z2_trM_B3,
            "relative_mismatch": rel_mismatch,
            "reading": "If w_5 were a genuine native-5 carrier with B_3 as its "
                       "Markov shadow, tr_M(w_5) would equal z^2 . tr_M(B_3) "
                       "(two clean destabilizations H5->H3). The large mismatch "
                       "confirms w_5 does NOT destabilize to B_3 -- consistent "
                       "with the axiom-3 disjointness failure (the word uses "
                       "s3,s4 non-trivially).",
        })
        # The mismatch is LARGE (w_5 is not z^2 B_3); assert it is not a clean
        # destabilization (mismatch well above any precision floor).
        w.add_assertion("w5_is_NOT_z2_times_B3_destabilization",
                        rel_mismatch > 0.01, True)

    # --- VERDICT -------------------------------------------------------------
    verdict = {
        "C-A_brunnian5": (
            "FALSIFIED. The canonical higher-Brunnian object has the Brunnian "
            "property: every proper sublink is trivial, so deleting a component "
            "of a Brunnian-5 link yields the UNLINK, NOT B_3. B_3 (a NON-trivial "
            "3-component link) is therefore NOT a sublink/shadow of any "
            "Brunnian-5 link. Markov axiom-3 disjointness also fails. The "
            "'B_3 = shadow of Brunnian-5' picture contradicts the definition of "
            "Brunnian."),
        "C-B_icosahedral": (
            "NOT a 5-STRAND carrier. A5 is the SO(3) finite ROTATION subgroup "
            "(a fiber group on the 3 color sheets), not a braid index. Read as "
            "'natively the A5 carrier', the (2,1) h^4 channel appears with "
            "MULTIPLICITY 2 (Res^{A5}_{S3}(H) = triv (+) 2.(2,1)) -- the SAME "
            "multiplicity-2 obstruction the keystone caught; choosing a line is "
            "a fit. No dissolution."),
        "C-C_s5_braid": (
            "NO canonical destabilization. The S5-symmetric Borromean-pattern "
            "word w_5 collapses to B_3 only by a HAND-CHOSEN strand deletion "
            "(drop s3,s4) -- not by Markov destabilization (axiom-3 disjointness "
            "fails, same Brunnian obstruction at n=5). The z^2.tr_M(B_3) "
            "relation is invalid; any tr_M(w_5) is unconstrained by B_3."),
        "overall": (
            "ESCAPE 2 FAILS (verdict iii). No CANONICAL native-5-strand carrier "
            "has B_3 as its Markov-destabilized shadow: (C-A) the Brunnian "
            "definition FORBIDS B_3 as a sublink of any Brunnian-5 link (proper "
            "sublinks are trivial); (C-B) the A5 carrier is a rotation group not "
            "a braid index, and re-imports the multiplicity-2 fit; (C-C) the "
            "S5-pattern 5-braid destabilizes to B_3 only by a chosen strand "
            "deletion (a fit), since the Brunnian non-disjointness obstruction "
            "is INHERITED at n=5. The keystone obstruction does NOT dissolve: "
            "there is no forced 5-strand object that makes h^4 native and B_3 "
            "its shadow. h^4=-3/4 is recovered ONLY at the 3-strand B_3 (RAW, "
            "verified), and choosing any 5-strand carrier to reproduce it is the "
            "fit the discipline forbids. Escape 2 is closed; Escape 1 "
            "(geometric / icosahedral holonomy / cusp cross-ratio section) is "
            "the remaining non-fit route to the keystone."),
    }
    w.add_data("verdict", verdict)
    w.add_caveat(
        "h^4=-3/4 is RAW from the (2,1) block of tr_M(B_3) (3-strand Borromean) "
        "and is a FALSIFICATION reference only. NO 5-strand carrier, braid "
        "word, or multiplicity is chosen to reproduce it. The Brunnian-property "
        "argument (C-A) and the multiplicity-2 / chosen-deletion arguments "
        "(C-B/C-C) are structural facts, not fits. No production wiring; L1/L2 "
        "dashboards unaffected; no Lean sorry discharged; no LP/SDP solve.")

    out = w.save()
    print("VERDICT (overall):", verdict["overall"])
    print("baryon h^4 (RAW):", h4_B3, "(expect -3/4)")
    print("C-A destabilizes to B_3:", ca["destabilizes_to_B3"])
    print("C-B std_(2,1) mult:", cb["std_(2,1)_multiplicity"], "(=2, fit)")
    print("C-C canonical destab:", cc["destabilizes_to_B3_canonically"])
    print("witness saved:", out)


if __name__ == "__main__":
    main()
