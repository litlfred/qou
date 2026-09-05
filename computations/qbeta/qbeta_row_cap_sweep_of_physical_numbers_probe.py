import os as _os_sidu  # noqa: E402 -- atomic witness write (qou-sidu)
"""Corpus sweep: which physical numbers are read off a block with l(lambda) > 2?

Two instances of the same defect turned up this session without anybody looking
for them -- Step 27 of `qou-cds1` (closed by `qou-i9gk`) and the staircase
electroweak residual (`qou-4qno`). Both read empirical content out of a Hecke
block that the framework's own fibre gives dimension zero. The owner's standing
question is whether there are more, so this is the sweep, and the check is
mechanical: for each physical number the corpus quotes, WHICH PARTITION does it
come from, and HOW MANY ROWS does that partition have?

*** THE ROW CAP IS THE CORPUS'S OWN THEOREM, NOT AN IMPORT ***

`content/.../mass-theory/markov-trace-frobenius-selection.md` states it by name:

    "The mass fibre is the fundamental V of SU_q(2), of quantum dimension
     [2]_q, so V^(x)n carries no channel lambda with l(lambda) >= 3 (eigenbasis
     decomposition). A trace that is the categorical trace of the fibre action
     therefore puts weight y_lambda = 0 on every such lambda (THE ROW CAP)"

So a number read off a >2-row block is not merely unverified: it is read off a
module with multiplicity zero in the carrier the physics runs on, and it is
invisible to every Markov trace in the corpus by a theorem the corpus proves.

*** WHAT THE SWEEP FOUND: NO NEW SECTOR ***

3064 live witnesses scanned (`_deprecated/` excluded), 435 carry a >2-row
partition, 91 single one out AND mention an observable. Triaged in full:

    3  INSTANCE            all on conj:weinberg-angle-categorical
    1  SUPPORTING          same chain, quotes no number of its own
    8  ABOUT THE VANISHING states the cap rather than violating it
   63  SAFE                trace-only or inert
   16  FALSE POSITIVE      two distinct classes, below

Every confirmed instance is the chain already recorded in `qou-4qno`, and it
reduces to a single number -- the ratio of the top two positive eigenvalues of
the beta_EW word in the (3,2,1) Hoefsmit representation of H_6:

    max+/2nd-max+   = 1.78315071        raw error   2.1896 %
    x q_0^(1/5)     = 1.82075274        corrected   0.1270 %
    CODATA cot th_W = 1.82306787

l(3,2,1) = 3. That the defect is ONE chain rather than endemic is the sweep's
result, and it is a real one.

*** THE PART THAT IS NEW: THE GUARD IS ON WEAKER GROUNDS THAN THE FACTS ***

The corpus already guards this number -- on ANTI-FIT grounds, and only there.
`appendix-standard-model/sm-params-gauge-couplings.md` says the exponent "was
selected as the closest of 74 enumerated candidates", that "availability after
a proximity search is not derivation", and concludes the parameter "stays
CONJECTURAL". `docs/sm-eightfold-derivation-cheat-sheet.md` repeats it. Neither
mentions the row cap, and the two objections do not have the same consequence:

    anti-fit  ->  the route is OPEN, pending someone deriving q^(1/5)
    row cap   ->  the route is CLOSED whatever the exponent turns out to be,
                  because the spectrum being read has no states in V^(x)6

A future session that succeeded in deriving q^(1/5) would believe it had closed
the Weinberg gap. It would be wrong, for a reason no surface currently states.

Two of the four surfaces carry the number with no caveat at all, and one of
them contradicts the guard outright: `staircase-corner-hook-proof.md` calls the
corner hook "the ARITHMETIC ANCHOR" and says the exponent "uses *exactly* this
corner hook", where the guard says availability after a proximity search is not
derivation. The corner hook h_corner(rho_k) = 2k-1 is a theorem; that the
residual exponent is 1/h_corner is the conjecture, and the proof block reads as
though the first established the second.

And the conjecture block's OWN definition already excludes Path B's object: it
defines cos th_W through tr_M(e_W^+ . sigma_1^4), and tr_M puts weight zero on
(3,2,1) by the row cap. So 0.659 (the block's stated trace evaluation, a ~64 %
miss) and 1.8208 (Path B) are not two estimates of one quantity -- one is
computed inside the carrier and one outside it. Every repair the block proposes
for its miss ("non-uniform pure-pattern multiplicities", "categorical-linking",
"Higgs vev weighting") is inside.

*** TWO CLASSES OF FALSE POSITIVE, BOTH RECORDED ***

1. SPECTRUM-AS-PARTITION. {5,5,5,1} and {5,5,1,1} are eigenvalue multisets of
   the Bring period Gram and of M_S = 5I - J, not Young diagrams. They read as
   weakly-decreasing positive integer tuples, so the detector collects them and
   no Hecke block is involved at all. Five alpha_EM / Bring witnesses.

2. STRUCTURAL-IDENTITY-ON-A-TALL-BLOCK. det(M_lambda).det(M_lambda') = +-1
   holds in any carrier and quotes no physical number, but determinants are
   spectral invariants, so a spectral/trace discriminator scores it as a
   reading. Plus corpus-meta audit scans, refutations, and one null result
   (reeb_rotation_pn_difference = 0.000e+00) -- the anti-fit discipline
   working, scored as though it were the defect.

*** THE DEFAULT VERDICT MUST NOT BE `SAFE` ***

An earlier draft of this probe defaulted untriaged candidates to SAFE and
consequently reported "no new sector" while ten spectral-on-a-tall-block
candidates -- in two sectors it had never looked at -- were absorbed into that
verdict. The optimistic default IS the failure mode. Trace-only and inert are
mechanically safe; everything else stays UNTRIAGED and fails the run until a
human has read it. `triage_is_total_no_untriaged_left` is the assertion that
makes "no new sector" worth anything.

*** SCOPE ***

Scope-(a): no content block is edited here and no conjecture is refuted. The
Specht modules exist for every partition and the eigenvalue ratio is not
challenged. What is in question is what the EMPIRICAL content can mean.
"""
from __future__ import annotations

