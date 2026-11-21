#!/usr/bin/env python3
"""T3 writhe-sign vs the mixed-sign Delta_lambda pattern (bean qou-buxs).

QUESTION.  The derived weak-isospin grading (PR #4618,
`WeakIsospinT3Grading.lean`) is  T3 = sign(kappa)/2,  kappa = signed writhe of a
quark's canonical T(2,n)=sigma_1^{+-n} braid: up-type = +crossing (T3=+1/2),
down-type = -crossing (T3=-1/2).  The per-QUARK datum is  sign(kappa) in {+1,-1}.

The Delta_lambda mixed-sign target (Option-E deuteron closure, Lean-proved
`QOU.BraidsAndKnots.deltaSign_mixed`, PROBE-4 prune 2026-06-16) is per-PARTITION:
    Delta_lambda = sgn(w0^{S_{lambda'}}) * dim(V_lambda),
    sgn(w0^{S_{lambda'}}) = prod_j sgn(w0^{S_{c_j}}) = prod_j (-1)^{C(c_j,2)},
where c_j = parts of the conjugate lambda' = COLUMN heights of lambda.
Mixed-sign: n=3 -> 1+/2-,  n=6 -> 6+/5- (prune script).

DERIVE-THEN-CHECK (no fit).  We do NOT choose an aggregation map to match the
target sign vector.  We DERIVE the aggregation from two independent, standard
structures and then compare:

  * Wedderburn/Frobenius:   a Wedderburn block lambda carries the standard Young
    symmetrizer -- ROWS symmetrize (bosonic, +crossing), COLUMNS antisymmetrize
    (fermionic, -crossing).  The chirality sign lives in the columns.
  * Chiral-EFT isospin template (Hammer-Koenig-van Kolck 1906.12122 p.12; the
    tau_1.tau_2 operator): the Pauli principle ties the isospin sign to the
    EXCHANGE SYMMETRY of the isospin wavefunction -- symmetric (triplet,
    tau1.tau2=+1) vs antisymmetric (singlet, tau1.tau2=-3).  The sign flip is
    the symmetric-vs-antisymmetric (= row-vs-column) Young sign.  This is the
    QCD-side template for how a per-pair isospin sign aggregates in a bound
    state.

Two READINGS of "aggregate the T3 crossing sign over the column antisymmetrizer"
-- these differ, and the difference IS the scientific content:

  MAP_A  (crossing-COUNT parity = sign character = Slater-determinant sign =
          chiral-EFT pairwise, product over ALL C(c,2) antisymmetric pairs):
              prod_j (-1)^{C(c_j,2)}
          = (-1)^{n(lambda)},  n(lambda)=sum_i (i-1) lambda_i.
          This equals the TARGET by the elementary identity
          l(w0^{S_m}) = C(m,2); it is the target's own definition re-read as a
          fermion parity, NOT independent information.

  MAP_B  (T3-LITERAL = sign of NET writhe of each column antisymmetrizer, i.e.
          the actual per-quark T3 statistic sign(kappa) applied per column):
          a column of height c is a NEGATIVE half-twist, net writhe -C(c,2),
          so sign(net) = -1 for every c>=2 and +1 for c=1:
              prod_{j} s(c_j),  s(1)=+1, s(c>=2)=-1
          = (-1)^{#columns of height >= 2}.
          This is what the *literal* T3 grading (sign-of-net-writhe) gives.

sign(net writhe) and (-1)^{crossing count} COINCIDE iff C(c,2) is odd
(c = 2,3 mod 4) and both +1 at c=1; they DIVERGE at c=4,5 (mod 4 in {0,1}).
So MAP_B = MAP_A exactly when every column height is <= 3 (all of n=3), and
they first diverge at a height-4/5 column (first appears at n=6).

Output: per-partition sign vectors for n=3 and n=6, TARGET vs MAP_A vs MAP_B,
plus per-partition agreement, written to a witness JSON.
"""
from __future__ import annotations
import hashlib
import json
import subprocess
import sys
from math import comb, factorial
from pathlib import Path


def partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for k in range(min(n, mx), 0, -1):
        for rest in partitions(n - k, k):
            yield (k,) + rest


def transpose(lam):
    if not lam:
        return ()
    return tuple(sum(1 for r in lam if r > c) for c in range(lam[0]))


def hook_dim(lam):
    n = sum(lam)
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            arm = row - j - 1
            leg = sum(1 for k in range(i + 1, len(lam)) if lam[k] > j)
            prod *= (arm + leg + 1)
    return factorial(n) // prod


def n_statistic(lam):
    """n(lambda) = sum_i (i-1) lambda_i (0-indexed rows)."""
    return sum(i * r for i, r in enumerate(lam))


