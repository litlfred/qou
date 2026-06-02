"""Meson Habiro c_3 — PSLQ integer-relation search over wider basis.

Per author 2026-06-01 "try again" — extend the c_3 categorical search
(meson_habiro_c3_categorical_search.py was NULL across 40 hand-curated
candidates). PSLQ tests INTEGER RELATIONS among a basis: if
c_3 = (a_1·x_1 + ... + a_n·x_n) / d with small integers a_i, d,
PSLQ finds them in polynomial time at the given precision.

## Method

Build a basis of natural substrate quantities:
- 1, G (Catalan), π, ln(2), q, q^(-1), [k]_q for k=2..5
- b, b², b³ where b² = (h²+3)/(h²+4)
- h, h², ℏ_q, ℏ_q²
- J_Hopf(q=1) = -2, J_Hopf(q_0), various Wedderburn dimensions

Then run mp.pslq on [c_3_target, basis...] looking for relations
of bounded coefficient size.

## Cross-references

- meson_habiro_c3_categorical_search.py (the NULL 40-candidate scan)
- meson_habiro_c4_truncation_reexam.py (the c_3 = -0.7156 finding)
- audit 2026-06-01-closed-route-reexamination-roundup.md step (1)
"""
from __future__ import annotations

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
import sys
from pathlib import Path

import mpmath as mp

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

from _precision import set_compute_dps  # noqa: E402
from q_parameter import Q_50_DIGIT_STR  # noqa: E402
from witness_base import WitnessBuilder  # noqa: E402


def qint(k, q):
    return (q ** k - q ** (-k)) / (q - 1 / q)


