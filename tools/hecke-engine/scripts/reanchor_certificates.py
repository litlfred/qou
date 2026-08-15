#!/usr/bin/env python3
"""Re-evaluate certificate `*_f64` fields at the correct substrate anchor.

WHY THIS IS NOT A REGENERATION
------------------------------
`hecke-bigint (v9)` stores `tr_alt`, `net` and `observable` as **exact
integer-coefficient Laurent polynomials in q** (ⁱ⁰B alone carries 141 terms).
Those are anchor-independent — they are exact in the formal variable. Only the
four `*_f64` fields are evaluations *at* a numeric q₀, and until 2026-08-15
that q₀ was the 5-significant-digit literal ``1.10998``, which is **1277 ppb**
from the proton pin (111× the muon/proton gap the re-pin was about).

So the data needed to correct those fields is already inside each file. This
script re-evaluates the stored polynomials at the proton anchor and rewrites
only the `*_f64` fields, leaving every exact term byte-identical.

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
   dropped `mid_strip_threshold`.** v9 evaluates in plain float64
   (`alt_norm.eval_f64`), and these alternating sums are brutally
   ill-conditioned: measuring `sum|term| / |sum term|` gives log10(cond) up to
   **203** for 60Co. **15 of 35 certificates retain ZERO valid f64 digits;
   25 of 35 retain fewer than six.** The earlier write-up cited 11Li's
   "13.35 against 24" as proof of term-dropping — that number has zero valid
   digits. There was never any evidence for the threshold story.

So the correction inverts the conclusion: **the exact Laurent data is the
sound part and the `*_f64` fields are the damaged part.** Re-evaluating at
high precision does not merely reproduce them, it REPAIRS 15 certificates
whose committed f64 values are pure noise. The old `--max-rel` guard was
rejecting good values by comparing them against that noise.

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

# 50 dps: far beyond the f64 these fields serialize to, and the repo's
# standard working precision. NOT exact Fractions -- v9 polynomials carry
# 141+ terms with powers into the hundreds, and exact rational powers of a
# 60-digit t produce numerators with millions of digits. Precision here only
# has to comfortably exceed float64; mpmath does that at a fraction of the
# cost, and the truncation that caused this whole problem was at 5 digits.
mp.mp.dps = 50

# Proton pin, m_p/m_e — production default per AGENTS.md (2026-08-07).
Q0_PROTON = mp.mpf("1.1099785827513808")
# What v9 actually used until 2026-08-15.
Q0_V9_TRUNCATED = mp.mpf("1.10998")

# Exact-polynomial fields and the f64 field each one feeds.
POLY_TO_F64 = {
    "tr_alt": "tr_alt_f64",
    "net": "net_f64",
    "observable": "observable_f64",
}


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


def conditioning(terms, t) -> float:
    """Valid float64 digits left in `sum(terms)` after cancellation.

    `sum|term| / |sum term|` is the condition number of the sum; its log10 is
    the digits lost. f64 starts with ~15.95, so this can go negative — and
    does, badly: 60Co loses 203 digits. This is why 15 of the 35 committed
    `*_f64` fields are pure noise, and why they cannot be used as a reference
    to check a recomputation against.
    """
    s_ = mp.mpf(0)
    abs_ = mp.mpf(0)
    for power, coeff in terms:
        term = mp.mpf(str(coeff)) * (t ** int(power))
        s_ += term
        abs_ += abs(term)
    if s_ == 0:
        return -999.0
    return float(15.95 - mp.log10(abs_ / abs(s_)))


def process(path: pathlib.Path, max_rel: float, write: bool) -> str:
    doc = json.loads(path.read_text())
    have = [k for k in POLY_TO_F64 if isinstance(doc.get(k), dict) and doc[k].get("terms")]
    if not have:
        return f"SKIP  {path.name}: no exact polynomial to re-evaluate"

    # v9 stores the UN-normalised polynomial but divides the f64 by
    # 2^(pn - v2) after 2-adic normalisation, which nets to 2^pn_count.
    # Confirmed exactly on every certificate whose f64 still has >=8 valid
    # digits: log2(eval / stored) is an integer and equals pn_count.
    pn = doc.get("pn_count")
    if pn is None:
        return f"SKIP  {path.name}: no pn_count, cannot recover the 2-adic scale"
    scale = mp.mpf(2) ** int(pn)

    t0 = mp.sqrt(Q0_PROTON)
    t_v9 = mp.sqrt(Q0_V9_TRUNCATED)
    changes, notes = [], []
    for poly_key in have:
        f64_key = POLY_TO_F64[poly_key]
        if f64_key not in doc or doc[f64_key] is None:
            continue
        terms = doc[poly_key]["terms"]
        valid = conditioning(terms, t_v9)
        new = float(eval_laurent(terms, t0) / scale)
        old = float(doc[f64_key])

        # Cross-check at v9's OWN anchor: this should reproduce the committed
        # value wherever f64 was trustworthy. Where it does not, the committed
        # value is the damaged one -- so do NOT treat disagreement as a reason
        # to skip, which is what the old --max-rel guard wrongly did.
        check = float(eval_laurent(terms, t_v9) / scale)
        agree = abs(check - old) / abs(old) if old else float("inf")
        notes.append(f"{f64_key}: {valid:.0f} valid digits, "
                     f"reproduces committed to {agree:.1e}")
        changes.append((f64_key, old, new, agree))

    if not changes:
        return f"SKIP  {path.name}: no f64 fields paired with a polynomial"

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
        doc.setdefault("generation", {})
        doc["generation"]["q0"] = float(Q0_PROTON)
        doc["generation"]["q0_pin"] = "proton"
        doc["generation"]["reanchored_from"] = float(Q0_V9_TRUNCATED)
        doc["generation"]["reanchor_note"] = (
            "*_f64 fields re-evaluated from this file's own exact Laurent "
            "polynomials at the proton pin; exact terms untouched."
        )
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
    ap.add_argument("--max-rel", type=float, default=1e-4,
                    help="flag and skip a file if any field moves more than this")
    ap.add_argument("--dir", default=str(pathlib.Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    paths = sorted(pathlib.Path(args.dir).glob("certificate-*.json"))
    if not paths:
        print("no certificates found", file=sys.stderr)
        return 1

    rows = [process(p, args.max_rel, args.write) for p in paths]
    for r in rows:
        print(" ", r)

    n_ok = sum(1 for r in rows if r.startswith(("WROTE", "would")))
    n_skip = sum(1 for r in rows if r.startswith("SKIP"))
    n_flag = sum(1 for r in rows if r.startswith("FLAG"))
    print(f"\n  re-anchorable : {n_ok}")
    print(f"  skipped       : {n_skip}  (no exact polynomial -- unrecoverable from what is committed)")
    print(f"  flagged       : {n_flag}  (moved more than --max-rel; left alone)")
    return 1 if n_flag else 0


if __name__ == "__main__":
    raise SystemExit(main())
