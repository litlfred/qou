#!/usr/bin/env python3
"""Re-evaluate certificate `*_f64` fields at the correct substrate anchor.

WHY THIS IS NOT A REGENERATION
------------------------------
`hecke-bigint (v9)` stores `tr_alt`, `net` and `observable` as **exact
integer-coefficient Laurent polynomials in q** (ⁱ⁰B alone carries 141 terms).
Those are anchor-independent — they are exact in the formal variable. The
`*_f64` fields, by contrast, are evaluations *at* a numeric q₀, and until
2026-08-15 that q₀ was the 5-significant-digit literal ``1.10998``, which is
**1277 ppb** from the proton pin (111× the muon/proton gap the re-pin was
about).

So for SOME fields the data needed to correct them is already inside each
file. This script re-evaluates those stored polynomials at the proton anchor
and rewrites only the corresponding `*_f64` fields, leaving every exact term
byte-identical.

**Coverage is partial, and the docstring used to overstate it** — it said
"the four `*_f64` fields", a count matching nothing. Measured across all 51
certificates:

===================  =====  =========================================
`*_f64` field        count  exact source
===================  =====  =========================================
``tr_alt_f64``          50  ``tr_alt``      — re-anchorable
``net_f64``             50  ``net``         — re-anchorable
``f_pauli_f64``         50  derived ratio   — re-anchorable
``tr_markov_f64``       12  ``tr_markov_cleared``, present in **1**
``l1_norm_f64``          2  none
===================  =====  =========================================

The last two are why `--write` reports BLOCK on 12 files: rewriting three
fields while a fourth stays at 1.10998 leaves one certificate straddling two
anchors, with nothing recording the split. That is worse than not touching it.

**`tr_markov_f64` is not a Markov trace, in any convention (measured
2026-10-11, bean qou-m7py).** `v9.rs` weights each word by ``z^len(w)``
with ``z = 1/(t + t⁻¹)``, ``t = √q`` (convention C, excised 2026-08-15). The
Markov trace is not multiplicative in word length: ``tr(σ₀σ₁σ₀) = h·z² + z``,
not ``z³`` (the same defect `gram.rs` fixed in `TR_M[5]`). The exact `jets`
reproduce the committed value under that z^len rule to ~12 digits, which
identifies the formula; it does not make the value a trace. A convention-D
trace needs the per-word element, which the certificates do not store.
**Deleted 2026-10-11 (owner ruling, litlfred/qou#7685):** v9 no longer
writes `tr_markov_f64` / `tr_markov_cleared` / `tr_markov_denom_power`; it
writes `tr_markov_d`, the exact Ocneanu trace at ``z = q³/(q²+1)``, computed
in v9 from the full crossing product. The old values and code are on branch
`cat/cat-harness/fsh-guts` under
`fsh-guts/deprecated/tools/hecke-engine/v9-tr-markov-zlen/`.

**And 34 of the 35 v9 certificates were built with a pre-fix crossing.**
Their exact polynomials carry odd powers of ``t``; at every commit they are
stamped with (`62d305e` and seven others, all 2026-04-05) the n-n crossing was ``t⁴σ + t − t³``, which is not
proportional to ``σ⁻¹ = σ − (t² − t⁻²)`` under v9's own relation
``σ² = (t² − t⁻²)σ + 1``. Only 40Ar (`1b1b1d5`) uses the fixed crossing.
So the 22 fields re-anchored on 2026-10-10 are faithful evaluations of a
mis-built element. Only `fsh-guts` deprecated scripts read these files.
All 35 were regenerated with the current v9 on 2026-10-11 (#7686), so the
v9 certificates now carry proton-pin `*_f64` fields straight from the
generator and this script has nothing to re-anchor in them.

That matters because the obvious alternative — re-running the generator — is
actively destructive here: the 51 committed certificates come from four
different binaries, and re-running the wrong one replaces exact symbolic data
with an f64 summary (measured: a `hecke-crt` re-run of ¹⁰B produced
``f_pauli_f64: 0.0`` and dropped 4188 lines of exact terms).

RETRACTED VERDICT, AND THE ACTUAL ANSWER (2026-08-15)
-----------------------------------------------------
An earlier version of this file concluded the 51 certificates are "not
reproducible from their own contents ... no amount of care recovers them",
and bean qou-f9th was titled "closed question, do not retry". **That was
wrong**, and it is the scope-(b) over-narrowing AGENTS.md forbids: a failed
probe was written up as a structural exclusion.

What was actually going on, measured:

1. **The 2-adic denominator is exactly `2^pn_count`.** v9 divides by
   `2^(pn - v2)` after 2-adically normalising, while storing the un-normalised
   polynomial. Across all 9 certificates whose f64 field has >=8 valid digits,
   `log2(eval(tr_alt) / tr_alt_f64)` is an exact integer AND equals `pn_count`
   in every case (3,4,6,6,5,12,6,10,16). `pn_count` is recorded in the file.

2. **The non-integer ratios elsewhere are CATASTROPHIC CANCELLATION, not a
   dropped `mid_strip_threshold`.** These alternating sums are brutally
   ill-conditioned: `sum|term| / |sum term|` reaches log10(cond) = **359** for
   60Co, 187 for 40Ar, 142 for 40Ca. The earlier write-up cited 11Li's
   "13.35 against 24" as proof of term-dropping — that number has ~0 valid
   digits. There was never any evidence for the threshold story.

   *Two corrections to my own earlier statement of this point, both found in
   review.* It said log10(cond) reached **203**; that figure is reproducible
   from nothing — the true value is 359.2 and this script used to report 52,
   because `conditioning()` measured the cancellation at a precision the
   cancellation had already exhausted. A diagnostic cannot be evaluated at the
   precision it is diagnosing, so the working precision is now chosen per
   certificate from a high-precision scratch pass (`--scratch-dps`).

3. **v9 does NOT always evaluate in float64.** It falls back to MPFR
   (`v9.rs:838-856`) when the f64 eval of the *normalised* polynomial
   overflows or the denominator underflows. Certificates that took that path
   have ACCURATE committed values. Measured across the set: exactly one did —
   60Co, which is also the worst-conditioned. So the blanket claim "15 of 35
   retain zero valid f64 digits" was wrong for the single most extreme file,
   and this script would have overwritten the most accurate certificate in the
   set with `-inf`. `took_mpfr_path()` now detects this per file and refuses.

So the correction inverts the conclusion: **the exact Laurent data is the
sound part and the `*_f64` fields are (mostly) the damaged part.** The old
`--max-rel` guard was rejecting good values by comparing them against that
noise; it has been removed rather than repaired, since its premise was wrong.

Credit where due: a red-team pass found the cancellation. It was right that
cancellation is real and that the threshold story was unsupported; it was
wrong that cancellation replaces the 2-adic explanation — both are present,
and separating them is what makes the repair possible.
"""
from __future__ import annotations

