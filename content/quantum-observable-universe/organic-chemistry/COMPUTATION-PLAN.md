# Organic Chemistry — Computation Plan

The chapter currently makes **eight quantitative claims** with zero verified
computational backing.  This document catalogues the computations,
algorithms, and propositions/lemmas needed once the computation pipeline
is reliable, so that work can resume without re-deriving the structure.

**Critical-path order:** C1 → (C3, C5) → C6 → C7/C8/C9.  Without C1 (the
molecular crossing-energy quantum), every numerical prediction downstream
is multiplied by an unknown constant and the chapter cannot be falsified.

---

## Section 1 — Molecular crossing-energy quantum (§A)

Everything depends on a trusted value of $|q + q^{-1}|_{\mathrm{mol}}$
(currently quoted as the hand-wavy "1–2 eV").  This is the single biggest
open problem flagged in `chain-ring-comparison.md`.

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C1** | `crossing-energy-mol.py` | (i) $\mathrm{Vol}(4_1) \to q$ via SnapPy (already in `knot-volumes.py`); (ii) symbolic eval of $\lvert q + q^{-1}\rvert$; (iii) $\alpha$ and $m_e/m_p$ from `topological-mass-formula`; (iv) propagate uncertainties | **`prop:molecular-crossing-quantum`** — "$\lvert q + q^{-1}\rvert_{\mathrm{mol}} = (\alpha^2 m_e/m_p)\,\lvert q + q^{-1}\rvert_{\mathrm{nuc}}$, with explicit error bounds from the trefoil-volume computation."  Currently asserted in prose only. |
| **C2** | `crossing-energy-mol-direct.py` | SnapPy: $\mathrm{Vol}(3_1)$ at electronic scale; ratio of hyperbolic volumes; cross-check against C1 | **`lem:trefoil-volume-electronic-scale`** — independent route to the same quantum.  Two independent computations agreeing within tolerance is a strong falsifiability test. |

---

## Section 2 — Topological invariants of $T(2,N)$ (§B)

Pure knot-theory computations with closed-form expected values — the
easiest wins.

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C3** | `alexander-T2N.py` | Sympy: closed form $(q^m - q^{-m})/(q - q^{-1})$ for even $N = 2m$; cross-check via Burau matrix of $(\sigma_1 \cdots \sigma_{N-1})^2$ in $B_N$ | **`lem:alexander-T2N-closed-form`** — currently inline in `threading-link.md`; promote to a lemma with `\lean{}` reference and Mathlib-backed Lean proof. |
| **C4** | `T2N-component-count.py` | Standard Gauss-code / link-component algorithm; verify $\gcd(2,N)$ component count, sign of crossings, writhe, signature | **`lem:T2N-components`** — currently a table in `threading-link.md`. |
| **C5** | `alexander-weight-ratio.py` | Symbolic limit: $\Delta_{T(2,2m)}(q)/N \to 1/2$ as $\lvert q\rvert \to 1$ for all even $N$ | **`prop:threading-half-weight`** — the central topological claim of the chapter; currently asserted as a consequence rather than proved. |

---

## Section 3 — Quantitative ring-closure & resonance predictions (§C)

The chapter's headline numerical predictions.  The current
`benzene_resonance.py` computes a different theoretical object (Hecke-level
cyclic-braid energy at $k = 3, 5, 7$) — see "Note" below.

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C6** | `ring-closure-barrier.py` | $\Delta E \propto [(N-1) - \Delta_{T(2,N)}(q)] \cdot \lvert q + q^{-1}\rvert_{\mathrm{mol}}$ for $N = 4, 6, 8, 10, 12$; uses C1 + C3; outputs in eV and kJ/mol; compares to CCSD(T) and Bergman-cyclisation literature | **`prop:ring-closure-barrier-quantitative`** — quantitative companion to the existing qualitative `prop:ring-closure-barrier`. |
| **C7** | `benzene-resonance-alexander.py` | Framework-consistent benzene resonance: $\Delta E_{\mathrm{res}} = [N - \Delta_{T(2,N)}(q)] \cdot \lvert q + q^{-1}\rvert_{\mathrm{mol}}$ at $N = 6$; predicts vs. 150 kJ/mol experimental | **`cor:benzene-resonance-from-threading`** — corollary of `prop:ring-closure-barrier-quantitative`. |
| **C8** | `even-N-ring-spectrum.py` | C6 swept over $N \in \{4, 6, 8, 10, 12, 14\}$ with literature lookup; predicted vs. experimental, percentage match | **`prop:even-N-barrier-spectrum`** — generalises beyond benzene; lifts the table on lines 98–103 of `chain-ring-comparison.md` to a numbered proposition. |
| **C9** | `chain-vs-ring-energy-N6.py` | Symbolic + numerical evaluation of "ring weight $\approx 3$ < chain weight $= 5$" at $N = 6$ | **`lem:c6-energy-comparison`** — promotes table on lines 13–17 of `chain-ring-energy.md`. |

