#!/usr/bin/env python3
"""qbeta_r12_knot_invariant_probe.py — bean j0q8 (T1): is R₁₂ / C(y) a
knot invariant of the net braid, or an isospin crossing-weight artifact?

Context. The Q_β bar-odd carrier's non-cyclotomic residual factors as
num = (q²−1)·R₁₂ with R₁₂/q⁶ = C(y) = y³−4y²+3y−2, y = q²+q⁻²
(`qbeta_r12_trace_variable_probe.py`, PR #3294). C is irreducible over ℚ
with discriminant −152 = −2³·19 — a **non-abelian S₃ cubic field**.

The "net braid" is NOT a single braid: `free-neutron-decay.witness.json`
gives the net decay carrier as the signed H₃ normal-form combination over
the basis {𝟏, σ₀, σ₁, L₊, L₋, e⁻} indexed by knots
{unknot, virtual, virtual, Hopf, Hopf, trefoil}, with the ONLY
neutron-vs-proton difference being the u/d crossing-weight assignment
([u,d,d] vs [u,u,d]; weights u-u = σ, d-d = q²σ−qs·𝟏, u-d = ½(1+q²)σ−½qs·𝟏).

This probe settles T1 with exact checks (and CORRECTS a tempting-but-wrong
argument — see the note on Galois below):

  (A) SINGLE-KNOT test — the primary, decisive one. Compute the Jones
      polynomials of the constituent knots (unknot 0₁, Hopf link, trefoil
      3₁). Each is a short Laurent polynomial (q-span ≤ 4). R₁₂ has q-span
      12 and neither equals nor divides any of them, so R₁₂ is NOT the
      Jones (nor a factor) of any constituent knot.

  (B) NON-KNOT OBJECT. The "net braid" is not a knot closure at all: it is
      the signed isospin DIFFERENCE Δ(neutron[u,d,d]) − Δ(proton[u,u,d]) of
      Hecke-trace amplitudes over the shared H₃ NF basis, where the only
      n-vs-p difference is the u/d crossing-weight assignment (u-d weight
      ½(1+q²)σ − ½qs·𝟏 ∈ ℚ[q²]·σ ⊕ ℚ[q²]·𝟏). R₁₂ is even in q, hence lives
      in ℚ[q²] = ℚ[y], y = q²+q⁻² — the same even sector the crossing
      weights inhabit. So R₁₂ is a Hecke crossing-weight (representation-
      theoretic) object, not a topological invariant of any braid closure.

  NOTE — a Galois argument that does NOT work (recorded to prevent
  re-proposal). One is tempted to argue "C(y) has S₃ (non-abelian) Galois,
  disc −152, whereas knot invariants are cyclotomic (abelian)." The second
  half is FALSE: the trefoil's own reduced Jones cubic (q³−q²−1 in the
  integer-power rep) is likewise non-cyclotomic with an S₃-type field. So
  the S₃ property of C(y) is a true and interesting arithmetic fingerprint
  but does NOT by itself separate R₁₂ from knot invariants; (A)+(B) do. The
  disc −152 = −2³·19 is recorded as structure, not as the separating
  invariant.

Verdict (scope (a) — this construction/comparison): R₁₂ is NOT the knot
invariant of any constituent knot (A), and the net object is not a braid
closure but an isospin crossing-weight difference (B); R₁₂ is therefore a
Hecke crossing-weight object, a cubic C(y)=y³−4y²+3y−2 in the bar-even
trace variable y=q²+q⁻². (Not claimed: that no braid anywhere has R₁₂ as an
invariant — only that it is not a constituent-knot invariant and not
topological in this construction.)

All exact (sympy over ℚ); audit-only; no wiring; nothing fitted.

Emits `qbeta-r12-knot-invariant.witness.json`.

Usage:
    python3 -u qbeta/qbeta_r12_knot_invariant_probe.py 2>&1 | tee /tmp/r12ki.log
"""
from __future__ import annotations

import sys
import json
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import _path_bridge as _pb  # noqa: E402, F401
sys.path.insert(0, str(Path(__file__).resolve().parent))

import sympy as sp  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402
from qbeta_ck_sseries_exact_rational import q, load_net_symbolic  # noqa: E402

