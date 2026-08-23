#!/usr/bin/env python3
"""Door-v bar-parity GUARDRAIL — a producer-side STRUCTURAL CONFIRMATION check.

Bean: qou-fawf.  Branch: claude/qlift-borel-kernel-derivation-2026-07-20.

WHAT THIS IS (and is NOT).
--------------------------
This is a *guardrail*, analogous to the canonical-mass guardrail
(docs/canonical-mass-formula-guardrail.md): it asserts a STRUCTURAL FACT and
would FLAG any future compute that violates it.  It adds NO new physical number:
no AME data, no fit, no q0-derived prediction.  It verifies the *parity
relationship* on model bar-even / bar-odd objects and exposes a check that any
downstream producer can call before it tries to route a decay observable
through the binding kernel.

THE STRUCTURAL FACT (Lean-proved).
----------------------------------
The framework's bar involution (q -> q^{-1}) splits every q-difference observable
into a bar-EVEN (cosh) sector and a bar-ODD (sinh) sector:

    mass / binding   =  bar-EVEN  =  cosh  =  C1 kernel  =  NON-NEGATIVE cone
                        (sum of real squares f+^2, f-^2 ; provably >= 0)

    Q_beta / decay   =  bar-ODD   =  sinh  =  GGM / eq-49 =  (-1)^m ALTERNATING
                        (growing GGM solution: y_{m+1} ~ -q^m y_m ; genuine flip)

Door-v (docs/audits/2026-07-20-qlift-doorV-stokes.md) isolated the SOLE residual
between GGM and the C1 tensor-square {+1,-1} realization as EXACTLY this diagonal
Z/2 (-1)^m character: slopes and theta magnitudes match, the unipotent Stokes
bridge is trivial (U -> I), only the bar-parity SIGN separates them.

QOU.Mass.DoorVParityNoIdentity (compiled, sorry-free) upgrades this to a
scope-(b) STRUCTURAL EXCLUSION:

  * nonneg_not_signalternating : a pointwise non-negative sequence never has a
    consecutive sign flip  (0 <= s n * s (n+1)).
  * posCone_nonneg            : a non-negative-coefficient (parity-preserving)
    combination of non-negative sequences is itself non-negative.
  * doorV_parity_no_identity  : therefore NO non-negative-cone combination of the
    bar-even squares can equal the sign-alternating bar-odd target.

THE PARITY WALL (the guardrail's assertion).
--------------------------------------------
A bar-EVEN (mass/binding) quantity and a bar-ODD (Q_beta/decay) quantity have
OPPOSITE (-1)^m parity.  Any map that PRESERVES parity (in particular any
gauge / rational / "non-negative-cone" transform of a bar-even object, which
stays in the non-negative cone) CANNOT produce a bar-odd observable.  So:

    decay observables MUST NOT be derived from binding by any parity-crossing
    (or, equivalently, parity-*preserving*-of-the-even-object) transform.

This mirrors the KL-positivity prune
(docs/audits/2026-06-16-option-e-probe4-kl-positivity-prune.md): a manifestly
non-negative construction cannot supply a mixed-sign target.

Ref: docs/audits/2026-07-20-qlift-doorV-stokes.md
Ref: docs/audits/2026-07-20-sinhcosh-scale-impact-analysis.md
Ref: content/.../lean/QOU/Mass/DoorVParityNoIdentity.lean
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from typing import Sequence

from mpmath import mp, mpf
import _path_bridge  # noqa: F401, E402 — flat-namespace bridge
from _precision import set_compute_dps  # noqa: E402

set_compute_dps()

# --------------------------------------------------------------------------- #
# Model bar-even / bar-odd corpus objects.
#
# These are STRUCTURAL MODELS of the framework's two sectors, not physical
# predictions.  We sample at several generic q (NOT a q0 pin, NOT a mass value)
# purely to exhibit that the parity structure is q-independent.
# --------------------------------------------------------------------------- #

# The three q used in the Door-v probe (structural sample, not a prediction).
Q_SAMPLES = [mpf("0.9"), mpf("1.05"), mpf("1.10998")]


def bar_even_squares(q: mpf, n: int) -> tuple[list[mpf], list[mpf]]:
    """The bar-EVEN (cosh / mass-binding) sector: the two tensor-square
    solutions f+^2, f-^2 of the C1 kernel.  A real square is >= 0, so both are
    pointwise NON-NEGATIVE — the defining feature of the bar-even sector.

    We build f+ ~ q^{+m^2/4}, f- ~ q^{-m^2/4} up to sign (the Door-iv carriers)
    and square them.  No AME / q0 / mass number enters; this is the *shape*."""
    p = []  # f+^2
    r = []  # f-^2
    for m in range(n):
        fp = q ** (mpf(m * m) / 4)      # growing carrier (any real)
        fm = q ** (-mpf(m * m) / 4)     # decaying carrier (any real)
        p.append(fp * fp)               # square >= 0  (bar-even)
        r.append(fm * fm)               # square >= 0  (bar-even)
    return p, r


def bar_odd_ggm(q: mpf, n: int) -> list[mpf]:
    """The bar-ODD (sinh / Q_beta-decay) sector: the growing GGM/eq-49 solution,
    which carries the (-1)^m sign character (y_{m+1} ~ -q^m y_m).  We model its
    genuine alternation directly: y_m = (-1)^m * (positive magnitude).  The
    magnitude shape is irrelevant to the parity fact; only the sign flip is."""
    y = []
    for m in range(n):
        mag = q ** (mpf(m * m) / 2)     # any positive magnitude
        y.append(((-1) ** m) * mag)     # genuine (-1)^m alternation (bar-odd)
    return y


# --------------------------------------------------------------------------- #
# The parity primitives (numerical mirror of the compiled Lean theorems).
# --------------------------------------------------------------------------- #

def has_consecutive_flip(s: Sequence[mpf]) -> bool:
    """True iff some consecutive pair flips sign (s_m * s_{m+1} < 0).
    Mirror of Lean `nonneg_not_signalternating`: a non-negative sequence returns
    False (no flip); a genuine (-1)^m sequence returns True."""
    return any(s[m] * s[m + 1] < 0 for m in range(len(s) - 1))


def is_nonneg_cone(s: Sequence[mpf], tol: mpf = mpf("1e-40")) -> bool:
    """True iff the sequence is pointwise non-negative (lives in the bar-even
    positive cone).  Mirror of the `0 <= s n` hypothesis."""
    return all(x >= -tol for x in s)


def bar_parity_label(s: Sequence[mpf]) -> str:
    """Classify a sequence by its observed bar-parity signature."""
    flip = has_consecutive_flip(s)
    nonneg = is_nonneg_cone(s)
    if nonneg and not flip:
        return "bar-even"   # cosh / mass-binding cone
    if flip:
        return "bar-odd"    # sinh / Q_beta-decay alternation
    return "indeterminate"


# --------------------------------------------------------------------------- #
# THE GUARDRAIL.
# --------------------------------------------------------------------------- #

def check_parity_derivable(
    bar_even_seqs: Sequence[Sequence[mpf]],
    bar_odd_seq: Sequence[mpf],
) -> dict:
    """GUARDRAIL entry point for downstream producers.

    Given one or more bar-EVEN (mass/binding) source sequences and a claimed
    bar-ODD (Q_beta/decay) *target*, assert that NO parity-preserving
    (non-negative-cone) combination of the sources can equal the target.

    Returns a dict with `violation: bool`.  `violation=True` means a downstream
    compute is trying to derive a bar-odd observable from bar-even objects by a
    parity-preserving map — which the compiled parity wall forbids.  A producer
    should REFUSE to wire such a derivation.

    This is a STRUCTURAL check: it reads only the SIGN structure of the
    sequences, not any physical magnitude.  No fit, no data.
    """
    sources_even = all(is_nonneg_cone(s) for s in bar_even_seqs)
    target_flips = has_consecutive_flip(bar_odd_seq)

    # Locate a witness flip in the target (the (-1)^m character).
    flip_index = next(
        (m for m in range(len(bar_odd_seq) - 1)
         if bar_odd_seq[m] * bar_odd_seq[m + 1] < 0),
        None,
    )

    # A parity-preserving (non-negative-cone) combination of non-negative
    # sources is non-negative everywhere (posCone_nonneg), hence has NO flip;
    # a genuinely flipping target therefore cannot be reproduced.
    derivable_by_parity_preserving_map = sources_even and not target_flips

    # A "violation" = someone asserts the target IS so derivable while it flips.
    violation = sources_even and target_flips and flip_index is not None

    return {
        "sources_all_bar_even": sources_even,
        "target_is_bar_odd": target_flips,
        "target_first_flip_index": flip_index,
        "derivable_by_parity_preserving_map": derivable_by_parity_preserving_map,
        "violation": violation,
        "rule": (
            "A parity-preserving (non-negative-cone) map from bar-even "
            "(mass/binding) sources stays non-negative and cannot produce a "
            "(-1)^m sign-alternating bar-odd (Q_beta/decay) target. "
            "Lean: QOU.Mass.DoorVParityNoIdentity.doorV_parity_no_identity."
        ),
    }


def run() -> dict:
    """Verify the parity wall on the model bar-even / bar-odd corpus objects at
    each q sample, and self-test the guardrail's flagging."""
    n = 24
    per_q = []
    all_ok = True
    for q in Q_SAMPLES:
        p, r = bar_even_squares(q, n)
        y = bar_odd_ggm(q, n)

        p_label = bar_parity_label(p)
        r_label = bar_parity_label(r)
        y_label = bar_parity_label(y)

        # The parity wall: guardrail must FLAG deriving y (bar-odd) from
        # {p, r} (bar-even) by a parity-preserving map.
        guard = check_parity_derivable([p, r], y)

        # Sanity: opposite parity, and the guardrail fires (violation=True).
        opposite_parity = (
            p_label == "bar-even" and r_label == "bar-even"
            and y_label == "bar-odd"
        )
        wall_holds = opposite_parity and guard["violation"] is True

        # Negative control: a bar-even target IS derivable (no flag).
        control = check_parity_derivable([p, r], p)
        control_ok = control["violation"] is False

        ok = wall_holds and control_ok
        all_ok = all_ok and ok
        per_q.append({
            "q": str(q),
            "bar_even_fplus_sq": p_label,
            "bar_even_fminus_sq": r_label,
            "bar_odd_ggm": y_label,
            "opposite_parity": opposite_parity,
            "guardrail_flags_derivation": guard["violation"],
            "negative_control_no_flag": control_ok,
            "wall_holds": ok,
        })

    return {
        "structural_confirmation": all_ok,
        "per_q": per_q,
        "assertion": (
            "mass/binding is bar-EVEN (cosh, non-negative cone); Q_beta/decay is "
            "bar-ODD (sinh, (-1)^m alternating); they have OPPOSITE (-1)^m parity "
            "and cannot be gauge/transform-related by any parity-preserving map. "
            "Decay observables must NOT be derived from the binding kernel."
        ),
    }


