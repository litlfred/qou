# ⁴He binding: where the 3.3× comes from

Issue #8960, PR #8969. Measured 2026-11-21 on `main` at `2c6aaeab2`, proton pin
q₀ = 1.10997858275…, mpmath at 60 dps. AME 2020 values appear only in comparison
columns; nothing here is tuned to them.

## 1. Which number the scorecard quotes

The six-month scorecard's "⁴He binding 3.26× low" is the dashboard's production
`B_sym` / `B_qCLT_fac` column (`computations/mass_binding_dashboard.py --group low`).
Fresh run:

| iso | B_AME | B_sym | AME/B_sym | B_qCLT_fac | AME/B_qCLT | B_can⁰ = E₀·Δtr | AME/B_can⁰ |
|---|---:|---:|---:|---:|---:|---:|---:|
| ²H | 2.225 | 2.861 | 0.78 | 2.86 | 0.78 | 0.62 | 3.6 |
| ³H | 8.482 | 6.201 | 1.37 | 6.04 | 1.40 | 0.46 | 18.4 |
| ³He | 7.718 | 5.428 | 1.42 | 5.53 | 1.40 | 0.58 | 13.4 |
| ⁴He | 28.296 | 8.767 | **3.23** | 8.68 | **3.26** | 0.33 | **85.6** |
| ⁶Li | 31.99 | 14.67 | 2.18 | 14.49 | 2.21 | 0.11 | 292 |
| ⁷Li | 39.25 | 18.01 | 2.18 | 17.73 | 2.21 | 0.05 | 741 |

`B_sym` is tagged POSITED by the dashboard: the extensivity of α·ln(tr_free/tr_atom)
follows from the Markov property, but no block licenses it as an energy. The form the
corpus does license (`conj:knot-factor-frobenius-pairing`, E₀ × trace difference) is
`B_can⁰`. It is 86× low on ⁴He and gets worse as A grows.

## 2. B_sym(⁴He), term by term

`B_sym = E₀ · [(Z−1) L_pp + L_pn + (N−1) L_nn]`: a chain over A − 1 = 3 interfaces.

| piece | value | source | status |
|---|---:|---|---|
| E₀ (tower-summed) | 4.22748 MeV | m_e/(q(q−1)) / (1 − ħ_q²) | owner ruling 2026-11-20; the series itself is open (bean `qou-y3bm`) |
| of which the tower factor | +0.086 MeV on ⁴He | 1/(1 − ħ_q²) = 1.0099 | asserted |
| L_pp = −ln z − ½ ln(1−h) | 0.607166 | σ interface, z = q³/(q²+1) | z Lean-forced (convention D); writhe term Lean-proved |
| L_pn | 0.676741 | colour-weighted interface d = −h(½ − δ/4) (the n–p cell) | colour weighting relaxed to a conjecture 2026-11-21 |
| L_nn | 0.789995 | σ⁻¹ interface | as L_pp |
| writhe normalisation | 0 for ⁴He | cancels on N = Z | Lean-proved (`WritheNormalisation.lean`) |
| chain vs exact p(3A) trace | 1.8 × 10⁻⁴⁹ MeV | dashboard Table 7 | numerics clean |
| **B_sym** | **8.767 MeV** | | |
| E_C (Coulomb) | 0.77 MeV | reported beside B, not subtracted | DERIVED* (Witten-κ sorry) |

Six-term terms 2–6, Term 4, the SDP cross-channel term and every three- or four-body
term are absent from `B_sym`.

## 3. Where the 19.53 MeV gap sits

| share | MeV | kind | what |
|---:|---:|---|---|
| ≈ 44 % | 8.58 | missing structure | **Bond count.** The atom word bonds only neighbouring nucleons, 3 bonds for ⁴He, which has C(4,2) = 6 pairs. The same L's over all pairs give 17.35 MeV. Section 6 builds the all-pairs word instead of just counting. |
| ≈ 56 % | 10.95 | missing physics | **Many-body / closed shell.** With all pairs counted, A = 3 lands at AME/B 0.93–0.94 and ²H at 0.78, but ⁴He stays 1.63× low. AME binding per pair is 2.22, 2.83, 2.57, 4.72 MeV for ²H, ³H, ³He, ⁴He; no pairwise form produces the ⁴He jump. |
| ≤ 5 % | ≲ 1 | asserted inputs | log form read as an energy; tower-summed E₀ (+0.086); n–p colour weight (−0.092 MeV per pn bond against the pp/nn mean); Coulomb not separated (would widen the gap by 0.77). |
| ≈ 0 | < 10⁻⁴⁸ | numerics | mpf end to end; the closed-form chain equals the exact trace. |

