#!/usr/bin/env python3
"""Canonical-binding residual Δ_λ(K) — tabulation + q₀-exponent structure.

EXPLORATORY / NEAR-MATCH TIER (per the c_k tiering discipline: this is an
observation of structure in the canonical residual, NOT a wired closure and
NOT a fit ansatz — nothing here feeds production).

Per the trace-convention reconciliation (docs/audits/
2026-06-09-binding-trace-convention-split.md, PR #2082): the trace-canonical
binding path is `binding_canonical.py`

    B_pred(Z,N) = E_0 · ( tr_M(W_free) − tr_M(W_atom) )

on the Jones–Markov trace `markov/markov_trace_canonical.tr_M_element`
(`prop:categorical-mass-markov`, markov-axioms-primitive). This probe reads
its witness and tabulates the per-nucleus residual

    Δ_λ(K) = B_AME / B_pred(K)

and its q₀-logarithm.

🛑 REFUTED ON THE CANONICAL WORD (2026-10-10, bean `qou-zf9n`). The "finding"
below was measured on the pre-2026-09-05 GROUPED atom word. On the canonical
BORROMEAN word the deuteron exponent is ~28.39, not ~15, and the family is not
within half a unit of 10A−5 anywhere. Kept for provenance; the assertions are
left at their original tolerances and now record the failure.

Former finding (grouped word): the exponent is a near-integer family

    log_{q₀} Δ_λ(K) ≈ 10·A − 5          (= 5(2A−1))

      D    14.99   vs 15   (δ = −0.01 — essentially exact)
      T    24.93   vs 25   (δ = −0.07)
      ³He  23.60   vs 25   (δ = −1.40 — Z-dependent deviation)
      ⁴He  35.27   vs 35   (δ = +0.27)

i.e. B_AME ≈ B_canonical · q₀^(10A−5+δ), |δ| ≤ 1.4 with δ ≈ 0 on the
N≥Z isotopes. The per-nucleon increment is exactly 10 in q₀-exponent
units. Whether 10A−5 has a categorical derivation (crossing-count /
jet-order / tower-depth bookkeeping of W_free vs W_atom) is the open
question this probe sharpens — that derivation, if it exists, IS the
canonical Δ_λ(K).

Output: delta-lambda-canonical-residual.witness.json
"""
from __future__ import annotations

import json
import sys
import time
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "substrate"))
sys.path.insert(0, str(HERE.parent / "tools" / "qou-substrate" / "python"))

from qou_substrate.witness import WitnessBuilder  # noqa: E402
from q_parameter import q_at  # noqa: E402
from _precision import set_compute_dps, fmt  # noqa: E402
import mpmath as mp  # noqa: E402

SRC = HERE / "binding-canonical.witness.json"


# The atoms, in the order `binding_canonical.__main__` tabulates them. AME
# values come from the SAME accessors that producer uses (mpf from the vendored
# decimal text, never a hand-typed float).
_ATOMS = (("D", 1, 1), ("T", 1, 2), ("3He", 2, 1), ("4He", 2, 2),
          ("6Li", 3, 3), ("7Li", 3, 4), ("7Be", 4, 3))

# Intra-nucleon word order the binding is evaluated on. Named, because this
# witness was a STALE CONSUMER for six weeks: its 2026-08-24 rows read
# `binding-canonical.witness.json` B_pred values computed on the pre-2026-09-05
# GROUPED word (D B_pred 0.4354 MeV), while that witness was regenerated on the
# BORROMEAN word on 2026-09-06 (D B_pred 0.1150 MeV) and nothing re-ran this
# one. Bean `qou-zf9n`; regenerated on owner approval 2026-10-10.
INTRA_ORDER = "borromean"


def _short(x, places: int):
    """Display-rounded numeric field, kept a JSON number because six
    consumers do arithmetic on it. Rounded IN mpf; the cast happens after."""
    r = mp.nint(x * 10 ** places) / 10 ** places
    return float(mp.nstr(r, 30))  # float64-ok: display-rounded field kept numeric for existing consumers


