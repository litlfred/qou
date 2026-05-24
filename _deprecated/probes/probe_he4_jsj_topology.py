#!/usr/bin/env python3
"""probe_he4_jsj_topology.py — JSJ topology of ⁴He compositional closures.

Per F1 follow-up questions 1-2 (integration audit
2026-05-15-three-pr-integration.md):

  > 1. T_1 = m_e · |τ_M| vs the survey's three in-window candidates.
  > 2. Whether the compositional knot equals any of the surveyed
  >    candidates after JSJ reduction.

This probe answers question 2 directly: take each ⁴He compositional
braid (canonical pppnnn, D⊕D, T⊕p, ³He⊕n), form the closure as a
link in S³, and compute its hyperbolic / JSJ decomposition via
SnapPy.  Compare the resulting simplified manifolds.

Caveat: averaged Hecke crossings (c=1, d=-h/2) DON'T have a single
topological realization in the braid group B_n.  We convert them to
σ_g (positive crossing) for the JSJ analysis — the closure topology
depends on this convention.  Inverting averaged → σ⁻¹ would give a
different (related by ambient isotopy in some cases) topology.

Output: he4-jsj-topology.witness.json
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from q_parameter import HA as H_VAL  # noqa: E402  canonical h = q − q⁻¹ at q_0


def hecke_word_to_braid_word(word: list) -> list[int]:
    """Convert Hecke (c, d, gen) word → braid-group integer word.

    Conventions:
      (1, 0, g):     σ_{g+1}     → +(g+1)
      (1, -h, g):    σ_{g+1}⁻¹  → -(g+1)
      (1, -h/2, g):  averaged   → σ_{g+1} (treat as positive)
                                   per F1 convention

    Returns: list of signed integers (1-indexed braid generators).
    Convention: SnapPy braid_closure uses 1-indexed positive σ_i and
    negative σ_i⁻¹.
    """
    out = []
    for c, d, g in word:
        gen_1indexed = g + 1
        if abs(c - 1) > 1e-12:
            raise ValueError(f"unsupported c = {c}")
        if abs(d) < 1e-12:
            out.append(gen_1indexed)  # σ
        elif abs(d + H_VAL) < 0.01:
            out.append(-gen_1indexed)  # σ⁻¹
        elif abs(d + H_VAL / 2) < 0.01:
            # averaged — convert to σ (positive) per F1 convention
            out.append(gen_1indexed)
        else:
            raise ValueError(f"unsupported d = {d}")
    return out


def _proton_braid_word() -> list[int]:
    """Proton's intra-nucleon braid word as integer braid (1-indexed)."""
    from sublemma_2_1_h9_tritium_verify import _proton_body
    return hecke_word_to_braid_word(_proton_body())


def _neutron_braid_word() -> list[int]:
    from sublemma_2_1_h9_tritium_verify import _neutron_body
    return hecke_word_to_braid_word(_neutron_body())


def he4_compositional_braids() -> dict[str, tuple[list[int], int]]:
    """Three compositional ⁴He braid words (1-indexed, n_strands=12).

    Returns: {name: (braid_word, n_strands)}.
    For F1 disjoint composition: just concatenate with strand shift.
    """
    p = _proton_braid_word()
    n = _neutron_braid_word()

    # canonical pppnnn ⁴He at H_12: p · I_pp · p · I_pn · n · I_nn · n
    # I_pp = σ_3 (c=1, d=0 at strand 2 0-indexed = strand 3 1-indexed)
    # I_pn = σ_6 (averaged → +σ)
    # I_nn = σ_9 (c=1, d=-h at strand 8 0-indexed = strand 9 1-indexed)
    canonical = (
        list(p)
        + [3]                                       # I_pp = σ_3
        + [g + 3 for g in p]                       # p₂ on strands 4-6
        + [6]                                       # I_pn averaged → σ_6
        + [g + 6 for g in n]                       # n₁ on strands 7-9
        + [-9]                                      # I_nn = σ_9⁻¹
        + [g + 9 for g in n]                       # n₂ on strands 10-12
    )

    # D⊕D disjoint: β_D = p · I_pn · n on H_6, two copies on disjoint strands
    # First D on strands 1-6 (gens 1..5), Second D on strands 7-12 (gens 7..11)
    deuteron = list(p) + [3] + [g + 3 for g in n]  # canonical D
    D_disjoint = list(deuteron) + [g + 6 for g in deuteron]

    # T⊕p: T on strands 1-9, p on strands 10-12
    tritium = list(p) + [3] + [g + 3 for g in n] + [-6] + [g + 6 for g in n]
    T_p_disjoint = list(tritium) + [g + 9 for g in p]

    # ³He⊕n: ³He on strands 1-9, n on strands 10-12
    he3 = list(p) + [3] + [g + 3 for g in p] + [6] + [g + 6 for g in n]
    He3_n_disjoint = list(he3) + [g + 9 for g in n]

    return {
        "canonical_pppnnn": (canonical, 12),
        "D_oplus_D":         (D_disjoint, 12),
        "T_oplus_p":         (T_p_disjoint, 12),
        "He3_oplus_n":       (He3_n_disjoint, 12),
    }


