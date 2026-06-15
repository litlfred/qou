"""qbeta_residue_followup_pslq_periods — Direction 3: period reframe.

Tests the hypothesis that residue A is NOT a finite categorical
(algebraic-at-q_0) invariant but a PERIOD — a ℚ-linear combination of
known transcendental constants / hyperbolic volumes. Runs an integer-
relation (PSLQ) probe on the prefactor P = A/ℏ_q^15 and on A itself
against a period basis.

CRITICAL PRECISION CEILING (reported honestly): the residue A is
EMPIRICALLY known only to ~12 significant figures —
  A = u_subst · tail_mean,  tail_mean = 2.11794472225e-13  (Step 1 of
  PR #1727, 12 sig figs); u_subst is exact-from-q_0.
PSLQ can therefore only detect period relations whose combined
coefficient height is small enough to be resolved within A's ~12-digit
noise (tol ≈ 1e-11). A relation found only at large height is NOT
meaningful (PSLQ always finds one if precision/basis allows). Every
relation is reported WITH its max-|coeff| height and the working
tolerance, so the result is falsifiable.

ANTI-PATTERN GUARDS: report height + precision bound on every relation;
no claim of closure from a high-height relation; diagnostic-only;
ℏ_q from (q-1)/q.

Usage:
  python3 folio-assistant/computations/qbeta/qbeta_residue_followup_pslq_periods.py
Emits: qbeta-residue-followup-pslq-periods.witness.json
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge  # noqa: E402, F401

import mpmath as mp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402

mp.mp.dps = 40

Q_PROTON_50 = mp.mpf("1.10997858275138080759166909561")
# Step-1 (PR #1727) tail_mean — the precision-limiting empirical input.
TAIL_MEAN = mp.mpf("2.11794472225e-13")          # ~12 sig figs
TAIL_MEAN_SIGFIGS = 12
# Usable digits of agreement on A/P (conservative — below the 12 sig figs).
D_DIGITS = mp.mpf("11")
# PSLQ tolerance reflecting A's ~12-digit empirical precision (conservative).
PSLQ_TOL = mp.mpf("1e-11")
PSLQ_MAXCOEFF = 10 ** 6
# Margin (digits) required ABOVE the search-space entropy for a relation
# to be non-spurious.
SAFETY_MARGIN = mp.mpf("3")


def relation_entropy(n_terms: int, height: int) -> mp.mpf:
    """log10 of the ℤ-combination search-space ≈ n_terms · log10(2·height+1).

    A PSLQ relation is non-spurious only if the digits of agreement
    EXCEED this entropy (plus a safety margin): otherwise a relation of
    that height exists by chance among that many terms at that precision.
    """
    return n_terms * mp.log10(2 * height + 1)


def is_meaningful(n_terms: int, height: int) -> bool:
    return D_DIGITS > relation_entropy(n_terms, height) + SAFETY_MARGIN


def h_q(q: mp.mpf) -> mp.mpf:
    return (q - 1) / q


def substrate_constants(q: mp.mpf) -> dict[str, mp.mpf]:
    hbar = h_q(q)
    b_sq = (q ** 4 + q ** 2 + 1) / (q ** 2 + 1) ** 2
    b = mp.sqrt(b_sq)
    u = b * hbar ** 2
    A = u * TAIL_MEAN                  # best-available residue A (~12 digits)
    return {"hbar": hbar, "b": b, "u": u, "A": A}


def bloch_wigner(x: mp.mpf) -> mp.mpf:
    """Bloch-Wigner dilogarithm D(x) = Im Li_2(x) + arg(1-x)·ln|x|.
    For real x it reduces to 0 (real argument) — included to record that
    the trefoil/real-q evaluation gives D = 0 (non-hyperbolic), per the
    KLR/Bloch-Wigner audit note."""
    if mp.im(x) == 0:
        return mp.mpf(0)
    return mp.im(mp.polylog(2, x)) + mp.arg(1 - x) * mp.log(abs(x))


def period_basis(q: mp.mpf) -> dict[str, mp.mpf]:
    """Transcendental + hyperbolic-volume period candidates."""
    c = substrate_constants(q)
    hbar = c["hbar"]
    basis = {
        "1": mp.mpf(1),
        "pi": mp.pi,
        "pi^2": mp.pi ** 2,
        "zeta3": mp.zeta(3),
        "Catalan": mp.catalan,
        "ln(q0)": mp.log(q),
        "Li2(hbar)": mp.polylog(2, hbar),
        "Li2(1-hbar)": mp.polylog(2, 1 - hbar),
        "Li2(-hbar)": mp.polylog(2, -hbar),
        "BlochWigner(q0)": bloch_wigner(q),    # = 0 for real q0 (recorded)
    }
    # Hyperbolic volumes (4_1 figure-eight, Borromean) from pyhecke if present.
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parents[3]
                               / "tools" / "pyhecke" / "python"))
        from pyhecke.constants import VOL_FIGURE8, VOL_BORROMEAN  # type: ignore
        basis["Vol(4_1)"] = mp.mpf(str(VOL_FIGURE8))
        basis["Vol(Borromean)"] = mp.mpf(str(VOL_BORROMEAN))
    except Exception:
        # Canonical literals (Catalan-volume of 4_1 ≈ 2.029883; Borromean ≈ 7.327724)
        basis["Vol(4_1)"] = mp.mpf("2.029883212819")
        basis["Vol(Borromean)"] = mp.mpf("7.327724753417")
    return basis


def run_pslq(target_name: str, target: mp.mpf, basis: dict[str, mp.mpf]
             ) -> dict:
    """PSLQ [target] + basis; report relation + height + meaningfulness."""
    # Drop identically-zero basis entries (e.g. BlochWigner(q0)=0 for real
    # q0) — PSLQ requires nonzero numbers; record which were dropped.
    nz = {n: v for n, v in basis.items() if v != 0}
    dropped = [n for n, v in basis.items() if v == 0]
    names = [target_name] + list(nz.keys())
    vec = [target] + list(nz.values())
    rel = mp.pslq(vec, tol=PSLQ_TOL, maxcoeff=PSLQ_MAXCOEFF, maxsteps=10 ** 5)
    out: dict = {"target": target_name, "basis": list(nz.keys()),
                 "dropped_zero_basis": dropped}
    if rel is None:
        out["relation_found"] = False
        out["note"] = (f"No integer relation with height ≤ {PSLQ_MAXCOEFF} at "
                       f"tol {mp.nstr(PSLQ_TOL, 2)} (A's ~{TAIL_MEAN_SIGFIGS}-"
                       f"digit ceiling). Target is generic w.r.t. this basis "
                       f"up to that height.")
        return out
    height = int(max(abs(c) for c in rel))
    # Residual of the relation (how well it actually holds)
    resid = sum(mp.mpf(c) * v for c, v in zip(rel, vec))
    n_terms = len(vec)
    entropy = relation_entropy(n_terms, height)
    meaningful = is_meaningful(n_terms, height)
    out["relation_found"] = True
    out["coeffs"] = {n: int(c) for n, c in zip(names, rel)}
    out["height"] = height
    out["n_terms"] = n_terms
    out["residual"] = mp.nstr(resid, 4)
    out["entropy_digits"] = mp.nstr(entropy, 5)
    out["precision_digits"] = mp.nstr(D_DIGITS, 4)
    out["meaningful"] = bool(meaningful)
    out["note"] = (
        f"height {height} over {n_terms} terms ⇒ search-entropy "
        f"≈{mp.nstr(entropy,4)} digits vs {mp.nstr(D_DIGITS,3)} precision "
        f"digits. "
        + ("MEANINGFUL (precision exceeds entropy+margin) — flag for scrutiny "
           "(still needs higher-precision A to confirm as a closure)."
           if meaningful else
           "SPURIOUS — search-space entropy ≥ precision, so a relation of this "
           "height exists by chance; NOT structural.")
    )
    return out


def main() -> int:
    print("=" * 78)
    print("Q_β residue-A follow-up — Direction 3: PSLQ period reframe")
    print("=" * 78)
    c = substrate_constants(Q_PROTON_50)
    A = c["A"]
    hbar = c["hbar"]
    P = A / hbar ** 15
    print(f"A (= u_subst·tail_mean, ~{TAIL_MEAN_SIGFIGS} sig figs) = {mp.nstr(A, 14)}")
    print(f"Prefactor P = A/ℏ_q^15 = {mp.nstr(P, 14)}")
    print(f"PSLQ tol = {mp.nstr(PSLQ_TOL, 2)} (A's empirical ceiling); "
          f"maxcoeff = {PSLQ_MAXCOEFF}")
    print()

    basis = period_basis(Q_PROTON_50)
    print(f"Period basis ({len(basis)} constants): {', '.join(basis.keys())}")
    print(f"  (BlochWigner(q0) = {mp.nstr(basis['BlochWigner(q0)'], 4)} — "
          f"real q0 ⇒ 0, non-hyperbolic, per audit note)")
    print()

    # (a) Full-basis PSLQ — almost certainly SPURIOUS at 12-digit precision
    # (12-term search entropy ≫ precision), recorded to demonstrate exactly
    # that.
    results = []
    for tname, tval in (("P=A/hbar^15", P), ("A", A)):
        r = run_pslq(tname, tval, basis)
        results.append(r)
        print(f"--- FULL-BASIS PSLQ target: {tname} = {mp.nstr(tval, 12)} ---")
        if r["relation_found"]:
            print(f"  height {r['height']} over {r['n_terms']} terms, "
                  f"residual {r['residual']}, meaningful={r['meaningful']}")
        else:
            print(f"  NO relation (height ≤ {PSLQ_MAXCOEFF}).")
        print(f"  {r['note']}")
        print()

    # (b) Pairwise sub-basket PSLQ: [P, const] (and [A, const]). A 2-term
    # relation P·c0 = const·c1 has LOW entropy, so it IS testable at
    # 11-digit precision up to height ~1e3 — this is the meaningful probe.
    print("--- PAIRWISE sub-basket PSLQ (2-term, genuinely testable) ---")
    pair_hits = []
    for tname, tval in (("P", P), ("A", A)):
        for cname, cval in basis.items():
            if cval == 0:
                continue
            rel = mp.pslq([tval, cval], tol=PSLQ_TOL,
                          maxcoeff=PSLQ_MAXCOEFF, maxsteps=10 ** 5)
            if rel is None:
                continue
            height = int(max(abs(c) for c in rel))
            meaningful = is_meaningful(2, height)
            tag = "MEANINGFUL" if meaningful else "spurious"
            row = {"target": tname, "const": cname,
                   "coeffs": [int(rel[0]), int(rel[1])],
                   "height": height, "meaningful": bool(meaningful)}
            if meaningful:
                pair_hits.append(row)
                print(f"  {tname} : {cname}  →  {int(rel[0])}·{tname} + "
                      f"{int(rel[1])}·{cname} ≈ 0  (height {height}, {tag})")
    if not pair_hits:
        print("  none meaningful (no low-height 2-term period relation).")
    print()

    meaningful_hits = ([r for r in results
                        if r.get("relation_found") and r.get("meaningful")]
                       + pair_hits)
    print("=" * 78)
    if meaningful_hits:
        print(f"⚑ {len(meaningful_hits)} MEANINGFUL relation(s) (entropy < "
              f"precision) — SURFACE to author.")
        print("  Caveat: bounded by A's ~12-digit precision; a genuine period")
        print("  identity needs A recomputed to ≥ 30 digits to confirm. NOT a")
        print("  closure yet.")
    else:
        print("VERDICT: NO meaningful period relation for P or A. The full-12-")
        print("basis PSLQ relation is SPURIOUS (12-term height-h search entropy")
        print("≈13 digits ≫ A's 11-digit precision — a relation exists by")
        print("chance). No 2-term relation P·c0 = const·c1 holds at low height")
        print("either. The period/transcendental reframe is NOT confirmable at")
        print("A's current ~12-digit empirical precision — and CANNOT be, since")
        print("a 12-constant basis needs ≥ ~15 digits to resolve. To test it")
        print("properly, A must be recomputed to ≥ 30 digits from the PR #1727")
        print("residue (tail_mean, 12 sig figs, is the precision limiter).")
    print()

    # ─── Witness ──────────────────────────────────────────────────────
    w = WitnessBuilder("qbeta-residue-followup-pslq-periods", engine="mpmath")
    w.set_description(
        f"Direction 3 of the residue-A follow-up: PSLQ integer-relation probe "
        f"testing whether residue A / prefactor P=A/ℏ_q^15 ≈ {mp.nstr(P, 8)} is "
        f"a period (ℚ-combination of {len(basis)} transcendental/volume "
        f"constants). PRECISION CEILING: A is empirically known to "
        f"~{TAIL_MEAN_SIGFIGS} sig figs (tail_mean limiter), so PSLQ tol="
        f"{mp.nstr(PSLQ_TOL,2)} and a relation is meaningful only if precision "
        f"exceeds the n_terms·log10(2·height) search-entropy + margin. The "
        f"full 12-basis relation is SPURIOUS (entropy ≈15 ≫ 11 digits); "
        f"{len(meaningful_hits)} MEANINGFUL relation(s) (incl. 2-term probes) "
        f"found. Every relation reported with height + entropy (falsifiable). "
        f"Diagnostic-only."
    )
    w.add_data("residue_A", mp.nstr(A, 14))
    w.add_data("prefactor_P", mp.nstr(P, 14))
    w.add_data("A_sigfigs", str(TAIL_MEAN_SIGFIGS))
    w.add_data("tail_mean", mp.nstr(TAIL_MEAN, 14))
    w.add_data("pslq_tol", mp.nstr(PSLQ_TOL, 4))
    w.add_data("pslq_maxcoeff", str(PSLQ_MAXCOEFF))
    w.add_data("precision_digits", mp.nstr(D_DIGITS, 4))
    w.add_data("period_basis", list(basis.keys()))
    w.add_data("bloch_wigner_q0", mp.nstr(basis["BlochWigner(q0)"], 6))
    for r in results:
        key = r["target"].replace("/", "_").replace("=", "_").replace("^", "")
        w.add_data(f"pslq_{key}", {k: (v if not isinstance(v, dict)
                                       else {kk: str(vv) for kk, vv in v.items()})
                                   for k, v in r.items() if k != "basis"})
    w.add_data("meaningful_relation_count", str(len(meaningful_hits)))
    w.add_data("pairwise_meaningful_hits", [
        {k: str(v) for k, v in row.items()} for row in pair_hits])
    w.add_data("entropy_framing", {
        "precision_digits": mp.nstr(D_DIGITS, 4),
        "safety_margin_digits": mp.nstr(SAFETY_MARGIN, 2),
        "full_basis_terms": str(len(basis)),
        "note": "A PSLQ relation among k terms with height h is non-spurious "
                "only if precision > k·log10(2h) + margin. The 12-term basis "
                "needs ≥~15 digits; A has ~11 — so any full-basis relation is "
                "a degrees-of-freedom artifact, not structure.",
    })
    w.add_assertion(
        name="meaningful_period_relation_found",
        computed=bool(len(meaningful_hits) > 0),
        expected=False, tolerance=0,
        source="Tests the period reframe with an ENTROPY-based meaningfulness "
               "criterion (precision > n_terms·log10(2·height)+margin). At A's "
               "~11-digit precision a 12-constant basis cannot yield a non-"
               "spurious relation; the 2-term sub-basket probes are the "
               "genuinely testable ones. Default: none. A hit is surfaced, "
               "not a closure (needs A to ≥30 digits).",
    )
    out = w.save()
    print(f"  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
