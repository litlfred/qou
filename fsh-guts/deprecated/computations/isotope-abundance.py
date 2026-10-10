#!/usr/bin/env python3
# polynomial_q_not_applicable: library / no own witness output; sympy used internally by callers.
"""
Isotope abundance predictions from Skein polynomial ratios.

Theory: For a fixed element (proton number Z), the relative stability
of isotope (Z, N) is governed by the magnitude of its nuclear Skein
polynomial P_N(q).  Larger |P_N(q₀)| → more stable → more abundant.

Four weighting models are compared:
  - Born rule:       w_N = |P_N|²         (abundance ∝ |P_N|² / Σ|P_N|²)
  - Boltzmann:       w_N = |P_N|          (abundance ∝ |P_N| / Σ|P_N|)
  - Per-nucleon:     w_N = |P_N|^{1/A}    (geometric mean per crossing)
  - Density:         w_N = |P_N|/|P_{ref}| where P_{ref} is linear fit

Since ln|P| grows monotonically with A, the raw Born/Boltzmann models
always favor heavier isotopes.  The per-nucleon model normalizes out
the A-dependence, and the density model looks at deviations from the
expected growth rate.

Usage:
    cd computations
    python3 isotope-abundance.py
"""

import math
import time
from transfer_matrix_symbolic import skein_ln_numeric, Q0

# ---------------------------------------------------------------------------
# Experimental natural abundances (approximate, in %)
# Source: IUPAC / NUBASE evaluations
# ---------------------------------------------------------------------------

# Format: EXPERIMENTAL[Z] = {N: (isotope_name, abundance_%)}
# Only include isotopes with measurable natural abundance.
EXPERIMENTAL = {
    1: {  # Hydrogen
        0: ("¹H",   99.9855),
        1: ("²H",    0.0145),
    },
    2: {  # Helium
        1: ("³He",   0.000137),
        2: ("⁴He",  99.999863),
    },
    3: {  # Lithium
        3: ("⁶Li",   7.59),
        4: ("⁷Li",  92.41),
    },
    4: {  # Beryllium
        5: ("⁹Be", 100.0),
    },
    5: {  # Boron
        5: ("¹⁰B",  19.9),
        6: ("¹¹B",  80.1),
    },
    6: {  # Carbon
        6: ("¹²C",  98.93),
        7: ("¹³C",   1.07),
    },
    7: {  # Nitrogen
        7: ("¹⁴N",  99.636),
        8: ("¹⁵N",   0.364),
    },
    8: {  # Oxygen
        8: ("¹⁶O",  99.757),
        9: ("¹⁷O",   0.038),
        10: ("¹⁸O",  0.205),
    },
}

ELEMENT_NAMES = {
    1: "H", 2: "He", 3: "Li", 4: "Be",
    5: "B", 6: "C", 7: "N", 8: "O",
}


def compute_ln_skein(Z, N_min, N_max, q_val):
    """Compute ln|P_N(q)| for all N in [N_min, N_max].

    Returns dict {N: (ln_abs_P, sign)}.
    Uses purely numeric computation via skein_ln_numeric.
    """
    results = {}
    for N in range(N_min, N_max + 1):
        if Z + N < 1:
            continue  # skip A=0
        try:
            ln_abs, sgn = skein_ln_numeric(Z, N, q_val)
            results[N] = (ln_abs, sgn)
        except Exception as e:
            # Some exotic combinations may fail; skip gracefully
            results[N] = (float('-inf'), 1)
    return results


def _softmax(score_dict, temperature=1.0):
    """Softmax normalization with temperature scaling.

    score_dict: {N: score}. Returns {N: fraction} summing to 1.
    """
    vals = {N: s for N, s in score_dict.items() if s > float('-inf')}
    if not vals:
        return {N: 0.0 for N in score_dict}
    max_s = max(vals.values())
    weights = {}
    for N, s in score_dict.items():
        if s > float('-inf'):
            weights[N] = math.exp((s - max_s) / temperature)
        else:
            weights[N] = 0.0
    total = sum(weights.values())
    if total == 0:
        return weights
    return {N: w / total for N, w in weights.items()}


def normalize_born(ln_abs_dict, Z):
    """Born-rule weighting: abundance ∝ |P|² = exp(2·ln|P|)."""
    scores = {N: 2.0 * lp for N, (lp, _) in ln_abs_dict.items()}
    return _softmax(scores)


def normalize_boltzmann(ln_abs_dict, Z):
    """Boltzmann weighting: abundance ∝ |P| = exp(ln|P|)."""
    scores = {N: lp for N, (lp, _) in ln_abs_dict.items()}
    return _softmax(scores)


