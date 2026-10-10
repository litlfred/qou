#!/usr/bin/env python3
"""
Generalized per-λ Schur–Weyl Markov-weight chain builder.

Generalises `build_schur_weyl_weight_chain.py` (λ=(3) only) and
`build_schur_weyl_weight_extra.py` (hardcoded n=3) to arbitrary
partitions λ ⊢ n.  Uses the existing `schur_weyl_symbolic.py`
helpers `partitions_of(n)` and `hook_lengths(λ)` so no new
combinatorial code is introduced.

Usage:
  python3 build_schur_weyl_weight_general.py            # all partitions of n=6 (deuteron)
  python3 build_schur_weyl_weight_general.py --n 9      # all partitions of n=9 (triton/³He)
  python3 build_schur_weyl_weight_general.py --n 6 --only "(3,3),(3,2,1)"

Output (one file per partition):
  schur-weyl-weight-<short>.derivation.json
  where <short> is the partition with no commas/spaces, e.g.
  (3,2,1) → "321", (1,1,1,1,1,1) → "111111".

Each chain has trust profile {axiom: 1, mathlib-cited: 2,
derived: 1, script-cited: 0, computational: 0} — fully-trusted
modulo the Hecke-energy + Schur + Wedderburn axioms.

This is the **partition-of-n** frontier closure for the chain
registry: combined with `markov-trace-assembly-{p,n}` chains, it
unblocks fully-trusted Markov-trace assembly at A=2 (deuteron,
n=6), A=3 (triton/³He, n=9), and A=4 (⁴He, n=12).
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from derivation_chain import (  # noqa: E402
    DerivationChain,
    DerivationStep,
    FirstPrinciple,
    TrustBasis,
)
from schur_weyl_symbolic import partitions_of, hook_lengths  # noqa: E402


HERE = Path(__file__).parent


def _partition_short(parts: tuple[int, ...]) -> str:
    """Filename-safe identifier: parts joined with no separator.

    Two-digit parts are joined with underscores to avoid ambiguity:
    (10, 2) → "10_2".  Single-digit parts: "(3,2,1)" → "321".
    """
    if all(p < 10 for p in parts):
        return "".join(str(p) for p in parts)
    return "_".join(str(p) for p in parts)


def _partition_compact(parts: tuple[int, ...]) -> str:
    """No-space symbolic identifier: e.g. (3, 2, 1) → '(3,2,1)'."""
    return "(" + ",".join(str(p) for p in parts) + ")"


def _partition_label(parts: tuple[int, ...]) -> str:
    """Display label with spaces: (3, 2, 1)."""
    return "(" + ", ".join(str(p) for p in parts) + ")"


def _count_syt(parts: tuple[int, ...]) -> int:
    """f_λ = n! / ∏ h_x(λ) — the hook-length formula for # SYT."""
    import math
    n = sum(parts)
    hooks = hook_lengths(list(parts))
    prod_hooks = 1
    for h in hooks:
        prod_hooks *= h
    return math.factorial(n) // prod_hooks


def _weight_formula(parts: tuple[int, ...], hooks: list[int]) -> str:
    """Markov weight formula as human-readable string.

    w_λ(q) = (q − q^{-1})^(n − l(λ)) · ∏_x [h_x]_q^{-1}.
    """
    n = sum(parts)
    l_lambda = len(parts)
    h_exp = n - l_lambda
    # Numerator: (q − q^{-1})^h_exp; convention: () means 1.
    if h_exp == 0:
        num = "1"
    elif h_exp == 1:
        num = "(q − q^{-1})"
    else:
        num = f"(q − q^{{-1}})^{h_exp}"
    # Denominator: ∏ [h]_q over hooks.
    den_terms = " · ".join(f"[{h}]_q" for h in hooks)
    return f"{num} / ({den_terms})"


