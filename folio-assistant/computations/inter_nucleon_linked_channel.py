#!/usr/bin/env python3
"""Inter-nucleon LINKED channel: braid word, Markov trace, writhe (EXPLORATORY, audit-only).

Tests the single most-promising DERIVED lead of the knot-operator census
(docs/audits/2026-06-01-knot-operator-census-group-actions.md, PR #1677):
the inter-nucleon LINKED channel that escapes BOTH Borromean obstructions
(Brunnianness; writhe-0).

DERIVATION OF THE BRAID WORD (provenance, NOT a fit):
  The inter-nucleon arc at braid generator 3k+2 links two nucleon
  color-tube components (inter-nucleon-channel-color-tube.md). Per
  fermion-boson-knot-link.md, the framework's 2-component LINK sector is
  exactly the T(2,n)-even (Hopf) family: "two components, one winds +1 and
  the other -1 around the Reeb direction." The MINIMAL non-Brunnian
  2-component link is the Hopf link T(2,2) = sigma_1^2 (linking number 1).
  Chirality (matter/matter vs matter/antimatter) gives the sign:
    pp  ->  sigma_1^{+2}  = T(2,2)   positive Hopf link   (writhe +2, lk +1)
    nn  ->  sigma_1^{-2}  = T(2,-2)  negative (mirror)     (writhe -2, lk -1)
    pn  ->  sigma_1^{ 0}  = T(2,0)   2-component UNLINK     (writhe  0, lk  0)
  The single-generator production assignment (pp->sigma, nn->sigma^-1,
  pn->sigma_avg; writhe +1/-1/0 in the s5-so3 audit) is the LINKING-NUMBER
  shadow of this Hopf-link object: lk(Hopf^{+/-}) = +/-1 matches the
  production writhe-of-one-crossing, while the full link's writhe is +/-2.
  NO numeric is tuned to m_n-m_p, B_AME, hypercharge, or any h^k.

COMPUTES (RAW @ 60 dps, plus symbolic-in-q closed forms):
  1. The braid words (pp/nn/pn) + strand count + B_n + generators used.
  2. tr_M(rho(B)) = J_B(q) in H_2(q): symbolic closed form + value at q0,
     with the Wedderburn (2),(1,1) block decomposition.
  3. The writhe (pp=+2, nn=-2, pn=0) and the linking number (+1/-1/0);
     confirms non-Brunnian (a 2-sublink that is genuinely linked).
  4. Claim 1 -- Markov destabilization (the 5<->3 bridge): does sigma_1^2
     in H_2 destabilize via the disjoint-strand axiom-3 to H_1, and is the
     trace preserved? (sigma_1^2 is NOT a single sigma_{n-1}^{+-1}; tests
     destabilizability honestly.)
  5. Claim 2 -- U(1)_framing q^{w.c} at writhe pp=+2 / nn=-2; the pp/nn
     framing-phase difference vs PDG m_n-m_p (FALSIFICATION reference only).

Audit doc: docs/audits/2026-06-01-inter-nucleon-linked-channel.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

START = time.monotonic()
mp.mp.dps = 60

# Substrate q0 (proton-anchored). FALSIFICATION reference only -- not tuned.
Q0_STR = "1.10997859561220225731080831999100762523924148"
Q0 = mp.mpf(Q0_STR)

# PDG / CODATA falsification references (NOT fit targets).
M_N_MINUS_M_P_MEV = mp.mpf("1.29333236")   # m_n - m_p, PDG 2024 (MeV)
M_P_MEV = mp.mpf("938.27208816")            # proton mass, CODATA (MeV)


# ---------------------------------------------------------------------------
# Symbolic Hecke Markov trace in H_2(q).
# H_2(q) = <sigma_1 | (sigma_1 - q)(sigma_1 + q^-1) = 0>; two 1-dim irreps:
#   (2)    : sigma_1 |-> q       (symmetric channel, eigenvalue q)
#   (1,1)  : sigma_1 |-> -q^-1   (antisymmetric channel, eigenvalue -q^-1)
# CANONICAL Wenzl / Jones-Markov trace (mass-formula convention):
#   the unique trace with tr_M(1)=1 and tr_M(beta.sigma_n)= z*tr_M(beta),
#   z = 1/(q^{1/2}+q^{-1/2}).  Decomposing on the two 1-dim H_2 blocks:
#     tr_M(sigma_1^k) = w_(2)*q^k + w_(1,1)*(-q^-1)^k
#   where the Wenzl weights (w_(2), w_(1,1)) are FIXED by the two Markov
#   axioms tr_M(1)=w_(2)+w_(1,1)=1 and tr_M(sigma_1)=w_(2)*q+w_(1,1)*(-q^-1)=z.
#   This is the convention in which sigma_1 destabilizes (tr_M(sigma_1)=z)
#   and the unlink T(2,0) has tr_M=1.  NOTE: this trace is NOT bar-symmetric
#   (tr_M(sigma_1^k)(q) != tr_M(sigma_1^k)(1/q)) -- it carries the framing /
#   writhe, which is exactly the U(1) datum tested in CLAIM 2.
# ---------------------------------------------------------------------------
q = sp.symbols('q', positive=True)

# Solve the two Markov axioms once for the Wenzl weights (symbolic in q).
_z_sym = 1 / (sp.sqrt(q) + 1 / sp.sqrt(q))
_A, _B = sp.symbols('A B')
_sol = sp.solve([_A + _B - 1, _A * q + _B * (-1 / q) - _z_sym], [_A, _B])
W_2 = sp.simplify(_sol[_A])     # Wenzl weight of block (2)
W_11 = sp.simplify(_sol[_B])    # Wenzl weight of block (1,1)


def trM_T2k_symbolic(k: int):
    """Canonical Wenzl/Jones-Markov trace tr_M(sigma_1^k) in H_2(q).

    tr_M(sigma_1^k) = W_(2)*q^k + W_(1,1)*(-q^-1)^k, Wenzl weights fixed by
    tr_M(1)=1 and tr_M(sigma_1)=z.  Returns (full_expr, block_dict).
    """
    term_2 = W_2 * q ** k                       # (2) block, eigenvalue q
    term_11 = W_11 * (-1 / q) ** k              # (1,1) block, eigenvalue -q^-1
    return sp.simplify(term_2 + term_11), {"(2)": term_2, "(1,1)": term_11}


def eval_at_q0(expr):
    """Evaluate a sympy expr in q at q0 to 60 dps via mpmath."""
    f = sp.lambdify(q, expr, modules="mpmath")
    return f(Q0)


def writhe(word):
    """Writhe = sum of crossing signs. word = list of signed gens."""
    return sum(1 if g > 0 else -1 for g in word)


def z_factor(qv):
    """Markov stabilization factor z = 1/(q^{1/2}+q^{-1/2})."""
    return 1 / (mp.sqrt(qv) + 1 / mp.sqrt(qv))


# ---------------------------------------------------------------------------
w = WitnessBuilder("inter-nucleon-linked-channel", engine="mpmath+sympy",
                   start_time=START)
w.set_description(
    "EXPLORATORY test of the knot-operator census DERIVED lead (PR #1677): "
    "the inter-nucleon LINKED channel = Hopf link T(2,+-2). Braid word "
    "(provenance: fermion-boson-knot-link.md 2-component link sector + "
    "inter-nucleon-channel-color-tube.md), Markov trace (symbolic + 60 dps, "
    "Wedderburn blocks), writhe (pp=+2/nn=-2) + linking number (+-1), Markov "
    "destabilizability of the 5<->3 bridge, U(1)_framing q^{w.c}. RAW; no fit."
)
w.set_audit_only("docs/audits/2026-06-01-inter-nucleon-linked-channel.md")
w.add_parameter("q0", Q0_STR)
w.add_parameter("dps", mp.mp.dps)
w.add_parameter("m_n_minus_m_p_MeV_PDG_falsification_ref", str(M_N_MINUS_M_P_MEV))

# --- 1. The DERIVED braid words ---------------------------------------------
# word format: signed generators, +1 = sigma_1, -1 = sigma_1^-1, in B_2.
WORDS = {
    "pp_T(2,2)_positive_Hopf": {"word": [1, 1], "k": 2,  "B_n": 2,
        "note": "positive Hopf link; matter-matter; lk +1"},
    "nn_T(2,-2)_negative_Hopf": {"word": [-1, -1], "k": -2, "B_n": 2,
        "note": "negative (mirror) Hopf link; matter-antimatter; lk -1"},
    "pn_T(2,0)_unlink": {"word": [], "k": 0, "B_n": 2,
        "note": "2-component unlink; mixed flavor; lk 0"},
}
braid_summary = {}
for name, d in WORDS.items():
    braid_summary[name] = {
        "braid_word_signed_gens": d["word"],
        "torus_T(2,k)": d["k"],
        "braid_group_B_n": d["B_n"],
        "generators_used": sorted({abs(g) for g in d["word"]}) or [],
        "writhe": writhe(d["word"]),
        "linking_number": d["k"] // 2,   # lk(T(2,k)) = k/2 for even k
        "note": d["note"],
    }
w.add_data("derived_braid_words", braid_summary)
w.add_data("strand_count", 2)
w.add_data("braid_group", "B_2 = Z (single generator sigma_1)")
w.add_data("hecke_algebra", "H_2(q), Wedderburn blocks (2) and (1,1)")
w.add_data("wenzl_markov_weights_symbolic", {
    "W_(2)": str(W_2), "W_(1,1)": str(W_11),
    "W_(2)_at_q0": mp.nstr(eval_at_q0(W_2), 60),
    "W_(1,1)_at_q0": mp.nstr(eval_at_q0(W_11), 60),
    "convention": "Wenzl/Jones-Markov: fixed by tr_M(1)=1 and tr_M(sigma_1)=z",
})
w.add_data("braid_word_provenance",
    "Hopf link T(2,+-2) = sigma_1^{+-2}. DERIVED from fermion-boson-knot-link.md "
    "(the 2-component LINK sector = T(2,n)-even, components winding +1/-1 around "
    "the Reeb direction) composed with the inter-nucleon arc of "
    "inter-nucleon-channel-color-tube.md. NOT chosen to hit any target.")

# writhe + linking-number assertions (structural, from the word)
w.add_assertion("writhe_pp_eq_+2", braid_summary["pp_T(2,2)_positive_Hopf"]["writhe"], 2)
w.add_assertion("writhe_nn_eq_-2", braid_summary["nn_T(2,-2)_negative_Hopf"]["writhe"], -2)
w.add_assertion("writhe_pn_eq_0", braid_summary["pn_T(2,0)_unlink"]["writhe"], 0)
w.add_assertion("linking_number_pp_eq_+1", braid_summary["pp_T(2,2)_positive_Hopf"]["linking_number"], 1)
w.add_assertion("linking_number_nn_eq_-1", braid_summary["nn_T(2,-2)_negative_Hopf"]["linking_number"], -1)

# --- 2. Markov trace tr_M(rho(B)) = J_B(q), symbolic + at q0 -----------------
trace_data = {}
for name, d in WORDS.items():
    k = d["k"]
    full, blocks = trM_T2k_symbolic(k)
    val = eval_at_q0(full)
    block_vals = {b: mp.nstr(eval_at_q0(e), 60) for b, e in blocks.items()}
    trace_data[name] = {
        "trM_symbolic_in_q": str(full),
        "trM_at_q0_60dps": mp.nstr(val, 60),
        "wedderburn_block_values_at_q0": block_vals,
        "block_symbolic": {b: str(sp.simplify(e)) for b, e in blocks.items()},
    }
w.add_data("markov_trace_J_B_of_q", trace_data)

# Cross-check: the (2)+(1,1) block decomposition sums to the full trace.
for name, d in WORDS.items():
    k = d["k"]
    full, blocks = trM_T2k_symbolic(k)
    block_sum = eval_at_q0(blocks["(2)"]) + eval_at_q0(blocks["(1,1)"])
    w.add_assertion(f"trM_block_sum_eq_full_{name}",
                    mp.nstr(block_sum, 55), mp.nstr(eval_at_q0(full), 55),
                    tolerance=1e-50)

# Cross-check pp vs nn: T(2,2) and T(2,-2) are mirror images. The Wenzl
# Jones-Markov trace is NOT bar-symmetric (it carries the framing/writhe),
# so tr_M(pp) != tr_M(nn): the asymmetry IS the framing datum.
tr_pp = eval_at_q0(trM_T2k_symbolic(2)[0])
tr_nn = eval_at_q0(trM_T2k_symbolic(-2)[0])
w.add_data("trM_pp_minus_trM_nn_at_q0", mp.nstr(tr_pp - tr_nn, 60))
w.add_data("trM_pp_nn_asymmetry_note",
    "tr_M(sigma_1^+2) != tr_M(sigma_1^-2): the Wenzl Jones-Markov trace is "
    "NOT bar-symmetric and carries the framing/writhe. tr_M(pp)=%s, "
    "tr_M(nn)=%s. This trace asymmetry between matter-matter and "
    "matter-antimatter linking is the RAW pp/nn distinction the channel "
    "supplies; it is reported, not tuned to any split."
    % (mp.nstr(tr_pp, 30), mp.nstr(tr_nn, 30)))
# Cross-check: tr_M(sigma_1^2) here vs the census Hopf closed form
# 1+(q-1)/sqrt(q) (which is the n-independent Hopf value under a DIFFERENT
# normalisation); record the raw gap (NOT an assertion -- different conventions).
census_hopf = 1 + (Q0 - 1) / mp.sqrt(Q0)
w.add_data("census_hopf_closed_form_1+(q-1)/sqrt(q)_at_q0", mp.nstr(census_hopf, 60))
w.add_data("trM_pp_vs_census_hopf_gap", mp.nstr(abs(tr_pp - census_hopf), 60))
# unlink T(2,0): tr_M(1) in H_2 with q-Schur weights = w_(2)+w_(1,1) = 1.
tr_pn = eval_at_q0(trM_T2k_symbolic(0)[0])
w.add_assertion("trM_unlink_pn_eq_1", mp.nstr(tr_pn, 55), mp.nstr(mp.mpf(1), 55),
                tolerance=1e-50)

# --- 3. Non-Brunnian check ---------------------------------------------------
w.add_data("non_brunnian", {
    "is_brunnian": False,
    "linking_number_nonzero": True,
    "reason": "Hopf link T(2,+-2) has linking number +-1 != 0: the two "
              "components are genuinely linked. Brunnianness (every proper "
              "sublink trivial) requires >=3 components AND lk=0 on each "
              "2-sublink (as the Borromean has). The Hopf link fails both: "
              "it is a 2-component link with nonzero linking number. So it "
              "ESCAPES the Borromean Brunnian obstruction.",
})

# --- 4. CLAIM 1: Markov destabilization (the 5<->3 / here 2<->1 bridge) ------
z0 = z_factor(Q0)
# (a) single sigma_1 destabilizes: tr_M(sigma_1) = z * tr_M(1 in B_1) = z
tr_single_sigma1 = eval_at_q0(trM_T2k_symbolic(1)[0])  # tr_M(sigma_1) in H_2
w.add_data("trM_single_sigma1_at_q0", mp.nstr(tr_single_sigma1, 60))
w.add_data("z_factor_at_q0", mp.nstr(z0, 60))
w.add_assertion("markov_destab_single_sigma1_eq_z",
                mp.nstr(tr_single_sigma1, 50), mp.nstr(z0, 50), tolerance=1e-45)
# (b) sigma_1^2 (the Hopf) does NOT destabilize in one move
tr_sigma1_sq = eval_at_q0(trM_T2k_symbolic(2)[0])
destab_pred = z0 * tr_single_sigma1   # what one destab of the LAST sigma_1 would give
w.add_data("trM_sigma1_sq_at_q0", mp.nstr(tr_sigma1_sq, 60))
w.add_data("z_times_trM_sigma1_destab_prediction", mp.nstr(destab_pred, 60))
w.add_data("hopf_destab_residual_NOT_clean",
           mp.nstr(abs(tr_sigma1_sq - destab_pred), 60))
w.add_data("markov_destabilization_finding", {
    "single_crossing_sigma1_destabilizes_cleanly": True,
    "single_crossing_trace_invariant_factor_z": mp.nstr(z0, 60),
    "hopf_sigma1_sq_destabilizes_in_one_move": False,
    "reason_hopf_not_one_move": "sigma_1^2 is two crossings on the same strand "
        "pair (Reidemeister-II / second-order), not beta.sigma_{n-1}^{+-1} with "
        "beta disjoint. It reduces by RII/conjugation within H_2, not by a "
        "single destabilization to H_1.",
    "contrast_with_borromean": "The Borromean (s1^-1 s2)^3 in B_3 uses BOTH "
        "generators and is Brunnian: NO trailing single sigma_2^{+-1} is "
        "disjoint, so it admits NO clean destabilization at all (census audit). "
        "The linked channel's word sigma_1^k DOES contain destabilizable single "
        "crossings (each sigma_1 alone destabilizes with factor z), so the "
        "linked channel ESCAPES the Brunnian destabilization block -- but its "
        "destabilization is the 2->1 strand move within the m=2 torus tower, "
        "NOT a derived 5->3 functor onto the Borromean H_3 trace.",
})

# --- 5. CLAIM 2: U(1)_framing q^{w.c} on nonzero writhe ----------------------
c = mp.mpf(1)   # per-crossing framing coupling, SET to 1 (NOT fitted)
framing = {}
for name, d in WORDS.items():
    wr = writhe(d["word"])
    framing[name] = {
        "writhe": wr,
        "framing_factor_q^{w.c}_at_q0_c=1": mp.nstr(Q0 ** (wr * c), 60),
    }
w.add_data("u1_framing_factor", framing)
f_pp = Q0 ** (2 * c)
f_nn = Q0 ** (-2 * c)
w.add_data("framing_factor_pp_over_nn_at_q0", mp.nstr(f_pp / f_nn, 60))
w.add_data("framing_factor_pp_minus_nn_at_q0", mp.nstr(f_pp - f_nn, 60))
w.add_data("PDG_m_n_minus_m_p_over_m_p_falsification_ref",
           mp.nstr(M_N_MINUS_M_P_MEV / M_P_MEV, 60))
w.add_caveat(
    "U(1)_framing -> hypercharge is NOT derived. q^{w.c} is a real framing "
    "FACTOR (Im(q0)=0 at observable level). A framing factor EXISTING is not a "
    "hypercharge assignment: writhe w is an integer braid invariant, Y is a "
    "continuous charge, and NO canonical map writhe->Y is supplied. The "
    "per-crossing coupling c is SET to 1 (not fitted); choosing c to make "
    "(f_pp - f_nn) reproduce m_n-m_p would be exactly the fit the discipline "
    "review catches. The PDG m_n-m_p is reported ONLY as a falsification "
    "reference. The framing U(1) is LIVE on the linked channel (writhe +-2 != "
    "0), unlike the writhe-0 Borromean baryon -- so the channel DOES carry a "
    "nontrivial U(1), but its identification with hypercharge remains UNDEFINED."
)
w.add_caveat(
    "Provenance discipline: the braid word sigma_1^{+-2} is the Hopf link "
    "T(2,+-2), DERIVED as the minimal non-Brunnian 2-component link of the "
    "fermion-boson-knot-link.md boson/link sector, with the +-sign fixed by "
    "matter/antimatter chirality. It is NOT chosen to make tr_M or the framing "
    "factor hit m_n-m_p, B_AME, hypercharge, or any h^k. The s5-so3 audit's "
    "production writhe pp=+1/nn=-1 is the LINKING NUMBER of this Hopf link "
    "(lk = +-1); the full-diagram writhe is +-2. Both reported raw."
)

path = w.save()
elapsed = time.monotonic() - START
print(f"[inter-nucleon-linked-channel] wrote {path} in {elapsed:.2f}s")
print(f"  braid words: pp=sigma_1^2 (T(2,2)), nn=sigma_1^-2 (T(2,-2)), pn=unlink")
print(f"  writhe pp/nn/pn = +2 / -2 / 0   (linking number +1 / -1 / 0)")
print(f"  tr_M(pp) at q0  = {mp.nstr(tr_pp, 40)}")
print(f"  tr_M(nn) at q0  = {mp.nstr(tr_nn, 40)}")
print(f"  tr_M(pn=unlink) = {mp.nstr(tr_pn, 40)}")
print(f"  z(q0)           = {mp.nstr(z0, 40)}")
print(f"  tr_M(single sigma_1) = {mp.nstr(tr_single_sigma1, 40)} (= z: destab OK)")
print(f"  framing q^{{+2}} / q^{{-2}} = {mp.nstr(f_pp,30)} / {mp.nstr(f_nn,30)}")