def normalize_per_nucleon(ln_abs_dict, Z):
    """Per-nucleon weighting: abundance ∝ |P|^{2/A} = exp(2·ln|P|/A).

    This normalizes out the monotonic growth of ln|P| with A.
    The quantity ln|P|/A is the "Skein density" -- log-magnitude per crossing.
    We use the squared version (Born analog) for sharper discrimination.
    """
    scores = {}
    for N, (lp, _) in ln_abs_dict.items():
        A = Z + N
        if A > 0 and lp > float('-inf'):
            scores[N] = 2.0 * lp / A
        else:
            scores[N] = float('-inf')
    return _softmax(scores)


def normalize_density(ln_abs_dict, Z):
    """Density weighting: look at deviations of ln|P| from a linear fit in A.

    Fit ln|P| ~ alpha * A + beta across all isotopes of this element.
    The residual delta_N = ln|P_N| - (alpha * A_N + beta) measures
    whether isotope N is over- or under-stabilized relative to trend.
    Abundance ∝ exp(2 * delta_N).
    """
    points = []
    for N, (lp, _) in ln_abs_dict.items():
        if lp > float('-inf'):
            A = Z + N
            points.append((A, lp, N))
    if len(points) < 2:
        return {N: 1.0 / len(ln_abs_dict) for N in ln_abs_dict}

    # Linear regression: ln|P| = alpha * A + beta
    n = len(points)
    sum_A = sum(p[0] for p in points)
    sum_lp = sum(p[1] for p in points)
    sum_A2 = sum(p[0] ** 2 for p in points)
    sum_Alp = sum(p[0] * p[1] for p in points)

    denom = n * sum_A2 - sum_A ** 2
    if abs(denom) < 1e-30:
        return {N: 1.0 / len(ln_abs_dict) for N in ln_abs_dict}

    alpha = (n * sum_Alp - sum_A * sum_lp) / denom
    beta = (sum_lp - alpha * sum_A) / n

    scores = {}
    for N, (lp, _) in ln_abs_dict.items():
        A = Z + N
        if lp > float('-inf'):
            expected = alpha * A + beta
            scores[N] = 2.0 * (lp - expected)  # residual, Born-squared
        else:
            scores[N] = float('-inf')

    return _softmax(scores)


