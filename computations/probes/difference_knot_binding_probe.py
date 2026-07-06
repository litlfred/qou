#!/usr/bin/env python3
"""difference_knot_binding_probe.py — binding = MASS of the difference knot.

Owner hypothesis (2026-06-13): binding energy is the mass of the knot you
get by taking the difference of the bound and free braids BEFORE any trace
is applied. "The difference will have its own knot structure, hence mass."

This is distinct from — and engineered to dodge — both prior attempts:

  * binding_link_volumes.py:  B = m_e·Vol(K_bind)·Δtr with HAND-ASSIGNED
    links (Hopf/8_11/L6a4).  Fails A≥3 because it still multiplies by the
    nearly-A-independent trace difference Δtr ≈ 0.6–0.9.

  * binding_volume_difference_probe.py:  Vol(atom) − Vol(free), each braid
    closed SEPARATELY and forced positive ([k+1]).  Both closures come out
    Seifert-fibred (Vol = 0) — positive braids are never hyperbolic.

The owner's reformulation removes the trace from binding ENTIRELY (binding
is a *mass*, computed by the SAME geometric formula as a particle's rest
mass) and forms the difference as a SINGLE braid

    D  =  W_atom · W_free⁻¹      (group difference in the braid group)

with crossing SIGNS respected (d≈0 → σ⁺ ; d≈−h → σ⁻).  D is mixed-sign by
construction, so its closure CAN be hyperbolic (cf. the figure-eight
σ₁σ₂⁻¹, the simplest hyperbolic knot — a positive braid never is).

Because W_atom = W_free + (inter-nucleon crossings), the intra-nucleon
crossings of W_atom and W_free⁻¹ largely cancel and D is essentially the
INTER-NUCLEON LINKING braid — the topological "binding link", now DERIVED
from the canonical words rather than read off the SDP registry.

The pn interface crossing carries the genuinely-quantum weight d≈−h/2
(neither σ⁺ nor σ⁻); its topological resolution is a physical choice, so
the probe runs three: pn→σ⁺, pn→σ⁻, pn→dropped (smoothed).

THREE QUESTIONS (no fit, no AME-tuning, no hand-assigned knots):
  Q1  Is closure(D) hyperbolic — i.e. does the mixed-sign difference braid
      escape the Seifert-fibred Vol=0 trap that killed the positive-braid
      probe?
  Q2  Does Vol(closure(D)) GROW with mass number A — i.e. does it carry the
      A-dependence that the flat trace difference Δtr cannot?
  Q3  Does the DERIVED difference knot reproduce the hand-assigned census
      binding-link volumes (8_11 → 8.2863 for ³H, L6a4 → 7.3277 for ³He)?
      A yes would DERIVE the conj:canonical-knot-id-sdp assignment.

EXPLORATORY / DIAGNOSTIC.  No production path, no content block, no fit.
Raw volumes reported; outcome assessed tiered (refuted / near-match /
derived) per the Δ_λ-gate discipline.

Ref: docs/audits/2026-06-13-9b-h1-exponent-location-refuted.md  (why the
     algebraic trace route is exhausted — motivates the geometric attack)
Ref: computations/binding_volume_difference_probe.py
Ref: computations/binding_link_volumes.py
Ref: content/quantum-observable-universe/mass-theory/conj-canonical-knot-id-sdp.md
"""
from __future__ import annotations

# Path bridge (probes cluster — subdirectory refactor Phase 1).
import sys as _sys  # noqa: E402
from pathlib import Path as _Path  # noqa: E402
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent))
import _path_bridge as _bridge  # noqa: E402, F401
del _sys, _Path, _bridge

import sys  # noqa: E402
from pathlib import Path  # noqa: E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from mass_at_3A_proper import atom_braid_word_3A  # noqa: E402

HERE = Path(__file__).resolve().parent

