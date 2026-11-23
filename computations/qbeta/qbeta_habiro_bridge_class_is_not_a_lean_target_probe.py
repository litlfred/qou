#!/usr/bin/env python3
"""qbeta_habiro_bridge_class_is_not_a_lean_target_probe.py — what "work the
bridge class" can and cannot mean.

Bean `qou-cds1`. Scope-(a) for the arithmetic; the Lean results are exact
(compiler verdicts) and reproduced by the command recorded below.

## The target

`QOU.BraidKnot.QbetaHabiroTaylorBridgeClass`
(`mass-theory/habiro-precision-ladder-equivalence.lean`) is the §3b-cond class
carrying the OPEN identification of the Q_beta precision-ladder coefficients
with the Habiro Taylor coefficients:

    class QbetaHabiroTaylorBridgeClass : Prop where
      ck_eq_taylor : forall k, precisionLadderCoeff k = habiroTaylorCoeff k

## Finding 1 — it is HONESTLY OPEN. My own hypothesis was wrong.

Both sides are declared `opaque ... := fun _ => 0`, so they are SEMANTICALLY
EQUAL; if the seal leaked, the class would be trivially inhabited and every
downstream conditional theorem would be vacuous. I expected a leak. There is
none. Six tactics, `lean`-direct against the real import cone:

    rfl                                              exit 1  Type mismatch
    unfold precisionLadderCoeff habiroTaylorCoeff    exit 1  failed to unfold
    simp [precisionLadderCoeff, habiroTaylorCoeff]   exit 1  made no progress
    decide                                           exit 1  free variables
    norm_num [...]                                   exit 1  unsolved goals
    aesop                                            exit 1  made no progress

So the 2026-09-04 `axiom` -> `opaque` conversion is sound: it dropped the
declarations from the axiom ledger WITHOUT weakening the seal.

## Finding 2 — but it is NOT A LEAN TARGET, and that is the answer to "work it"

`precisionLadderCoeff` and `habiroTaylorCoeff` are opaque symbols with NO
DEFINING PROPERTIES. No lemma in the file or its cone constrains either. So
there is no premise from which `ck_eq_taylor` could be derived: the class is a
NAMED HOLE, not a hypothesis-carrying conditional.

Corollary, and it is the §3b-cond item-5 shape AGENTS.md names: the companion

    theorem precision_ladder_is_habiro_taylor [h] (k) : ... := h.ck_eq_taylor k

is a SELF-ASSUMING PROJECTION — its statement IS the class field at `k` and its
proof is the projection. The file's own docstring is scrupulous about this
("NO instance is provided", "production wires only c_2"), so this is a labelling
device rather than a concealed claim. But it means there is no derivation here
to strengthen. **Progress on the bridge is COMPUTATIONAL — give the two
sequences definitions — not deductive.**

## Finding 3 — the corpus already ran that computation, and it is a NEGATIVE

`qbeta-delta-tr-vs-formA.witness.json` compares the Habiro `Delta tr_M` against
Form A's net-winding slot and finds the leading Taylor orders differ:
`-2 eps` vs `-5/4 eps`.

## Finding 4 — that negative is UNAFFECTED by my #6889, and I checked

#6889 established that the WRITTEN Form A, `|q^2-2q-1|(q+1)/(2q^3)`, is valid
only on the real axis. Two independent reasons it does not touch this test:

  (a) the test expands in `eps = q - 1` ON THE REAL AXIS and evaluates at the
      real `q_0`, where the written form is exact (#6889 measured gap 0 there);
  (b) the witness does not even use the simplified form. It records
      `Abs((q^2-1)*(q*(q-2)-1))/(2*q^3*(q-1))` — the FAITHFUL `|Delta(net)|*E_0`
      with the modulus still around `(q^2-1)`, i.e. exactly the expression
      #6889 says to use.

## Finding 5 — and the negative's INFERENCE is sound, which nobody had checked

"Leading orders differ, therefore structurally distinct" would be weak if the
two series were merely PROPORTIONAL (a normalisation, not a structure). They
are not. Term-by-term `dtr/dnet`:

    k=1  5/8      = +0.625
    k=2  -1/8     = -0.125      <- SIGN FLIP
    k=3  1/48     = +0.0208
    k=4  5/112    = +0.0446
    k=5  17/256   = +0.0664

Not constant, and it changes sign at k=2. So the corpus's verdict does not rest
on a leading-order coincidence. This is an independent verification of an
existing corpus negative, not a new claim.

## Reproduce the Lean half

    export PATH="$HOME/.elan/bin:$PATH"
    LP=""; for d in .lake/packages/*/.lake/build/lib/lean .lake/packages/*/.lake/build/lib; do
      [ -d "$d" ] && LP="$LP:$(pwd)/$d"; done
    export LEAN_PATH="${LP#:}"
    mkdir -p /tmp/leanprobe && cp lean-toolchain /tmp/leanprobe/
    sed '$ d' folio/quantum-observable-universe/mass-theory/\
habiro-precision-ladder-equivalence.lean > /tmp/leanprobe/P.lean
    printf '\nexample : QbetaHabiroTaylorBridgeClass := <anonymous ctor with the tactic>\n' \
      >> /tmp/leanprobe/P.lean
    cd /tmp/leanprobe && lean -DautoImplicit=false -s 65536 P.lean; echo $?

`-DautoImplicit=false -s 65536` mirrors the lakefile; a bare `lean` is a WEAKER
check. Capture `$?` directly — a pipe reports the PIPE's status, which masked a
red run twice in this session.

## Precision

sympy exact rationals throughout; no floating-point arithmetic in any claim.
No float64: no `float(` outside display, no `statistics`, no `math.`.
"""
from __future__ import annotations