def main():
    t_start = time.time()
    q_val = Q0
    print(f"Isotope Abundance from Skein Polynomial Ratios")
    print(f"q₀ = {q_val}")
    print(f"Using purely numeric computation (no sympy)")
    print(f"=" * 100)

    # Collect all results for summary
    all_results = []

    for Z in range(1, 9):
        elem = ELEMENT_NAMES[Z]
        exp_data = EXPERIMENTAL.get(Z, {})

        # Range of neutron numbers to scan
        # N=0 is needed for protium (¹H), so use max(0, Z-2)
        N_min = max(0, Z - 2)
        N_max = Z + 4

        # Compute Skein magnitudes
        ln_dict = compute_ln_skein(Z, N_min, N_max, q_val)

        # Normalize under all four models
        born = normalize_born(ln_dict, Z)
        boltz = normalize_boltzmann(ln_dict, Z)
        pernuc = normalize_per_nucleon(ln_dict, Z)
        density = normalize_density(ln_dict, Z)

        print(f"\n  Z={Z}  {elem}  (N scanned: {N_min}..{N_max})")
        hdr = f"  {'A':>4}  {'Isotope':>8}  {'ln|P|':>10}  {'ln|P|/A':>8}  {'Born%':>7}  {'Boltz%':>7}  {'PerNuc%':>8}  {'Dens%':>7}  {'Expt%':>8}"
        print(hdr)
        print(f"  {'─'*4}  {'─'*8}  {'─'*10}  {'─'*8}  {'─'*7}  {'─'*7}  {'─'*8}  {'─'*7}  {'─'*8}")

        for N in range(N_min, N_max + 1):
            if N not in ln_dict:
                continue
            A = Z + N
            ln_abs, sgn = ln_dict[N]

            # Isotope name from experimental data, or generic
            if N in exp_data:
                iso_name, exp_pct = exp_data[N]
            else:
                iso_name = f"A={A}"
                exp_pct = None

            born_pct = born.get(N, 0.0) * 100
            boltz_pct = boltz.get(N, 0.0) * 100
            pernuc_pct = pernuc.get(N, 0.0) * 100
            dens_pct = density.get(N, 0.0) * 100

            ln_str = f"{ln_abs:10.4f}" if ln_abs > float('-inf') else "    -inf   "
            lnA_str = f"{ln_abs/A:8.5f}" if (ln_abs > float('-inf') and A > 0) else "     -  "
            exp_str = f"{exp_pct:8.4f}" if exp_pct is not None else "      -"

            print(f"  {A:4d}  {iso_name:>8}  {ln_str}  {lnA_str}  {born_pct:7.3f}  {boltz_pct:7.3f}  {pernuc_pct:8.3f}  {dens_pct:7.3f}  {exp_str}")

            if exp_pct is not None:
                all_results.append({
                    'elem': elem, 'A': A, 'N': N, 'Z': Z,
                    'name': iso_name,
                    'ln_abs': ln_abs,
                    'born_pct': born_pct,
                    'boltz_pct': boltz_pct,
                    'pernuc_pct': pernuc_pct,
                    'dens_pct': dens_pct,
                    'exp_pct': exp_pct,
                })

    # Summary: comparison of all models
    print(f"\n{'=' * 100}")
    print(f"Summary: Predicted vs Experimental for known stable isotopes")
    print(f"{'=' * 100}")
    print(f"\n{'Iso':>5}  {'ln|P|':>10}  {'Born%':>7}  {'PerNuc%':>8}  {'Dens%':>7}  {'Expt%':>8}  {'Born':>7}  {'PerNuc':>7}  {'Dens':>7}")
    print(f"{'─'*5}  {'─'*10}  {'─'*7}  {'─'*8}  {'─'*7}  {'─'*8}  {'─'*7}  {'─'*7}  {'─'*7}")

    model_errors = {'born': [], 'pernuc': [], 'density': []}

    for r in all_results:
        ln_str = f"{r['ln_abs']:10.4f}" if r['ln_abs'] > float('-inf') else "    -inf   "
        err_b = r['born_pct'] - r['exp_pct']
        err_p = r['pernuc_pct'] - r['exp_pct']
        err_d = r['dens_pct'] - r['exp_pct']
        model_errors['born'].append(err_b ** 2)
        model_errors['pernuc'].append(err_p ** 2)
        model_errors['density'].append(err_d ** 2)
        print(f"{r['name']:>5}  {ln_str}  {r['born_pct']:7.3f}  {r['pernuc_pct']:8.3f}  {r['dens_pct']:7.3f}  {r['exp_pct']:8.3f}  {err_b:+7.2f}  {err_p:+7.2f}  {err_d:+7.2f}")

    n = len(all_results)
    if n > 0:
        print(f"\nRMSE (percentage points):")
        for name, errs in model_errors.items():
            rmse = math.sqrt(sum(errs) / n)
            print(f"  {name:>12}: {rmse:.2f}")

    # Check if dominant isotope is correctly predicted
    print(f"\nDominant isotope prediction (most abundant isotope per element):")
    print(f"  {'Elem':>4}  {'Expt':>6}  {'Born':>6}  {'PerNuc':>8}  {'Density':>9}")
    print(f"  {'─'*4}  {'─'*6}  {'─'*6}  {'─'*8}  {'─'*9}")

    model_correct = {'born': 0, 'pernuc': 0, 'density': 0}
    total_elements = 0

    for Z in range(1, 9):
        elem = ELEMENT_NAMES[Z]
        exp_data = EXPERIMENTAL.get(Z, {})
        if not exp_data:
            continue

        # Find experimentally dominant
        exp_dominant_N = max(exp_data, key=lambda n: exp_data[n][1])

        # Compute predictions
        N_min = max(0, Z - 2)
        N_max = Z + 4
        ln_dict = compute_ln_skein(Z, N_min, N_max, q_val)

        models = {
            'born': normalize_born(ln_dict, Z),
            'pernuc': normalize_per_nucleon(ln_dict, Z),
            'density': normalize_density(ln_dict, Z),
        }

        total_elements += 1
        exp_A = Z + exp_dominant_N

        parts = [f"  {elem:>4}  A={exp_A:>2}"]
        for mname in ['born', 'pernuc', 'density']:
            pred_N = max(models[mname], key=models[mname].get)
            pred_A = Z + pred_N
            ok = pred_N == exp_dominant_N
            if ok:
                model_correct[mname] += 1
            mark = "ok" if ok else "  "
            w = 6 if mname == 'born' else (8 if mname == 'pernuc' else 9)
            parts.append(f"{'A='+str(pred_A)+' '+mark:>{w}}")
        print("  ".join(parts))

    print()
    for mname in ['born', 'pernuc', 'density']:
        print(f"  {mname:>12} correct: {model_correct[mname]}/{total_elements}")

    # Model 5: Restrict competition to experimentally known isotopes only
    print(f"\n{'=' * 100}")
    print(f"Model 5: Born rule restricted to experimentally known isotopes only")
    print(f"(Only stable isotopes compete; no exotic A values in normalization)")
    print(f"{'=' * 100}")

    model5_errors = []
    model5_correct = 0

    for Z in range(1, 9):
        elem = ELEMENT_NAMES[Z]
        exp_data = EXPERIMENTAL.get(Z, {})
        if not exp_data:
            continue

        # Compute Skein only for experimentally known N values
        ln_known = {}
        for N in exp_data:
            ln_abs, sgn = skein_ln_numeric(Z, N, q_val)
            ln_known[N] = (ln_abs, sgn)

        # Born-rule among known isotopes
        born_known = normalize_born(ln_known, Z)

        print(f"\n  {elem} (Z={Z}):")
        exp_dominant_N = max(exp_data, key=lambda n: exp_data[n][1])
        pred_dominant_N = max(born_known, key=born_known.get)

        for N in sorted(exp_data):
            A = Z + N
            iso_name, exp_pct = exp_data[N]
            pred_pct = born_known.get(N, 0.0) * 100
            ln_abs, _ = ln_known[N]
            err = pred_pct - exp_pct
            model5_errors.append(err ** 2)
            print(f"    {iso_name:>5}  A={A:2d}  ln|P|={ln_abs:10.4f}  pred={pred_pct:8.3f}%  expt={exp_pct:8.4f}%  err={err:+8.3f}")

        ok = pred_dominant_N == exp_dominant_N
        if ok:
            model5_correct += 1
        mark = "correct" if ok else f"WRONG (pred A={Z+pred_dominant_N})"
        print(f"    Dominant: A={Z+exp_dominant_N} {mark}")

    rmse5 = math.sqrt(sum(model5_errors) / len(model5_errors)) if model5_errors else 0
    print(f"\n  RMSE: {rmse5:.2f} pp")
    print(f"  Dominant correct: {model5_correct}/8")

    # Model 6: Ratio of adjacent isotopes ln|P_{N+1}|/ln|P_N|
    print(f"\n{'=' * 100}")
    print(f"Model 6: Adjacent Skein ratio -- ln|P(Z,N)| - ln|P(Z,N-1)| (marginal stability)")
    print(f"(Adding one neutron: how much does the Skein magnitude grow?)")
    print(f"{'=' * 100}")

    for Z in range(1, 9):
        elem = ELEMENT_NAMES[Z]
        exp_data = EXPERIMENTAL.get(Z, {})

        N_min = max(0, Z - 2)
        N_max = Z + 4
        ln_dict = compute_ln_skein(Z, N_min, N_max, q_val)

        print(f"\n  {elem} (Z={Z}):")
        prev_lp = None
        for N in range(N_min, N_max + 1):
            if N not in ln_dict:
                prev_lp = None
                continue
            A = Z + N
            lp, _ = ln_dict[N]
            if prev_lp is not None and lp > float('-inf') and prev_lp > float('-inf'):
                delta = lp - prev_lp
            else:
                delta = None

            marker = ""
            if N in exp_data:
                marker = f" <-- {exp_data[N][0]}"

            if delta is not None:
                delta_str = f"delta={delta:+8.4f}"
            else:
                delta_str = "delta=     N/A"

            print(f"    A={A:2d}  ln|P|={lp:10.4f}  {delta_str}{marker}")
            prev_lp = lp

    # Additional analysis: Skein density (ln|P|/A) vs A plot data
    print(f"\n{'=' * 100}")
    print(f"Skein density profile: ln|P|/A vs A for each element")
    print(f"(Peaks in this quantity should correlate with stability)")
    print(f"{'=' * 100}")

    for Z in range(1, 9):
        elem = ELEMENT_NAMES[Z]
        exp_data = EXPERIMENTAL.get(Z, {})

        N_min = max(0, Z - 2)
        N_max = Z + 4
        ln_dict = compute_ln_skein(Z, N_min, N_max, q_val)

        print(f"\n  {elem} (Z={Z}):")
        best_A = None
        best_density = float('-inf')

        for N in range(N_min, N_max + 1):
            if N not in ln_dict:
                continue
            A = Z + N
            lp, _ = ln_dict[N]
            if lp <= float('-inf') or A == 0:
                continue
            d = lp / A
            if d > best_density:
                best_density = d
                best_A = A

            # Find if this is an experimentally known isotope
            marker = ""
            if N in exp_data:
                marker = f" <-- {exp_data[N][0]} ({exp_data[N][1]:.2f}%)"

            # Simple bar chart
            bar_len = max(0, int((d - 0.0) * 40))
            bar = "█" * bar_len
            print(f"    A={A:2d}  ln|P|/A={d:.5f}  {bar}{marker}")

        exp_dom_N = max(exp_data, key=lambda n: exp_data[n][1]) if exp_data else None
        exp_dom_A = Z + exp_dom_N if exp_dom_N is not None else None
        ok_str = " (matches)" if best_A == exp_dom_A else f" (expt: A={exp_dom_A})"
        print(f"    Peak density at A={best_A}{ok_str}")

    elapsed = time.time() - t_start
    print(f"\nTotal runtime: {elapsed:.2f}s")


if __name__ == "__main__":
    main()