import argparse
import json
import pathlib
import sys

import mpmath as mp

# Precision is chosen PER CERTIFICATE, not fixed.
#
# A fixed `mp.dps = 50` was the original choice, on the reasoning that it
# comfortably exceeds float64 and the truncation that caused the problem was
# at 5 digits. That reasoning does not survive the cancellation: 60Co loses
# 359 digits, so at 50 dps the result is not merely imprecise, it is sign- and
# magnitude-wrong, and the conditioning diagnostic reported 52 instead of 359
# because it was clamped by the same exhausted precision.
#
# So: measure the cancellation at SCRATCH_DPS, then evaluate at
# `cancellation + PRECISION_MARGIN`. Still mpmath rather than exact Fractions
# -- v9 polynomials carry 141+ terms with powers into the hundreds, and exact
# rational powers of a t at this precision produce numerators with millions of
# digits.
SCRATCH_DPS = 1200
PRECISION_MARGIN = 60

# Proton pin, m_p/m_e — production default per AGENTS.md (2026-08-07).
Q0_PROTON = "1.1099785827513808"
# What v9 actually used until 2026-08-15.
Q0_V9_TRUNCATED = "1.10998"

# Exact-polynomial fields and the f64 field each one feeds.
#
# `observable` is NOT here despite 11 certificates carrying it as an exact
# polynomial: NO certificate has an `observable_f64` field, so the mapping was
# dead -- `process()` skipped it on the `f64_key not in doc` branch every time.
# Measured over all 51: the *_f64 fields present are f_pauli_f64 (50),
# tr_alt_f64 (50), net_f64 (50), tr_markov_f64 (12), l1_norm_f64 (2).
POLY_TO_F64 = {
    "tr_alt": "tr_alt_f64",
    "net": "net_f64",
}

