#!/usr/bin/env python3
"""
Derive the α-α coupling binding c_αα via knot-operator decomposition
rather than positing m_e · Vol(7²_1) a priori.

Per prop:knot-operator-transition (content/.../braids-and-knots/
knot-operator-transition.md), the nucleon-addition knot-operators
along the light atomic chain are:

    p   → D      : σ_0 − h/2                   (single crossing, unknot)
    D   → ³H     : σ_1⁻¹ · (σ_0 − h/2)         (Hopf link)
    D   → ³He    : (σ_1 − h/2) · σ_0           (Hopf link)
    ³H  → ⁴He    : (σ_0 − h/2)(σ_1 − h/2)σ_0   (trefoil, T_{2,3})
    ³He → ⁴He    : (σ_0 − h/2)σ_1⁻¹(σ_0 − h/2) (trefoil, T_{2,3})

The 4th nucleon completes a TORUS knot (T_{2,3} = trefoil, which is
itself non-hyperbolic).  Adding a 5th nucleon (⁴He → ⁵Li or similar
unbound) or a 6th (⁴He + ⁴He → ⁸Be) adds MORE crossings to the braid.
The resulting closure MAY be hyperbolic even though the ingredient
trefoil was not.

The user's physical intuition:
    mass = ρ · Vol(hyperbolic JSJ pieces obtained by knot-operator
                    decomposition)

For ⁸Be = 2·⁴He + 1 (α-α) coupling:

  The α-α coupling operator adds an inter-⁴He crossing to the
  (trefoil ⊔ trefoil) initial state.  Closure of the combined braid
  is a link whose JSJ decomposition should split into:

    • 2× trefoil-like torus pieces (Vol = 0, Seifert-fibred)
    • 1× HYPERBOLIC α-α coupling piece of some Vol_αα

  Then c_αα = ρ · Vol_αα where ρ is the appropriate density.

This script:
  1. Builds the composite ⁸Be knot-operator braid symbolically
  2. Closes it in SnapPy to get the link
  3. Identifies JSJ pieces (torus + hyperbolic)
  4. Computes Vol of the hyperbolic piece(s)
  5. Compares m_e · Vol_αα to the target c_αα ≈ 2.427 MeV

If the derivation yields Vol_αα = Vol(7²_1) = 4.7495, then m_e·
Vol(7²_1) is NOT out of nowhere — it's the output of this pipeline.
Otherwise, the true Vol_αα tells us the correct α-α coupling.

Output: c-alpha-via-knot-operators.witness.json
"""
from __future__ import annotations

import math
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
sys.path.insert(0, str(Path(__file__).parent))

from hecke_core import h as H_A_VAL, q0 as Q_NUM
from q_parameter import Q as Q0
from experimental_constants import M_E_MEV
from witness_base import WitnessBuilder

try:
    import snappy as _snappy
    _SNAPPY = True
except ImportError:
    _snappy = None
    _SNAPPY = False


CATALAN_G = 0.915965594177219015054603514932
VOL_BORROMEAN = 8.0 * CATALAN_G
VOL_7_SQ_1_REF = 4.7494999818744385084980865556375718851941577840553
C_ALPHA_ASSUMED = M_E_MEV * VOL_7_SQ_1_REF
B_AME_12C = 92.161728
B_AME_8Be = 56.49951
B_AME_4He = 28.29569


# ─────────────────────────────────────────────────────────────────
# Knot-operator decomposition: what σ_i sequence makes up ⁸Be
# as (⁴He ⊔ ⁴He + α-α bond)?
# ─────────────────────────────────────────────────────────────────
# The two ⁴He are each a trefoil (T_{2,3}).  On 2 strands per α,
# total 4 strands for 2α.  The α-α bond adds crossings BETWEEN the
# two trefoil complexes.  With the Hecke convention for ud-half
# factors (1, -H_A/2), the simplest α-α coupling is a single
# inter-trefoil Hecke crossing.
#
# The PAIR LINK 7²_1 (Whitehead-like) = two 2-strand trefoils
# linked by a single crossing.  Let's build that explicitly.
#
# 7²_1 braid word on 4 strands:
#   σ_0 σ_1 σ_0      — trefoil on strands 0,1
#   σ_2              — link to strand 2
#   σ_2 σ_3 σ_2      — trefoil on strands 2,3
#   Closure = 7²_1 (L7a7 in SnapPy census)