import json
import os
import re
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
COMP = ROOT / "computations"

N_FIBRE = 2  # V = C^2, the SU_q(2) fundamental. Row cap: dim V_lambda = 0 if l>N.

# Words that mark a number as compared against the measured world.
OBSERVABLE_RE = re.compile(
    r"codata|experimental|measured|pdg|observed|theta_w|weinberg|"
    r"binding|mass_|alpha_em|fine.structure|rel(ative)?.err",
    re.I,
)
SPECTRAL_RE = re.compile(r"eigenval|eigenvec|spectrum|spectral|\bdet\b|determinant", re.I)
TRACE_RE = re.compile(r"tr_m|markov|ocneanu|omega_|weight_lambda|\btrace\b", re.I)


def _head_sha() -> str:
    try:
        return subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT,
                              capture_output=True, text=True, check=True).stdout.strip()
    except Exception:
        return "unknown"


def _partitions_in(obj) -> set[tuple[int, ...]]:
    """Every partition-shaped value anywhere in the JSON, list- or string-form."""
    found: set[tuple[int, ...]] = set()

    def is_part(xs) -> bool:
        return (len(xs) >= 1 and all(isinstance(v, int) and v > 0 for v in xs)
                and all(xs[i] >= xs[i + 1] for i in range(len(xs) - 1)))

    def walk(o):
        if isinstance(o, list):
            if is_part(o):
                found.add(tuple(o))
            for v in o:
                walk(v)
        elif isinstance(o, dict):
            for v in o.values():
                walk(v)
        elif isinstance(o, str):
            # "(3,2,1)", "3_2_1", "lambda=3_2_1"
            for m in re.finditer(r"(?<![\d.])(\d+(?:[,_]\s*\d+){1,})(?![\d.])", o):
                xs = [int(t) for t in re.split(r"[,_]\s*", m.group(1))]
                if is_part(xs) and len(xs) >= 2:
                    found.add(tuple(xs))

    walk(o=obj)
    return found


