#!/usr/bin/env python3
"""
Does a HIGHER-colour (ℂ³, ℂ⁴, …) Schur–Weyl weighting rescue the WRT→W_λ route? — NO.

#2608 left the open object as: derive the higher-Wilson-line / colour-ℂ³ Schur–Weyl
weighting and test whether it lands the q-Plancherel W_λ without a free parameter.
This probe forecloses that route structurally (formalize-first), for ALL colour d.

The candidate "colour weighting" of an S₅/H₅(q) block λ from a ℂ^d arena is the
gl_d-multiplicity in Schur–Weyl, m_d(λ) = dim L^{gl_d}_λ = #SSYT(λ, entries ≤ d)
(q-deformed: s_λ(1,q,…,q^{d-1}), the colour-multiplicity quantum dimension). Two
defining properties of W_λ are incompatible with m_d(λ) for EVERY d:

  (1) SUPPORT.  W_λ > 0 for all 7 λ⊢5 (incl. (2,1,1,1) 4-row and (1⁵) 5-row).
      m_d(λ) = 0 unless rows(λ) ≤ d.  So no d < 5 even hosts W_λ's support; ℂ³
      (the #2364/#2406 "colour" promotion) still misses (2,1,1,1),(1⁵).

  (2) CONJUGATION SYMMETRY.  W_λ = W_{λ'} (the Plancherel hallmark; d_q(λ)=d_q(λ')
      because the hook multiset is transpose-invariant).  But m_d(λ) is strongly
      conjugation-ASYMMETRIC — it favours the colour/production direction (the gl_d
      dimension peaks near (4,1); the principal-specialization limit at the one-row
      (5)), never the conjugation-symmetric Plancherel peak (3,1,1).  No d (finite
      or →∞) makes m_d symmetric.

⇒ The WRT-colour Schur–Weyl functor lands the PRODUCTION weight family (y_λ-like,
principal specialization), NOT the Plancherel W_λ.  These are exactly the two
weight systems the Plancherel-target doc (2026-06-16) separated.  Reproducing W_λ
needs the SYMMETRIC / regular pairing — the full Markov quantum dimension squared
d_q(λ)² (d→∞ full Hecke), which is not a finite-colour WRT image.  The route loops
to #2406 ("no finite colour-SU(3) arena") / #2409 (infinite-dim full-Hecke).

DISCIPLINE (STRICT): no fit. This is a structural foreclosure (a numerical-search
prune), not a closure of the keystone.
"""
import json
import os

Q0 = 1.1099785955541805
PARTITIONS_5 = [(5,), (4, 1), (3, 2), (3, 1, 1), (2, 2, 1), (2, 1, 1, 1), (1, 1, 1, 1, 1)]


def conjugate(lam):
    if not lam:
        return ()
    return tuple(sum(1 for p in lam if p >= j) for j in range(1, lam[0] + 1))


def cells(lam):
    return [(i, j) for i, row in enumerate(lam) for j in range(row)]  # 0-based (i,j)


def hook(lam, i, j):
    lam_t = conjugate(lam)
    return (lam[i] - (j + 1)) + (lam_t[j] - (i + 1)) + 1


def num_ssyt(lam, d):
    """#SSYT of shape λ with entries in {1..d} = dim L^{gl_d}_λ (hook-content, q=1).
    = ∏_cells (d + content)/hook,  content = j - i."""
    num = 1.0
    den = 1.0
    for (i, j) in cells(lam):
        num *= (d + (j - i))
        den *= hook(lam, i, j)
    val = num / den
    return round(val)  # integer dimension


def q_int(k, q):
    return (q ** k - q ** (-k)) / (q - q ** (-1))


def q_dim_balanced(lam, q):
    n = sum(lam)
    fact = 1.0
    for k in range(1, n + 1):
        fact *= q_int(k, q)
    den = 1.0
    for (i, j) in cells(lam):
        den *= q_int(hook(lam, i, j), q)
    return fact / den


