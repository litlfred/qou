"""

CLASS-A acknowledged-anchor banner (per Workplan-0b, applies to
hardcoded CODATA-precision literals in this file as well — see
`docs/audits/2026-05-18-workplan-0b-m-n-substrate-derivation.md`).
The numeric mass / Q-value constants used here are validation-chain
anchors pending substrate derivation; until that lands, treat them
as CAL-3-ish acknowledged inputs, NOT independent calibrations.
The compute-integration-watcher I9 audit therefore classifies this
script as `ok_acknowledged_anchor` rather than as a registry-bypass
violation.
"""

import _path_bridge  # noqa: F401, E402 — Phase 6 bridge: substrate modules moved into substrate/ subdir
#!/usr/bin/env python3
"""
DERIVED atomic mass for Z=1-20 — no fitted parameters.

⚠️  STRUCTURAL BUG — DO NOT TRUST OUTPUT  ⚠️
═══════════════════════════════════════════════════════════════════
This script computes
    M_derived = tr_M(atom NF) × E_0
multiplicatively from the assembled atom's normal form.  This is
the wrong combination law: composing nucleon Markov traces by
multiplication does not represent atomic mass.

The right structural object on the QOU side is the LP-dual
shadow price y_λ* per Wedderburn block (`prop:operator-selection-lp`)
together with the GB normal form in H_n(R, q).  The active set
{λ : y_λ* > 0} identifies which Wedderburn blocks the bound
state saturates.

The right experimental comparison object (separate question) is
the *additive* constituent sum
    M_atom = Z·M_p + N·M_n + Z·M_e − E_binding(A, Z).
(The additive baseline was purged 2026-06-09; the canonical absolute
nucleon/atom mass is the muon-anchored Hecke energy via the
`canonical_mass` facade (`canonical_mass.proton_mass_mev` /
`neutron_mass_mev` / `nucleon_mass_mev`), NOT the deprecated
Borromean-volume form `m_e·Vol(𝓑₃)·ρ/ℏ_q²` in `mass_vol_density.py`
(owner ruling 2026-06-24, docs/canonical-mass-formula-guardrail.md;
that form → 966 MeV, +2.96 %, a λ_A fit). Experimental
binding is in `ame-2020-binding-energies.witness.json`.)
Whether the LP active set reproduces empirical Δ_binding via
ρ_F · V_hyp is the interpretive question tracked in
docs/audits/rho-f-volume-binding-gap.md (not a 1ppb gate).

This file is preserved for two reasons:
1. Its proton/neutron Hecke-trace primitives (PROTON_TR,
   NEUTRON_TR) are correct and are still used by downstream
   scripts (cross-check-trM-1ppb, atomic-braid-mass-table) for
   per-nucleon character data.  Don't delete those.
2. Provenance: the computational chain that produces the bad
   atomic-mass table feeds existing audits' "deprecated lineage"
   records.  Removing it would break those audits.

If you're authoring a new mass-formula path, do NOT extend this
script — route absolute nucleon/atom mass through the `canonical_mass`
facade (muon-anchored Hecke energy; owner ruling 2026-06-24,
docs/canonical-mass-formula-guardrail.md), NOT the deprecated
`m_e·Vol(𝓑₃)·ρ/ℏ_q²` form in `mass_vol_density.py`, and source
experimental binding from `ame-2020-binding-energies.witness.json`.

Original (legacy) docstring:

    Builds each atom from the categorical construction:
        γγ → quarks → B₃ confinement → nucleon NF → nuclear
        assembly → atom

    Mass = Markov trace of atom NF × energy scale E₀.
    The ONLY inputs are: q₀ (from Vol(4₁)/m_μ/m_e) and m_e
    (energy scale).  No Bethe-Weizsacker, no CODATA m_p/m_n.

Usage:
    python3 computations/atom_mass_derived.py
"""

import math
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))

from q_parameter import Q as q0, Q_INV as qi0, HA as HA_val
from experimental_constants import M_E_MEV, M_P_MEV, M_N_MEV
from witness_base import WitnessBuilder
from codata_constants import M_HE4_ATOMIC_MEV_VALIDATION  # noqa: E402  (AME registry)