# AME2020 binding energies (MeV) — comparison targets only, nothing tuned.
B_AME = {"D": 2.224566, "T": 8.481798, "3He": 7.718043, "4He": 28.295673}
CASES = [("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2)]
# Hand-assigned census binding-link volumes (binding_link_volumes.py) — the
# Q3 reference the derived difference knot is asked to reproduce.
CENSUS_BINDING_VOL = {"D": 0.0, "T": 8.2863168, "3He": 7.3277248}

# Substrate h = q − q⁻¹ at q₀; the crossing-sign classifier thresholds.
_Q0 = mp.mpf("1.1099785955573347")
_H = float(_Q0 - 1 / _Q0)            # ≈ 0.2091


def _topo_sign(d: float, gen: int, pn_mode: str):
    """Map a Hecke crossing (c, d, gen) to a topological braid generator.

    d ≈ 0     → σ⁺  (+(gen+1))         [pp interface / intra g₀]
    d ≈ −h    → σ⁻  (−(gen+1))         [nn interface / intra σ⁻¹]
    d ≈ −h/2  → pn interface (quantum) → resolved per pn_mode.
    Returns a signed generator int, or None to drop the crossing.
    """
    g = gen + 1
    if abs(d) < 0.25 * _H:
        return g
    if abs(d - (-_H)) < 0.25 * _H:
        return -g
    if abs(d - (-_H / 2)) < 0.25 * _H:          # pn mixed
        if pn_mode == "plus":
            return g
        if pn_mode == "minus":
            return -g
        return None                              # "drop" → smoothed
    # any other weight: classify by sign of d (negative → σ⁻)
    return -g if d < 0 else g


def _free_reduce(braid: list[int]) -> list[int]:
    """Cancel adjacent inverse generators (σ_i σ_i⁻¹ = 1) — the braid-group
    free reduction that strips the cancelling intra-nucleon structure and
    drives W_atom·W_free⁻¹ toward its essential binding core. Iterated to a
    fixed point (a cancellation can expose a new adjacent pair)."""
    changed = True
    out = list(braid)
    while changed:
        changed = False
        nxt: list[int] = []
        for g in out:
            if nxt and nxt[-1] == -g:
                nxt.pop()
                changed = True
            else:
                nxt.append(g)
        out = nxt
    return out


def _difference_braid(Z: int, N: int, pn_mode: str, reduce: bool) -> list[int]:
    """D = W_atom · W_free⁻¹ as a topological signed braid word."""
    w_atom = atom_braid_word_3A(Z, N, include_inter=True)
    w_free = atom_braid_word_3A(Z, N, include_inter=False)
    atom_topo = [s for (_c, d, k) in w_atom
                 if (s := _topo_sign(float(d), k, pn_mode)) is not None]
    free_topo = [s for (_c, d, k) in w_free
                 if (s := _topo_sign(float(d), k, pn_mode)) is not None]
    # W_free⁻¹ : reverse order, negate every generator.
    free_inv = [-s for s in reversed(free_topo)]
    braid = atom_topo + free_inv
    return _free_reduce(braid) if reduce else braid


def _closure_volume(braid: list[int]):
    """(vol, solution_type, verified, n_crossings) of the braid closure.

    Randomizes the triangulation up to 40× to reach an
    'all tetrahedra positively oriented' solution and confirms with
    verify_hyperbolicity (rigorous interval volume) where available —
    so 'contains degenerate tetrahedra' (an imperfect triangulation, NOT a
    zero volume) doesn't masquerade as a refutation."""
    import snappy  # lazy
    if not braid:
        return 0.0, "empty", False, 0
    try:
        M = snappy.Link(braid_closure=braid).exterior()
    except Exception as exc:  # noqa: BLE001
        return 0.0, f"failed:{type(exc).__name__}", False, len(braid)
    best_vol, best_sol = 0.0, "degenerate"
    for _ in range(40):
        try:
            sol = M.solution_type()
            v = float(M.volume())
        except Exception:
            try:
                M.randomize()
            except Exception:
                break
            continue
        if v > best_vol:
            best_vol, best_sol = v, sol
        if "positively" in sol or "geometric" in sol:
            verified = False
            try:
                ok, _ = M.verify_hyperbolicity()
                verified = bool(ok)
            except Exception:
                verified = False
            return v, sol, verified, len(braid)
        try:
            M.randomize()
        except Exception:
            break
    return best_vol, best_sol, False, len(braid)


def main() -> int:
    set_compute_dps()
    w = WitnessBuilder("difference-knot-binding", engine="snappea")
    w.set_description(
        "Owner hypothesis: binding = mass of the difference knot "
        "D = W_atom·W_free⁻¹ (braid-group difference, crossing signs "
        "respected), taken BEFORE any trace — a single mixed-sign braid "
        "that can be hyperbolic, unlike the positive-braid Vol(atom)−"
        "Vol(free) probe, and with NO multiplicative Δtr, unlike the "
        "hand-assigned binding-link probe. Q1 hyperbolic? Q2 volume grows "
        "with A? Q3 reproduces census binding-link volumes (8_11→8.286, "
        "L6a4→7.328), which would DERIVE the conj:canonical-knot-id-sdp "
        "assignment. Diagnostic only; no fit, no wiring."
    )
    w.set_content_block("conj:canonical-knot-id-sdp")

    print(f"h = q0 - 1/q0 = {_H:.5f}   (pn weight = -h/2 = {-_H/2:.5f})")
    print("difference braid D = W_atom·W_free⁻¹, FREE-REDUCED to its core.")
    results = {}
    for pn_mode in ("plus", "minus", "drop"):
        print(f"\n=== pn interface resolved as: {pn_mode} ===")
        print(f"{'iso':4s} {'A':>2s} {'|D|':>4s} {'Vol(D)':>10s} {'verif':>6s} "
              f"{'solution':>26s} {'B_AME':>8s}")
        results[pn_mode] = {}
        for iso, Z, N in CASES:
            A = Z + N
            braid = _difference_braid(Z, N, pn_mode, reduce=True)
            vol, sol, verified, ncr = _closure_volume(braid)
            hyp = vol > 0.5  # nonzero geodesic volume = hyperbolic-class
            results[pn_mode][iso] = {
                "A": A, "n_crossings": ncr, "vol": vol,
                "solution_type": sol, "verified": bool(verified),
                "hyperbolic": bool(hyp),
            }
            print(f"{iso:4s} {A:>2d} {ncr:>4d} {vol:>10.5f} "
                  f"{'yes' if verified else '·':>6s} {sol:>26s} "
                  f"{B_AME[iso]:>8.3f}")
            w.add_data(f"{pn_mode}_{iso}_vol", mp.nstr(mp.mpf(repr(vol)), 12))
            w.add_data(f"{pn_mode}_{iso}_solution_type", sol)
            w.add_data(f"{pn_mode}_{iso}_verified_hyperbolic", bool(verified))
            w.add_data(f"{pn_mode}_{iso}_n_crossings", ncr)

    # Critical check: is Vol(D) carrying BINDING, or just tracking the
    # crossing count |D| (hyperbolic volume-per-crossing is ~bounded, so a
    # bigger braid is trivially a bigger volume)? Report B_AME/Vol spread
    # (constant ⇒ binding signal) and Vol/|D| (constant ⇒ trivial-count).
    print("\n--- critical ratios (B_AME/Vol should be CONSTANT for a "
          "derivation; Vol/|D| constant ⇒ volume is just crossing-count) ---")
    for pn_mode in results:
        rows = [(iso, results[pn_mode][iso]) for iso, _, _ in CASES
                if results[pn_mode][iso]["vol"] > 0.5]
        b_over_v = {iso: B_AME[iso] / r["vol"] for iso, r in rows}
        v_over_c = {iso: r["vol"] / r["n_crossings"] for iso, r in rows
                    if r["n_crossings"]}
        if b_over_v:
            spread = max(b_over_v.values()) / min(b_over_v.values())
            print(f"  [{pn_mode:5s}] B/Vol = "
                  + " ".join(f"{i}:{v:.3f}" for i, v in b_over_v.items())
                  + f"  (spread {spread:.2f}×)")
            print(f"          Vol/|D| = "
                  + " ".join(f"{i}:{v:.3f}" for i, v in v_over_c.items()))
            w.add_data(f"{pn_mode}_B_over_Vol", {i: round(v, 4) for i, v in b_over_v.items()})
            w.add_data(f"{pn_mode}_B_over_Vol_spread", round(float(spread), 3))
            w.add_data(f"{pn_mode}_Vol_per_crossing", {i: round(v, 4) for i, v in v_over_c.items()})
            # mirror-nucleus ordering: does Vol(D_T) > Vol(D_3He) like B?
            if "T" in dict(rows) and "3He" in dict(rows):
                vt, vh = results[pn_mode]["T"]["vol"], results[pn_mode]["3He"]["vol"]
                w.add_data(f"{pn_mode}_mirror_ordering_T_gt_3He_matches_AME",
                           bool((vt > vh) == (B_AME["T"] > B_AME["3He"])))

    # Q1 — did ANY resolution produce a hyperbolic difference knot at A≥3
    # (escaping the positive-braid Vol=0 trap)?
    a3_hyp = any(
        results[m][iso]["hyperbolic"] and results[m][iso]["vol"] > 0.5
        for m in results for iso in ("T", "3He", "4He")
    )
    w.add_assertion(
        name="Q1_difference_knot_hyperbolic_at_A3",
        computed=bool(a3_hyp),
        expected=True,
        tolerance=0,
        source="mixed-sign difference braid W_atom·W_free⁻¹ yields a "
               "hyperbolic closure at some A≥3 (vs the positive-braid "
               "Vol=0 refutation in binding_volume_difference_probe.py)",
    )

    # Q2 — monotone growth of Vol(D) with A in the best (most-hyperbolic)
    # resolution (informational; recorded, not asserted pass/fail).
    for pn_mode in results:
        vols_by_A = [(results[pn_mode][iso]["A"], results[pn_mode][iso]["vol"])
                     for iso, _, _ in CASES]
        grows = all(vols_by_A[i + 1][1] >= vols_by_A[i][1] - 1e-9
                    for i in range(len(vols_by_A) - 1))
        w.add_data(f"{pn_mode}_volume_monotone_in_A", bool(grows))

    # Q3 — does any derived difference knot reproduce a census binding-link
    # volume (would DERIVE the conj assignment)?
    q3_hits = []
    for pn_mode in results:
        for iso in ("T", "3He"):
            v = results[pn_mode][iso]["vol"]
            target = CENSUS_BINDING_VOL[iso]
            if target > 0 and abs(v - target) < 0.05:
                q3_hits.append(f"{pn_mode}/{iso}: {v:.4f}≈{target:.4f}")
    w.add_data("Q3_census_volume_reproductions",
               q3_hits if q3_hits else "none")

    verdict = (
        "DERIVED-MATCH: difference knot reproduces a census binding-link "
        f"volume ({'; '.join(q3_hits)})" if q3_hits else
        ("HYPERBOLIC-SIGNAL: difference knot is hyperbolic at A≥3 but does "
         "not (yet) hit a census volume — volume route is live, assignment "
         "not yet derived" if a3_hyp else
         "REFUTED-AT-THIS-RESOLUTION: difference braid closures stay "
         "non-hyperbolic / Vol≈0 even mixed-sign; the binding volume is not "
         "in the bare topological difference at q₀ (converges with the "
         "binding_volume_difference_probe.py finding)")
    )
    print(f"\nVERDICT: {verdict}")
    w.add_data("verdict", verdict)
    out = w.save()
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