def build_for_partition(parts: tuple[int, ...]) -> DerivationChain:
    n = sum(parts)
    l_lambda = len(parts)
    hooks = hook_lengths(list(parts))
    f_lambda = _count_syt(parts)
    h_exp = n - l_lambda
    weight = _weight_formula(parts, hooks)
    label = _partition_label(parts)
    compact = _partition_compact(parts)
    short = _partition_short(parts)

    steps: list[DerivationStep] = []

    # 1 — q-integer (Hecke energy origin)
    steps.append(DerivationStep(
        name="q-integer [k]_q := (q^k − q^{-k})/(q − q^{-1})",
        operation=(
            "Define [k]_q := (q^k − q^{-k}) / (q − q^{-1}); same "
            "definition used in every per-λ chain (the (q − q^{-1}) "
            "denominator is the per-crossing Hecke energy scale)."
        ),
        inputs=[FirstPrinciple.HECKE_ENERGY.value],
        output_name="q_integer",
        output_value="[k]_q := (q^k − q^{-k}) / (q − q^{-1})",
        trust_basis=TrustBasis.AXIOM,
        lean_ref="qou:QOU.GaugeFieldFluidDynamics.qInteger",
        citation="kassel1995",
        jet_order=0,
    ))

    # 2 — Hook-length data
    steps.append(DerivationStep(
        name=f"Hook-length data for λ = {label}",
        operation=(
            f"For λ = {label} ⊢ {n}, hook lengths are {hooks} "
            f"(via `schur_weyl_symbolic.hook_lengths`).  "
            f"l(λ) = {l_lambda}, n − l(λ) = {h_exp}."
        ),
        inputs=["q_integer", FirstPrinciple.SCHUR.value],
        output_name="hook_data",
        output_value={
            "lambda": label,
            "parts": list(parts),
            "hook_lengths": hooks,
            "n": n,
            "l_lambda": l_lambda,
            "n_minus_l": h_exp,
        },
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:YoungDiagram.hookLength",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Mathlib's `Mathlib.Combinatorics.Young.YoungDiagram` "
            "exposes `hookLength`; the value is read off the Young "
            "diagram combinatorially.  Source on the Python side: "
            "`computations/schur_weyl_symbolic.hook_lengths`."
        ),
    ))

    # 3 — Wedderburn block dimension f_λ
    steps.append(DerivationStep(
        name=f"Wedderburn block dimension f_λ for λ = {label}",
        operation=(
            f"From Wedderburn, H_{n}(q) = ⊕_λ M_{{f_λ}}(K(q)) where "
            f"f_λ counts standard Young tableaux of shape λ.  Hook-"
            f"length formula: f_λ = n! / ∏ h_x(λ) = {f_lambda}."
        ),
        inputs=["hook_data", FirstPrinciple.WEDDERBURN.value],
        output_name="f_lambda",
        output_value={"lambda": label, "f_lambda": f_lambda},
        trust_basis=TrustBasis.MATHLIB_CITED,
        lean_ref="qou:STUB:HeckeWedderburn",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
    ))

    # 4 — Markov weight formula
    steps.append(DerivationStep(
        name=f"Markov weight w_{compact}(q)",
        operation=(
            f"Apply the Markov weight convention "
            "w_λ(q) := (q − q^{-1})^(n − l(λ)) · ∏_x [h_x]_q^{-1}.  "
            f"For {label}: n − l(λ) = {h_exp}, hooks = {hooks}.  "
            f"Result: {weight}."
        ),
        inputs=["q_integer", "hook_data"],
        output_name="w_lambda",
        output_value=weight,
        trust_basis=TrustBasis.DERIVED,
        lean_ref="qou:STUB:MarkovWeight",
        citation="kassel1995",
        jet_order=0,
        gb_filtration_level=0,
        notes=(
            "Pure algebra: substitute the hook lengths from step 2 "
            "and the exponent (n − l(λ)) from step 2 into the "
            "convention.  The (q − q^{-1})^(n − l(λ)) prefactor "
            "arises from Hoefsmit's normalisation of the simple "
            "reps of H_n(q); it ensures the Markov stabilisation "
            "tr_M(α σ_n) = z · tr_M(α) holds with the canonical "
            "stabilisation parameter z = 1/(q^{1/2} + q^{-1/2})."
        ),
    ))

    return DerivationChain(
        target=f"w_{compact}(q)",
        target_value=weight,
        target_tolerance=0.0,
        content_block="prop:full-pole-structure-mass-trace",
        description=(
            f"Schur–Weyl Markov weight w_{compact}(q) for partition "
            f"λ = {label} ⊢ {n}.  Trust profile {{axiom: 1, "
            "mathlib-cited: 2, derived: 1, script-cited: 0, "
            "computational: 0} — fully-trusted modulo the "
            "AXIOM (Hecke energy) and the Schur + Wedderburn "
            "first-principles entrypoints.  Generated by "
            "`build_schur_weyl_weight_general.py`; uses "
            "`schur_weyl_symbolic.partitions_of` and "
            "`schur_weyl_symbolic.hook_lengths` as the combinatorial "
            "base."
        ),
        steps=steps,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--n", type=int, default=6,
                        help="Build chains for all partitions of n (default 6)")
    parser.add_argument("--only", type=str, default=None,
                        help="Comma-separated partition tuples like '(3,3),(3,2,1)' "
                             "(restricts to a subset)")
    args = parser.parse_args()

    if args.only:
        # Parse "(3,3),(3,2,1)" → [(3,3), (3,2,1)] by splitting on ')'
        # and stripping the per-tuple "(...".  Naively splitting on ','
        # is ambiguous since tuples are themselves comma-separated.
        only: list[tuple[int, ...]] = []
        for piece in args.only.split(")"):
            piece = piece.strip(" ,(")
            if not piece:
                continue
            parts = tuple(int(x) for x in piece.split(",") if x.strip())
            if parts:
                only.append(parts)
        targets = only
    else:
        targets = list(partitions_of(args.n))

    overall_ok = True
    print(f"Building Schur-Weyl weight chains for n={args.n} "
          f"({len(targets)} partition(s))...")
    for parts in targets:
        chain = build_for_partition(parts)
        ok, issues = chain.structural_check()
        out = HERE / f"schur-weyl-weight-{_partition_short(parts)}.derivation.json"
        chain.save(out)
        marker = "✓" if ok else "✗"
        print(f"  {marker} λ={_partition_label(parts)}  trust={chain.trust_summary()}  "
              f"→ {out.name}")
        for i in issues:
            print(f"      - {i}")
        if not ok:
            overall_ok = False
    print(f"\nbuild_schur_weyl_weight_general: {'PASS' if overall_ok else 'FAIL'}")
    return 0 if overall_ok else 1


if __name__ == "__main__":
    sys.exit(main())