def sgn_w0_m(m):
    """sign of the longest element of S_m = (-1)^{C(m,2)}."""
    return (-1) ** comb(m, 2)


def target_sign(lam):
    """sgn(w0^{S_{lambda'}}) = prod over column heights (-1)^{C(c,2)}."""
    s = 1
    for c in transpose(lam):
        s *= sgn_w0_m(c)
    return s


def map_A_sign(lam):
    """Crossing-COUNT parity / sign character = (-1)^{n(lambda)}.
    Independent route (via n(lambda)); cross-checked == target below."""
    return (-1) ** n_statistic(lam)


def map_B_sign(lam):
    """T3-LITERAL: sign of NET writhe of each column antisymmetrizer.
    Column height c => negative half-twist, net writhe -C(c,2):
    sign = -1 for c>=2, +1 for c=1.  Product over columns."""
    s = 1
    for c in transpose(lam):
        if c >= 2:
            s *= -1
    return s


def analyze(n):
    rows = []
    for lam in partitions(n):
        colh = transpose(lam)
        d = hook_dim(lam)
        tgt = target_sign(lam)
        a = map_A_sign(lam)
        b = map_B_sign(lam)
        rows.append({
            "lambda": list(lam),
            "conjugate_col_heights": list(colh),
            "dim": d,
            "n_of_lambda": n_statistic(lam),
            "target_sign": tgt,
            "target_delta": tgt * d,
            "mapA_sign_character": a,
            "mapB_T3_net_writhe_sign": b,
            "A_matches_target": a == tgt,
            "B_matches_target": b == tgt,
        })
    return rows


def summarize(rows):
    tpos = sum(1 for r in rows if r["target_sign"] > 0)
    tneg = sum(1 for r in rows if r["target_sign"] < 0)
    amatch = sum(1 for r in rows if r["A_matches_target"])
    bmatch = sum(1 for r in rows if r["B_matches_target"])
    return {
        "num_partitions": len(rows),
        "target_pos": tpos, "target_neg": tneg,
        "mapA_matches": amatch, "mapB_matches": bmatch,
    }


def git_head_sha():
    try:
        return subprocess.run(["git", "log", "-1", "--format=%H", "--", __file__],
                              capture_output=True, text=True).stdout.strip() or None
    except Exception:
        return None