So the ⁴He error is structural. It is neither numerical nor in any single input.

**Why the chain.** `QOU/Mass/StrandLayoutForcesChain.lean` proves that with nucleon k on
strands 3k, 3k+1, 3k+2, one generator joins two nucleons only when they are neighbours.
The chain is therefore a consequence of the strand layout and the nucleon ordering, which
that file calls "the same unlicensed choice". It was not derived from the physics.

## 4. Growth with A

AME/B_sym: 0.78 (²H) → 1.37–1.42 (A = 3) → 3.23 (⁴He) → 2.18 (⁶Li, ⁷Li).
Two effects stack. The chain undercounts pairs by C(A,2)/(A−1) = A/2, and ⁴He has a
closed-shell jump on top. ⁶Li and ⁷Li fall back to 2.18, so ⁴He is a spike, not a smooth
trend. ²H over-binds by 28 %, so the per-bond scale is already too large at A = 2.

## 5. The other ⁴He routes

| route | ⁴He B | AME/B | what dominates | defects found |
|---|---:|---:|---|---|
| canonical trace `B_can⁰` (dashboard) | 0.33 | 85.6 | E₀(tr_free − tr_atom) | falls with A |
| `binding_canonical.py` witness (2026-09-06) | 0.876 | 32.3 | same idea | stale witness |
| six-term sweep `assemble_per_derivation_weights` | 22.11 | 1.28 | T2+T3 brane tower, 22.02 | **T1 was identically 0** (`canonical_t1(label)` ignored `include_inter`), and ⁴He's T1 was a stale literal (0.0553 against the live 0.011237). Fixed in this PR: ⁴He 22.131 → 22.106 MeV. T4 is 0 (as #8950 found). The scale α_Bor = m_e·8G is a hard-coded float, and 8G is the magic-A census scale the scorecard grades F. ²H over-binds 2.0× (4.58); ³He (13.13) > ³H (10.61) is the wrong mirror order. |
| `unified_low_isotope_predictor.py` | 23.74 | 1.19 | T5 = Bethe–Weizsäcker, 22.55 | T5 imports an empirical SEMF (a fit under the 2026-09-05 rule); T4 is added once (+1.15, the #8950 inconsistency); its k ≥ 3 tail gives ²H and ³H at −1.6 × 10⁵ and −2.9 × 10⁵ MeV; it uses a different tr_M (p 0.0126, n −0.089). |
| `mass_formula_6term.py` | — | — | — | does not compute ⁴He |
| `hadron_knot_table` (SDP, #8930) | not run | — | — | #8930 reports a solver-limited SDP part of 16.2 MeV inside a deuteron B of 0.54 MeV, so this route's B is set by float64 solver tolerance |

The two routes that land near ⁴He (1.2–1.3×) do so through a selected scale (8G) or an
imported SEMF. Under the no-fit rule they rank below `B_sym`.

## 6. Every pair bonded, by formation route

Owner, 2026-11-21: *"Not all γγ production should be on same strands. Look at how He
formed."*

`QOU/Mass/TransportedPairBond.lean` (sorry-free, no imports) gives the word that reaches a
non-neighbour: `T_ij = σ_{3i+2} ⋯ σ_{3j−2}` carries nucleon i's last strand to position
3j − 1 and fixes 3j, so the pair letter on generator 3j − 1, conjugated by T_ij, joins
nucleons i and j. The probe
`computations/probes/he4_all_pairs_formation/` (pre-registered in commit `d19e01e54`
before computing) bonds every pair, in the order a formation route makes them, with an
over and an under transport. Every row is reported.

**These rows use the superseded single-crossing bond letters** (owner, 2026-11-21: *"Are you
using γγ production for this? P-n-p-n seems chosen, not derived"*). They measure the
bond-count effect only. The nucleon order (p p n n, the production layout) and the four
formation routes were chosen, not derived. On the γγ-selected bond G³ = (σ₂σ₃⁻¹)³ every pair
has μ > 1 (`gamma-gamma-bond-is-pair-independent.witness.json`), so the γγ chain binds ⁴He by
about −10 keV. Owner card choice 2026-11-21: derive the order before any γγ compute.

| atom | word | transport | tr_atom | B_log (MeV) | B_diff (MeV) | AME/B_log (comparison) |
|---|---|---|---:|---:|---:|---:|
| ³H | production chain | – | 0.029144042361 | 6.697 | 0.477 | 1.27 |
| ³H | all pairs | over | 0.0161015656975 | 9.205 | 0.533 | 0.92 |
| ³H | all pairs | under | 0.0188879450875 | 8.530 | 0.521 | 0.99 |
| ³He | production chain | – | 0.0585962536544 | 4.932 | 0.548 | 1.56 |
| ³He | all pairs | over | 0.0362372801496 | 6.964 | 0.642 | 1.11 |
| ³He | all pairs | under | 0.0377264312414 | 6.794 | 0.636 | 1.14 |
| ⁴He | production chain | – | 0.0112374176598 | 8.768 | 0.330 | 3.23 |
| ⁴He | D+D pairing a | over | 0.00756676106134 | 10.440 | 0.346 | 2.71 |
| ⁴He | D+D pairing a | under | 0.00471988229408 | 12.435 | 0.358 | 2.28 |
| ⁴He | D+D pairing b | over | 0.00756676106134 | 10.440 | 0.346 | 2.71 |
| ⁴He | D+D pairing b | under | 0.00471988229408 | 12.435 | 0.358 | 2.28 |
| ⁴He | ³H + p | over | 0.00442365720127 | 12.709 | 0.359 | 2.23 |
| ⁴He | ³H + p | under | 0.0075038799308 | 10.475 | 0.346 | 2.70 |
| ⁴He | ³He + n | over | 0.00756676106134 | 10.440 | 0.346 | 2.71 |
| ⁴He | ³He + n | under | 0.00471988229408 | 12.435 | 0.358 | 2.28 |

Controls: each atom's production word reproduces `tr_m_atom_zn` exactly; on A = 3 the
commuted arrangement equals the pre-registered appended word to ≤ 1e−62.

Observations (measured, not proved):
- Three of the four ⁴He routes give the **same** trace to all printed digits for each
  transport (D+D a, D+D b, ³He + n). Only ³H + p differs, and its over/under pair is close to,
  but not equal to, the others' under/over pair. This fits the reading that block order
  enters only through conjugation (`tr(PWP⁻¹) = tr(W)`) and the over/under path of the
  transported bonds; that reading is not yet proved.
- With all six pairs bonded, ⁴He stays 2.2–2.7× low, against 0.92–1.14 for A = 3. The
  closed-shell excess of §3 survives the bond count.
- B_diff (the licensed E₀·Δtr form) barely moves: 0.33 → 0.35 MeV.

## 7. Diagnostic: adding the GPMT ≥3-row cumulant

The only Lean-backed many-body quantity on main is the GPMT ≥3-row cumulant
(`H4GPMTModifiedDimensionCumulants`). Dashboard Table 9 now shows it beside `B_sym` as a
labelled diagnostic, `B_sym + E₀·B_ext(H4)`. It is not production: no block licenses
adding it to B.

| iso | B_sym | E₀·B_ext | sum | AME/sum |
|---|---:|---:|---:|---:|
| ²H | 2.861 | 0 | 2.861 | 0.78 |
| ³H | 6.201 | 0.691 | 6.891 | 1.23 |
| ³He | 5.428 | 0.691 | 6.118 | 1.26 |
| ⁴He | 8.767 | 5.169 | 13.937 | 2.03 |

## Reproduce

```
python3 -u computations/mass_binding_dashboard.py --group low
python3 -u computations/probes/he4_all_pairs_formation/he4_all_pairs_formation_probe.py
```
Six-term per-term values: `assemble_per_derivation_weights(Z, N)` in
`computations/sweeps/paper_six_term_isotope_sweep.py`.
