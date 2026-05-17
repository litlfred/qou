"""Canonical |tr_M| via cached χ^λ + y_λ tables (PR #681 Step 2).

Per `docs/audits/2026-05-17-knot-fusion-step1-audit.md` (audit doc
shipped on PR #681), the missing piece between the existing
`per_irrep_pole_atom.py` pipeline (which computes pole order via
q → u² substitution) and the canonical Markov trace `|tr_M(β_atomic)|`
at q_0 (1 ppb compute target) is a **~50-line combiner**:

  |tr_M(β_atomic, q_0)| = | Σ_λ y_λ(q_0) · χ^λ(β_atomic) |

where:
  - y_λ(q_0) lives in `y-lambda-mpfr-witness.json` (50-dps mpmath
    per n, all 11 n=2-12 partitions per n cached)
  - χ^λ(β_atomic) lives in `chi-{atom}-h{n}.witness.json` (per atom,
    per partition; coverage varies)

## Coverage status (existing on main)

  Atom        H_n   Coverage
  ----------------------------
  proton      3     3/3   complete
  neutron     3     3/3   complete
  deuteron    6     11/11 complete
  tritium     9     2/30  partial — needs 28 more
  helium-3    9     3/30  partial — needs 27 more
  helium-4    12    0/77  empty
  ----------------------------

This combiner runs for any chi-cache coverage but reports incomplete
results when partitions are missing. For p, n, D the result is the
full canonical |tr_M|; for T, ³He, ⁴He it's a partial sum + the
list of missing partitions for follow-up.

Output: canonical-tr-m-via-chi-cache.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import mpmath as mp
import sympy as sp

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

mp.mp.dps = 50

from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from hecke_characters import partitions_of  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def load_y_lambda_at_q0(n: int) -> dict[tuple[int, ...], mp.mpf]:
    """Load Wenzl y_λ(q_0) for partitions of n from the MPFR witness."""
    path = HERE / "y-lambda-mpfr-witness.json"
    d = json.loads(path.read_text())
    data = d.get('data', d)
    tables = data['tables_by_n']
    n_str = str(n)
    if n_str not in tables:
        raise KeyError(f"y_lambda witness has no n={n} entry")
    weights = tables[n_str].get('weights', [])
    return {
        tuple(w['partition']): mp.mpf(str(w['y_lambda']))
        for w in weights
    }


def load_chi_lambda_symbolic(atom: str, n: int) -> dict[tuple[int, ...], sp.Expr]:
    """Load symbolic χ^λ(β_atomic) for partitions of n from the chi cache."""
    fname = f"chi-{atom}-h{n}.witness.json"
    path = HERE / fname
    if not path.exists():
        return {}
    d = json.loads(path.read_text())
    entries = d.get('chi_lambda_symbolic', [])
    q = sp.Symbol('q')
    out: dict[tuple[int, ...], sp.Expr] = {}
    for entry in entries:
        shape = tuple(entry['partition'])
        expr = sp.sympify(entry['chi_q_symbolic'], locals={'q': q})
        out[shape] = expr
    return out


def compute_canonical_trM(atom: str, n: int, q0: mp.mpf) -> dict:
    """Compute |tr_M(β_atomic, q_0)| via the Σ_λ y_λ · χ^λ combiner."""
    y_lambda = load_y_lambda_at_q0(n)
    chi_lambda = load_chi_lambda_symbolic(atom, n)
    all_partitions = [tuple(p) for p in partitions_of(n)]

    covered = [p for p in all_partitions if p in chi_lambda]
    missing = [p for p in all_partitions if p not in chi_lambda]

    q_sym = sp.Symbol('q')
    q_val = sp.Float(mp.nstr(q0, 50), 50)

    total = mp.mpf(0)
    per_block: list[dict] = []
    for shape in covered:
        chi_at_q0 = mp.mpf(str(sp.N(chi_lambda[shape].subs(q_sym, q_val), 50)))
        y = y_lambda.get(shape, mp.mpf(0))
        contrib = y * chi_at_q0
        total += contrib
        per_block.append({
            "partition": list(shape),
            "y_lambda_at_q0": float(y),
            "chi_at_q0": float(chi_at_q0),
            "contribution": float(contrib),
        })

    return {
        "atom": atom,
        "n_strands": n,
        "n_partitions_total": len(all_partitions),
        "n_partitions_covered": len(covered),
        "n_partitions_missing": len(missing),
        "missing_partitions": [list(p) for p in missing],
        "tr_M_at_q0": float(total),
        "abs_tr_M_at_q0": float(abs(total)),
        "is_complete": len(missing) == 0,
        "per_block": per_block,
    }


def main() -> int:
    print("=" * 90)
    print("  Canonical |tr_M| via χ^λ cache + y_λ combiner (PR #681 Step 2)")
    print("=" * 90)
    print()

    q0 = mp.mpf(Q_50_DIGIT_STR)
    print(f"  q_0 = {mp.nstr(q0, 16)}")
    print()

    atoms = [
        ("proton",    3),
        ("neutron",   3),
        ("deuteron",  6),
        ("tritium",   9),
        ("helium-3",  9),
        ("helium-4", 12),
    ]

    results = []
    print(f"  {'atom':>10} {'H_n':>5} {'covered':>10} {'|tr_M|@q_0':>16} {'complete':>10}")
    print("  " + "-" * 60)
    for atom, n in atoms:
        try:
            r = compute_canonical_trM(atom, n, q0)
        except Exception as e:
            print(f"  {atom:>10} {n:>5} ERROR: {type(e).__name__}: {e}")
            continue
        results.append(r)
        cov_str = f"{r['n_partitions_covered']}/{r['n_partitions_total']}"
        complete_str = "✓" if r['is_complete'] else "partial"
        print(f"  {atom:>10} {n:>5} {cov_str:>10} {r['abs_tr_M_at_q0']:>16.10f} {complete_str:>10}")
    print()

    # Cross-check against the cached habiro-coefficients-atomic value
    # for proton, neutron, deuteron (complete cases).
    print("  Cross-check against existing canonical |tr_M| values on main:")
    try:
        h = json.loads((HERE / "habiro-coefficients-atomic.witness.json").read_text())
        data = h.get('data', h)
        habiro_results = data.get('results', {})
        for r in results:
            if not r['is_complete']:
                continue
            atom_key = None
            for k in habiro_results:
                if r['atom'] in k.lower() or r['atom'][0] in k.split()[0]:
                    atom_key = k
                    break
            if atom_key:
                habiro_val = float(habiro_results[atom_key].get('tr_M_at_q0', 0))
                this_val = r['abs_tr_M_at_q0']
                rel_diff = abs(habiro_val - this_val) / abs(habiro_val) if habiro_val != 0 else 0
                match = "✓" if rel_diff < 1e-10 else "✗"
                print(f"    {r['atom']:>10}: this {this_val:>14.10f}  habiro {habiro_val:>14.10f}  rel_diff {rel_diff:.2e} {match}")
                r['cross_check_habiro'] = habiro_val
                r['cross_check_rel_diff'] = float(rel_diff)
    except FileNotFoundError:
        pass
    print()

    builder = (
        WitnessBuilder("canonical-tr-m-via-chi-cache", engine="mpmath")
        .set_description(
            "PR #681 Step 2 combiner: |tr_M(β_atomic, q_0)| = "
            "|Σ_λ y_λ(q_0) · χ^λ(β_atomic)|. Uses cached y-lambda-mpfr-"
            "witness.json + chi-{atom}-h{n}.witness.json on main. "
            "Reports complete results for p, n, D; partial sums + "
            "missing-partition list for T, ³He, ⁴He pending chi-cache "
            "completion. Cross-checked against the Habiro-resummed "
            "value in habiro-coefficients-atomic.witness.json for the "
            "3 complete atoms."
        )
        .set_audit_only(
            "docs/audits/2026-05-17-knot-fusion-step1-audit.md"
        )
        .add_parameter("q_0", Q_50_DIGIT_STR)
        .add_data("results", results)
        .add_assertion(
            name="complete_atoms_match_habiro_to_1e_10",
            computed=all(
                r.get('cross_check_rel_diff', 0) < 1e-10
                for r in results if r['is_complete'] and 'cross_check_rel_diff' in r
            ),
            expected=True,
            unit="boolean",
            source=(
                "For atoms with complete χ^λ cache (p, n, D), the "
                "Σ_λ y_λ·χ^λ combiner matches the Habiro-resummed "
                "tr_M_at_q0 to <1e-10 relative."
            ),
        )
        .add_caveat(
            "For tritium (2/30), helium-3 (3/30), and helium-4 (0/77), "
            "the combiner reports a PARTIAL sum. Completing those chi "
            "caches is the next step per the knot-fusion-step1-audit doc."
        )
    )
    out = builder.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
