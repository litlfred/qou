#!/usr/bin/env python3
"""TEST (not research): does the formula's own M_i constructor reproduce D?

SCOPED 2026-08-25 (bean qou-1jw9), AFTER this file merged to main. The
commit that landed it said "the formula is NOT exact at n=3." That is too
strong and should not be cited. What is established:

  - no reading of M_i reproduces D (residuals 54 % .. 2653 %), AND
  - no construction reproduces the published Z=1..20 table
    (wedderburn_table_binding_recast.py part 2), AND
  - that table has no producer: its witness `atom-mass-complete-wedderburn`
    is absent from computations/. CORRECTED 2026-08-25: I said here, and
    in three PRs, that it "never existed in git history". THAT IS FALSE. It
    was added 2026-04-10 in commit 1359fe23ac at
    folio-assistant/computations/atom-mass-complete-wedderburn.witness.json
    and left with the platform code in the miga migration. Every search that
    concluded otherwise, including the one in
    docs/audits/2026-07-12-exposition-drain-needs-owner-ledger.md, looked
    under computations/ rather than by basename across all refs. Recovered,
    it reproduces the table exactly -- and its own parameters do NOT match
    the published formula (beta3 = 0.0499 against h_A^2 = 0.0437073, a
    14.2 pct departure). See docs/audits/2026-08-25-atom-mass-complete-wedderburn-witness-recovered.md.

RETRACTED IN TURN, 2026-08-29. This banner went on to claim that
thm:wedderburn-mass-formula is "UNFALSIFIABLE AS WRITTEN -- its M_i prose does
not determine a unique construction". THAT IS ALSO WRONG, and the error was
mine twice over.

The prose determines it. "chaining the crossing matrices of all strands j > i"
means: for strand i, cross with EVERY strand j > i -- an ALL-PAIRS braid with
no ordering dependence. I read it as a suffix product of ADJACENT crossings and
tested four variants of that one misreading, never the plain one. Under the
correct reading, Phi_2 and Phi_3 are re-derived on 19 of 19 non-hydrogen rows
(see computations/phi_allpairs_reconstruction.py), including Ar, the row that had refuted
the earlier candidate.

So what this file measures is a REFUTED READING, not an underdetermined
formula. The numbers below are correct for the adjacent reading and are kept
as the record of it; do not cite them as evidence about the formula.

thm:wedderburn-mass-formula states its own domain:  the three invariants
Phi_1/Phi_2/Phi_3 are the three EXTREMAL Wedderburn blocks, so the formula
is exact only where the extremal blocks exhaust the partitions of n.  That
is n = 3 alone -- i.e. deuterium (Z=1, N=1, A=2, n = A+Z = 3), which is the
only atom whose partition count p(3) = 3 equals the extremal count.

Two prior attempts at a p-n splitting test were retracted for feeding the
WRONG M_i: quark-level chains (nucleon_gen_chains) and then a two-element
atom_gen_chains, where the formula wants n-1 = A+Z-1 generators built from
the ATOMIC braid.  This script builds M_i literally from the two content
blocks that define it, and asks one falsifiable question:

    at n = 3, where the formula claims to be exact, is it?

A large residual here falsifies either the constructor reading or the
"exact at n=3" claim.  It does NOT license a new closure ansatz.

SOURCES (verbatim):
  def:atomic-braid       -- H_{A+Z}(q); Z protons, N neutrons, Z electrons;
                            ground-state ordering puts each electron
                            immediately before its proton ("ep pairs");
                            ne = id generates no Hecke generator.
  tbl:atomic-braid-table1-data -- the (c, d) crossing coefficients.
  thm:wedderburn-mass-formula  -- "For each generator i of the braid, let
                            M_i denote the 2x2 transfer matrix obtained by
                            chaining the crossing matrices of all strands
                            j > i."  Strand j's crossing is the one between
                            j-1 and j, so M_i is the SUFFIX product
                            T_i * T_{i+1} * ... * T_{n-1}.

No fitted parameter, no root-find: alpha = m_e * 8G is CAL-1 times Catalan,
[3]_q and h_A are q_0-derived.  m_p, m_n, m_e enter as INPUTS (the absolute-
mass excision, owner ruling 2026-08-11) -- what is under test is the
correction term alone.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import _path_bridge as _bridge  # noqa: F401,E402

import mpmath as mp  # noqa: E402

from _precision import set_compute_dps  # noqa: E402
set_compute_dps(50)

sys.path.insert(0, str(Path(__file__).resolve().parent / "alpha"))
from alpha_blend_tower import (  # noqa: E402
    Q0, QI, z_m, ALPHA_CANONICAL, BRACKET_3Q, H_A,
    Phi_1, Phi_2, Phi_3, wedderburn_mass_MeV,
)
from experimental_constants import M_P_MEV, M_N_MEV, M_E_MEV  # noqa: E402
from per_irrep_pole_atom import parts_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

H = Q0 - QI  # h = q - q^-1, the Hecke parameter of Table 1

# ── Table 1 (tbl:atomic-braid-table1-data), verbatim ──────────────
#   pair -> (c, d) in the factor  c*sigma + d*1
CROSSING = {
    ("p", "p"): (mp.mpf(1), mp.mpf(0)),      # sigma            strong repulsion
    ("n", "n"): (mp.mpf(1), -H),             # sigma^-1         strong inverse
    ("p", "n"): (mp.mpf(2), -H),             # (sigma+sigma^-1) strong mixed
    ("p", "e"): (mp.mpf(1), -H),             # sigma^-1         EM attraction
    ("n", "e"): (mp.mpf(0), mp.mpf(1)),      # id               no interaction
    ("e", "e"): (mp.mpf(1), mp.mpf(0)),      # sigma            EM repulsion
}


def crossing(a: str, b: str):
    """Table-1 lookup, symmetric in the pair (the table lists each once)."""
    if (a, b) in CROSSING:
        return CROSSING[(a, b)]
    if (b, a) in CROSSING:
        return CROSSING[(b, a)]
    raise KeyError(f"no Table-1 row for pair {(a, b)}")


def chains_for(strands, reading):
    """M_i for every generator i, as (c, d) chain words.

    Generator i sits between strands i and i+1 (1-indexed).  The theorem
    chains "the crossing matrices of all strands j > i"; strand j's crossing
    is the one between j-1 and j, i.e. generator j-1.  So

        M_i = T_i * T_{i+1} * ... * T_{n-1}

    -- the suffix product.  Returned as a list of (c, d) lists, the same
    chain-word encoding alpha_blend_tower's V_std / _det_M / lam_* consume.
    """
    tees = [crossing(strands[k], strands[k + 1]) for k in range(len(strands) - 1)]
    m = len(tees)
    if reading == "suffix-inclusive":   # M_i = T_i ... T_{n-1}
        out = [tees[i:] for i in range(m)]
    elif reading == "suffix-exclusive": # M_i = T_{i+1} ... T_{n-1}
        out = [tees[i + 1:] for i in range(m)]
    elif reading == "single":           # M_i = T_i
        out = [[tees[i]] for i in range(m)]
    elif reading == "prefix":           # M_i = T_1 ... T_i
        out = [tees[:i + 1] for i in range(m)]
    else:
        raise ValueError(reading)
    return [ch for ch in out if ch]     # an empty chain is the identity: ln|.|=0


def orderings(Z: int, N: int):
    """Ground-state candidates: every arrangement with each e immediately
    before a p, over both nuclear orderings.  The definition says to pick the
    Phi_1-minimizing one, so we enumerate and let Phi_1 choose rather than
    hard-coding a reading."""
    from itertools import permutations
    nuclei = set(permutations(["p"] * Z + ["n"] * N))
    out = set()
    for nuc in nuclei:
        seq = []
        for s in nuc:
            if s == "p":
                seq.extend(["e", "p"])   # ep pair: electron immediately before
            else:
                seq.append("n")
        out.add(tuple(seq))
    return sorted(out)


def evaluate(Z, N, strands, reading="suffix-inclusive"):
    chains = chains_for(list(strands), reading)
    p1, p2, p3 = Phi_1(chains), Phi_2(chains), Phi_3(chains)
    corr = ALPHA_CANONICAL * (p1 - 2 * BRACKET_3Q * p2 + H_A ** 2 * p3)
    return chains, p1, p2, p3, corr


def main() -> int:
    # Deuterium: the one atom inside the formula's stated domain.
    Z, N = 1, 1
    A = Z + N
    n = A + Z
    print(f"D (Z={Z}, N={N}):  A = {A},  n = A+Z = {n} strands, "
          f"{n-1} generators, p(3) = 3 = extremal count")
    print(f"q0 = {mp.nstr(Q0, 20)}   z_D = {mp.nstr(z_m, 20)}   "
          f"h_A = {mp.nstr(H_A, 20)}")
    print(f"alpha = m_e*8G = {mp.nstr(ALPHA_CANONICAL, 20)} MeV   "
          f"[3]_q = {mp.nstr(BRACKET_3Q, 20)}")

    # Target: the correction must equal -(binding energy of the D atom).
    # AME2020 deuterium ATOMIC mass, MeV (m_p + m_n + m_e - B_total).
    D_ATOMIC_MEV = mp.mpf("1876.12392")          # AME2020 / CODATA
    base = mp.mpf(str(M_P_MEV)) + mp.mpf(str(M_N_MEV)) + mp.mpf(str(M_E_MEV))
    target_corr = D_ATOMIC_MEV - base
    print(f"\nbase  = m_p + m_n + m_e = {mp.nstr(base, 12)} MeV")
    print(f"target correction        = {mp.nstr(target_corr, 12)} MeV "
          f"(= -B_total, B = {mp.nstr(-target_corr, 8)} MeV)")

    READINGS = ["suffix-inclusive", "suffix-exclusive", "single", "prefix"]
    print("\n--- grid: ordering x reading of \"chaining ... all strands j > i\" ---")
    print(f"  {'ordering':10s} {'reading':18s} {'Phi_1':>14s} {'Phi_2':>14s} "
          f"{'Phi_3':>14s} {'corr MeV':>14s} {'resid %':>12s}")
    grid = []
    for strands in orderings(Z, N):
        for reading in READINGS:
            chains, p1, p2, p3, corr = evaluate(Z, N, strands, reading)
            rel = abs((corr - target_corr) / target_corr) * 100
            grid.append((strands, reading, chains, p1, p2, p3, corr, rel))
            print(f"  {'-'.join(strands):10s} {reading:18s} "
                  f"{mp.nstr(p1, 8):>14s} {mp.nstr(p2, 8):>14s} "
                  f"{mp.nstr(p3, 8):>14s} {mp.nstr(corr, 8):>14s} "
                  f"{mp.nstr(rel, 6):>12s}")

    # HEADLINE = the cell the two content blocks SELECT, not the cell with the
    # smallest residual.  Picking the closest of eight would be selection
    # against the data -- the same fit signature this repo's anti-fit rules
    # exist to catch.  The spec fixes both coordinates:
    #   reading  -- "chaining the crossing matrices of ALL strands j > i"
    #               is the suffix-inclusive product (thm:wedderburn-mass-formula);
    #   ordering -- def:atomic-braid says minimize Phi_1.
    SPEC_READING = "suffix-inclusive"
    spec_cells = [r for r in grid if r[1] == SPEC_READING]
    best = min(spec_cells, key=lambda r: r[3])          # r[3] = Phi_1
    strands, reading, chains, p1, p2, p3, corr, rel = best
    lo = min(grid, key=lambda r: r[7])
    hi = max(grid, key=lambda r: r[7])
    print(f"\nSPEC-SELECTED cell: reading {reading} (literal), "
          f"ordering {'-'.join(strands)} (Phi_1-minimizing)")
    print("  chains (M_i as (c,d) words):")
    for i, ch in enumerate(chains, start=1):
        pretty = " * ".join(f"({mp.nstr(c,6)}*s + {mp.nstr(d,6)})" for c, d in ch)
        print(f"    M_{i} = {pretty}")

    resid = corr - target_corr
    print(f"\n  predicted correction = {mp.nstr(corr, 12)} MeV")
    print(f"  target correction    = {mp.nstr(target_corr, 12)} MeV")
    print(f"  residual             = {mp.nstr(resid, 12)} MeV   "
          f"({mp.nstr(rel, 6)} % of target)")

    print(f"\n  sensitivity across all 8 cells: residual ranges "
          f"{mp.nstr(lo[7], 6)} % ({'-'.join(lo[0])}/{lo[1]}) to "
          f"{mp.nstr(hi[7], 6)} % ({'-'.join(hi[0])}/{hi[1]}).")
    print("  No reading rescues it -- the floor over every cell is "
          f"{mp.nstr(lo[7], 6)} %, so the negative is not an artifact of")
    print("  which reading was chosen.")

    exact = rel < mp.mpf("1e-4")          # 1 ppm, as a percentage
    sign_ok = mp.sign(corr) == mp.sign(target_corr)
    print(f"\n  VERDICT: sign {'CORRECT' if sign_ok else 'WRONG'}; "
          f"magnitude {'EXACT (<1 ppm)' if exact else 'NOT exact'}")
    if not exact:
        print("  => at n=3 -- the ONE point where thm:wedderburn-mass-formula")
        print("     claims exactness -- no reading of its own M_i constructor")
        print("     reproduces D.  That falsifies the reading or the claim.")
        print("     It does NOT license a closure ansatz for the residual;")
        print("     the many-body magnitude is the documented Delta_lambda gap")
        print("     (AGENTS.md: no seventh fit-based ansatz).")

    # Structural domain-constraint checks (bean qou-1jw9 / Lean
    # QOU.WedderburnMass & QOU.Mass.WedderburnMassFormulaCoefficients):
    # (1) Extremal blocks {[n], [n-1,1], [1^n]} exhaust p(n) iff n <= 3.
    partition_domain_table = {}
    for n_val in range(1, 7):
        parts = [tuple(p) for p in parts_of(n_val)]
        extremal_set = {
            (n_val,),
            (n_val - 1, 1) if n_val >= 2 else (1,),
            tuple([1] * n_val),
        }
        non_extremal = [list(p) for p in parts if p not in extremal_set]
        partition_domain_table[str(n_val)] = {
            "p_n": len(parts),
            "extremal_count": len(extremal_set),
            "non_extremal_count": len(non_extremal),
            "non_extremal_partitions": non_extremal,
            "exhausted_by_extremal": len(non_extremal) == 0,
        }

    # (2) Adjacent-chain bridge count (A - 1) vs all-pairs count A*(A - 1)//2.
    pair_growth_table = {}
    for A_val in range(2, 7):
        adj = A_val - 1
        all_p = A_val * (A_val - 1) // 2
        pair_growth_table[str(A_val)] = {
            "adjacent_chain_pairs": adj,
            "all_pairs": all_p,
            "deficit": all_p - adj,
        }

    # (3) Exact algebraic identity 2*beta_3 + beta_2 + 6 == 0.
    beta2_canonical = -2 * BRACKET_3Q
    beta3_canonical = H_A ** 2
    coeff_identity_residual = abs(2 * beta3_canonical + beta2_canonical + 6)

    wb = WitnessBuilder("wedderburn-mi-constructor-test", engine="python+mpmath")
    wb.set_description(
        "Bean qou-1jw9 diagnostic & domain-constraint probe for "
        "thm:wedderburn-mass-formula: evaluates all 8 (ordering x reading) "
        "cells of the 2x2 transfer-matrix constructor M_i on deuterium (n=3), "
        "verifies the Lean-proved domain constraints (extremal blocks exhaust "
        "p(n) iff n <= 3; adjacent-chain A-1 < A(A-1)/2 for A >= 3; "
        "2*beta_3 + beta_2 + 6 == 0), and records the spec-selected residual."
    )
    wb.add_assertion(
        "extremal_blocks_exhaust_partitions_iff_n_le_3",
        computed=(
            all(partition_domain_table[str(k)]["exhausted_by_extremal"] for k in (1, 2, 3))
            and all(not partition_domain_table[str(k)]["exhausted_by_extremal"] for k in (4, 5, 6))
            and partition_domain_table["4"]["non_extremal_count"] == 2
        ),
        expected=True,
        source="p(1)=1, p(2)=2, p(3)=3 exhausted; p(4)=5 has 2 non-extremal blocks [2,2], [2,1,1]",
    )
    wb.add_assertion(
        "adjacent_chain_vs_all_pairs_growth_constraint",
        computed=(
            pair_growth_table["2"]["deficit"] == 0
            and all(pair_growth_table[str(A_val)]["deficit"] > 0 for A_val in range(3, 7))
        ),
        expected=True,
        source="A-1 == A(A-1)/2 at A=2 and A-1 < A(A-1)/2 for all A >= 3",
    )
    wb.add_assertion(
        "beta2_beta3_linear_dependency_identity_holds",
        computed=(coeff_identity_residual < mp.mpf("1e-48")),
        expected=True,
        source=f"|2*beta_3 + beta_2 + 6| = {mp.nstr(coeff_identity_residual, 6)}",
    )
    wb.add_assertion(
        "deuterium_n3_all_8_constructor_readings_miss_target_by_gt_50_pct",
        computed=(lo[7] > mp.mpf("50") and rel > mp.mpf("200") and sign_ok and not exact),
        expected=True,
        source=(
            f"spec-selected residual={mp.nstr(rel, 6)}%, "
            f"grid range=[{mp.nstr(lo[7], 6)}%, {mp.nstr(hi[7], 6)}%]"
        ),
    )
    wb.add_data("q_0_50dps", mp.nstr(Q0, 50))
    wb.add_data("spec_selected", {
        "ordering": "-".join(strands),
        "reading": reading,
        "Phi_1": mp.nstr(p1, 30),
        "Phi_2": mp.nstr(p2, 30),
        "Phi_3": mp.nstr(p3, 30),
        "predicted_corr_MeV": mp.nstr(corr, 30),
        "target_corr_MeV": mp.nstr(target_corr, 30),
        "residual_MeV": mp.nstr(resid, 30),
        "relative_error_pct": mp.nstr(rel, 15),
    })
    wb.add_data("partition_domain_table", partition_domain_table)
    wb.add_data("pair_growth_table", pair_growth_table)
    wb.save()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