def _read(x):
    """A READ measurement (AME2020, 8-9 sig figs) as its shortest decimal, kept
    numeric because two consumers call repr()/str() on it then mpf. Not padded
    to 60 digits: that would manufacture digits the measurement does not have."""
    return float(mp.nstr(x, 15))  # float64-ok: verbatim read value, repr round-trips


def main() -> int:
    t0 = time.monotonic()
    # mpmath end to end, and B_pred is now computed LIVE rather than read from
    # binding-canonical.witness.json, whose B_MeV is stored as a JSON float
    # (float64 at source). The live route returns B as mpf = Q_beta * Delta_tr
    # with Delta_tr at 50 dps. The upstream witness is still read, but only to
    # CROSS-CHECK Delta_tr and to fail loudly if the two disagree -- which is
    # exactly the staleness that went unnoticed before.
    #
    # Precision ceiling, stated honestly: B_pred inherits Q_beta(n)'s 11
    # significant digits and B_AME its 8; the *_exact fields carry the
    # arithmetic, not those measurements' precision.
    set_compute_dps()
    import inspect
    from binding_canonical import binding_canonical
    from mass_at_3A_proper import atom_braid_word_3A
    from codata_constants import (
        AME_B_DEUTERON_MEV_VALIDATION, AME_B_TRITIUM_MEV_VALIDATION,
        AME_B_HE3_MEV_VALIDATION, AME_B_HE4_MEV_VALIDATION, ame_binding_mev,
    )
    default_order = inspect.signature(atom_braid_word_3A).parameters[
        "intra_order"].default
    if default_order != INTRA_ORDER:
        raise SystemExit(
            f"atom_braid_word_3A default intra_order is {default_order!r}, not "
            f"{INTRA_ORDER!r}; binding_canonical would evaluate a different word.")
    ame = {"D": AME_B_DEUTERON_MEV_VALIDATION, "T": AME_B_TRITIUM_MEV_VALIDATION,
           "3He": AME_B_HE3_MEV_VALIDATION, "4He": AME_B_HE4_MEV_VALIDATION}

    q0 = q_at(50)
    q0 = q0 if isinstance(q0, mp.mpf) else mp.mpf(str(q0))
    lnq = mp.log(q0)
    upstream = {r["atom"]: r for r in json.loads(SRC.read_text())["data"]["results"]}

    rows = []
    max_upstream_dtr = mp.mpf(0)
    for atom, Z, N in _ATOMS:
        A = Z + N
        res = binding_canonical(Z, N)
        if res.get("status") != "solved":
            raise SystemExit(f"binding_canonical({Z},{N}) -> {res.get('status')}")
        B_pred = mp.mpf(res["B_MeV"])
        dtr = mp.mpf(res["delta_tr_exact"])
        if atom in upstream:
            gap = abs(dtr - mp.mpf(upstream[atom]["delta_tr_exact"]))
            max_upstream_dtr = max(max_upstream_dtr, gap)
        B_ame = mp.mpf(ame[atom]) if atom in ame else mp.mpf(ame_binding_mev(Z, A))
        delta = B_ame / B_pred
        x = mp.log(delta) / lnq
        law = 10 * A - 5
        rows.append({
            "atom": atom, "Z": Z, "N": N, "A": A,
            "B_AME_MeV": _read(B_ame),
            "B_pred_canonical_MeV": fmt(B_pred),
            "delta_tr_exact": fmt(dtr),
            "Delta_lambda": _short(delta, 4),
            "log_q0_Delta": _short(x, 3),
            "law_10A_minus_5": law,
            "deviation_from_law": _short(x - law, 3),
            "Delta_lambda_exact": fmt(delta),
            "log_q0_Delta_exact": fmt(x),
            "deviation_from_law_exact": fmt(x - law),
        })
        print(f"  {atom:>4}: B_pred={mp.nstr(B_pred, 12)} MeV  "
              f"log_q0 Delta={mp.nstr(x, 8)}  ({time.monotonic()-t0:.1f}s)",
              flush=True)

    if max_upstream_dtr > mp.mpf("1e-40"):
        raise SystemExit(
            f"live Delta_tr disagrees with binding-canonical.witness.json by "
            f"{mp.nstr(max_upstream_dtr, 6)} -- regenerate that witness first.")

    # Deviations in mpf from the *_exact fields, not from the display-rounded
    # numbers. The N>=Z family is the one the assertion's own source text names
    # -- D, T, 4He -- not every N>=Z row (6Li/7Li were appended later and made
    # the old assertion fail for a reason unrelated to the claim it states).
    dev = {r["atom"]: abs(mp.mpf(r["deviation_from_law_exact"])) for r in rows}
    devs = list(dev.values())
    devs_ngez = [dev[a] for a in ("D", "T", "4He")]

    w = WitnessBuilder("delta-lambda-canonical-residual", engine="python",
                       start_time=t0)
    w.set_description(
        "Canonical-binding residual Δ_λ(K)=B_AME/B_pred on the Jones–Markov "
        "trace-canonical path (binding_canonical.py), evaluated LIVE on the "
        "BORROMEAN (interleaved) atom word. The former NEAR-MATCH 'log_q0 Δ_λ ≈ "
        "10A−5' was read off the pre-2026-09-05 GROUPED word and does NOT "
        "survive the canonical word: see the assertions and law.deviations. "
        "NOT wired; nothing here feeds production."
    )
    w.add_data("q0", fmt(q0))
    w.add_data("q0_exact", fmt(q0))
    w.add_data("intra_order", INTRA_ORDER)
    w.add_data("upstream_delta_tr_max_abs_gap", fmt(max_upstream_dtr))
    w.add_data("precision_note", (
        "Computed in mpmath end to end; B_pred is computed live (mpf, 50-dps "
        "Delta_tr) rather than read from binding-canonical.witness.json's "
        "float64 B_MeV, which is used only as a cross-check of Delta_tr. The "
        "rounded row fields are display values kept numeric for consumers; "
        "*_exact carry the arithmetic. Measurement precision is bounded by "
        "Q_beta(n) (11 sig figs) and AME2020 (8 sig figs), not by the arithmetic."
    ))
    w.add_data("trace_convention",
               "Jones–Markov (markov/markov_trace_canonical.tr_M_element; "
               "prop:categorical-mass-markov)")
    w.add_data("binding_path",
               "B_pred = Q_β(n) · (tr_M(W_free) − tr_M(W_atom)) — binding_canonical.py "
               "(the parameter was once misnamed E_0; see that file's docstring)")
    w.add_data("rows", rows)
    w.add_data("law", {
        "candidate": "Delta_lambda(K) ≈ q0^(10A−5)",
        "equivalently": "B_AME ≈ B_canonical · q0^(5(2A−1))",
        "tier": "near-match (c_k tiering discipline) — observation, NOT wired",
        "max_abs_deviation_all": fmt(max(devs)),
        "max_abs_deviation_D_T_4He": fmt(max(devs_ngez)),
        "status": (
            "REFUTED on the canonical (borromean) word — the near-match was a "
            "property of the retired grouped word. The assertions below are "
            "left at their original tolerances and FAIL; they are not widened."
        ),
    })
    w.add_assertion(
        name="deuteron_exponent_matches_15",
        computed=fmt(dev["D"]),
        expected="0", tolerance="0.05",
        source="log_q0(B_AME/B_pred) for the deuteron vs 10·2−5 = 15",
    )
    w.add_assertion(
        name="N_ge_Z_family_within_half_unit",
        computed=fmt(max(devs_ngez)), expected="0", tolerance="0.5",
        source="max |log_q0 Δ_λ − (10A−5)| over D, T, ⁴He",
    )

    out = w.save()
    print(f"{'atom':>5} {'A':>2} {'Δ_λ':>9} {'log_q0':>8} {'10A−5':>6} {'dev':>6}")
    for r in rows:
        print(f"{r['atom']:>5} {r['A']:>2} {r['Delta_lambda']:>9.3f} "
              f"{r['log_q0_Delta']:>8.2f} {r['law_10A_minus_5']:>6} "
              f"{r['deviation_from_law']:>+6.2f}")
    print("10A−5 near-match: see assertions (borromean word) — not wired.")
    print(f"Witness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
