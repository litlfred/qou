# Review: Horsley et al., "Isospin splittings of meson and baryon masses from three-flavor lattice QCD + QED"

arXiv:1508.06401v2 (QCDSF-UKQCD). Already held in the repo: `library/arxiv-1508.06401v2/`, bib key `horsley-et-al-2016-qcd-qed`.
(The coordinator's note named it as Fermilab/MILC/TUMQCD 2018; that is a different paper.)
All scripts and outputs: `computations/flavour_strange_strand/`. Lean: `QOU/BraidsAndKnots/StrangeStrandOctet.lean`. Issue #8867.
Reviewed 2026-11-21. Physical guidance only: none of these numbers belong in a formal proof.

## Verdict

Relevant as a benchmark, but it does not support "a missing strange quark is why n–p is off".
At first order in quark masses and O(e²), the strange quark drops out of M_n − M_p in the paper's own expansion,
and in QOU an s strand provably cannot change the direction result.

## Key numbers (Table 1, MeV, infinite volume, Dashen scheme)

| splitting | total QCD+QED | QED part | QCD part | experiment |
|---|---|---|---|---|
| M_n − M_p | 1.35(18)(8) | −2.20(28)(10) | +3.51(31) | 1.29 |
| M_Σ− − M_Σ+ | 7.60(73)(8) | −0.63(8)(6) | 9.07(47) | 8.08 |
| M_Ξ− − M_Ξ0 | 6.10(55)(45) | 1.26(16)(13) | 5.58(31) | 6.85 |
| M_π+ − M_π0 (QED) | | 4.60(20) | | 4.59 |
| M_K0 − M_K+ | 4.09(10) | −1.66(6) | | 3.93 |

- Signs: QCD part (m_d > m_u) makes the neutron heavier; QED part makes the proton heavier.
- With the alternative Σ-constraint scheme the QED part is −1.71(28)(10). Compare BMW 2015: +2.52 / −1.00; Cottingham (WLCM 2012): −1.30(50).
- **The QCD/QED split is scheme-dependent** (the paper says so). Only the total is physical.
- m_u/m_d = 0.52(2), m_s/m_d = 19.7(9); ε = 0.50(6) (MS-bar).
- Setup: 2+1 dynamical flavours, s is dynamical, expansion around the SU(3)-symmetric point at fixed m̄ = (m_u+m_d+m_s)/3. Single lattice spacing (a ≈ 0.068 fm).

## Where the strange quark enters (paper's Eq. 14)

Octet baryon aab:
M² = M0² + α1(2δμ_a + δμ_b) + α2(δμ_a − δμ_b) + β1(2e_a² + e_b²) + β2(e_a − e_b)² + β3(e_a² − e_b²).

- Nucleon strong part: M_p² − M_n² = (α1 + 2α2)(δμ_u − δμ_d). No δm_s.
- Σ: (2α1 + α2)(δμ_u − δμ_d); Ξ: (α1 − α2)(δμ_u − δμ_d). These sum to the nucleon coefficient (Coleman–Glashow).
- e_s appears only in the β0 sea term, common to all baryons, which cancels in n − p.
- So s affects n − p only through the sea, i.e. through the values of α1, α2, β_i — a common renormalisation, not a new isospin-odd term.

## QOU check (computed this session)

The n–p machinery (`NucleonWeightSpaceTwoTerm.lean` etc.) lives on (C²)^⊗3: u and d only. The dictionary lists s as "σ_j⁻¹ (2nd gen), conditional on N = 3"; it is not used in any n–p computation.

Extending to (C³)^⊗3 with the sl₃ Jimbo braiding (sympy, `computations/flavour_strange_strand/octet_isospin_probe.py`):
- σ₁, σ₂ restricted to the (2,1,0) and (1,2,0) weight spaces are **identical** to the sl₂ matrices on (2,1), (1,2).
- tr(V³) on p and n: identical in both cases, −q⁶ + 3q⁴ − 3q² + 5 − 3q⁻² + 3q⁻⁴ − q⁻⁶.
- Quantum-trace weight ratio K(n)/K(p): q⁻² for sl₂ (K = diag(q, q⁻¹)) and q⁻² for sl₃ (K = diag(q², 1, q⁻²)).

So ε_n = q⁻² ε_p survives adding an s strand. A strange strand cannot flip the direction. This matches the lattice
statement that s cancels from n − p at leading order.

Where an s strand does give new, testable content:
- Σ and Ξ splittings. Weight spaces (2,0,1)/(0,2,1) and (1,0,2)/(0,1,2) carry the same braid matrices; the K ratios are
  q⁻⁴ (Σ) and q⁻² (Ξ). So the QOU Cartan term predicts Σ : N : Ξ ≈ 2 : 1 : 1 at first order in log q.
  Lattice QCD parts: 9.07 : 3.51 : 5.58 ≈ 2.6 : 1 : 1.6.
- Sea strand: a B₄ word with a traced 4th (s) strand. By the Markov property this should rescale p and n by the same factor
  (size, not direction). Worth checking whether that common factor is what is missing from the −35%.

## Housekeeping

`docs/audits/2026-11-18-two-term-qed-downstream-and-211ppb-audit.md` line 116 cites this paper as JHEP 04, 093 (2016).
That reference looks like it belongs to the companion meson paper; the bib entry correctly says no journal ref was added. Needs checking.

## Probe: Σ and Ξ splittings with an s strand (2026-11-21, owner chose this option)

Script `octet_isospin_probe.py`, output `octet_isospin_probe.out` (exact sympy over Q(q); q₀ only in the display block).

- Exact in q: every octet weight space carries literally the sl₂ nucleon matrices: p, Σ⁺, Σ⁻ the proton-type ones (odd flavour has the larger index), n, Ξ⁰, Ξ⁻ the neutron-type ones. These two types are intertwined by P(q), so tr V³ (indeed tr of any braid word) is the same on every member. So each splitting comes only from the Cartan weight and the charge operators.
- Cartan term, isospin Cartan q^{H₁} = diag(q, q⁻¹, 1) (the direct extension of QOU's T³; s is isospin-blind):
  Σ/N = q + q⁻¹ = [2]_q, Ξ/N = 1. At q₀: 2.011 : 1 : 1.
- Cartan term, full sl₃ quantum-trace weight q^{2ρ} = diag(q², 1, q⁻²): Σ/N = (q²+1)/q⁴, Ξ/N = q⁻⁶. At q₀: 1.470 : 1 : 0.535.
- Coleman–Glashow defect of the isospin-Cartan term: Σ − N − Ξ = −(q−1)³(q+1)/q², third order in (q−1).
- Charge operators (low minus high member): ΔQ_self = −1/3, −2/3, −1/3 and ΔQ_pair = −1/3, +1/3, +2/3 for N, Σ, Ξ.
- Signs: same direction problem in all three pairs (the I₃ = −½ / −1 member comes out lighter).

Comparison (physics enters only here). Lattice QCD parts 9.07 : 3.51 : 5.58 = 2.58 : 1 : 1.59.
In the first-order form (2α₁+α₂) : (α₁+2α₂) : (α₁−α₂), the isospin-Cartan term is exactly the case α₂ = 0
(Ξ = N). The lattice needs α₂/α₁ ≈ −0.14. So the Cartan term cannot supply α₂ at any order. α₂ is the term that
depends on whether the odd quark is the u/d or the s. It has to come from an operator that sees which strand
position carries which flavour, for example position-resolved Q₁₂/Q₂₃-type operators, or a word that is not
symmetric in the strands.

## Probe: sea strand (traced 4th strand), 2026-11-21

Script `sea_strand_probe.py`, output `sea_strand_probe.out`. Jimbo sl₃ braiding on (C³)^⊗4. Valence word V³ on strands 1–3,
coupled to strand 4 by its monodromy L₄ = σ₃σ₂σ₁²σ₂σ₃. Strand 4 is projected onto one flavour, then given a bare trace.
Words tested: V³ (uncoupled), V³·L₄, L₄·V³·L₄. Exact in Q(q).

| sea strand | tr_p − tr_n (V³·L₄) |
|---|---|
| u | (q² − 1)·tr V³ |
| d | −q²(q² − 1)·tr V³ |
| **s** | **0, exactly** |
| u+d+s, bare trace | (q² − 1)(1 − q²)·tr V³ |
| u+d+s, quantum trace (weights q², 1, q⁻²) | **0, exactly** |

(Here tr V³ = tr of V³ on the nucleon weight space; the polynomial factor printed by the script is −q⁶·tr V³. L₄·V³·L₄ has the same pattern with a different polynomial.)

- **A strange sea strand gives zero p/n splitting, exactly, for every word tested.** Argument (sketch, not yet Lean):
  the projector onto e₃ on strand 4 commutes with the U_q(sl₂) acting on span(e₁, e₂). Every braid word is invariant,
  so the s-projected partial trace is a U_q(sl₂)_{ud}-invariant operator on the valence strands. The p and n weight
  spaces are conjugate under the sl₂ Weyl reflection, so the trace is equal on them, to all orders in q.
- u and d sea strands do split p from n, by ∓(q² − 1)·tr V³ (first order in q − 1). Their quantum-trace combination cancels exactly.
- So inside the Jimbo model, the strange quark cannot enter n − p at any order, as a valence strand or as a sea strand.
  If the lattice's higher-order s effects are real, QOU would need an operator on the s strand that is not U_q(sl₂)_{ud}-invariant.
  Nothing in the current corpus supplies one.

## Probe: sl₃ reflection-equation wall (2026-11-21; run on the recommended option while the card was open)

Scripts `sl3_reflection_probe.py`, `sl3_wall_octet_probe.py` (exact). Constant reflection equation Ř K₁ Ř K₁ = K₁ Ř K₁ Ř on C³.
- Diagonal solutions: diag(a,a,0), diag(a,0,0), scalar. **The reflection equation forces the s entry to 0 whenever u and d
  are kept equal.** There is no free u/s ratio. The wall that respects isospin is the projector onto span(u,d) on the boundary strand.
- The only non-diagonal family that contains H5's sl₂ wall [[a,b],[c,0]] on (u,d) is [[a,b,0],[c,0,0],[0,0,0]]: again the s row and column vanish.
  (A second family [[(k₄²−k₂k₆)/k₄,0,k₂],[0,k₄,0],[k₆,0,0]] is the sl₂ wall placed on (u,s) with d spectating.)
  So the reflection equation itself treats s differently from u and d. This is derived, not chosen.
- Scored as the Cartan-weighted wall trace K_w·tr(K₁V³) with K = diag(1,1,0): Σ:N:Ξ = 1.335 : 1 : 0.337 at q₀
  (lattice QCD parts 2.58 : 1 : 1.59). The bare wall traces are still equal within each pair. Scope (a): this wall,
  in this functional, moves the ratios the wrong way. It does not exclude the wall from a fuller assembly (e.g. with H5's off-diagonal part).

## Sea strand with the valence Cartan weight (2026-11-21, owner rule: keep every derivable correction)

Script `sea_strand_cartan_probe.py` (exact). Valence V³ coupled to a traced 4th strand by L₄, with the isospin Cartan weight on the valence strands.
Normalisation-free relative splitting δ = (F_n − F_p)/(F_n + F_p):

| sea strand trace | δ at q₀ | δ / δ(no sea) |
|---|---|---|
| no sea strand | −(q²−1)/(q²+1) = −0.10396 | 1 |
| quantum trace, weights q^{2ρ} = (q², 1, q⁻²) | −0.10396 | **1, exactly** (the sea's p/n difference vanishes, see above) |
| isospin-quantum trace, weights (q, q⁻¹, 1) | −0.10396 | **1, exactly** |
| bare trace, u+d+s | −0.09701 | 0.933 |

- Under any quantum (Markov-compatible) sea trace the sea-strand correction to the relative n–p splitting is **exactly 0**.
  That is a derived value, not a neglected term. The s contribution is 0 under every trace.
- Only a bare (non-quantum) sea trace gives a correction: −6.7 % of the splitting. Which trace a closed sea loop takes is not chosen here.
  Under convention D the Markov trace is the quantum one, which gives 0.

## Lean (formalize-first), 2026-11-21

`StrangeStrandOctet.lean` (copy here; in the local clone at `folio/quantum-observable-universe/lean/QOU/BraidsAndKnots/`, uncommitted).
`lean -DautoImplicit=false -s 65536`: exit 0, 0 warnings, ~6 s. `#print axioms`: propext, Classical.choice, Quot.sound only. No sorry.
- `jimbo n q`: level-n Jimbo braiding on Cⁿ⊗Cⁿ (generic field, generic n).
- `jimbo_entry_ne_zero`: Ř only maps eᵢ⊗eⱼ into span(eᵢ⊗eⱼ, eⱼ⊗eᵢ).
- `jimbo_submatrix_orderEmbedding`: restricted to any two flavours a<b, Ř is the sl₂ braiding; `us_sector_eq_ud_sector`, `ds_sector_eq_ud_sector`.
- `reflection_diag_iff`: diag(a,b,c) solves Ř K₁ Ř K₁ = K₁ Ř K₁ Ř ⇔ b(a−b) = c(a−c) = c(b−c) = 0 (q ≠ 0, q² ≠ 1).
- `strange_entry_forced`: a = b, c ≠ a ⇒ c = 0. `ud_projector_wall_solves`: diag(a,a,0) solves it.

Not yet in Lean (exact sympy only): the three-strand octet weight-space restriction, and the 81-dimensional sea-strand partial traces.