y = sp.Symbol("y")
HERE = Path(__file__).resolve().parent


def jones_constituents():
    """Jones polynomials V_K(t) of the constituent knots, standard
    normalization (t = q here for span comparison only). Unknot = 1;
    Hopf link (positive) V = −t^{1/2}−t^{5/2} → in integer powers use
    t→q²: −q−q⁵ (span 4); trefoil V = −t^{−4}+t^{−3}+t^{−1} (span 3).
    We only need spans + cyclotomic factorization, so use integer-power
    representatives."""
    t = q
    return {
        "unknot": sp.Integer(1),
        "Hopf": -t - t**5,                 # positive Hopf, integer-power rep
        "trefoil": -t**4 + t**3 + t,       # (right-handed) integer-power rep
    }


def galois_is_abelian_cubic(poly_y):
    """For an irreducible cubic, Galois group is C₃ iff discriminant is a
    perfect square (in ℚ), else S₃ (non-abelian). Returns (is_abelian,
    disc, is_square)."""
    P = sp.Poly(poly_y, y)
    disc = sp.discriminant(P, y)
    is_square = sp.sqrt(disc).is_rational if disc >= 0 else False
    return (bool(is_square), disc, bool(is_square))


def cyclotomic_content(poly_q):
    """Cyclotomic vs non-cyclotomic irreducible factors of poly (in q)."""
    from sympy import cyclotomic_poly
    cyclo, noncyclo = [], []
    for f, m in sp.factor_list(sp.expand(poly_q))[1]:
        p = sp.Poly(f, q)
        if p.degree() == 0:
            continue
        if p.is_cyclotomic:
            for n in range(1, 6 * p.degree() + 2):
                if sp.Poly(cyclotomic_poly(n, q), q) == p:
                    cyclo.append(n)
                    break
        else:
            noncyclo.append(f)
    return sorted(cyclo), noncyclo


