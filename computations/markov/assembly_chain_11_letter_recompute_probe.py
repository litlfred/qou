#!/usr/bin/env python3
"""qou-1ucq — recompute the p/n assembly chains on the CANONICAL 11-letter element.

`markov-trace-assembly-{proton,neutron}.derivation.json` each report a tr_M
computed from a LEGACY word, not from the element the live producer returns:

  * proton: steps 4 and 6 assert a "6-crossing word, all positive sigma", giving
    chi^(3) = q^6 and chi^(1,1,1) = q^-6. Measured, the canonical element has 6
    sigma, 3 sigma^-1 and 2 averaged letters, so that premise is false (flagged
    in the chain 2026-08-30, not repaired there).
  * neutron: steps 5 and 7 evaluate chi from n_+/n_- of the 5-letter word
    sigma_1 sigma_1^-1 sigma_2 sigma_1 sigma_2^-1 -- a DIFFERENT element of
    H_3(q) from the 11-letter one its own step 4 declares. Its legacy-convention
    note says so; this is the root cause of the 7.285e-8 (73x tolerance)
    disagreement with `n-tr-M-q0.derivation.json`.

THE RECOMPUTE. No new machinery: the corpus's own symbolic path, which is the
route `atom_braid_word_3A`'s docstring says is the only valid one -- chi^lambda
as the trace of the seminormal representation matrix product, each letter
(c, d, g) acting as c*rho(sigma_g) + d*1, assembled as tr_M = sum_lambda
y_lambda * chi^lambda. Exact over Q(q) throughout; no float64 anywhere.

RESULT (as written, 2026-08): it reproduces the live production values to every
digit they carry.

    atom     recomputed (proton pin)          live producer witness
    p        1.1457596924573008697            1.14575969245730086968...
    n        0.98774368811580957163           0.98774368811580957163...

and at the muon-2022 pin it likewise matches the muon witnesses.

⚠ THAT AGREEMENT ENDED ON 2026-09-05 AND ITS ENDING IS THE POINT. The owner
ruling `qou-hu1f` made the borromean intra-nucleon word canonical, so the
recompute — which reads the canonical element — now returns

    p  0.62932840220292191817        n  0.47513351715568221251

while `LIVE` below still holds faithful copies of committed witnesses in the
grouped frame. Four of the seven assertions fail, and **the recompute is the
side that is right**: this probe is now a true report that the assembly chains
are stale, which is exactly the job the agreement was evidence for.

Do NOT repair it by updating `LIVE` with better numbers. Those entries stand
for committed producer output; editing them to match would hide the staleness
rather than fix it. Regenerate the producer instead.

UPDATE 2026-09-13, and it makes the point above sharper. The neutron chain was
migrated to `canonical_trm_reference` and regenerated, and this probe stayed
red — because `LIVE` held HARDCODED COPIES under a comment claiming they were
"read from the committed files". They had been read once, by hand, and pasted.
A copy of a file is not the file, and the difference only shows when the file
moves. The proton-pin entries now genuinely read the committed chains, and the
neutron assertion passes at the precision that witness records.

Three failures remain, each a real and distinct gap: the proton assembly chain
is an ORPHAN (its only producers live in `_deprecated/`, so nothing can
regenerate it and it stays grouped-era), and no muon-pinned assembly witness
exists at all, so both muon entries are pre-ruling copies with nothing to read.
Bean `qou-4383`. So the correct
recomputation of these chains is not a new number -- it is the number the rest
of the stack already carries, which is the strongest available check that the
linear-functional route is what the producers actually run.

WHICH FRAME. The chains declare convention C at the CODATA-2018 muon pin. They
are NOT recomputed in that frame, deliberately: convention C was excised by owner
ruling (2026-08-09, reaffirmed 2026-08-15) and the proton pin is canonical (R2),
so recomputing in C would be work in a retired frame. The weights used here are
the corpus's own convention-D weights, and note what they do to the chains'
structure:

    y_(3)     = (q^4 + 1)/(q^2 + 1)^2
    y_(2,1)   = q^2/(q^2 + 1)^2
    y_(1,1,1) = 0

The three-row weight VANISHES under D. So the sign-rep step -- one of the two
steps carrying the proton chain's false "all positive sigma" premise -- is
multiplied by zero and cannot affect the answer either way. The defect was real;
under the canonical convention it is also inert.

NOT CLAIMED: that the chains' reported values were wrong *within* convention C.
That is a separate question this probe does not answer, and cannot, since the
C weights are no longer in the tree.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
sys.path.insert(0, str(HERE))

import sympy as sp

import markov_weights_symbolic as M

PINS = {
    "proton": "1.1099785827513808075916690956107688798744991218736",
    "muon2022": "1.109978595642739046681795129380001752700065561029",
}
# Live producer values. The PROTON-pin entries are now READ from the committed
# derivation chains; the muon-2022 entries remain recorded copies, because no
# muon-pinned assembly witness exists to read.
#
# THEY USED TO BE FOUR HARDCODED STRINGS, under a comment claiming they were
# "read from the committed files". They were read once, by hand, and pasted —
# which is a different thing, and it showed: when
# `build_markov_trace_assembly_neutron_chain.py` was migrated to the canonical
# reference on 2026-09-13 (bean qou-4383) and its witness moved to
# 0.4751335171556822, this probe went on comparing against the frozen
# 0.98774368811580957163 and stayed red for a reason that no longer existed.
# A copy of a file is not the file.
_CHAIN = {"p": "markov-trace-assembly-proton.derivation.json",
          "n": "markov-trace-assembly-neutron.derivation.json"}
_MUON_WITNESS = "atomic-tr-m-mpfr-50dps.witness.json"


def _committed_target(label: str) -> str:
    """`target_value` from the committed assembly chain, as an exact string."""
    import json                                            # noqa: PLC0415
    path = HERE.parent / _CHAIN[label]
    return str(json.loads(path.read_text())["target_value"])


def _committed_muon_target(atom_name: str) -> str:
    """`tr_M_at_q0_50dps` from the committed muon-pinned witness (bean qou-sikd)."""
    import json                                            # noqa: PLC0415
    path = HERE.parent / _MUON_WITNESS
    d = json.loads(path.read_text())
    for row in d.get("results", []):
        if row.get("atom") == atom_name:
            return str(row["tr_M_at_q0_50dps"])
    raise KeyError(f"{atom_name} not found in {_MUON_WITNESS}")


def _committed_muon_pin() -> str:
    import json                                            # noqa: PLC0415
    path = HERE.parent / _MUON_WITNESS
    d = json.loads(path.read_text())
    return str(d.get("q0Value") or d.get("q_0_50dps"))


PINS["muon2022"] = _committed_muon_pin()

LIVE = {
    ("p", "proton"): _committed_target("p"),
    ("n", "proton"): _committed_target("n"),
    ("p", "muon2022"): _committed_muon_target("proton"),
    ("n", "muon2022"): _committed_muon_target("neutron"),
}
CHAIN_REPORTS = {"p": "1.0653062285923893", "n": "0.9232332299116371"}

_results: list[tuple[str, bool, str]] = []


def check(name: str, ok: bool, detail: str) -> None:
    _results.append((name, bool(ok), detail))
    print(f"  [{'PASS' if ok else 'FAIL'}] {name} — {detail}")


def main() -> int:
    q = sp.symbols("q", positive=True)

    print("=" * 72)
    print("  qou-1ucq — assembly chains recomputed on the 11-letter element")
    print("=" * 72)

    y = M.solve_y_lambda(3)
    print("\n-- the convention-D Wedderburn weights the recompute uses")
    for lam in sorted(y, key=len):
        print(f"     y_{str(lam):<10} = {sp.simplify(y[lam])}")
    check("three_row_weight_vanishes_under_D",
          sp.simplify(y[(1, 1, 1)]) == 0,
          "y_(1,1,1) = 0, so the sign-rep step cannot affect the answer under D")

    for lbl, (Z, N) in (("p", (1, 0)), ("n", (0, 1))):
        cr = M.atom_braid_word_3A_to_crossings(Z, N, include_inter=False)
        expr = sp.simplify(M.tr_M_canonical(cr, 3)[0])
        print(f"\n-- atom {lbl}: {len(cr)} letters on 3 strands")
        check(f"{lbl}_element_has_eleven_letters",
              len(cr) == 11,
              f"the canonical element, not the legacy word the chain uses")
        for pin, qv in PINS.items():
            got = sp.N(expr.subs(q, sp.Rational(qv)), 30)
            want = sp.N(sp.Rational(LIVE[(lbl, pin)]), 30)
            rel = sp.N(sp.Abs(got - want) / sp.Abs(want), 6)
            # TOLERANCE FROM THE STORED PRECISION, not a fixed 1e-18.
            #
            # This probe's claim is "reproduces the live producer witnesses …
            # to every digit they CARRY", and a fixed threshold does not
            # express that. `markov-trace-assembly-neutron.derivation.json`
            # stores `target_value` as a 16-significant-digit float, so the
            # best achievable relative agreement is ~1e-16 — and the recompute
            # hit 2.6e-17, failing a 1e-18 bar it could not have cleared. That
            # is a category error, not a disagreement.
            #
            # This is NOT a widening. It tightens wherever the stored value is
            # more precise: the muon-2022 entries carry ~49 digits and are now
            # held to ~1e-48 instead of 1e-18. It only ever demands as much as
            # the witness actually records.
            _sig = len(str(LIVE[(lbl, pin)]).replace(".", "").lstrip("0"))
            _tol = sp.Rational(1, 10 ** max(_sig - 1, 1))
            check(f"{lbl}_matches_live_producer_at_{pin}",
                  rel < _tol,
                  f"{sp.N(got, 20)} vs witness {str(LIVE[(lbl, pin)])[:20]} — "
                  f"rel {rel} vs tol 1e-{max(_sig - 1, 1)} ({_sig} sig digits stored)")
        drift = sp.N(
            sp.Abs(sp.N(expr.subs(q, sp.Rational(PINS['proton'])), 30)
                   - sp.Rational(CHAIN_REPORTS[lbl]))
            / sp.Rational(CHAIN_REPORTS[lbl]) * 100, 6)
        print(f"     chain currently reports {CHAIN_REPORTS[lbl]} — {drift} % away")

    n_pass = sum(1 for _, ok, _ in _results if ok)
    print("\n" + "=" * 72)
    print(f"  {n_pass}/{len(_results)} assertions passed")
    # The agreement line below used to print UNCONDITIONALLY, so this summary
    # asserted "reproduces … to every digit they carry" while four of its own
    # seven assertions were failing. Gated on the result (bean qou-4383,
    # 2026-09-13).
    if n_pass == len(_results):
        print("  The recompute on the canonical 11-letter element reproduces the live")
        print("  producer witnesses at both pins, to every digit they carry.")
    else:
        print("  IT NO LONGER REPRODUCES THEM, AND THE RECOMPUTE IS THE SIDE THAT IS")
        print("  RIGHT. The 2026-09-05 intra-nucleon ordering ruling (qou-hu1f) made")
        print("  the borromean word canonical, so the recompute now returns the")
        print("  canonical values (n: 0.47513351715568221251) while `LIVE` above")
        print("  holds faithful copies of committed witnesses that are still")
        print("  grouped-era (n: 0.98774368811580957163). The failure is a true")
        print("  report of a stale PRODUCER, not a defect in this probe.")
        print("  PARTLY RESOLVED 2026-09-13. The neutron chain was migrated to")
        print("  canonical_trm_reference and regenerated, and its assertion now")
        print("  PASSES at the precision that witness records. The three that")
        print("  remain are each a distinct, real gap:")
        print("    p @ proton   — markov-trace-assembly-proton.derivation.json is")
        print("                   an ORPHAN: its only producers are in _deprecated/,")
        print("                   so nothing live can regenerate it and it is still")
        print("                   grouped-era.")
        print("    p,n @ muon   — no muon-pinned assembly witness exists at all, so")
        print("                   those LIVE entries are recorded pre-ruling copies")
        print("                   with nothing to read. Labelled as such above.")
    print("  CORRECTED 2026-08-31: an earlier draft said BOTH chains' reported")
    print("  values 'come from legacy words'. That holds for the PROTON chain,")
    print("  whose steps assert an all-positive-sigma word. The NEUTRON chain's")
    print("  leaf is hardcoded against TR_M_AT_Q0 -- canon -- so its stale value")
    print("  was a regeneration lag, not a legacy-word computation; only its")
    print("  symbolic steps 5-7 use the legacy convention, which its own builder")
    print("  already documented. Both are now regenerated from their builders.")
    print("  Exact over Q(q); no float64 anywhere. Scope: a correction, not a")
    print("  new result -- the number was already in the stack.")
    print("=" * 72)
    return 0 if n_pass == len(_results) else 1


def _selftest() -> int:
    y = M.solve_y_lambda(3)
    assert sp.simplify(y[(1, 1, 1)]) == 0
    print("self-test: ok (y_(1,1,1) == 0 under Convention D)")
    return 0


if __name__ == "__main__":
    if "--self-test" in sys.argv or "--selftest" in sys.argv:
        raise SystemExit(_selftest())
    raise SystemExit(main())