# ══════════════════════════════════════════════════════════════
# §1  HECKE ENGINE (numerical at q₀)
# ══════════════════════════════════════════════════════════════

HA = HA_val
z = q0**3 / (q0**2 + 1)

# H₃ NF basis
NF_BASIS_3 = [(), (0,), (1,), (0, 1), (1, 0), (0, 1, 0)]
NF_NAMES_3 = ["γ", "σ₀", "σ₁", "L₊", "L₋", "e⁻"]
# Markov trace values for H₃ basis elements
h_trm = q0 - 1.0 / q0
# TR_M_3[5] = tr_M(sigma_0 sigma_1 sigma_0) = h*z^2 + z, NOT z^3. Markov
# axioms: tr(s0 s1 s0) = tr(s1 s0^2) = tr(s1 (h s0 + 1)) = h*z^2 + z.
# docs/audits/2026-05-19-trm5-markov-bug.md; fixed in pyhecke.gram
# 2026-05-19, never propagated here (bean qou-ssex).
TR_M_3 = [1.0, z, z, z**2, z**2, h_trm * z**2 + z]


def hecke_mul(t1, t2):
    """Multiply two H_n(q) elements (word → coefficient dicts)."""
    result = {}
    for w1, c1 in t1.items():
        for w2, c2 in t2.items():
            w = w1 + w2
            result[w] = result.get(w, 0.0) + c1 * c2
    return {w: c for w, c in result.items() if abs(c) > 1e-15}


