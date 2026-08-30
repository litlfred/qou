#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical mpmath/sympy regenerator; symbolic source is y-lambda-wenzl-bridge-symbolic-witness.json.
"""Regenerate `y-lambda-mpfr-witness.json` at TRUE 50 dps from the
symbolic Wenzl-bridge witness.

Per the convention/precision audit on PR #564, the previous
`y-lambda-mpfr-witness.json` was produced by
`_deprecated/y_lambda_mpfr_witness.py:152` with

    q_str = str(Q0_FLOAT)   # truncates Python float to 16 digits

so its claimed "50 dps" y_λ values were f64-truncated past digit ~14:

    mpfr  (claimed 50 dps): 0.05918771693214865618475938399646…
    symbolic (true 50 dps): 0.05918771693214863172663201740000…
                                          ^^^^^^^^^^^^^^^^^^ noise

The downstream cascade (`tr_m_wenzl_bridge_mpfr.py` →
`atomic-tr-m-mpfr-50dps.witness.json` → every canonical |tr_M|
reader) inherited this truncation, capping the Schur-Weyl identity
residual in `rho_k_h3a_refinement.py` at 1.4e-16 (machine f64
precision floor) instead of the 1e-40 tolerance the test gates at.

This regenerator side-steps the f64 issue by reading the symbolic
y_λ witness (`y-lambda-wenzl-bridge-symbolic-witness.json`, n=2..12,
exact symbolic in q) and evaluating each y_λ at the substrate q_0 to
true 50 dps via sympy's `subs(q, q_0_str_50dps).evalf(50)`.

The resulting witness is bit-identical at 50 dps to what the Rust
kernel `pyhecke_native.chi_lambda_braid_mpfr` would have produced
had its q_str input been correct, but doesn't require the Rust
extension (which is unavailable in many environments) and covers
n=12 (which the Rust kernel times out on at >45 min wall).

Output: `y-lambda-mpfr-witness.json` (replaces the f64-truncated
witness in place; consumed by `tr_m_wenzl_bridge_mpfr.py`).
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))


from _precision import set_compute_dps, fmt  # noqa: E402
from q_parameter import Q_MP  # noqa: E402
from y_lambda_wenzl_bridge import y_lambda_wenzl_bridge_numeric  # noqa: E402

set_compute_dps()

SOURCE = HERE / "y-lambda-wenzl-bridge-symbolic-witness.json"

# One cache per q0 LAYER, never one shared between them.
#
# Before this split there was a single `y-lambda-mpfr-witness.json` holding the
# muon (ideal) evaluation, while THIS producer defaulted to `Q_MP` — proton. So
# running it rewrote the ideal-layer cache with experimental-layer numbers, in
# place, under the same filename: the layer straddle AGENTS.md §"q₀ anchor
# convention" forbids, installed at the base of the chain. Measured live — the
# rewrite moved 295 fields with 12 anchor flips, and `atomic_tr_m_mpfr_50dps`
# (an `ideal_muon` producer) then moved 49 fields reading it.
#
# The ideal cache keeps the legacy filename so the existing consumers and
# `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_DEFAULT` stay unbroken.
OUTPUT_BY_ANCHOR = {
    "ideal": HERE / "y-lambda-mpfr-witness.json",
    "proton": HERE / "y-lambda-mpfr-proton-witness.json",
}
Q_PINNING = HERE / "q-pinning-50-digit.witness.json"


def q0_for(anchor: str) -> str:
    """The 50-dps q₀ string for one layer. Never guesses, never falls back.

    `proton` is `q_parameter.Q_MP` — the experimental pin the 2026-08-07 owner
    directive makes the default for new compute.

    `ideal` is read from `q-pinning-50-digit.witness.json`, which `q_parameter`
    itself treats as the canonical muon source (`_MUON_Q_STR`): it matches
    neither the proton Newton solve nor the `q_muon_at()` closed form, so it
    has to be read rather than recomputed.
    """
    if anchor == "proton":
        return mp.nstr(Q_MP, 50, strip_zeros=False)
    if anchor == "ideal":
        q = json.loads(Q_PINNING.read_text())["derived_50_digit"]["q"]
        return mp.nstr(mp.mpf(q), 50, strip_zeros=False)
    raise SystemExit(f"unknown anchor {anchor!r}: expected 'proton' or 'ideal'")


def evaluate_y_at_q0(partition, q0_str_50dps: str) -> str:
    """Evaluate y_λ at q_0 to 50 dps, from the LIVE formula.

    Returns the value as a 50-dp decimal string (mpf-roundtrip safe).

    CONVENTION (2026-08-10, bean `qou-eea0` / `qou-toi3`).  This took the
    `y_lambda_symbolic` string from
    `y-lambda-wenzl-bridge-symbolic-witness.json` and `sp.sympify`'d it.
    That witness is convention C — its entries carry `sqrt(q)` / `q**(3/2)`,
    the half-argument variable of `z = 1/(q^{1/2}+q^{-1/2})`, which D never
    produces because D stays inside ℚ(q).

    `y_lambda_wenzl_bridge` guards that cache (`_cached_symbolic_agrees`,
    bean `qou-wgta` item 3), but the guard is on the module's symbolic entry
    point and this script opened the JSON itself — so the guard never ran.
    Four scripts shared that shape; this is one of them.

    Takes the number from the module's numeric entry point instead, which is
    convention D.  Anchor-neutral: q₀ still arrives from the caller, so
    `--anchor proton` / `--anchor ideal` keep writing their own caches.
    """
    with mp.workdps(mp.mp.dps):
        val = y_lambda_wenzl_bridge_numeric(
            list(partition), mp.mpf(q0_str_50dps), dps=mp.mp.dps
        )
    return mp.nstr(val, mp.mp.dps, strip_zeros=False)


def run_anchor(anchor: str) -> int:
    OUTPUT = OUTPUT_BY_ANCHOR[anchor]

    print("=" * 96)
    print(f"  Regenerate {OUTPUT.name} at TRUE 50 dps  [anchor={anchor}]")
    print("  Source: y-lambda-wenzl-bridge-symbolic-witness.json (exact symbolic)")
    print("=" * 96)

    q0_str = q0_for(anchor)
    print(f"\n  q_0 (50 dps) = {q0_str}")

    sym = json.loads(SOURCE.read_text())
    sym_tables = sym["tables_by_n"]
    ns = sorted(int(k) for k in sym_tables.keys())
    print(f"  Source has tables for n in: {ns}")

    out_tables: dict = {}
    for n in ns:
        n_str = str(n)
        src = sym_tables[n_str]
        weights = src["weights"]
        print(f"  Evaluating n={n}: {len(weights)} partitions ...", flush=True)
        # Markov parameter at 50 dps, convention D: z = q^3 / (q^2 + 1).
        #
        # Was `1 / (sqrt(q) + 1/sqrt(q))` — convention C — emitted verbatim
        # into the witness's `z` field. The producer audit reports this file
        # clean because it looks for C in the *y_λ* computation; this is a
        # separate scalar written beside it. D needs no `mp.sqrt`, which is
        # the same portability tell the migration found from the other side:
        # C must reach for a square root, D never leaves ℚ(q).
        #
        # z_D is not a choice. `qou-u2jg` proves in Lean (sorry-free,
        # QOU/QBeta/TemperleyLiebTower.lean §ConventionPinning) that the three
        # Markov normalisations on H_3(q) force
        #     y_(1^3) · (q²+1)(q⁴+q²+1) = q² (z − q) (z(q²+1) − q³)
        # so the three-strand antisymmetriser dies at exactly two values of z;
        # z = q collapses to the one-dimensional character, leaving
        # z_D = q³/(q²+1) as the unique non-trivial Markov trace whose radical
        # contains it. C's z is neither root — which is precisely why it carried
        # y_(1^3) = 0.0227449 instead of zero.
        q = mp.mpf(q0_str)
        z = q ** 3 / (q ** 2 + 1)

        out_weights = []
        for w in weights:
            lam = w["partition"]
            # partition only — the y_lambda_symbolic beside it is
            # convention C and is deliberately not read (see above).
            y_str = evaluate_y_at_q0(lam, q0_str)
            out_weights.append({
                "partition": lam,
                "depth": max(0, len(lam) - 1),
                "y_lambda": y_str,
            })

        out_tables[n_str] = {
            "n": n,
            "num_partitions": len(weights),
            "q": q0_str,
            "z": mp.nstr(z, 50, strip_zeros=False),
            "dps": 50,
            "weights": out_weights,
        }

    # ── Emit witness ──────────────────────────────────────────────
    src_bytes = SOURCE.read_bytes()
    src_hash = "sha256:" + hashlib.sha256(src_bytes).hexdigest()
    script_hash = "sha256:" + hashlib.sha256(
        Path(__file__).read_bytes()
    ).hexdigest()

    out = {
        "computation": "y-lambda-mpfr-witness",
        "computedAt": datetime.now(timezone.utc).isoformat(),
        "description": (
            "y_λ values at H_n(R, q_0) evaluated to true 50 dps from "
            "the exact symbolic y_λ expressions in "
            "y-lambda-wenzl-bridge-symbolic-witness.json. Replaces the "
            "f64-truncated witness produced by "
            "_deprecated/y_lambda_mpfr_witness.py (line 152: "
            "q_str = str(Q0_FLOAT) truncates to 16 digits). The "
            "previous witness's claimed '50 dps' values matched true "
            "50 dps only to ~14 digits; this regeneration uses "
            "mp.nstr(Q_MP, 50) for q and sympy subs+evalf for each "
            "y_λ, giving full 50-dps precision."
        ),
        "engine": "sympy subs(q, q_0_50dps).evalf(50) over symbolic y_λ",
        "scriptFile": "regenerate_y_lambda_mpfr.py",
        "scriptHash": script_hash,
        "source_witness": "y-lambda-wenzl-bridge-symbolic-witness.json",
        "source_witness_hash": src_hash,
        "q_0_50dps": q0_str,
        # Self-declared layer. Without it a reader has to infer the pin by
        # string-matching the q0 prefix, which is how the two caches got
        # confused for one another in the first place.
        "q0Anchor": "proton" if anchor == "proton" else "muon",
        # Declared alongside the anchor, and it has to be declared HERE.
        #
        # `stamp_staleness_metadata` writes `q0Value` only inside
        # `if "q0Anchor" not in payload` (witness.py ~:1799). This producer
        # sets `q0Anchor` itself two lines up -- deliberately, see the NOTE
        # below -- so the stamper's whole block is skipped and the explicit
        # `q0_value=q0_str` handed to it is silently dropped. The result was a
        # cache carrying `q_0_50dps` with NO `q0Value` beside it.
        #
        # That is not the stamper being wrong: the 2026-08-24 change removed a
        # carry-forward that paired a fresh anchor label with the PREVIOUS
        # run's number, manufacturing exactly the Q0_FLIP the field exists to
        # catch. A producer that states its own anchor is therefore expected to
        # state its own value too. This does, from the same `q0_str` the whole
        # table was evaluated at, so label and number cannot disagree.
        "q0Value": q0_str,
        "q0Layer": ("experimental / Physical-Observations" if anchor == "proton"
                    else "ideal / canonical 3-CAL"),
        "dps": 50,
        "tables_by_n": out_tables,
        "audit_reference": "AUDIT-DEEP-2026-05.md §7; PR #564 convention/precision audit",
        "pr": "#564",
    }
    # NOTE: Cannot use WitnessBuilder.wrap_legacy().save() here
    # because the output filename is `y-lambda-mpfr-witness.json`
    # (without the standard `.witness.json` suffix), and consumers
    # (tr_m_wenzl_bridge_mpfr.py:53 _Y_LAMBDA_DEFAULT) read that
    # exact name. Use the public WitnessBuilder.stamp_staleness_metadata
    # helper to inject scriptHash/scriptCommitSha/commitSha/engine/
    # engineVersion/computedAt/durationMs in place, then write to
    # the legacy filename — keeps the consumer chain unbroken.
    from witness_base import WitnessBuilder
    out["auditOnly"] = "AUDIT-DEEP-2026-05.md"
    # `q0_anchor` MUST be passed explicitly. `stamp_staleness_metadata`
    # overwrites `payload["q0Anchor"]` UNCONDITIONALLY, and when the argument
    # is omitted it *infers* the anchor from the script path
    # (`resolve_q0_anchor(spath)`). A path can only name the producer, not
    # which of its two caches this invocation is writing — so the careful
    # per-anchor label set above was silently clobbered to "proton" for BOTH
    # anchors, leaving the ideal cache self-contradictory:
    #
    #     q_0_50dps  1.10997859555733471…   <- the muon/ideal pin
    #     q0Layer    "ideal / canonical 3-CAL"
    #     q0Anchor   "proton"               <- wrong, and it is the field
    #                                          downstream tooling selects on
    #
    # Caught by Copilot review on PR #4928. This is the layer-straddle hazard
    # of AGENTS.md §"q₀ anchor convention" appearing in the witness tooling
    # itself: the numeric q₀ was right the whole time, only the label lied,
    # which is the harder version to notice.
    WitnessBuilder.stamp_staleness_metadata(
        out, script_path=__file__, engine="python+mpmath",
        engine_version=f"sympy {sp.__version__} + mpmath {mp.__version__}",
        q0_anchor=out["q0Anchor"], q0_value=q0_str,
    )
    OUTPUT.write_text(json.dumps(out, indent=2) + "\n")
    print(f"\n  Wrote {OUTPUT.name} ({OUTPUT.stat().st_size} bytes).")
    print(f"  tables_by_n keys: {sorted(out_tables.keys(), key=int)}")
    print("=" * 96)
    return 0


def main() -> int:
    """Both anchors by default.

    This defaulted to `proton` alone, which is a *coverage* defect rather than
    an anchor one: the producer owns two caches, wrote one, and exited 0. The
    convention-C regeneration harness reads that exit code as "this producer's
    witnesses are now migrated", so `y-lambda-mpfr-witness.json` (the ideal
    cache, and the one `tr_m_wenzl_bridge_mpfr._Y_LAMBDA_DEFAULT` reads) stayed
    convention C through a full pass while the run reported success. Two
    producers had this shape; the other was `chi_at_q0_via_hoefsmit_mpfr`,
    which owns six atoms and default-ran two.

    Defaulting to both keeps the 2026-08-07 owner directive intact — each layer
    still writes only its OWN cache, so neither anchor's numbers ever land in
    the other's file, and `--anchor proton` / `--anchor ideal` still select one.
    """
    import argparse
    ap = argparse.ArgumentParser(description=main.__doc__)
    ap.add_argument("--anchor", choices=("proton", "ideal", "both"),
                    default="both",
                    help="q0 layer(s) to evaluate at. Default BOTH: each layer "
                         "writes its own cache, so running one and exiting 0 "
                         "left the other silently un-migrated.")
    a = ap.parse_args()
    anchors = ("proton", "ideal") if a.anchor == "both" else (a.anchor,)
    for anchor in anchors:
        rc = run_anchor(anchor)
        if rc != 0:
            return rc
    return 0


if __name__ == "__main__":
    sys.exit(main())
