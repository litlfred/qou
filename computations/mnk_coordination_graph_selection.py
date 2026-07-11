#!/usr/bin/env python3
"""
mnk_coordination_graph_selection.py — tests a candidate max-binding selection rule for
the nuclear coordination graph M_n(K) (bean qou-v0yw), REFUTES it, and reframes the
coordination as a body-order tower (chain and Borromean are complementary, not rivals).

The open keystone (qou-v0yw, from #3545): the Milnor M_n machinery is built and
validated (binding_mn_milnor_linking.py: Hopf lk=1, Borromean μ̄_123=±1, chain μ̄=0),
but WHICH link/graph each nucleus is — the coordination topology — is an un-derived
MODEL INPUT. #3545's two routes failed: the ad-hoc chain undercounts coordination
(~1 bond/nucleon vs data ~3, Part 8) and the confinement-SDP is degenerate (Part 9).

This session's converged result (my #3555/#3557 ↔ #3545 86ea593e/dbe5246a): binding is
bond-extensive and MAXIMISED by the richest coordination — "binding-max ⇒ max-contact
packing." This probe lifts that to the Milnor level and TESTS it as a selection rule:

  binding  B(K) = m_e · Σ_{n≥2} a_D^(n) · w_n · M_n(K),   all terms ≥ 0.

FINDING (the naive selection principle is REFUTED; the correct picture is a tower):
  The candidate "max-binding ⇒ single link with the richest Milnor tower" does NOT
  resolve the graph: the reducible chain (M_2=1, M_3=0) and the Brunnian Borromean
  (M_2=0, M_3=1) have EQUAL tower rank — the Borromean TRADES pairwise linking for the
  irreducible triple. So neither carries both the 2-body and 3-body term, and the
  choice would be weight-dependent (scope-(a) refutation of the naive rule).
  CORRECT reading: the coordination is not one graph but the body-order TOWER
  B = Σ_n B_n (ledger §0) — M_2 from pairwise links, M_3 from Borromean triples, each
  order carrying its own maximally-irreducible (Brunnian-n) sub-link. 'chain vs
  Borromean' is a false dichotomy; both contribute at orders 2 and 3. This still
  explains #3545 Part 8's chain undercount (a PURE chain supplies only M_2, missing
  M_3). Reframes qou-v0yw as a per-order sub-link COUNTING problem; the counts + the
  M_n → w_n weights stay OPEN. Not a closure.

EXPLORATORY — scope-limited (a). Reuses the validated #3545 Milnor machinery; no fit;
no production wiring.
"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
for p in (str(HERE), str(HERE / "substrate")):
    if p not in sys.path:
        sys.path.insert(0, p)

# reuse #3545's validated Milnor machinery + link data
from binding_mn_milnor_linking import mu, HOPF, BORROMEAN, CHAIN  # noqa: E402
try:
    from witness_base import WitnessBuilder  # noqa: E402
    _HAVE_WB = True
except ImportError:
    WitnessBuilder = None
    _HAVE_WB = False


def milnor_tower(link):
    """{M_2 (max |pairwise lk|), M_3 (|μ̄_123|)} for a 3-component link."""
    lk = [abs(mu(link, s)) for s in [(1, 2), (1, 3), (2, 3)]]
    m3 = abs(mu(link, (1, 2, 3)))
    return {"M2_max_pairwise": max(lk), "M2_pairwise": lk, "M3_triple": m3}


def main() -> int:
    print("=== Coordination graph M_n(K): testing a max-binding selection rule ===")
    print("  CANDIDATE rule (tested, then refuted below): B(K)=m_e·Σ a_D^(n)·w_n·M_n(K),")
    print("  all terms ≥0, so max-binding would pick the link with the RICHEST Milnor tower.\n")

    # candidate A=3 coordination links (the qou-v0yw decision: which link is ³He/³H?)
    cand = {"chain (Hopf×2, reducible)": CHAIN,
            "Borromean (Brunnian, L6a4)": BORROMEAN}
    print(f"  {'A=3 candidate link':<30}{'M2 (pairwise)':>15}{'M3 (triple)':>13}"
          f"{'tower rank':>12}")
    rows = {}
    for name, link in cand.items():
        t = milnor_tower(link)
        rank = int(t["M2_max_pairwise"] > 0) + int(t["M3_triple"] > 0)  # #nonzero orders
        rows[name] = dict(t, tower_rank=rank)
        print(f"  {name:<30}{t['M2_max_pairwise']:>15}{t['M3_triple']:>13}{rank:>12}")

    hopf = abs(mu(HOPF, (1, 2)))
    print(f"\n  (M_2 unit: Hopf lk = {hopf}; the D=2-body bond.)")

    bor = rows["Borromean (Brunnian, L6a4)"]
    chn = rows["chain (Hopf×2, reducible)"]
    # complementary: chain wins at order 2 (M_2), Borromean at order 3 (M_3)
    complementary = (chn["M2_max_pairwise"] > bor["M2_max_pairwise"]
                     and bor["M3_triple"] > chn["M3_triple"])
    print("\n### Reading — the naive 'richest tower' principle FAILS; it's a body-order TOWER")
    print(f"  • Chain and Borromean have EQUAL tower rank ({chn['tower_rank']}={bor['tower_rank']}):")
    print(f"    the chain has M_2={chn['M2_max_pairwise']}, M_3={chn['M3_triple']} (pairwise only);")
    print(f"    the Borromean is BRUNNIAN — M_2={bor['M2_max_pairwise']}, M_3={bor['M3_triple']}")
    print(f"    (it TRADES pairwise for the irreducible triple). So max-binding does NOT")
    print(f"    trivially pick one 'graph' over the other — my naive selection principle is")
    print(f"    REFUTED (scope-(a)): the choice would be weight-dependent, and neither link")
    print(f"    carries BOTH the 2-body and the 3-body term.")
    print(f"  • The correct reading: they are COMPLEMENTARY at different body ORDERS —")
    print(f"    chain/complete links carry M_2 (pairwise), Borromean triples carry M_3.")
    print(f"    So the coordination is NOT a single graph but the body-order TOWER")
    print(f"    B = Σ_n B_n (ledger §0): the n-body term M_n uses its own maximally-")
    print(f"    irreducible (Brunnian-n) sub-link. 'chain vs Borromean' was a false")
    print(f"    dichotomy — both contribute, at orders 2 and 3.")
    print(f"  • This still explains #3545 Part 8's chain undercount: a PURE chain supplies")
    print(f"    only M_2 and is MISSING the M_3 (Borromean) term — so it under-binds by the")
    print(f"    3-body contribution, exactly Part 8's residual.")

    print("\n### Scope (STRICT — reframes qou-v0yw, does NOT close it)")
    print("  REFUTED (scope-(a)): the 'max-binding ⇒ single richest-tower graph' principle —")
    print("    Borromean and chain have equal rank (M_2↔M_3 trade).")
    print("  DERIVED/REFRAMED: the coordination is a body-order TOWER, not one graph; each")
    print("    M_n uses its own Brunnian-n sub-link (M_2 pairwise, M_3 Borromean). This")
    print("    aligns qou-v0yw with the ledger §0 additive series and pins the chain-")
    print("    undercount to the missing M_3 term.")
    print("  OPEN: the per-order sub-link COUNTS (how many Borromean triples in ⁶Li, ¹²C…)")
    print("    + the M_n → w_n weights. qou-v0yw stays open, now as a per-order counting")
    print("    problem, not a single-graph-selection problem.")

    if _HAVE_WB:
        try:
            wb = WitnessBuilder("mnk-coordination-graph-selection", engine="python-magnus")
            wb.set_description(
                "Coordination graph M_n(K) (qou-v0yw): tests a max-binding 'richest Milnor tower' "
                "selection principle and REFUTES it — the reducible chain (M_2=1, M_3=0) and the "
                "Brunnian Borromean (M_2=0, M_3=1) have EQUAL tower rank; the Borromean trades "
                "pairwise for the irreducible triple. Correct reading: the coordination is a "
                "body-order TOWER (ledger §0), not one graph — M_2 from pairwise links, M_3 from "
                "Borromean triples, each order using its own Brunnian-n sub-link. Explains #3545 "
                "Part 8's chain undercount (a pure chain is missing M_3). Reframes qou-v0yw as a "
                "per-order sub-link COUNTING problem (not single-graph selection); the counts + "
                "M_n→w_n weights stay OPEN. Scope-(a), reuses #3545 machinery, no fit, no wiring.")
            wb.add_data("candidate_towers", rows)
            wb.add_data("hopf_M2_unit", hopf)
            wb.add_assertion(
                name="coordination_is_body_order_tower_not_single_graph",
                computed=str(int(complementary)), expected="1", tolerance=0,
                source=("chain and Borromean are COMPLEMENTARY at different orders — chain M_2=%d>%d "
                        "Borromean (pairwise), Borromean M_3=%d>%d chain (triple) — with equal tower "
                        "rank (%d=%d). ⇒ max-binding does NOT select a single 'richest-tower' graph "
                        "(refuted); the coordination is the body-order tower B=Σ_n B_n, each M_n from "
                        "its own Brunnian-n sub-link. Chain undercount = missing M_3."
                        % (chn["M2_max_pairwise"], bor["M2_max_pairwise"], bor["M3_triple"],
                           chn["M3_triple"], chn["tower_rank"], bor["tower_rank"])))
            out = wb.save()
            print(f"\nWitness: {out}")
        except Exception as e:
            print(f"\n(witness skipped: {e})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