def main() -> int:
    print("=" * 74)
    print(" T1 — is R₁₂ / C(y) a knot invariant of the net braid?")
    print("=" * 74)

    # rebuild R₁₂ from the net (same path as PR #3294)
    dnet = sp.cancel(sp.simplify(load_net_symbolic("neutron"))
                     - sp.simplify(load_net_symbolic("proton")))
    dbar = dnet.subs(q, 1 / q)
    odd = sp.cancel((dnet - dbar) / 2)
    num = sp.Poly(sp.expand(sp.numer(odd)), q)
    r12 = next(sp.Poly(sp.expand(f), q) for f, m in sp.factor_list(num.as_expr())[1]
               if sp.Poly(f, q).degree() == 12)
    r12_span = r12.degree() - r12.monoms()[-1][0]
    print(f"  R₁₂ q-span = {r12_span} (degree {r12.degree()})")

    # C(y) Galois
    Cy = sp.expand(y**3 - 4 * y**2 + 3 * y - 2)
    is_abelian, disc, is_sq = galois_is_abelian_cubic(Cy)
    print(f"  C(y) = {Cy};  disc = {disc};  perfect square: {is_sq} ⇒ "
          f"Galois {'C₃ (abelian)' if is_abelian else 'S₃ (NON-abelian)'}")

    # (A) constituent Jones spans (+ note their cyclotomic content, which is
    #     NOT uniformly cyclotomic — the trefoil is not — so it does not
    #     serve as a separating argument; recorded for honesty).
    jones = jones_constituents()
    print("  constituent-knot Jones (integer-power reps):")
    max_span = 0
    constituents_all_cyclo = True
    for name, V in jones.items():
        P = sp.Poly(sp.expand(V), q) if V != 1 else sp.Poly(1, q)
        span = (P.degree() - P.monoms()[-1][0]) if V != 1 else 0
        max_span = max(max_span, span)
        cyc, noncyc = cyclotomic_content(V) if V != 1 else ([], [])
        constituents_all_cyclo = constituents_all_cyclo and not noncyc
        print(f"    {name:<8} V={V}  span={span}  cyclotomic-only={not noncyc}")
    span_mismatch = r12_span > max_span
    print(f"  (constituents all cyclotomic-only: {constituents_all_cyclo} "
          f"— note: FALSE, so the S₃-vs-cyclotomic argument does NOT separate)")

    # (B) is R₁₂ divisible by / equal to any constituent Jones?
    divides_any = any(V != 1 and sp.rem(r12.as_expr(), sp.expand(V), q) == 0
                      for V in jones.values())
    equals_any = any(sp.simplify(r12.as_expr() - sp.expand(V)) == 0
                     for V in jones.values())

    verdict = (
        "R₁₂ is NOT a constituent-knot invariant, and the net object is not "
        "a braid closure (scope (a)). (A) R₁₂ q-span %d ≫ every "
        "constituent-knot Jones span (max %d); it neither equals nor "
        "divides any. (B) the net is the isospin difference "
        "Δ(n[u,d,d])−Δ(p[u,u,d]) of Hecke-trace amplitudes, differing only "
        "in the u/d crossing weights (∈ ℚ[q²]); R₁₂ is even in q ⇒ lives in "
        "ℚ[y], y=q²+q⁻², the crossing-weight sector — a representation "
        "object, not topological. C(y) has disc %s ⇒ S₃ Galois, recorded as "
        "structure but NOT the separating invariant (the trefoil's own "
        "reduced Jones cubic is likewise non-cyclotomic)."
        % (r12_span, max_span, disc))
    print("\n  VERDICT:", verdict)

    w = WitnessBuilder("qbeta-r12-knot-invariant", engine="sympy")
    w.set_description(
        "T1: R_12/C(y) is not a constituent-knot invariant and the net is "
        "not a braid closure. Separators: (A) R_12 q-span 12 >> every "
        "constituent Jones span (<=4), equals/divides none; (B) R_12 even "
        "in q lives in Q[y], y=q^2+q^-2, the isospin crossing-weight sector. "
        "NOTE: the S_3/cyclotomic Galois argument does NOT separate (the "
        "trefoil's own reduced Jones cubic is also non-cyclotomic); "
        "disc(C)=-152 => S_3 is recorded as structure only.")
    w.add_parameter("C_of_y", str(Cy))
    w.add_parameter("net_basis_knots",
                    "unknot,virtual,Hopf,trefoil (H_3 NF basis)")
    w.add_data("R12_q_span", int(r12_span))
    w.add_data("max_constituent_jones_span", int(max_span))
    w.add_data("C_discriminant", int(disc))
    w.add_data("C_galois_abelian", bool(is_abelian))
    w.add_data("R12_equals_a_constituent_jones", bool(equals_any))
    w.add_data("R12_divides_by_a_constituent_jones", bool(divides_any))
    w.add_data("verdict", verdict)
    w.add_data("constituents_all_cyclotomic", bool(constituents_all_cyclo))
    w.add_data("galois_note",
               "C(y) disc -152 ⇒ S_3, but this does NOT separate R_12 from "
               "knot invariants (trefoil reduced Jones cubic is also "
               "non-cyclotomic); separation is by (A)+(B), not Galois.")
    w.add_assertion(
        name="C_galois_nonabelian_S3_structural_fact",
        computed=0.0 if not is_abelian else 1.0,
        expected=0.0, tolerance=0.0,
        unit="bool (0 = disc not a perfect square ⇒ S_3); STRUCTURE not separator",
        source="cubic Galois criterion: C_3 iff disc is a rational square.")
    w.add_assertion(
        name="R12_span_exceeds_constituents",
        computed=0.0 if span_mismatch else 1.0,
        expected=0.0, tolerance=0.0,
        unit="bool (0 = R12 q-span > max constituent Jones span)",
        source="degree comparison against constituent-knot Jones polynomials.")
    w.add_assertion(
        name="R12_not_a_constituent_jones",
        computed=0.0 if not (equals_any or divides_any) else 1.0,
        expected=0.0, tolerance=0.0,
        unit="bool (0 = R12 neither equals nor divides any constituent Jones)",
        source="exact polynomial equality / divisibility tests.")
    w.set_audit_only("docs/audits/2026-07-04-zeta4-fibre-cyclotomic-refutation.md")
    out = w.save()
    print(f"\nWitness: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