# f64 fields this script CANNOT re-anchor, and why. Reported per file rather
# than silently left at the old anchor, because a partial rewrite is worse
# than none: it would leave one file carrying some fields at the proton pin
# and others at 1.10998, with nothing recording the split.
UNPAIRED_F64 = {
    # 12 certificates carry tr_markov_f64; only 1 carries tr_markov_cleared.
    "tr_markov_f64": "tr_markov_cleared",
    # 2 certificates carry l1_norm_f64; no exact source field exists at all.
    "l1_norm_f64": None,
}


def _fits_f64(x) -> bool:
    """Can this mpf be serialized as a JSON number at all?

    `float(mpf)` silently yields +-inf on overflow, and `json.dumps` writes
    that as bare `Infinity` -- accepted by Python, rejected by serde_json, so
    the certificate would stop parsing in the engine that consumes it. 60Co
    hit exactly this.
    """
    try:
        v = float(x)
    except (OverflowError, ValueError):
        return False
    return v == v and abs(v) != float("inf")


def eval_laurent(terms, t):
    """Evaluate a sparse Laurent polynomial at 50 dps.

    `terms` is a list of `[power, coeff]`; coefficients are exact integers
    carried as decimal strings, so they are read with `mp.mpf(str(...))` and
    never through a float. The variable is t = sqrt(q) — v9 stores powers in
    t, which is why the caller passes sqrt(q0), not q0.
    """
    acc = mp.mpf(0)
    for power, coeff in terms:
        acc += mp.mpf(str(coeff)) * (t ** int(power))
    return acc


def cancellation_digits(terms, q0: str) -> float:
    """Decimal digits annihilated by cancellation in `sum(terms)`.

    `sum|term| / |sum term|` is the condition number of the sum; its log10 is
    the digits lost. Measured at SCRATCH_DPS, NOT at the working precision --
    the previous version measured it at the working precision and so reported
    52 for a value of 359, having run out of digits mid-diagnosis. A
    conditioning estimate evaluated at the precision it is estimating is
    self-limiting and reads as reassuring exactly when it should not.
    """
    with mp.workdps(SCRATCH_DPS):
        t = mp.sqrt(mp.mpf(q0))
        s_ = mp.mpf(0)
        abs_ = mp.mpf(0)
        for power, coeff in terms:
            term = mp.mpf(str(coeff)) * (t ** int(power))
            s_ += term
            abs_ += abs(term)
        if s_ == 0 or abs_ == 0:
            return float("inf")
        return float(mp.log10(abs_ / abs(s_)))


def valid_f64_digits(cancel: float) -> float:
    """Valid digits left in a float64 evaluation. f64 starts with ~15.95."""
    return 15.95 - cancel


def _v2(n: int) -> int:
    """2-adic valuation; `10**9` stands in for infinity at n = 0."""
    n = abs(int(n))
    if n == 0:
        return 10**9
    return (n & -n).bit_length() - 1


def took_mpfr_path(doc) -> bool:
    """Did v9 compute this certificate's f64 fields in MPFR rather than f64?

    v9.rs:838 takes the f64 branch only when the eval of the *2-adically
    normalised* polynomials is finite and the denominator is not underflowed;
    otherwise it falls back to MPFR at `(mc + 100) * 4` bits. A certificate
    that took the fallback has ACCURATE committed values and must not be
    "repaired" -- doing so would replace the best data in the set with worse.

    Replicated here rather than inferred, because the distinction is invisible
    in the certificate: nothing records which branch ran. Measured over the 35
    certificates with an exact tr_alt/net pair, exactly one took it (60Co),
    which is also the worst-conditioned file at 359 digits of cancellation.
    """
    ta, nt = doc.get("tr_alt"), doc.get("net")
    if not (isinstance(ta, dict) and ta.get("terms")):
        return False
    if not (isinstance(nt, dict) and nt.get("terms")):
        return False
    t0 = float(Q0_V9_TRUNCATED) ** 0.5

    def eval_normalised(terms) -> float:
        k = min(_v2(c) for _, c in terms)
        acc = 0.0
        for power, coeff in terms:
            try:
                acc += float(int(coeff) >> k) * (t0 ** int(power))
            except OverflowError:
                return float("inf")
        return acc

    a = eval_normalised(ta["terms"])
    n = eval_normalised(nt["terms"])
    finite = a == a and n == n and abs(a) != float("inf") and abs(n) != float("inf")
    return not (finite and abs(n) > 1e-300)


