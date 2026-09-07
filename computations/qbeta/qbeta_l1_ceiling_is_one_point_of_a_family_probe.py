#!/usr/bin/env python3
"""The ell-1 binding ceiling bounds ONE evaluation point, not the family.

*** 🛑 READ THE ANTI-FIT BANNER BEFORE THE NUMBERS ***

This probe does NOT close the binding gap and does not claim to. It measures the
SCOPE of an exclusion argument. No `w` below is selected for being close to the
target; the sampling is systematic and the reported figure is a RANGE over the
whole sample, not a winner. Selecting a `w` by proximity and calling it a
derivation would be exactly the defect recorded against the electroweak residual
in `qou-4qno`, one directory over.

*** THE ARGUMENT BEING SCOPED ***

`computations/deltalambda/l1_ceiling_d_frame_remeasure.py` computes, per atom,

    ceiling = ( sum_lambda |y_lambda . chi^lambda(beta_atom) . Delta_lambda| )
              / |B_AME / m_e|

and finds it < 1 everywhere in the D frame -- deuteron 0.5661, tritium 0.3604,
3He 0.6925, 4He 0.4335. Since the numerator takes the ABSOLUTE VALUE of every
term, it is the most generous reweighting of the partition sum available: no
choice of coefficients on {Delta_lambda} reaches the binding target.

`qou-fvzm` combines that with N = 2 being locked and concludes, in its closing
line, **"THE MISSING ADDITIVE TERM IS NOT A HECKE-TRACE OBJECT AT ALL."**

*** WHAT THE CEILING ACTUALLY FIXES, AND WHAT IT LEAVES FREE ***

`chi^lambda(beta_atom)` is evaluated at ONE element. The ceiling ranges over
COEFFICIENTS at that fixed point. It never varies the point.

But `tr_M(x . w) = sum_lambda y_lambda chi^lambda(x . w)` is a Markov trace for
every `w`, so every member of that family is a Hecke-trace object, lives inside
the N = 2 carrier, and is NOT row-capped. The corpus reads `w = 1`. The ceiling
bounds `w = 1`. Nothing has bounded the rest.

The owner's steer names the same freedom from the other side: an operator's
order-0 shadow is not one number. `E_2(Delta_bind)` -- the Markov-orthogonal
projection onto `H_2` -- already carries TWO coordinates, `tr_M(Delta)` and
`tr_M(Delta . sigma_1)`, where the corpus reads only the first.

*** THE SHARP VERSION: THE CEILING BOUNDS EXACTLY THE CENTRE ***

Part 5 below settles what kind of freedom this is. For CENTRAL `z`, Schur gives
`rho_lambda(z) = c_lambda . I`, so

    chi^lambda(beta . z)  =  c_lambda . chi^lambda(beta)

which IS a reweighting `y_lambda -> c_lambda y_lambda` -- the move the ceiling
already bounds. Verified on the transposition class-sum to 3.6e-49.

So the claim is not "the ceiling misses multiplication by anything". It is:

    THE ELL-1 CEILING BOUNDS PRECISELY THE CENTRE OF H_n.
    THE FREEDOM IT NEVER TOUCHED IS EXACTLY THE NON-CENTRAL PART.

Which also says what a candidate additive term must NOT be. The full twist is
central, so it is already excluded and cannot be the answer.

*** WHAT IS MEASURED HERE ***

For the deuteron (n = 6, 11 partitions):

  1. VALIDATION. `rho_lambda(beta_atom)` built from Hoefsmit seminormal matrices
     reproduces every committed `chi_lambda` in
     `chi-deuteron-h6-at-q0-50dps.witness.json`, and the ceiling at `w = 1`
     reproduces the committed D-frame 0.5661. Without this the rest is noise.

  2. THE FAMILY IS NOT DEGENERATE. `chi^lambda(beta . sigma_g)` varies with `g`,
     so the extra coordinates are not copies of `tr_M(beta)`.

  3. THE FAMILY SPANS EVERYTHING. Collect `v(w) = (chi^lambda(beta.w))_lambda`
     in R^11 over a systematic word sample and take the rank. Wedderburn makes
     the expectation exact rather than empirical: `rho_lambda` is onto
     `Mat_{d_lambda}`, so `w -> tr(rho_lambda(beta) rho_lambda(w))` is a nonzero
     functional whenever `rho_lambda(beta) != 0`, and the blocks are
     independent. Rank 11 means the corpus reads one point of a space that fills
     R^11.

  4. THE CEILING AT `w = 1` DOES NOT BOUND THE FAMILY. Report the range of
     `ceiling(w)` over the sample.

*** WHAT THIS DOES AND DOES NOT LICENSE ***

DOES: `qou-fvzm`'s closing line is stronger than its evidence. The ell-1 ceiling
excludes reweightings at one point; it does not exclude Hecke-trace objects in
general, because `tr_M(. w)` for `w != 1` is one and was never bounded.

DOES NOT: produce the missing additive term, or identify which `w` (if any) is
physically meaningful. `beta_atom . w` is a different element of the algebra --
it is not the deuteron -- so a large `ceiling(w)` is a statement about the
algebra, not about binding. The physical question is which functionals of
`Delta_bind` are observables, and that is not settled by having many of them.
"""
from __future__ import annotations

