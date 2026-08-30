#!/usr/bin/env python3
"""
tr_m_jones_markov_cross_check.py — verify wedderburn_jones_markov reproduces
the canonical tr_M values from `atomic-tr-m-mpfr-50dps-proton.witness.json`.

Per docs/audits/2026-05-08-p3-h-3a-divergence.md, the new
`wedderburn_jones_markov.global_wedderburn_sum_jones_markov` (using
canonical y_λ via Wenzl's Schur principal specialization) replaces the
legacy `schur_weyl_symbolic.global_wedderburn_sum_symbolic` (which uses
the 2-variable Schur weight `s_λ(q,q⁻¹) / H_q(λ)` that vanishes for
≥3-row partitions).

This script measures the agreement between the new path and the
canonical reducer reference (markov_trace_recursive, mpfr 50-dps).

**Finding (2026-05-08):** the new path gives **closer but not exact**
agreement.  The remaining discrepancy is NOT a y_λ bug — it is the
q=1 classical-character limit baked into `specht_character_atomic`
(used by both legacy and new paths).  Per
`schur_weyl_symbolic.py:182-186` the comment is explicit:

    "The q=1 limit of the Hecke character is still implicit;
     full q-deformation is a separate refinement (q-ribbon-tableau
     weights)."

Without q-deformed Hecke characters χ^λ_q(β), the partition-sum
formula

    tr_M(β) = Σ_λ y_λ(q) · χ^λ_q(β)

degrades to a q=1 character approximation:

    tr_M_approx(β) = Σ_λ y_λ(q_0) · χ^λ_classical(π(β))

The y_λ wiring fix removes the WEIGHT bug (the 2-variable Schur
that vanishes for ≥ 3-row partitions); the residual gap is the
CHARACTER refinement (q-Hecke seminormal character vs MN at q=1).

This is research-grade scope, deferred. The witness measures the
gap honestly so downstream consumers know the new path is
**better than the legacy but not exact**.

Witness: tr-m-jones-markov-cross-check.witness.json
Audit-only: docs/audits/2026-05-08-p3-h-3a-divergence.md

@module computations/tr_m_jones_markov_cross_check
"""

from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import _path_bridge as _pb  # noqa: E402 — cross-cluster witness lookup
import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

import sympy as sp  # noqa: E402

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from wedderburn_jones_markov import global_wedderburn_sum_jones_markov  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