def build_alpha_alpha_link_candidate() -> list[int]:
    """Return a signed braid word on 4 strands = two trefoils +
    inter-link crossing."""
    return [1, 2, 1, 3, 3, 4, 3]  # σ_0 σ_1 σ_0 σ_2 σ_2 σ_3 σ_2


def build_alpha_alpha_minimal_bond() -> list[int]:
    """Minimal α-α bond: two trefoils with a SINGLE crossing between
    them (a Whitehead-style linking).  On 4 strands."""
    return [1, 2, 1, 3, 4, 3, 3]


def closure_volume(word: list[int]) -> dict:
    """SnapPy closure + volume extraction."""
    if not _SNAPPY:
        return {"status": "snappy_missing"}
    try:
        L = _snappy.Link(braid_closure=word)
        E = L.exterior()
        v_raw = E.volume()
        v = float(v_raw.real) if hasattr(v_raw, "real") else float(v_raw)
        try:
            comps = len(L.link_components)
        except Exception:
            comps = None
        return {"volume": v, "components": comps,
                "is_hyperbolic": v > 1e-4,
                "braid_word": word,
                "crossings": len(word)}
    except Exception as e:
        return {"status": "error", "error": str(e), "braid_word": word}


def jsj_decomposition(word: list[int]) -> dict:
    """Return the JSJ-piece volume decomposition for the link closure.

    Uses SnapPy's `.decomposition()` if available.
    """
    if not _SNAPPY:
        return {"status": "snappy_missing"}
    try:
        L = _snappy.Link(braid_closure=word)
        M = L.exterior()
        # Check for toroidal JSJ structure
        pieces = []
        vol_total = float(M.volume().real) if hasattr(M.volume(), 'real') \
                    else float(M.volume())
        pieces.append({"type": "total", "volume": vol_total})
        # SnapPy's JSJ is somewhat limited; report total + basic info
        return {"total_volume": vol_total,
                "pieces": pieces,
                "note": "Full JSJ decomposition requires regina or explicit tori detection"}
    except Exception as e:
        return {"status": "error", "error": str(e)}


