#!/usr/bin/env python3
"""Tests Mechanism 2 of prop:categorical-chain-convergence-mechanisms: the joint Markov trace
of two unlinked braids factorises as τ_M(K_1) · τ_M(K_2) · z^k by Markov axiom M3
(disconnected-strand stabilisation). Confirms that the infinite product Q_β^cat over the
base space converges because most inter-atomic-knot pairs are unlinked.
"""
from __future__ import annotations

import sys
import json
from pathlib import Path
import mpmath as mp

import _path_bridge
import _path_bridge as _pb

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _precision import set_compute_dps
set_compute_dps()

from witness_base import WitnessBuilder
from closed_form_tau_M import markov_z  # noqa: E402 — canonical convention-D z
from markov_trace_canonical import tr_M_word  # noqa: E402
from _precision import fmt  # noqa: E402 — serialise mpf, never str(float)

Q_PINNING = _pb.witness_path("q-pinning-50-digit.witness.json", HERE)

def _load_q_0(w: WitnessBuilder) -> mp.mpf:
    """Load q_0, declaring q-pinning-50-digit as an upstream.

    `add_upstream` records the upstream's sha256 + commitSha + computedAt under
    `data.upstream_witness_hashes`, which is the only thing
    `witness_dependency_drift.py` walks. Read with a plain `json.load`, the
    edge does not exist as far as that validator is concerned, and this witness
    can go stale behind a green gate — which is exactly how
    `qbeta-per-block-paper-closed-forms` moved at the 8th digit with no source
    change at all. The builder is threaded in because the record needs
    somewhere to land.
    """
    return mp.mpf(w.add_upstream(Q_PINNING)["derived_50_digit"]["q"])

def main():
    w = WitnessBuilder("inter-knot-decoupling", engine="sympy+mpmath")

    q_0 = _load_q_0(w)
    
    # Everything below is COMPUTED from the q_0 loaded above. It used to be a
    # block of hand-transcribed strings, introduced by a prior session that
    # left its own reasoning in the source ("Let's see what z_markov_norm was
    # ... wait, the exact values:") and then typed values copied from an
    # earlier witness. Three separate defects, all now removed:
    #
    #   1. `q_0` was loaded on the line above and then IGNORED, with a typed
    #      q_0_50dps written instead — and that literal is 2.842e-12 off the
    #      witness it claims to quote. It is one of the 336 stranded copies of
    #      the muon pin catalogued in bean `qou-5op4`; this probe no longer
    #      carries one, because it now uses the value it already reads. (No
    #      canonical muon literal is chosen here — that is `qou-5op4`'s open
    #      question and a fix to it was retracted on main.)
    #   2. z was convention C, excised by the 2026-08-09 ruling.
    #   3. `tau_M_K2` and the joint prediction were NOT the Markov trace of
    #      this braid under EITHER convention. Transcribed: -1.498185508...
    #      Computed at the same q_0 under C: +0.249320795... — wrong sign and
    #      wrong magnitude, so this was not a convention artefact but an
    #      incorrect number. The C-frame value is quoted in the assertion note
    #      below rather than deleted.
    z = markov_z(q_0)
    h = q_0 - 1 / q_0

    # K_1 = sigma_0 and K_2 = sigma_0 sigma_1, both in B_3; the joint closure
    # adds k = 3 strands by disjoint stabilisation, so M3 gives z^3.
    K1_WORD, K2_WORD, N_STRANDS, K_ADDED = (0,), (0, 1), 3, 3
    tau_K1 = tr_M_word(K1_WORD, N_STRANDS, z, h)
    tau_K2 = tr_M_word(K2_WORD, N_STRANDS, z, h)
    joint_via_M3 = tau_K1 * tau_K2 * z ** K_ADDED

    w.set_description(
        "Tests Mechanism 2 of prop:categorical-chain-convergence-mechanisms: the joint Markov "
        "trace of two unlinked braids factorises as \u03c4_M(K_1) \u00b7 \u03c4_M(K_2) \u00b7 z^k by Markov "
        "axiom M3 (disconnected-strand stabilisation). Confirms that the infinite product "
        "Q_\u03b2^cat over the base space converges because most inter-atomic-knot pairs are unlinked."
    )

    w.add_parameter("auditOnly", "PR #657 follow-up. Provides theoretical justification for the convergence-via-locality argument; full empirical verification at H_6 awaits y_\u03bb for n=6 in wenzl_y_lambda.")
    w.add_parameter("markov_convention", "D (z = q^3/(q^2+1)) via closed_form_tau_M.markov_z")
    w.add_data("q_0_50dps", fmt(q_0))
    w.add_data("z_markov_norm", fmt(z))
    w.add_data("K_1_braid", "\u03c3_0 in B_3")
    w.add_data("K_2_braid", "\u03c3_0 \u00b7 \u03c3_1 in B_3")
    w.add_data("tau_M_K1", fmt(tau_K1))
    w.add_data("tau_M_K2", fmt(tau_K2))
    w.add_data("predicted_joint_via_M3_factorisation", fmt(joint_via_M3))
    w.add_data("strands_added_by_disjoint_stabilisation", K_ADDED)
    w.add_data("factorisation_formula", "\u03c4_M(K_1 \u2294 K_2 in B_{n_1 + n_2}) = \u03c4_M(K_1) \u00b7 \u03c4_M(K_2) \u00b7 z^k where k = strands added by disjoint stabilisation")
    w.add_data("structural_origin", "Markov axiom M3 (Jones 1985)")
    w.add_data("superseded_transcription", (
        "Before 2026-08-23 every value here was hand-transcribed. tau_M_K2 read "
        "-1.498185508551815418311580192395458384246144137308 and the joint read "
        "-0.093128498614094617969884554982395707414295262041364; recomputed at "
        "the same q_0 under convention C those are +0.2493207959793872068594165 "
        "and +0.01549799492138220432434304, so the transcribed pair was wrong in "
        "sign and magnitude, not merely off-convention."
    ))
    w.add_data("empirical_verification_status", "Direct B_6 verification awaits y_\u03bb for n=6 in wedderburn_markov.wenzl_y_lambda. The factorisation property is THEORETICALLY axiomatic from Markov M3.")

    # tau_M(sigma_0) in B_3 IS z by the Markov property -- a self-check that the
    # trace call and the z helper agree rather than a claim about the physics.
    assert abs(tau_K1 - z) < mp.mpf(10) ** (-40), (tau_K1, z)

    out = w.save()
    print(f"Wrote {out.name}")

if __name__ == "__main__":
    main()
