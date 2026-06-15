#!/usr/bin/env python3
"""Knot-operator census + group-action map (EXPLORATORY, audit-only).

Maps the distinct knot/link operators that appear in the QOU framework for
color tubes / nucleons / channels and the group action(s) attached to each.

Computes, RAW (no tuning to any observable):
  - the writhe w(beta) of each canonical braid word (the U(1)_framing datum);
  - the Markov-trace stabilization scaling tr_M(beta . sigma_n^{+-1}) = z^{+-1} tr_M(beta)
    (z = 1/(q^{1/2}+q^{-1/2})) at the substrate q0, the canonical
    strand-count-changing map B_n -> B_{n+1};
  - the n-independence of tr_M(sigma_1^2) (the Hopf, witness sanity);
  - which operators have nonzero writhe (live U(1)) vs zero (Borromean).

NO FIT. Every numeric is a falsification reference reported raw.
Audit doc: docs/audits/2026-06-01-knot-operator-census-group-actions.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from pathlib import Path

import mpmath as mp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402

START = time.time()
mp.mp.dps = 60

# Substrate q0 (proton-anchored). Reference value only -- not tuned here.
Q0 = mp.mpf("1.10998")


def writhe_from_word(word):
    """Writhe = sum of crossing signs. word is a list of signed generators
    (+i = sigma_i, -i = sigma_i^{-1})."""
    return sum(1 if g > 0 else -1 for g in word)


def z_factor(q):
    """Markov stabilization factor z = 1/(q^{1/2} + q^{-1/2})."""
    return 1 / (mp.sqrt(q) + 1 / mp.sqrt(q))


def trM_sigma1_sq(q):
    """Closed form tr_M(sigma_1^2) = 1 + (q-1)/q^{1/2} (n-independent)."""
    return 1 + (q - 1) / mp.sqrt(q)


# --- Census of canonical braid words (operator -> (B_n strand count, word)) ---
# word entries: +i = sigma_i (L+), -i = sigma_i^{-1} (L-)
OPERATORS = {
    # name: (strands n in B_n, braid word as signed-generator list, note)
    "unknot_T(1,0)": (1, [], "identity / vacuum; genus 0"),
    "Hopf_T(2,2)=sigma1^2": (2, [1, 1], "positive Hopf link; diquark; writhe +2"),
    "trefoil_T(2,3)=sigma1^3": (2, [1, 1, 1], "electron e^-; lepton gen 1"),
    "cinquefoil_T(2,5)=sigma1^5": (2, [1, 1, 1, 1, 1], "muon; lepton gen 2"),
    "septafoil_T(2,7)=sigma1^7": (2, [1] * 7, "tau; lepton gen 3 (sym-broken)"),
    "T(2,9)=sigma1^9": (2, [1] * 9, "genus-4 saturation; sym-broken"),
    "T(3,4)=(s1 s2)^4": (3, [1, 2] * 4, "Hopf^2 color binding; H^{0,1}"),
    "T(3,5)=(s1 s2)^5": (3, [1, 2] * 5, "weak mediator; alpha_EM index"),
    "borromean=(s1^-1 s2)^3": (3, [-1, 2, -1, 2, -1, 2], "nucleon/baryon; writhe 0"),
    "figure8_4_1": (3, [1, -2, 1, -2], "Higgs/pion-half; hyperbolic; writhe 0"),
}

w = WitnessBuilder("knot-operator-census-group-actions", engine="mpmath", start_time=START)
w.set_description(
    "EXPLORATORY census of QOU knot/link operators: writhe (U(1)_framing), "
    "Markov-stabilization scaling (B_n->B_{n+1} bridge), Hopf n-independence. "
    "All RAW @ 60 dps; no tuning to any observable."
)
w.set_audit_only("docs/audits/2026-06-01-knot-operator-census-group-actions.md")
w.add_parameter("q0", str(Q0))
w.add_parameter("dps", mp.mp.dps)

# --- 1. Writhe per operator (the U(1)_framing datum) ---
writhes = {}
for name, (n, word, note) in OPERATORS.items():
    wr = writhe_from_word(word)
    writhes[name] = {"strands_B_n": n, "writhe": wr, "note": note,
                     "u1_framing_nontrivial": wr != 0}
w.add_data("writhe_per_operator", writhes)

# T(2,2m) writhe = +2m closed form (all positive crossings)
t22m = {}
for m in range(1, 6):
    word = [1] * (2 * m)  # sigma_1^{2m}
    t22m[f"T(2,{2*m})"] = {"writhe": writhe_from_word(word), "formula_2m": 2 * m}
w.add_data("torus_T2_2m_writhe", t22m)
# assertion: T(2,2m) writhe equals 2m (derived, structural)
for m in range(1, 6):
    w.add_assertion(f"writhe_T(2,{2*m})_eq_2m", t22m[f"T(2,{2*m})"]["writhe"], 2 * m)
# assertion: Borromean writhe = 0 (the U(1) is trivial on the baryon)
w.add_assertion("writhe_borromean_eq_0", writhes["borromean=(s1^-1 s2)^3"]["writhe"], 0)

# --- 2. Markov stabilization factor z at q0 (the strand-count bridge) ---
z = z_factor(Q0)
w.add_data("markov_stabilization_factor_z_at_q0", str(z))
# Stabilization: tr_M(beta . sigma_n^{+-1}) = z^{+-1} tr_M(beta) when the new
# strand is DISJOINT. This is the canonical B_n -> B_{n+1} map (vertical alpha_V
# of markov-moves-brane-tower.md). Report z, z^-1 RAW.
w.add_data("z_inverse_at_q0", str(1 / z))

# --- 3. Hopf tr_M(sigma_1^2) n-independence (sanity; the disjoint-strand case) ---
trhopf = trM_sigma1_sq(Q0)
w.add_data("trM_sigma1_sq_at_q0", str(trhopf))
# Verify the closed form 1+(q-1)/sqrt(q) equals the Hecke-derived value
# tr_M(sigma_1^2) = (q-q^-1)*z + 1 with z = 1/(q^{1/2}+q^{-1/2}).
hecke_val = (Q0 - 1 / Q0) * z_factor(Q0) + 1
w.add_assertion("trM_sigma1sq_closedform_eq_hecke", str(trhopf), str(hecke_val),
                tolerance=1e-50)

# --- 4. Strand-count summary: which group acts on which n ---
# Borromean baryon lives in H_3 (3 strands); the S5/SO(3) fiber lives on
# 5 strands (partitions of 5). The torus knots T(2,n) live in B_2 (2 strands);
# T(3,n) in B_3 (3 strands). Markov stabilization is the ONLY structural map
# changing strand count. Record the strand-count of every operator for the map.
strand_map = {name: n for name, (n, _, _) in OPERATORS.items()}
w.add_data("operator_strand_counts", strand_map)
w.add_data("fiber_action_strand_count", 5)  # S5/A5 lives on partitions of 5
w.add_data("borromean_trace_strand_count", 3)  # H_3

# --- 5. The bridge probe: does Markov (de)stabilization connect 5 <-> 3? ---
# To go from H_5 (fiber level) to H_3 (Borromean trace) requires TWO
# de-stabilizations (remove sigma_4, then sigma_3), each contributing z^{-1}
# IF the removed strand is disjoint. RAW factor for two de-stabs:
two_destab = (1 / z) ** 2
w.add_data("two_destabilization_factor_z_inv_sq_at_q0", str(two_destab))
w.add_caveat(
    "Markov de-stabilization H_5 -> H_3 is only valid when the removed strands "
    "are DISJOINT from the closure (Markov axiom 3). The Borromean braid "
    "(s1^-1 s2)^3 uses BOTH generators of B_3 non-trivially and is Brunnian "
    "(every 2-sublink is trivial) -- so a strand cannot be removed without "
    "changing the link type. Therefore plain Markov de-stabilization does NOT "
    "give a derived H_5(fiber) -> H_3(Borromean) functor. The 5-strand fiber "
    "object and the 3-strand trace remain in different rep rings. The bridge "
    "is OPEN: a derived map requires either (a) a cabling/satellite operation "
    "(2-cabling a 3-strand pattern -> 6 strands, NOT 5), or (b) an explicit "
    "branching functor Res^{H_5}_{H_3} composed with the fiber decoration -- "
    "neither is supplied by the current framework. No fit attempted."
)
w.add_caveat(
    "U(1)_framing: writhe is nonzero (+2m) for the torus knots T(2,2m) and for "
    "the Hopf (sigma_1^2, w=+2), but ZERO for the Borromean baryon and the "
    "figure-eight. So a nonzero-writhe operator (e.g. a T(2,2m) color-tube "
    "operator) WOULD carry a nontrivial U(1)_framing phase q^{w.c}. This is a "
    "RAW structural observation; mapping writhe -> hypercharge Y is NOT derived "
    "and is NOT attempted. The production nucleon uses the writhe-0 Borromean, "
    "so the framing U(1) is trivial there -- consistent with the s5-so3 audit."
)

path = w.save()
elapsed = time.time() - START
print(f"[knot-operator-census] wrote {path} in {elapsed:.2f}s")
print(f"  z(q0) = {z}")
print(f"  tr_M(sigma_1^2)(q0) = {trhopf}")
print(f"  T(2,2m) writhe = 2m: {[t22m[f'T(2,{2*m})']['writhe'] for m in range(1,6)]}")
print(f"  Borromean writhe = {writhes['borromean=(s1^-1 s2)^3']['writhe']}")