def main():
    w = WitnessBuilder("c-alpha-via-knot-operators",
                        engine="knot-op-decomposition + SnapPy")
    w.set_description(
        "Derive c_αα via the knot-operator decomposition of the "
        "α-α bond: close the composite braid, extract hyperbolic Vol, "
        "compute m_e · Vol.  Compare to the 'picked' m_e · Vol(7²_1) "
        "value to check whether the topological identification is a "
        "genuine prediction or an after-the-fact match."
    )
    w.add_parameter("m_e_MeV", M_E_MEV)
    w.add_parameter("q_0", float(Q0))
    w.add_parameter("c_alpha_assumed_m_e_Vol_7sq1", C_ALPHA_ASSUMED)
    w.add_parameter("B_AME_8Be", B_AME_8Be)
    w.add_parameter("B_AME_4He", B_AME_4He)

    print("=" * 100)
    print("c_αα VIA KNOT-OPERATOR DECOMPOSITION")
    print("=" * 100)
    print(f"  Target c_αα (from 8Be and 4He AME):")
    print(f"    c_αα = B(8Be) − 2·B(4He) = {B_AME_8Be:.4f} − 2·{B_AME_4He:.4f}")
    print(f"         = {B_AME_8Be - 2*B_AME_4He:.4f} MeV   (actually NEGATIVE — 8Be is")
    print(f"           unbound against 2α decay.)")
    print()
    print(f"  The 'assumed' framework value c_αα = m_e · Vol(7²_1):")
    print(f"    m_e         = {M_E_MEV:.6f} MeV")
    print(f"    Vol(7²_1)   = {VOL_7_SQ_1_REF:.6f}")
    print(f"    c_αα (fwk)  = {C_ALPHA_ASSUMED:.6f} MeV")
    print()
    print(f"  Note: real 8Be = 2α + 0 binding (unbound by ~90 keV).")
    print(f"  The framework 8Be formula 2·B(⁴He) + 1·c_αα uses c_αα as a")
    print(f"  POSITIVE correction — this is the bound-state α-cluster")
    print(f"  ansatz (not physical 8Be which is α-α unbound).")
    print()

    # Build candidate α-α braids
    print("─" * 100)
    print("Candidate α-α braid words (4 strands):")
    print("─" * 100)
    for name, word in [
        ("7²_1-like (trefoil ∪ trefoil + single link crossing)",
         build_alpha_alpha_link_candidate()),
        ("minimal α-α bond (two trefoils + 1 σ between)",
         build_alpha_alpha_minimal_bond()),
    ]:
        result = closure_volume(word)
        if "volume" in result:
            v = result["volume"]
            comps = result["components"]
            c_alpha_derived = M_E_MEV * v
            err = (c_alpha_derived - C_ALPHA_ASSUMED) / C_ALPHA_ASSUMED * 100
            print(f"  [{name}]")
            print(f"    braid word     : {word}")
            print(f"    closure Vol    : {v:.6f}   (hyperbolic: {result['is_hyperbolic']})")
            print(f"    components     : {comps}")
            print(f"    m_e · Vol      : {c_alpha_derived:.6f} MeV")
            print(f"    vs assumed     : {err:+.3f}% deviation from m_e·Vol(7²_1)")
        else:
            print(f"  [{name}] ERROR: {result}")
        print()

    # Reference: look up Vol(7²_1) directly
    print("─" * 100)
    print("Direct SnapPy lookup of 7²_1:")
    print("─" * 100)
    if _SNAPPY:
        try:
            M = _snappy.Manifold("L7a1")  # 7²_1 is often L7a7 in SnapPy; try several
            names_to_try = ["L7a1", "L7a2", "L7a3", "L7a4", "L7a5", "L7a6", "L7a7"]
            for name in names_to_try:
                try:
                    M = _snappy.Manifold(name)
                    v = float(M.volume().real) if hasattr(M.volume(), 'real') else float(M.volume())
                    if abs(v - VOL_7_SQ_1_REF) < 1e-4:
                        print(f"  SnapPy: {name} has Vol = {v:.10f} (matches 7²_1 reference)")
                        break
                except Exception:
                    pass
        except Exception as e:
            print(f"  lookup failed: {e}")
    print()

    # Alternative topological Check
    print("─" * 100)
    print("ALTERNATIVE: is the α-α bond really 7²_1 by framework derivation?")
    print("─" * 100)
    print(
        "  From prop:knot-operator-transition (content block):\n"
        "    ³H → ⁴He operator is (σ_0 − h/2)(σ_1 − h/2)σ_0  = trefoil (T_{2,3}).\n"
        "  \n"
        "  The *next* addition ⁴He → ⁵Li (unbound) would add another\n"
        "  knot operator.  Two ⁴He's linked as in ⁸Be correspond to a\n"
        "  pair of trefoils bridged by one or more Hecke crossings.\n"
        "\n"
        "  7²_1 is the 2-component link consisting of two trefoils\n"
        "  connected at ONE crossing (Whitehead-style).  If the paper's\n"
        "  framework identifies the α-α bond operator as exactly this\n"
        "  single-crossing bridge, then the closed α-α link IS 7²_1 —\n"
        "  not picked, but derived from the knot-operator hierarchy.\n"
        "\n"
        "  The RIGOROUS derivation (not done here) would:\n"
        "    (a) Identify the α-α inter-nucleon Hecke element from the\n"
        "        confinement SDP (2 α's = 8 strands, add min-crossing\n"
        "        inter-link σ's).\n"
        "    (b) Show that the closure is Markov-equivalent to 7²_1.\n"
        "    (c) Conclude c_αα = m_e · Vol(7²_1).\n"
        "\n"
        "  Step (b) is the MISSING piece.  The numerical coincidence\n"
        "  m_e · 4.7495 ≈ 2.427 MeV matches the α-cluster-formula\n"
        "  residual extracted from ¹²C, but the Markov-equivalence to\n"
        "  7²_1 is asserted, not proven.\n")

    w.add_data("braid_candidates", [
        {"name": "trefoil ∪ trefoil + link crossing",
         "word": build_alpha_alpha_link_candidate(),
         "closure": closure_volume(build_alpha_alpha_link_candidate())},
        {"name": "minimal α-α bond",
         "word": build_alpha_alpha_minimal_bond(),
         "closure": closure_volume(build_alpha_alpha_minimal_bond())},
    ])
    w.add_data("verdict", {
        "c_alpha_assumed_MeV": C_ALPHA_ASSUMED,
        "vol_7sq1_reference": VOL_7_SQ_1_REF,
        "status": (
            "Derivation INCOMPLETE: the Markov-equivalence of the "
            "α-α bond braid to the 7²_1 link class is the missing "
            "step.  Without it, m_e · Vol(7²_1) is a topological "
            "identification asserted by the framework (two linked "
            "trefoils = Whitehead-like) but not derived from the "
            "confinement SDP or the knot-operator hierarchy."
        ),
    })
    w.save()


if __name__ == "__main__":
    main()
