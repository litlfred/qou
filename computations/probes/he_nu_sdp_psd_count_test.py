#!/usr/bin/env python3
"""Per-block-PSD count is NOT ν_SDP — REFUTED by T (8_11) at H₅.

EXPLORATORY — derive-or-refute, no fit. Follow-up to the #2552 finding that no
solver computes ν_SDP (= ρ_F, the magic-A prefactor); the confirmed D/T/³He =
1, 2, 2 were hardcoded ("manual-historical-volume-match").

Tested candidate operational definition:

  CANDIDATE:  ν_SDP(K_w) = #{ λ ⊢ n, λ ≠ (n) : ρ_λ(T_w) PSD }
              (symmetric part (M+Mᵀ)/2 ⪰ 0; trivial rep (n) excluded — it is
               q^{writhe} > 0, always positive, never an informative channel).

Computed in the CANONICAL ORTHOGONAL Hoefsmit seminormal form
(`hoefsmit_numpy.hoefsmit_matrices_numpy`, the principled basis where ρ_λ(σ_i) is
symmetric) for the three confirmed atoms — including T (8_11) at H₅, the first
out-of-sample test at a NEW strand count:

  | atom | knot | n | non-trivial PSD blocks        | ν_pred | ν_canon |
  |------|------|---|-------------------------------|-------:|--------:|
  | D    | 6_2  | 3 | {(1,1,1)}                     | 1      | 1  ✓    |
  | ³He  | L6a4 | 3 | {(2,1), (1,1,1)}              | 2      | 2  ✓    |
  | T    | 8_11 | 5 | {(1,1,1,1,1)} only            | 1      | 2  ✗    |

**Verdict: REFUTED.** The rule reproduces the two B₃ atoms (D, ³He) but FAILS the
out-of-sample H₅ atom T: only the fully-antisymmetric sign rep (1⁵) is PSD; all
five higher-dimensional non-trivial blocks ((4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1))
are indefinite, giving ν_pred = 1 ≠ 2. The 2-point B₃ agreement was coincidental.

(Note: "exclude trivial" ≡ "(#PSD)−1" identically — the trivial rep is q^{writhe}>0
for any braid, so it is always PSD; there was never a second reading to discriminate.)

**Implication.** ν_SDP is NOT "count the per-block-PSD-feasible Wedderburn blocks of
ρ_λ(T_w)". The actual object is the operator-SELECTION SDP (an objective t + Frobenius
Gram G + target n_target, per `lp_dual_solver.solve_psd_operator_selection_sdp`),
whose saturating set is the multiplicity — not a per-block sign test. No per-atom
(t, G, n_target) spec that reproduces 1, 2, 2 exists in the corpus, so the #2552
core finding stands and is sharpened: the obvious per-block-PSD shortcut is refuted.

Hoefsmit matrices via the canonical numpy producer (arbitrary n). q₀ inlined.

Output: he-nu-sdp-psd-count-test.witness.json
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))            # computations/ on path for hoefsmit_numpy
from hoefsmit_numpy import hoefsmit_matrices_numpy  # noqa: E402

# Canonical substrate q₀ (proton-pinned; == computations/q_parameter.Q), inlined.
Q0 = 1.1099785955573347
H = Q0 - 1.0 / Q0
TOL = 1e-9

# Confirmed atoms: canonical braid words (1-based generators; sign = inverse) + ν_SDP.
ATOMS = {
    "D":   {"knot": "6_2",  "word": [1, -2, 1, 1, 1, -2],   "nu": 1},
    "3He": {"knot": "L6a4", "word": [-1, 2, -1, 2, -1, 2],  "nu": 2},
    "T":   {"knot": "8_11", "word": [-1, 2, -3, 2, 1, -3, -3, 4, -3, -2, -3, -4, -3, 2],
            "nu": 2},
}


def _partitions(n, mx=None):
    if mx is None:
        mx = n
    if n == 0:
        yield ()
        return
    for f in range(min(n, mx), 0, -1):
        for r in _partitions(n - f, f):
            yield (f,) + r


def _rho_word(shape, word):
    mats, dim = hoefsmit_matrices_numpy(shape, Q0)
    if dim == 0:
        return None, 0
    eye = np.eye(dim)
    M = np.eye(dim)
    for i in word:
        s = mats[abs(i) - 1]                       # 1-based gen → 0-based matrix
        M = M @ (s if i > 0 else (s - H * eye))    # σ⁻¹ = σ − h
    return M, dim


def main() -> int:
    print("=" * 84)
    print("  Per-block-PSD count vs ν_SDP — canonical ORTHOGONAL Hoefsmit form  "
          f"q₀={Q0:.8f}")
    print("  candidate: ν = #{ λ≠(n) : ρ_λ(T_w) sym-part PSD }")
    print("=" * 84)
    rows = []
    verdict_ok = True
    for name, info in ATOMS.items():
        word = info["word"]
        n = max(abs(i) for i in word) + 1
        blocks = []
        nontriv_psd = []
        for lam in _partitions(n):
            M, dim = _rho_word(lam, word)
            emin = float(np.linalg.eigvalsh((M + M.T) / 2.0).min())
            psd = emin >= -TOL
            triv = (lam == (n,))
            if psd and not triv:
                nontriv_psd.append(lam)
            blocks.append({"lambda": list(lam), "dim": dim,
                           "min_eig_sym": emin, "psd": bool(psd), "trivial": bool(triv)})
        nu_pred = len(nontriv_psd)
        ok = (nu_pred == info["nu"])
        verdict_ok = verdict_ok and ok
        print(f"\n  {name} ({info['knot']}, n={n}):  non-triv PSD = "
              f"{[tuple(b['lambda']) for b in blocks if b['psd'] and not b['trivial']]}"
              f"  ν_pred={nu_pred}  canonical={info['nu']}  {'✓' if ok else '✗ MISMATCH'}")
        for b in blocks:
            t = " [triv,excl]" if b["trivial"] else (" *PSD*" if b["psd"] else "")
            print(f"      λ={str(tuple(b['lambda'])):<16} d={b['dim']:<2} "
                  f"min_eig(sym)={b['min_eig_sym']:+.5f} "
                  f"{'PSD' if b['psd'] else 'neg'}{t}")
        rows.append({"atom": name, **info, "n": n, "blocks": blocks,
                     "nu_predicted": nu_pred, "match": ok})

    refuted = not verdict_ok
    print("\n" + "=" * 84)
    print(f"  VERDICT: {'REFUTED' if refuted else 'consistent'} — per-block-PSD count "
          f"{'≠' if refuted else '='} canonical ν_SDP.")
    if refuted:
        print("  Reproduces D=1, ³He=2 (B₃) but FAILS T=1≠2 (8_11, H₅, first out-of-sample).")
        print("  ⇒ ν_SDP is NOT a per-block PSD sign test; it needs the operator-selection")
        print("    SDP (objective + Frobenius Gram). #2552 finding stands & sharpened.")
    print("=" * 84)

    witness = {
        "computation": "he-nu-sdp-psd-count-test",
        "kind": "exploratory-probe",
        "description": (
            "Tests whether ν_SDP = #{non-trivial Wedderburn blocks λ≠(n) with ρ_λ(T_w) "
            "PSD} reproduces the confirmed D/T/³He = 1,2,2. Canonical orthogonal Hoefsmit "
            "form. REFUTED: matches D,³He (B₃) but T (8_11,H₅) gives 1≠2. The per-block-PSD "
            "shortcut is not ν_SDP; the operator-selection SDP is needed. No fit."
        ),
        "engine": "numpy", "q0": Q0,
        "candidate_definition": "nu = #{ lambda != (n) : rho_lambda(T_w) sym-part PSD }",
        "atoms": rows,
        "verdict": "REFUTED" if refuted else "consistent",
        "refutation_atom": "T (8_11, H_5): nu_pred=1 != canonical 2",
        "note": ("'exclude trivial' == '(#PSD)-1' identically (trivial rep = q^writhe > 0 "
                 "always PSD). The real ν_SDP is the operator-selection SDP saturating-set "
                 "multiplicity (t, G, n_target); no per-atom spec reproducing 1,2,2 exists."),
        "refs": ["PR #2552 (no-solver-computes-nu_SDP)",
                 "computations/hoefsmit_numpy.py (canonical orthogonal seminormal)",
                 "computations/lp_dual_solver.py (operator-selection SDP)"],
        "discipline": "EXPLORATORY — derive-or-refute, no fit, no forced ⁴He number.",
    }
    out = HERE.parent / "he-nu-sdp-psd-count-test.witness.json"
    out.write_text(json.dumps(witness, indent=2, ensure_ascii=False) + "\n")
    print(f"  witness: {out}")
    return 0   # a clean refutation is a successful probe outcome


if __name__ == "__main__":
    raise SystemExit(main())