---

## Section 4 — Odd-$N$ rings and Hückel (§D)

Currently deferred in prose; the framework should at least state what the
computations would be.

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C10** | `torus-knot-T2-odd.py` | Closed form $\Delta_{T(2,2m+1)}(q) = (q^{2m+1} + q^{-(2m+1)})/(q + q^{-1})$ — note divide by $q + q^{-1}$ not $q - q^{-1}$ | **`def:torus-knot-T2-odd-alexander`** + **`prop:odd-N-ring-barrier`** — new definition + proposition. |
| **C11** | `huckel-bridge.py` | Try: signature of Goeritz matrix; $J_{T(2,N)}(q)$ at roots of unity; Conway polynomial discriminant — find the invariant of $T(2,N)$ encoding the $4n+2$ rule | **`conj:huckel-from-T2N-invariant`** — promotes open problem #2 to a labelled conjecture. |

---

## Section 5 — Taxonomy verification (§E)

`organic-chain-taxonomy.md` makes claims about hydrogen-capacity formulae
and aromaticity that are currently unverified.

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C12** | `hydrogen-capacity.py` | Combinatorial: count free sites $= 4N - 2\sum k_i$ (interior) plus endpoint correction for chains, $-0$ for rings; verify $\mathrm{C}_N\mathrm{H}_{2N+2-2d}$ (chain) and $\mathrm{C}_N\mathrm{H}_{2N-2d}$ (ring) | **`prop:hydrogen-capacity`** — promotes table to a proposition with a Lean proof from the linking-site axioms in `def:covalent-bond-types`. |
| **C13** | `bond-order-energy.py` | Two-parameter fit ($\mathbf{E}_{\mathrm{cross}}$, $\Delta E_{\mathrm{inter}}$) over thermochemical data: C–C 346, C=C 614, C≡C 839 kJ/mol; report residuals | **`prop:bond-order-energy-formula`** — splits the falsifiable energy formula out of `def:covalent-bond-types`. |

---

## Section 6 — Heteroatom extension (§F)

| ID | Script | Algorithm | Backing prop / lemma |
|----|--------|-----------|----------------------|
| **C14** | `pyridine-furan-alexander.py` | Generalised Alexander polynomial of a coloured/labelled link where one strand carries different linking-site multiplicity (N for pyridine, O for furan) | **`conj:heteroaromatic-alexander`** — promotes open problem #3 to a labelled conjecture. |

---

## Appendix — Shared infrastructure (§G)

| Need | Status | Where it goes |
|------|--------|---------------|
| `q_parameter.py` exporting $q_0$, $q_0^{-1}$, $h = q_0 - q_0^{-1}$ | exists | reuse |
| `alexander.py` with closed-form $\Delta_{T(p,q)}$ | new | `computations/lib/` |
| `witness_base.py` enforcing `engine`, `engineVersion`, `commitSha`, `assertions[]` | exists | reuse |
| Unit-conversion module (eV ↔ kJ/mol ↔ kcal/mol ↔ Hartree) with explicit CODATA references | new | `computations/lib/` |
| `experimental-organic.json` with citations (CCSD(T) barriers, hydrogenation calorimetry, bond enthalpies) so witnesses don't hard-code numbers | new | `computations/data/` |

---

## Note on the existing `benzene_resonance.py`

The current script computes a **Hecke-level cyclic-braid energy** (open
chain vs. closed chain at $k = 3, 5, 7$ in $H_N(q)$), reporting 2.13 eV
vs. experimental 1.5 eV.  This is a different theoretical object from the
chapter's prediction, which is built from
$\Delta_{T(2,6)}(q) = q^2 + 1 + q^{-2}$ times $\lvert q + q^{-1}\rvert_{\mathrm{mol}}$.

Both derivations deserve to live, but they should be wired to **different**
propositions so the chapter doesn't conflate two distinct routes to the
same observable.  The proof block currently in
`benzene-resonance-verification` should be retitled and linked to a new
`prop:hecke-cyclic-braid-energy`, or removed pending C7.