def reduce_nf(terms):
    """Gröbner-Shirshov reduction: Hecke + Yang-Baxter + far-commutativity."""
    changed = True
    while changed:
        changed = False
        new_terms = {}
        for word, coeff in terms.items():
            if abs(coeff) < 1e-15:
                continue
            done = False
            # Hecke: σᵢ² = HA·σᵢ + 1
            for pos in range(len(word) - 1):
                if word[pos] == word[pos + 1]:
                    i = word[pos]
                    pre, suf = word[:pos], word[pos + 2:]
                    new_terms[pre + (i,) + suf] = new_terms.get(pre + (i,) + suf, 0.0) + coeff * HA
                    new_terms[pre + suf] = new_terms.get(pre + suf, 0.0) + coeff
                    done = changed = True
                    break
            if done:
                continue
            # Yang-Baxter: σᵢσⱼσᵢ = σⱼσᵢσⱼ (|i-j|=1), orient to smaller
            for pos in range(len(word) - 2):
                a, b, c = word[pos], word[pos + 1], word[pos + 2]
                if a == c and abs(a - b) == 1:
                    new_trip = (b, a, b)
                    if new_trip < (a, b, a):
                        nw = word[:pos] + new_trip + word[pos + 3:]
                        new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                        done = changed = True
                        break
            if done:
                continue
            # Far-commutativity: σᵢσⱼ = σⱼσᵢ (|i-j|≥2), orient to smaller
            for pos in range(len(word) - 1):
                a, b = word[pos], word[pos + 1]
                if abs(a - b) >= 2 and a > b:
                    nw = word[:pos] + (b, a) + word[pos + 2:]
                    new_terms[nw] = new_terms.get(nw, 0.0) + coeff
                    done = changed = True
                    break
            if not done:
                new_terms[word] = new_terms.get(word, 0.0) + coeff
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def expand_inverse(word):
    """Expand braid word with inverses: negative gen g means σ_{|g|-1}⁻¹."""
    terms = {(): 1.0}
    for g in word:
        new_terms = {}
        if g >= 0:
            for w, c in terms.items():
                nw = w + (g,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
        else:
            i = -g - 1
            for w, c in terms.items():
                # σ⁻¹ = σ - HA
                nw = w + (i,)
                new_terms[nw] = new_terms.get(nw, 0.0) + c
                new_terms[w] = new_terms.get(w, 0.0) - c * HA
        terms = {w: c for w, c in new_terms.items() if abs(c) > 1e-15}
    return terms


def markov_trace_general(terms):
    """**Approximation** of the Markov trace for general H_3(q) elements.

    Uses the canonical TR_M_3 lookup table for the 6 NF basis elements
    of H_3 (these are exact), and a `z^len(word)` heuristic fallback
    for words outside NF_BASIS_3. The fallback is **NOT** the canonical
    Markov trace — it over-counts when adjacent generators don't
    commute. For the H_3 atomic mass computation this script targets,
    the input `terms` should already be in NF basis after Hecke
    reduction (lines ~95-125 above), so the fallback branch typically
    doesn't fire in practice.

    See docs/audits/2026-05-17-dual-tr-m-discrepancy.md for the
    broader Plancherel/Markov-trace audit. For the canonical Markov
    trace of an arbitrary H_n braid word, use
    `markov_trace_recursive.markov_trace_of_word(n, signed_word)`
    directly.
    """
    total = 0.0
    for word, coeff in terms.items():
        if word in NF_BASIS_3:
            idx = NF_BASIS_3.index(word)
            total += coeff * TR_M_3[idx]
        else:
            # Fallback heuristic (NOT canonical Markov; flagged above).
            # In practice this branch is rare because Hecke reduction
            # in this script normalises into NF_BASIS_3 first.
            total += coeff * z ** len(word)
    return total


def nf_net(terms):
    """Sum of all NF coefficients."""
    return sum(terms.values())


def quark_crossing(type_i, type_j, gen):
    """Typed crossing for quark pair in H₃(q)."""
    if type_i == type_j == 'u':
        return {(gen,): 1.0}
    elif type_i == type_j == 'd':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


def nuclear_crossing(type_i, type_j, gen):
    """Typed crossing for nucleon pair in H_A(q)."""
    if type_i == type_j == 'p':
        return {(gen,): 1.0}
    elif type_i == type_j == 'n':
        return {(gen,): 1.0, (): -HA}
    else:
        return {(gen,): 1.0, (): -HA / 2}


# ══════════════════════════════════════════════════════════════
# §2  BUILD NUCLEONS FROM B₃ + TYPED CROSSINGS
# ══════════════════════════════════════════════════════════════

# B₃ = (σ₀σ₁⁻¹)³ — the unique minimum-action confinement operator
B3_RAW = expand_inverse((0, -2, 0, -2, 0, -2))
B3_NF = reduce_nf(B3_RAW)


def build_nucleon(quark_types):
    """Build nucleon NF from B₃ + typed crossings.

    quark_types: list of 'u' or 'd', length 3.
    Returns: NF terms dict.
    """
    elem = dict(B3_NF)
    for i in range(3):
        for j in range(i + 1, 3):
            gen = min(i, j)
            if gen > 1:
                gen = 1
            cx = quark_crossing(quark_types[i], quark_types[j], gen)
            elem = hecke_mul(elem, cx)
            elem = reduce_nf(elem)
    return elem


# Build proton and neutron NFs (derived, not imported)
PROTON_NF = build_nucleon(['u', 'u', 'd'])
NEUTRON_NF = build_nucleon(['u', 'd', 'd'])

# Derived masses from Markov trace
PROTON_TR = markov_trace_general(PROTON_NF)
NEUTRON_TR = markov_trace_general(NEUTRON_NF)
PROTON_NET = nf_net(PROTON_NF)
NEUTRON_NET = nf_net(NEUTRON_NF)

# Energy scale: E₀ such that tr_M(proton) × E₀ = m_p (CODATA)
# This is the ONE calibration — mapping Hecke units to MeV.
# Alternatively: E₀ = m_e / tr_M(electron_NF).
E0_MEV = M_P_MEV / PROTON_TR


# ══════════════════════════════════════════════════════════════
# §3  BUILD ATOM FROM NUCLEONS
# ══════════════════════════════════════════════════════════════

def build_atom(Z, N):
    """Build full atom NF in H_A(q) from derived nucleons.

    Returns (nucleus_nf, atom_nf, metadata).
    """
    A = Z + N
    nucleon_types = ['p'] * Z + ['n'] * N
    nucleon_nfs = [dict(PROTON_NF) if t == 'p' else dict(NEUTRON_NF) for t in nucleon_types]

    if A == 0:
        return {(): 1.0}, {(): 1.0}, {}

    # Start with first nucleon
    elem = dict(nucleon_nfs[0])

    # Inductively add nucleons with typed crossings
    for k in range(1, A):
        gen = min(k - 1, max(A - 2, 0))
        cx = nuclear_crossing(nucleon_types[k - 1], nucleon_types[k], gen)
        nuc = nucleon_nfs[k]
        # elem × crossing × nucleon, then reduce
        temp = hecke_mul(elem, cx)
        temp = hecke_mul(temp, nuc)
        elem = reduce_nf(temp)

    nucleus_nf = dict(elem)

    # Add Z electrons via Hopf links
    electron = {(0, 1, 0): 1.0}  # e⁻ = σ₀σ₁σ₀ (closure: Hopf link)
    atom_elem = dict(nucleus_nf)
    for e_idx in range(Z):
        gen = e_idx % max(A - 1, 1)
        hopf = {(gen,): 1.0}  # electromagnetic Hopf crossing
        temp = hecke_mul(atom_elem, hopf)
        temp = hecke_mul(temp, electron)
        atom_elem = reduce_nf(temp)

    metadata = {
        'nucleus_terms': len(nucleus_nf),
        'atom_terms': len(atom_elem),
        'nucleus_net': nf_net(nucleus_nf),
        'atom_net': nf_net(atom_elem),
    }

    return nucleus_nf, atom_elem, metadata


# ══════════════════════════════════════════════════════════════
# §4  RESULT + MAIN
# ══════════════════════════════════════════════════════════════

@dataclass
class DerivedAtomResult:
    element: str
    Z: int
    N: int
    A: int
    nucleus_terms: int
    atom_terms: int
    nucleus_net: float
    atom_net: float
    tr_M_nucleus: float
    tr_M_atom: float
    M_derived_MeV: float
    M_observed_MeV: float
    delta_MeV: float
    delta_pct: float
    elapsed_s: float


# Most abundant isotope for Z=1-20
ELEMENTS = {
    1:  ("Hydrogen",   "¹H",   1, 0),
    2:  ("Helium",     "⁴He",  2, 2),
    3:  ("Lithium",    "⁷Li",  3, 4),
    4:  ("Beryllium",  "⁹Be",  4, 5),
    5:  ("Boron",      "¹¹B",  5, 6),
    6:  ("Carbon",     "¹²C",  6, 6),
    7:  ("Nitrogen",   "¹⁴N",  7, 7),
    8:  ("Oxygen",     "¹⁶O",  8, 8),
    9:  ("Fluorine",   "¹⁹F",  9, 10),
    10: ("Neon",       "²⁰Ne", 10, 10),
}

# AME2020 observed atomic masses (MeV)
AME2020_MASS = {
    (1, 0): 938.783,     (2, 2): float(M_HE4_ATOMIC_MEV_VALIDATION),   (3, 4): 6535.367,
    (4, 5): 8394.794,    (5, 6): 10255.103,  (6, 6): 11177.930,
    (7, 7): 13043.781,   (8, 8): 14899.169,  (9, 10): 17696.901,
    (10, 10): 18622.835,
}


def main():
    print("=" * 100)
    print("DERIVED ATOMIC MASS — NO FITTED PARAMETERS")
    print("=" * 100)
    print()
    print(f"  q₀ = {q0:.10f}")
    print(f"  HA = {HA:.10f}")
    print(f"  z  = {z:.10f}")
    print()
    print(f"  B₃ NF: {len(B3_NF)} terms, net = {nf_net(B3_NF):.6f}")
    print(f"  Proton NF:  net = {PROTON_NET:.6f}, tr_M = {PROTON_TR:.6f}")
    print(f"  Neutron NF: net = {NEUTRON_NET:.6f}, tr_M = {NEUTRON_TR:.6f}")
    print(f"  Energy scale E₀ = {E0_MEV:.3f} MeV (from m_p / tr_M(proton))")
    print(f"  Derived m_n = {NEUTRON_TR * E0_MEV:.3f} MeV (CODATA: {M_N_MEV:.3f})")
    print()

    results = []

    for Z in range(1, 11):
        name, label, z_check, n = ELEMENTS[Z]
        assert z_check == Z
        A = Z + n
        t0 = time.time()

        nucleus_nf, atom_nf, meta = build_atom(Z, n)
        tr_nucleus = markov_trace_general(nucleus_nf)
        tr_atom = markov_trace_general(atom_nf)

        M_derived = tr_atom * E0_MEV
        M_obs = AME2020_MASS.get((Z, n), 0.0)
        delta = M_derived - M_obs
        pct = delta / M_obs * 100 if M_obs > 0 else 0

        elapsed = time.time() - t0

        r = DerivedAtomResult(
            element=name, Z=Z, N=n, A=A,
            nucleus_terms=meta['nucleus_terms'],
            atom_terms=meta['atom_terms'],
            nucleus_net=meta['nucleus_net'],
            atom_net=meta['atom_net'],
            tr_M_nucleus=tr_nucleus,
            tr_M_atom=tr_atom,
            M_derived_MeV=M_derived,
            M_observed_MeV=M_obs,
            delta_MeV=delta,
            delta_pct=pct,
            elapsed_s=elapsed,
        )
        results.append(r)

        print(f"{'─' * 100}")
        print(f"  {label} ({name}): Z={Z}, N={n}, A={A}")
        print(f"  NF terms: nucleus={meta['nucleus_terms']}, atom={meta['atom_terms']}")
        print(f"  net: nucleus={meta['nucleus_net']:.6f}, atom={meta['atom_net']:.6f}")
        print(f"  tr_M: nucleus={tr_nucleus:.6f}, atom={tr_atom:.6f}")
        print(f"  M_derived = {M_derived:.3f} MeV")
        print(f"  M_observed = {M_obs:.3f} MeV")
        print(f"  Δ = {delta:+.3f} MeV ({pct:+.4f}%)")
        print(f"  time: {elapsed:.2f}s")
        print()

    # Summary
    print("=" * 100)
    print("SUMMARY: DERIVED MASS vs AME2020")
    print("=" * 100)
    print(f"{'Atom':>5} | {'A':>3} | {'NF terms':>8} | {'tr_M(atom)':>12} | "
          f"{'M_derived':>12} | {'M_observed':>12} | {'Δ MeV':>8} | {'Δ%':>8}")
    print("─" * 100)
    for r in results:
        print(f"{r.element:>5} | {r.A:3d} | {r.atom_terms:8d} | {r.tr_M_atom:12.6f} | "
              f"{r.M_derived_MeV:12.3f} | {r.M_observed_MeV:12.3f} | "
              f"{r.delta_MeV:+8.3f} | {r.delta_pct:+7.3f}%")

    # Witness
    w = WitnessBuilder("atom-mass-derived", engine="python")
    w.set_description(
        "DERIVED atomic mass Z=1-10 from B₃ confinement + typed crossings "
        "+ Markov trace. No fitted Bethe-Weizsacker. One calibration: E₀ = m_p/tr_M(p)."
    )
    w.set_content_block("rem:atom-mass-full-hecke")
    w.add_parameter("q0", str(q0))
    w.add_parameter("E0_MeV", str(E0_MEV))
    w.add_parameter("derived_m_n_MeV", str(NEUTRON_TR * E0_MEV))
    w.add_parameter("proton_tr_M", str(PROTON_TR))
    w.add_parameter("neutron_tr_M", str(NEUTRON_TR))

    # ---- THE TEN `M(<element>)` ASSERTIONS HERE WERE TAUTOLOGIES ---------
    #
    # They read
    #
    #     computed  = M_derived,  expected = M_observed,
    #     tolerance = max(abs(r.delta_MeV) * 2, 50)
    #
    # and `delta_MeV` IS the deviation `M_derived - M_observed`. So the check
    # was `|dev| <= 2*|dev|` -- true for every input, unconditionally. Not a
    # loose tolerance: an assertion mathematically incapable of failing. All
    # ten passed, and `allPassed: true` rested entirely on them, while seven
    # atoms compute a mass of zero or NEGATIVE against expected values of
    # thousands of MeV (bean `qou-tol0`).
    #
    # 🛑 THE BEAN'S CHARACTERISATION IS A COINCIDENCE, NOT THE RULE, and
    #    fixing what it describes would be the wrong fix. It reads "in every
    #    row the tolerance is twice the expected value". Twice the *expected*
    #    and twice the *deviation* agree only because these computed values
    #    are ~0, which makes deviation ~ expected. Checked: M(Helium) carried
    #    tolerance 7695.22 = 2*|-3847.6| (the deviation), where 2*3728.4 =
    #    7456.8 (the expected) is a different number. The code's rule is a
    #    tautology for ANY data; "2x expected" would merely be very loose.
    #
    # WHAT REPLACES THEM. This script's own banner says the combination law
    # is wrong and the output must not be trusted, so an assertion claiming
    # agreement with AME2020 was never the right shape. The falsifiable claim
    # the script actually establishes is the NEGATIVE: the multiplicative law
    # `M = tr_M(atom NF) * E_0` does not reproduce atomic masses beyond
    # hydrogen. If it ever started to, this assertion goes red and someone
    # revisits the banner -- which is exactly the signal that was missing.
    #
    # The per-element numbers are NOT lost: every one is already carried in
    # `results` below (M_derived_MeV, M_observed_MeV, delta_MeV, delta_pct).
    # They move from unfalsifiable assertions to honest data.
    _beyond_h = [r for r in results if r.Z >= 2 and r.M_observed_MeV != 0]
    if _beyond_h:
        _best_rel = min(abs(r.delta_MeV) / abs(r.M_observed_MeV)
                        for r in _beyond_h)
        _best_el = min(_beyond_h,
                       key=lambda r: abs(r.delta_MeV) / abs(r.M_observed_MeV))
        w.add_data("best_relative_error_beyond_hydrogen", _best_rel)
        w.add_data("best_relative_error_element", _best_el.element)
        w.add_data("n_atoms_with_nonpositive_derived_mass",
                   sum(1 for r in results if r.M_derived_MeV <= 0))
        w.add_assertion(
            "multiplicative_law_refuted_beyond_hydrogen",
            # Boolean form: an EMPTY-style failure is representable. The same
            # pattern reports `passed: false` elsewhere in this corpus
            # (`selector_direction_S_independent`), so it is demonstrably
            # capable of going red rather than merely believed to be.
            computed=bool(_best_rel > 0.5),
            expected=True,
            tolerance=0,
            source="min over Z>=2 of |M_derived - M_AME| / |M_AME| exceeds "
                   "50%. Asserts the NEGATIVE this script establishes (its "
                   "own header: the multiplicative combination law is wrong). "
                   "Goes RED if any atom beyond hydrogen ever lands within "
                   "50%, which would mean the header needs revisiting.",
        )

    w.add_data("results", [asdict(r) for r in results])
    # Lean SDP-uniqueness cross-reference (post-#1537 wiring).
    w.add_data("lean_uniqueness_ref", {
        "generic": "qou:QOU.BraidKnot.@nucleus_uniqueness_closed (3*A)",
        "framework_doc":
            "folio/quantum-observable-universe/lean/QOU/BraidKnot/NucleusEmptySDPUniqueness.lean",
        "note": "Certifies T_w uniqueness at the abstract empty-constraint SDP level (PR #1537 parameterised module). Workplan: docs/workplans/2026-05-31-witness-lean-uniqueness-ref-wiring.md.",
    })

    w.save()

    return results


if __name__ == "__main__":
    main()
