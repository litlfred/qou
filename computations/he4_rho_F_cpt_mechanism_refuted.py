"""ρ_F(⁴He) item-2 — the CPT alt-block-doubling mechanism is REFUTED under the canonical convention.

Arc bk-crossing-coordination, open item 2 (derive the magic-shell prefactor ρ_F(⁴He), equivalently
a_D^(4)). The corpus is internally split on its status:

  • `magic-A-binding-formula-context.md` (AUTHORITATIVE): "The categorical derivation of the integer
    2 — vs [2]_q, 2cos(π/3), or another natural candidate — is NOT closed ... the value is consumed
    as an input hypothesis."
  • `2026-08-02-he4-nu-sdp-decisive-2-not-3.md`: ρ_F=2 "is not derived"; data-implied 1.889.
  • `frobenius-packing-density.md` (OVER-CLAIMS): asserts ρ_F ∈ {m_e, 2m_e} is derived from a CPT
    mechanism — "closed-shell clusters saturate all blocks internally, [the alternating antiparticle
    channel] populated ⇒ CPT doubling ⇒ ρ_F = 2m_e ... derives the {m_e, 2m_e} threshold directly
    from the Frobenius pairing without phenomenological tuning."

This probe adjudicates by reading the canonical ⁴He Wedderburn decomposition.

## Result — the alt block is STRUCTURALLY EMPTY ⇒ the CPT mechanism cannot operate

Reading `chi-helium-4-h12-at-q0-50dps.witness.json` (convention: colour-weighted-averaged-crossing
= the canonical convention-D / colour-weighting per the 2026-08-15 owner ruling), the H₁₂ Frobenius
weights `y_λ` are:

  NONZERO (7 blocks, ALL ≤ 2 rows): [12], [11,1], [10,2], [9,3], [8,4], [7,5], [6,6]
  ZERO    (70 blocks, ALL > 2 rows): including the alternating channel [1¹²] and [2⁶]

So `y_[1¹²] = 0` exactly — the **alternating antiparticle channel is structurally empty** (exact
two-row dominance: `max rows among nonzero = 2`). The CPT-doubling mechanism requires that channel
POPULATED in order to double the density; it carries zero Frobenius mass, so there is nothing to
double. **`frobenius-packing-density.md`'s CPT derivation of ρ_F = 2m_e is refuted under the
canonical convention** (it is a convention-C-frame / pre-colour-weighting artifact). The
authoritative "not closed" status is correct.

## Consequence — the open problem is sharpened

ρ_F(⁴He) = 2 loses its one corpus candidate mechanism. Any derivation must now live INSIDE the
two-row stratum {[12],[11,1],[10,2],…,[6,6]} — the only blocks with nonzero colour-weighted
Frobenius mass — not in an alt-block CPT doubling. And the target itself is a rounded empirical
prefactor: data-implied ρ_F = B_AME/(m_e·A·8G) = 1.889, while the "natural" categorical candidates
overshoot (integer 2: +5.9%; [2]_q ≈ 2.011: +6.4%; 2cos(π/3) = 1: −47%). Scope-(a): the CPT
mechanism is tested and shown structurally unable (its required channel is empty); no reading of the
canonical decomposition supports it. No fit; no wiring; q₀ proton-anchored.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import _path_bridge  # noqa: F401, E402
import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
import q_parameter as qp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

HE4_WITNESS = HERE / "chi-helium-4-h12-at-q0-50dps.witness.json"
VOL_L6A4 = "7.327724753417752"   # 8G = Vol(L6a4) = Vol(Borromean)
B_AME_HE4 = "28.295674"


def main() -> int:
    set_compute_dps(50)
    w = json.load(open(HE4_WITNESS))
    conv = w.get("convention")
    bp = w["by_partition"]

    nonzero, zero = [], []
    for e in bp:
        lam = tuple(e["partition"])
        y = mp.mpf(str(e["y_lambda"]))
        (nonzero if y != 0 else zero).append((lam, y))
    max_rows_nonzero = max(len(l) for l, _ in nonzero)
    alt = tuple([1] * 12)
    y_alt = next((y for l, y in (nonzero + zero) if l == alt), None)
    all_zero_gt2 = all(len(l) > 2 for l, _ in zero)
    all_nonzero_le2 = all(len(l) <= 2 for l, _ in nonzero)

    print("=" * 78)
    print("ρ_F(⁴He) item-2 — CPT alt-block-doubling mechanism REFUTED (canonical convention)")
    print("=" * 78)
    print(f"  ⁴He witness convention: {conv}")
    print(f"  nonzero y_λ blocks ({len(nonzero)}), all ≤2 rows: {all_nonzero_le2}")
    for l, y in sorted(nonzero, key=lambda t: -t[1]):
        print(f"      λ={str(l):<16} rows={len(l)}  y={mp.nstr(y,6)}")
    print(f"  zero-weight blocks: {len(zero)}/{len(bp)}, all >2 rows: {all_zero_gt2}")
    print(f"  alternating channel  y_[1¹²] = {mp.nstr(y_alt,3)}  (max rows among nonzero = {max_rows_nonzero})")
    print("  ⇒ the alt/antiparticle channel is STRUCTURALLY EMPTY ⇒ CPT doubling has nothing to")
    print("    double ⇒ frobenius-packing-density.md's ρ_F=2m_e derivation is REFUTED under the")
    print("    canonical convention.")

    # candidate values vs data
    me = mp.mpf(str(qp.M_E_MEV))
    A8G = 4 * mp.mpf(VOL_L6A4)
    rho_data = mp.mpf(B_AME_HE4) / (me * A8G)
    q = qp.Q_MP
    two_q = q + 1 / q
    print("\n  ρ_F candidates vs data-implied 1.889:")
    print(f"      data B_AME/(m_e·A·8G) = {mp.nstr(rho_data,6)}")
    for name, val in [("integer 2", mp.mpf(2)), ("[2]_q", two_q), ("2cos(π/3)=1", mp.mpf(1))]:
        print(f"      {name:<14} = {mp.nstr(val,6)}  ({mp.nstr((val/rho_data-1)*100,4)}% vs data)")
    print("\n### Net (scope-a): CPT mechanism refuted under canonical convention; ρ_F=2 stays OPEN,")
    print("    and any derivation must live inside the two-row stratum (the only nonzero blocks).")

    ok = (y_alt == 0) and all_zero_gt2 and all_nonzero_le2 and (max_rows_nonzero == 2)
    wb = WitnessBuilder("he4-rho-F-cpt-mechanism-refuted", engine="python (mpf 50 dps; reads ⁴He H₁₂ witness)")
    wb.set_description(
        "Item 2 (ρ_F(⁴He) / a_D^(4)) adjudication. The canonical colour-weighted convention-D ⁴He H₁₂ "
        "decomposition (chi-helium-4-h12-at-q0-50dps) has EXACT two-row dominance: the 7 nonzero "
        "y_λ blocks all have ≤2 rows ([12],[11,1],[10,2],…,[6,6]); all 70 zero-weight blocks have >2 "
        "rows, including the alternating channel [1¹²] with y=0 exactly. So the CPT alt-block-doubling "
        "mechanism of frobenius-packing-density.md (closed shell populates the alt block ⇒ CPT "
        "doubling ⇒ ρ_F=2m_e) is REFUTED under the canonical convention — the alt channel is "
        "structurally empty, nothing to double; that block's 'derives ρ_F without tuning' claim is a "
        "convention-C-frame over-claim, and the authoritative 'not closed' status (magic-A context "
        "block) is correct. Sharpens the open problem: ρ_F=2 must be derived within the two-row "
        "stratum; the data-implied value is 1.889 (integer 2 overshoots +5.9%, [2]_q +6.4%). "
        "Scope-(a): mechanism tested and structurally unable. No fit; no wiring; q₀ proton-anchored.")
    wb.add_parameter("q0_anchor", "proton/experimental (q_parameter.Q_MP)")
    wb.add_parameter("he4_witness_convention", conv)
    wb.add_data("y_alt_block_1e12", mp.nstr(y_alt, 3))
    wb.add_data("n_nonzero_blocks", len(nonzero))
    wb.add_data("max_rows_among_nonzero", max_rows_nonzero)
    wb.add_data("rho_F_data_implied", mp.nstr(rho_data, 12))
    wb.add_assertion(
        name="alt_block_empty_cpt_doubling_refuted",
        computed=bool(ok), expected=True, tolerance=0,
        source=("Canonical ⁴He H₁₂ decomposition: alt channel y_[1¹²]=0 exactly, all nonzero blocks "
                "≤2 rows, all zero blocks >2 rows (exact two-row dominance). The CPT alt-block-doubling "
                "mechanism for ρ_F=2m_e requires the alt channel populated — it is structurally empty, "
                "so the mechanism is refuted under the canonical convention. ρ_F=2 stays open. No fit."))
    out = wb.save()
    print(f"\nWitness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