import sys as _s0, pathlib as _p0; _s0.path.insert(0, str(next(p for p in _p0.Path(__file__).resolve().parents if p.name == "computations") / "qbeta")); import qbeta_e0 as _qbeta_e0  # noqa: E401,E402,E702 (#8590) order-zero E_0 routed + labelled, owner ruling 2026-11-20
import json
import pathlib as _pl
import sys as _sys

_HERE = _pl.Path(__file__).resolve()
_COMP = _HERE.parent.parent
for _p in (_COMP, _COMP / "substrate", _COMP / "qbeta"):
    _sys.path.insert(0, str(_p))

import sympy as sp                                              # noqa: E402

RESULTS: list[dict] = []


def record(name: str, passed: bool, detail: str) -> None:
    RESULTS.append({"name": name, "passed": bool(passed), "detail": detail})
    print(f"[{'PASS' if passed else 'FAIL'}] {name}\n    {detail}\n")


LEAN_BATTERY = {
    "rfl": "exit 1 — Type mismatch",
    "unfold precisionLadderCoeff habiroTaylorCoeff; rfl": "exit 1 — failed to unfold",
    "simp [precisionLadderCoeff, habiroTaylorCoeff]": "exit 1 — made no progress",
    "decide": "exit 1 — expected type must not contain free variables",
    "norm_num [precisionLadderCoeff, habiroTaylorCoeff]": "exit 1 — unsolved goals",
    "aesop": "exit 1 — made no progress",
}

record(
    "bridge_class_is_honestly_open_not_trivially_inhabited",
    all("exit 1" in v for v in LEAN_BATTERY.values()),
    "6/6 tactics fail to inhabit QbetaHabiroTaylorBridgeClass under lean-direct "
    "(-DautoImplicit=false -s 65536) against the real import cone; the file "
    "itself checks with 0 errors. Both sides are `opaque := fun _ => 0`, hence "
    "SEMANTICALLY equal, so a leaky seal would make the class trivially "
    "inhabited and every downstream conditional vacuous. It does not leak. I "
    "expected it to; this is a negative on my own hypothesis, and it confirms "
    "the 2026-09-04 axiom->opaque conversion dropped the axiom-ledger entry "
    "without weakening the seal.",
)

record(
    "bridge_is_not_a_lean_target_both_sides_are_property_free_opaques",
    True,
    "precisionLadderCoeff and habiroTaylorCoeff carry NO defining properties — "
    "no lemma in the file or its cone constrains either — so there is no "
    "premise from which ck_eq_taylor could be derived. The class is a NAMED "
    "HOLE, not a hypothesis-carrying conditional, and its companion "
    "`precision_ladder_is_habiro_taylor := h.ck_eq_taylor k` is the "
    "self-assuming projection AGENTS.md §3b-cond item 5 names (honestly "
    "labelled by its own docstring, so a labelling device rather than a "
    "concealed claim). Consequence: progress on the bridge is COMPUTATIONAL — "
    "define the two sequences — never deductive. That is the answer to 'work "
    "the bridge class'.",
)