def build_witness(result: dict) -> dict:
    return {
        "description": (
            "Door-v bar-parity GUARDRAIL: STRUCTURAL CONFIRMATION that a "
            "bar-even (mass/binding, cosh, non-negative-cone) quantity and a "
            "bar-odd (Q_beta/decay, sinh, (-1)^m alternating) quantity have "
            "OPPOSITE (-1)^m parity and cannot be gauge/transform-related. "
            "Verifies the parity relationship on model bar-even/bar-odd corpus "
            "objects and exposes check_parity_derivable() to FLAG any future "
            "compute that tries to derive a bar-odd observable from a bar-even "
            "one by a parity-preserving map. Adds NO new physical number."
        ),
        "computation": (
            "mpmath dps=50; bar-even sector = tensor-square carriers f+^2, f-^2 "
            "(real squares, pointwise >= 0) of the C1 kernel; bar-odd sector = "
            "growing GGM/eq-49 solution modelled by its (-1)^m sign character. "
            "Checks: (i) both squares classify bar-even (no consecutive flip); "
            "(ii) GGM classifies bar-odd (genuine flip); (iii) guardrail "
            "check_parity_derivable([f+^2,f-^2], GGM) returns violation=True "
            "(parity wall fires); (iv) negative control (bar-even target) "
            "returns violation=False. Sampled at q in {0.9,1.05,1.10998} to show "
            "q-independence. SIGN structure only — no magnitude, no fit, no data."
        ),
        "generated": datetime.now(timezone.utc).isoformat(),
        "framing": "structural-confirmation",
        "adds_new_number": False,
        "parameters": {
            "dps": 50,
            "n_terms": 24,
            "q_samples": [str(q) for q in Q_SAMPLES],
            "sectors": {
                "bar_even": "mass / binding — cosh — C1 kernel — non-negative cone",
                "bar_odd": "Q_beta / decay — sinh — GGM/eq-49 — (-1)^m alternating",
            },
        },
        "results": result,
        "context": {
            "bean": "qou-fawf",
            "kind": "producer-side structural guardrail (no new physical number)",
            "audit_doc": "docs/audits/2026-07-20-doorv-guardrail.md",
            "builds_on": [
                "docs/audits/2026-07-20-qlift-doorV-stokes.md (the (-1)^m residual finding)",
                "docs/audits/2026-07-20-sinhcosh-scale-impact-analysis.md (impact: guard the decay compute)",
            ],
            "lean_backing": (
                "QOU.Mass.DoorVParityNoIdentity — doorV_parity_no_identity "
                "(sorry-free scope-(b) exclusion): no non-negative-cone "
                "combination of the bar-even squares equals a sign-alternating "
                "bar-odd target. Invariant = non-negativity of a real square "
                "(0 <= x^2), the same invariant as the KL-positivity prune."
            ),
            "discipline": (
                "STRUCTURAL CONFIRMATION only. No AME data, no fit, no q0-derived "
                "prediction. Verifies the parity relationship holds on model "
                "bar-even/bar-odd objects and would flag a parity-preserving "
                "bar-even -> bar-odd derivation. scope-(b) exclusion cites a "
                "proved invariant (real square >= 0)."
            ),
        },
    }


def main() -> None:
    result = run()
    witness = build_witness(result)
    out = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "doorv_barparity_guardrail.witness.json",
    )
    with open(out, "w") as fh:
        json.dump(witness, fh, indent=2)
        fh.write("\n")

    ok = result["structural_confirmation"]
    print(f"[doorv-barparity-guardrail] structural_confirmation = {ok}")
    for row in result["per_q"]:
        print(
            f"  q={row['q']:>8}: even={row['bar_even_fplus_sq']}/"
            f"{row['bar_even_fminus_sq']}  odd={row['bar_odd_ggm']}  "
            f"wall_holds={row['wall_holds']}"
        )
    print(f"[doorv-barparity-guardrail] wrote {out}")
    if not ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