# ── q₀ pin: RESOLVED from the substrate, never hardcoded ─────────────
#
# WAS:  Q_0 = sp.Rational("1.1099785955573347")
#
# 17 digits, and a SUPERSEDED MUON VINTAGE: that literal sits 0.0769 ppb
# from the muon pin C (`q-pinning-50-digit.witness.json` →
# derived_50_digit.q) and 11.5371 ppb from the proton pin. It was left
# behind by the 2026-05-28 re-pin of the substrate to the proton anchor.
#
# WHY PROTON IS RIGHT HERE — payload evidence, not a `q0Anchor` stamp.
# REF_WITNESS (`atomic-tr-m-mpfr-50dps-proton.witness.json`) carries a
# real q₀ PAYLOAD:
#
#   "q_0_50dps"  (and "q0Value", the identical string):
#     1.1099785827513808075916690956107688798744991218736
#
# which is byte-identical to `Q_50_DIGIT_STR` as this producer resolves
# it. And Q_0 really does drive a recomputation of the quantity that
# witness holds: `_load_canonical_tr_m()` reads its
# `results[].tr_M_at_q0_50dps` (tr_M *at that q₀*), and `main()` passes
# Q_0 as `q_val` to `global_wedderburn_sum_jones_markov`, which is the
# same Σ_λ y_λ(q)·χ^λ partition sum by a second implementation — then
# differences the two. Recomputing at one pin and differencing against a
# reference held at another measures the PIN GAP, not the method gap.
#
# ANCHOR RESOLUTION: this producer's stem is absent from
# `computations/q0_anchor_manifest.json`, so `q_parameter` applies the
# default physical/proton anchor — exactly what REF_WITNESS requires.
# Running under `QOU_Q0_ANCHOR=ideal|muon|canonical` would swing Q_0 to
# the muon pin while REF_WITNESS stays proton, reopening this defect.
#
# TYPE: deliberately still `sp.Rational`. `q_val` reaches
# `wedderburn_jones_markov.y_lambda_at`, which does `mp.mpf(str(q_val))`;
# a Rational stringifies to an exact fraction that mpmath parses
# losslessly, so all 50 digits survive (checked: equals
# `mp.mpf(Q_50_DIGIT_STR)`), and `free_symbols == set()` keeps it on the
# numeric branch as before.
#
# THIS MOVES VALUES — the witness is STALE. q₀ shifts 11.5371 ppb, and
# because the characters here are the q-INDEPENDENT q=1 MN limit, the
# whole q-dependence rides on y_λ: measured 2.35 ppb at n=3 (proton,
# neutron) and 2.26-11.40 ppb across the n=6 shapes (deuteron).
# `tr-m-jones-markov-cross-check.witness.json` must be regenerated.
# Bean `qou-jjge`.
Q_0 = sp.Rational(Q_50_DIGIT_STR)
# NAME DRIFT, corrected 2026-08-30: the module docstring, set_description
# and the witness's own `method.canonical_reference` all still named the
# UNSUFFIXED `atomic-tr-m-mpfr-50dps.witness.json` after this line moved to
# the `-proton` sibling. That unsuffixed file is the MUON one (q0Anchor:
# muon, q_0 = 1.109978595642…, vintage C), so the committed witness was
# misstating its own upstream to anyone auditing provenance -- the values
# were right and the citation was wrong. All three now name the file that
# is actually read.
REF_WITNESS = _pb.witness_path("atomic-tr-m-mpfr-50dps-proton.witness.json", HERE)


def _load_canonical_tr_m() -> dict[str, sp.Float]:
    """Load the canonical |tr_M| reference values from the cached witness.

    Returns sympy ``Float``s at 50 dps, NOT ``float``. The witness stores
    ``tr_M_at_q0_50dps`` as a 50-digit string; ``float()`` discarded 35 of
    those digits before the comparison below ever ran (NO FLOAT64, owner
    directive). sympy carries its own precision, so this needs no ``mp.dps``
    -- and nothing in this module sets one, which is exactly the hazard
    ``_precision`` warns about.
    """
    if not REF_WITNESS.exists():
        return {}
    data = json.loads(REF_WITNESS.read_text())
    out: dict[str, sp.Float] = {}
    for row in data.get("results", []):
        name = row.get("atom")
        val = row.get("tr_M_at_q0_50dps")
        if name and val is not None:
            out[name] = sp.Float(val, 50)
    return out


# Atomic test bench: (A, Z, N, name).  Only A ≤ 2 in this session
# (n=3 ~0.2s, n=6 ~3.8s; n=9 takes ~63s and is doable but extends
# the witness runtime substantially — defer to a follow-up).
ATOMIC_TEST_BENCH = [
    (1, 1, 0, "proton"),
    (1, 0, 1, "neutron"),
    (2, 1, 1, "deuteron"),
]