def main():
    out = {"n3": analyze(3), "n6": analyze(6)}
    s3, s6 = summarize(out["n3"]), summarize(out["n6"])

    print("=" * 78)
    print("TARGET  Delta_lambda = sgn(w0^{S_lambda'}) * dim   vs   T3 aggregations")
    print("=" * 78)
    for n, rows, summ in ((3, out["n3"], s3), (6, out["n6"], s6)):
        print(f"\n--- n = {n}  ({summ['num_partitions']} partitions;"
              f" target {summ['target_pos']}+/{summ['target_neg']}-) ---")
        print(f"{'lambda':<16}{'cols':<14}{'dim':>4}{'TGT':>5}"
              f"{'A(char)':>9}{'B(T3net)':>10}{'A=T':>5}{'B=T':>5}")
        for r in rows:
            lam = "(" + ",".join(map(str, r["lambda"])) + ")"
            cols = "(" + ",".join(map(str, r["conjugate_col_heights"])) + ")"
            print(f"{lam:<16}{cols:<14}{r['dim']:>4}{r['target_sign']:>+5}"
                  f"{r['mapA_sign_character']:>+9}{r['mapB_T3_net_writhe_sign']:>+10}"
                  f"{str(r['A_matches_target']):>5}{str(r['B_matches_target']):>5}")
        print(f"  MAP_A (sign character / crossing-count parity) matches target: "
              f"{summ['mapA_matches']}/{summ['num_partitions']}")
        print(f"  MAP_B (T3 literal sign-of-net-writhe) matches target:          "
              f"{summ['mapB_matches']}/{summ['num_partitions']}")

    # Cross-check: MAP_A must equal target for EVERY partition (elementary
    # identity n(lambda) = sum_j C(col_j,2)); if not, the code is wrong.
    assert all(r["A_matches_target"] for r in out["n3"] + out["n6"]), \
        "MAP_A != target: n(lambda)=sum C(col,2) identity violated -- bug"
    # Mixed-sign target sanity (matches prune script)
    assert (s3["target_pos"], s3["target_neg"]) == (1, 2), "n=3 target drift"
    assert s6["target_pos"] > 0 and s6["target_neg"] > 0, "n=6 not mixed"

    print("\n" + "=" * 78)
    print("VERDICT (per-partition, no fit)")
    print("=" * 78)
    print(f"  n=3: MAP_B (literal T3) matches {s3['mapB_matches']}/3 "
          f"(all columns height <=3 => coincidental).")
    print(f"  n=6: MAP_B (literal T3) matches {s6['mapB_matches']}/11 "
          f"-- diverges at height-4/5 columns.")
    mismatch6 = [r["lambda"] for r in out["n6"] if not r["B_matches_target"]]
    print(f"       n=6 MAP_B mismatches (lambda): {mismatch6}")
    print("  MAP_A (sign character = crossing-COUNT parity) matches ALL by")
    print("  construction: it IS sgn(w0^{S_lambda'}) re-read as column-anti-")
    print("  symmetrizer fermion parity (= target definition, not new info).")
    print("  => The *literal* T3 sign-of-net-writhe is the WRONG sign statistic")
    print("     for Delta_lambda; the correct one is the crossing-count parity")
    print("     (sign character), which T3 interprets but does not derive.")

    witness = {
        "witness_schema": "witness/v1",
        "name": "t3-writhe-vs-delta-lambda-sign",
        "bean": "qou-buxs",
        "description": ("Per-partition comparison of the derived weak-isospin "
                        "T3 writhe-sign grading (PR #4618) against the mixed-sign "
                        "Delta_lambda target sgn(w0^{S_lambda'})*dim for n=3 and "
                        "n=6. Derive-then-check: aggregation maps derived from the "
                        "Young/Wedderburn column-antisymmetrizer + chiral-EFT "
                        "tau1.tau2 Pauli template, not fitted to the sign vector."),
        "engine": "python-combinatorics (pure, no external deps)",
        "target": "Delta_lambda = sgn(w0^{S_lambda'}) * dim(V_lambda)",
        "n3": out["n3"],
        "n6": out["n6"],
        "summary": {"n3": s3, "n6": s6},
        "verdict": "partial",
        "verdict_detail": {
            "mapA_sign_character": "matches target for ALL partitions (= target definition, crossing-count parity; not independent info)",
            "mapB_T3_literal_net_writhe_sign": {
                "n3": f"{s3['mapB_matches']}/3 (coincidental: all column heights <= 3)",
                "n6": f"{s6['mapB_matches']}/11 (diverges at height-4/5 columns)",
                "n6_mismatches": mismatch6,
            },
            "conclusion": ("The literal per-quark T3 = sign(net writhe) is a "
                           "COARSER statistic than the crossing-count parity "
                           "Delta_lambda needs. They agree only for column "
                           "heights <= 3 (all of n=3, most of n=6) and diverge "
                           "at height >= 4. T3 supplies the physical crossing "
                           "reading of the antisymmetric channel (down-type = "
                           "negative crossing), consistent with the chiral-EFT "
                           "tau1.tau2 Pauli/exchange-symmetry template, but does "
                           "NOT independently reproduce the Delta_lambda sign "
                           "vector: that is the column-antisymmetrizer sign "
                           "character, the target's own definition."),
        },
        "chiral_eft_template": ("Hammer-Koenig-van Kolck arXiv:1906.12122 p.12: "
                                "Pauli principle => isospin sign = exchange "
                                "symmetry of isospin wavefunction (triplet "
                                "tau1.tau2=+1 symmetric / singlet tau1.tau2=-3 "
                                "antisymmetric) = Young row(+)/column(-) sign."),
        "anti_fit_statement": ("No aggregation map was chosen to match the sign "
                               "vector. MAP_A and MAP_B are the two standard "
                               "readings of 'crossing sign aggregated over the "
                               "column antisymmetrizer'; MAP_A is the target "
                               "restated, MAP_B is the literal T3 statistic. "
                               "MAP_B's partial match/failure is the honest "
                               "derived result, not a tuned success."),
        "scriptHash": None,
        "scriptCommitSha": git_head_sha(),
    }
    src = Path(__file__).read_bytes()
    witness["scriptHash"] = hashlib.sha256(src).hexdigest()[:12]

    wpath = Path(__file__).with_name("t3-writhe-vs-delta-lambda-sign.witness.json")
    # Provenance stamp (bean qou-4un2): this producer writes its
    # witness directly, so nothing else records which script made
    # it -- and a re-run of an unstamped producer DELETES the
    # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
    import os as _os  # noqa: E402 -- provenance stamp
    from qou_substrate.witness import WitnessBuilder as _WB
    witness.setdefault("scriptFile", _os.path.basename(__file__))
    _WB.stamp_staleness_metadata(
        witness, script_path=__file__, engine=None, q0_anchor=False)
    wpath.write_text(json.dumps(witness, indent=2) + "\n")
    print(f"\nwitness -> {wpath}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