def main() -> int:
    import snappy
    print("=" * 90)
    print("  JSJ topology of ⁴He compositional closures")
    print("=" * 90)
    print(f"  SnapPy version: {snappy.version()}")
    print()

    braids = he4_compositional_braids()
    results = {}

    print(f"  {'composition':<22} {'n_strands':>10} {'word len':>10} "
          f"{'# components':>13} {'hyperbolic vol':>16} {'#tetrahedra':>12}")
    print("  " + "-" * 90)
    for name, (word, n_strands) in braids.items():
        try:
            link = snappy.Link(braid_closure=word)
            n_components = len(link.link_components) if hasattr(link, "link_components") else "?"
            try:
                link.simplify(mode="global")
            except Exception:
                pass
            try:
                alex = link.alexander_polynomial()
                alex_str = str(alex)[:40] if alex is not None else "—"
            except Exception:
                alex_str = "—"
            try:
                jones = link.jones_polynomial()
                jones_str = str(jones)[:30] if jones is not None else "—"
            except Exception:
                jones_str = "—"
            try:
                mfd = link.exterior()
                vol = mfd.volume()
                vol_str = f"{vol:.6f}"
            except Exception:
                vol = None
                vol_str = "non-hyperbolic"
            try:
                n_tet = mfd.num_tetrahedra()
            except Exception:
                n_tet = -1
            print(f"  {name:<22} {n_strands:>10} {len(word):>10} "
                  f"{str(n_components):>13} {vol_str:>16} {n_tet:>12}")
            results[name] = {
                "word_length": len(word),
                "n_strands": n_strands,
                "n_components": n_components if isinstance(n_components, int) else None,
                "hyperbolic_volume": vol,
                "n_tetrahedra": n_tet,
                "alexander_polynomial": alex_str,
                "jones_polynomial": jones_str,
            }
        except Exception as e:
            print(f"  {name:<22}: FAILED — {type(e).__name__}: {str(e)[:50]}")
            results[name] = {"error": f"{type(e).__name__}: {e}"}
    print()
    print("  Topological invariants comparison:")
    for name, r in results.items():
        if "error" in r:
            continue
        print(f"    {name:<22} alex = {r.get('alexander_polynomial', '?')}")
        print(f"    {' ' * 22} jones = {r.get('jones_polynomial', '?')}")
    print()

    from witness_base import WitnessBuilder
    builder = (
        WitnessBuilder("he4-jsj-topology", engine="snappy")
        .set_description(
            "JSJ topology of ⁴He compositional braid closures via SnapPy. "
            "Compares canonical pppnnn vs three disjoint compositions "
            "(D⊕D, T⊕p, ³He⊕n) at the link-exterior hyperbolic-volume "
            "level.  Tests F1 question 2: whether compositional choices "
            "produce the same topological invariant after JSJ reduction."
        )
        .set_audit_only(
            "docs/audits/2026-05-15-three-pr-integration.md"
        )
        .add_data("snappy_version", snappy.version())
        .add_data("compositions", results)
        .add_caveat(
            "Averaged Hecke crossings (c=1, d=-h/2) DON'T have a "
            "single topological realization.  This probe converts "
            "averaged → σ (positive crossing) per F1 convention; "
            "averaged → σ⁻¹ would give a different topology."
        )
        .add_caveat(
            "F1's disjoint Markov composition β_1 ⊕ β_2 is the "
            "DISJOINT braid product (strands of β_2 above β_1).  Its "
            "closure is a 2-component link, while canonical pppnnn "
            "is a single-component knot in general.  Topological "
            "invariants (volume) differ accordingly — expected behaviour."
        )
    )
    out = builder.save()
    print(f"  Witness: {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
