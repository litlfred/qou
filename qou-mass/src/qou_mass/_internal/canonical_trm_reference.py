#!/usr/bin/env python3
"""|tr_M| for the nucleons, read from the witness built at THIS RUN'S pin.

WHY THIS EXISTS.  Fifteen files hardcoded `mp.mpf("1.0653062286131670…")` as
the proton's Markov trace. That number is **convention C** — proved to 50
digits by `audits/he4_witness_convention_attribution_probe.py` — and convention
D has been canonical since the owner ruling of 2026-08-15. The D value is
`1.14575969245730086968…` at the proton pin, so every one of those sites was
**7.55 %** out.

Seven of them were not comparing against it, they were multiplying by it:

    pred_0 = tr_M * plancherel_ratio * vol_over_hsq      # habiro_h9_*
    S      = hab_sum / pred_0                            # => 7.552 % high

WHY NOT JUST SUBSTITUTE THE D LITERAL.  Because that is how the corpus got
here. A hardcoded D constant is stale the moment the anchor or the convention
moves again, and it carries no way for a reader to tell which frame it is in.
Worse, the previous migration could not have caught it: `.work/convention-c-regen*.jsonl`
logs `markov_weights_symbolic.py` as **`ok`, 5.2 s** and its C constant is
still there today, because re-running a producer cannot change a literal. A
regeneration sweep is the wrong instrument for this class and reports success
against it.

So: read the value, at the pin the caller is actually running at.

TWO PINS, SELECTED BY THE ARTIFACT'S OWN STAMP.  `atomic-tr-m-mpfr-50dps.witness.json`
is muon-built and `…-proton.witness.json` is proton-built; this picks whichever
records the q₀ that `q_parameter` resolves for the *running producer's stem*,
and raises if neither does. Same shape as the fixes in
`y_lambda_symbolic_validate.load_mpfr_witness` and
`atomic_tr_m_helium4._pick_witness_for_pin` (bean qou-y313) — reconciling
against the recorded stamp rather than trusting a filename.

STRAND COUNT IS NOT A PARAMETER, AND THAT IS NOT AN OVERSIGHT.  The Markov
trace is invariant under stabilisation, so tr_M of the proton braid is the same
computed in H₃ or H₉. The habiro/ callers say "H₉" and the witness rows are
built at 3A strands; both are the same number, and a caller does not need to
say which.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE))

import mpmath as mp                                        # noqa: E402

#: Proton-built first only as a hint; the recorded q₀ decides.
_WITNESSES = ("atomic-tr-m-mpfr-50dps-proton.witness.json",
              "atomic-tr-m-mpfr-50dps.witness.json")

_CACHE: dict[str, mp.mpf] = {}


def _rows_for_pin() -> dict[str, dict]:
    from q_parameter import Q_50_DIGIT_STR                  # noqa: PLC0415
    want = mp.mpf(Q_50_DIGIT_STR)
    seen = []
    for name in _WITNESSES:
        p = _HERE / name
        if not p.exists():
            continue
        d = json.loads(p.read_text())
        w = d.get("witness", d)
        q_rec = ((w.get("parameters") or {}).get("q_0") or w.get("q_0")
                 or d.get("q_0_50dps") or w.get("q_0_50dps"))
        seen.append((name, str(q_rec)[:26]))
        if q_rec is not None and abs(mp.mpf(str(q_rec)) - want) < mp.mpf("1e-40"):
            return {r["atom"]: r
                    for r in (w.get("results") or d.get("results") or [])}
    raise FileNotFoundError(
        f"no |tr_M| witness recorded at this run's pin "
        f"{str(Q_50_DIGIT_STR)[:26]}…; inspected {seen}. Regenerate "
        f"atomic_tr_m_mpfr_50dps.py at this anchor rather than reading the "
        f"other layer — a silent cross-layer read is the defect this avoids."
    )


def tr_m_nucleon(atom: str) -> mp.mpf:
    """|tr_M(atom)| at the running producer's pin, convention D.

    `atom` is `"proton"` or `"neutron"`. Raises rather than falling back to the
    other pin: a 78 ppb cross-layer error that reads as a successful load is
    worse than a stack trace.
    """
    if atom not in _CACHE:
        rows = _rows_for_pin()
        if atom not in rows:
            raise KeyError(f"{atom!r} not in the |tr_M| witness; have "
                           f"{sorted(rows)}")
        _CACHE[atom] = abs(mp.mpf(rows[atom]["tr_M_at_q0_50dps"]))
    return _CACHE[atom]


def tr_m_proton() -> mp.mpf:
    """Convenience alias — the value 15 files used to hardcode."""
    return tr_m_nucleon("proton")


def tr_m_neutron() -> mp.mpf:
    return tr_m_nucleon("neutron")


if __name__ == "__main__":
    mp.mp.dps = 50
    for a in ("proton", "neutron"):
        print(f"  {a:8} {tr_m_nucleon(a)}")