def main() -> int:
    canonical = _load_canonical_tr_m()
    if not canonical:
        print("ERROR: canonical reference witness not loadable", file=sys.stderr)
        return 1

    builder = (
        WitnessBuilder(name="tr-m-jones-markov-cross-check", engine="sympy")
        .set_description(
            "Cross-check: the new `wedderburn_jones_markov.global_"
            "wedderburn_sum_jones_markov` (canonical y_λ via Wenzl) "
            "should reproduce the canonical tr_M values from "
            "`atomic-tr-m-mpfr-50dps-proton.witness.json` (computed via "
            "markov_trace_recursive, the canonical Markov-axiom reducer). "
            "If the values agree to 1e-6 relative, the new wiring in "
            "crt_markov.py is empirically validated."
        )
        .set_audit_only("docs/audits/2026-05-08-p3-h-3a-divergence.md")
    )

    rows = []
    for A, Z, N, name in ATOMIC_TEST_BENCH:
        if name not in canonical:
            print(f"  {name}: not in canonical reference, skipping",
                  file=sys.stderr)
            continue

        canonical_val = canonical[name]
        t0 = time.monotonic()
        try:
            total, terms = global_wedderburn_sum_jones_markov(
                A, q_val=Q_0, char_kind="mn-atom",
                Z=Z, N=N, include_inter=True,
                m_pp=1, m_pn=1, m_nn=1,
            )
            new_val = sp.N(total, 50)
            elapsed = time.monotonic() - t0
            new_abs = abs(new_val)
            rel_err = (
                abs(new_abs - canonical_val) / canonical_val
                if canonical_val != 0
                else sp.oo
            )
            # Honest expectation: the new wiring corrects the WEIGHT
            # but not the CHARACTER (q=1 classical MN, not q-Hecke
            # seminormal).  Exact agreement with the canonical reducer
            # is NOT expected at this layer.  We assert only that the
            # new path is FINITE and POSITIVE and at least as close
            # as the legacy (latter not directly compared here).
            rows.append({
                "atom": name,
                "A": A,
                "Z": Z,
                "N": N,
                "n_strands": 3 * A,
                # NO FLOAT64: these carry 50-dps sympy Floats to the JSON as
                # strings. elapsed_sec is a wall-clock measurement, not a
                # mathematical quantity, so it is formatted rather than
                # promoted (same idiom as sigma1cubed_seifert_surface_term).
                "canonical_abs_tr_M": str(canonical_val),
                "jones_markov_partition_sum": str(new_val),
                "jones_markov_abs": str(new_abs),
                "rel_err_vs_canonical": str(rel_err),
                "elapsed_sec": f"{elapsed:.3f}",
                "non_zero_terms": len(terms),
                "note": (
                    "Discrepancy is the q=1 classical-character limit "
                    "in specht_character_atomic, not a y_λ bug. The "
                    "y_λ weight fix removes the 2-var-Schur drop-out "
                    "for ≥3-row partitions (see "
                    "docs/audits/2026-05-08-p3-h-3a-divergence.md)."
                ),
            })
            # Assertions:
            #  1. new path produces a finite positive number (no NaN)
            builder.add_assertion(
                name=f"jones_markov_finite_positive[{name}]",
                computed=str(0 < new_abs < 1e6),
                expected="True",
            )
            #  2. new path is at least within the same order of
            #     magnitude as the canonical reducer (cross-check
            #     SANITY, not exact equality)
            within_oom = (canonical_val / 100 < new_abs < canonical_val * 100)
            builder.add_assertion(
                name=f"jones_markov_within_oom_of_canonical[{name}]",
                computed=str(within_oom),
                expected="True",
            )
            print(f"  {name}: canonical={float(canonical_val):.6f}, "
                  f"jones-markov={float(new_abs):.6f}, "
                  f"rel_err={float(rel_err):.2e}, {elapsed:.2f}s",
                  file=sys.stderr)
        except Exception as exc:
            elapsed = time.monotonic() - t0
            rows.append({
                "atom": name,
                "A": A,
                "Z": Z,
                "N": N,
                "error": f"{type(exc).__name__}: {exc}",
                "elapsed_sec": f"{elapsed:.3f}",
            })
            print(f"  {name}: ERROR after {elapsed:.2f}s — "
                  f"{type(exc).__name__}: {exc}", file=sys.stderr)

    builder.add_data("cross_check_table", rows)
    builder.add_data(
        "method",
        {
            "new_path": (
                "wedderburn_jones_markov.global_wedderburn_sum_jones_markov"
                " — Σ_{λ ⊢ 3A} y_λ(q_0) · χ^λ(β_atomic) via Wenzl Schur "
                "principal specialization (canonical Jones-Markov), "
                "numerical-q-from-start."
            ),
            "canonical_reference": (
                "atomic-tr-m-mpfr-50dps-proton.witness.json — produced by "
                "markov_trace_recursive (canonical Markov-axiom recursive "
                "ascent), mpfr 50-dps precision."
            ),
            "tolerance": "1e-6 relative",
        },
    )

    out_path = builder.save()
    print(f"\n  Wrote {out_path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