SIGNOFF = ""


def process(path: pathlib.Path, write: bool) -> str:
    doc = json.loads(path.read_text())
    have = [k for k in POLY_TO_F64 if isinstance(doc.get(k), dict) and doc[k].get("terms")]
    if not have:
        # Scope (a): not re-anchorable BY THIS ROUTE -- re-evaluating a stored
        # polynomial needs a stored polynomial. An earlier version called
        # these "unrecoverable from what is committed", which is the scope-(b)
        # over-claim AGENTS.md forbids: these certificates come from
        # hecke-modular and hecke-crt, whose generators can be re-run, and no
        # invariant says their values cannot be obtained.
        return f"SKIP  {path.name}: no exact polynomial (f64-summary generator)"

    if took_mpfr_path(doc):
        return (f"KEEP  {path.name}: v9 computed this in MPFR, not float64 "
                f"(v9.rs:838 fallback) -- committed f64 is accurate; "
                f"re-evaluating would REPLACE good data")

    # v9 stores the UN-normalised polynomial but divides the f64 by
    # 2^(pn - v2) after 2-adic normalisation, which nets to 2^pn_count.
    # Confirmed exactly on every certificate whose f64 still has >=8 valid
    # digits: log2(eval / stored) is an integer and equals pn_count.
    pn = doc.get("pn_count")
    if pn is None:
        return f"SKIP  {path.name}: no pn_count, cannot recover the 2-adic scale"
    # Working precision from the worst cancellation in this file, so a
    # 359-digit annihilation is evaluated at ~419 dps and a benign one is not
    # paid for. Both anchors are measured; they differ by 1277 ppb, which does
    # not move the conditioning, but taking the max costs nothing.
    cancel = max(
        max(cancellation_digits(doc[k]["terms"], q)
            for q in (Q0_PROTON, Q0_V9_TRUNCATED))
        for k in have
    )
    if cancel == float("inf"):
        return f"SKIP  {path.name}: a polynomial sums to exactly zero"
    work_dps = max(50, int(cancel) + PRECISION_MARGIN)

    changes, notes = [], []
    with mp.workdps(work_dps):
        scale = mp.mpf(2) ** int(pn)
        t0 = mp.sqrt(mp.mpf(Q0_PROTON))
        t_v9 = mp.sqrt(mp.mpf(Q0_V9_TRUNCATED))
        for poly_key in have:
            f64_key = POLY_TO_F64[poly_key]
            if f64_key not in doc or doc[f64_key] is None:
                continue
            terms = doc[poly_key]["terms"]
            valid = valid_f64_digits(cancellation_digits(terms, Q0_V9_TRUNCATED))
            new_mp = eval_laurent(terms, t0) / scale
            old = float(doc[f64_key])

            # An mpf can exceed f64 range even when the value is correct;
            # emitting it as a float would serialize as Infinity, which is not
            # valid JSON and which serde_json rejects outright. Report the
            # magnitude rather than writing an unusable number.
            if not _fits_f64(new_mp):
                notes.append(f"{f64_key}: OUT OF f64 RANGE "
                             f"(10^{int(mp.log10(abs(new_mp)))})")
                continue
            new = float(new_mp)

            # Cross-check at v9's OWN anchor: this should reproduce the
            # committed value wherever f64 was trustworthy. Where it does not,
            # the committed value is the damaged one -- so do NOT treat
            # disagreement as a reason to skip, which is what the old
            # --max-rel guard wrongly did.
            check_mp = eval_laurent(terms, t_v9) / scale
            agree = (float(abs(check_mp - old) / abs(old)) if old
                     else float("inf"))
            notes.append(f"{f64_key}: {valid:.0f} valid digits, "
                         f"reproduces committed to {agree:.1e}")
            changes.append((f64_key, old, new, agree))

        unpaired = [k for k in UNPAIRED_F64 if doc.get(k) is not None]
        if unpaired:
            notes.append("CANNOT re-anchor " + ",".join(unpaired)
                         + " (no exact source field)")

    if not changes:
        return f"SKIP  {path.name}: no f64 fields paired with a polynomial"
    if unpaired:
        return (f"BLOCK {path.name}: {len(changes)} field(s) re-anchorable but "
                f"{','.join(unpaired)} has no exact source -- writing would "
                f"leave one file straddling two anchors; " + "; ".join(notes))

    # f_pauli = |tr_alt / net| — derived, so recompute from the corrected pair
    # rather than re-evaluating a ratio of two separately-rounded floats.
    if {"tr_alt", "net"} <= set(have) and doc.get("f_pauli_f64") is not None:
        # f_pauli = |tr_alt/net| -- the 2^pn_count cancels in the ratio.
        ta = eval_laurent(doc["tr_alt"]["terms"], t0)
        nt = eval_laurent(doc["net"]["terms"], t0)
        if nt != 0:
            changes.append(
                ("f_pauli_f64", float(doc["f_pauli_f64"]), float(abs(ta / nt)), 0.0)
            )

    if write:
        for key, _old, new, _rel in changes:
            doc[key] = new
        # A schema-VALID generation block. The previous version wrote only
        # `q0` and `q0_pin` onto a possibly-absent object, leaving the
        # schema's required `binary`, `argv` and `reproduce` missing -- so a
        # --write run would have produced certificates that fail validation
        # against the very schema this branch added.
        #
        # The honest content is this script's own invocation: after a
        # re-anchor, THIS is how the f64 fields got their values, and the
        # original generator no longer describes them. The prior block is
        # preserved rather than overwritten.
        prior = doc.get("generation")
        doc["generation"] = {
            "binary": pathlib.Path(sys.argv[0]).name,
            "argv": [pathlib.Path(sys.argv[0]).name, *sys.argv[1:]],
            "reproduce": "python3 tools/hecke-engine/scripts/reanchor_certificates.py --write",
            "q0": float(mp.mpf(Q0_PROTON)),
            "q0_pin": "proton",
            "engine_version": "reanchor",
            "commit": "",
            "reanchored_from": float(mp.mpf(Q0_V9_TRUNCATED)),
            "reanchor_note": (
                "*_f64 fields re-evaluated from this file's own exact Laurent "
                f"polynomials at the proton pin, at {work_dps} dps chosen from "
                f"{cancel:.0f} digits of cancellation; exact terms untouched."
            ),
            "owner_signoff": SIGNOFF,
            "generated_by": prior,
        }
        path.write_text(json.dumps(doc, indent=2) + "\n")

    worst = max(c[3] for c in changes)
    verdict = "REPRODUCED" if worst < 1e-6 else "REPAIRS-NOISE"
    return (
        f"{'WROTE' if write else 'would'} {path.name}: {verdict}, "
        f"{len(changes)} field(s); " + "; ".join(notes)
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="apply (default: dry run)")
    ap.add_argument("--signoff", default="",
                    help="required with --write: where the owner approved it")
    ap.add_argument("--dir", default=str(pathlib.Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    paths = sorted(pathlib.Path(args.dir).glob("certificate-*.json"))
    if not paths:
        print("no certificates found", file=sys.stderr)
        return 1

    if args.write and not args.signoff:
        print(
            "--write rewrites committed certificate data, which is an owner\n"
            "call. Pass --signoff '<where the owner approved it>' so the record\n"
            "of that approval lands in each rewritten file's generation block.\n"
            "BLOCK, KEEP and SKIP files are never written either way.\n",
            file=sys.stderr,
        )
        return 2
    if args.write:
        global SIGNOFF
        SIGNOFF = args.signoff

    rows = [process(p, args.write) for p in paths]
    for r in rows:
        print(" ", r)

    def n(prefix):
        return sum(1 for r in rows if r.startswith(prefix))

    print(f"\n  re-anchorable : {n('would') + n('WROTE')}"
          f"{'  (written)' if args.write else ''}")
    print(f"  blocked       : {n('BLOCK')}  (an f64 field has no exact source; "
          f"a partial write would straddle two anchors)")
    print(f"  keep as-is    : {n('KEEP')}   (v9 used MPFR; committed value is "
          f"the accurate one)")
    print(f"  skipped       : {n('SKIP')}  (no exact polynomial in the file -- "
          f"NOT a claim that the value is unrecoverable; these come from "
          f"generators that can be re-run)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