import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)

import json
import os
import subprocess
import sys
import time
from math import factorial  # float64-ok: exact integer factorial for the hook-length dimension; same import as l1_ceiling_d_frame_remeasure.py
from pathlib import Path

import mpmath as mp
import pyhecke_native as ph

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "computations"))

DPS = 50
mp.mp.dps = DPS
Q0S = "1.1099785827513808075916690956107688798744991218736"
Q0 = mp.mpf(Q0S)
M_E_MEV = mp.mpf("0.51099895069")
B_AME_DEUTERON = mp.mpf("2.224566")
N_STRANDS = 6
COMMITTED_CEILING_D = mp.mpf("0.5661")     # l1_ceiling_d_frame_remeasure.py


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def dim_irrep(lam):
    n = sum(lam)
    conj = [sum(1 for i in range(len(lam)) if lam[i] > j) for j in range(lam[0])]
    prod = 1
    for i in range(len(lam)):
        for j in range(lam[i]):
            prod *= (lam[i] - j) + (conj[j] - i) - 1
    return factorial(n) // prod


def delta_lambda(lam):
    return (-1) ** sum(i * p for i, p in enumerate(lam)) * dim_irrep(lam)


def main() -> int:
    t0 = time.monotonic()
    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    ok = True
    from mass_at_3A_proper import atom_braid_word_3A
    letters = atom_braid_word_3A(1, 1, include_inter=True, q=Q0)
    wit = json.loads((ROOT / "computations" /
                      "chi-deuteron-h6-at-q0-50dps.witness.json").read_text())
    target = abs(B_AME_DEUTERON / M_E_MEV)

    # --- seminormal generators, once per partition -----------------------
    gens_by_lam, rho_beta = {}, {}
    for r in wit["by_partition"]:
        lam = tuple(r["partition"])
        mats = ph.seminormal_matrices_mpfr(list(lam), Q0S, DPS)
        gens = []
        for m in mats:
            d = len(m)
            M = mp.zeros(d, d)
            for i, row in enumerate(m):
                for (j, s) in row:
                    M[i, j] = mp.mpf(s)
            gens.append(M)
        gens_by_lam[lam] = gens
        d = gens[0].rows
        acc = mp.eye(d)
        for (c, dd, g) in letters:
            acc = acc * (mp.mpf(c) * gens[int(g)] + mp.mpf(dd) * mp.eye(d))
        rho_beta[lam] = acc

    lams = [tuple(r["partition"]) for r in wit["by_partition"]]
    y = {tuple(r["partition"]): mp.mpf(r["y_lambda"]) for r in wit["by_partition"]}

    def chi_of(lam, word):
        """chi^lambda(beta_atom . w) for a signed word w."""
        R = rho_beta[lam]
        gs = gens_by_lam[lam]
        d = R.rows
        h = Q0 - 1 / Q0
        for (sgn, g) in word:
            G = gs[g] if sgn > 0 else (gs[g] - h * mp.eye(d))
            R = R * G
        return sum(R[i, i] for i in range(d))

    def ceiling_of(word):
        return sum(abs(y[l] * chi_of(l, word) * delta_lambda(l)) for l in lams) / target

    print("=" * 72)
    print("1. VALIDATION — does this machinery reproduce the corpus?")
    print("=" * 72)
    worst = mp.mpf(0)
    for r in wit["by_partition"]:
        lam = tuple(r["partition"])
        worst = max(worst, abs(chi_of(lam, []) - mp.mpf(r["chi_lambda"])))
    print(f"  worst |chi_mine - chi_committed| over 11 partitions: {mp.nstr(worst, 4)}")
    ok &= chk("reproduces_every_committed_chi", worst < mp.mpf("1e-45"), True)

    c1 = ceiling_of([])
    print(f"  ceiling at w = 1 : {mp.nstr(c1, 10)}   (committed D-frame 0.5661)")
    ok &= chk("reproduces_committed_ceiling_at_w_eq_1",
              abs(c1 - COMMITTED_CEILING_D) < mp.mpf("5e-5"), True)

    print("\n" + "=" * 72)
    print("2. IS THE FAMILY DEGENERATE? tr_M(beta . sigma_g) against g")
    print("=" * 72)
    trs = {}
    tr_beta = sum(y[l] * chi_of(l, []) for l in lams)
    print(f"  tr_M(beta)            = {mp.nstr(tr_beta, 20)}   <- what the corpus reads")
    for g in range(N_STRANDS - 1):
        t = sum(y[l] * chi_of(l, [(1, g)]) for l in lams)
        trs[f"sigma_{g}"] = mp.nstr(t, 20)
        print(f"  tr_M(beta . sigma_{g})  = {mp.nstr(t, 20)}")
    distinct = len({trs[k][:24] for k in trs})
    ok &= chk("second_coordinate_varies_with_the_generator", distinct > 1, True,
              "the extra coordinates are not copies of tr_M(beta)")

    print("\n" + "=" * 72)
    print("3. WHAT DOES THE FAMILY SPAN? rank of {v(w)} in R^11")
    print("=" * 72)
    # Systematic sample: identity, both crossings of every generator, and every
    # ordered pair of generators. Nothing here is chosen by its value.
    words = [[]]
    for g in range(N_STRANDS - 1):
        words.append([(1, g)])
        words.append([(-1, g)])
    for g in range(N_STRANDS - 1):
        for k in range(N_STRANDS - 1):
            words.append([(1, g), (1, k)])
    rows = []
    for w in words:
        rows.append([chi_of(l, w) for l in lams])
    # rank by Gram-Schmidt at working precision
    basis = []
    for v in rows:
        u = list(v)
        for b in basis:
            d = sum(u[i] * b[i] for i in range(len(u)))
            u = [u[i] - d * b[i] for i in range(len(u))]
        nrm = mp.sqrt(sum(x * x for x in u))
        if nrm > mp.mpf("1e-30"):
            basis.append([x / nrm for x in u])
    rank = len(basis)
    print(f"  sampled words: {len(words)}   partitions: {len(lams)}   rank: {rank}")
    ok &= chk("family_spans_the_whole_partition_space", rank, len(lams),
              "the corpus reads ONE point of a space that fills R^11")

    print("\n" + "=" * 72)
    print("4. DOES THE w = 1 CEILING BOUND THE FAMILY?")
    print("=" * 72)
    ceils = []
    for w in words:
        ceils.append((ceiling_of(w), w))
    cmin = min(c for c, _ in ceils)
    cmax = max(c for c, _ in ceils)
    n_above = sum(1 for c, _ in ceils if c > c1)
    n_above_one = sum(1 for c, _ in ceils if c > 1)
    print(f"  ceiling(w=1)             : {mp.nstr(c1, 10)}")
    print(f"  range over {len(words)} sampled w : [{mp.nstr(cmin, 8)}, {mp.nstr(cmax, 8)}]")
    print(f"  sampled w with ceiling > ceiling(1) : {n_above} / {len(words)}")
    print(f"  sampled w with ceiling > 1          : {n_above_one} / {len(words)}")
    ok &= chk("w_eq_1_ceiling_does_not_bound_the_family", n_above > 0, True,
              "so the exclusion at w = 1 says nothing about w != 1")

    print("\n  🛑 No w above is selected. The figure is a RANGE over a systematic")
    print("     sample. beta_atom . w is a different element of the algebra — it is")
    print("     not the deuteron — so a large ceiling(w) is a fact about the")
    print("     algebra, not a binding result.")

    print("\n" + "=" * 72)
    print("5. THE CENTER IS EXACTLY THE PART THE CEILING ALREADY EXCLUDES")
    print("=" * 72)
    # For CENTRAL z, rho_lambda(z) = c_lambda . I by Schur, so
    #     chi^lambda(beta . z) = c_lambda . chi^lambda(beta)
    # which is precisely a REWEIGHTING y_lambda -> c_lambda y_lambda -- the move
    # the ell-1 ceiling already bounds. So the freedom the ceiling misses is not
    # "multiply by anything"; it is exactly the NON-CENTRAL part.
    central_ok, central_rows = True, []
    for lam in lams:
        d = rho_beta[lam].rows
        raw = ph.transposition_class_sum_mpfr(list(lam), 0, N_STRANDS - 1, Q0S, DPS)
        Z = mp.zeros(d, d)
        for i, row in enumerate(raw):
            for j, sv in enumerate(row if isinstance(row, list) else []):
                Z[i, j] = mp.mpf(sv)
        # Schur: a central element is a scalar on each block.
        off = max((abs(Z[i, j]) for i in range(d) for j in range(d) if i != j),
                  default=mp.mpf(0))
        c_lam = Z[0, 0]
        chi_bz = sum((rho_beta[lam] * Z)[i, i] for i in range(d))
        pred = c_lam * chi_of(lam, [])
        err = abs(chi_bz - pred)
        central_rows.append({"partition": list(lam), "c_lambda": mp.nstr(c_lam, 12),
                             "max_offdiag": mp.nstr(off, 4),
                             "reweighting_residual": mp.nstr(err, 4)})
        if err > mp.mpf("1e-40"):
            central_ok = False
    print(f"  central class-sum acts as a scalar on every block; "
          f"chi(beta.z) = c_lambda.chi(beta) to "
          f"{max(mp.mpf(r['reweighting_residual']) for r in central_rows)}")
    ok &= chk("central_w_is_exactly_a_reweighting", central_ok, True,
              "so the ceiling DOES bound the centre; the freedom it misses is "
              "precisely the non-central part")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-l1-ceiling-is-one-point-of-a-family",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"q0": Q0S, "dps": DPS, "atom": "deuteron", "n_strands": N_STRANDS,
                       "B_AME_MeV": str(B_AME_DEUTERON),
                       "target_m_e": mp.nstr(target, 20),
                       "trace_convention": "D (SU(2)/Temperley-Lieb)"},
        "data": {
            "validation": {
                "worst_chi_error_vs_committed": mp.nstr(worst, 6),
                "ceiling_at_w_eq_1": mp.nstr(c1, 20),
                "committed_ceiling_D": str(COMMITTED_CEILING_D)},
            "tr_M_beta": mp.nstr(tr_beta, 25),
            "tr_M_beta_sigma_g": trs,
            "span": {"sampled_words": len(words), "partitions": len(lams),
                     "rank": rank},
            "central_is_reweighting": central_rows,
            "ceiling_over_family": {
                "at_w_eq_1": mp.nstr(c1, 20),
                "min": mp.nstr(cmin, 20), "max": mp.nstr(cmax, 20),
                "n_sampled": len(words),
                "n_above_w_eq_1": n_above, "n_above_one": n_above_one},
        },
        "context": {
            "axis": "does the ell-1 binding ceiling bound the family tr_M(. w), "
                    "or only the single point w = 1 that the corpus reads?",
            "answer": "Only w = 1. The ceiling ranges over COEFFICIENTS at a fixed "
                      "evaluation point and never varies the point. Every tr_M(x.w) "
                      "is a Markov trace, hence a Hecke-trace object inside the "
                      "N = 2 carrier and not row-capped, and the family's "
                      "chi-vectors span the full partition space.",
            "consequence": "qou-fvzm's closing line, 'THE MISSING ADDITIVE TERM IS "
                           "NOT A HECKE-TRACE OBJECT AT ALL', is stronger than its "
                           "evidence: the ell-1 ceiling excludes reweightings at one "
                           "point, not Hecke-trace objects in general.",
            "anti_fit": "NO w IS SELECTED. The sample is systematic (identity, both "
                        "crossings of every generator, every ordered pair) and the "
                        "reported figure is a range. beta_atom . w is a different "
                        "element of the algebra -- it is not the deuteron -- so a "
                        "large ceiling(w) is a fact about the algebra, not about "
                        "binding. This probe does not close the gap and does not "
                        "identify which functionals are observables.",
            "scope": "Scope-(a). No content block is edited here.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-l1-ceiling-is-one-point-of-a-family.witness.json"
    # Imported BEFORE `open(..., "w")`, and it must stay there (bean `qou-sidu`):
    # opening for write TRUNCATES immediately, so an import that raises inside the
    # `with` block closes the file EMPTY and destroys the witness. `qou_substrate`
    # is not importable from a bare producer context, which is how 22 witnesses were
    # emptied by a single `producer_importability_audit` run.
    from qou_substrate.witness import WitnessBuilder as _WB
    # Atomic write (bean `qou-sidu`): serialize to a sibling temp file and
    # `os.replace` it into position. `open(..., "w")` TRUNCATES before the
    # dump runs, so any exception in between leaves the committed witness
    # empty or partial -- the shape that emptied 22 witnesses to zero bytes
    # in one `producer_importability_audit` run. `os.replace` is atomic on
    # POSIX within a filesystem, hence a SIBLING temp file.
    _wpath_sidu = out_p
    _wtmp_sidu = str(_wpath_sidu) + ".tmp"
    with open(_wtmp_sidu, "w") as f:
        witness.setdefault("scriptFile", os.path.basename(__file__))
        _WB.stamp_staleness_metadata(
            witness, script_path=__file__, engine="mpmath",
            q0_anchor="proton",
            q0_anchor_reason="experimental pin (Physical-Observations layer): q0 read at the proton m_p/m_e pin", q0_value=Q0S)
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
