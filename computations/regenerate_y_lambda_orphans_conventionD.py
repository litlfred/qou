#!/usr/bin/env python3
# polynomial_q_not_applicable: numerical/symbolic evaluation of a closed form whose
# source is the convention-D pinning in QOU/QBeta/TemperleyLiebTower.lean.
"""Bring the **orphan** `y_λ` witnesses to convention D, preserving each schema.

These carry `y_λ` tables but have no producer the regeneration harness can
reach — their producers are in `_deprecated/`, or there never was one. They
cannot simply be retired, because live code and paper content read them
(`qou-rohl`: `wenzl-y-lambda-h9/h12` alone feed six consumers, including
`nucleus_real_sdp.py` and three `mass-theory` content blocks).

So each is rewritten in place **by recomputation**, not by editing: every
`y_λ` value is recomputed from the convention-D closed form and written back
into the file's own schema, with every other field left alone.

## The weights

`z_D = q³/(q²+1)` is the unique non-trivial Markov trace on `H₃(q)` whose
radical contains the three-strand antisymmetriser (`qou-u2jg`, Lean,
sorry-free). At that `z`:

    y_λ = [n − 2k + 1]_q / [2]_q^n      for λ = (n−k, k),  ℓ(λ) ≤ 2
    y_λ = 0                             for ℓ(λ) ≥ 3

with `[m]_q = (q^m − q^{−m})/(q − q^{−1})`.

## Why a rewriter rather than one canonical emitter

The six files disagree on nearly everything except the mathematics: the weight
field is variously `y_lambda`, `y_lambda_numeric`, `y_lambda_float`,
`y_lambda_symbolic`, `y_lambda_simplified_factored`; the table lives under
`tables_by_n` or under `data`; values are strings in some and floats in others.
Consumers read those exact names. Emitting one canonical shape would migrate
the convention and break every reader in the same commit, so the schema is
preserved and only the numbers move.

`y-lambda-sdp-witness.json` is **not** handled: it has no partition-paired
weight field, so there is nothing here to rewrite. It needs its own look.

## Anchor

Each file's own `q₀` is used where the file states one, so that only the
convention moves and the ideal/experimental layer is left where it was
(AGENTS.md §"q₀ anchor convention" — never straddle). Files that state no `q₀`
fall back to the muon pin, matching the other `y_λ` tables, and say so.

## Verification

Nothing is written unless, for every `n` touched, `Σ_λ dim_λ · y_λ = 1` holds
on the rewritten values, and every `ℓ(λ) ≥ 3` weight is exactly zero.

Usage:
    python3 computations/regenerate_y_lambda_orphans_conventionD.py [--check]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

from q0_stamp import pin_value_for_anchor  # noqa: E402

HERE = Path(__file__).resolve().parent
DPS = 50

# q0 comes from the pin table, never a literal. This held
# `1.1099785955541805`, the SUPERSEDED muon value -- it matches neither
# current pin. The NAME says muon, so the muon pin is taken explicitly
# rather than through the manifest, which would hand this stem proton.
# Owner ruling 2026-08-24, bean `qou/ftuv`.
MUON_Q0 = pin_value_for_anchor("muon")

TARGETS = [
    "wenzl-y-lambda-h9.witness.json",
    "wenzl-y-lambda-h12.witness.json",
    "y-lambda-symbolic-witness.json",
    "y-lambda-wenzl-bridge-numeric-witness.json",
    "y-lambda-wenzl-witness.json",
]

_qs = sp.Symbol("q", positive=True)


def qint_num(q, m: int):
    return (q ** m - q ** (-m)) / (q - 1 / q)


def qint_sym(m: int):
    return sp.simplify((_qs ** m - _qs ** (-m)) / (_qs - 1 / _qs))


def y_num(q, n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return mp.mpf(0)
    k = lam[1] if len(lam) == 2 else 0
    return qint_num(q, n - 2 * k + 1) / qint_num(q, 2) ** n


def y_sym(n: int, lam: tuple[int, ...]):
    if len(lam) >= 3:
        return sp.Integer(0)
    k = lam[1] if len(lam) == 2 else 0
    return sp.simplify(qint_sym(n - 2 * k + 1) / qint_sym(2) ** n)


def dim_irrep(n: int, lam: tuple[int, ...]) -> int:
    conj = [sum(1 for p in lam if p > j) for j in range(lam[0])]
    prod = 1
    for i, row in enumerate(lam):
        for j in range(row):
            prod *= row - j + conj[j] - i - 1
    return int(sp.factorial(n) / prod)


def find_q0(doc) -> tuple[str, str]:
    """(q0_string, where_it_came_from) — ALWAYS the pin table; the file's own
    field is read only to report a disagreement.

    FIXED 2026-09-04 (bean qou-9ugp).  This used to RETURN the file's own `q0`
    when it stated one, and fall back to the pin table otherwise.  That made the
    producer a FIXED POINT ON ITS OWN STALE INPUT: the witness records a q0, the
    producer reads it back, recomputes the weights at it, and writes it out
    again — so an anchor move can never propagate, no matter how often this runs.
    It is the same self-certification shape AGENTS.md records for the
    anchor-defining witness, one file over.

    Measured at the time of the fix: the 2026-08-22 re-derivation of the muon
    anchor to the CODATA-2022 lepton ratio had not reached ANY of the three
    file-field targets, all three of which still held the CODATA-2018 value
    `1.109978595554180575…` — one stale number perpetuated across three files.
    None held proton, so there was no legitimate per-file pin being preserved.

    The file's claim is still read, because a disagreement is worth seeing; it
    just no longer wins.
    """
    stack, stated = [doc], None
    while stack:
        node = stack.pop()
        if isinstance(node, dict):
            for k, v in node.items():
                if stated is None and k in ("q_0", "q0", "q_0_50dps") \
                        and isinstance(v, (str, float)):
                    stated = (k, str(v))
                stack.append(v)
        elif isinstance(node, list):
            stack.extend(node[:20])
    if stated is None:
        return MUON_Q0, "pin table (file states none)"
    k, v = stated
    if v[:30] == str(MUON_Q0)[:30]:
        return MUON_Q0, f"pin table (file field `{k}` agrees)"
    return MUON_Q0, (f"pin table — OVERRIDING stale file field `{k}` = {v[:24]}…")


def rewrite(doc, q):
    """Rewrite every partition-paired y_λ in place. Returns (count, per_n)."""
    n_seen: dict[int, list] = {}
    count = 0

    def walk(node):
        nonlocal count
        if isinstance(node, dict):
            part = node.get("partition")
            lam = None
            if isinstance(part, (list, tuple)):
                cleaned = [x for x in part if x not in ("_", "", None)]
                try:
                    lam = tuple(int(x) for x in cleaned)
                except (TypeError, ValueError):
                    lam = None
            if lam:
                n = sum(lam)
                for key in list(node):
                    if "y_lam" not in key and "y_at" not in key:
                        continue
                    old = node[key]
                    if "symbolic" in key or "factored" in key:
                        new = str(y_sym(n, lam))
                    else:
                        val = y_num(q, n, lam)
                        new = (mp.nstr(val, DPS, strip_zeros=False)
                               if isinstance(old, str) else float(val))
                    node[key] = new
                    count += 1
                n_seen.setdefault(n, []).append((lam, y_num(q, n, lam)))
            for v in node.values():
                walk(v)
        elif isinstance(node, list):
            for v in node:
                walk(v)

    walk(doc)
    return count, n_seen


def verify(n_seen) -> list[str]:
    fails = []
    tol = mp.mpf(10) ** (-(DPS - 6))
    for n, rows in sorted(n_seen.items()):
        seen = {}
        for lam, y in rows:
            seen[lam] = y
        total = sum(dim_irrep(n, lam) * y for lam, y in seen.items())
        # Only meaningful when the table is complete for that n.
        from sympy.utilities.iterables import partitions as _p
        n_parts = sum(1 for _ in _p(n))
        if len(seen) == n_parts and abs(total - 1) > tol:
            fails.append(f"n={n}: tr(1) = {mp.nstr(total, 20)} (expected 1)")
        for lam, y in seen.items():
            if len(lam) >= 3 and y != 0:
                fails.append(f"n={n} λ={lam}: ℓ(λ)≥3 weight {y} != 0")
    return fails


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n", 1)[0])
    ap.add_argument("--check", action="store_true", help="verify without writing")
    args = ap.parse_args()
    mp.mp.dps = DPS

    rc = 0
    for name in TARGETS:
        path = HERE / name
        if not path.exists():
            print(f"  SKIP   {name} (absent)")
            continue
        doc = json.loads(path.read_text())
        q0_str, origin = find_q0(doc)
        q = mp.mpf(q0_str)
        count, n_seen = rewrite(doc, q)
        fails = verify(n_seen)
        ns = ",".join(str(n) for n in sorted(n_seen))
        if fails:
            print(f"  FAIL   {name}: {'; '.join(fails[:2])}", file=sys.stderr)
            rc = 1
            continue
        print(f"  OK     {name:<42} {count:4d} weights, n={ns}, q0 from {origin}")
        if not args.check:
            # Write back the q0 ACTUALLY COMPUTED WITH (bean qou-9ugp,
            # 2026-09-04).  Until this line the producer recomputed every
            # weight at the pin table's value and then left the file's own
            # stale `q0` field untouched -- so after the find_q0 fix above the
            # witness would have claimed a pin it did not compute at, which is
            # worse than the fixed point it replaced.
            def _set_q0(node):
                if isinstance(node, dict):
                    for k in list(node):
                        if k in ("q_0", "q0", "q_0_50dps") and isinstance(
                                node[k], (str, float)):
                            node[k] = q0_str
                        else:
                            _set_q0(node[k])
                elif isinstance(node, list):
                    for v in node:
                        _set_q0(v)
            _set_q0(doc)
            doc["markov_convention"] = "D"
            doc["markov_parameter_symbolic"] = "q**3/(q**2 + 1)"
            doc["scriptFile"] = f"computations/{Path(__file__).name}"
            # Provenance stamp (bean qou-4un2): this producer writes its
            # witness directly, so nothing else records which script made
            # it -- and a re-run of an unstamped producer DELETES the
            # scriptFile a downstream pass had added. no q0 in this producer's cone; stamp provenance only.
            from qou_substrate.witness import WitnessBuilder as _WB
            import os as _os  # noqa: E402 -- provenance stamp
            doc.setdefault("scriptFile", _os.path.basename(__file__))
            # q0_anchor was False -- "no q0 in this producer's cone".  That is
            # false and always was: every value this producer writes is a Wenzl
            # weight y_lambda(q0), a function of the pin, and the fix above
            # moved them by 3.18e-10.  The stem is declared `ideal_muon` in the
            # manifest so this resolves the MUON anchor, per the owner ruling of
            # 2026-08-24 that this producer is muon by name.
            # Drop the PREVIOUS run's anchor fields before stamping. The
            # builder guards on `if "q0Anchor" not in payload`, writing anchor
            # AND value only inside it (bean qou-ftuv), so a doc that already
            # carries a stale `q0Anchor` silently ignores everything passed
            # here -- which is how these five sat at `independent` with a null
            # q0Value while computing at the muon pin.
            for _k in ("q0Anchor", "q0AnchorReason", "q0Value", "q0Values"):
                doc.pop(_k, None)
            _WB.stamp_staleness_metadata(
                doc, script_path=__file__, engine=None,
                q0_anchor="muon", q0_value=q0_str,
                q0_anchor_reason=(
                    "computes Wenzl weights y_lambda(q0) at the MUON pin, taken "
                    "explicitly from pin_value_for_anchor('muon') rather than "
                    "through the manifest (owner ruling 2026-08-24). Stamped "
                    "explicitly because the auto-detector reads the import cone "
                    "and this producer reaches q0 via q0_stamp, not q_parameter, "
                    "so it was being stamped 'independent' on a value that is a "
                    "function of the pin."))
            path.write_text(json.dumps(doc, indent=2) + "\n")
    if args.check:
        print("\n--check: nothing written.")
    return rc


if __name__ == "__main__":
    sys.exit(main())
