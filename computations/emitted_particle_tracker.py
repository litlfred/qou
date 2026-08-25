#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical witness; per-step emitted-particle
# ledger in MeV, no symbolic-q polynomial output.
"""
Emitted-particle tracker for the iterative knot build.

Owner directive (2026-06-17): regardless of whether it closes the mass gap,
the iterative build SHOULD track the particles emitted at each step and their
energy. `iterative_knot_builder.py` currently records only crossing counts +
a volume proxy — no emission ledger. This adds one.

What is "emitted". Each nucleon's braid is a sequence of γγ̄ pair-production
vertices (β_Bor = (σ₀σ₁⁻¹)³; `gamma_gamma_pair_production_decomposition.py`),
and adding a nucleon links it to the assembly (the inter-nucleon crossings).
The trace splits under the bar-involution q↦q⁻¹ into:
  • bar-EVEN  (cosh, (tr(q₀)+tr(q₀⁻¹))/2) — the RETAINED binding / volume
    channel (mirror-symmetric, the bound state that stays);
  • bar-ODD   (sinh, (tr(q₀)−tr(q₀⁻¹))/2) — the EMITTED / radiated channel
    (the Chern–Simons / decay partner; the γγ̄ that leaves).
Computable now that the q-parameterised core gives tr_M(q⁻¹)
(`tr_m_atom_zn(q=…)`, stage-2 refactor).

Per step we record: γγ̄ vertices (non-trivial crossings) added, the retained
(bar-even) and emitted (bar-odd) trace content, and the emitted energy
E₀·|bar-odd| in MeV — both cumulative and the per-nucleon increment.

Exploratory; no fit.

Run:  python3 -u computations/emitted_particle_tracker.py 2>&1 | tee /tmp/emit.log
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402
import sys
import mpmath as mp  # noqa: E402

from tr_m_atom_via_transfer import tr_m_atom_zn  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402
from q_parameter import Q_MP as Q0  # noqa: E402
from codata_constants import M_E_MEV  # noqa: E402
from _precision import set_compute_dps  # noqa: E402

SEQUENCE = [("p", 1, 0), ("D", 1, 1), ("3He", 2, 1), ("4He", 2, 2),
            ("6Li", 3, 3), ("7Li", 3, 4)]


def _gamma_vertices(Z, N):
    """γγ̄ pair-production vertices = non-trivial crossings (d≠0) in the atom
    word: each is a positive/negative/mixed crossing that links strands."""
    word = atom_braid_word_3A(Z, N, include_inter=True)
    return sum(1 for (_c, d, _g) in word if abs(float(d)) > 1e-12)


def main() -> int:
    set_compute_dps()
    q0 = mp.mpf(str(Q0)); qi = mp.mpf(1) / q0
    E0 = mp.mpf(str(M_E_MEV)) / (q0 * (q0 - 1))   # canonical energy scale

    print("\n  EMITTED-PARTICLE TRACKER — iterative knot build")
    print(f"  E₀ = {float(E0):.4f} MeV;  emitted = E₀·|bar-odd tr|, "
          f"retained = E₀·bar-even tr  (bar-involution q↦q⁻¹)\n")
    print("| step | A | γγ̄ vertices | retained E (MeV) | emitted E (MeV) | multi-link emit (MeV) | Δemitted/step |")
    print("|---|--:|--:|--:|--:|--:|--:|")
    rows = []
    prev_emit = mp.mpf(0)
    for name, Z, N in SEQUENCE:
        ta0, tf0, _, _ = tr_m_atom_zn(Z, N, q=q0)
        tai, tfi, _, _ = tr_m_atom_zn(Z, N, q=qi)
        bar_even = (ta0 + tai) / 2
        bar_odd = (ta0 - tai) / 2
        retained = E0 * bar_even
        emitted = E0 * abs(bar_odd)
        # MULTI-LINK (inter-nucleon) emission: bar-odd of the binding defect
        # (tr_free − tr_atom). The free word is the un-linked product
        # tr_p^Z·tr_n^N; the defect is purely the inter-nucleon linking, and
        # its bar-odd part is the γγ̄ radiated specifically by binding the
        # nucleons together (zero for A=1 — no interfaces).
        defect0 = tf0 - ta0
        defecti = tfi - tai
        emitted_multilink = E0 * abs((defect0 - defecti) / 2)
        d_emit = emitted - prev_emit
        nv = _gamma_vertices(Z, N)
        rows.append({
            "name": name, "Z": Z, "N": N, "A": Z + N, "gamma_vertices": nv,
            "tr_q0": float(ta0), "tr_qinv": float(tai),
            "retained_MeV": float(retained), "emitted_MeV": float(emitted),
            "emitted_multilink_MeV": float(emitted_multilink),
            "delta_emitted_MeV": float(d_emit),
        })
        print(f"| {name} | {Z+N} | {nv} | {float(retained):.3f} "
              f"| {float(emitted):.3f} | {float(emitted_multilink):.3f} "
              f"| {float(d_emit):+.3f} |")
        prev_emit = emitted

    print("\n  Reading: 'retained' (bar-even / cosh) is the volume/binding "
          "channel that stays in the bound state; 'emitted' (bar-odd / sinh) "
          "is the Chern–Simons / γγ̄ channel that radiates. The per-step "
          "Δemitted is the energy carried off as each nucleon is linked in — "
          "the ledger the iterative build previously did not keep.")

    try:
        from witness_base import WitnessBuilder
        w = WitnessBuilder("emitted-particle-tracker",
                           engine="emitted_particle_tracker.py")
        w.set_description(
            "Per-step emitted-particle ledger for the iterative knot build: "
            "γγ̄ vertices + retained (bar-even) / emitted (bar-odd) trace "
            "energy in MeV, via the q-parameterised core tr_M(q⁻¹). "
            "Emitted = E₀·|bar-odd|, the Chern–Simons/decay channel that "
            "radiates as each nucleon links in. Exploratory.")
        w.add_parameter("E0_MeV", float(E0))
        w.add_parameter("q_0", float(q0))
        for r in rows:
            w.add_data(f"step_{r['name']}", r)
        w.save()
        print("\n  witness written: emitted-particle-tracker.witness.json")
    except Exception as e:
        print(f"\n  (witness skipped: {e})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