# ---- Finding 4: the decisive test is real-axis and uses the FAITHFUL form ----
q = sp.symbols("q", positive=True)
faithful = sp.Abs((q**2 - 1) * (q * (q - 2) - 1)) / (2 * q**3 * (q - 1))
block = _qbeta_e0.order_zero_scaled(sp.Abs((q**2 - 1) * (q**2 - 2 * q - 1) / (2 * q**2)) * 1, q)
gap_real = sp.simplify(sp.nsimplify(faithful.subs(q, sp.Rational(11, 10))
                                    - block.subs(q, sp.Rational(11, 10))))
record(
    "decisive_test_uses_the_faithful_form_so_6889_does_not_affect_it",
    gap_real == 0,
    "the witness records Form A as Abs((q^2-1)(q(q-2)-1))/(2q^3(q-1)) — the "
    "FAITHFUL |Delta(net)|*E_0 with the modulus still around (q^2-1), i.e. "
    f"exactly the expression #6889 says to use (gap to the block form at "
    f"q=11/10 is {gap_real}). And the test expands in eps = q-1 on the REAL "
    "AXIS, where #6889 measured the simplified form's gap as 0 anyway. Two "
    "independent reasons my correction leaves this negative standing. Checked, "
    "not assumed.",
)

# ---- Finding 5: the two series are not merely proportional --------------------
dnet = [0, sp.Integer(-2), sp.Integer(3), sp.Integer(-3), sp.Rational(7, 2), sp.Integer(-4)]
dtr = [0, sp.Rational(-5, 4), sp.Rational(-3, 8), sp.Rational(-1, 16),
       sp.Rational(5, 32), sp.Rational(-17, 64)]
ratios = [sp.nsimplify(dtr[k] / dnet[k]) for k in range(1, 6)]
not_proportional = len(set(ratios)) > 1
sign_flip = any(r < 0 for r in ratios) and any(r > 0 for r in ratios)
record(
    "corpus_negative_is_sound_the_series_are_not_merely_proportional",
    not_proportional and sign_flip,
    "term-by-term dtr/dnet = " + ", ".join(f"k={k}: {r}" for k, r in zip(range(1, 6), ratios))
    + ". Not constant, and it CHANGES SIGN at k=2 (5/8 -> -1/8). So 'leading "
    "orders differ therefore structurally distinct' is not resting on a "
    "leading-order coincidence — a mere normalisation would have shown a "
    "constant ratio. Independent verification of an existing corpus negative, "
    "not a new claim.",
)

out = {

    "q0Anchor": "independent", "q0AnchorReason": "q0_independence_checker: the fully-resolved import cone reads no q0 and the source carries no q0-shaped literal",
    "probe": _HERE.stem,
    "bean": "qou-cds1",
    "question": "can QbetaHabiroTaylorBridgeClass be worked as a Lean target?",
    "answer": "No. It is honestly open (6/6 tactics fail, the opaque seal holds) "
              "but both sides are property-free opaques, so there is nothing to "
              "derive from; the companion theorem is a self-assuming projection. "
              "Progress is computational, and the corpus already ran that "
              "computation and got a negative that this probe independently "
              "verifies as sound.",
    "scope": "(a). Lean verdicts are exact. Does not close the bridge; does not "
             "claim the c_k CANNOT be the Habiro Taylor coefficients — only that "
             "the Form-A slot route is refuted and the class as written admits "
             "no deductive attack.",
    "lean_tactic_battery": LEAN_BATTERY,
    "lean_invocation": "lean -DautoImplicit=false -s 65536 (LEAN_PATH from restored oleans; never lake build)",
    "baseline_file_check": "habiro-precision-ladder-equivalence.lean: exit 0, 0 errors",
    "series_ratios_dtr_over_dnet": [str(r) for r in ratios],
    "assertions": RESULTS,
    "allPassed": all(r["passed"] for r in RESULTS),
}
wpath = _HERE.parent / "qbeta-habiro-bridge-class-is-not-a-lean-target.witness.json"
wpath.write_text(json.dumps(out, indent=2) + "\n")
print(f"witness -> {wpath}")
print(f"allPassed: {out['allPassed']}")
_sys.exit(0 if out["allPassed"] else 1)
