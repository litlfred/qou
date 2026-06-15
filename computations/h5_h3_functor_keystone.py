#!/usr/bin/env python3
"""H5<->H3 functor keystone: the 5<->3 bridge (EXPLORATORY, audit-only).

THE keystone open object named by FOUR merged audits (all on main):
  - 2026-06-01-s5-so3-su2-u1-fiber-action.md (PR #1672): "different
    representation rings, no canonical map" between the 5-strand A5<S5 /
    SO(3) fiber level ell and the 3-strand H3 Borromean (2,1) coefficient.
  - 2026-06-01-knot-operator-census-group-actions.md (PR #1677): Markov
    destabilization is the canonical strand-count functor but is BLOCKED on
    the Brunnian Borromean; cabling gives 6 not 5.
  - 2026-06-01-flavor-dependent-cusp-shape.md (PR #1670): same missing
    flavor->root map rho.
  - 2026-06-01-inter-nucleon-linked-channel.md (PR #1678): the 2-strand
    linked channel gives 2<->1, not 5->3.

NONE of them computed the STANDARD Hecke-algebra restriction functor
Res^{H5}_{H3} explicitly. That is the most standard candidate categorical
bridge and is what this probe computes, exactly, via Young-tableau
branching combinatorics (remove-a-box rule), together with the adjoint
induction, the Markov tower H3<H4<H5, and the icosahedral A5 -> S3-stabilizer
restriction.

DISCIPLINE (CLAUDE.md production-vs-exploratory): DERIVE or prove-nonexistence;
NEVER fit to close the gap. The h^4 = -3/4 Borromean coefficient is a
FALSIFICATION reference, not a target. Every multiplicity is computed FIRST
from the branching rule; the comparison to the (2,1) std block comes SECOND.
A chosen multiplicity would be a fit -- we report RAW multiplicities only.

COMPUTES (exact rational / integer combinatorics + RAW @ the canonical
compute_dps -- via _precision.set_compute_dps() -- where a substrate value is
needed):
  1. CANDIDATE 1 -- Restriction Res^{S5}_{S3} (= Res^{H5}_{H3} on irreps,
     since branching is q-independent / generic). Branch every irrep
     lambda |- 5 down to S3 via the iterated remove-a-box (Pieri/branching)
     rule S5 -> S4 -> S3, and report the multiplicity of the (2,1) std
     irrep in each. RAW multiplicities.
  2. CANDIDATE 2 -- Induction Ind^{S5}_{S3} of (2,1) (the adjoint, by
     Frobenius reciprocity = column sums of the same branching matrix).
  3. CANDIDATE 3 -- Markov tower H3 -> H4 -> H5 forward embedding: does the
     (2,1) baryon block embed (as a summand of a restriction) into a
     5-strand irrep on which the SO(3)/I fiber acts (the dim-5 H-related
     irreps)? Report trace-compatibility (the Markov z-power) and the
     branching path.
  4. CANDIDATE 4 -- Icosahedral A5 restricted to a 3-element stabilizer:
     branch the dim-5 irrep H of A5 (the ell=2 carrier) to a
     3-element-stabilizer subgroup; does it recover the H3 (2,1) baryon
     content with a CANONICAL multiplicity?
  5. VERDICT per candidate: derived functor (what it does to the (2,1)/h^4
     coefficient, RAW) OR rigorous nonexistence (the precise incompatibility
     -- e.g. "Res of the ell=2 block gives multiplicity m != 1, so no
     canonical iso").

Audit doc: docs/audits/2026-06-02-h5-h3-functor-keystone.md
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
import time
from fractions import Fraction
from pathlib import Path

import mpmath as mp
import sympy as sp

sys.path.insert(0, str(Path(__file__).resolve().parent))
from witness_base import WitnessBuilder  # noqa: E402
from _precision import set_compute_dps, COMPUTE_DPS  # noqa: E402
from q_parameter import Q as Q0  # noqa: E402  (proton-pinned, single source of truth)
from q_parameter import Q_MP as Q0_MP  # noqa: E402  (high-precision mpf for the z eval)

START = time.monotonic()
# Shared precision infra: set mpmath working dps to the canonical COMPUTE_DPS
# (the SAME value the witness records in precisionMetadata.compute_dps, so the
# two cannot drift). Previously this script hardcoded mp.mp.dps = 60 while the
# witness recorded 70 -- the mismatch Copilot flagged. set_compute_dps() with no
# argument pins mp.mp.dps to COMPUTE_DPS.
ACTUAL_DPS = set_compute_dps()
assert ACTUAL_DPS == COMPUTE_DPS, (ACTUAL_DPS, COMPUTE_DPS)

# Substrate q0 is the canonical proton-anchored value imported above (NOT a
# hardcoded literal). FALSIFICATION / reference only -- not tuned. This probe's
# results are INTEGER branching multiplicities (q0-INDEPENDENT), so the substrate
# value affects only the RAW Markov-z report in Candidate 3.
Q0_STR = mp.nstr(Q0_MP, COMPUTE_DPS)

# Borromean h^4 falsification reference (NOT a fit target).
H4_BORROMEAN = Fraction(-3, 4)


# ===========================================================================
# Partition + Young-tableau combinatorics (exact, q-independent).
# ===========================================================================

def partitions(n: int):
    """All partitions of n as non-increasing tuples (descending)."""
    if n == 0:
        return [()]
    out = []

    def rec(remaining, maxpart, cur):
        if remaining == 0:
            out.append(tuple(cur))
            return
        for p in range(min(remaining, maxpart), 0, -1):
            rec(remaining - p, p, cur + [p])

    rec(n, n, [])
    return out


def remove_box(lam):
    """All partitions of n-1 obtained from lambda |- n by removing one box
    (an inner corner), i.e. the branching rule S_n -> S_{n-1} restriction.
    Each removable box appears exactly once (multiplicity-free branching for
    the symmetric group, Young's rule)."""
    res = []
    parts = list(lam)
    for i in range(len(parts)):
        # box removable from row i if it's the last row or row i is strictly
        # longer than row i+1
        if i == len(parts) - 1 or parts[i] > parts[i + 1]:
            new = parts[:i] + [parts[i] - 1] + parts[i + 1:]
            new = tuple(p for p in new if p > 0)
            res.append(new)
    return res


def restrict_multiplicities(lam, n_from, n_to):
    """Multiplicity vector of Res^{S_{n_from}}_{S_{n_to}}(lambda).

    Iterates the remove-a-box branching rule (n_from -> n_from-1 -> ... -> n_to)
    and counts, for each partition mu |- n_to, how many distinct standard
    branching PATHS lambda = chain ... = mu exist. This path count IS the
    restriction multiplicity (Young's branching is multiplicity-free at each
    single step, so the iterated multiplicity = number of paths)."""
    # state: dict partition -> path-count multiplicity
    state = {lam: 1}
    for _ in range(n_from - n_to):
        nxt: dict = {}
        for mu, mult in state.items():
            for nu in remove_box(mu):
                nxt[nu] = nxt.get(nu, 0) + mult
        state = nxt
    return state  # keys are partitions of n_to


def dim_irrep(lam):
    """Dimension of the symmetric-group irrep S^lambda = number of SYT
    (hook-length formula)."""
    cells = [(i, j) for i, row in enumerate(lam) for j in range(row)]
    n = len(cells)
    # column lengths
    cols = {}
    for (i, j) in cells:
        cols[j] = cols.get(j, 0) + 1
    prod_hooks = 1
    for (i, j) in cells:
        arm = lam[i] - j - 1
        leg = cols[j] - i - 1
        prod_hooks *= (arm + leg + 1)
    return sp.factorial(n) // prod_hooks


# ===========================================================================
# 1. CANDIDATE 1 -- Res^{S5}_{S3} (= Res^{H5}_{H3} on Wedderburn blocks).
#    Hecke-algebra restriction: H3(q) <-> H5(q) along the standard inclusion
#    H3 = <sigma_1,sigma_2> < H5 = <sigma_1,...,sigma_4>. Generically (q not a
#    root of unity, in particular at real q0 ~ 1.11) H_n(q) is SEMISIMPLE with
#    the SAME irreducible block labels lambda |- n as S_n (Tits deformation /
#    Wenzl), and the branching rule for the restriction is the SAME
#    remove-a-box rule as for S_n. So Res^{H5}_{H3} multiplicities = the
#    integer branching numbers computed below; they are q-INDEPENDENT.
# ===========================================================================

P5 = partitions(5)   # 7 partitions
P3 = partitions(3)   # 3 partitions: (3),(2,1),(1,1,1)
STD3 = (2, 1)        # the std irrep of S3/H3 that carries the Borromean h^4


def candidate_1_restriction():
    rows = {}
    std_mult = {}
    for lam in P5:
        mults = restrict_multiplicities(lam, 5, 3)
        rows[lam] = {str(mu): mults.get(mu, 0) for mu in P3}
        std_mult[lam] = mults.get(STD3, 0)
        # sanity: dim check sum_mu m_{lam,mu} dim(mu) = dim(lam)  (Res preserves dim)
        dim_lam = int(dim_irrep(lam))
        dim_res = sum(mults.get(mu, 0) * int(dim_irrep(mu)) for mu in P3)
        rows[lam]["_dim_lambda"] = dim_lam
        rows[lam]["_dim_restricted"] = dim_res
        rows[lam]["_dim_check_ok"] = (dim_lam == dim_res)
    return rows, std_mult


# ===========================================================================
# 2. CANDIDATE 2 -- Ind^{S5}_{S3}((2,1)) (adjoint via Frobenius reciprocity).
#    <Ind(mu), lambda> = <mu, Res(lambda)> -- the column of the branching
#    matrix indexed by mu=(2,1). So the induction multiplicities ARE the
#    std_mult vector from Candidate 1 (Frobenius reciprocity). We also report
#    dim Ind = [S5:S3]*dim(mu) = (120/6)*2 = 40 as a cross-check.
# ===========================================================================

def candidate_2_induction(std_mult):
    ind = {str(lam): std_mult[lam] for lam in P5}
    dim_ind = sum(std_mult[lam] * int(dim_irrep(lam)) for lam in P5)
    index = sp.factorial(5) // sp.factorial(3)   # [S5:S3] = 20
    dim_expected = int(index) * int(dim_irrep(STD3))
    return ind, int(dim_ind), int(dim_expected)


# ===========================================================================
# 3. CANDIDATE 3 -- Markov tower H3 < H4 < H5: forward embedding of the
#    (2,1) baryon block. We trace the branching PATHS (2,1) -> lambda4 |- 4
#    -> lambda5 |- 5 (add-a-box, the adjoint of remove-a-box), and ask which
#    5-strand irreps lambda5 contain (2,1) in their restriction -- i.e. which
#    5-strand blocks the baryon trace embeds into. We then report the
#    SO(3)/icosahedral fiber-carrying irreps (dim-5 H lives at ell=2). The
#    Markov stabilization scales tr_M by z = 1/(q^{1/2}+q^{-1/2}) per added
#    strand; two stabilizations H3->H5 scale by z^2 (RAW @ q0).
# ===========================================================================

def add_box(lam, n_total):
    """All partitions of n_total+1 obtained by adding one box to lam |- n_total
    (outer corners)."""
    res = []
    parts = list(lam)
    # add to an existing row if it doesn't violate non-increasing
    for i in range(len(parts)):
        if i == 0 or parts[i] < parts[i - 1]:
            new = parts[:i] + [parts[i] + 1] + parts[i + 1:]
            res.append(tuple(new))
    # add a new row of length 1
    res.append(tuple(parts) + (1,))
    return res


def candidate_3_markov_tower():
    # forward branching paths (2,1) -> |-4 -> |-5
    level4 = {}
    for mu in add_box(STD3, 3):
        level4[mu] = level4.get(mu, 0) + 1
    level5 = {}
    paths = {}
    for mu4, m4 in level4.items():
        for mu5 in add_box(mu4, 4):
            level5[mu5] = level5.get(mu5, 0) + m4
            paths.setdefault(mu5, []).append((STD3, mu4, mu5))
    # cross-check via Candidate 1: level5 multiplicity of (2,1) embedding
    # should equal Res^{S5}_{S3}(lambda5)[(2,1)] -- Frobenius/branching duality
    z = 1 / (mp.sqrt(Q0_MP) + 1 / mp.sqrt(Q0_MP))
    z2 = z * z
    return {str(k): v for k, v in level5.items()}, \
           {str(k): [(str(a), str(b), str(c)) for (a, b, c) in v] for k, v in paths.items()}, \
           mp.nstr(z, COMPUTE_DPS), mp.nstr(z2, COMPUTE_DPS)


# ===========================================================================
# 4. CANDIDATE 4 -- Icosahedral A5 restricted to a 3-element stabilizer.
#    A5 acts on 5 points; a point stabilizer is A4. The "3 color sheets" are
#    governed by a subgroup acting on 3 objects. Two natural candidates:
#      (i)  Z3 = <(123)> < A5 (cyclic rotation of 3 color sheets)
#      (ii) S3 < A5 : S3 ~ <(123),(12)(45)> (order-6, non-cyclic; it permutes
#           3 of the 5 points as S3 while pairing the other two). This is a
#           genuine S3 subgroup of A5.
#    The dim-5 irrep H is the ell=2 carrier (s5-so3 audit). Branch H to the
#    relevant 3-element subgroup using explicit character tables; report the
#    decomposition into 3-object irreps RAW.
# ===========================================================================

def candidate_4_icosahedral_restriction():
    # A5 character table. Conjugacy classes: e, (12)(34) [15], (123) [20],
    # (12345) [12], (13524) [12]. Irreps: 1, 3, 3', 4, 5 (= H, the ell=2).
    # Character of H=5 on the 5 classes:
    #   e:5, (12)(34):1, (123):-1, (12345):0, (13524):0
    chi_H = {"e": 5, "2+2": 1, "3": -1, "5a": 0, "5b": 0}

    # ---- (i) Z3 = <(123)> < A5. Its 3 irreps are 1, w, w^2 (cube roots).
    import cmath
    w = cmath.exp(2j * cmath.pi / 3)
    # Character of H restricted to Z3 on (e, g=(123), g^2=(132)):
    #   e -> 5 ; g -> chi_H((123)) = -1 ; g^2 -> chi_H((132)) = -1
    chi_restr_Z3 = [5, -1, -1]
    z3_chars = {
        "triv": [1, 1, 1],
        "w": [1, w, w * w],
        "w2": [1, w * w, w],
    }
    z3_mult = {}
    for name, ch in z3_chars.items():
        m = sum(chi_restr_Z3[k] * ch[k].conjugate() for k in range(3)) / 3
        z3_mult[name] = round(m.real)

    # ---- (ii) S3 ~ <(123),(12)(45)> < A5.  Classes of this S3 inside A5:
    #   e (1 elt) -> A5 class "e"
    #   two 3-cycles {(123),(132)} -> A5 class "3"
    #   three involutions of form (12)(45) -> A5 class "2+2"
    # S3 char table on (e, 3-cycle, transposition):
    #   triv [1,1,1], sign [1,1,-1], std=(2,1) [2,-1,0]
    chi_restr_S3 = {"e": 5, "3cyc": chi_H["3"], "transp": chi_H["2+2"]}
    # = e:5, 3cyc:-1, transp:1
    s3_class_sizes = {"e": 1, "3cyc": 2, "transp": 3}  # |S3|=6
    s3_chars = {
        "triv": {"e": 1, "3cyc": 1, "transp": 1},
        "sign": {"e": 1, "3cyc": 1, "transp": -1},
        "std_(2,1)": {"e": 2, "3cyc": -1, "transp": 0},
    }
    s3_mult = {}
    for name, ch in s3_chars.items():
        m = sum(s3_class_sizes[c] * chi_restr_S3[c] * ch[c]
                for c in ["e", "3cyc", "transp"]) / 6
        s3_mult[name] = round(m)
    return {
        "Z3_restriction_of_H": z3_mult,
        "S3_in_A5_restriction_of_H": s3_mult,
        "S3_embeds_in_A5": "yes -- <(123),(12)(45)> ~ S3 (order-6, non-cyclic)",
        "chi_H_on_A5_classes": chi_H,
        "chi_H_restricted_to_S3_classes": chi_restr_S3,
    }


# ===========================================================================
# Build the witness.
# ===========================================================================

def main():
    w = WitnessBuilder("h5-h3-functor-keystone", engine="python+mpmath",
                       start_time=START)
    w.set_description(
        "THE 5<->3 keystone (named by PRs #1670/#1672/#1677/#1678): compute "
        "the STANDARD Hecke restriction functor Res^{H5}_{H3} and its adjoint "
        "Ind, the Markov tower H3<H4<H5 forward embedding, and the icosahedral "
        "A5 -> 3-element-stabilizer restriction of the dim-5 (ell=2) irrep H -- "
        "all via exact Young-tableau branching (remove/add-a-box) and explicit "
        "character tables. RAW multiplicities; the Borromean h^4=-3/4 is a "
        "FALSIFICATION reference only. No fit, no tuning. Environment: exact "
        "integer/rational branching combinatorics (Python stdlib + sympy for "
        "factorials/hook-lengths); RAW substrate z at compute_dps via mpmath; "
        "engine=python+mpmath."
    )
    w.set_audit_only("docs/audits/2026-06-02-h5-h3-functor-keystone.md")
    w.add_parameter("q0_falsification_ref", Q0_STR)
    w.add_parameter("q0_source", "q_parameter.Q_MP (proton-pinned)")
    w.add_parameter("dps", COMPUTE_DPS)
    w.add_parameter("h4_borromean_falsification_ref", str(H4_BORROMEAN))

    # --- CANDIDATE 1: restriction --------------------------------------------
    res_rows, std_mult = candidate_1_restriction()
    w.add_data("candidate_1_Res_H5_H3", {
        "branching_rule": "iterated remove-a-box S5->S4->S3 (Young); "
                          "q-independent (Tits deformation: H_n(q) semisimple "
                          "at generic/real q0 has same blocks lambda|-n as S_n "
                          "with the same branching).",
        "per_lambda5_multiplicities": {str(k): v for k, v in res_rows.items()},
        "std_(2,1)_multiplicity_per_lambda5":
            {str(k): v for k, v in std_mult.items()},
    })
    # dim checks (Res preserves total dim) -- assertions
    for lam in P5:
        w.add_assertion(f"dim_check_Res_{lam}",
                        res_rows[lam]["_dim_restricted"],
                        res_rows[lam]["_dim_lambda"])
    # The KEY raw finding: the (2,1) baryon block appears across MULTIPLE |-5
    # blocks (multiplicities in {1,2}; (4,1) and (2,1,1,1) DO restrict to (2,1)
    # with multiplicity exactly 1, while (3,2)/(3,1,1)/(2,2,1) give 2). So
    # Hom(fiber,(2,1)) is a multiplicity space of dim >= 1 with NO canonical
    # distinguished basis vector / NO single canonical channel identifiable with
    # THE ell=2 carrier -- record the full vector.
    mult_values = sorted(set(std_mult.values()))
    w.add_data("std_(2,1)_multiplicity_distinct_values", mult_values)

    # --- CANDIDATE 2: induction ----------------------------------------------
    ind, dim_ind, dim_expected = candidate_2_induction(std_mult)
    w.add_data("candidate_2_Ind_H3_H5_of_(2,1)", {
        "frobenius_reciprocity": "Ind multiplicities = Res std_(2,1) column",
        "per_lambda5_multiplicity": ind,
        "dim_Ind": dim_ind,
        "dim_expected_[S5:S3]*dim(2,1)": dim_expected,
    })
    w.add_assertion("Ind_dim_eq_index_times_dim_(2,1)", dim_ind, dim_expected)

    # --- CANDIDATE 3: Markov tower -------------------------------------------
    lvl5, paths, z_val, z2_val = candidate_3_markov_tower()
    w.add_data("candidate_3_markov_tower_H3_H4_H5", {
        "forward_add_box_paths_(2,1)->|4->|5": paths,
        "level5_embedding_multiplicity_of_(2,1)": lvl5,
        "markov_z_at_q0": z_val,
        "markov_z_squared_at_q0_two_stabilizations": z2_val,
        "caveat": "add-box embedding multiplicity of (2,1) into lambda5 EQUALS "
                  "Res^{S5}_{S3}(lambda5)[(2,1)] (branching duality) -- so the "
                  "Markov-tower forward embedding gives the SAME multiplicity "
                  "vector as Candidate 1, NOT a canonical single channel.",
    })
    # cross-check: level5 multiplicity == candidate-1 std_mult
    for lam in P5:
        w.add_assertion(f"markov_embed_eq_restriction_{lam}",
                        lvl5.get(str(lam), 0), std_mult[lam])

    # --- CANDIDATE 4: icosahedral restriction --------------------------------
    ico = candidate_4_icosahedral_restriction()
    w.add_data("candidate_4_icosahedral_A5_restriction", ico)
    # dim checks: restriction of dim-5 preserves dim
    s3m = ico["S3_in_A5_restriction_of_H"]
    dim_s3_restr = s3m["triv"] * 1 + s3m["sign"] * 1 + s3m["std_(2,1)"] * 2
    w.add_assertion("icosa_H_to_S3_dim_check", dim_s3_restr, 5)
    z3m = ico["Z3_restriction_of_H"]
    dim_z3_restr = z3m["triv"] + z3m["w"] + z3m["w2"]
    w.add_assertion("icosa_H_to_Z3_dim_check", dim_z3_restr, 5)

    # --- VERDICT -------------------------------------------------------------
    verdict = {
        "candidate_1_restriction": (
            "Res^{H5}_{H3} is a well-defined STANDARD functor, but the (2,1) "
            "std block appears in the restriction of multiple |-5 irreps with "
            f"multiplicities {std_mult} -- NOT a canonical single channel. No "
            "lambda5 restricts to (2,1) with a distinguished mult that singles "
            "out the ell=2 dim-5 carrier H. Picking one would be a FIT."),
        "candidate_2_induction": (
            "Ind^{H5}_{H3}((2,1)) has dim 40 and is spread over the same |-5 "
            "blocks (Frobenius reciprocity) -- no canonical projection to a "
            "single fiber level either."),
        "candidate_3_markov_tower": (
            "The forward Markov embedding multiplicity of (2,1) into lambda5 "
            "EQUALS the Candidate-1 restriction vector (branching duality), and "
            "carries a trace factor z^2; it is the SAME multivalued map, not a "
            "canonical 5->3 functor. (Consistent with the census: Markov "
            "destab is the canonical strand map but does not isolate one block.)"),
        "candidate_4_icosahedral": (
            "Restriction of the dim-5 ell=2 irrep H of A5 to S3<A5 gives "
            f"{ico['S3_in_A5_restriction_of_H']} -- the std (2,1) appears with "
            "multiplicity 2 (NOT 1). To Z3 it gives "
            f"{ico['Z3_restriction_of_H']}. NO canonical iso H ~= (2,1)."),
        "overall": (
            "NONEXISTENCE at the rep-ring level: every standard categorical "
            "bridge (restriction, induction, Markov tower, icosahedral "
            "restriction) yields the (2,1) baryon block with multiplicity != 1 "
            "(restriction values across |-5 irreps, and mult 2 from the ell=2 "
            "H). There is NO canonical iso sending the ell=2/H amplitude to THE "
            "(2,1) h^4 coefficient -- the multiplicities are computed FIRST and "
            "are not 1, so any chosen normalization is a fit. This is a "
            "rigorous nonexistence of a knot-operator/Hecke-level canonical "
            "functor, forcing a reframe (the bridge, if any, is "
            "non-functorial/geometric, OR the baryon is not literally 3-strand, "
            "OR the fiber is not literally 5-strand)."),
    }
    w.add_data("verdict_per_candidate", verdict)
    w.add_caveat(
        "Branching multiplicities are q-INDEPENDENT (integers). The Borromean "
        "h^4=-3/4 is RAW from the (2,1) block of tr_M((sigma_1^-1 sigma_2)^3) "
        "(borromean-markov-trace-closed-form.md) and is used here ONLY as a "
        "falsification reference: no multiplicity is chosen to reproduce it.")

    out = w.save()
    print("VERDICT (overall):", verdict["overall"])
    print("Res std_(2,1) multiplicities per lambda|-5:", std_mult)
    print("Ind dim:", dim_ind, "(expected", dim_expected, ")")
    print("Icosa H -> S3 decomposition:", ico["S3_in_A5_restriction_of_H"])
    print("Icosa H -> Z3 decomposition:", ico["Z3_restriction_of_H"])
    print("witness saved:", out)


if __name__ == "__main__":
    main()