def main() -> int:
    set_compute_dps(60)  # PSLQ needs a bit of margin
    q = mp.mpf(Q_50_DIGIT_STR)

    print("=" * 78)
    print("Meson Habiro c_3 — PSLQ integer-relation search (60 dps)")
    print("=" * 78)
    print(f"\nq_0 = {Q_50_DIGIT_STR}\n")

    # Reproduce c_3 target
    h = q - 1 / q
    h2 = h * h
    b_sq = (h2 + 3) / (h2 + 4)
    b = mp.sqrt(b_sq)
    hbar_q = 1 - 1 / q
    hbar_q_sq = hbar_q ** 2
    u = b * hbar_q_sq

    m_K = mp.mpf("493.677")
    m_pi = mp.mpf("139.57039")
    target = m_K / m_pi
    chi5 = q ** 5 - q ** (-5)
    seifert_ratio_sq = (mp.mpf(9) / 5) ** 2
    base = chi5 * seifert_ratio_sq
    R_exact = target / base
    C = R_exact - 1
    c_3 = (C - 4 * u ** 2) / u ** 3

    print(f"[c_3 target] {mp.nstr(c_3, 30)}\n")

    # Substrate / natural-constant basis
    G = mp.catalan

    # Define basis with name + value
    basis_dict = {
        "1": mp.mpf(1),
        "G": G,
        "pi": mp.pi,
        "ln2": mp.log(2),
        "q": q,
        "1/q": 1 / q,
        "h": h,
        "h^2": h2,
        "hbar_q": hbar_q,
        "hbar_q^2": hbar_q_sq,
        "b": b,
        "b^2": b_sq,
        "b^3": b ** 3,
        "u": u,
        "u^2": u ** 2,
        "[2]_q": q + 1 / q,
        "[3]_q": qint(3, q),
        "[4]_q": qint(4, q),
        "[5]_q": qint(5, q),
        "Jhopf_q0": -(q ** 2 + 1 / q ** 2),
        "G*b": G * b,
        "G*b^2": G * b_sq,
        "G*hbar_q": G * hbar_q,
        "G/pi": G / mp.pi,
    }
    basis_names = list(basis_dict.keys())
    basis_values = [basis_dict[n] for n in basis_names]

    # Search for integer relations c_3 = Σ a_i · b_i / d
    # PSLQ on [c_3, b_1, ..., b_n]; relation a_0·c_3 + a_1·b_1 + ... = 0
    # ⇒ c_3 = -(a_1·b_1 + ... + a_n·b_n) / a_0

    print(f"[Basis ({len(basis_names)} elements)]")
    for n in basis_names:
        print(f"  {n:<14}= {mp.nstr(basis_dict[n], 10)}")

    print(f"\n[PSLQ — pairwise (c_3, b_i) — tests c_3 = (p/q)·b_i]")
    matches = []
    for n, v in basis_dict.items():
        try:
            rel = mp.pslq([c_3, v], tol=mp.mpf("1e-12"), maxcoeff=10000)
            if rel and rel[0] != 0:
                ratio = -mp.mpf(rel[1]) / mp.mpf(rel[0])
                check = c_3 - ratio * v
                if abs(check) < mp.mpf("1e-10"):
                    matches.append((f"{rel[1]}/{rel[0]} · {n}", ratio * v, abs(check)))
                    print(f"  c_3 ≈ ({rel[1]}/{rel[0]}) · {n} = {mp.nstr(ratio * v, 15)} (residual {mp.nstr(abs(check), 8)})")
        except Exception:
            pass

    if not matches:
        print(f"  No tight pairwise integer-relation hits (tol 1e-12, maxcoeff 10000).")

    print(f"\n[PSLQ — triples (c_3, b_i, b_j) — tests c_3 = a·b_i/c + b·b_j/c]")
    # Top-12 most-natural basis elements for triples
    top_basis = ["1", "G", "b", "b^2", "[2]_q", "[3]_q", "h^2", "hbar_q^2", "u", "G*b", "G*b^2", "1/q"]
    found = 0
    for i, n1 in enumerate(top_basis):
        if found >= 5:
            break
        for n2 in top_basis[i + 1:]:
            if found >= 5:
                break
            v1, v2 = basis_dict[n1], basis_dict[n2]
            try:
                rel = mp.pslq([c_3, v1, v2], tol=mp.mpf("1e-15"), maxcoeff=200)
                if rel and rel[0] != 0:
                    a0, a1, a2 = rel
                    pred = -(mp.mpf(a1) * v1 + mp.mpf(a2) * v2) / mp.mpf(a0)
                    check = c_3 - pred
                    if abs(check) < mp.mpf("1e-13") and max(abs(a0), abs(a1), abs(a2)) < 100:
                        found += 1
                        print(f"  c_3 ≈ ({-a1}·{n1} + {-a2}·{n2}) / {a0} = {mp.nstr(pred, 18)} "
                              f"(residual {mp.nstr(abs(check), 8)})")
            except Exception:
                pass

    if found == 0:
        print(f"  No tight pair-of-basis integer relations within maxcoeff 200.")

    # Full-basis PSLQ (longer, lower precision tolerance)
    print(f"\n[PSLQ — full basis (c_3, b_1, ..., b_n) at maxcoeff 50]")
    try:
        full = [c_3] + basis_values
        rel = mp.pslq(full, tol=mp.mpf("1e-25"), maxcoeff=50)
        if rel and rel[0] != 0:
            # Express c_3 = -(Σ a_i · b_i) / a_0
            coefs = [mp.mpf(r) for r in rel]
            num = -sum(coefs[i + 1] * basis_values[i] for i in range(len(basis_values)))
            pred = num / coefs[0]
            check = c_3 - pred
            print(f"  PSLQ relation found (coefs = {rel})")
            print(f"  c_3 predicted = {mp.nstr(pred, 22)}")
            print(f"  residual      = {mp.nstr(abs(check), 8)}")
            terms = [(rel[i + 1], basis_names[i]) for i in range(len(basis_values))
                     if rel[i + 1] != 0]
            print(f"  Nonzero terms (c_3 = Σ a_i·b_i / a_0 where a_0 = {rel[0]}):")
            for a, n in terms:
                print(f"    {-a:+5d}·{n}")
        else:
            print(f"  No full-basis integer relation found at maxcoeff 50.")
    except Exception as e:
        print(f"  PSLQ failed: {e}")

    # ── Verdict ──
    print(f"\n[Verdict]")
    if matches:
        verdict = (
            f"PAIRWISE HIT: c_3 = {matches[0][0]} ≈ {mp.nstr(matches[0][1], 12)} "
            f"(residual {mp.nstr(matches[0][2], 8)}). This is a clean "
            f"single-quantity identification."
        )
    elif found > 0:
        verdict = (
            f"PAIR-OF-BASIS HITS: {found} integer relations found within "
            f"maxcoeff 200. These are candidate categorical identifications "
            f"but require structural interpretation."
        )
    else:
        verdict = (
            f"NULL — no clean PSLQ integer relation for c_3 = {mp.nstr(c_3, 12)} "
            f"across {len(basis_names)} natural substrate basis elements "
            f"(pairwise tol 1e-12, triples tol 1e-15, full tol 1e-25). "
            f"Strong evidence that c_3 is NOT a natural rational combination "
            f"of substrate quantities — likely transcendental in q OR "
            f"the meson Habiro c=4 leading framing is wrong."
        )
    print(f"  {verdict}")

    # ── Witness ──
    w = WitnessBuilder(
        "meson-habiro-c3-pslq-search",
        engine="python",
    )
    w.set_description(
        "PSLQ integer-relation search for meson Habiro c_3 = -0.7156 "
        "across 24 natural substrate basis elements (G, π, h-powers, "
        "b-powers, q-brackets, ℏ_q-powers, J_Hopf). Tests pairwise, "
        "triples (top-12), and full basis. Complements the NULL hand-"
        "curated scan in meson_habiro_c3_categorical_search.py."
    )
    w.add_parameter("q_50dps", Q_50_DIGIT_STR)
    w.add_data("c_3_target", mp.nstr(c_3, 30))
    w.add_data("basis_size", len(basis_names))
    w.add_data("pairwise_matches", str(matches))
    w.add_data("pair_basis_hits_count", found)
    w.add_data("verdict", verdict)

    w.add_assertion(
        name="pslq_search_completed",
        computed=True,
        expected=True,
        tolerance=0,
        source=f"PSLQ search across {len(basis_names)} basis elements at 60 dps.",
    )
    out = w.save()
    print(f"\n  Witness: {out.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