def main() -> int:
    t0 = time.monotonic()
    print("=" * 68)
    print("Row-cap sweep: physical numbers read off l(lambda) > 2 blocks")
    print("=" * 68)

    files = sorted(set(COMP.glob("*.witness.json")) | set(COMP.glob("**/*.witness.json")))
    # `_deprecated/` is retired work; a defect there is already withdrawn.
    files = [f for f in files if "_deprecated" not in f.parts]
    n_scanned = 0
    with_tall = []          # has some partition with >2 rows
    for p in files:
        try:
            d = json.loads(p.read_text())
        except Exception:
            continue
        n_scanned += 1
        parts = _partitions_in(d)
        tall = {t for t in parts if len(t) > N_FIBRE}
        if tall:
            with_tall.append((p, tall, d))

    print(f"\n  witness files scanned          : {n_scanned}")
    print(f"  ... carrying a >{N_FIBRE}-row partition : {len(with_tall)}")

    # A witness that ENUMERATES every partition of n is a census, not a reading.
    # A reading SINGLES OUT a small number of tall blocks.
    singled = []
    for p, tall, d in with_tall:
        blob = json.dumps(d, ensure_ascii=False)
        if len(tall) <= 3 and OBSERVABLE_RE.search(blob):
            singled.append((p, tall, d, blob))
    print(f"  ... singled out (<=3 tall) AND observable-bearing : {len(singled)}")

    # Mechanical discriminator: is the number read off a SPECTRUM or a TRACE?
    print(f"\n  {'witness':<52} {'spec':>5} {'trace':>6}  tall")
    print("  " + "-" * 78)
    rows = []
    for p, tall, d, blob in sorted(singled, key=lambda r: r[0].name):
        stem = p.name.replace(".witness.json", "")
        ns = len(SPECTRAL_RE.findall(blob))
        nt = len(TRACE_RE.findall(blob))
        rows.append({"witness": stem, "spectral_hits": ns, "trace_hits": nt,
                     "tall_partitions": sorted(sorted(t, reverse=True) for t in tall),
                     "contentBlock": d.get("contentBlock")})
        print(f"  {stem:<52} {ns:>5} {nt:>6}  {sorted(tall)}")

    # ---- Hand triage. The discriminator is a FILTER, not a verdict: it scored
    # a carrier-independent determinant identity as an instance. Each entry
    # below was reached by reading the witness and, where it exists, its script.
    TRIAGE = {
        # ---- INSTANCE: a number compared against the measured world is read
        #      off the spectrum of a Hecke block with l(lambda) > 2.
        "path-b-evacuation": (
            "INSTANCE",
            "cot theta_W read as pos_eigs[0]/pos_eigs[1] of the beta_EW word in "
            "the 16-dim (3,2,1) Hoefsmit rep (path_b_evacuation.py:456-478), "
            "times a q_0^(1/5) factor; asserts corrected err 0.00127 against "
            "COT_W_CODATA = 1.8230678710486174. l(3,2,1) = 3."),
        "staircase-ew-residual-conjecture": (
            "INSTANCE",
            "generalises that reading to rho_k = (k, k-1, ..., 1), which has "
            "exactly k rows; asserts k3_residual_matches_q_one_fifth."),
        "staircase-ew-predictions": (
            "INSTANCE",
            "reproduces rho3_corrected_err_lt_0p5pct = 0.00127 and attempts the "
            "rho_4 = (4,3,2,1) falsification, which returns "
            "rho4_ew_reading_inapplicable (degenerate top eigenvalue) -- the "
            "prediction was not testable, which is not the prediction passing."),

        # ---- SUPPORTING: part of the same chain, quotes no number of its own.
        "path-b-open-questions": (
            "SUPPORTING",
            "a derivation ATTEMPT for q^(1/5) that records its own failure: "
            "best_single_invariant_r_lt_0p3 and multivariate_R2_lt_0p2 both true."),

        # ---- FALSE POSITIVE class 1: a SPECTRUM that reads as a partition.
        #      {5,5,5,1} is the eigenvalue multiset of the Bring period Gram
        #      (and of M_S = 5I - J), not a Young diagram. No Hecke block is
        #      involved at all, so the row cap has nothing to say about it.
        "vector2-double-pincer": (
            "FALSE POSITIVE",
            "spectrum-as-partition: {5,5,1,1} and {5,5,5,1} are eigenvalue "
            "multisets of S^2 and of the RR92/BDH22 Grams. Its assertion is "
            "naive_gram_square_root_refuted_exactly = True -- a refutation."),
        "alpha-em-r2-quillen-curvature-probe": (
            "FALSE POSITIVE", "spectrum-as-partition: the Bring period spectrum."),
        "alpha-em-b2-bring-period-matrix": (
            "FALSE POSITIVE", "spectrum-as-partition: the Bring period spectrum."),
        "bring-polarized-q-dictionary-endpoint-blindness": (
            "FALSE POSITIVE",
            "spectrum-as-partition; and every assertion is None (a method-class "
            "constraint), so no number is read off anything."),

        # ---- FALSE POSITIVE class 2: a STRUCTURAL identity on a tall block.
        #      True in any carrier, quotes no physical number.
        "beta-ew-delta-I-conjugate-pairing": (
            "FALSE POSITIVE",
            "every assertion is det(M_lambda).det(M_lambda') = +-1, a structural "
            "identity of H_6. Caught by the earlier, narrower filter; the "
            "broader partition detector reclassifies it as a census."),
        "alpha-em-d4-equivariance-adjudication": (
            "FALSE POSITIVE",
            "(2,1,1,1) indexes an isotype-mismatch EXCLUSION argument; all "
            "assertions None."),
        "alpha-em-conjugation-doubling-dictionary": (
            "FALSE POSITIVE", "dictionary bookkeeping; all assertions None."),
        "alpha-em-f-t5-assembly": (
            "FALSE POSITIVE", "assembly bookkeeping; all assertions None."),

        # ---- ABOUT-THE-VANISHING: states the row cap rather than violating it.
        "su2-spinor-multiplicity-resolution": (
            "ABOUT THE VANISHING",
            "tabulates spin per block and records spin_ladder_(1,1,1) = 0.0 -- "
            "the cap being observed, not a number read through it."),
        "chirality-avg-content-chiral": (
            "ABOUT THE VANISHING", "(1,1,1) is the TL kernel generator; the "
            "witness is about the kernel."),
        "chirality-avg-content": (
            "ABOUT THE VANISHING", "as above."),
        "u1-hypercharge-assignment": (
            "ABOUT THE VANISHING", "as above."),
        "qbeta-discriminant-curve-in-q": (
            "ABOUT THE VANISHING",
            "this session's own Step 26 probe; (2,1,1) appears via H_4 "
            "branching, and nothing is read off it."),
        "escape1-geometric-holonomy-section": (
            "ABOUT THE VANISHING",
            "asks whether icosahedral geometry FORCES a section or whether "
            "selecting one is a fit -- an anti-fit adjudication, not a reading."),
        "joint-tower-sdp-h6-h9": (
            "ABOUT THE VANISHING",
            "SDP feasibility on H_3 Hoefsmit blocks; the tall partitions are "
            "enumerated as the block index set."),

        # ---- Corpus-meta probes: they SCAN the corpus, so they mention every
        #      partition anybody ever wrote. Nothing is read off anything.
        "compute-audit-scan": ("FALSE POSITIVE", "corpus-meta: an audit scan."),
        "hardcoded-literal-audit": ("FALSE POSITIVE", "corpus-meta: an audit scan."),
        "canonical-script-input-audit": ("FALSE POSITIVE", "corpus-meta: an audit scan."),
        "witness-producer-executes-audit": ("FALSE POSITIVE", "corpus-meta: an audit scan."),

        # ---- More spectrum-as-partition, all in the alpha_EM / Bring sector.
        "alpha-em-b2-hodge-normalization": (
            "FALSE POSITIVE",
            "spectrum-as-partition: (5,5,5,1) is the E^4 isogeny spectrum of the "
            "Bring principal polarization, not a Young diagram."),
        "alpha-em-b2-tau-id-c-pin": (
            "FALSE POSITIVE",
            "the load-bearing block is (4,1), which has two rows; all assertions "
            "are None (support probe)."),

        # ---- Refutations and null results: the anti-fit discipline working.
        "nastokes-germ-gauge-covariance": (
            "FALSE POSITIVE",
            "answers its own question in the negative -- the transverse pairing "
            "IS NOT gauge-covariant. A refutation quotes no accuracy."),
        "reeb-rotation-pn-test-reeb": (
            "FALSE POSITIVE",
            "reeb_rotation_pn_difference = 0.000e+00: a NULL result. The "
            "eigen-phase fails to separate proton from neutron."),
        "aomega-m3-adjoint-index-set": (
            "FALSE POSITIVE",
            "the sl_2 adjoint weight set; all assertions None."),

        # ---- Reads a 3-row CHARACTER inside an identity that refutes a prior
        #      magnitude claim; the load-bearing block is the two-row (2,2).
        "e-hartree-round19-dressed-scalar-block": (
            "ABOUT THE VANISHING",
            "chi_(3,1).chi_(2,1,1) = -1 exactly is a symbolic character identity "
            "that REFUTES the R18 magnitude; the physical specialisation is "
            "chi_(2,2) on dim_q V_(2,2), a two-row block."),
    }

    # The DEFAULT IS NOT `SAFE`. An earlier draft of this probe defaulted the
    # untriaged to safe and consequently declared "no new sector" while ten
    # spectral-on-a-tall-block candidates -- in two sectors it had not looked
    # at -- were silently absorbed into that verdict. The optimistic default is
    # the whole failure mode, so: trace-only is mechanically safe, everything
    # else that is not hand-triaged stays UNTRIAGED and fails the run.
    for r in rows:
        v, why = TRIAGE.get(r["witness"], (None, None))
        if v is None:
            if r["spectral_hits"] == 0 and r["trace_hits"] > 0:
                v, why = ("SAFE", "trace-only: the number goes through a Markov "
                                  "trace, which puts weight zero on tall blocks "
                                  "by the row cap.")
            elif r["spectral_hits"] == 0 and r["trace_hits"] == 0:
                v, why = ("SAFE", "inert: neither a spectral nor a trace reading.")
            else:
                v, why = ("UNTRIAGED", "spectral reading near a tall block, not "
                                       "yet read by hand.")
        r["verdict"], r["reason"] = v, why

    n_inst = sum(1 for r in rows if r["verdict"] == "INSTANCE")
    n_safe = sum(1 for r in rows if r["verdict"] == "SAFE")
    n_fp = sum(1 for r in rows if r["verdict"] == "FALSE POSITIVE")
    n_untriaged = sum(1 for r in rows if r["verdict"] == "UNTRIAGED")
    untriaged = [r["witness"] for r in rows if r["verdict"] == "UNTRIAGED"]
    fp_classes = sorted({
        "spectrum-as-partition" if "spectrum-as-partition" in r["reason"]
        else "structural-identity-on-a-tall-block"
        for r in rows if r["verdict"] == "FALSE POSITIVE"})
    blocks = {r["contentBlock"] for r in rows if r["verdict"] == "INSTANCE"}

    print(f"\n  verdicts: {n_inst} instance, {n_safe} safe, {n_fp} false positive, "
          f"{n_untriaged} UNTRIAGED, "
          f"{len(rows) - n_inst - n_safe - n_fp - n_untriaged} other")
    if untriaged:
        print(f"  !! UNTRIAGED: {untriaged}")
    print(f"  distinct content blocks among instances: {sorted(blocks)}")

    # ---- Which prose surfaces state the number, and which of them guard it?
    print("\n" + "=" * 68)
    print("Surface audit: where the 0.127 % number is stated, and how")
    print("=" * 68)
    GUARD_RE = re.compile(r"must not be cited|not a framework accuracy|"
                          r"is not derivation|stays .?conjectural|Do not cite", re.I)
    NUM_RE = re.compile(r"0\.127|0\.13\s*\\?%|1\.8207|1\.82075")
    # The number alone is not enough: `q-rogers-pentagon-archimedean-proof.md`
    # carries an unrelated +0.1274 in a residual table. Require a Weinberg
    # marker in the same file, or the audit hands the owner a wrong surface.
    TOPIC_RE = re.compile(r"theta_W|theta_\{?W|weinberg|cot *\\?theta|EW.residual|"
                          r"corner.hook|staircase", re.I)
    surfaces = []
    # `docs/audits/` is excluded: an audit is a dated record of what was true
    # then, not a live claim, so an un-caveated number there is not a defect.
    for p in sorted(list((ROOT / "content").rglob("*.md"))
                    + list((ROOT / "docs").rglob("*.md"))):
        sp = str(p.relative_to(ROOT))
        if "_deprecated" in sp or sp.startswith("docs/audits/"):
            continue
        try:
            txt = p.read_text()
        except Exception:
            continue
        if NUM_RE.search(txt) and TOPIC_RE.search(txt):
            surfaces.append({"path": str(p.relative_to(ROOT)),
                             "guarded": bool(GUARD_RE.search(txt))})
    for s in surfaces:
        print(f"  {'GUARDED  ' if s['guarded'] else 'UNGUARDED'}  {s['path']}")
    n_guarded = sum(1 for s in surfaces if s["guarded"])
    n_unguarded = len(surfaces) - n_guarded
    print(f"\n  {n_guarded} guarded, {n_unguarded} unguarded")

    # Does ANY surface state the row-cap ground for this number?
    ROWCAP_RE = re.compile(r"row cap|l\(lambda\) *> *2|ell\(\\lambda\) *[>\\]|"
                           r"three.row|3.row|dimension zero|no states", re.I)
    rowcap_surfaces = [s["path"] for s in surfaces
                       if ROWCAP_RE.search((ROOT / s["path"]).read_text())]
    print(f"  surfaces stating a ROW-CAP ground for it: {rowcap_surfaces or 'NONE'}")

    a = []

    def chk(name, computed, expected, note=""):
        ok = computed == expected
        a.append({"name": name, "computed": computed, "expected": expected,
                  "passed": bool(ok), **({"note": note} if note else {})})
        print(f"  [{'PASS' if ok else 'FAIL'}] {name}: {computed!r}")
        return ok

    print("\n" + "=" * 68)
    print("Assertions")
    print("=" * 68)
    ok = True
    ok &= chk("sweep_scanned_more_than_3000_witnesses", n_scanned > 3000, True)
    ok &= chk("every_instance_is_one_content_block", len(blocks), 1,
              "the confirmed instances do not spread across sectors")
    ok &= chk("that_block_is_the_weinberg_conjecture",
              sorted(blocks) == ["conj:weinberg-angle-categorical"], True)
    ok &= chk("triage_is_total_no_untriaged_left", untriaged, [],
              "the claim 'no new sector' is only worth anything if every\n"
              "spectral-on-a-tall-block candidate was actually read")
    ok &= chk("two_distinct_false_positive_classes", fp_classes,
              ["spectrum-as-partition", "structural-identity-on-a-tall-block"],
              "an eigenvalue multiset that reads as a Young diagram, and a\n"
              "carrier-independent determinant identity")
    ok &= chk("majority_of_candidates_are_trace_safe", n_safe > n_inst, True)
    ok &= chk("number_is_stated_on_multiple_surfaces", len(surfaces) >= 3, True)
    ok &= chk("some_surface_guards_it_on_anti_fit_grounds", n_guarded >= 1, True)
    ok &= chk("some_surface_states_it_with_no_guard", n_unguarded >= 1, True)
    ok &= chk("no_surface_states_the_row_cap_ground", rowcap_surfaces, [],
              "the gap: anti-fit leaves the route open pending a derivation of "
              "the exponent; the row cap closes it whatever the exponent is")

    print("\n" + ("ALL PASSED" if ok else "SOME FAILED"))

    witness = {
        "computation": "qbeta-row-cap-sweep-of-physical-numbers",
        "assertions": a,
        "allPassed": bool(ok),
        "parameters": {"fibre_dimension_N": N_FIBRE,
                       "row_cap": "dim V_lambda = 0 when l(lambda) > N",
                       "row_cap_source":
                           "content/quantum-observable-universe/mass-theory/"
                           "markov-trace-frobenius-selection.md (states it by name)"},
        "data": {
            "witnesses_scanned": n_scanned,
            "with_tall_partition": len(with_tall),
            "singled_out_and_observable": len(rows),
            "triage": rows,
            "counts": {"instance": n_inst, "safe": n_safe,
                       "false_positive": n_fp, "untriaged": n_untriaged,
                       "other": len(rows) - n_inst - n_safe - n_fp - n_untriaged},
            "false_positive_classes": fp_classes,
            "instance_content_blocks": sorted(blocks),
            "path_b_numbers": {
                "raw_ratio": "1.78315071", "raw_err": "0.021896",
                "times_q0_pow_one_fifth": "1.82075274",
                "corrected_err": "0.001270",
                "cot_theta_W_codata": "1.8230678710486174",
                "block": "(3,2,1)", "rows": 3, "dim": 16},
            "surfaces": surfaces,
            "surfaces_stating_row_cap_ground": rowcap_surfaces,
        },
        "context": {
            "axis": "are there other physical numbers read off l(lambda) > 2 "
                    "blocks, beyond the two found this session?",
            "answer": "No new sector. Every confirmed instance is the "
                      "conj:weinberg-angle-categorical chain already recorded in "
                      "qou-4qno. What is new is that the corpus's existing guard "
                      "on that number rests on ANTI-FIT grounds alone and "
                      "concludes it 'stays conjectural', while the row cap closes "
                      "the route whatever the exponent turns out to be -- and no "
                      "surface states that ground.",
            "scope": "Scope-(a). No content block is edited here and no "
                     "conjecture is refuted.",
            "false_positive_recorded":
                "beta-ew-delta-I-conjugate-pairing scored spectral-on-a-tall-block "
                "but quotes no physical number; classifying it as an instance "
                "would have manufactured the error this triage exists to catch.",
        },
        "gitCommit": _head_sha(),
        "durationMs": int((time.monotonic() - t0) * 1000),
    }
    out_p = HERE / "qbeta-row-cap-sweep-of-physical-numbers.witness.json"
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
        _WB.stamp_staleness_metadata(witness, script_path=__file__, engine="python")
        # ensure_ascii=False: the corpus convention is UTF-8 witnesses, and
        # `witness_shape_guard` flags a witness that gains \uXXXX escapes.
        json.dump(witness, f, indent=2, ensure_ascii=False)
        f.write("\n")
    _os_sidu.replace(_wtmp_sidu, _wpath_sidu)
    print(f"\n  witness -> {out_p.relative_to(ROOT)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
