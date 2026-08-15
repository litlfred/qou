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

RESULT: THE PREMISE ABOVE IS FALSE FOR ALL 51 — THIS IS NOW A DIAGNOSTIC
------------------------------------------------------------------------
The hypothesis was that re-evaluating a stored polynomial at the proton pin
reproduces the committed `*_f64` up to the ~1.3e-6 anchor shift. It does not,
for any of the 35. The guard refused every one rather than overwrite it, which
is the only reason this did not become 35 files of quietly wrong numbers.

Two distinct reasons, both traced:

1. **An unrecorded 2-adic denominator.** v9 computes the f64 from a
   2-adically normalised polynomial divided by `2^(pn - v2)`; the stored
   polynomial is the un-normalised one. For some files the ratio is exactly
   `2^pn_count` — ¹⁰B gives log2 = 24.998 against `pn_count = 25`, ¹¹C gives
   29.994 against 30 — so those differ by that factor alone.

2. **The mid-strip threshold dropped terms.** For the rest the ratio's log2 is
   NOT an integer: ¹⁰He 14.91 against `pn_count = 16`, ¹¹Li 13.35 against 24.
   A non-integer log2 cannot be a 2-adic factor, so the stored polynomial is
   not the one the f64 was computed from. `hecke-bigint`'s
   `mid_strip_threshold` *drops terms during accumulation*, and it was never
   recorded — so which terms survived is unknowable from the file.

So the 51 committed certificates are **not reproducible from their own
contents**, and no amount of care recovers them. That is exactly the gap
`crate::provenance` closes for everything emitted from now on.

This script is retained as the DIAGNOSTIC that established the above.
`--write` is disabled: there is no correct value to write.

Usage:
    python3 reanchor_certificates.py        # diagnostic report
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


def process(path: pathlib.Path, max_rel: float, write: bool) -> str:
    doc = json.loads(path.read_text())
    have = [k for k in POLY_TO_F64 if isinstance(doc.get(k), dict) and doc[k].get("terms")]
    if not have:
        return f"SKIP  {path.name}: no exact polynomial to re-evaluate"

    t0 = mp.sqrt(Q0_PROTON)
    changes, flags = [], []
    for poly_key in have:
        f64_key = POLY_TO_F64[poly_key]
        if f64_key not in doc or doc[f64_key] is None:
            continue
        new = float(eval_laurent(doc[poly_key]["terms"], t0))
        old = float(doc[f64_key])
        rel = abs(new - old) / abs(old) if old else (0.0 if new == 0 else float("inf"))
        if rel > max_rel:
            flags.append(f"{f64_key} moved {rel:.2e} (> {max_rel:.0e})")
        changes.append((f64_key, old, new, rel))

    if flags:
        return f"FLAG  {path.name}: " + "; ".join(flags) + " -- left alone"
    if not changes:
        return f"SKIP  {path.name}: no f64 fields paired with a polynomial"

    # f_pauli = |tr_alt / net| — derived, so recompute from the corrected pair
    # rather than re-evaluating a ratio of two separately-rounded floats.
    if {"tr_alt", "net"} <= set(have) and doc.get("f_pauli_f64") is not None:
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
    return (
        f"{'WROTE' if write else 'would'} {path.name}: "
        f"{len(changes)} f64 field(s), worst rel move {worst:.2e}"
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true",
                    help="DISABLED - see the module docstring. The committed "
                         "certificates cannot be re-anchored from their own "
                         "contents, so there is no correct value to write.")
    ap.add_argument("--max-rel", type=float, default=1e-4,
                    help="flag and skip a file if any field moves more than this")
    ap.add_argument("--dir", default=str(pathlib.Path(__file__).resolve().parent.parent))
    args = ap.parse_args()

    paths = sorted(pathlib.Path(args.dir).glob("certificate-*.json"))
    if not paths:
        print("no certificates found", file=sys.stderr)
        return 1

    if args.write:
        print("--write is disabled: the committed certificates are not "
              "reproducible from their own contents (unrecorded 2-adic "
              "denominator + unrecorded mid_strip_threshold). See the module "
              "docstring.", file=sys.stderr)
        return 2

    rows = [process(p, args.max_rel, False) for p in paths]
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