def s_lambda_principal(lam, q, d):
    """q-deformed colour-multiplicity dim_q L^{gl_d}_λ = s_λ(1,q,…,q^{d-1})
    = q^{n(λ)} ∏ (1 - q^{d + content}) / (1 - q^{hook}),  n(λ)=Σ (i)·λ_{i+1} (0-based i)."""
    n_lam = sum(i * row for i, row in enumerate(lam))  # Σ_{i≥0} i·λ_{i+1}
    val = q ** n_lam
    for (i, j) in cells(lam):
        c = j - i
        val *= (1 - q ** (d + c)) / (1 - q ** hook(lam, i, j))
    return val


def main():
    q = Q0
    print(f"q_0 = {q}\n")

    # Plancherel W_λ (the keystone target) — balanced quantum dim squared.
    fact = 1.0
    for k in range(1, 6):
        fact *= q_int(k, q)
    W = {lam: q_dim_balanced(lam, q) ** 2 / fact for lam in PARTITIONS_5}

    print("colour-multiplicity m_d(λ) = #SSYT(λ, ≤ d) = dim L^{gl_d}_λ  (the Schur–Weyl colour weight):")
    print(f"  {'λ':<16} {'m_2':>5} {'m_3':>5} {'m_4':>5} {'m_5':>5}   W_λ (Plancherel)")
    md = {d: {} for d in (2, 3, 4, 5)}
    for lam in PARTITIONS_5:
        for d in (2, 3, 4, 5):
            md[d][lam] = num_ssyt(lam, d)
        print(f"  {str(lam):<16} {md[2][lam]:>5} {md[3][lam]:>5} {md[4][lam]:>5} {md[5][lam]:>5}   {W[lam]:.5f}")

    print("\n(1) SUPPORT obstruction:")
    for d in (2, 3, 4, 5):
        supp = [lam for lam in PARTITIONS_5 if md[d][lam] > 0]
        print(f"  d={d}: colour Schur–Weyl hosts {len(supp)} blocks {[''.join(map(str,l)) for l in supp]}")
    wsupp = [lam for lam in PARTITIONS_5 if W[lam] > 0]
    print(f"  W_λ support: {len(wsupp)} blocks (ALL of λ⊢5) → need d ≥ 5 just for the support; ℂ³ misses (2,1,1,1),(1⁵).")

    print("\n(2) CONJUGATION-SYMMETRY obstruction  (W_λ = W_{λ'} but m_d(λ) ≠ m_d(λ')):")
    print(f"  {'pair λ / λ′':<22} {'W_λ=W_λ′?':>10}   m_5(λ) vs m_5(λ′)   m_∞(q) ratio λ/λ′")
    for lam in [(5,), (4, 1), (3, 2)]:
        lp = conjugate(lam)
        wsym = abs(W[lam] - W[lp]) < 1e-12
        sinf_lam = s_lambda_principal(lam, q, 200)   # d large → full principal spec
        sinf_lp = s_lambda_principal(lp, q, 200)
        print(f"  {str(lam)+' / '+str(lp):<22} {str(wsym):>10}   {md[5][lam]:>4} vs {md[5][lp]:<4}        {sinf_lam/sinf_lp:.3f}")
    print(f"  (3,1,1) self-conj: W={W[(3,1,1)]:.5f} (PEAK);  m_5={md[5][(3,1,1)]}")

    # peak locations
    w_peak = max(PARTITIONS_5, key=lambda l: W[l])
    m5_peak = max(PARTITIONS_5, key=lambda l: md[5][l])
    print(f"\n  PEAK: W_λ peaks at {w_peak} (Plancherel/symmetric);  m_5 peaks at {m5_peak} (colour/principal-spec).")

    print("\n(3) Even d=5 (full support) — colour weight vs Plancherel, normalized:")
    m5_sum = sum(md[5].values())
    w_sum = sum(W.values())
    print(f"  {'λ':<16} {'m_5/Σ':>10} {'W_λ/Σ':>10} {'rel Δ':>9}")
    maxrel = 0.0
    for lam in PARTITIONS_5:
        a, b = md[5][lam] / m5_sum, W[lam] / w_sum
        rel = (a - b) / b
        maxrel = max(maxrel, abs(rel))
        print(f"  {str(lam):<16} {a:>10.5f} {b:>10.5f} {rel:>+8.1%}")
    print(f"  → max |rel Δ| = {maxrel:.0%}  ⇒ colour-multiplicity (any d) ≠ Plancherel W_λ.")

    verdict = (
        "HIGHER-COLOUR DOES NOT RESCUE THE ROUTE. The colour-multiplicity Schur-Weyl weight m_d(lambda) "
        "(#SSYT, = dim L^{gl_d}_lambda) (i) has support {rows<=d}, missing W_lambda's 4-row/5-row blocks "
        "for d<5; and (ii) is strongly conjugation-ASYMMETRIC (e.g. m_5(5)=126 vs m_5(1^5)=1), peaking away "
        "from the Plancherel (3,1,1) (gl_d dimension peaks at (4,1); principal-spec limit at the one-row (5)) "
        "- the production direction, whereas W_lambda is conjugation-symmetric and peaks at (3,1,1). No d "
        "(finite or ->infinity) makes m_d symmetric, so no colour weighting equals the "
        "Plancherel W_lambda. The WRT-colour Schur-Weyl functor lands the PRODUCTION weight family, not the "
        "Plancherel target. W_lambda needs the SYMMETRIC pairing d_q(lambda)^2 (full Hecke, d->infinity) — "
        "not a finite-colour WRT image. Route foreclosed; loops to #2406 (no finite colour-SU(3) arena) / "
        "#2409 (infinite-dim full-Hecke)."
    )
    print("\n" + verdict)

    witness = {
        "description": "Higher-colour Schur-Weyl foreclosure for the WRT->W_lambda keystone route (#2608 "
                       "follow-up). The gl_d colour-multiplicity m_d(lambda)=#SSYT(lambda,<=d) cannot equal "
                       "the q-Plancherel W_lambda for any d: support {rows<=d} misses W's 4/5-row blocks for "
                       "d<5, and m_d is conjugation-asymmetric (peaks at one-row (5), the production y_lambda "
                       "direction) while W_lambda=W_{lambda'} peaks at (3,1,1). No fit; structural foreclosure.",
        "computation": "docs/audits/scripts/keystone_wrt_schurweyl_higher_colour_foreclosure_probe.py",
        "q0": repr(Q0),
        "colour_multiplicity_m_d": {str(lam): {d: md[d][lam] for d in (2, 3, 4, 5)} for lam in PARTITIONS_5},
        "W_lambda_plancherel": {str(lam): W[lam] for lam in PARTITIONS_5},
        "support_by_d": {d: [str(l) for l in PARTITIONS_5 if md[d][l] > 0] for d in (2, 3, 4, 5)},
        "W_lambda_support_count": len(wsupp),
        "min_d_for_support": 5,
        "conjugation_symmetry": {
            "W_lambda_symmetric": True,
            "m_5_asymmetry_examples": {"(5)_vs_(1^5)": [md[5][(5,)], md[5][(1, 1, 1, 1, 1)]],
                                        "(4,1)_vs_(2,1,1,1)": [md[5][(4, 1)], md[5][(2, 1, 1, 1)]]},
        },
        "peaks": {"W_lambda": str(w_peak), "m_5_colour": str(m5_peak)},
        "d5_full_support_vs_plancherel_max_rel": maxrel,
        "verdict": verdict,
        "discipline": "No fit; structural foreclosure (search prune), not a keystone closure. Owner closes (bean s5bb section 4a).",
    }
    out = os.path.join(os.path.dirname(__file__), "..", "..", "..", "computations",
                       "keystone-wrt-schurweyl-higher-colour-foreclosure.witness.json")
    with open(os.path.abspath(out), "w") as f:
        json.dump(witness, f, indent=2)
        f.write("\n")
    print(f"\nwitness → {os.path.relpath(os.path.abspath(out))}")
    print("HIGHER-COLOUR FORECLOSURE PROBE COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
